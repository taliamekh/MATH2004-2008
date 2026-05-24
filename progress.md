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
    ├── exam-formulas.html ← Official exam-provided formula sheet
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

### Ch3 — Partial Derivatives & Vector Fields (§3.1–3.7) ✅ COMPLETE
**Defined:** limit of f(x,y) (ε-δ), continuity, partial derivative (∂f/∂x, ∂f/∂y), higher-order partials, mixed partials, Clairaut's theorem, gradient (∇f), directional derivative (D_u f), steepest ascent/descent, level curves, chain rule (one/two parameters), tree diagram, implicit partial derivatives, tangent plane, normal line, vector field, conservative field, potential function, curl (∇×F), divergence (∇·F), irrotational, source/sink/incompressible
**Key formulas:**
- Partial derivative: ∂f/∂x = lim[f(x₀+h,y₀)−f(x₀,y₀)]/h
- Clairaut: f_xy = f_yx (continuous mixed partials)
- Gradient: ∇f = (f_x, f_y) [2D], (f_x, f_y, f_z) [3D]
- Directional derivative: D_u f = ∇f · u = |∇f||u|cosθ
- Max rate of change: |∇f| in direction ∇f/|∇f|
- Chain rule (1 param): dz/dt = z_x·x' + z_y·y'
- Implicit: ∂z/∂x = −f_x/f_z, ∂z/∂y = −f_y/f_z
- Tangent plane: f_x(x−x₀)+f_y(y−y₀)+f_z(z−z₀)=0
- Normal line: r(t) = P + t∇f
- Curl: ∇×F = det[i,j,k; ∂_x,∂_y,∂_z; P,Q,R]
- Conservative test: curl F = 0 (2D: Q_x = P_y)
- Divergence: ∇·F = P_x + Q_y + R_z
**Key identities:** curl(∇f) = 0, div(curl F) = 0
**Key tests:** limit DNE ↔ two-path test gives different values; conservative ↔ curl F = 0
**Examples:** 18 worked examples (ε-δ limit proof, two-path DNE, continuity proof, cannot-be-made-continuous, basic partials, 3-variable partials, Clairaut verification, max directional derivative, directional derivative in given direction, related rates cylinder, implicit differentiation, tangent plane to sphere, tangent plane to z=g(x,y), 2D conservative test, potential function, 3D conservative test, divergence computation, div(curl F)=0 proof)
**Diagrams:** 2 SVG figures (partial derivative geometry — surface slice, gradient perpendicular to level curves)

### Ch7 — Maxima, Minima & Lagrange (§7.2–7.3) ✅ COMPLETE
**Defined:** critical point (stationary point), discriminant D, Hessian matrix, Second Derivative Test (SDT), saddle point, local/global max/min, compact set, closed-region extrema algorithm, Lagrange multiplier λ, Lagrangian function ℓ, constrained optimization
**Key formulas:**
- Critical point: f_x(a,b) = 0 and f_y(a,b) = 0
- Discriminant: D = f_xx·f_yy − (f_xy)² at P
- SDT: D>0+f_xx>0 → min; D>0+f_xx<0 → max; D<0 → saddle; D=0 → inconclusive
- Closed region: check interior CPs + boundary CPs + corners/endpoints
- Lagrangian: ℓ = f − λg, set ∂ℓ/∂x = ∂ℓ/∂y = ∂ℓ/∂λ = 0
- Geometric meaning: ∇f = λ∇g (gradients parallel at constrained extremum)
**Key tests:** saddle ↔ D<0; local extremum only at CPs; closed+bounded → global max/min exist
**Examples:** 9 worked examples (quadratic max, 4-CP classification with saddles, rectangle boundary, trig on square, semicircle Lagrange, ellipse distance, 3-variable Lagrange, interior+Lagrange boundary, substitution vs Lagrange)
**Diagrams:** 4 SVG figures (saddle point cross-sections, closed-region strategy, semicircle rectangle, Lagrange gradient geometry)

