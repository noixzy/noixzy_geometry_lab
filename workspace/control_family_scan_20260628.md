# Control Family Scan — 2026-06-28

Result:
- Total active modules: 57
- Control families found: 12
- Main shared control family: 46 modules
- One-off/special families: 11 modules

Main shared family:
- 46 modules
- html ids: 60
- js ids: 61
- missing JS ids: 12
- Missing ids are consistent and appear to be runtime/dynamic:
  - navNext
  - navPrev
  - p_drift
  - p_glow
  - p_height
  - p_pal
  - p_speed
  - v_drift
  - v_glow
  - v_height
  - v_pal
  - v_speed

Main migration target:
Build shell-owned controls for the 46-module family first.

Do not migrate yet:
- grid_extrude
- displacement
- displacement_primitives
- gyroid
- sdf_raymarch
- metafluid
- mandelbulb
- hex_grid
- rose_curve
- lissajous_mesh
- torus_knot

Reason:
These are one-off/special control families with different legacy bridge dependencies.

Migration rule:
Keep module panels hidden with body.geoOnly until the shell owns replacement controls or hidden fallback stubs exist for every JS id dependency.
