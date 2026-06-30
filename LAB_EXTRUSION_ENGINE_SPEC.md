# Lab Extrusion Engine Spec

**Status: not started — this is the spec. Prototype comes next.**

---

## 1. The Problem

Every module that uses `renderHeightfield(g, heights, G, pal, opts)` produces
the same visual: a straight oblique box-push. The extrusion method is hardcoded
as three `g.quad()` calls — two shaded side faces and a lit cap — and there is
no way to swap in a different shape without editing the renderer directly.

This means terrain_slice, wave_lattice, contour_field, echo_contours and ~20
other engine-generated modules all look structurally identical under extrusion.
A pluggable `extrudeMode` system would give each module a distinct 3D character
from a single slider, at zero per-module implementation cost once the interface
is rolled out.

---

## 2. Architectural Decision: Written Spec, Not a Shared JS File

The lab's core design constraint is **self-contained HTML files**. Every module
is a single `.html` that works in isolation — no external JS dependencies, no
shared runtime, no import maps. This is not accidental: it enables direct iframe
embedding, standalone save/export, and prevents any one module from breaking
others.

A shared `extrude-modes.js` file would violate this constraint. If it drifts,
breaks, or needs a path change, every module that imports it breaks simultaneously.

**The approach instead:**

Same discipline used for the postMessage bridge rollout:

1. Write a strict interface spec (this document)
2. Prototype it in one module (`terrain_slice`) — validate the draw contracts,
   test the mode-specific params, confirm the edge cases
3. Once the prototype is solid, propagate via batched Codex passes across all
   `renderHeightfield` modules — the same mechanical batch operation that wired
   the bridge across 52 modules
4. Each module gets the full mode array inlined — no external dependency, full
   self-containment preserved

The spec is the coordination mechanism. Codex is the propagation mechanism.

---

## 3. What the Renderer Actually Is

**Important constraint:** The entire rendering stack is **2D Canvas painting
with oblique projection math**. There is no WebGL, no vertex buffer, no normals,
no depth buffer.

Evidence: every graphics buffer is created as `createGraphics(W, H)` — no
`WEBGL` flag. All draw calls are `g.quad()`, `g.fill()`, `g.triangle()`,
`g.ellipse()` from the p5.js Canvas2D renderer.

The "3D" effect is achieved by:
1. Computing a per-row foreshortening transform (`planeS`, `planeY`) to simulate
   perspective — pure 2D arithmetic
