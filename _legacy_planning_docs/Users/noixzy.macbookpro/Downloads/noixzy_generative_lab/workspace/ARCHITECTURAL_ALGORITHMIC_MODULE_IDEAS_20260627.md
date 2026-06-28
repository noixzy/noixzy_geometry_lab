# Architectural Algorithmic Module Ideas
# Generated: 2026-06-27

This file extends the existing module planning docs in this project:

- `workspace/NEXT_MODULES.md`
- `workspace/IDEAS_module_expansion.md`
- `workspace/ALGORITHMIC_ARCHITECTURAL_ART.md`
- `algorithmic_art_ideas_sort_20260626.md`
- `algorithmic_art_roadmap_clean_20260626.md`
- `modules.manifest.json`

The live lab already has a strong base of 48-ish modules across fields, tilings, implicit geometry, waves, erosion, growth, glyphs, and SDF forms. The most useful expansion path now is to add modules that feel intentionally architectural: proportion systems, facades, plans, massing, structural diagrams, material surfaces, urban grids, and modernist/brutalist/organic-modern spatial logic.

Note: the prompt says "Frank Lloyd White"; this list interprets that as Frank Lloyd Wright-inspired. These ideas should draw from broad principles like horizontality, organic integration, hearth/core organization, cantilevers, prairie grids, compression/release, and masonry/wood rhythm, not copy specific buildings.

---

## Existing Direction Found

## Already live or strongly represented

- Tiling and grids: `truchet`, `truchet_b`, `hex_grid`, `fractal_tiles`, `recursive_grid`, `grid_extrude`
- Spatial fields: `voronoi`, `contour_field`, `topographic_rings`, `terrain_slice`, `crater_field`
- Mathematical geometry: `gyroid`, `mandelbulb`, `torus_knot`, `lissajous_mesh`, `rose_curve`, `spiral_lattice`
- Simulations and natural systems: `reaction_diffusion`, `cellular_erosion`, `cellular_bloom`, `crystal_growth`, `flow_field`, `vortex_sheet`
- Signal/op-art systems: `moire_field`, `interference_grid`, `wave_interference`, `prism_moire`, `vector_scope`
- Atmosphere and texture systems: `stipple`, `glyph_field`, `signal_rain`, `signal_weave`, `magnetic_dust`, `plasma_membrane`

## Already planned or mentioned in docs

- DLA, differential growth, physarum, Lenia, boids, falling sand
- Fourier epicycles, Julia/Mandelbrot, strange attractors, Apollonian packing
- Space-filling curves, Hitomezashi, Chladni/cymatics, spectrogram terrain
- WFC, Penrose/quasicrystal tiling, Menger sponge, substrate cracks, Voronoi 3D
- Islamic geometric systems, floorplan generation, brick bonds, origami folds, catenary arches

## Expansion gap

The lists are rich in algorithmic art, but less developed in these architectural directions:

- Minimalist composition systems with deliberate negative space
- Modernist proportion, facade, plan, and grid modules
- Brutalist massing, concrete texture, megastructure, and section studies
- Wright-inspired organic-modern modules: prairie horizontals, hearth cores, cantilevers, nested terraces, leaded-glass grids, site contour integration
- Parametric architectural primitives: walls, slabs, stairs, columns, vaults, courtyards, screens, apertures, mullions, brise-soleil, parti diagrams
- Urban morphology: parcels, setbacks, street grids, towers, courtyards, arcades, plazas

---

## Highest-Priority New Modules

These are the best next candidates because they are visually distinct from the current lab, architecturally legible, and feasible as single-file p5/WEBGL modules.

