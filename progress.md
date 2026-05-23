# MATH 2004 — Multivariable Calculus: Session Progress

**Course:** MATH 2004 — Multivariable Calculus
**Textbook:** The ABCs of Calculus, Volume 2 — A. Mingarelli
**Solutions Manual:** https://people.math.carleton.ca/~angelo/calculus/ABC2-Solutions-July-4-2023-book-Pandemic.pdf
**Theme:** Grid Paper (#8) — Architects Daughter font
**Repo:** https://github.com/taliamekh/MATH2004-2008
**Raw base URL:** `https://raw.githubusercontent.com/taliamekh/MATH2004-2008/main/`
**NotebookLM notebook ID:** `6d79ff99-8491-49cf-9d6e-d707d634ac90`
**Textbook source ID (in NotebookLM):** `df7898f7-ca93-4ebc-b44a-9a479f6a052c`

## Source Materials — PAGE RANGES PER CHAPTER

**Two source PDFs.** When the user uploads either PDF, read ONLY the pages for the chapter being written. Do NOT read the entire document.

### Textbook: *The ABCs of Calculus, Vol 2* (Mingarelli)
NotebookLM source ID: `df7898f7-ca93-4ebc-b44a-9a479f6a052c`

| Chapter | Sections | Textbook Pages |
|---------|----------|----------------|
| Ch 1 — Vectors | §1.1–1.10 | 1–49 |
| Ch 2 — Curves & Surfaces | §2.1–2.14 | 51–163 |
| Ch 3 — Partial Derivatives | §3.1–3.7 | 165–257 |
| Ch 4 — Line Integrals | §4.1–4.3 | 259–289 |
| Ch 5 — Double Integrals | §5.1–5.6 | 291–369 |
| Ch 6 — Surface Int. & Theorems | §6.1–6.8 | 371–471 |
| Ch 7 — Max/Min & Lagrange | §7.2–7.3 | 477–496 |

### Lecture Notes: *Math2004 Notes* (Eric Hua, 77 pages)
File: `Math2004_Notes.pdf` — uploaded by user. This is a condensed set of lecture notes with worked examples. It has its own TOC on page 1.

| Chapter | Lecture Note Sections | Note Pages |
|---------|----------------------|------------|
| Pre-knowledge (trig/integration review) | Pre-knowledge | 2 |
| Ch 1 — Vectors | §1.1–1.10 | 3–6 |
| Ch 2 — Curves & Surfaces | §2.1–2.14 | 7–22 |
| Ch 3 — Partial Derivatives | §3.1–3.7 | 22–33 |
| Ch 4 — Line Integrals | §4.1–4.3 | 33–37 |
| Ch 5 — Double Integrals | §5.1–5.6 | 38–50 |
| Ch 6 — Surface Int. & Theorems | §6.1–6.8 | 51–66 |
| Ch 7 — Max/Min & Lagrange | §6.11–6.12 (= §7.2–7.3) | 67–77 |

**Ch 2 lecture notes detail (for scoped reading):**
- §2.1–2.5 Lines & Planes: pages 7–9
- §2.6 Rotations & Translations: pages 9–11
- §2.7–2.8 Parametric Curves: pages 11–15
- §2.9 Area Applications: pages 15–16
- §2.10 Arc Length: pages 16–17
- §2.11–2.14 Polar Coordinates: pages 17–22

**How to use both sources:** The textbook has full theory, derivations, and exercise sets. The lecture notes have condensed definitions + worked examples from class. Use BOTH for a chapter — the textbook for depth and the notes for the professor's emphasis and example style. Read the lecture notes pages first (shorter), then the textbook pages for anything the notes don't cover.

---

## ⚠ CLAUDE: READ THIS FIRST — FETCH GUIDE

**Step 1:** You already have this file. Do NOT fetch anything else yet.
**Step 2:** Read the user's request below.
**Step 3:** Look up the task in the fetch table. Fetch ONLY the listed files.
**Step 4:** Do the work, rebuild, update this file.

### Fetch Table — What to load per task

| Task | Fetch these files ONLY | NEVER fetch |
|------|----------------------|-------------|
| **Write Chapter N notes** | `chN-notes.html`, `formulas.html`, `summary.html`, `progress.html`, `shell-head.html` (for sidebar pending class) | Any other chapter's notes file |
| **Write Chapter N problems** | `chN-prob.html` | Any notes files |
| **Edit existing Chapter N** | `chN-notes.html` | Any other chapter's files |
| **Edit Chapter N problems** | `chN-prob.html` | Any other chapter's files |
| **Add test prep** | `tNprep.html` or `final.html` | Chapter notes files |
| **Fix formula sheet** | `formulas.html` | Chapter notes files |
| **Fix summary** | `summary.html` | Chapter notes files |
| **Fix progress tracker** | `progress.html` | Chapter notes files |
| **Fix CSS or sidebar** | `shell-head.html` | Chapter content files |
| **Fix JS** | `shell-foot.html` | Chapter content files |
| **Rebuild only** | Nothing — just run `build.py` | Everything |

### How to fetch a file
```bash
curl -sL "https://raw.githubusercontent.com/taliamekh/MATH2004-2008/main/chapters/ch2-notes.html" -o /home/claude/ch2-notes.html
```

### Cross-referencing previous chapters
**DO NOT fetch previous chapter files.** Use the Concepts Index section below instead.
It tells you every concept, formula, and example that was covered in each chapter.
If you need to reference Ch1's dot product formula in Ch3, write `recall from §1.7 that v·w = |v||w|cosθ` — don't load ch1-notes.html.

---

## File Structure

```
MATH2004-2008/
├── build.py              ← assembles fragments into one HTML
├── shell-head.html       ← CSS, sidebar, opening tags (NEVER edit)
├── shell-foot.html       ← JS, closing tags (NEVER edit)
├── progress.md           ← this file — session log
├── MATH2004-notes.html   ← built output (view this, don't edit directly)
└── chapters/
    ├── ch1-notes.html    ← Chapter 1 notes (COMPLETE)
    ├── ch1-prob.html     ← Chapter 1 recommended problems
    ├── ch2-notes.html    ← Chapter 2 notes (outline only)
    ├── ch2-prob.html     ← Chapter 2 recommended problems
    ├── ch3-notes.html    ← Chapter 3 notes (outline only)
    ├── ch3-prob.html     ← Chapter 3 recommended problems
    ├── ch7-notes.html    ← Chapter 7 notes (outline only)
    ├── ch7-prob.html     ← Chapter 7 recommended problems
    ├── ch4-notes.html    ← Chapter 4 notes (outline only)
    ├── ch4-prob.html     ← Chapter 4 recommended problems
    ├── ch5-notes.html    ← Chapter 5 notes (outline only)
    ├── ch5-prob.html     ← Chapter 5 recommended problems
    ├── ch6-notes.html    ← Chapter 6 notes (outline only)
    ├── ch6-prob.html     ← Chapter 6 recommended problems
    ├── formulas.html     ← Formula sheet (Ch1 only so far)
    ├── summary.html      ← Course summary (Ch1 only so far)
    ├── progress.html     ← Progress tracker checkboxes
    ├── t1prep.html       ← Test 1 prep (placeholder)
    ├── t2prep.html       ← Test 2 prep (placeholder)
    ├── t3prep.html       ← Test 3 prep (placeholder)
    ├── t4prep.html       ← Test 4 prep (placeholder)
    └── final.html        ← Final exam prep (placeholder)
```

## Workflow for Claude

1. User says "write Chapter N notes" or "add problems for Chapter N"
2. Claude fetches `progress.md` from the repo → knows current state
3. Claude fetches ONLY the specific fragment file(s) being edited
4. Claude edits the fragment with `str_replace` or `create_file`
5. If adding a chapter, Claude also appends to: `formulas.html`, `summary.html`, `progress.html`
6. Claude updates the sidebar pending status in `shell-head.html` (remove `pending` class)
7. Claude runs `python3 build.py` to assemble the output
8. Claude updates this `progress.md` with what was done
9. User pushes all changed files to GitHub

**NEVER read ch1-notes.html when writing ch3. Use this file for cross-references.**

---

## Concepts Index

### Ch1 — Vectors (§1.1–1.10) ✅ COMPLETE
**Defined:** vectors (geometric + algebraic), magnitude, unit vector, scalar multiplication, vector addition/subtraction, standard basis (i,j,k in ℝ² and ℝ³), inclination angle, direction cosines, dot product (algebraic + geometric), orthogonality, scalar projection, vector projection, work, cross product (component + determinant), right-hand rule, parallelogram area, triangle area, scalar triple product, parallelepiped volume, coplanarity test
**Key formulas:**
- Magnitude: |v| = √(v₁²+v₂²+v₃²)
- Unit vector: û = v/|v|
- Dot product: v·w = v₁w₁+v₂w₂+v₃w₃ = |v||w|cosθ
- Angle: cosθ = v·w/(|v||w|)
- Scalar projection: comp_v u = u·v/|v|
- Vector projection: proj_v u = (u·v/|v|²)v
- Work: W = F·d
- Cross product: v×w via 3×3 determinant
- |v×w| = |v||w|sinθ = parallelogram area
- Triangle area = ½|u×v|
- Volume = |u·(v×w)| = |det[u;v;w]|
- Direction cosines: cosα=a/|v|, cos²α+cos²β+cos²γ=1
**Key tests:** ⊥ ↔ v·w=0, ∥ ↔ v×w=0, coplanar ↔ u·(v×w)=0
**Examples:** 7 worked examples (linear combinations, inclination angles, angle between vectors, perpendicularity, projections, cross products, triangle area, parallelepiped volume)
**Properties tables:** vector arithmetic (6 properties), dot product (6 properties), cross product (7 properties)

### Ch2 — Lines, Planes & Parametric Curves (§2.1–2.14) ⬜ OUTLINE ONLY
**Sections:** lines in space, planes, parametric curves, conics, sketching parametric, area/length of parametric curves, polar coordinates, polar area, polar arc length
**Recommended problems:** Exercise Sets 5, 6, 10, 11, 16–22

### Ch3 — Partial Derivatives & Vector Fields (§3.1–3.7) ⬜ OUTLINE ONLY
**Sections:** limits, continuity, partial derivatives, directional derivatives, gradients, chain rule, implicit differentiation, tangent planes, normal lines, conservative fields, divergence, curl
**Recommended problems:** Exercise Sets 23–25, 27, 29, 30, 31

### Ch7 — Maxima, Minima & Lagrange (§7.2–7.3) ⬜ OUTLINE ONLY
**Sections:** critical points, second derivative test, saddle points, Lagrange multipliers
**Recommended problems:** Exercise Sets 49–50

### Ch4 — Line Integrals (§4.1–4.3) ⬜ OUTLINE ONLY
**Sections:** line integrals of scalar functions, line integrals of vector fields, fundamental theorem for line integrals
**Recommended problems:** Exercise Sets 32–38

### Ch5 — Double Integrals & Surfaces (§5.1–5.6) ⬜ OUTLINE ONLY
**Sections:** double integrals, iterated integrals, volume, change of variables, sketching 3D surfaces, parametric surfaces
**Recommended problems:** Exercise Sets 37–42

### Ch6 — Surface Integrals & Integral Theorems (§6.1–6.8) ⬜ OUTLINE ONLY
**Sections:** surface area, surface integrals, flux, Green's theorem, Stokes' theorem, triple integrals, cylindrical/spherical coords, Divergence theorem
**Recommended problems:** Exercise Sets 41–48

---

## Shared Sections Status

| Section | Status | Contains |
|---------|--------|----------|
| Formula Sheet | Ch1 only | 8 formula cards with variable popups, 3-view toggle |
| Summary | Ch1 only | 7 concept clusters + quick reference table |
| Progress | Full skeleton | All checkpoints and groups, Ch1–Ch7 items |
| Test 1 Prep | Placeholder | — |
| Test 2 Prep | Placeholder | — |
| Test 3 Prep | Placeholder | — |
| Test 4 Prep | Placeholder | — |
| Final Prep | Placeholder | — |

---

## Session Log

### Session 1 — May 23, 2026
- Built Chapter 1 notes from scratch (§1.1–1.10): full definitions, equations, proofs, SVG diagrams, 7 worked examples
- Created formula sheet with Ch1 formulas (3-view toggle, clickable variable popups)
- Created summary with Ch1 concept clusters
- Created progress tracker with full course skeleton
- Created test prep placeholders (T1–T4, Final)

### Session 2 — May 23, 2026 (current)
- Added course outline info to blank chapters (Ch2–Ch7): section breakdowns by week
- Added recommended problems pages for all chapters with exercise set listings
- Added sidebar sub-links (└ Problems) for Ch2–Ch7
- **Restructured into modular file system**: shell + 22 fragment files + build.py
- Created progress.md for cross-session state tracking
- NotebookLM was unresponsive this session — progress.md serves as fallback
