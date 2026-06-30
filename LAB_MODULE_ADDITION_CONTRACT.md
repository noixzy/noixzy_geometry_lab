# LAB MODULE ADDITION CONTRACT

Last updated: 2026-06-30

This contract defines the required steps and acceptance checks for adding a new live module to this repo.

## 1) Required file layout

For a module id `my_module`:

1. Create folder: `my_module/`
2. Create module HTML: `my_module/noixzy_my_module.html`
3. Create thumbnail PNG: `home/thumbs/my_module.png`
4. Add one manifest record in `modules.manifest.json`

## 2) Required module id and naming rules

1. id must be lowercase snake_case: `^[a-z0-9]+(?:_[a-z0-9]+)*$`
2. Folder must exactly match id
3. HTML filename must be exactly `noixzy_<id>.html`
4. Thumbnail filename must be exactly `<id>.png`

## 3) Required manifest contract

Each live module entry must include these keys:

- `id` (string)
- `title` (string)
- `file` (string)
- `thumb` (string)
- `authorship` (string)
- `listedInHome` (boolean)
- `enabledInShell` (boolean)
- `status` (string; expected `listed` for active modules)

Required path values for id `<id>`:

- `file`: `<id>/noixzy_<id>.html`
- `thumb`: `home/thumbs/<id>.png`

## 4) Shell compatibility minimum

The module must run inside:

- Home route: `home/home.html`
- Shell route: `module_shell.html?module=<id>`

Minimum behavior:

1. No console errors on load
2. Visual output appears and animates/renders
3. `save png` works from shell controls
4. `reset` and `pause` do not crash the module

## 5) Optional but recommended bridge support

If the module defines shell-exposed params, use the modern param bridge contract:

1. Expose PARAMS in modern shape (`k`, `g`, `step`, `v`)
2. Reply to `postMessage` `getParams` with `type: "params"`
3. Handle `setParam` updates without full reload

Note: modules without bridge wiring are still allowed, but shell param sidebar will not populate.

## 6) Validation command (required before commit)

Run:

`npm run verify:modules`

This checks:

1. Required manifest keys
2. id/path naming consistency
3. Duplicate ids
4. HTML and thumbnail file existence
5. `summary.listedCount` vs actual manifest module count

## 7) PR acceptance checklist

Before merging a new module:

1. `npm run verify:modules` passes
2. New module appears in home grid
3. New module opens from shell URL param
4. Thumbnail renders in home rail
5. No unrelated manifest edits

## 8) Example manifest entry

```json
{
  "id": "my_module",
  "title": "my module",
  "file": "my_module/noixzy_my_module.html",
  "thumb": "home/thumbs/my_module.png",
  "authorship": "generated",
  "listedInHome": true,
  "enabledInShell": true,
  "status": "listed"
}
```
