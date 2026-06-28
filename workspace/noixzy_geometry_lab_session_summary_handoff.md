# noixzy_geometry_lab — Session Summary / Handoff

## Project paths

New local repo:

```text
/Users/noixzy.macbookpro/Documents/noixzy_geometry_lab
```

Old archived/replaced repo:

```text
/Users/noixzy.macbookpro/Downloads/noixzy_generative_lab
```

Current GitHub repo:

```text
https://github.com/noixzy/noixzy_geometry_lab
```

Current local/home URL:

```text
http://localhost:8765/home/home.html
```

## Current confirmed repo state

Current confirmed local/GitHub head:

```text
da6adee remove home label and module count
```

Confirmed remote main after force push:

```text
da6adee3edccfdcb3951dbd8eb5f1c5cbe8ee37f refs/heads/main
```

Backup ZIP created on Desktop:

```text
/Users/noixzy.macbookpro/Desktop/noixzy_geometry_lab_LOCAL_BACKUP_20260628_121853.zip
```

GitHub was initially missing/inaccessible, then manually created in browser. After force push, the GitHub connector could read `home/home.html`, confirming the real project is now on GitHub.

## Project direction

The project is now `noixzy_geometry_lab`.

The intended conceptual model:

- Modules are geometry engines.
- `home/home.html` is the central browsing surface.
- The home/gallery page reads `modules.manifest.json`.
- Module cards should route through the module shell wrapper where possible.
- Do not keep treating modules as separate hand-authored/generated UI systems unless explicitly requested.
- Do not edit individual module files unless explicitly requested.

## Home page status

Main file:

```text
home/home.html
```

The home page now reads `modules.manifest.json`.

The first two modules were moved to the front:

```text
grid_extrude
sdf_raymarch
```

Current visible order starts:

```text
grid_extrude → sdf_raymarch → displacement → displacement_primitives → mandelbulb → metafluid ...
```

The old `fold` module was not restored because it is not present in the current repo/manifest.

## Routing

Cards now route through module shell:

```js
function shellHref(module) {
  const id = module.id || (module.file || "").split("/")[0];
  return `../module_shell.html?module=${encodeURIComponent(id)}`;
}
```

Confirmed in GitHub `home/home.html`.

## Header/logo cleanup

A broken/blank top logo/header issue was traced to this actual line:

```html
<a href="home.html" aria-label="home"><img class="homeMark" src="home.svg" alt="home"></a>
```

That link was removed.

The leftover empty `.navBar` wrapper was later identified as the blank rounded bar and deleted.

The thumbnail rail remains as the top visible navigation element.

## Rail/current layout

Current intended home layout:

- Thumbnail rail at/near top.
- Rail centered.
- Rail should not be sticky/fixed.
- Rail should scroll away with page content.
- Native horizontal rail scrollbar hidden while preserving horizontal scrolling.
- Grid starts below rail.
- No HOME label.
- No `57 modules` count text.
- Background forced black.

Confirmed rail markup from GitHub:

```html
<div class="thumbRailWrap">
  <nav class="thumbRail" id="thumbRail" aria-label="module thumbnails"></nav>
</div>
```

## Current visual CSS behaviors

Hidden HOME/count text:

```css
.topLine {
  display: none !important;
}
```

Forced black background:

```css
html,
body {
  background: #000 !important;
  background-color: #000 !important;
}
```

Rail scrollbar hidden:

```css
.thumbRail {
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}
.thumbRail::-webkit-scrollbar {
  display: none !important;
}
```

## Important file condition

`home/home.html` currently contains multiple stacked CSS patch blocks from rapid fixes. Functionally the later overrides win, but the file is not clean.

Known issue: the CSS should be consolidated later instead of adding more override patches.

The cleanup pass should preserve only the final intended layout:

- Black background.
- No blank nav/logo/header.
- Thumbnail rail top, centered, non-sticky.
- No HOME/count text.
- Manifest-driven grid.
- Cards route through module shell.
- Keep horizontal rail scrolling but hide the visible scrollbar.
- Preserve module order with `grid_extrude` and `sdf_raymarch` first.

## Process lesson / guardrail

The main process failure in this session was making speculative regex/CSS edits before reading exact source lines.

Going forward:

- Scan/read exact file lines before patching.
- No guessing.
- No broad regex unless the source is visible.
- Make one scoped change at a time.
- Commit after confirmed visible success.
- Do not touch module files unless explicitly requested.
- Prefer exact `git add <specific files>` over broad adds.
- Use `pbcopy` in Terminal status/check commands when practical.

## Useful checks

Check repo status:

```bash
cd "/Users/noixzy.macbookpro/Documents/noixzy_geometry_lab" || exit 1

{
  echo "=== STATUS ==="
  git status --short
  echo
  echo "=== HEAD ==="
  git --no-pager log -1 --oneline
  echo
  echo "=== REMOTE HEADS ==="
  git ls-remote --heads origin
} | tee /dev/tty | pbcopy
```

Open home page:

```bash
open "http://localhost:8765/home/home.html"
```

Run local server if needed:

```bash
cd "/Users/noixzy.macbookpro/Documents/noixzy_geometry_lab" || exit 1
python3 -m http.server 8765
```

## Next recommended cleanup pass

Only when explicitly requested:

1. Read `home/home.html`.
2. Consolidate the CSS into a clean single layout block.
3. Remove stale `.navBar` styles if no `.navBar` markup remains.
4. Remove obsolete stacked override comments.
5. Preserve visual state exactly: rail top/centered/non-sticky, black background, no HOME/count text, module shell card routing.
6. Commit and push only `home/home.html`.
