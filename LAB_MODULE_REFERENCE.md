# noixzy Lab — Module Reference for Blender MCP

**Author:** Chris Tucker  
**Purpose:** Per-module geometry descriptions for use as FORM SOURCE seeds in Blender MCP prompts. Each entry names the primary algorithm and what makes the form visually distinct.

---

## Hand-Authored

Modules with bespoke rendering pipelines — unique geometry logic not shared with the engine framework.

---

### grid_extrude

Recursive noise-gated quad-tree subdivision divides the canvas into cells of varying sizes, each rendered as an isometrically extruded block with a three-pass metallic/roughness/sheen lighting model. A `depth` parameter drives layer stacking — the full grid is ghosted 1–4 times at increasing Y offsets and decreasing opacity. Distinctive for its hard-cornered cuboid relief that reads as cast metal or circuit board topography.

---

### flow_field

Thousands of particles stream along a noise vector field — each path follows `noise(x·s, y·s, t·speed) · TWO_PI · turbulence`, drawn as curveVertex splines with additive blending. Density, scale, and turbulence independently control stroke count, field grain, and directional chaos. Reads as luminous fiber bundles or brushed metal grain in continuous motion.

---

### rose_curve

Draws polar rose curves `r = cos(n/d · θ)` in multiple rotating and counter-rotating layers with independent speed and phase offsets. Overlapping layers produce interference moiré as petal counts and rotation rates shift. Reads as hypnotic crystalline mandala with breathing, interference-driven symmetry.

---

### lissajous_mesh

Parametric Lissajous figures — `x = sin(a·θ + phase)`, `y = sin(b·θ)` — drawn as connected mesh grids across multiple simultaneous curves. A drift parameter slowly mutates the phase relationship, causing the knotted forms to slip in and out of closed harmonics. Reads as a taut, woven line cage whose topology continuously deforms.

---

### gyroid

GLSL raymarched gyroid isosurface — `sin(x)cos(y) + sin(y)cos(z) + sin(z)cos(x) = 0` — phase-animated with a `shell` thickness parameter and clipped by a bounding sphere. The form is a triply periodic minimal surface with no flat faces: all geometry is saddle-curved tunnels and passages. Distinctive for its continuous, labyrinthine interior topology.

---

### mandelbulb

GLSL raymarched 3D Mandelbulb fractal — power parameter `pw = mix(2, 10, u_power) + sin(t·0.31)·morph·2.5` drives orbit-trap distance estimation with glow accumulated along the escape-time boundary. At high power, the surface reads as a spiky, tentacled orb; at lower power it collapses toward a smooth sphere. The animated morph parameter causes the bulbs to breathe and unfurl in real time.

---

### metafluid

GLSL raymarched metaball/fluid isosurface — multiple implicit sphere potentials sum into a smooth blobby mass rendered with AO and Phong surface shading. Orbit camera with azimuth, elevation, and distance controls allows full 3D inspection. Reads as biological tissue, liquid mercury globule, or soft-body fluid at rest.

---

### torus_knot

GLSL SDF using `torusKnotPoint(t)` — a closest-point distance function from a knotted parametric curve in 3D — with p:q winding ratio as the primary form parameter. At p:q = 2:3 the geometry is a trefoil knot; other ratios produce increasingly complex knotted chains through the torus. Reads as a single continuous knotted tube with clear 3D rotational mass.

---

### hex_grid

GLSL hexagonal grid shader with ripple wave propagation, per-hex extrusion height, edge highlight intensity, and bloom glow. A noise field modulates per-hex activation level, producing organic spread patterns across the tessellation. Distinctive for crisp hexagonal tiling combined with fluid, propagating radial highlights.

---

## Migrated

Modules brought in from standalone files with their own original rendering pipelines, now embedded in the lab shell.

---

### brutalist_massing

Generates a procedural city block of stacked concrete slabs, stepped cores, tower masses, voids, and bridge connectors via `generateBlocks()`, rendered with `drawBox()` isometric projection. Silhouettes are hard and geometric — no smoothing or lighting gradient, purely faceted planes. Reads as a top-down brutalist architectural massing model with heavy, interlocking volumes.

---

### triangulated_signal_mesh

A jittered point field built by `buildPoints()` is triangulated into a Delaunay-like mesh by `drawFacets()`, with proximity-based additional edges drawn within `connectionRadius`. Seed-deterministic — the same seed always produces identical jitter and triangulation topology. Reads as a stress diagram, topological mesh, or signal-noise interference surface.

