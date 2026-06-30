# blob_field — Module Spec

**Track:** WESDF (net-new SDF-native modules)  
**Status:** proposal approved, implementation not started  
**File:** `blob_field/noixzy_blob_field.html`

---

## 1. Concept

A 2D noise field sampled at an N×N grid drives metaball placement in 3D. Each
grid cell produces one implicit sphere; the field value at that cell controls
blob size and vertical position. Adjacent high-value blobs merge via polynomial
smooth minimum (`smin`) into connected ridges and plateaux. Low-value cells
produce near-zero radii that fall below the isosurface threshold, leaving empty
space between terrain features.

Visual reading: blobby terrain landscape rather than a floating cluster. The
grid positions are fixed; only field values change over time.

**Closest existing reference:** `metafluid` — same `smin` blending math and
Phong + AO shading pipeline. Key difference: metafluid positions are hardcoded
sinusoidal orbits; blob_field positions are field-sampled from a 2D noise
function evaluated at grid coordinates.

---

## 2. metafluid reference — what the new module inherits and changes

**Inherited:**
- `smin(a, b, k)` polynomial smooth minimum for blending
- `sdSphere(p, r)` as the primitive SDF
- AO sampling (4-step cone), Phong lighting model, fog, vignette
- `smin` k parameter → `u_smooth`
- Orbit camera (azimuth + elevation + distance + spin)
- Palette system (pal 0–11), bgAlpha transparency, rim/fmSat/fmVal material

**Changed:**
- Blob positions: hardcoded orbital constants → field-sampled grid coordinates
- Blob radii: fixed per-sphere scale → `base_rad * max(0, h - thresh)`
- Blob count: `u_count` (1–32 explicit blobs) → `density²` (N×N grid, N=2–6)
- Animation: all blobs orbit around fixed paths → field phase advances in time,
  blobs grow/shrink/merge in place
- Y position: all blobs at `elev` height → `cy = h * height_scale` so tall
  blobs are centered higher, producing true vertical terrain variation

---

## 3. Field-to-blob-placement mapping

### Grid sampling

```
N = round(u_density),  N ∈ {2..6}  →  4..36 blobs total

For each cell (i, j),  i,j = 0..N-1:

  u = (float(i) + 0.5) / float(N)      // normalized 0..1
  v = (float(j) + 0.5) / float(N)

  h = field(u * scale, v * scale, t)    // 0..1 FBM noise, 3 octaves + domain warp
                                         // t = u_time * mix(0.02, 0.4, u_speed)

  cx = (u - 0.5) * spr                  // XZ: centered grid in world space
  cz = (v - 0.5) * spr                  //     spr = mix(1.0, 4.0, u_spread)
  cy = h * mix(0.0, 2.0, u_height)      // Y: blob center rises with field value

  rad = mix(0.1, 0.6, u_radius) * max(0.0, h - u_thresh)   // 0 below threshold
```

### Why Y = h × height_scale (not flat)

Blobs centered at altitude proportional to field value means two adjacent tall
blobs merge at altitude, forming a ridge. A tall blob next to a short one has
its center well above the short blob's radius range, so they separate naturally
instead of forming a flat carpet. This produces genuine topographic variation:
connected peaks, isolated mounds, empty valleys.

### Why `rad = base_rad * max(0, h - thresh)`

Below `thresh`, radius is zero — the blob doesn't reach the isosurface and the
cell reads as empty terrain. Above `thresh`, radius scales linearly with field
intensity. This gives clean separation between "terrain present" and "terrain
absent" regions without a hard cutoff in the isosurface itself (`smin` handles
the transition smoothly at the boundary).

### Density × smooth visual matrix

| density | smooth | visual |
|---------|--------|--------|
| 2 (4 blobs) | high | 4 massive merging lobes |
| 4 (16 blobs) | mid | connected hills, default |
| 6 (36 blobs) | low | textured ridge field |
| any | 0 | discrete unmerged blobs |

---

## 4. GLSL implementation note

The field is evaluated once per blob position at pixel startup (in `main()`
before the raymarching loop), results stored in a global `vec4 _blobs[36]`
(constant-size array, GLSL ES 1.00 compatible). `map()` reads `_blobs[]`
without re-evaluating the field. This avoids evaluating a 3-octave FBM 36
times per ray step — the field cost is O(N²) per pixel, not O(N² × steps).

