# VCL Effects Data for noixzy Geometry Lab

Date: 2026-06-30  
Purpose: Brainstorm report for using gathered VCL effects data inside the noixzy geometry lab.

## Executive Summary

The VCL effects data should become an effects intelligence layer for the noixzy geometry lab.

Instead of treating the VCL files as a loose reference pile, we can translate them into reusable creative behaviors: distortion, glow, particle drift, analog damage, timing, optical energy, decay, displacement, trails, scanlines, and turbulence.

The timing is especially strong now because the bridge migration to the final shell is finished. That means the lab can stop thinking only in isolated prototype pages and start treating these effects as a shared system across the final shell: common data, common module families, consistent controls, and reusable export logic.

## Why This Matters Now

The final shell bridge migration gives the project a better place to organize behavior across modules. VCL-derived data can now plug into the shell as:

- module family tags
- preset recipes
- parameter mappings
- prompt scaffolds
- Blender export instructions
- AE/Resolve look references
- style DNA for randomization

This helps solve one of the bigger creative problems in the lab: randomization should not just change numbers. It should produce recognizable visual behaviors.

## Core Concept

Use VCL effects data as the geometry lab's effects brain.

Each effect or preset can be translated into:

- what it does visually
- what geometry behavior it implies
- what sliders it should control
- which modules it belongs to
- what Blender or AE workflow it suggests
- whether it is useful for production, reference, motion, material, or shader development

## Proposed Data Structure

Create a shared file such as:

```text
data/vcl_effect_map.json
```

Example entry:

```json
{
  "name": "glitch displacement",
  "family": "analog_damage",
  "geometry_controls": [
    "slice_offset",
    "cell_skip",
    "noise_displace",
    "edge_jitter"
  ],
  "material_controls": [
    "threshold",
    "scanline_alpha",
    "emission_edge"
  ],
  "motion_controls": [
    "strobe_rate",
    "echo_count"
  ],
  "best_modules": [
    "recursive_grid",
    "sdf",
    "contour_field",
    "flow_field"
  ],
  "blender_targets": [
    "boolean_slices",
    "displace_modifier",
    "emissive_curves"
  ]
}
```

## Recommended VCL Families

| Family | Visual Behavior | Geometry Lab Translation |
|---|---|---|
| Analog Damage | glitch, scanlines, frame tear, static breakup | sliced grids, skipped cells, jittered contours, threshold erosion |
| Optical Energy | bloom, glow, prism, glare, lens artifacts | emissive curves, halo edges, chromatic offsets, bright node clusters |
| Particle Systems | trails, swarms, sparks, dust, drifting points | boids, point clouds, instanced fragments, field-following particles |
| Distortion Fields | ripple, twirl, bend, turbulence, displacement | warped SDF space, displaced mesh fields, curved grids |
| Time Echo | trails, afterimages, strobe, frame stepping | repeated shells, offset copies, ghost geometry, timeline states |
| Architectural FX | stacking, extrusion, grids, contours, recursive forms | massing studies, recursive arrays, brutalist modules, greeble systems |
| Signal Blueprint | HUD lines, wireframes, diagrams, technical overlays | SVG paths, contour fields, graph networks, plexus structures |
| Decay / Erosion | dissolve, fragmentation, breakup, surface loss | delete thresholds, cellular erosion, fractured masks, porous surfaces |

## Module Mapping

| Existing / Planned Module | VCL Data Use |
|---|---|
| `recursive_grid` | analog damage, architectural stacking, scanline offsets |
| `sdf` | distortion fields, warped space, boolean-style blending |
| `flow_field` | particle trails, turbulence, force-field behavior |
| `reaction_diffusion` | decay, organic spread, chemical-looking surface patterns |
| `voronoi` | fracture, cells, architectural plates, cracked surface logic |
| `contour_field` | blueprint lines, terrain bands, stacked architectural profiles |
| `truchet` | optical patterning, repeated signal paths, tile logic |
| `l_system` | branching trails, growth, root systems, diagrammatic motion |
| `cellular_erosion` | dissolve, surface loss, damaged architecture |
| `grid_extrude` | brutalist massing, stack height, extrusion rhythm |
| `plexus / point network` | particle systems, neural maps, holographic bust logic |

