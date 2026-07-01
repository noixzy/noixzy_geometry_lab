# Studio Backdrop Audit

All 55 modules assessed for use as studio backdrops (live or static) in a broadcast/photo-studio context.

> **Note (2026-07-01):** the manifest now has 57 modules. The assessment below covers the 55 modules present at audit time and has not been extended to the 2 added since.

**Render types:**
- `2D canvas` — p5.js Canvas 2D, CPU-only, low cost
- `WebGL GLSL` — GLSL raymarcher/raytracer, GPU, moderate cost

**Backdrop recommendations:**
- `live 3D` — true WebGL 3D with orbit camera; best choice for a dynamic studio backdrop with shell-driven camera
- `static` — strong centered subject with open dark canvas around it; usable as a printed or looping-still backdrop
- `borderline` — only viable at specific low-density/low-depth param settings; not reliable as a general backdrop
- `skip` — full-field pattern fills canvas edge-to-edge; backdrop would be invisible behind subject

**BG note (all 2D modules):** Every module has a `bgAlpha` toggle. When active, the canvas becomes transparent and CSS behind the iframe shows through. However, most modules call `g.background(pal[0])` at the start of every render, which paints the canvas opaque unless the bgAlpha bridge flag suppresses it. The notes below reflect default/typical rendering.

---

## Modules 1–11

| # | Module | Render | Camera | BG Treatment | Visual fit | Backdrop rec | Cost note |
|---|--------|--------|--------|-------------|-----------|-------------|-----------|
| 1 | grid_extrude | 2D canvas | fixed | Dark bg + stacked grid layer fill | Extruded grid fills canvas at any useful layer count; the stacking is a depth illusion, not a 3D object | **skip** | Grid tiles cover canvas; no open ground |
| 2 | brutalist_massing | 2D canvas | fixed | Dark gradient (`#101010` → `#020202`), ground plane drawn first, then buildings | Isometric building massing — 1–3 discrete tower forms on a ground plane; significant dark sky above; clearly a centered subject floating on void | **static** | Most subject-like of all 2D modules. Pan/zoom/dolly mouse interaction adds some dynamic quality. Dark gradient bg reads as studio floor. |
| 3 | triangulated_signal_mesh | 2D canvas | fixed | Solid bg fill per frame; bgAlpha supported | Triangulated signal mesh — dense edge network distributed across canvas | **skip** | Edge network fills canvas edge-to-edge |
| 4 | mandelbulb | WebGL GLSL | orbit (azimuth param, `_camAzimuth`) | Dark void shader bg; fog/glow in GLSL | Raymarched 3D Mandelbulb fractal object; isolated self-similar 3D form against void; azimuth rotates it | **live 3D** | Premier live-3D backdrop candidate. Rich surface detail, dramatic depth. Moderate GPU (single raymarching object). |
| 5 | metafluid | WebGL GLSL | orbit (inertia drag — mousemove/mouseup + velocity damping) | Dark void shader bg | Raymarched metaball/fluid surface; organic blobby 3D form with inertia-driven camera; drag can be driven from shell via synthetic events | **live 3D** | Second live-3D candidate. Fluid/organic feel contrasts with Mandelbulb's crystalline. Inertia makes it feel physically alive. |
| 6 | moire_field | 2D canvas | fixed | Solid bg fill per frame; bgAlpha supported | Full-field moiré interference (46–210 line density); covers entire canvas by definition | **skip** | Moiré is spatially exhaustive |
| 7 | particle_orbitals | 2D canvas | fixed | Solid pal[0] fill per frame + ADD blend | Centered orbital ring system (`baseR` = 70–46% of canvas half); at moderate radius, rings float in the center third of canvas with dark surround | **static** | Clean centered subject with generous dark field. Ring trails glow on black. Works well as a looping still or subtle animation. Low 2D cost. |
| 8 | radial_noise | 2D canvas | fixed | Brightened pal[0] fill per frame; bgAlpha supported | Concentric noisy rings radiating from center; rings extend outward and at high count may reach canvas edge | **borderline** | At low ring count, sparse rings float on dark bg. At higher counts, rings fill toward edge. Only viable at low ring settings. |
| 9 | kaleidoscope_field | 2D canvas | fixed | Brightened pal[0] fill + ADD blend | Kaleidoscope disk, max radius 0.58×min(W,H)/2; low-signal cells skip render (`if v<0.12 continue`) — leaves dark gaps between wedges and outside disk | **static** | Centered disk subject with natural dark border and dark inter-wedge gaps. Mandala quality. Works as a strong static backdrop with good compositional weight. |
| 10 | topographic_rings | 2D canvas | fixed | Brightened pal[0] fill + radial gradient (center bright, fades to 0 at r=0.58) | Concentric topographic ring system with built-in radial fade; rings naturally dim toward canvas edge | **static** | Self-framing centered subject — the radial gradient does the vignetting. Feels like a radar or target. Reliable as static backdrop at any ring count. |
| 11 | ribbon_flow | 2D canvas | fixed | Solid pal[0] fill per frame + ADD blend | Ribbon filaments distributed across canvas via lane system; covers full canvas width | **skip** | Ribbon lanes span canvas edge-to-edge |