### Ch4 — Line Integrals (§4.1–4.3) ✅ COMPLETE
**Defined:** line integral w.r.t. arc length, line integral of vector field (F·dr), work integral, circulation, average value on a curve, center of mass of a wire, gradient field / potential function, Fundamental Theorem for Line Integrals (FTCLI), path independence, simply connected region, conservation of energy
**Key formulas:**
- Scalar line integral: ∫f ds = ∫ₐᵇ f(r(t))|r'(t)| dt
- Vector line integral: ∫F·dr = ∫ₐᵇ F(r(t))·r'(t) dt
- Component form: ∫P dx + Q dy + R dz = ∫(Px'+Qy'+Rz') dt
- FTCLI: ∫∇f·dr = f(r(b)) − f(r(a))
- Closed loop: F conservative ⟹ ∮F·dr = 0
- Potential via line integral: f(x,y,z) = ∫F·dr (from P₀ to P)
- Average value: f̄ = (1/L)∫f ds
- Center of mass: x̄ = (1/M)∫xf ds, etc.
- Work-energy: ∫F·dr = ½m|v(b)|² − ½m|v(a)|²
**Key tests:** orientation-independent ↔ scalar (ds), orientation-dependent ↔ vector (F·dr); conservative ↔ curl F = 0 ↔ path-independent ↔ ∮F·dr = 0
**Examples:** 11 worked examples (parabola arc, helix, piecewise triangle, wire mass, vector line integral with reversal, three methods same integral, piecewise 3D, work by force field, Newton/Coulomb conservative, potential via line integral, FTCLI evaluation)

### Ch5 — Double Integrals & Surfaces (§5.1–5.6) ✅ COMPLETE
**Defined:** x-simple (Type I) region, y-simple (Type II) region, vertical slices (R_yx), horizontal slices (R_xy), double integral, partition, mesh, iterated integral, Fubini's theorem (rectangle + general), reversing integration order, volume under a surface, volume between surfaces, Jacobian matrix, Jacobian determinant, change of variables formula, polar double integral (dA = r dr dθ), area in polar, trace/cross-section, quadric surfaces (ellipsoid, elliptic paraboloid, hyperbolic paraboloid, elliptic cone, hyperboloid 1/2 sheets, elliptic cylinder), parametric surface r(u,v), sphere parametrization, graph surface parametrization, surface of revolution
**Key formulas:**
- Fubini (rect): ∬f dA = ∫ₐᵇ∫_c^d f dy dx = ∫_c^d∫ₐᵇ f dx dy
- Fubini (general): ∬f dA = ∫ₐᵇ∫_{f₁(x)}^{f₂(x)} f dy dx
- Volume: V = ∬f(x,y) dA
- Jacobian: J = |∂(x,y)/∂(u,v)| = |det[∂x/∂u ∂y/∂u; ∂x/∂v ∂y/∂v]|
- Change of variables: ∬_R f dA = ∬_S f(g,h)|J| dA
- Polar: ∬f(x,y) dA = ∬f(r cosθ, r sinθ) r dr dθ
- Polar Jacobian = r
- Area (polar): ∬r dr dθ
- Sphere: r(u,v) = (R cos v cos u, R cos v sin u, R sin v)
**Key tests:** x-simple ↔ vertical slices → dy dx; y-simple ↔ horizontal slices → dx dy; quadric ID by counting squared terms + signs
**Examples:** 9 worked examples (region by parabolas, iterated rectangle, variable limits, reversing order, volume under paraboloid, polar disk integral, cardioid area, elliptic paraboloid, cylinder parametrization)
**Quadric catalog:** ellipsoid, elliptic paraboloid, hyperbolic paraboloid, cone, hyperboloid (1/2 sheets), cylinder — all with standard equations and trace descriptions

### Ch6 — Surface Integrals & Integral Theorems (§6.1–6.8) ✅ COMPLETE
**Defined:** surface integral (scalar), surface area via integration, orientable/non-orientable surface, open/closed surface, Möbius strip, outer/inner unit normal, upward/downward pointing, positive side, flux (net flow through surface), dS = n dS, Green's theorem, positive orientation (CCW), 2D scalar curl (Q_x − P_y), area via Green's, divergence form of Green's, Stokes' theorem, right-hand rule for orientation, surface independence, triple integral, Fubini for triple integrals (6 orderings), hypervolume, mass/center of mass of solid, cylindrical coordinates, spherical coordinates, 3D Jacobian, Divergence theorem (Gauss's theorem)
**Key formulas:**
- Surface integral (graph): ∬F dS = ∬F(x,y,f(x,y)) √(1+f_x²+f_y²) dA
- Surface integral (parametric): ∬F dS = ∬F(r(u,v)) |r_u × r_v| dA
- Outer unit normal: n = (−f_x,−f_y,1)/√(1+f_x²+f_y²)
- Flux (graph): ∬F·dS = ∬(−Pf_x − Qf_y + R) dA
- Flux (parametric): ∬F·dS = ∬F(r(u,v))·(r_u × r_v) dA
- Green's: ∮P dx+Q dy = ∬(Q_x−P_y) dA
- Area: ½∮(x dy − y dx)
- Green's divergence: ∬div F dA = ∮F·n ds
- Stokes': ∮F·dr = ∬(∇×F)·n dS
- Triple integral: ∭f dV (6 orderings via Fubini)
- Cylindrical: x=rcosθ, y=rsinθ, z=z, J=r, dV=r dr dθ dz
- Spherical: x=ρsinφcosθ, y=ρsinφsinθ, z=ρcosφ, J=ρ²sinφ
- Divergence: ∭div F dV = ∬F·n dS
**Key tests:** closed surface → Divergence; open surface with boundary → Stokes'; 2D closed curve → Green's
**Key identities:** curl flux through closed surface = 0 (∵ div(curl F) = 0); Volume = ∬F·n dS with div F = 1
**Examples:** 12 worked examples (plane surface integral, cylinder 3 methods, paraboloid flux, Green's with e^{y²}, annulus area, Stokes' hemisphere verification, elliptic Stokes', tetrahedron triple integral, sphere volume, cylinder volume, Divergence tetrahedron, Divergence sphere)
**Diagrams:** 5 SVG figures (surface integral geometry, Green's theorem region, Stokes' surface+boundary, cylindrical vs spherical coordinates, Divergence theorem solid+flux)

---

## Shared Sections Status

| Section | Status | Contains |
|---------|--------|----------|
| Formula Sheet | Ch1 + Ch2 + Ch3 + Ch4 + Ch5 + Ch6 + Ch7 | 59 formula cards with variable popups, 3-view toggle. Ch6: surface integral graph/parametric, flux, Green's, area via Green's, Stokes', triple Fubini, cylindrical, spherical, Divergence theorem |
| Summary | Ch1 + Ch2 + Ch3 + Ch4 + Ch5 + Ch6 + Ch7 | Ch1: 7 clusters. Ch2: 4 clusters. Ch3: 6 clusters. Ch4: 3 clusters. Ch5: 3 clusters. Ch6: 5 clusters (surface int/flux, Green's, Stokes', triple/coords, Divergence). Ch7: 3 clusters. Quick ref table with 46 rows |
| Progress | Full skeleton | All checkpoints and groups. Ch6 expanded to 15 items (8 sections + 6 example groups + formulas) |
| Test 1 Prep | Placeholder | — |
| Test 2 Prep | Placeholder | — |
| Test 3 Prep | Placeholder | — |
| Test 4 Prep | Placeholder | — |
| Final Prep | ✅ COMPLETE | W19 (18 Q), F14 (18 Q), F13 (18 Q), Practice (28 Q) — 76 fully worked solutions with Quick Guides + Exam Intel segment |

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

### Session 6 — May 23, 2026
- **Chapter 3 notes written** (35KB, §3.1–3.7): 18 worked examples, 2 SVG diagrams
  - §3.1 Limits & Continuity: ε-δ definition, two-path DNE test, continuity definition, 4 examples
  - §3.2 Partial Derivatives: definitions, geometric meaning, notation, 2 examples
  - §3.3 Higher-Order Partials: Clairaut's theorem, 1 example
  - §3.5 Directional Derivatives & Gradients: gradient definition, D_u f formula, steepest ascent/descent, 2 examples
  - §3.6 Chain Rule: one-parameter and two-parameter forms, tree diagram, 1 example
  - §3.6.2 Implicit Differentiation: shortcut formula ∂z/∂x = −fₓ/f_z, 1 example
  - §3.6.3 Tangent Planes & Normal Lines: surface form and z=g(x,y) special case, 2 examples
  - §3.7 Conservative Fields, Curl, Divergence: definitions, tests, identities, 5 examples including div(curl F)=0 proof
  - SVG diagrams: partial derivative geometry (surface slice), gradient perpendicular to level curves
- **Formula sheet expanded** — 10 new Ch3 cards added (25→35 total):
  - Partial derivative definition, Clairaut, directional derivative, gradient steepest ascent, chain rule, implicit partials, tangent plane, curl, conservative test, divergence
- **Summary expanded** — 6 new Ch3 concept clusters + 8 new quick reference rows (20→27 total)
  - Orange palette (#B33000/#CC4A00/#E06600/#F09000) for What/Why/How/Trap labels
- **Progress tracker expanded** — Ch3 group: 2→9 items (notes + 6 example sub-groups + formulas)
- **Shell-head updated** — --ch3-title set to #D35400, pending removed from Ch3 sidebar links
- **Built MATH2004-notes.html** — 294KB, 22/22 fragments assembled
- Files changed: shell-head.html, ch3-notes.html, formulas.html, summary.html, progress.html, progress.md, MATH2004-notes.html

### Session 7 — May 23, 2026
- **Ch3 formula sheet fixed** — removed commas from htmlData tooltips (commas break KaTeX parsing). All 42 tooltips now comma-free and clickable.
- **Color legend converted to table** — 5-row table format (dot + category + variables), easy to extend per chapter
- **Ch1/Ch2 formula details trimmed** — avg ~1010 → ~575 chars, matching Ch3's ~644 avg
- **Quick reference table color-coded** — left border + label color per chapter (navy Ch1, green Ch2, orange Ch3)
- **Progress tracker expanded** — Ch2: 2→15 items (6 sections + 8 examples + formulas). Ch3: 9→15 items (7 sections + 6 examples + formulas)
- **5 SVG diagrams added to Ch3 notes** (47KB total):
  - Fig 3.1: Two-path limit test (§3.1)
  - Fig 3.3: Chain rule tree diagram (§3.6)
  - Fig 3.4: Tangent plane with normal vector (§3.6.3)
  - Fig 3.5: Source/sink/curl visualization (§3.7)
  - Fig 3.6: Grad-curl-div triangle with identities (§3.7)
- **Key learning: \htmlData tooltip text must NEVER contain commas** — zero of 110 working Ch1/Ch2 tooltips had commas; all Ch3 breaks were caused by commas in tooltip text

### Session 8 — May 23, 2026
- **Chapter 4 notes written** (31KB, §4.1–4.3): 11 worked examples
  - §4.1 Line integrals w.r.t. arc length: definition, computation formulas (3D + 2D), arc-length parametrization, average value, center of mass. 4 examples (parabola, helix, triangle, wire mass)
  - §4.2 Line integrals of vector fields: definition (F·dr), component form (P dx + Q dy + R dz), work, circulation, orientation-dependence. 4 examples (line segment + reversal, three methods, piecewise 3D, work)
  - §4.3 Fundamental Theorem for Line Integrals: FTCLI statement + proof sketch, path independence, closed-loop test, simply connected regions, potential via line integral, work-energy theorem. 3 examples (Newton/Coulomb, potential by line integral, FTCLI evaluation)
- **Chapter 5 notes written** (24KB, §5.1–5.6): 9 worked examples
  - §5.1 Describing planar regions: x-simple, y-simple, vertical/horizontal slices, notation R_yx and R_xy. 1 example
  - §5.2 Double integrals & Fubini: definition, geometric meaning (volume/area), Fubini for rectangles + general regions, reversing order. 3 examples
  - §5.3 Volume under a surface: formula, volume between surfaces. 1 example
  - §5.4 Change of variables: Jacobian matrix/determinant, general change of variables formula, polar coordinates (dA = r dr dθ), area in polar. 2 examples
  - §5.5 3D plots / quadric surfaces: traces, full quadric catalog table (7 types), identification strategy. 1 example
  - §5.6 Parametric surfaces: r(u,v), sphere/graph/revolution parametrizations. 1 example
- **Formula sheet expanded** — 9 new cards added (35→44 total):
  - Ch4: scalar line integral, vector line integral, FTCLI, potential via line integral
  - Ch5: Fubini (rect), Fubini (general), polar double integral, change of variables, sphere parametrization
  - All tooltips comma-free per established convention
- **Summary expanded** — 6 new clusters + 8 new quick reference rows (27→35 total)
  - Ch4: pink palette (#3A0519/#670D2F/#A53860/#EF88AD) for What/Why/How/Trap
  - Ch5: maroon palette (#280905/#740A03/#C3110C/#E6501B) for What/Why/How/Trap
- **Progress tracker expanded** — Ch4: 2→11 items. Ch5: 2→14 items (6 sections + 6 example groups + formulas). Ch6 separated from Ch4-6 placeholder.
- **Shell-head updated** — --ch4-title set to #670D2F, --ch5-title set to #740A03, pending removed from Ch4/Ch5 sidebar links
- **Built MATH2004-notes.html** — 388KB, 22/22 fragments assembled
- Files changed: shell-head.html, ch4-notes.html, ch5-notes.html, formulas.html, summary.html, progress.html, progress.md, MATH2004-notes.html

### Session 8 (continued) — Fixes & Polish
- **Formula sheet fixes:**
  - Fixed FTCLI + Chain Rule — `=` sign in tooltip text broke KaTeX rendering. NEW RULE: tooltip text must NEVER contain `=` signs (joins comma ban)
  - Cleaned all Ch4/Ch5 tooltips: removed `()` function-call syntax and `=` signs
  - Color legend: replaced 5-row table with 7-color card grid. Added rose (#B8336A) for Fields/operators and forest (#4A8060) for Bounds/constants
  - Applied new colors: rose for F in curl/div/conservative formulas; forest for bounds in Fubini general
- **SVG diagrams fixed:**
  - Fig 5.3 (sphere): rebuilt — axes through center O, proper P→Q projection, latitude circle, legend
  - Fig 5.4 (revolution): rebuilt — profile curve with exact control points, cross-section radii matched to profile, u-arrow repositioned
  - Verified both via Playwright screenshots
- **Ch4 content improved:**
  - Key Properties: color-coded card grid replacing plain numbered list
  - Average Value & Center of Mass: added plain-language "why" + bar notation explanation
  - FTCLI: problem→shortcut→when-to-use→analogy structure
  - Closed-Loop Test: plain English what/why
  - Work-Energy Theorem: underbrace KE labels + conservation of energy
- **Ch5 content improved:**
  - Example 5.1: step-by-step + answer boxes
  - §5.2 Fubini: expanded geometric meaning + "Why Fubini Works" tip + inner/outer limit rule
  - §5.5 quadric table: Shape column restored alongside SVG Sketch column
  - §5.6 parametric surfaces: full rewrite with derivations, 2 SVGs, decision guide
- **Ch2 sidebar fix:** removed pending class (Session 3 oversight)
- **htmlData tooltip rules (cumulative):** NO commas, NO `=` signs, avoid `()` function syntax
- Files changed: ch4-notes.html, ch5-notes.html, formulas.html, shell-head.html, MATH2004-notes.html

### Session 9 — May 23, 2026
- **Chapter 7 notes written** (29KB, §7.2–7.3): 9 worked examples, 4 SVG diagrams
  - §7.2 Critical Points: definition, ∇f = 0 condition, case analysis strategy. 2 examples (quadratic max, 4-CP classification with 3 saddles + 1 min)
  - §7.2 Closed-Region Extrema: algorithm (interior + boundary + corners), Extreme Value Theorem. 2 examples (rectangle boundary, sin x + sin y on square)
  - §7.3 Lagrange Multipliers: geometric derivation (∇f ∥ ∇g), Lagrangian ℓ = f − λg, method for 2D and 3D. 5 examples (semicircle rectangle, rotated ellipse distance, 3-variable xyz²z³, interior+Lagrange boundary on disk, substitution vs Lagrange comparison)
  - SVG diagrams: saddle point cross-sections, closed-region strategy, semicircle inscribed rectangle, Lagrange gradient geometry
- **Formula sheet expanded** — 4 new Ch7 cards added (44→48 total):
  - Critical point condition, SDT discriminant, closed-region extrema, Lagrange multiplier method
  - All tooltips comma-free and equals-free per established convention
- **Summary expanded** — 3 new Ch7 concept clusters + 4 new quick reference rows (35→39 total)
  - Ch7: red palette (#4A0404/#7B0A0A/#B91C1C/#E53935) for What/Why/How/Trap labels
- **Progress tracker expanded** — Ch7: 2→9 items (3 sections + 5 example groups + formulas)
- **Shell-head updated** — --ch7-title set to #B91C1C (bright red), pending removed from Ch7 sidebar links
- **Built MATH2004-notes.html** — 472KB, 22/22 fragments assembled
- Files changed: shell-head.html, ch7-notes.html, formulas.html, summary.html, progress.html, progress.md, MATH2004-notes.html

### Session 9 (continued) — Fixes & Polish
- **Fig 7.1 (3-panel CP types) completely redrawn**: stripped to essentials — one clean curve per panel (U for min, arch for max, crossing curves for saddle). No contour ellipses, no overlapping arrows. Condition badges at bottom.
- **Saddle point explanation rewritten**: mountain pass analogy first ("stand at a pass — valley one way, hilltop the other, so neither max nor min"), then math. Simple → complex.
- **Fig 7.3 (rectangle) fixed**: edge labels moved outside rectangle, boundary CP separated from corner dots, legend added.
- **Fig 7.4 (Lagrange) fixed**: ∇g and ∇f arrows vertically offset (start from above/below P), no overlap. ∥ symbol between them. Labels in clear open space past arrowheads.
- **Critical point strategy expanded**: single paragraph → 6 numbered steps (compute partials → set to zero → factor → case analysis → list all CPs → classify).
- **Lagrange explanation expanded**: hiking analogy, "kissing curves" intuition, step-by-step method card with explicit equations.
- **Formula sheet: numbering + lookup bar**: all 48 cards auto-numbered with #N badges. Search bar at top — type name, chapter, or #number to instant-scroll to any equation.
- Files changed: ch7-notes.html, formulas.html, MATH2004-notes.html

### Session 9 (final fixes)
- **All prose subscripts fixed** — 58 instances of f_x, f_xx, g_x etc. converted to proper HTML <sub> tags. KaTeX math mode left untouched.
- **All 9 examples rewritten** to full solution pipeline standard:
  - Every example now has: thought process, "what we need to find", setup, annotated step-by-step solution, boxed answer, ★ Tips card, concept bridge (formula sheet #refs)
  - Classification tables expanded to show all intermediate values (f_xx, f_yy, f_xy, D)
  - Closed-region examples label results as ★ GLOBAL MIN / ★ GLOBAL MAX
- Files changed: ch7-notes.html, MATH2004-notes.html

### Session 10 — May 23, 2026
- **Chapter 6 notes written** (57KB, §6.1–6.8): 12 worked examples, 5 SVG diagrams
  - §6.1 Surface Integrals: definition via Riemann sums, graph form (3 projections), parametric form, evaluation strategy. 2 examples (plane triangle, cylinder 3 methods)
  - §6.2 Flux & Oriented Surfaces: orientability, open/closed surfaces, Möbius strip, outer/inner normals, flux definition F·dS = F·n dS, flux formulas (graph + parametric). 1 example (paraboloid flux)
  - §6.3 Green's Theorem: statement, positive orientation, proof idea, area formula, divergence form, regions with holes. 2 examples (e^{y²} shortcut, annulus area)
  - §6.4 Stokes' Theorem: statement, right-hand rule, Green's as special case, surface independence, conservative fields. 2 examples (hemisphere verification, elliptic surface)
  - §6.5 Triple Integrals: definition, Fubini (6 orderings), mass/center of mass. 1 example (tetrahedron)
  - §6.6 Cylindrical & Spherical Coordinates: cylindrical (J=r), spherical (J=ρ²sinφ), volume elements. 2 examples (sphere volume, cylinder volume)
  - §6.7 Describing Solids: reference table (sphere/cylinder/cone/plane in each system), coordinate choice guide
  - §6.8 Divergence Theorem: statement, consequences (curl flux = 0, volume via flux), unified view of all 3 theorems. 2 examples (tetrahedron, sphere)
  - SVG diagrams: surface integral geometry, Green's theorem region, Stokes' surface+boundary, cylindrical vs spherical, Divergence theorem solid
- **Formula sheet expanded** — 11 new Ch6 cards added (48→59 total):
  - Surface integral (graph + parametric), flux, Green's theorem, area via Green's, Stokes', triple Fubini, cylindrical, spherical, Divergence theorem
  - All tooltips comma-free and equals-free per established convention
- **Summary expanded** — 5 new Ch6 concept clusters + 7 new quick reference rows (39→46 total)
  - Ch6: teal palette (#0A5C64/#0B7D7D/#10A0AA/#D85050) for What/Why/How/Trap labels
- **Progress tracker expanded** — Ch6: 2→15 items (8 sections + 6 example groups + formulas)
- **Shell-head updated** — --ch6-title set to #0E7C86 (deep teal), pending removed from Ch6 sidebar links
- **Built MATH2004-notes.html** — 580KB, 22/22 fragments assembled
- **ALL CHAPTERS COMPLETE** — Ch1 through Ch7 now have full notes. Course content is 100% written.
- Files changed: shell-head.html, ch6-notes.html, formulas.html, summary.html, progress.html, progress.md, MATH2004-notes.html

### Session 11 — May 23, 2026
- **Added official exam-provided formula sheet** as new page `exam-formulas.html`
  - Converted React/JSX component to static HTML+KaTeX matching Grid Paper (#8) theme
  - 41 equations across 12 categories: Trig Identities, Parametric Curves, Polar Curves, Multivariable Calculus, Vector Calculus, Optimization, Line Integrals, Double Integrals, Surface Integrals, Triple Integrals, Coordinate Systems, Fundamental Theorems
  - Category color badges matching the original React component colors
  - Variable chips with click-to-popup definitions (body-level fixed positioning)
  - Row click to expand/collapse explanation text
  - Search bar + category dropdown filter with live count
  - All formulas rendered via KaTeX (consistent with rest of notes)
- **Sidebar updated** — added "└ Exam Provided" sub-link under "Formula Sheet"
- **build.py updated** — added `exam-formulas.html` to FRAGMENTS list after `formulas.html`
- **Built MATH2004-notes.html** — 642KB, 23/23 fragments assembled
- Files changed: shell-head.html, build.py, chapters/exam-formulas.html (NEW), MATH2004-notes.html
- **NO REGRESSION**: no existing fragment files were modified (only shell-head sidebar link added)

### Session 11 (continued) — Cross-reference pills
- **Cross-referenced formula sheet with exam-provided sheet** — 27 of 58 formula cards matched to exam equations
- Each matching card now shows a blue pill on the right side of the title bar: `📋 Exam #N` (or `#N, #M` for multi-match)
- Non-matching cards show a subtle `not on exam sheet` label
- Clicking the exam pill navigates to the Exam Provided page
- **Exam formula sheet variable chips updated** — every chip now shows `symbol — name` format (e.g. `dy/dx — slope`) with full popup descriptions on click
- Missing variables added to 11 equations: x/y/z on chain rules, r′(t) on line integrals, h₁/h₂ on double integrals, dS on surface integrals
- Popup positioning improved (clamps to screen edges)
- Files changed: chapters/formulas.html, chapters/exam-formulas.html, MATH2004-notes.html

### Session 12 — May 23, 2026
- **Final Exam Prep page written** — 76 fully worked solutions from 3 past finals + practice set
  - **Winter 2019 Final**: A1–A12 (MC) + B1–B6 (long answer) — 18 questions
  - **Fall 2014 Final**: A1–A12 (MC) + B1–B6 (long answer) — 18 questions
  - **Fall 2013 Final**: A1–A12 (MC) + B1–B6 (long answer) — 18 questions
  - **Practice Questions**: Q1–Q28 — 28 questions covering all chapters
  - Every solution follows the 5-part structure: 🧠 What is this asking? → 📋 Formulas needed → 🔧 Setup → 📝 Full solution (every step) → ✅ Boxed answer
  - Key questions include ⚡ Quick Guide checklists (5-8 mechanical steps for similar problems)
  - Topics covered: planes, polar coords, ellipse area, chain rule, conservative fields, line integrals, Green's theorem, Stokes' theorem, Divergence theorem, surface integrals, Lagrange multipliers, critical points, potential functions, arc length, flux, triple integrals, change of variables
- **Sidebar updated** — Final Prep link activated (pending removed), sub-link "W19 · F14 · F13" added
- **Built MATH2004-notes.html** — 679KB, 23/23 fragments assembled
- Files changed: shell-head.html, chapters/final.html (76 solutions), MATH2004-notes.html

### Session 13 — May 23, 2026
- **Added Exam Intel segment to Final Prep page** — sourced from W26 Discord chat logs
  - Exam Structure: ~15 MCQ (scantron) + 4 long answer (40 marks), no minimum exam grade
  - Confirmed Long Answer Topics: (1) Continuity, (2) Critical Points/SDT, (3) Stokes' Theorem via curl, (4) Divergence Theorem on cylinder
  - High-Priority Topics table: line integrals, divergence/Stokes'/Green's theorems, formula sheet fluency, continuity, SDT, scalar triple product
  - Medium-Priority: plane intersection parameterization, cylindrical coords, change of variables, conservative fields
  - Low-Priority (deprioritize): plotting/sketching, standalone triple integrals, proofs
  - Insider Tips: questions reused from W19 final, MCQ from Lucy's tests, div F = constant shortcut, Stokes' normal from plane equation
- **Built MATH2004-notes.html** — 769KB, 27/27 fragments assembled
- Files changed: chapters/final.html, MATH2004-notes.html, progress.md
