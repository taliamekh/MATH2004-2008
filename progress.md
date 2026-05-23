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

### Ch2 — Lines, Planes & Parametric Curves (§2.1–2.14) ✅ COMPLETE
**Defined:** parametric line, line segment, parallel/intersecting/skew lines, plane equation, normal vector, angle between planes, plane-plane intersection, active rotation, passive rotation, translation, combined transforms, parametric curve, conic sections (parabola/ellipse/hyperbola), conic discriminant, parametric derivatives (1st and 2nd), horizontal/vertical tangents, parametric area, closed curve area, parametric arc length, polar coordinates, polar conversion, common polar curves, polar slope, polar area, area between polar curves, polar arc length
**Key formulas:**
- Line: r(t) = P + tv, segment: r(t) = (1-t)P + tQ
- Plane: ax+by+cz=d, normal n=(a,b,c), find from cross product PQ×PR
- Angle between planes: cosθ = n₁·n₂/(|n₁||n₂|)
- Active rotation: A = [cosθ -sinθ; sinθ cosθ], Passive: transpose
- Translation: (x',y') = (x-h, y-k)
- Parametric slope: dy/dx = (dy/dt)/(dx/dt)
- Parametric 2nd deriv: d²y/dx² = (d/dt(dy/dx))/(dx/dt) — NOT (y''/x'')
- Parametric area: ∫y·x'dt, closed: |∫g(t)f'(t)dt|
- Arc length: ∫√(x'²+y'²)dt
- Polar↔Cartesian: x=rcosθ, y=rsinθ, r=√(x²+y²)
- Polar slope: dy/dx = (r'sinθ+rcosθ)/(r'cosθ-rsinθ)
- Polar area: ½∫r²dθ, between curves: ½∫(r_out²-r_in²)dθ
- Polar arc length: ∫√(r'²+r²)dθ
- Conic discriminant: B²-4AC (=0 parabola, >0 hyperbola, <0 ellipse)
**Key results:** cycloid arch area=3πr², cycloid length=8r, ellipse area=πab, cardioid length=8
**Key tests:** parallel lines ↔ v₁×v₂=0, skew ↔ not parallel + z-check fails
**Examples:** 17 worked examples (line through points, intersecting lines, skew lines, plane through 3 points, line-plane intersection, two-plane intersection, active rotation, parametric tangent lines, H/V tangents, cycloid area, ellipse area, cycloid arc length, coordinate conversion, polar tangent, inner loop area, area between polar curves, cardioid length)
**Diagrams:** 15 SVG figures + 3 inline table diagrams (line, segment, skew, plane+normal, two-plane intersection, rotation active/passive, parametric curve, conics, tangent types, cycloid, arc length element, polar coords, cardioid, polar area sector, limaçon) — ALL DIAGRAM LABELS VERIFIED CLEAR

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
| Formula Sheet | Ch1 + Ch2 | 25 formula cards with variable popups, 3-view toggle, updated color legend |
| Summary | Ch1 + Ch2 | Ch1: 7 concept clusters. Ch2: 3 clusters (Lines/Planes, Parametric, Polar). Quick ref table with 12 rows |
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

### Session 2 — May 23, 2026
- Added course outline info to blank chapters (Ch2–Ch7): section breakdowns by week
- Added recommended problems pages for all chapters with exercise set listings
- Added sidebar sub-links (└ Problems) for Ch2–Ch7
- **Restructured into modular file system**: shell + 22 fragment files + build.py
- Created progress.md for cross-session state tracking
- NotebookLM was unresponsive this session — progress.md serves as fallback

### Session 3 — May 23, 2026
- **Wrote Chapter 2 notes** (§2.1–2.14): 79KB, full prose for first-time learners
- Content: lines, planes, rotations/translations, parametric curves, conics, polar coordinates
- 17 worked examples with full solution pipeline (thought process → setup → annotated steps → boxed answer → tips)
- Variable pills under every equation card
- **Formula sheet:** expanded from 6 to 13 Ch2 cards. Fixed \htmlData bugs (commas and = signs in descriptions broke KaTeX). Updated color legend for Ch2 variables.
- **Summary:** added 3 Ch2 clusters + 7 rows to Quick Reference table
- **Diagrams:** 15 SVG figure-box diagrams + 3 inline table mini-diagrams. Used computed polar paths for cardioid and limaçon. ⚠ KNOWN ISSUE: several diagrams still have label collision/overlap problems — need collision check fixes next session.
- Fixed Π labels → "Plane 1"/"Plane 2" for clarity
- Added \quad spacing between matrices in §2.6
- Updated claude.md to require /course-notes skill for all content

### Session 4 — May 23, 2026
- **Fixed all Ch2 SVG diagram label collisions** — 11 label fixes across 8 diagrams:
  - Diagram 1 (Line): moved `t=0` label below the dashed line (was overlapping at 1.2px)
  - Diagram 5 (Two planes): moved `line of intersection` above green line (was at 5.5px), moved `Plane 2` above blue edge (was at 1px)
  - Diagram 7 (Parametric curve): moved `(f(t), g(t))` label above the curve path
  - Diagram 8 (Conics): moved `foci` above ellipse b-axis intersection, moved `directrix` further below dashed line
  - Diagram 9 (H/V tangents): moved `dx/dt = 0` label further from curve at vertical tangent
  - Diagram 10 (Cycloid): moved `r` label away from dashed circle edge (was at 14.75px)
  - Diagram 11 (Arc length): moved `ds` label above curve/ds line (was at 14.7px)
  - Diagram 12 (Polar coords): moved `θ` label to clear space (was at 7.4px from r-line)
  - Diagram 14 (Polar area): moved `r=f(θ)` below curve (text top was 17px from curve), moved `α` away from x-axis (was at 7px)
- **Recalculated Diagram 13 (Cardioid)**: new path with 216 points + adaptive cusp density, increased scale (55→65) and viewBox for visible cusp, fixed all label positions
- **Recalculated Diagram 15 (Limaçon)**: new path with 316 points including extra points near r=0 transitions, increased scale (16→22) for visible inner loop, added dashed arrow from label to inner loop, fixed all label positions
- Every fix verified with Playwright screenshots (before + after)
- Used mandatory collision check arithmetic per /course-notes skill rules for all label placements
- Pushed `ch2-notes.html` and rebuilt `MATH2004-notes.html`

### Session 5 — May 23, 2026
- **Second-pass diagram fixes** for 4 remaining collision issues:
  - Diagram 8 (Conics): spread geometry — increased viewBox to 210px tall, enlarged ellipse from (rx=75,ry=50) to (rx=80,ry=60), repositioned foci/a/b labels with 20+ px clearance
  - Diagram 9 (H/V tangents): moved vertical tangent condition text to y=118 (below tangent line end at y=100), 80px clear of curve
  - Diagram 10 (Cycloid): moved "r" label outside dashed circle to x=138 with leader line
  - Diagram 14 (Polar area): moved "r=f(θ)" above curve at y=52, moved α to (92,198) with 24px axis clearance
  - All 4 fixes verified with Playwright screenshots
- **Ch2 title color** set to green #255F38 (was --muted grey)
  - Updated `--ch2-title` in shell-head.html
  - Applied green palette (#18230F/#27391C/#255F38/#1F7D53) to Ch2 summary cluster What/Why/How/Trap labels
- **Formula sheet expanded** — all 25 cards (12 Ch1 + 13 Ch2) rewritten with beginner-friendly explanations:
  - Every card now has: plain-English explanation assuming zero background, "Where it comes from" origin story, step-by-step usage instructions, specific exam scenarios, common mistakes
  - Formula sheet grew from ~22KB to ~50KB
  - 3-mode toggle preserved: Full Detail (expanded), Quick Reference (concise), Equations Only
- **Summary expanded** — Ch2 section grew from 3 clusters to 8:
  - NEW clusters: Rotations & Translations, Conic Sections, Key Parametric Results, Polar Calculus (split from Polar Coordinates)
  - Existing clusters expanded: Lines split from Planes, both enriched with intersection methods
  - Quick Reference table: 12 → 20 rows (added skew test, plane angle, conic discriminant, param 2nd deriv, cycloid results, polar slope, polar between curves)
  - Cross-links section expanded
- Files changed: shell-head.html, chapters/ch2-notes.html, chapters/formulas.html, chapters/summary.html, MATH2004-notes.html
