# noixzy_geometry_lab

Browser-based generative module system. 53 geometry engines, each a self-contained HTML file. Central home grid and module shell for navigation and control.

## Structure

modules.manifest.json   — single source of truth for all modules
home/home.html          — module grid + thumbnail rail
module_shell.html       — iframe shell with controls and nav rail
[module_id]/            — one folder per module, self-contained
home/thumbs/            — one PNG thumbnail per module
home/assets/            — shared assets (logo etc)

## Running locally

npx serve . -l 3000

Then open http://localhost:3000/home/home.html

## Adding a module

1. Create folder [id]/noixzy_[id].html
2. Add thumbnail home/thumbs/[id].png
3. Add entry to modules.manifest.json
4. Validate contract: npm run verify:modules

See LAB_MODULE_ADDITION_CONTRACT.md for the full acceptance checklist and naming rules.