2. Computing an iso offset vector `[ox, oy]` ≈ `[z*0.5, -z]` (cabinet projection)
3. Painting faces back-to-front (painter's algorithm) with hand-multiplied
   shading values — no light model, no normals

**Implication for extrudeMode:** all modes are 2D drawing routines. There is no
mesh generation, no real bevels, no actual shells. Bevel, shell, and recursive
modes are visual tricks achieved by drawing additional polygons or overdrawing
with background color. The 3D reading is an illusion that holds under standard
viewing conditions.

---

## 4. The `extrudeMode` Interface

### 4a. Call site inside `renderHeightfield`

Two changes to the existing function:

**Before the cell loop** — select mode once:
```javascript
const _mode = EXTRUDE_MODES[
  Math.min(EXTRUDE_MODES.length - 1, Math.round(P.extrudeMode ?? 0))
];
```

**Inside the cell loop** — replace the three hardcoded `g.quad()` calls with:
```javascript
_mode.draw(g, {
  A, B, C, D,          // base quad corners (staged, canvas px)
  tA, tB, tC, tD,      // top quad corners = base + iso offset
  ox, oy,              // iso offset vector
  z,                   // extrusion depth in canvas pixels
  cW, cH,              // cell pixel dimensions
  h,                   // raw height from heightField (0–1)
  hEff,                // height after hvar weighting (0–1)
  neg,                 // bool — inverted extrude direction
}, {
  tc,                  // [r,g,b] base tint, height-mapped pal[1]→pal[2]
  lF,                  // light factor — side face darkening multiplier
  shn,                 // sheen/metallic — specular highlight strength
  pal,                 // [[r,g,b]×3] full palette (pal[0]=bg, used by shell)
});
```

The mode owns **all** drawing for the cell. `renderHeightfield` draws nothing
inside the loop itself. The existing `P.caps` dome/sphere logic lives outside
the mode (it paints on top of the cap after the mode call) and is unchanged.

### 4b. Corner naming convention

Base quad corners follow render order (back-to-front in the oblique view):

```
A (TL) ── B (TR)
│               │
D (BL) ── C (BR)
```

Top quad corners are the base corners shifted by `[ox, oy]`:
`tA = A + [ox,oy]`, `tB = B + [ox,oy]`, etc.

In positive (default) extrude direction:
- Visible right side face: `B → tB → tC → C`
- Visible bottom face: `D → C → tC → tD`
- Cap: `tA → tB → tC → tD`

In `neg` (negative/inverted) direction the visible faces swap:
- Left face: `A → tA → tD → D`
- Top face: `A → B → tB → tA`

### 4c. Mode definitions

```javascript
const EXTRUDE_MODES = [

  {
    id: "box",
    // Current default — straight oblique push. Verbatim extraction of existing logic.
    draw(g, { A, B, C, D, tA, tB, tC, tD, neg }, { tc, lF }) {
      if (neg) {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(A[0],A[1],   tA[0],tA[1], tD[0],tD[1], D[0],D[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(A[0],A[1],   B[0],B[1],   tB[0],tB[1], tA[0],tA[1]);
      } else {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(B[0],B[1],   tB[0],tB[1], tC[0],tC[1], C[0],C[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(D[0],D[1],   C[0],C[1],   tC[0],tC[1], tD[0],tD[1]);
      }
      g.fill(tc[0], tc[1], tc[2]);
      g.quad(tA[0],tA[1], tB[0],tB[1], tC[0],tC[1], tD[0],tD[1]);
    }
  },

  {
    id: "taper",
    // Top quad shrinks toward centroid — columns narrow toward the peak.
    // P.taperAmt (0–1): 0 = identical to box, 1 = spike to a single point.
    draw(g, { A, B, C, D, tA, tB, tC, tD, neg }, { tc, lF, shn }) {
      const amt = Math.min(0.98, P.taperAmt ?? 0.55);
      const cx  = (tA[0]+tB[0]+tC[0]+tD[0]) / 4;
      const cy  = (tA[1]+tB[1]+tC[1]+tD[1]) / 4;
      const T   = ([x,y]) => [cx + (x-cx)*(1-amt), cy + (y-cy)*(1-amt)];
      const pA=T(tA), pB=T(tB), pC=T(tC), pD=T(tD);
      if (neg) {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(A[0],A[1],   pA[0],pA[1], pD[0],pD[1], D[0],D[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(A[0],A[1],   B[0],B[1],   pB[0],pB[1], pA[0],pA[1]);
      } else {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(B[0],B[1],   pB[0],pB[1], pC[0],pC[1], C[0],C[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(D[0],D[1],   C[0],C[1],   pC[0],pC[1], pD[0],pD[1]);
      }
      const hi = Math.min(1.25, 1.05 + shn*0.3);
      g.fill(Math.min(255,tc[0]*hi), Math.min(255,tc[1]*hi), Math.min(255,tc[2]*hi));
      g.quad(pA[0],pA[1], pB[0],pB[1], pC[0],pC[1], pD[0],pD[1]);
    }
  },

  {
    id: "bevel",
    // Chamfered top edge — a flat angled ring between the side wall and the inset cap.
    // Adds one extra polygon layer per visible side face.
    // P.bevelW (0–0.5): ring width as fraction of min(cW, cH).
    // Note: bevel ring is a 2D quad in oblique space, not a true geometric chamfer.
    draw(g, { A, B, C, D, tA, tB, tC, tD, ox, oy, neg, cW, cH }, { tc, lF, shn }) {
      const bw  = (P.bevelW ?? 0.18) * Math.min(cW, cH);
      const bx  = bw * (ox < 0 ? -1 : 1) * 0.5;
      const by  = bw * (oy < 0 ? -1 : 1) * 0.5;
      const iA  = [tA[0]+bx, tA[1]+by], iB = [tB[0]-bx, tA[1]+by];
      const iC  = [tC[0]-bx, tC[1]-by], iD = [tD[0]+bx, tC[1]-by];
      // Side faces run to the top of the wall (tA..tD), not to the inset cap
      if (neg) {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(A[0],A[1],   tA[0],tA[1], tD[0],tD[1], D[0],D[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(A[0],A[1],   B[0],B[1],   tB[0],tB[1], tA[0],tA[1]);
      } else {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(B[0],B[1],   tB[0],tB[1], tC[0],tC[1], C[0],C[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(D[0],D[1],   C[0],C[1],   tC[0],tC[1], tD[0],tD[1]);
      }
      // Bevel ring — mid-tone between side and cap
      const bF = lF + (1-lF)*0.5;
      g.fill(tc[0]*bF, tc[1]*bF, tc[2]*bF);
      g.quad(tA[0],tA[1], tB[0],tB[1], iB[0],iB[1], iA[0],iA[1]);
      g.quad(tD[0],tD[1], tC[0],tC[1], iC[0],iC[1], iD[0],iD[1]);
      // Inset cap
      const hi = Math.min(1.2, 1.05 + shn*0.3);
      g.fill(Math.min(255,tc[0]*hi), Math.min(255,tc[1]*hi), Math.min(255,tc[2]*hi));
      g.quad(iA[0],iA[1], iB[0],iB[1], iC[0],iC[1], iD[0],iD[1]);
    }
  },

  {
    id: "shell",
    // Hollow top — full outer cap, then overdraw with pal[0] to simulate a rim wall.
    // P.shellThick (0–0.5): wall thickness as fraction of cell size.
    // Constraint: the hollow is an overdraw trick. It holds visually when zdepth ≈ 0
    // and cells are dense enough that columns don't leave gaps. Under heavy zdepth
    // staging, a neighbour's side face can repaint the punch area.
    draw(g, { A, B, C, D, tA, tB, tC, tD, neg }, { tc, lF, pal }) {
      const th = P.shellThick ?? 0.22;
      const cx  = (tA[0]+tB[0]+tC[0]+tD[0]) / 4;
      const cy  = (tA[1]+tB[1]+tC[1]+tD[1]) / 4;
      const I   = ([x,y]) => [cx + (x-cx)*(1-th*2), cy + (y-cy)*(1-th*2)];
      const iA=I(tA), iB=I(tB), iC=I(tC), iD=I(tD);
      if (neg) {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(A[0],A[1],   tA[0],tA[1], tD[0],tD[1], D[0],D[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(A[0],A[1],   B[0],B[1],   tB[0],tB[1], tA[0],tA[1]);
      } else {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(B[0],B[1],   tB[0],tB[1], tC[0],tC[1], C[0],C[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(D[0],D[1],   C[0],C[1],   tC[0],tC[1], tD[0],tD[1]);
      }
      // Outer cap
      g.fill(tc[0], tc[1], tc[2]);
      g.quad(tA[0],tA[1], tB[0],tB[1], tC[0],tC[1], tD[0],tD[1]);
      // Punch hollow with bg color
      g.fill(pal[0][0], pal[0][1], pal[0][2]);
      g.quad(iA[0],iA[1], iB[0],iB[1], iC[0],iC[1], iD[0],iD[1]);
    }
  },

  {
    id: "recursive",
    // Two stacked extrusions: outer box to height h, then a 50%-footprint inner
    // column rising further above the cap.
    // P.recBoost (0–1): how much higher the inner tower rises relative to outer z.
    // Constraint: inner tower is drawn in the same painter pass — no depth sort
    // between levels. Safe because the inner tower always sits on top of the outer
    // cap in paint order, so it never gets occluded incorrectly.
    draw(g, { A, B, C, D, tA, tB, tC, tD, ox, oy, z, neg }, { tc, lF, shn }) {
      // Outer box (identical to box mode)
      if (neg) {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(A[0],A[1],   tA[0],tA[1], tD[0],tD[1], D[0],D[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(A[0],A[1],   B[0],B[1],   tB[0],tB[1], tA[0],tA[1]);
      } else {
        g.fill(tc[0]*lF,    tc[1]*lF,    tc[2]*lF);
        g.quad(B[0],B[1],   tB[0],tB[1], tC[0],tC[1], C[0],C[1]);
        g.fill(tc[0]*lF*.7, tc[1]*lF*.7, tc[2]*lF*.7);
        g.quad(D[0],D[1],   C[0],C[1],   tC[0],tC[1], tD[0],tD[1]);
      }
      g.fill(tc[0], tc[1], tc[2]);
      g.quad(tA[0],tA[1], tB[0],tB[1], tC[0],tC[1], tD[0],tD[1]);
      // Inner tower — 50% footprint, extra height above cap
      const boost = P.recBoost ?? 0.55;
      const cx = (tA[0]+tB[0]+tC[0]+tD[0]) / 4;
      const cy = (tA[1]+tB[1]+tC[1]+tD[1]) / 4;
      const S  = ([x,y]) => [cx + (x-cx)*0.5, cy + (y-cy)*0.5];
      const sA=S(tA), sB=S(tB), sC=S(tC), sD=S(tD);
      const iox = ox*boost*0.5, ioy = oy*boost*0.5;
      const siA=[sA[0]+iox,sA[1]+ioy], siB=[sB[0]+iox,sB[1]+ioy];
      const siC=[sC[0]+iox,sC[1]+ioy], siD=[sD[0]+iox,sD[1]+ioy];
      const hi = Math.min(1.3, 1.1 + shn*0.35);
      g.fill(Math.min(255,tc[0]*hi*lF),   Math.min(255,tc[1]*hi*lF),   Math.min(255,tc[2]*hi*lF));
      g.quad(sB[0],sB[1],   siB[0],siB[1], siC[0],siC[1], sC[0],sC[1]);
      g.fill(Math.min(255,tc[0]*hi*lF*.7), Math.min(255,tc[1]*hi*lF*.7), Math.min(255,tc[2]*hi*lF*.7));
      g.quad(sD[0],sD[1],   sC[0],sC[1],   siC[0],siC[1], siD[0],siD[1]);
      g.fill(Math.min(255,tc[0]*hi), Math.min(255,tc[1]*hi), Math.min(255,tc[2]*hi));
      g.quad(siA[0],siA[1], siB[0],siB[1], siC[0],siC[1], siD[0],siD[1]);
    }
  },

];
```

### 4d. PARAMS additions

One selector in the existing `extrude` group plus four mode-specific params.
Mode-specific params are always present in the PARAMS array; the shell uses them
only when the corresponding mode is active (same pattern as `hvar`/`light` which
are ignored when `height=0`).

```javascript
{k:"extrudeMode", g:"extrude", label:"extrude mode", min:0, max:4, step:1,    v:0},
// 0=box  1=taper  2=bevel  3=shell  4=recursive

{k:"taperAmt",   g:"extrude", label:"taper",         min:0, max:0.98, step:0.01, v:0.55},
{k:"bevelW",     g:"extrude", label:"bevel width",   min:0, max:0.5,  step:0.01, v:0.18},
{k:"shellThick", g:"extrude", label:"shell thick",   min:0, max:0.5,  step:0.01, v:0.22},
{k:"recBoost",   g:"extrude", label:"rec boost",     min:0, max:1,    step:0.01, v:0.55},
```

---

## 5. Prototype Module: `terrain_slice`

**File:** `terrain_slice/noixzy_terrain_slice.html`

**Why this one:**

- `heightField(G)` is six lines of clean octave-noise math with no side effects —
  nothing to accidentally break when adding mode dispatch
- `renderHeightfield` is present verbatim, with no module-specific hacks or shims
  (unlike `contour_field` which has a legacy `P.depth` alias inside the function)
- The 2D render path (horizontal contour slices) and the 3D path (extrude) are
  cleanly separated by the `(P.height||0) > 0.01` gate — the two paths never
  interfere, so a regression in the mode dispatch will be visually obvious
- Terrain heights are spatially coherent (low-frequency noise), so all five modes
  produce readable, meaningfully different results at G=220 — taper narrows peaks,
  bevel chamfers ridges, shell hollows plateaux, recursive stacks towers on hills.
  A module with noisy fine-grained heights (e.g. `crater_field`) would make the
  mode differences harder to see at normal resolution

**Why not the alternatives:**

- `wave_lattice` — has a two-stage render (specular texture precomputed in setup,
  then composited in draw) that adds surface area for the prototype to break
- `contour_field` — has the `P.depth` alias shim inside `renderHeightfield` itself;
  patching a module with a bespoke shim in the shared function is a bad prototype
- `grid_extrude` — gold standard reference; do not use as a prototype for anything
- `brutalist_massing` — bespoke renderer, not using `renderHeightfield` at all

---

## 6. Propagation Plan (after prototype is validated)

Same discipline as the postMessage bridge rollout:

1. Prototype lands in `terrain_slice`, verified visually and via `npm run verify:modules`
2. Identify all modules that contain `renderHeightfield` verbatim (expected ~20–25)
3. Batch Codex pass: for each module, add `EXTRUDE_MODES` array + mode dispatch
   call site + five new PARAMS entries
4. Each batch gets a verify pass before the next batch starts
5. `grid_extrude` is handled last as a separate bespoke migration (its renderer is
   not `renderHeightfield` — it has its own `drawScene` with multi-layer support
   and displacement modes that need individual treatment)

---

*Grounded in code reading of `grid_extrude`, `terrain_slice`, `wave_lattice`, and
`contour_field` — confirmed 2D Canvas oblique projection, no WebGL.*
