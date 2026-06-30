# Claude Code Handoff — noixzy_geometry_lab

**Updated:** 2026-06-30 — pending commits: legacy cleanup + bridge rollout batch 1 sub-batches 1–2

## Repo
Repo-relative paths only. Local checkout path varies by environment (e.g. devcontainer mounts at `/workspaces/noixzy_geometry_lab`).

## Dev server
Already running: `npx serve . -l 3000`
Test at: `http://localhost:3000/module_shell?module=grid_extrude`

## Current task
_None active — pick from "Future Milestones" or open new work._

The previous task (layer stacking in `grid_extrude/noixzy_grid_extrude.html`) shipped in commit `96fa0d9`. `P.depth` now drives both recursion max depth (`buildLeaves()`, line ~779) and a layer-stacking pass in `drawScene()` around line ~822: 1–4 layers offset by `layerIndex * P.depth * 18` px on Y, alpha reduced 0.25 per layer, brightness dimmed 0.08 per layer.

### Shell / UI notes
- Shell is at `module_shell.html` (root)
- Param panel populated via postMessage bridge in each module (end of file, separate `<script>` tag)
- Param panel column width: **225px** (buttons, sliders, undo bar all match); `.shellTrigger` hover area 255px
- Speed slider is sorted to top of param panel by shell
- `__extrudeOff` checkbox lives in shell controls above random buttons, not in param panel
- When extrude is **on** in grid_extrude, the world origin is shifted -30px X in `drawScene()` to compensate for the 3D mass shifting right

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

## brutalist_massing — recent work

### Shipped
- **Form mode 1 (megaform):** background/secondary form removed; mat now draws as base layer; mega tower is the only standing form. Modes 0 and 2 unchanged.
- **Pan/zoom view layer:** mouse-driven `view { panX, panY, zoom }` wired into `makeCfg()`; layered over param-driven camera.
- **Mouse interaction:** `mousemove` / `wheel` drive rotate-on-drag, pan, and dolly. (`15a5e73`)
- **Mat z-order fix:** mat cells get a small negative Y offset (`zBase -= 0.04`) so their top faces never project above other forms' ground planes at extreme camera angles. 2D-canvas painter's renderer, so this is a Y-offset fix, not a depth-test one. (`5813146`)
- **Draw-order param group:** new `order` group exposes `orderMain` / `orderTower` / `orderMat` (0–2 each). `draw()` collects enabled layers, sorts by `order` ascending, runs them — replaces the previous hardcoded sequence. Defaults: mat=0, main=1, tower=2. (`5813146`)
- **Orphan variants archived:** `brutalist_massing_folded`, `brutalist_massing_mat`, `brutalist_massing_megaform` moved out of tree — only the unified `brutalist_massing/` remains. (`2207108`)

### Open
_None tracked here. Open new tasks as they come up._

## Bridge Rollout

Rolling out the PARAMS/postMessage bridge to all 55 modules. Reference implementation: `grid_extrude/noixzy_grid_extrude.html`.

### Batch 1 — core visual modules

**Sub-batch 1 of 3 — done (`5129b27`):**
- `hex_grid/noixzy_hex_grid.html`
- `rose_curve/noixzy_rose_curve.html`
- `lissajous_mesh/noixzy_lissajous_mesh.html`

**Sub-batch 2 of 3 — done (`5129b27`):**
- `torus_knot/noixzy_torus_knot.html`
- `moire_field/noixzy_moire_field.html`
- `particle_orbitals/noixzy_particle_orbitals.html`
- `radial_noise/noixzy_radial_noise.html`
- `kaleidoscope_field/noixzy_kaleidoscope_field.html`
- `topographic_rings/noixzy_topographic_rings.html`
- `ribbon_flow/noixzy_ribbon_flow.html`

Notes: shared-template modules now expose the shell bridge, `randomizeParams`, `noixzyModuleControls`, `__extrudeOff`, and `__bgAlpha`; stale native `ALL_MODULES` payloads were cleared to stop archived-thumbnail 404s. `torus_knot` has a custom bridge with lightweight shell history and seed state.

**Sub-batch 3 of 3 — not started.** (remaining modules TBD)

