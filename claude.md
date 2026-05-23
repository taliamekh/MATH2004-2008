# CLAUDE.md — MATH2004 Course Notes

## Rules

1. **Fetch `progress.md` FIRST.** It has the fetch guide, concepts index, and session log. Do not fetch any other file until you've read it.
2. **Fetch ONLY what `progress.md` says.** The fetch table maps every task to the exact files needed. Never fetch files outside that list.
3. **Never read a chapter file you aren't editing.** Cross-reference using the Concepts Index in `progress.md`, not by loading HTML.
4. **Never regenerate the full HTML.** Edit fragment files. Run `build.py` to assemble.
5. **Never simplify, shorten, or restructure existing content.** If you aren't editing it, don't touch it.
6. **Update `progress.md` at the end of every session** — add to the Concepts Index and Session Log.

## Project Structure

- `shell-head.html` / `shell-foot.html` — CSS, sidebar, JS (rarely edited)
- `chapters/chN-notes.html` — chapter notes (one file per chapter)
- `chapters/chN-prob.html` — recommended problems (one file per chapter)
- `chapters/formulas.html` — formula sheet (appended each chapter)
- `chapters/summary.html` — summary (appended each chapter)
- `chapters/progress.html` — progress tracker (appended each chapter)
- `chapters/tNprep.html` / `final.html` — test prep pages
- `build.py` — assembles all fragments into `MATH2004-notes.html`
- `progress.md` — session state, concepts index, fetch guide

## Build

```bash
python3 build.py
```

Reads `shell-head.html` + all `chapters/*.html` + `shell-foot.html` → outputs `MATH2004-notes.html`.

## Theme

Grid Paper (#8). Colors and component specs are in `shell-head.html` CSS variables. Use the course-notes skill's theme table for reference values.