Inactive blobs (index >= density²) receive `rad = 0.0`; `sdSphere(p, 0)` =
`length(p - center)` which is always > 0.001 at any raymarch position, so
inactive blobs never contribute to the isosurface. Same pattern as metafluid's
`(u_count >= k.0) ? rad : 0.0001` gating.

---

## 5. Blender portability

### formSpec output

```json
{
  "primitive": "metaball_field",
  "field": { "type": "fbm", "octaves": 3, "scale": 0.42, "warp": 0.30 },
  "grid": { "N": 4, "spread": 2.0, "height": 1.1, "thresh": 0.28 },
  "blobs": [
    { "pos": [cx, cy, cz], "radius": rad },
    "..."
  ],
  "blend_stiffness": 0.65,
  "time": 0.0
}
```

### Blender reconstruction steps

1. Evaluate the same FBM field at the same N×N grid points (given `scale`,
   `warp`, `time`)
2. Compute `(cx, cy, cz, rad)` per cell using the formulas in §3
3. Create one Blender metaball object per blob, set `radius = rad`
4. Set metaball `resolution = 0.05`, `stiffness = mix(0.05, 0.65, smooth)` to
   match the `smin` k parameter
5. Render — Blender's metaball isosurface solver is structurally identical to
   the GLSL `map()` function

This is the most direct Blender-portable design available: the GLSL SDF is
what Blender's metaball renderer computes internally, just expressed in shader
code. No approximation needed.

---

## 6. PARAMS array

```javascript
const PARAMS = [
  // field
  {k:"density", g:"field",    label:"density",    min:2,  max:6,   step:1,    v:4},
  {k:"scale",   g:"field",    label:"scale",      min:0,  max:1,   step:0.01, v:0.42},
  {k:"warp",    g:"field",    label:"warp",       min:0,  max:1,   step:0.01, v:0.30},
  {k:"thresh",  g:"field",    label:"threshold",  min:0,  max:0.8, step:0.01, v:0.28},
  // form
  {k:"radius",  g:"form",     label:"radius",     min:0,  max:1,   step:0.01, v:0.55},
  {k:"height",  g:"form",     label:"height",     min:0,  max:1,   step:0.01, v:0.55},
  {k:"smooth",  g:"form",     label:"smooth",     min:0,  max:1,   step:0.01, v:0.45},
  {k:"spread",  g:"form",     label:"spread",     min:0,  max:1,   step:0.01, v:0.55},
  // motion
  {k:"speed",   g:"motion",   label:"speed",      min:0,  max:1,   step:0.01, v:0.20},
  {k:"spin",    g:"motion",   label:"spin",       min:0,  max:1,   step:0.01, v:0.15},
  // camera
  {k:"dist",    g:"camera",   label:"dist",       min:2,  max:10,  step:0.05, v:5.0},
  {k:"elev",    g:"camera",   label:"elev",       min:-2, max:2,   step:0.05, v:0.8},
  // material
  {k:"ao",      g:"material", label:"ambient occ",min:0,  max:1,   step:0.01, v:0.70},
  {k:"pal",     g:"material", label:"palette",    min:0,  max:11,  step:1,    v:4},
  {k:"bgVal",   g:"material", label:"bg value",   min:0,  max:2,   step:0.01, v:1.0},
  {k:"fmVal",   g:"material", label:"form value", min:0,  max:2,   step:0.01, v:1.0},
  {k:"fmSat",   g:"material", label:"form sat",   min:0,  max:2,   step:0.01, v:1.0},
  {k:"rim",     g:"material", label:"rim",        min:0,  max:2,   step:0.01, v:1.0},
  {k:"bgAlpha", g:"material", label:"bg alpha",   min:0,  max:1,   step:1,    v:0},
];
```

19 params across 5 groups. No `mirror`/`zdepth`/`stack`/`recdepth` — 2D
heightfield concepts not applicable to a raymarched SDF module.

`density` replaces metafluid's `count`: it's a grid resolution (spatial layout
changes), not just adding/removing blobs from a fixed set.

---

## 7. Repo layout (per LAB_MODULE_ADDITION_CONTRACT.md)

```
blob_field/
  noixzy_blob_field.html
home/thumbs/
  blob_field.png              ← placeholder needed before verify:modules
modules.manifest.json         ← one new entry required
```

Manifest entry:
```json
{
  "id": "blob_field",
  "title": "blob field",
  "file": "blob_field/noixzy_blob_field.html",
  "thumb": "home/thumbs/blob_field.png",
  "authorship": "generated",
  "listedInHome": true,
  "enabledInShell": true,
  "status": "listed"
}
```