| Priority | Module ID | Style | Why it belongs |
|---|---|---|---|
| 1 | `prairie_grid` | Wright-inspired | Strong horizontal grammar; bridges art, architecture, and pattern. |
| 1 | `brutalist_massing` | Brutalist | Distinct volumetric identity; natural successor to `grid_extrude`. |
| 1 | `modernist_facade` | Minimal / modern | Clean, useful, endlessly variable facade studies. |
| 1 | `courtyard_plan` | Modern / organic | Architectural plan generator with readable spatial logic. |
| 1 | `concrete_relief` | Brutalist | Turns generative fields into cast wall panels and depth maps. |
| 2 | `cantilever_stack` | Wright / modern | Dramatic slab compositions; works as WEBGL or fake-isometric 2D. |
| 2 | `leaded_glass_grid` | Wright-inspired | Ornament that still feels geometric and algorithmic. |
| 2 | `axonometric_city` | Modern / brutalist | Isometric block fields; gallery-friendly and production-useful. |
| 2 | `brise_soleil` | Modern | Kinetic facade screen with light/shadow rhythm. |
| 2 | `site_section` | Organic modern | Contours + architecture; extends terrain/topographic modules. |
| 3 | `megastructure` | Brutalist / metabolist | Larger, stranger, modular architectural fiction. |
| 3 | `modulor_field` | Modernist | Proportion system as art machine. |
| 3 | `coffered_ceiling` | Brutalist / classical-modern | Deep geometric overhead field, good for depth/export. |
| 3 | `parametric_stair` | Minimal / brutalist | Small but iconic architectural generator. |
| 3 | `sacred_modern_plan` | Minimal / Wright | Calm plan/section hybrids with axial and hearth logic. |

---

## Module Idea Bank

## A. Minimalist composition systems

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `minimal_parti` | Abstract architectural parti diagrams using circles, bars, walls, voids, and axes. | void ratio, axis bias, block count, line weight | Great default opener: black/white, one accent, lots of negative space. |
| `quiet_grid` | Sparse orthogonal grid with occasional interruptions, courtyards, and shifted bays. | bay count, deletion rate, offset, stroke hierarchy | A minimalist counterpart to `recursive_grid`. |
| `white_space_field` | Layout engine that composes only a few geometric masses against a large empty ground. | mass count, margin, alignment, tension | Useful for album covers and gallery stills. |
| `monolith_sequence` | Single or repeated slab forms arranged by interval, scale, and shadow. | slab count, spacing, lean, shadow length | Minimal/brutalist crossover. |
| `line_weight_study` | Architectural drawing generator: centerlines, poche, hidden lines, index lines. | scale, hierarchy, hatch density, ghost lines | More drawing-like than painterly. |
| `proportion_bands` | Rectangular bands based on root-2, golden ratio, silver ratio, and modular scales. | ratio system, subdivision depth, accent band, gap | Modernist poster and facade source. |
| `negative_space_tiles` | Tiling system where absence is the main shape. | tile size, void shape, density, jitter | Use 70% empty ground by default. |
| `planar_balance` | Dynamic balance of rectangles and circles using Swiss/modernist composition rules. | grid unit, object count, alignment, asymmetry | Clean, print-ready. |
| `threshold_frames` | Nested frames, apertures, and portals arranged as an abstract spatial procession. | depth count, aperture ratio, offset, glow | Good for motion: slow passage through frames. |
| `single_cut` | One decisive cut through a plane creates two architectural regions. | cut angle, offset, thickness, reveal | Ultra-minimal, very controllable. |

## B. Modernist architecture generators

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `modernist_facade` | Curtain wall, mullions, panels, open windows, and opaque cores. | bay grid, window ratio, panel rhythm, lighting | Clean facade studies; export as texture/displacement. |
| `modulor_field` | Proportion-driven figure/space grid inspired by modernist measurement systems. | scale ratio, human mark, bay rhythm, color accent | Avoid literal Le Corbusier copying; use general proportion logic. |
| `curtain_wall_variations` | Glass facade generator with reflective panels and structural mullions. | mullion spacing, reflectivity, open panels, tint | Could use shader-like gradients for glass. |
| `pilotis_grid` | Columns lift a plane, creating an abstract ground-floor plan. | column spacing, slab thickness, voids, perspective | Works in 2D axonometric or WEBGL. |
| `free_plan` | Walls float independently from structure; plan generator with columns and partitions. | column grid, wall count, openness, poche | Very architectural and readable. |
| `ribbon_window` | Horizontal window bands wrap shifting volumes. | band height, wrap offset, mass count, shadow | Modernist plus Wright-adjacent horizontality. |
| `case_study_shell` | Lightweight post-and-beam house elevation/axonometric generator. | bay count, roof plane, glazing ratio, deck size | Great restrained modern residential module. |
| `miesian_grid` | Perfect structural grid with glass/solid panels and minimal steel lines. | bay size, solid ratio, asymmetry, line hierarchy | High-control minimalist facade. |
| `bauhaus_blocks` | Primary forms and asymmetrical modernist massing. | block count, color restraint, rotation, stacking | Use sparse color, not a toy palette. |
| `sun_path_facade` | Facade panels respond to computed sun angle and shading depth. | sun angle, fin depth, panel tilt, density | Makes brise-soleil logic visual. |
| `open_plan_furniture` | Plan-like composition of walls, rugs, tables, hearths, and circulation voids. | room count, furniture density, circulation, grid | More human-scaled than current modules. |
| `structural_bay` | Repeating beams, columns, trusses, and infill variations. | bay rhythm, beam depth, infill mode, perspective | A practical architectural texture source. |