---

## Engine-Generated

Modules sharing the lab's `renderHeightfield` / `heightField(G)` engine pattern. Each defines its own field generation function; the shared engine handles extrusion, lighting, and PBR material rendering.

---

### agent_swarm_relief

Multiple autonomous agents walk a noise-curl vector field via `_asAngle(x,y,t)`, depositing additive-blend strokes that accumulate into a luminous sediment of tangled paths. The heightField encodes curl magnitude for 3D extrusion. Reads as nervous-system fiber bundles or ink diffusing in water.

---

### catenary_web

`arches` catenary curves computed as `cosh((x−0.5)·span) / cosh(span) · sag` layer over `ribs` vertical crossing lines, with zdepth perspective deformation. Reads as a structural cable network under gravity — architectural, tensile, and structural in character.

---

### cellular_bloom

Voronoi-seeded cellular heightfield where each cell emits a radial soft glow modulated by `radius`, `growth`, and `softness` parameters. Overlapping bloom footprints merge into a luminous, organic growth array. Reads as cell mitosis, lichen colony, or bioluminescent tissue cross-section.

---

### cellular_erosion

Game-of-Life-style cellular automaton iterated on a pixel grid (CEG resolution), sampled and upscaled into the heightfield. Fill, iterations, and pixel size parameters control pattern density and texture grain coarseness. Reads as corroded crystalline surface, pixelated erosion, or degraded electronic signal.

---

### contour_field

Multi-octave FBM noise heightfield sampled with `scale` and `turbulence` parameters, rendered as marched iso-contour lines tracing constant-elevation bands across the smooth noise surface. Reads as topographic map without color fill — pure line structure expressing elevation gradient.

---

### crater_field

Scattered craters defined by radial bowl functions — a noise base plus per-impact `exp(−r²/rim²) · depth` depressions with a slight raised rim ring. `count`, `size`, `depth`, and `rim` parameters control the impact distribution and morphology. Reads as lunar or planetary surface bombardment field.

---

### crystal_growth

Branching crystal arms from `_crysPoint(c, u, t)` — jitter-perturbed parametric lines with segment count and spread angle — accumulated into a heightfield via inverse-distance weighting. Parameters control branch count, spread, segment resolution, and jitter magnitude. Reads as mineral dendrite, ice crystal growth, or galvanized metal grain.

---

### echo_contours

`_ecVal(x,y,t)` computes concentric ripple rings from multiple seed centers `EC_CENTERS`, each contributing `exp(−dist·rings) · sin(dist·echoes − t)`. Multiple overlapping ring systems produce interference patterns between their echo trains. Reads as concentric wave interference from multiple simultaneous drop sources.

---

### fractal_tiles

Recursive tile subdivision with fold/mirror symmetry, accumulated into a heightfield — each subdivision level contributes a different frequency of geometric detail. Reads as Islamic geometric tilework or fractal quilt pattern with self-similar structure at multiple scales.

---

### glyph_field

A regular grid of randomly selected glyphs from a symbol set, each contributing a radial Gaussian footprint scaled by the `size` parameter to the heightfield. The result encodes character presence as relief height. Reads as a dense typographic relief map or cipher field — text dissolved into terrain.

---

### hyperbolic_tiling

Hyperbolic disk projection — rings drawn as `sin(log(1/(0.505−r))·rings)` and spoke lines in the Poincaré disk model, producing infinite tiling compressed into a unit disk. Reads as hyperbolic geometry visualization, Klein disk, or Escher-style infinite tessellation.

---

### interference_grid

Two perpendicular sine-wave grids with noise warp applied independently: `sin(x·f + noise·warp) · sin(y·f + noise·warp)`. The product of the two wave families produces a cross-hatch moiré interference pattern. Reads as diffraction grating, mesh interference, or optical anti-aliasing artifact.

---

### kaleidoscope_field

Rotational fold/mirror symmetry applied to a noise field in multiple overlapping passes, each contributing a different frequency of symmetry axis. Reads as kaleidoscope view through a tube — geometric jewel faceting radiating from a central point.

---

### l_system

