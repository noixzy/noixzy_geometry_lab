# Module Bridge Status

**55 modules total — 13 migrated, 39 PARAMS-only, 3 not started**

Legend:
- `✅` — PARAMS array + postMessage bridge fully wired; shell can read/write all params
- `〇` — PARAMS array present but bridge not yet wired; shell cannot control
- `✗` — No PARAMS array; needs full migration from scratch

Reference implementation: `grid_extrude/noixzy_grid_extrude.html`

---

| # | id | file | status | notes |
|---|-----|------|--------|-------|
| 1 | grid_extrude | `grid_extrude/noixzy_grid_extrude.html` | ✅ | Gold standard — reference implementation. Layer stacking (1–4 layers), `__extrudeOff` toggle, extrude-on world-origin shift (-30px X). |
| 2 | brutalist_massing | `brutalist_massing/noixzy_brutalist_massing.html` | ✅ | Custom bridge. Configurable draw order (orderMain/orderTower/orderMat), mat z-offset, pan/zoom/dolly mouse interaction, megaform mode 1 rework. |
| 3 | triangulated_signal_mesh | `triangulated_signal_mesh/noixzy_triangulated_signal_mesh.html` | ✅ | Bridge wired. **Open:** native UI suppression block (lines 177–179) still uses `!important` — violates migration checklist. Replace with specificity-based approach. |
| 4 | moire_field | `moire_field/noixzy_moire_field.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). Shared-template pattern; `ALL_MODULES` payload cleared. |
| 5 | particle_orbitals | `particle_orbitals/noixzy_particle_orbitals.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). Shared-template pattern; `ALL_MODULES` payload cleared. |
| 6 | radial_noise | `radial_noise/noixzy_radial_noise.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). Shared-template pattern; `ALL_MODULES` payload cleared. |
| 7 | kaleidoscope_field | `kaleidoscope_field/noixzy_kaleidoscope_field.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). Shared-template pattern; `ALL_MODULES` payload cleared. |
| 8 | topographic_rings | `topographic_rings/noixzy_topographic_rings.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). Shared-template pattern; `ALL_MODULES` payload cleared. |
| 9 | ribbon_flow | `ribbon_flow/noixzy_ribbon_flow.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). Shared-template pattern; `ALL_MODULES` payload cleared. |
| 10 | hex_grid | `hex_grid/noixzy_hex_grid.html` | ✅ | Batch 1 sub-batch 1 (`5129b27`). |
| 11 | rose_curve | `rose_curve/noixzy_rose_curve.html` | ✅ | Batch 1 sub-batch 1 (`5129b27`). |
| 12 | lissajous_mesh | `lissajous_mesh/noixzy_lissajous_mesh.html` | ✅ | Batch 1 sub-batch 1 (`5129b27`). |
| 13 | torus_knot | `torus_knot/noixzy_torus_knot.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). Custom bridge with lightweight shell history and seed state. |
| 14 | glyph_field | `glyph_field/noixzy_glyph_field.html` | 〇 | |
| 15 | crystal_growth | `crystal_growth/noixzy_crystal_growth.html` | 〇 | |
| 16 | vector_scope | `vector_scope/noixzy_vector_scope.html` | 〇 | |
| 17 | wave_lattice | `wave_lattice/noixzy_wave_lattice.html` | 〇 | |
| 18 | fractal_tiles | `fractal_tiles/noixzy_fractal_tiles.html` | 〇 | |
| 19 | plasma_membrane | `plasma_membrane/noixzy_plasma_membrane.html` | 〇 | |
| 20 | interference_grid | `interference_grid/noixzy_interference_grid.html` | 〇 | |
| 21 | cellular_bloom | `cellular_bloom/noixzy_cellular_bloom.html` | 〇 | |
| 22 | vortex_sheet | `vortex_sheet/noixzy_vortex_sheet.html` | 〇 | |
| 23 | prism_moire | `prism_moire/noixzy_prism_moire.html` | 〇 | |
| 24 | terrain_slice | `terrain_slice/noixzy_terrain_slice.html` | 〇 | |
| 25 | signal_weave | `signal_weave/noixzy_signal_weave.html` | 〇 | |
| 26 | crater_field | `crater_field/noixzy_crater_field.html` | 〇 | |
| 27 | spiral_lattice | `spiral_lattice/noixzy_spiral_lattice.html` | 〇 | |
| 28 | signal_rain | `signal_rain/noixzy_signal_rain.html` | 〇 | |
| 29 | echo_contours | `echo_contours/noixzy_echo_contours.html` | 〇 | |
| 30 | magnetic_dust | `magnetic_dust/noixzy_magnetic_dust.html` | 〇 | |
| 31 | neural_lattice | `neural_lattice/noixzy_neural_lattice.html` | 〇 | |
| 32 | flow_field | `flow_field/noixzy_flow_field.html` | 〇 | |
| 33 | reaction_diffusion | `reaction_diffusion/noixzy_reaction_diffusion.html` | 〇 | |
| 34 | voronoi | `voronoi/noixzy_voronoi.html` | 〇 | |
| 35 | contour_field | `contour_field/noixzy_contour_field.html` | 〇 | |
| 36 | truchet | `truchet/noixzy_truchet.html` | 〇 | |
| 37 | truchet_b | `truchet_b/noixzy_truchet_b.html` | 〇 | |
| 38 | l_system | `l_system/noixzy_l_system.html` | 〇 | |
| 39 | cellular_erosion | `cellular_erosion/noixzy_cellular_erosion.html` | 〇 | |
| 40 | recursive_grid | `recursive_grid/noixzy_recursive_grid.html` | 〇 | |
| 41 | wave_interference | `wave_interference/noixzy_wave_interference.html` | 〇 | |
| 42 | stipple | `stipple/noixzy_stipple.html` | 〇 | |
| 43 | agent_swarm_relief | `agent_swarm_relief/noixzy_agent_swarm_relief.html` | 〇 | |
| 44 | catenary_web | `catenary_web/noixzy_catenary_web.html` | 〇 | |
| 45 | hyperbolic_tiling | `hyperbolic_tiling/noixzy_hyperbolic_tiling.html` | 〇 | |
| 46 | origami_fold_field | `origami_fold_field/noixzy_origami_fold_field.html` | 〇 | |
| 47 | phyllotaxis_stack | `phyllotaxis_stack/noixzy_phyllotaxis_stack.html` | 〇 | |
| 48 | quasicrystal_relief | `quasicrystal_relief/noixzy_quasicrystal_relief.html` | 〇 | |
| 49 | reaction_terraces | `reaction_terraces/noixzy_reaction_terraces.html` | 〇 | Dead `edge` PARAMS entry removed (`08f7c99`). |
| 50 | tensegrity_nodes | `tensegrity_nodes/noixzy_tensegrity_nodes.html` | 〇 | |
| 51 | voronoi_tower_field | `voronoi_tower_field/noixzy_voronoi_tower_field.html` | 〇 | |
| 52 | woven_lattice_relief | `woven_lattice_relief/noixzy_woven_lattice_relief.html` | 〇 | |
| 53 | mandelbulb | `mandelbulb/noixzy_mandelbulb.html` | ✗ | No PARAMS array. Needs full migration. |
| 54 | metafluid | `metafluid/noixzy_metafluid.html` | ✗ | No PARAMS array. Needs full migration. Has inertia drag (`mousemove` / `mouseup`) added separately. |
| 55 | gyroid | `gyroid/noixzy_gyroid.html` | ✗ | No PARAMS array. Needs full migration. |