## C. Brutalist and concrete systems

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `brutalist_massing` | Stacked concrete volumes, voids, setbacks, and cantilevers. | mass count, cantilever, void carve, roughness | Prime WEBGL candidate; direct successor to `grid_extrude`. |
| `concrete_relief` | Cast-concrete wall panel reliefs from grids, noise, and carved channels. | relief depth, joint grid, aggregate noise, bevel | Export-friendly height/displacement map. |
| `board_form_concrete` | Board-formed texture with plank seams, knots, pours, and stains. | plank width, grain, pour lines, weathering | Architectural material generator. |
| `megastructure` | Repeating habitat/service modules in a large brutalist lattice. | module size, span, density, circulation, fog | Can feel like speculative architecture. |
| `habitat_stack` | Modular capsules, terraces, balconies, and cores. | unit count, offset, balcony depth, core size | Metabolist/brutalist crossover. |
| `coffered_ceiling` | Deep square/triangular coffers with perspective shadows. | coffer count, depth, bevel, light angle | Strong geometric depth. |
| `waffle_slab` | Structural slab grid with ribs and penetrations. | rib spacing, rib depth, opening count, perspective | Good bridge to Blender geometry. |
| `béton_topography` | Terrain-like concrete panels with contours, cracks, and aggregate. | contour pitch, crack rate, grain, depth | Connects `topographic_rings` to architecture. |
| `bunker_section` | Cutaway section of earth-sheltered concrete forms. | earth depth, chamber count, wall thickness, light wells | Brutalist plus site/terrain. |
| `void_carver` | Boolean-like subtractive massing: carve courtyards, slots, tunnels, shafts. | mass size, void count, slot ratio, bevel | SDF/raymarch-friendly. |
| `concrete_shadow_boxes` | Array of deep boxes and openings with strong sun shadows. | box grid, opening ratio, depth, sun angle | Beautiful monochrome defaults. |
| `fortress_grid` | Heavy walls, towers, courtyards, and defensive geometries abstracted. | wall thickness, tower count, courtyard, asymmetry | Brutal, monumental, plan/elevation hybrid. |
| `service_core` | Central cores, stair/elevator shafts, ducts, and surrounding floor plates. | core count, plate offset, shaft depth, labels off/on | Architectural diagram as art. |
| `mass_and_void_field` | Alternating solid/void blocks scored by structural stability. | block density, erosion, support bias, shadow | More architectural than random cube stacks. |

## D. Frank Lloyd Wright-inspired / organic-modern systems

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `prairie_grid` | Long horizontal lines, low roof planes, masonry piers, terraces, and landscape bands. | horizon weight, pier rhythm, terrace depth, overhang | Best Wright-inspired first build. |
| `cantilever_stack` | Interlocking horizontal slabs extend from a central core over terrain. | slab count, cantilever length, core mass, contour fit | Great WEBGL/axonometric module. |
| `hearth_plan` | Plan generator organized around a central hearth/core. | core size, room wings, compression, circulation | Captures spatial principle, not specific buildings. |
| `leaded_glass_grid` | Geometric stained/leaded glass patterns from rectilinear subdivisions and accents. | subdivision, symmetry, accent ratio, line weight | Wright-adjacent ornament; exportable SVG. |
| `organic_site_plan` | Building wings grow along contour lines and tree/rock avoidance zones. | contour strength, wing count, site obstacles, terrace | Bridges topography and plan generation. |
| `low_roofline` | Elevation generator with deep eaves, compressed entries, and layered roof planes. | eave depth, roof layers, pier spacing, shadow | Quiet but very distinctive. |
| `textile_block` | Repeating relief blocks with geometric perforation and casting variation. | block size, perforation, relief depth, weathering | Organic-modern/block architecture. |
| `usonian_module` | Affordable modular house plan logic: grid, core, carport, terrace, garden. | grid unit, wing length, carport, garden court | A warm modern plan module. |
| `compression_release` | Spatial sequence diagram: narrow/dark entry opens into wide/light room. | compression, reveal size, path curve, glow | Abstract but architectural. |
| `masonry_rhythm` | Brick/stone piers and horizontal bands with varied coursing. | course height, pier spacing, stone jitter, shadow | Material-forward and restrained. |
| `waterfall_terraces` | Terraces and slab edges respond to falling contour/water lines. | terrace count, water path, cantilever, rock mass | Inspired by site-integration principles, not a replica. |
| `prairie_window_band` | Window bands, mullions, screens, and piers in long horizontal composition. | bay rhythm, glass ratio, pier weight, glow | Could pair with `leaded_glass_grid`. |
| `landscape_hearth` | Abstract core emits bands, paths, terraces, and planting fields. | core heat, band count, path bend, plant density | Plan/elevation hybrid. |
| `tree_column_canopy` | Branching supports become roof/canopy grids. | branch count, canopy span, column taper, openness | Organic architecture bridge to `l_system`. |