---

## Modules 12–33

All entries: Canvas 2D (p5.js), fixed camera, per-frame `g.background(pal[0])`, bgAlpha toggle present.

| # | Module | Render | Camera | BG Treatment | Visual fit | Backdrop rec | Cost note |
|---|--------|--------|--------|-------------|-----------|-------------|-----------|
| 12 | glyph_field | 2D canvas | fixed | Solid pal[0] fill per frame | Glyphs distributed across full canvas with z-depth layer scaling — covers edge-to-edge | **skip** | Canvas fully covered; backdrop hidden under glyph grid |
| 13 | crystal_growth | 2D canvas | fixed | Solid pal[0] fill per frame | Branching crystal tree growing outward from seeds — fills canvas at typical density | **skip** | Branches cover canvas |
| 14 | vector_scope | 2D canvas | fixed | Solid pal[0] fill per frame + ADD blend | Layered lissajous/scope loops centered at canvas mid — traces overlap and fill with glow | **skip** | Concentric glow traces fill canvas |
| 15 | wave_lattice | 2D canvas | fixed | Brightened pal[0] fill per frame | Dense wave grid (14–58 lines), full canvas coverage at all densities | **skip** | Wave grid is edge-to-edge by design |
| 16 | fractal_tiles | 2D canvas | fixed | Solid pal[0] fill per frame | Recursive tile subdivision — fills the plane | **skip** | Tiling covers entire canvas |
| 17 | plasma_membrane | 2D canvas | fixed | Solid pal[0] fill per frame | Organic cell forms, Voronoi-like bubbles across canvas | **skip** | Membrane fills canvas |
| 18 | interference_grid | 2D canvas | fixed | Solid pal[0] fill per frame | Grid interference moiré — edge-to-edge raster pattern | **skip** | Pattern is mathematically full-field |
| 19 | cellular_bloom | 2D canvas | fixed | Solid pal[0] fill per frame | Cellular growth bloom — spreads to fill canvas over time | **skip** | Coverage by design |
| 20 | vortex_sheet | 2D canvas | fixed | Brightened pal[0] fill + ADD blend | Vortex filaments swept across full canvas | **skip** | Filaments span canvas width; ADD glow fills dark areas |
| 21 | prism_moire | 2D canvas | fixed | Solid pal[0] fill per frame | Prismatic angular moiré — full-field interference pattern | **skip** | Pattern is full-canvas by construction |
| 22 | terrain_slice | 2D canvas | fixed | Brightened pal[0] fill per frame | Stacked horizontal contour slices, 9–42 layers spanning full width | **skip** | Slices span edge-to-edge |
| 23 | signal_weave | 2D canvas | fixed | Solid pal[0] fill per frame | Dense interlocking woven signal paths across canvas | **skip** | Weave pattern fills canvas |
| 24 | crater_field | 2D canvas | fixed | Brightened pal[0] fill per frame | Crater/impact-ring field distributed across canvas (52–120 craters) | **skip** | Too dense for backdrop to read |
| 25 | spiral_lattice | 2D canvas | fixed | Brightened pal[0] fill + ADD blend | Spiral arms (3–12) radiating from center; at minimum arm count, inter-arm gaps exist | **borderline** | At low arm count + bgAlpha, backdrop visible between arms. Not compelling enough to recommend by default. |
| 26 | signal_rain | 2D canvas | fixed | Solid pal[0] fill per frame | Vertical rain columns distributed across full canvas | **skip** | Rain columns cover canvas at any useful density |
| 27 | echo_contours | 2D canvas | fixed | Brightened pal[0] fill + ADD blend | Concentric expanding rings from 1–3 centers, multiple echoes | **skip** | Rings fill the plane at any non-trivial ring count |
| 28 | magnetic_dust | 2D canvas | fixed | Solid pal[0] fill per frame | Magnetic field particle simulation — particles + field lines distributed across canvas | **skip** | Field lines + dust fill canvas |
| 29 | neural_lattice | 2D canvas | fixed | Solid pal[0] fill + ADD blend | Node-link network; at very low node density, network is sparse with open gaps | **borderline** | Sparse network at extreme low density + bgAlpha. Links fill gaps quickly at moderate density — not reliable. |
| 30 | flow_field | 2D canvas | fixed | Solid pal[0] fill per frame | Perlin-noise flow field — streamlines cover full canvas | **skip** | Streamlines fill edge-to-edge |
| 31 | reaction_diffusion | 2D canvas | fixed | Solid pal[0] fill per frame | Gray-Scott RD simulation renders every pixel | **skip** | Pixel-level simulation; full coverage |
| 32 | voronoi | 2D canvas | fixed | Solid pal[0] fill per frame | Voronoi tessellation fills entire canvas | **skip** | Tessellation is spatially exhaustive |
| 33 | contour_field | 2D canvas | fixed | Solid pal[0] fill per frame | Noise-based contour/isoline field — lines span full canvas | **skip** | Isoline coverage is edge-to-edge |