String-rewriting Lindenmayer grammar (e.g., `F → FF+[+F−F−F]−[−F+F+F]`) expanded to depth 3–6, rendered as turtle-graphics strokes accumulated into the heightfield. Rule angle, depth, and branch ratio parameters shape the fractal plant form. Reads as procedural botanical branching, coral, or dendritic tree structure.

---

### magnetic_dust

N particles each moving in direction `atan2(dy,dx) + π/2·curl + noise·2π`, deposited with additive blending and configurable trail width. Luminous fiber bundles concentrate near field-strength maxima. Reads as iron filings in a magnetic field or ferrofluid under a magnet.

---

### moire_field

Two sine-stripe families with noise warp — `sin((v/spacing + t)·π)` — overlaid at slightly offset angles or frequencies. Interference between the two families produces traveling moiré fringe patterns. Reads as optical interference artifact, analog video roll, or fabric moiré.

---

### neural_lattice

Nodes placed by power-law radial distribution from center, connected by proximity edges within `maxD` distance, animating with slow noise drift. The resulting sparse network of varying-length connections reads as a neural network diagram, dendritic tree cross-section, or metabolic pathway map.

---

### origami_fold_field

N fold lines at regular angular intervals; each contributes `exp(−|s|·ridge)` and `sign(sin(s·facets))·crease` to the heightfield, simulating paper folded along straight creases. Reads as origami crease pattern, pleated fabric, or faceted paper sculpture relief.

---

### particle_orbitals

Particles placed in discrete orbital lanes at varying radii with jitter, drawn with additive blending. Orbital speed, lane count, and jitter parameters shape the ring density and animation. Reads as atomic orbital diagram, planetary ring system, or accelerator particle track.

---

### phyllotaxis_stack

Golden-angle spiral (φ ≈ 2.39996 rad) point packing — `sqrt(i/n)` radial spacing — piled into z-depth layers with petal size and stack height controls. Reads as sunflower seed head, botanical phyllotaxis array, or seed pod cross-section.

---

### plasma_membrane

Sine-wave membrane pattern: `sin((n1 + n2 + r·0.9 + t·0.12)·TWO_PI·veins)` where n1, n2 are FBM noise samples. Produces organic, undulating wave surfaces suggestive of cell membranes or liquid crystal domains. Reads as tissue cross-section, soap film, or biological interface.

---

### prism_moire

Multiple sine-stripe families rotated at evenly spaced angles, their interference producing starburst moiré patterns rotating from center. Similar to `moire_field` but with rotational rather than translational stripe families. Reads as prism diffraction, star filter, or laser diffraction grating.

---

### quasicrystal_relief

Sum of cosine waves at N-fold symmetric angles: `Σ cos((x·cos(aₖ) + y·sin(aₖ))·freq)` for k=0..N. Produces non-repeating quasiperiodic tiling analogous to Penrose patterns. Reads as quasicrystal atomic structure, Penrose tiling, or diffraction pattern with forbidden symmetry.

---

### radial_noise

Rings computed as `sin(r·freq)`, spokes as `sin(a·count)`, with noise applied as warp on both radius and angle. The combination of ring and spoke components produces a hybrid radial-noise field. Reads as radar scope, ripple-tank interference, or mandala under distortion.

---

### reaction_diffusion

Gray-Scott reaction-diffusion system iterated on a 170×170 grid in real time — feed and kill rate parameters control the pattern regime (spots, stripes, worm labyrinths, coral). The evolving chemistry is rendered as heightfield extrusion. Reads as living organic chemistry: Turing patterns, coral polyp, or bacterial colony.

---

### reaction_terraces

FBM noise heightfield quantized into `floor(v·steps)/steps` discrete terraces — smooth noise given a hard-edge, stacked-layer appearance by the quantization. Reads as contour-mapped geology with cliff faces, or terraced rice paddies carved into rolling hills.

---

### recursive_grid

Noise-gated quad-tree subdivision rendered as flat 2D strokes on normalized coordinates, without the isometric extrusion of grid_extrude. Cell subdivision halts below a noise threshold, producing variable-density grid regions. Reads as an information-density map, floor plan subdivision, or signal segmentation diagram.

---

### ribbon_flow

N horizontal ribbons deformed by sine wave plus curl noise — each ribbon is a wavy horizontal band with vertical displacement driven by `sin(x·freq + t) + curl·noise`. Reads as folded ribbon fabric in airflow, magnetic tape spooling, or laminar fluid layer.

---

### signal_rain

