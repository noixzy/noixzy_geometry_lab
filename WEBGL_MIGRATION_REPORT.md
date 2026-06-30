# WebGL Module Migration Report

Full migration of mandelbulb, metafluid, and gyroid from raw GLSL/P-state modules into the standard PARAMS + postMessage bridge pattern. These are raymarching modules — no canvas heightfield, no SHARED array, bespoke PARAMS per module.

Status: **awaiting approval on mandelbulb PARAMS before implementation begins**

---

## Module 1 — mandelbulb

**File:** `mandelbulb/noixzy_mandelbulb.html`  
**Status:** Proposed — pending confirmation

### What drives the shader today

| Key | Object | Shader uniform | Range |
|-----|--------|----------------|-------|
| `power` | P | `u_power` | 0–1 → fractal power 2–10 |
| `morph` | P | `u_morph` | 0–1 → power swing ±2.5 via sin(t) |
| `detail` | P | `u_detail` | 0–1 → ray epsilon 0.0015–0.0003 |
| `glow` | P | `u_glow` | 0–1 → glow brightness |
| `ao` | P | `u_ao` | 0–1 → ambient occlusion strength |
| `spin` | P | `u_spin * 0.28` | 0–1 → auto-orbit speed |
| `dist` | P | `u_dist` | 0–1 → camera distance 2.15–5.25 |
| `elev` | P | `u_elev` | 0–1 → camera elevation −1.35–1.85 |
| `pal` | P (int slider) | → `applyPalette()` → cs.bg/form/hi | int 0–11 |
| `bgVal` | cs | `u_bgValue` | 0–2 |
| `fSat` | cs | `u_formSat` | 0–2 |
| `fVal` | cs | `u_formValue` | 0–2 |
| `rim` | cs | `u_rim` | 0–2 |
| `transparentBg` | bool | `u_transparentBg` | bool |

Individual `bgColor`/`formColor`/`hiColor` color pickers are replaced by `pal` (same as all template modules).

### Proposed PARAMS array

```javascript
const PARAMS = [
  // fractal form
  {k:"power",  label:"power",       min:0,  max:1,  step:0.01, v:0.75},
  {k:"morph",  label:"morph",       min:0,  max:1,  step:0.01, v:0.22},
  {k:"detail", label:"detail",      min:0,  max:1,  step:0.01, v:0.55},
  {k:"glow",   label:"glow",        min:0,  max:1,  step:0.01, v:0.45},
  {k:"ao",     label:"ambient occ", min:0,  max:1,  step:0.01, v:0.70},
  // camera
  {k:"spin",   label:"spin",        min:0,  max:1,  step:0.01, v:0.18},
  {k:"dist",   label:"distance",    min:0,  max:1,  step:0.01, v:0.52},
  {k:"elev",   label:"elevation",   min:0,  max:1,  step:0.01, v:0.50},
  // material
  {k:"pal",    label:"palette",     min:0,  max:11, step:1,    v:4},
  {k:"bgVal",  label:"bg value",    min:0,  max:2,  step:0.01, v:1.0},
  {k:"fmVal",  label:"form value",  min:0,  max:2,  step:0.01, v:1.0},
  {k:"fmSat",  label:"form sat",    min:0,  max:2,  step:0.01, v:1.0},
  {k:"rim",    label:"rim",         min:0,  max:2,  step:0.01, v:1.0},
  // meta
  {k:"bgAlpha",label:"bg alpha",    min:0,  max:1,  step:1,    v:0, type:"bool"},
];
```

**Naming notes:**
- `fSat`/`fVal` renamed `fmSat`/`fmVal` — matches template SHARED naming; `setParam` maps them back to shader uniforms.
- `spin` stays `spin`, not `speed` — it controls orbit rotation specifically; there is no independent time-scale uniform in this shader.
- No `mirror`/`zdepth`/`stack`/`recdepth`/`erosion`/`noise` — 2D heightfield concepts not applicable to GLSL raymarcher.
- `bgAlpha` wired as `type:"bool"` — same pattern as `__extrudeOff`, sets `transparentBg` bool and updates `u_transparentBg` uniform.

### Migration checklist

- [ ] Remove `ALL_MODULES` array (line 1124) — `buildNav()` switches to `modules.manifest.json` fetch
- [ ] Strip stacked `!important` CSS blocks (lines 91–413) — replace with specificity-based rules matching migrated module standard
- [ ] Remove native `<div class="panel">` slider rows from HTML — shell owns the param panel
- [ ] Collapse `P` + `cs` into flat `P` driven by PARAMS
- [ ] Wire `_noixzySetParam(key, value)` with special handling for `pal` → `applyPalette()` and `bgAlpha` → `transparentBg`
- [ ] Add `_noixzyPostShellParams()` — posts `{type:"params", defs:[...], P:{...}}` to parent
- [ ] Add `window.addEventListener("message", ...)` handler for `getParams` / `setParam`
- [ ] Confirm `verify:modules` passes

---

## Module 2 — metafluid

**File:** `metafluid/noixzy_metafluid.html`  
**Status:** Not yet inventoried — pending mandelbulb completion

Known: WebGL GLSL raymarcher. Has inertia drag (mousemove/mouseup + velocity damping). Camera uses azimuth/elevation + damping velocity state.

---

## Module 3 — gyroid

**File:** `gyroid/noixzy_gyroid.html`  
**Status:** Not yet inventoried — pending metafluid completion

Known: WebGL GLSL raymarcher. Orbit camera via `u_azimuth` + `u_elevation` uniforms.

---

## Shared migration decisions (apply to all three)

| Decision | Rationale |
|----------|-----------|
| No SHARED array | These modules have no mirror symmetry, no 2D z-depth, no stack layers — SHARED is meaningless here |
| `pal` int 0–11 replaces color pickers | Consistent with all 52 bridged modules |
| Orbit drag stays native | Mouse/pointer drag updates `P.elev` / `_camAzimuth` directly; bridge just reads/writes the same keys |
| `bgAlpha` as bool param | Shell shows it as a checkbox (same as `__extrudeOff` / `__symmetryOff` pattern) |
| No `__symmetryOff` | No mirror param in these modules; toggle has nothing to control |
| `buildNav()` via manifest fetch | Removes hardcoded `ALL_MODULES` array present in all three |
