# Module Bridge Status

**55 modules total — 52 bridged, 0 PARAMS-only, 3 in migration**

Legend:
- `✅` — PARAMS array + postMessage bridge fully wired; shell can read/write all params
- `〇` — PARAMS array present but bridge not yet wired; shell cannot control
- `✗` — No PARAMS array; needs full migration from scratch
- `🔧` — Migration in progress (WebGL raymarcher family); see `WEBGL_MIGRATION_REPORT.md`

Reference implementation: `grid_extrude/noixzy_grid_extrude.html`

---

| # | id | file | status | notes |
|---|-----|------|--------|-------|
| 1 | grid_extrude | `grid_extrude/noixzy_grid_extrude.html` | ✅ | Gold standard — reference implementation. Layer stacking (1–4 layers), `__extrudeOff` toggle, extrude-on world-origin shift (-30px X). |
| 2 | brutalist_massing | `brutalist_massing/noixzy_brutalist_massing.html` | ✅ | Custom bridge. Configurable draw order (orderMain/orderTower/orderMat), mat z-offset, pan/zoom/dolly mouse interaction, megaform mode 1 rework. |
| 3 | triangulated_signal_mesh | `triangulated_signal_mesh/noixzy_triangulated_signal_mesh.html` | ✅ | Bridge wired. **Open:** native UI suppression block (lines 177–179) still uses `!important` — violates migration checklist. Replace with specificity-based approach. |
| 4 | moire_field | `moire_field/noixzy_moire_field.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). |
| 5 | particle_orbitals | `particle_orbitals/noixzy_particle_orbitals.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). |
| 6 | radial_noise | `radial_noise/noixzy_radial_noise.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). |
| 7 | kaleidoscope_field | `kaleidoscope_field/noixzy_kaleidoscope_field.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). |
| 8 | topographic_rings | `topographic_rings/noixzy_topographic_rings.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). |
| 9 | ribbon_flow | `ribbon_flow/noixzy_ribbon_flow.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). |
| 10 | hex_grid | `hex_grid/noixzy_hex_grid.html` | ✅ | Batch 1 sub-batch 1 (`5129b27`). |
| 11 | rose_curve | `rose_curve/noixzy_rose_curve.html` | ✅ | Batch 1 sub-batch 1 (`5129b27`). |
| 12 | lissajous_mesh | `lissajous_mesh/noixzy_lissajous_mesh.html` | ✅ | Batch 1 sub-batch 1 (`5129b27`). |
| 13 | torus_knot | `torus_knot/noixzy_torus_knot.html` | ✅ | Batch 1 sub-batch 2 (`5129b27`). |
| 14 | glyph_field | `glyph_field/noixzy_glyph_field.html` | ✅ | Batch 5. |
| 15 | crystal_growth | `crystal_growth/noixzy_crystal_growth.html` | ✅ | Batch 5. |
| 16 | vector_scope | `vector_scope/noixzy_vector_scope.html` | ✅ | Batch 5. |
| 17 | wave_lattice | `wave_lattice/noixzy_wave_lattice.html` | ✅ | Batch 5. |
| 18 | fractal_tiles | `fractal_tiles/noixzy_fractal_tiles.html` | ✅ | Batch 5. |
| 19 | plasma_membrane | `plasma_membrane/noixzy_plasma_membrane.html` | ✅ | Batch 5. |
| 20 | interference_grid | `interference_grid/noixzy_interference_grid.html` | ✅ | Batch 5. |
| 21 | cellular_bloom | `cellular_bloom/noixzy_cellular_bloom.html` | ✅ | Batch 5. |
| 22 | vortex_sheet | `vortex_sheet/noixzy_vortex_sheet.html` | ✅ | Batch 5. |
| 23 | prism_moire | `prism_moire/noixzy_prism_moire.html` | ✅ | Batch 5. |
| 24 | terrain_slice | `terrain_slice/noixzy_terrain_slice.html` | ✅ | Batch 5. |
| 25 | signal_weave | `signal_weave/noixzy_signal_weave.html` | ✅ | Batch 5. |
| 26 | crater_field | `crater_field/noixzy_crater_field.html` | ✅ | Batch 5. |
| 27 | spiral_lattice | `spiral_lattice/noixzy_spiral_lattice.html` | ✅ | Batch 5. |
| 28 | signal_rain | `signal_rain/noixzy_signal_rain.html` | ✅ | Batch 5. |
| 29 | echo_contours | `echo_contours/noixzy_echo_contours.html` | ✅ | Batch 5. |
| 30 | magnetic_dust | `magnetic_dust/noixzy_magnetic_dust.html` | ✅ | Batch 5. |
| 31 | neural_lattice | `neural_lattice/noixzy_neural_lattice.html` | ✅ | Batch 5. |
| 32 | flow_field | `flow_field/noixzy_flow_field.html` | ✅ | Batch 5. |
| 33 | reaction_diffusion | `reaction_diffusion/noixzy_reaction_diffusion.html` | ✅ | Batch 5. |
| 34 | voronoi | `voronoi/noixzy_voronoi.html` | ✅ | Batch 4. |
| 35 | contour_field | `contour_field/noixzy_contour_field.html` | ✅ | Batch 4. |
| 36 | truchet | `truchet/noixzy_truchet.html` | ✅ | Batch 4. |
| 37 | truchet_b | `truchet_b/noixzy_truchet_b.html` | ✅ | Batch 4. |
| 38 | l_system | `l_system/noixzy_l_system.html` | ✅ | Batch 4. |
| 39 | cellular_erosion | `cellular_erosion/noixzy_cellular_erosion.html` | ✅ | Batch 4. |
| 40 | recursive_grid | `recursive_grid/noixzy_recursive_grid.html` | ✅ | Batch 4. |
| 41 | wave_interference | `wave_interference/noixzy_wave_interference.html` | ✅ | Batch 4. |
| 42 | stipple | `stipple/noixzy_stipple.html` | ✅ | Batch 4. |
| 43 | agent_swarm_relief | `agent_swarm_relief/noixzy_agent_swarm_relief.html` | ✅ | Batch 4. |
| 44 | catenary_web | `catenary_web/noixzy_catenary_web.html` | ✅ | Batch 5. |
| 45 | hyperbolic_tiling | `hyperbolic_tiling/noixzy_hyperbolic_tiling.html` | ✅ | Batch 5. |
| 46 | origami_fold_field | `origami_fold_field/noixzy_origami_fold_field.html` | ✅ | Batch 5. |
| 47 | phyllotaxis_stack | `phyllotaxis_stack/noixzy_phyllotaxis_stack.html` | ✅ | Batch 5. |
| 48 | quasicrystal_relief | `quasicrystal_relief/noixzy_quasicrystal_relief.html` | ✅ | Batch 5. |
| 49 | reaction_terraces | `reaction_terraces/noixzy_reaction_terraces.html` | ✅ | Batch 5. Dead `edge` PARAMS entry removed (`08f7c99`). |
| 50 | tensegrity_nodes | `tensegrity_nodes/noixzy_tensegrity_nodes.html` | ✅ | Batch 5. |
| 51 | voronoi_tower_field | `voronoi_tower_field/noixzy_voronoi_tower_field.html` | ✅ | Batch 5. |
| 52 | woven_lattice_relief | `woven_lattice_relief/noixzy_woven_lattice_relief.html` | ✅ | Batch 5. |
| 53 | mandelbulb | `mandelbulb/noixzy_mandelbulb.html` | 🔧 | WebGL GLSL raymarcher. PARAMS proposed (14 params: power/morph/detail/glow/ao/spin/dist/elev/pal/bgVal/fmVal/fmSat/rim/bgAlpha). Awaiting implementation sign-off. See `WEBGL_MIGRATION_REPORT.md`. |
| 54 | metafluid | `metafluid/noixzy_metafluid.html` | 🔧 | WebGL GLSL raymarcher. Has inertia drag (mousemove/mouseup + velocity damping). Queued — starts after mandelbulb lands. |
| 55 | gyroid | `gyroid/noixzy_gyroid.html` | 🔧 | WebGL GLSL raymarcher. Orbit camera via azimuth + elevation uniforms. Queued — starts after metafluid lands. |