Vertical streak field with noise gating — each streak has slant and glitch parameters introducing horizontal displacement and break artifacts. Reads as rain on glass, scan-line dropout, data corruption artifact, or falling particle curtain.

---

### signal_weave

Two-axis interference: `sin((x·f + t)) + sin(y·f·0.72 + ph)·w · sin((y·f + t))`, blended with FBM noise. Produces an animated fabric-like texture with traveling shimmer. Reads as textile under light, signal interference grid, or CRT scanline weave.

---

### spiral_lattice

Logarithmic spiral arms with node dots at fixed arc-length intervals, cross-linked by radial struts at even spoke angles. Arm count, node spacing, and strut radius controls shape the web density. Reads as mechanical cam, galaxy spiral arm diagram, or spider web geometry.

---

### stipple

FBM noise heightfield where dot size in a regular stipple grid is proportional to the noise value at each sample point. Darker (higher-value) regions receive larger dots; lighter regions receive smaller or no dots. Reads as hand-engraved stipple illustration or mezzotint print.

---

### tensegrity_nodes

Nodes placed by golden-angle phyllotaxis distribution, connected by proximity struts, animating with slow orbital drift per node. Reads as tensegrity structure diagram, cable-net skeleton, or structural force network.

---

### terrain_slice

Five-octave FBM heightfield rendered as horizontal slice contour lines — each line is drawn at a constant-elevation cut through the noise surface. No color fill, only the line structure. Reads as geological cross-section, LIDAR terrain model, or elevation contour survey.

---

### topographic_rings

Polar noise with swirl warp rendered as `sin(a·rings + r·levels − t)` ring bands. Rings and levels parameters independently control angular band count and radial level count. Reads as topographic elevation rings viewed from above, or polar sonar sweep.

---

### truchet

Noise-biased square-capped Truchet tiles — each cell's arc direction (0° or 90°) is biased by a noise field, then two square-capped arcs fill the cell. The noise bias produces organic clustering of direction rather than uniform randomness. Reads as Celtic knotwork, continuous-path maze, or circuit trace layout.

---

### truchet_b

Same noise-biased Truchet tile algorithm as `truchet` but with round caps and per-tile color lerp between palette[1] and palette[2]. The rounded arc terminations and gradient coloring produce a softer, more illustrative result. Reads as soft continuous arc tiling with flowing color transition.

---

### vector_scope

Oscilloscope Lissajous pattern with multiple gain/frequency layers drawn with additive blending, accumulating a glowing 2D trace. Parameters control the individual layer frequencies and gains. Reads as broadcast vectorscope, audio Lissajous display, or electron beam art.

---

### voronoi

Lloyd-relaxed Voronoi tessellation — sites drift slowly through the field, iterative centroid relaxation is applied, then nearest-site regions are filled. Reads as cell biology packing, soap bubble tessellation, or geographic territory diagram.

---

### voronoi_tower_field

Nearest-site Voronoi height with per-cell random bias plus terrace quantization and an edge highlight on cell boundaries. Reads as terraced city blocks, abstracted urban density map, or stepped crystal facets.

---

### vortex_sheet

Particle streams follow the velocity gradient of superimposed rotating vortex centers with shear: `direction = atan2(dy,dx) + π/2·curl`. Multiple overlapping vortex funnels create braided, swirling fiber structures. Reads as fluid dynamics cyclone pattern, von Kármán vortex street, or atmospheric vortex field.

---

### wave_interference

N point sources summed as `Σ sin(dist(p, srcₙ)·freq − t)` with contrast sharpening applied post-summation. Interference between multiple sources creates complex standing-wave patterns whose geometry shifts as sources move. Reads as ripple tank with multiple simultaneous drop sources, or acoustic room mode map.

---

### wave_lattice

`sin((x+y)·f + t) · sin((x−y)·f·1.13 − t)` with FBM noise warp applied to both x and y coordinates before evaluation. The diagonal sine product creates diamond-lattice standing waves that warp into organic, flowing interference. Reads as crystal lattice vibration, Chladni figure, or transverse wave superposition.

---

### woven_lattice_relief

Thread width modeled as `exp(−dx²/tw²)` for warp and `exp(−dy²/tw²)` for weft, with over/under alternation at crossing points controlling which thread appears on top. Multiple warp × weft frequency combinations layer into a compound weave structure. Reads as physical textile microstructure, loom pattern, or basket weave cross-section.
