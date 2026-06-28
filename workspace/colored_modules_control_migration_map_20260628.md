# Colored Modules Control Migration Map — 2026-06-28

Scope:
- agent_swarm_relief
- catenary_web
- hyperbolic_tiling
- origami_fold_field
- phyllotaxis_stack
- quasicrystal_relief
- reaction_terraces
- tensegrity_nodes
- voronoi_tower_field
- woven_lattice_relief

Current state:
- All 10 modules use the same internal panel/control architecture.
- All 10 modules have 60 HTML ids.
- All 10 modules have 61 JS id references.
- Panels are currently hidden with body.geoOnly, not deleted.

Shared controls to migrate into module_shell later:

Core:
- seedField
- seedRead
- vSeed
- newSeed
- pause
- reset

Randomization:
- randomAll
- randomForm
- randomColor
- extrudeOff

Theme:
- themeSelect
- themePrev
- themeNext
- themeDet

Color:
- colorDet
- p_bgc
- p_acc
- p_ink

Generated parameter host:
- groups
- p_
- v_

Presets:
- presetName
- savePreset
- localPreset
- loadPreset
- deletePreset
- presetStatus

History:
- btnUndo
- btnRedo
- previewHistory

Import/export:
- copyP
- pasteP
- save
- save2x
- savePBR
- thumb
- rec
- recDur
- btnTransparentBg

Audio:
- btnAudio
- audioPanel
- audioDropZone
- audioFileInput
- audioStatus
- audioPlayPause
- audioFilename
- btnMic
- audioBands

Favorites:
- favs
- stageFavs
- exportFavs
- clearFavs

Stage/thumb rail:
- stage
- stageTools
- stageThumbs
- moduleThumbStrip
- thumbUp
- thumbDown
- pin

Keyboard help:
- kbHelp

Runtime/dynamic ids:
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

Migration rule:
Do not delete panel HTML until module_shell owns replacement controls or hidden stubs exist for every JS dependency.