## E. Facades, screens, apertures

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `brise_soleil` | Repeating fins rotate by light, wave, or audio input. | fin count, tilt, depth, sun angle | Excellent motion module. |
| `perforated_screen` | Parametric perforation facade with gradients, image sampling, or noise. | hole size, spacing, gradient, thickness | Modern, Islamic, or brutalist depending palette. |
| `mashrabiya_modern` | Geometric lattice screen with modern simplified star/rectilinear patterns. | pattern order, aperture, screen depth, light | Avoid over-ornament; make it architectural. |
| `mullion_drift` | Window mullion grid subtly drifts, breaks, and recombines. | grid pitch, drift, break rate, hierarchy | Minimal but alive. |
| `aperture_field` | Wall openings generated by light, view, privacy, and rhythm scores. | view bias, opening size, privacy, wall depth | Architectural logic beyond random holes. |
| `light_well` | Top-lit shafts and courtyards projected in plan/section. | shaft count, depth, light angle, haze | Could be moody and spatial. |
| `shadow_louver` | Louver fields cast layered shadows onto a backing plane. | louver pitch, rotation, shadow softness, wind | Motion-friendly, modern. |
| `facade_weathering` | Rain streaks, mineral deposits, soot, and panel discoloration. | streak length, stain rate, panel grid, age | Pair with brutalist/concrete systems. |
| `panelization_solver` | Optimizes a surface into buildable panels with seams and tolerance marks. | panel size, seam width, irregularity, labels | Feels like architectural fabrication. |
| `window_light_map` | Night facade with occupancy/lights pattern and floor rhythm. | lit ratio, flicker, floor count, color temp | City/modernist output. |

## F. Plans, sections, circulation

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `courtyard_plan` | Courtyard-building generator using rings, bars, courts, and thresholds. | court count, ring thickness, entries, garden ratio | Strong architectural identity. |
| `floorplan_bsp` | Binary-space-partition room plans with walls, doors, corridors. | split depth, room ratio, corridor width, door count | Already mentioned generally; make it lab-specific. |
| `gallery_plan` | Museum/gallery plan with rooms arranged around sightlines and circulation loops. | room count, sightline, loop strength, wall thickness | Fitting for art lab context. |
| `section_cut` | Building section generator with floors, stairs, shafts, terrain, and light. | floor count, cut depth, stair logic, terrain | Distinct from top-down plan modules. |
| `circulation_loop` | Paths organize spaces as loops, spines, branches, or spirals. | path type, room density, width, compression | Can generate abstract diagrams or plans. |
| `stair_core` | Parametric stair, landings, rail rhythm, and shadows. | rise/run, turns, width, landing count | A crisp architectural object module. |
| `ramp_spiral` | Continuous ramp field wrapping courtyards, voids, or towers. | radius, slope, turns, opening | Modern museum/parking-structure energy. |
| `threshold_map` | Doors, gates, portals, walls, and nested transitions. | threshold count, wall thickness, privacy gradient, axis | Good for plan diagrams. |
| `served_servant_plan` | Large open rooms contrasted with compact service cores. | service ratio, core position, bay grid, openness | Modern architectural planning principle. |
| `poche_generator` | Thick black wall/void drawings in plan and section. | wall thickness, room carve, hatch, hierarchy | Beautiful monochrome architectural drawings. |

