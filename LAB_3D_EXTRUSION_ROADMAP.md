# LAB 3D Extrusion Roadmap

Roadmap for net-new 3D SDF-native WebGL modules and extrusion upgrades across
the geometry lab. Two parallel tracks:

- **Track EXTRUDE** — upgrade existing canvas modules with a z-extrusion
  layer (height field, bevel, shell). Governed by LAB_EXTRUSION_ENGINE_SPEC.md.
- **Track WESDF** — net-new SDF-raymarched modules, no canvas counterpart.

Blender-portability is a standing goal for every WESDF module: each module
ships a `formSpec` JSON schema sufficient to reconstruct the geometry in
Blender without re-implementing the raymarcher.

---

## Track WESDF — Initial 8

Process: proposal → sign-off → implementation → commit.  
Items 5–6 are the template for the sign-off gate (PARAMS array + field-to-form
mapping reviewed before any shader code is written).

| # | Module | Status | Notes |
|---|--------|--------|-------|
| 1 | mandelbulb | shipped `76051da` | WebGL migration; power/morph/orbit |
| 2 | metafluid  | shipped `bb4aee5` | WebGL migration; smin metaballs, inertia orbit |
| 3 | — | TBD | |
| 4 | — | TBD | |
| 5 | blob_field | shipped `1a4b0fd` | Field-driven N×N metaball terrain; smin blending |
| 6 | curl_tendrils | proposal approved, implementation pending | Swept capsule paths along curl-noise flow lines |
| 7 | domain-warped canyon | scoped (see extended candidates below) | Noise-warped boolean subtraction, erosion geometry |
| 8 | — | TBD | |

---

## Track WESDF — Extended candidates (post-initial-8)

**Status: proposed, unscoped.** These are candidates only — not yet spec'd to
the depth of blob_field or spine/path. Pick and scope individually when ready,
same process as items 5/6/7: proposal → sign-off → implementation.

---

### Fractal / recursive family

**Box-fold / sphere-fold IFS fractal**
Mandelbox-style iterated fold-and-scale; sharp recursive boxy detail. Distinct
fractal language from mandelbulb's orbit-trap approach — hard folds produce
crystalline angularity vs. mandelbulb's flowing bulges.

**Menger sponge / recursive cube subtraction**
True subtractive geometric fractal via recursive cube carving. Highly
Blender-portable: geometry nodes recursive instancing reconstructs the exact
same hierarchy without approximation. Hard-edged, architectural negative space.

**Polyhedral kaleidoscope fold**
Icosahedral or octahedral mirror-fold fractal; gem-faceted recursive detail.
Different fold symmetry from the Mandelbox family — rotational rather than
axial — produces jewel-like interior repetition.

---

### Structural / architectural family

**Linked torus chain**
Interlocking rings (Hopf-link style); chainmail aesthetic. SDF of a torus is
cheap (`sdTorus`); linking is a modular-space trick. Highly regular, good
candidate for pattern-based Blender reconstruction via array modifiers.

**Architectural truss / lattice cage**
Node-strut SDF cylinders arranged on a 3D lattice; 3D evolution of
tensegrity_nodes. Hard-edged structural look, no smin blending — strict
geometric union. Maps to Blender geometry nodes instancing on a point cloud.

**Helix / spiral staircase sweep**
Parametric helical tube: deterministic mathematical sweep (distinct from
curl_tendrils' flow-field-driven sweep). Closed-form SDF via modular angle
folding along the helix axis. Blender: curve object with Screw modifier or
Array + Curve modifier.

---

### Organic / growth family

**Crystal growth SDF, faceted**
3D version of crystal_growth using hard `min()` instead of `smin()` for sharp
mineral-facet branching; opposite surface language from blob_field. Branching
geometry via recursive SDF union of oriented slabs or rhombohedra.
Blender-portable as geometry nodes recursive convex hull.

**Capsule swarm with flocking alignment**
Boids-driven capsule positions updated in JS each frame (same pattern as
blob_field's `_buildBlobs`), smin-blended in shader. Alive and directional
rather than static terrain-like placement; capsule orientation tracks local
velocity vector.

---

### Field / surface family

**Domain-warped subtractive canyon**
Noise-warped boolean subtraction carving into a solid block; true erosion
geometry. Maps to roadmap item 7. The SDF is `max(−noise_warp(p), solid_box)`
— negative space is the subject. Blender: sculpt displacement + boolean
subtract, or geometry nodes procedural displacement.

**3D standing wave interference**
Sum-of-sines SDF displacement on a base surface; true 3D version of
wave_interference / wave_lattice. Multiple plane waves with different
frequencies and phase offsets; isosurface of the interference pattern produces
nodal sheets and ridges. Blender: shader displacement node with the same
sum-of-sines formula, baked to mesh.