## Slider and Control Ideas

VCL data can make the controls more meaningful.

Instead of only:

```text
amount
speed
scale
randomness
```

Use controls like:

```text
tear amount
scanline density
cell skip
trail length
echo count
field turbulence
emission edge
decay threshold
slice offset
ghost shell count
particle drift
architectural stack height
```

These names are more directly tied to production effects and will make the modules feel more intentional.

## Preset Recipe System

The lab should support recipes made from VCL-derived behaviors.

Example recipes:

| Recipe | Stack |
|---|---|
| Signal-Damaged Brutalism | grid extrusion + scanline offsets + skipped cells + edge glow |
| Holographic Neural Field | point cloud + plexus curves + bloom edges + particle drift |
| Broken Blueprint Terrain | contour field + threshold erosion + jittered linework + cyan emission |
| Turbulent SDF Mass | SDF blend + noise displacement + chromatic rim + slow field motion |
| Echo Architecture | repeated offset shells + strobe states + transparent material layers |
| Analog Decay Grid | recursive grid + dissolve mask + frame tear + grain overlay |

## Blender Bridge Ideas

Each VCL family can output a Blender-friendly target.

| VCL Family | Blender Translation |
|---|---|
| Analog Damage | boolean slices, displaced strips, broken mesh sections |
| Optical Energy | emissive curves, compositor glow notes, rim-light materials |
| Particle Systems | Geometry Nodes point instances, force fields, curve trails |
| Distortion Fields | Displace modifier, noise texture, lattice deformation |
| Time Echo | duplicated mesh states along a motion path |
| Architectural FX | stacked arrays, extrusions, bevelled brutalist massing |
| Signal Blueprint | SVG curves, bevel-depth linework, wireframe overlays |
| Decay / Erosion | delete geometry thresholds, alpha masks, fractured plates |

## Prompt Generator Use

VCL data can also drive better generation prompts.

Example:

```text
Create a brutalist recursive grid structure using analog damage behavior:
horizontal signal tearing, broken scanline spacing, edge glow, sparse particle debris,
low-frequency displacement, monochrome concrete material with oxidized copper accents.
Export seed, parameters, SVG contour layer, and Blender scaffold JSON.
```

This turns the lab into a production assistant, not just a visual toy.

## Suggested Tags

Use tags to score each VCL entry:

```text
geometry-useful
material-useful
motion-useful
shader-useful
blender-useful
ae-useful
resolve-useful
reference-only
duplicate-cluster
high-noixzy-fit
final-shell-ready
```

## First Practical Build

Start with one data file and one module integration.

Recommended first pass:

1. Create `data/vcl_effect_map.json`.
2. Add 20 to 40 hand-picked VCL effect entries.
3. Group them into the families listed above.
4. Add one final-shell control called `Effect DNA`.
5. Wire it into one module first, ideally `grid_extrude`, `recursive_grid`, or `sdf`.
6. Make randomization pull from the selected VCL family instead of changing every parameter blindly.

## Why This Fits noixzy

This fits the existing noixzy direction because the project is already moving toward:

- brutalist sci-fi forms
- geometry-first visual systems
- Blender-ready production assets
- modular shells
- reusable prompts
- effect-driven motion graphics
- AE / Blender / Resolve crossover
- data-backed creative exploration

The VCL layer gives those ideas a shared language.

## Bottom Line

The VCL effects data should become a translation layer between effect language and geometry behavior.

Now that the final shell bridge migration is finished, the lab has the structure needed to use that layer properly. The strongest next move is to build a small `vcl_effect_map.json`, connect it to one final-shell module, and let that prove the system before expanding it across the full noixzy geometry lab.