Already bridged before this rollout: `brutalist_massing`, `triangulated_signal_mesh`, `grid_extrude`.

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
- 55 active modules in `modules.manifest.json`, all listed and enabled
- brutalist_massing and triangulated_signal_mesh migrated — bridge wired, native UI hidden
- Full repo audit report added (`92e9037`)
- brutalist_massing configurable draw order + mat z-offset shipped (`5813146`)
- Orphan brutalist_massing variants (folded, mat, megaform) archived (`2207108`)
- Touch-only param panel toggle for iPad / phones (`aeee7f4`)
- Dead PARAMS entries removed: `depthAxis` in grid_extrude, `edge` in reaction_terraces (`08f7c99`)
- Module addition contract + validator: `LAB_MODULE_ADDITION_CONTRACT.md`, `scripts/validate_modules_manifest.js`, `npm run verify:modules`
- Param panel sliders widened to 225px across all modules (`eec6a7e`)
- grid_extrude: extrude-on form centering (-30px X shift in `drawScene()`) (`4d9b589`)
- `_legacy_planning_docs/Users/` absolute-path clone removed: 44 outdated duplicates discarded, 21 unique files archived to `workspace/_legacy_archive_merge_20260629/` (`1bc99fa`)
- Bridge rollout batch 1 sub-batch 1: `hex_grid`, `rose_curve`, `lissajous_mesh` — PARAMS array + postMessage bridge wired (`5129b27`)
- Bridge rollout batch 1 sub-batch 2: `torus_knot`, `moire_field`, `particle_orbitals`, `radial_noise`, `kaleidoscope_field`, `topographic_rings`, `ribbon_flow` — PARAMS bridge + shell control shims wired (`5129b27`)

## Git status
Clean on `main`. Last two commits:
- `1bc99fa` — `chore: remove _legacy_planning_docs/ absolute-path clone (65 files)`
- `5129b27` — `feat(bridge): roll out PARAMS/postMessage bridge — batch 1 sub-batches 1–2`

## Housekeeping Backlog

Verified against current repo state (2026-06-30) from `LAB_AUDIT_20260629.md` (audit HEAD `15a5e73`). Items below remain open; resolved items are omitted.

### Debug logs in module_shell.html
Two `// DEBUG` console.log calls still live:
- `module_shell.html:689` — `console.log("[shell] → getParams attempt", attempts, frame.src);`
- `module_shell.html:702` — `console.log("[shell] msg:", e.data?.type, e.origin, e.data);`

Remove both before any production build.

### !important in triangulated_signal_mesh
The native UI suppression block in `triangulated_signal_mesh/noixzy_triangulated_signal_mesh.html` (lines 177–179) uses `!important` on `body`, `main`, `aside`, and `canvas` — violating the migration checklist rule "No !important CSS overrides". Replace with a specificity-based approach matching the pattern in `grid_extrude`.

### .gitignore cleanup
Three issues remain:
1. `.DS_Store` appears twice (lines 1 and 9) — deduplicate.
2. The `planning_dashboard/dashboard_preview.png` rule is dead at the root level — the file lives at `_legacy_import/planning/planning_dashboard/dashboard_preview.png`, not the path the rule targets.
3. No coverage for `*.zip`, `*.blend`, or `home/thumbs/*.png` — all currently tracked (see "Large files" below).

### Large files tracked in git
All of the following are in the index with no `.gitignore` exclusion:
- `home/thumbs/*.png` — 60+ thumbnails; six exceed 500 KB (`contour_field.png`, `phyllotaxis_stack.png`, `reaction_terraces.png`, `agent_swarm_relief.png`, `voronoi_tower_field.png`, `origami_fold_field.png`)
- `workspace/module_archive_20260629.zip` (≈2.7 MB) tracked alongside its unzipped `workspace/module_archive_20260629/` tree
- `workspace/ae_scripts.zip` tracked alongside `workspace/ae_scripts/`
- `_legacy_import/old_build_assets/blender_builds/unified_shell_pilot_scene.blend` tracked

Consider `.gitignore`-ing archives and blends and generating `home/thumbs/` on demand rather than committing them.

### make_contact_sheets.py at repo root
`make_contact_sheets.py` sits at the repo root with no declared home. Move to `scripts/` or `_legacy_import/tools/` to reduce root-level noise.

## Future Milestones

### Color / Palette Audit
After the postMessage bridge is rolled out to all modules, conduct a full palette audit:
1. Inventory all PALETTES arrays across all modules
2. Identify shared colors and divergent ones
3. Build a shared noixzy palette registry modules can pull from
4. Wire shell to switch palettes globally via postMessage
5. Goal: lab feels like one coherent visual system, not 55 separate things

Prerequisite: bridge rolled out to all modules first.
