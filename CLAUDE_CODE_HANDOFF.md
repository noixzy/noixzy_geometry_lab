# Claude Code Handoff — noixzy_geometry_lab

**Updated:** 2026-06-30 — commit `5813146` (brutalist_massing configurable draw order and mat z-offset)

## Repo
Repo-relative paths only. Local checkout path varies by environment (e.g. devcontainer mounts at `/workspaces/noixzy_geometry_lab`).

## Dev server
Already running: `npx serve . -l 3000`
Test at: `http://localhost:3000/module_shell.html?module=grid_extrude`

## Current task
_None active — pick from "Future Milestones" or open new work._

The previous task (layer stacking in `grid_extrude/noixzy_grid_extrude.html`) shipped in commit `96fa0d9`. `P.depth` now drives both recursion max depth (`buildLeaves()`, line ~779) and a layer-stacking pass in `drawScene()` around line ~822: 1–4 layers offset by `layerIndex * P.depth * 18` px on Y, alpha reduced 0.25 per layer, brightness dimmed 0.08 per layer.

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
- **Pan/zoom view layer:** mouse-driven `view { panX, panY, zoom }` object added; wired into `makeCfg()` so pan and dolly apply on top of existing param-driven camera.
- **Mouse interaction:** `mousemove` / `wheel` events mutate `view.panX`, `view.panY`, `view.zoom` (drag to rotate/pan, scroll to dolly). Shipped in `15a5e73`.
- **Mat z-order fix:** mat cells now get a small negative Y offset (`zBase -= 0.04`) so their top faces never project above other forms' ground planes at extreme camera angles. The renderer is 2D-canvas painter's algorithm, so this is a Y-offset fix rather than a depth-test one.
- **Draw-order param group:** new `order` group exposes `orderMain` / `orderTower` / `orderMat` (0–2 each). `draw()` now collects enabled layers, sorts by `order` ascending, and runs them — replacing the previous hardcoded sequence. Defaults: mat=0, main=1, tower=2 (mat behind, tower on top).

### Still pending
_None tracked here. Open new tasks as they come up._

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
- Full repo audit report added (`92e9037`)
- brutalist_massing configurable draw order + mat z-offset shipped (`5813146`)
- Module addition contract + validator: `LAB_MODULE_ADDITION_CONTRACT.md`, `scripts/validate_modules_manifest.js`, `npm run verify:modules`

## Git status
Clean on `main`. Last commit: `feat(brutalist_massing): configurable draw order and mat z-offset` (`5813146`).

## Future Milestones

### Color / Palette Audit
After the postMessage bridge is rolled out to all modules, conduct a full palette audit:
1. Inventory all PALETTES arrays across all modules
2. Identify shared colors and divergent ones
3. Build a shared noixzy palette registry modules can pull from
4. Wire shell to switch palettes globally via postMessage
5. Goal: lab feels like one coherent visual system, not 55 separate things

Prerequisite: bridge rolled out to all modules first.
