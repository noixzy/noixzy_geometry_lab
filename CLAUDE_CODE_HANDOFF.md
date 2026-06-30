# Claude Code Handoff — noixzy_geometry_lab

**Updated:** 2026-06-29 — commit `96989fc` (restore param panel to sidebar, JS hover bridge for shell controls, brutalist_massing pan/zoom view layer)

## Repo
`/Users/noixzy.macbookpro/Documents/noixzy_geometry_lab`

## Dev server
Already running: `npx serve . -l 3000`
Test at: `http://localhost:3000/module_shell?module=grid_extrude`

## Current task
Add layer stacking to `grid_extrude/noixzy_grid_extrude.html`.

### What depth currently does
`P.depth` (line ~460, group `"system"`, range 0–1) maps to recursion max depth in `buildLeaves()`:
```js
const maxD = Math.floor(map(P.depth, 0, 1, 3, 8));
```
This controls grid subdivision but has no visible effect at default settings.

### What we want depth to also do
Drive a **layer stacking** effect — draw the full grid 1–4 times at increasing Y offsets, each layer slightly darker and more transparent. Depth = 0 → 1 layer (no stacking). Depth = 1 → 4 layers stacked behind the main one.

### Where to hook in
`drawScene()` function. The leaf draw loop starts at line ~806:
```js
const drawLeaves = Math.abs(P.zdepth||0) > 0.01 ? [...leaves].sort(...) : leaves;
for (const c of drawLeaves) { ... }
```
Wrap the existing leaf block in a layer loop. Each layer pass should:
- Offset Y by `layerIndex * P.depth * 18` pixels
- Reduce alpha by `layerIndex * 0.25`
- Reduce brightness slightly per layer

### Shell / UI notes
- Shell is at `module_shell.html` (root)
- Param panel populated via postMessage bridge in `grid_extrude` (end of file, separate `<script>` tag)
- Speed slider is sorted to top of param panel by shell
- `__extrudeOff` checkbox lives in shell controls above random buttons, not in param panel

## Module Migration Checklist

Every module migrated into the main lab MUST implement all of the following before being considered complete:

### Required functionality
- [ ] Seed variable — deterministic randomness, exposed as param
- [ ] New seed — generates new random seed and redraws on demand
- [ ] Undo / redo — history stack (min 50 snapshots), full P state snapshots
- [ ] Pause / resume — toggles animation loop
- [ ] Reset — restores all params to defaults
- [ ] Save — exports canvas as PNG
- [ ] Save 2x — exports canvas at 2x resolution
- [ ] Thumb — exports a thumbnail-sized PNG
- [ ] Record — captures a video/gif loop
- [ ] BG alpha — toggles transparent background on/off
- [ ] Randomize all — randomizes all unlocked params
- [ ] Randomize form — randomizes form/geometry params only
- [ ] Randomize color — randomizes color/palette params only

### Required bridge
- [ ] PARAMS array with all params declared (k, label, min, max, step, v, g)
- [ ] P state object initialized from PARAMS
- [ ] postMessage bridge handling getParams and setParam
- [ ] No ALL_MODULES list
- [ ] No !important CSS overrides
- [ ] No native UI visible (canvas only)

### Reference implementation
grid_extrude/noixzy_grid_extrude.html is the gold standard. Match its patterns.

## brutalist_massing — in-progress work

### Done this session
- **Form mode 1 (megaform):** background/secondary form removed; mat now draws as base layer; mega tower is the only standing form. Modes 0 and 2 unchanged. No params, generators, or postMessage bridge touched.
- **Pan/zoom view layer:** mouse-driven `view { panX, panY, zoom }` object added; wired into `getCamera()` so pan and dolly apply on top of existing param-driven camera. Not yet hooked to mouse events — wiring is the next step.

### Still pending
- **Mouse interaction:** wire `mousemove` / `wheel` events to mutate `view.panX`, `view.panY`, `view.zoom`; rotate on drag, pan on middle-click/two-finger, dolly on scroll.
- **Mat z-order fix:** mat polygon is currently drawn mid-stack; needs to render as true ground plane beneath all towers regardless of sort order.

## What's already done and committed
- CSS consolidated in `home/home.html` and `module_shell.html` (no overrides, no !important)
- Routing fixed (module_shell uses ?module= param correctly)
- Param panel via postMessage bridge (shell ↔ module)
- Utility bar (save, save 2x, thumb, rec) — hover-to-reveal, centered top
- Prev/next nav pills on left and right sides — hover-to-reveal
- Extrude off toggle in shell controls above random buttons
- Speed rotation bug fixed, speed max increased to 2
- ALL_MODULES cleared in grid_extrude (was causing 404s for dead modules)
- sdf module archived and removed from manifest
- 55 active modules, all listed and enabled
- brutalist_massing and triangulated_signal_mesh migrated — bridge wired, native UI hidden

## Git status
Clean on `main`. Last commit: `feat: migrate brutalist_massing and triangulated_signal_mesh, migration checklist added`

## Future Milestones

### Color / Palette Audit
After the postMessage bridge is rolled out to all modules, conduct a full palette audit:
1. Inventory all PALETTES arrays across all modules
2. Identify shared colors and divergent ones
3. Build a shared noixzy palette registry modules can pull from
4. Wire shell to switch palettes globally via postMessage
5. Goal: lab feels like one coherent visual system, not 55 separate things

Prerequisite: bridge rolled out to all modules first.
