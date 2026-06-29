# Shell Controls Handoff

Repo:
`/Users/noixzy.macbookpro/Documents/noixzy_geometry_lab`

Current aim:
Finish `module_shell.html` control forwarding after removing hidden legacy control bridges.

Committed:
- `64e9364` shell proxy controls
- `77104de` reset fallback
- `51bc889` sdf syntax fix
- `4b10b56` sdf thumbnail
- `d613b7` displacement forwarding
- `0ea2398` removed hidden legacy bridges

Current dirty state:
- `module_shell.html` modified
- `control_consistency_audit.txt` untracked/generated, safe to delete if not needed

Main finding:
Most modules use old/plain control IDs:
`randomForm`, `randomColor`, `newSeed`, `pause`, `reset`, `save`, `save2x`, `thumb`, `rec`

Some newer modules use `btn*` IDs:
`btnNewSeed`, `btnPause`, `btnReset`, `btnSave`, `btnSave2x`, `btnThumb`, `btnRec`

Correct direction:
Keep compatibility in `module_shell.html`.
Do not re-add hidden bridge buttons inside modules.

Likely last patch:
In `module_shell.html`, `randomAll` fallback currently short-circuits:

```js
return clickFirst(doc, ["randomForm", "btnRandomForm"]) || clickFirst(doc, ["randomColor", "btnRandomColor"]);