## G. Structural and tectonic modules

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `truss_field` | Parametric truss webs: Warren, Pratt, Vierendeel, random hybrids. | span, web type, depth, stress color | Strong linear architecture module. |
| `space_frame` | 3D lattice of nodes and struts with perspective/depth. | grid size, node jitter, missing members, rotation | Bridges `neural_lattice` and architecture. |
| `tensegrity_field` | Compression bars and tension cables in balanced diagrams. | bar count, cable tension, spread, rotation | Already mentioned broadly; make visually iconic. |
| `rib_vault` | Gothic/modern rib vault curves projected as plan or 3D ceiling. | bay count, arch height, rib density, symmetry | Historic logic with modern abstraction. |
| `catenary_arch` | Hanging-chain/catenary families as arches and shells. | span, sag, thickness, array count | Minimal and structural. |
| `shell_structure` | Thin-shell surfaces from sine, paraboloid, hyperbolic paraboloid forms. | curvature, grid, thickness, light | Modern structural expression. |
| `folded_plate` | Origami-like folded concrete/metal roof planes. | fold count, ridge angle, depth, light | Extends existing `fold` toward architecture. |
| `diagrid_tower` | Tower facade/structure using diagonal grids. | height, taper, diagonal pitch, openness | Modern high-rise generator. |
| `buttress_system` | External supports and load paths abstracted into rhythmic fins. | thrust, spacing, height, mass | Brutalist/gothic hybrid. |
| `load_path` | Visualizes forces through columns, beams, walls, and foundations. | load count, gravity, support spacing, color | Algorithmic structural art. |

## H. Urbanism and landscape architecture

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `axonometric_city` | Isometric city blocks with height, setbacks, courtyards, streets. | block count, height rule, street width, shadow | Great gallery module. |
| `urban_parcels` | Parcel subdivision from roads, setbacks, and zoning envelopes. | road density, parcel size, setback, FAR | Architectural/urban generator. |
| `modernist_superblock` | Towers in park, slabs, plazas, paths, and landscape fields. | tower count, slab length, park ratio, path curves | Modernist planning as pattern. |
| `brutalist_campus` | Heavy connected blocks, plazas, bridges, and sunken courts. | mass count, bridge density, plaza size, level changes | Distinct urban/brutalist vibe. |
| `garden_city_radial` | Radial/belt city diagrams with green wedges and civic centers. | rings, spokes, green ratio, density | Diagrammatic but beautiful. |
| `topographic_settlement` | Buildings grow along contour-safe terraces. | contour pitch, building density, slope limit, paths | Excellent bridge to existing terrain modules. |
| `desire_paths` | Paths emerge from agents crossing a site. | agent count, destinations, erosion, path width | Simulation plus landscape design. |
| `plaza_field` | Paving grids, benches, trees, fountains, and shade fields. | paving unit, object density, shade, axis | Human-scale outdoor architecture. |
| `street_canyon` | Facade walls and perspective street sections with light/shadow. | street width, building height, sun, signage off/on | Cinematic urban stills. |
| `infrastructure_map` | Bridges, viaducts, rail, canals, ducts as abstract network forms. | network density, span, hierarchy, curvature | Architecture meets systems art. |

## I. Ornament, pattern, and material systems

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `girih_modern` | Simplified girih/star polygon tiling with modern line hierarchy. | star order, subdivision, gap, accent | Already mentioned as Islamic geometry; this is a clean module direction. |
| `penrose_facade` | Penrose/quasicrystal logic converted into panels/windows. | inflation, panel depth, color rule, aperture | Architecturalizes Penrose. |
| `brick_bond_lab` | Flemish, English, running, stack, herringbone, basketweave bonds. | bond type, brick size, mortar, weathering | Very useful texture generator. |
| `stone_coursing` | Irregular ashlar, random rubble, stacked stone wall generator. | stone size, coursing, mortar, roughness | Wright/brutalist material adjacency. |
| `tile_glaze_field` | Ceramic tile with glaze variation, crackle, grout, and defects. | tile size, glaze noise, crackle, grout | Works for modern interiors. |
| `terrazzo_seed` | Aggregate chips embedded in field, with polishing/specular cues. | chip density, chip size, color mix, polish | Modern material system. |
| `acoustic_panel` | Slotted/perforated acoustic wall panels. | slot pitch, depth, waveform, absorption gradient | Algorithmic and architectural. |
| `hatch_library` | Section hatches for concrete, earth, insulation, glass, steel, wood. | hatch type, scale, density, angle | Architectural drawing texture module. |
| `screen_block` | Breeze-block/perforated masonry patterns. | block pattern, aperture, bevel, light angle | Modern/brutalist facade detail. |
| `ornament_reduced` | Traditional ornament reduced to modern parametric lines. | motif source, simplification, repeat, line weight | Keeps ornament without becoming decorative clutter. |