---

## Modules 34–55

All 2D canvas entries: fixed camera, per-frame `g.background(pal[0])`, bgAlpha toggle present.

| # | Module | Render | Camera | BG Treatment | Visual fit | Backdrop rec | Cost note |
|---|--------|--------|--------|-------------|-----------|-------------|-----------|
| 34 | truchet | 2D canvas | fixed | Solid pal[0] fill per frame | Arc-tile tessellation (6–40 tiles), z-depth row scaling — fills entire canvas | **skip** | Tile grid is spatially exhaustive |
| 35 | truchet_b | 2D canvas | fixed | Solid pal[0] fill per frame | Variant-B truchet — same tile-fill structure, alternate arc orientation | **skip** | Same as truchet; covers canvas edge-to-edge |
| 36 | l_system | 2D canvas | fixed | Solid pal[0] fill per frame | L-system tree branching upward from `baseY = 0.9H`; at low depth (3–4) the tree is a clean isolated subject | **borderline** | At depth ≤ 0.4, the tree reads as a centered subject with open space. Usable as static if param-locked to low depth. Not reliable as a general backdrop. |
| 37 | cellular_erosion | 2D canvas | fixed | Solid pal[0] fill per frame | Cellular automaton erosion — per-pixel simulation fills entire canvas | **skip** | Pixel-level simulation; full coverage |
| 38 | recursive_grid | 2D canvas | fixed | Solid pal[0] fill per frame | Recursive quad-tree subdivision — fills canvas by partitioning the plane | **skip** | Subdivision always covers full canvas |
| 39 | wave_interference | 2D canvas | fixed | Solid pal[0] fill per frame | Standing wave interference — full-canvas raster field | **skip** | Interference is edge-to-edge |
| 40 | stipple | 2D canvas | fixed | Solid pal[0] fill per frame | Dot stipple field; at very low density, isolated dots on black | **borderline** | Technically open canvas at extreme low density. Dots read as noise rather than a compositional subject. Weak backdrop candidate. |
| 41 | hex_grid | 2D canvas | fixed | Solid black bg per frame | Hex grid with ripple/glow (hexR 16–80 px) — grid tiles fill entire canvas | **skip** | Hexagonal tessellation covers canvas |
| 42 | rose_curve | 2D canvas | fixed | Solid-color trail-fade bg; bgAlpha supported | Rose curve `R = min(W,H)×0.45×P.scale`; at scale < 1, centered petal curves clearly contained on dark canvas | **static** | Clean centered subject with controlled radius. Trail glow on black looks polished. Scale param constrains subject. Recommend as primary static candidate for 2D family. |
| 43 | lissajous_mesh | 2D canvas | fixed | Solid-color trail-fade bg; bgAlpha supported | Lissajous mesh (`rx = 0.44W`) reaches ~88% canvas width at any trace count | **skip** | Curves fill the canvas at any useful trace count |
| 44 | torus_knot | WebGL GLSL | orbit (azimuth param, `_camAzimuth`) | Dark/gradient shader bg; GLSL fog | Raymarched torus knot in 3D space; true isolated 3D object against void; azimuth drives rotation | **live 3D** | Clean isolated 3D subject. Already in the gold-standard set. Moderate GPU (single raymarching object). |
| 45 | agent_swarm_relief | 2D canvas | fixed | Solid pal[0] fill + ADD blend | Agent swarm paths with `fract()` wrapping — paths tile seamlessly across entire canvas | **skip** | Wrapping ensures full canvas coverage |
| 46 | catenary_web | 2D canvas | fixed | Solid pal[0] fill per frame | Catenary arches (4–22) spanning full canvas width + vertical ribs | **skip** | Arches span W edge-to-edge |
| 47 | gyroid | WebGL GLSL | orbit (azimuth + elevation uniforms) | Dark void shader bg | Raymarched gyroid minimal surface; continuous 3D structure fills the render volume; azimuth/elevation drive orbit | **live 3D** | Immersive 3D surface — best used at high bgAlpha transparency for a "looking into a world" effect. Moderate GPU cost. |
| 48 | hyperbolic_tiling | 2D canvas | fixed | Solid pal[0] fill + ADD blend | Concentric rings + geodesic arcs, max radius 0.48 of canvas half — entire pattern contained in a centered disk; canvas corners are dark | **static** | Strong centered-disk subject with ADD glow. Dark corners naturally frame it. Works as a static art-poster backdrop. Low 2D cost. |
| 49 | origami_fold_field | 2D canvas | fixed | Solid pal[0] fill per frame | 86×86 rasterized origami fold field — every pixel classified, fills canvas | **skip** | Full-canvas pixel raster |
| 50 | phyllotaxis_stack | 2D canvas | fixed | Solid pal[0] fill per frame | Phyllotaxis seed spiral, max `rr = 0.48` of canvas half — tight centered circular arrangement; dark canvas outside the disk | **static** | Cleanest circular subject in the lab. Golden-angle spiral reads instantly as a unified form. Generous dark canvas around it. Strongly recommended for static backdrop. Low 2D cost. |
| 51 | quasicrystal_relief | 2D canvas | fixed | Solid pal[0] fill per frame | Threshold-gated dot field across full canvas; threshold controls density but canvas scan is full-field | **skip** | Covers canvas at any useful threshold |
| 52 | reaction_terraces | 2D canvas | fixed | Solid pal[0] fill per frame | 96×96 rasterized RD terrace field — fills entire canvas | **skip** | Full-canvas pixel raster |
| 53 | tensegrity_nodes | 2D canvas | fixed | Solid pal[0] fill per frame | Node-strut network distributed across canvas; covers canvas at any useful node count | **skip** | Canvas-filling network |
| 54 | voronoi_tower_field | 2D canvas | fixed | Solid pal[0] fill per frame | Voronoi cell grid (28–78 res), all cells filled — complete tessellation | **skip** | Tessellation is spatially exhaustive |
| 55 | woven_lattice_relief | 2D canvas | fixed | Solid pal[0] fill per frame | 92×92 woven pixel grid with low threshold — near-full coverage at all useful settings | **skip** | Near-full coverage |

---

## Summary

| Tier | Count | Modules |
|------|-------|---------|
| **live 3D** | 4 | mandelbulb (4), metafluid (5), torus_knot (44), gyroid (47) |
| **static** | 7 | brutalist_massing (2), particle_orbitals (7), kaleidoscope_field (9), topographic_rings (10), rose_curve (42), hyperbolic_tiling (48), phyllotaxis_stack (50) |
| **borderline** | 5 | radial_noise (8), spiral_lattice (25), neural_lattice (29), l_system (36), stipple (40) |
| **skip** | 39 | all others |

**Top picks for immediate use:**
1. `phyllotaxis_stack` — most self-contained circular subject, works at any palette
2. `mandelbulb` — live 3D, richest surface, most dramatic
3. `kaleidoscope_field` — mandala quality, natural dark border
4. `rose_curve` — elegant centered curves, easy to tune via scale param
5. `torus_knot` — already gold-standard; reliable live 3D with shell orbit control
