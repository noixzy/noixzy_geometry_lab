# noixzy Visual Engine — Blender MCP Prompt Template

**Author:** Chris Tucker  
**Purpose:** Structured prompt template for generating Blender MCP scenes seeded by noixzy lab geometry. Fill each axis independently. All five axes are required — omitting any axis risks defaulting to the excluded behaviors listed below.

---

## Template

```
FORM SOURCE: [module_name] — [one sentence describing the specific geometry aspect to reference]

COMPOSITION: [camera position relative to geometry] — [spatial relationship between camera and form] — [framing intent: tight / mid / wide / environmental]

MATERIAL: [surface finish descriptor] — [roughness level: matte / satin / semi-gloss / mirror] — [additional material properties: refraction, translucency, subsurface, coating, anisotropy]

ATMOSPHERE: [light quality: quality and direction of primary light source] — [environment: void / industrial / architectural / natural / abstract] — [color temperature: warm / neutral / cool / monochromatic / split]

DO NOT USE: centered object placement, gray matte default material, eye-level camera, empty void environment unless explicitly stated above, symmetric composition
```

---

## Axis Definitions

### FORM SOURCE
Reference a noixzy lab module by name as the geometry seed. Specify which formal quality of the module to amplify — its subdivision rhythm, surface curvature, edge sharpness, topology, or density pattern. The module name should direct the Blender MCP operator toward that module's characteristic geometry rather than a generic interpretation.

**Example values:**  
`grid_extrude — emphasize the stepped cuboid relief and isometric extrusion depth`  
`gyroid — preserve the continuous saddle-surface tunneling with no flat faces`  
`reaction_diffusion — use Turing stripe regime, not spot regime`

---

### COMPOSITION
Describe the camera's physical and spatial relationship to the geometry. Specify angle, distance, and framing intent explicitly. Avoid vague descriptors like "interesting angle" — give axis of approach (top-down, low oblique, Dutch tilt, macro close), distance (tight crop / mid / environmental pull-back), and whether the frame should feel contained or expansive.

**Example values:**  
`low oblique 15° off ground — geometry fills 80% of frame — tight crop revealing surface texture`  
`overhead looking straight down — geometry offset left of center — wide with negative space right`  
`close macro on edge detail — camera parallel to dominant ridge direction — shallow depth of field`

---

### MATERIAL
Surface finish and optical properties. Specify roughness, reflectivity, and any special material behaviors (translucency, subsurface scattering, refraction, iridescence, anisotropy, clearcoat). Do not leave material undefined — Blender MCP will default to gray matte if no material is specified.

**Example values:**  
`oxidized copper — rough 0.7, metallic 1.0, green patina in crevices`  
`backlit frosted resin — translucent, rough 0.3, subsurface scattering warm amber`  
`mirror-polished black granite — metallic 0.0, rough 0.02, specular highlights only`  
`anisotropic brushed aluminum — metallic 1.0, rough 0.15, highlight streaks horizontal`

---

### ATMOSPHERE
Light quality, environmental context, and color temperature together. Specify: the key light character (hard directional, soft overcast, point highlight, volumetric), any secondary fill or bounce light, the surrounding environment type (not just "a void" — even empty space has character: dark industrial, white limbo, night exterior, overcast sky), and color temperature or tonal intent.

**Example values:**  
`single hard directional from upper left — deep shadow fill — dark limbo environment — cool blue-gray 5500K with orange accent bounce`  
`overcast soft diffuse — no hard shadows — pale industrial haze — neutral 6000K`  
`three-point: warm key, cool fill, rim from behind — architectural void — tungsten warm 3200K key`  
`interior bounce light off white walls — no visible light source — soft and directionless — neutral 5000K`

---

### DO NOT USE
Explicit exclusions that prevent Blender MCP from reverting to its default behaviors. Always include this axis unchanged unless you are intentionally requesting a default behavior. Adding items to this list prevents reversion.

**Fixed exclusions (always include):**
- centered object placement
- gray matte default material
- eye-level camera
- empty void environment unless explicitly stated in ATMOSPHERE
- symmetric composition

**Add module-specific exclusions as needed:**  
`smooth subdivision modifier on grid_extrude geometry` (would destroy the hard-edge cuboid character)  
`ambient occlusion as the only shadow source` (too flat for the form)  
`wide-angle lens distortion` (distorts isometric reading)

---

## Filled Example — grid_extrude

```
FORM SOURCE: grid_extrude — emphasize the stepped cuboid relief with variable-depth isometric extrusion; preserve the noise-driven cell size variation and hard 90° edges; do not smooth or bevel

COMPOSITION: low oblique at 25° above horizon — camera approaches from the left-front corner — geometry fills the frame with no padding — tight mid-shot showing approximately 6×6 cell region at center

MATERIAL: cast iron — metallic 1.0, rough 0.55, dark near-black base with subtle blue-gray sheen on raised faces; crevice areas slightly darker via AO; no clearcoat

ATMOSPHERE: single hard directional from upper right at 40° elevation — long shadow cast across stepped surfaces — dark industrial limbo, no ground plane visible — cool-neutral 5800K key light with very faint warm fill from below at 3200K, intensity 0.08

DO NOT USE: centered object placement, gray matte default material, eye-level camera, empty void environment unless explicitly stated above, symmetric composition, smooth subdivision modifier, beveled edges, soft diffuse lighting
```

---

## Usage Notes

- Write each axis as a single continuous description. Do not use bullet points inside an axis — the MCP operator reads it as a single instruction.
- Specificity beats brevity. "rough 0.55, metallic 1.0" is more reliable than "metallic."
- The DO NOT USE axis is a guardrail, not an afterthought. Fill it every time.
- FORM SOURCE and MATERIAL are independent. The material is not implied by the module — a gyroid can be rendered in ceramic, glass, or rusted iron.
- To vary results from the same module, change COMPOSITION and ATMOSPHERE while holding FORM SOURCE and MATERIAL fixed.