## J. 3D / WEBGL architectural showpieces

| Module ID | Concept | Key controls | Output / notes |
|---|---|---|---|
| `sdf_architecture` | Raymarched building-like SDF: boxes, cylinders, arches, boolean voids. | primitive count, smoothness, subtraction, camera | Architectural cousin of `sdf_raymarch`. |
| `raymarched_megastructure` | Infinite modular concrete lattice with fog and soft shadows. | cell size, repetition, void rule, fog | Flagship brutalist/liminal piece. |
| `parametric_pavilion` | Lightweight pavilion generated from columns, roof surface, screens. | column count, roof curvature, screen density, openness | Modern architectural object. |
| `hypar_roof` | Hyperbolic paraboloid roof mesh with ribs and shadow. | saddle, rib count, twist, material | Clean structural 3D. |
| `cantilever_house` | Abstract house mass on terrain, with slabs and core. | terrain, slab count, cantilever, glazing | Wright-inspired/modern showpiece. |
| `concrete_tower` | Stack of floor plates, cores, balconies, and facade grids. | floor count, taper, balcony pattern, weathering | Brutalist high-rise generator. |
| `interior_lightwell` | Procedural interior void with floors, railings, shaft light. | floor count, void size, light angle, haze | Atmospheric but architectural. |
| `architectural_boolean` | Live boolean-like cuts through solids to create diagrams/objects. | cube count, cutter count, bevel, reveal color | Very satisfying interactive module. |
| `sectional_model` | White/gray architectural model style: terrain + cut building mass. | scale, floor plates, terrain, cut plane | A clean "model photography" visual. |
| `voxel_archipelago` | Voxel islands/towers connected by bridges and terraces. | island count, bridge rate, height, erosion | Brutalist fantasy but still geometric. |

---

## K. Newly Added Batch 12 (Escrow)

These modules have now been prototyped in the escrow shell as a focused architectural/mathematical expansion set:

- `noixzy_minimal_parti`
- `noixzy_quiet_grid`
- `noixzy_white_space_field`
- `noixzy_modulor_field`
- `noixzy_brise_soleil`
- `noixzy_aperture_field`
- `noixzy_section_cut`
- `noixzy_load_path`
- `noixzy_shadow_louver`
- `noixzy_service_core`

These fill the previously underrepresented design territory of:

- minimalist negative-space composition systems
- facade shading and aperture logic
- section/cut architectural drawing systems
- structural force tracing diagrams
- served/servant core-plate organization

---

## L. Next 10 Suggested Unexplored Modules

To continue the 10-at-a-time cadence with minimal overlap, the next strongest unexplored batch is:

1. `noixzy_courtyard_plan`
2. `noixzy_light_well`
3. `noixzy_mashrabiya_modern`
4. `noixzy_poche_generator`
5. `noixzy_threshold_map`
6. `noixzy_screen_block`
7. `noixzy_diagrid_tower`
8. `noixzy_parametric_pavilion`
9. `noixzy_street_canyon`
10. `noixzy_panelization_solver`

Recommended emphasis for the next cycle:

- keep simulation light, structure clear, and controls broad enough for stage-to-module translation
- prioritize modules that output both image-friendly stills and diagram-like readability

---

## M. Newly Added Batch 13 (Escrow)

These modules have now been prototyped in the escrow shell as the next unexplored architectural systems set:

- `noixzy_courtyard_plan`
- `noixzy_light_well`
- `noixzy_mashrabiya_modern`
- `noixzy_poche_generator`
- `noixzy_threshold_map`
- `noixzy_screen_block`
- `noixzy_diagrid_tower`
- `noixzy_parametric_pavilion`
- `noixzy_street_canyon`
- `noixzy_panelization_solver`

These extend the escrow with:

- plan-first spatial logics (courtyard, threshold, poche)
- facade/screen tectonics (mashrabiya, block, panelization)
- structural and urban section systems (diagrid tower, street canyon)
- pavilion-scale lightweight architectural forms

## N. Next 10 Suggested Unexplored Modules (Batch 14)

To continue the cadence with minimal overlap, the next strongest queue is:

1. `noixzy_prairie_grid`
2. `noixzy_cantilever_stack`
3. `noixzy_leaded_glass_grid`
4. `noixzy_axonometric_city`
5. `noixzy_site_section`
6. `noixzy_megastructure`
7. `noixzy_coffered_ceiling`
8. `noixzy_parametric_stair`
9. `noixzy_sacred_modern_plan`
10. `noixzy_hypar_roof`

---

## Style-Specific Build Notes

## Minimalist

- Default to few elements, strong margins, and black/white/one-accent palettes.
- Avoid filling the canvas. Negative space should be a first-class parameter.
- Use line hierarchy: construction lines, primary lines, poche, shadow.
- Best module candidates: `minimal_parti`, `quiet_grid`, `white_space_field`, `single_cut`, `proportion_bands`.

## Modern

- Lean on rational grids, structural bays, curtain walls, pilotis, open plans, facade panelization, and sun logic.
- Use restrained materials: glass, steel, concrete, warm wood, white planes.
- Add "drawing mode" and "render mode" toggles where possible.
- Best candidates: `modernist_facade`, `free_plan`, `curtain_wall_variations`, `brise_soleil`, `structural_bay`.

## Brutalist

- Make mass, void, depth, and shadow do the talking.
- Use concrete grain, board-form seams, weathering, bevels, occlusion, and hard sunlight.
- Prefer 3D/axonometric/sectional modules over flat decorative patterns.
- Best candidates: `brutalist_massing`, `concrete_relief`, `board_form_concrete`, `megastructure`, `coffered_ceiling`.

## Wright-inspired / organic modern

- Emphasize horizontality, hearth/core, terraces, overhangs, masonry rhythm, site integration, and compression/release.
- Use warm neutrals, stone/wood/concrete, muted glass accents, and long shadow bands.
- Keep it principle-based, not a replica generator.
- Best candidates: `prairie_grid`, `hearth_plan`, `cantilever_stack`, `leaded_glass_grid`, `organic_site_plan`.

---

## Suggested First Build Batch

Build these 8 as a cohesive architectural installment:

1. `prairie_grid` — 2D, Wright-inspired horizontal composition/pattern.
2. `brutalist_massing` — WEBGL or axonometric 2D, concrete block/void generator.
3. `modernist_facade` — 2D facade engine with mullions, panels, lights, and shadow.
4. `courtyard_plan` — 2D plan generator with poche and garden courts.
5. `concrete_relief` — 2D height/depth map for cast wall panels.
6. `cantilever_stack` — 2.5D slabs and core over contour/site lines.
7. `brise_soleil` — animated facade fins driven by sun/audio/wave.
8. `axonometric_city` — isometric urban block field with setbacks and shadows.

## Suggested Second Build Batch

1. `leaded_glass_grid`
2. `free_plan`
3. `coffered_ceiling`
4. `board_form_concrete`
5. `site_section`
6. `void_carver`
7. `perforated_screen`
8. `space_frame`

---

## Shared Parameters For Architecture Modules

Most architecture modules should share these controls when possible:

- `seed`: deterministic reroll
- `palette`: existing lab palette system
- `scale`: grid/site/building scale
- `density`: amount of geometry/detail
- `void_ratio`: how much space is carved away
- `line_hierarchy`: drawing weight system
- `depth`: relief or extrusion amount
- `sun_angle`: shadow direction
- `shadow_softness`: graphic vs atmospheric rendering
- `material`: concrete/glass/stone/wood/ink mode
- `weathering`: age, stains, patina, grain
- `axonometric`: flat plan/elevation vs 2.5D projection
- `export_mode`: beauty PNG, height map, SVG/drawing, or Blender-friendly map

---

## Implementation Fit With Current Lab

- 2D p5 modules should follow the existing standalone pattern: `module_id/noixzy_module_id.html`.
- WEBGL modules should reuse the orbit/camera idioms from `gyroid`, `mandelbulb`, `torus_knot`, `metafluid`, and `sdf_raymarch`.
- Drawing/plan modules should support SVG export eventually.
- Material modules should export height/displacement maps for Blender.
- Facade/plan/city modules should include a "drawing mode" that disables glow/grain and uses clean architectural line weights.
- Brutalist modules should include high-contrast shadows and ambient occlusion-like darkening by default.
- Wright-inspired modules should include site/contour options so they do not become simple decorative grids.

