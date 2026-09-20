---
name: visual_design_mandatory
description: MANDATORY — Canonical global slide layout and visual constants
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 5.8
---

# 🎨 VISUAL DESIGN MANDATORY

This file is the **single authority for global presentation appearance**.

It owns:
- global palette
- slide background
- card surface family
- global slide-title and section-title roles
- maximum card density / grid behavior
- global visual consistency

It does **not** own card-internal spacing, card-internal type sizes, assignee emphasis, merge/review formatting or timestamp placement. Those belong exclusively to `CARD_COMPONENT_STANDARD.md`.

If a card-internal example in this file ever conflicts with `CARD_COMPONENT_STANDARD.md`, the card standard wins.

## Absolute rule: WCAG first

`ACCESSIBILITY_NEURODIVERSITY.md` and WCAG 2.2 AA are above all visual preferences.

At minimum:
- normal text contrast >= **4.5:1**
- WCAG large text contrast >= **3:1**
- information-bearing components >= **3:1**
- color is never the sole information carrier
- no clipping, overlap or hidden text

If a layout cannot satisfy these rules, change the layout or paginate.

---

## 1. GLOBAL VISUAL LANGUAGE

The global presentation design uses:
- calm deep navy canvas
- soft dark glass-like cards
- rounded corners
- subtle depth/shadow
- low-glare surfaces
- clear hierarchy
- sufficient internal padding
- no decorative layer crossing readable text
- no clipping, overlap or visual corruption

Projects may add semantic accents and project-specific composition, but must preserve
this global visual foundation unless a future explicit framework decision replaces it.
- responsive cards
- cards are the shared component language across the deck, but **slide geometry is owned by the active meeting-point contract**
- responsive card grids are the default only when no meeting-point-specific geometry is registered
- chronology, dependencies, planning and priority use the geometry required by their meeting-point authority; the global visual system must not flatten those formats into a generic grid
- registered meeting-point formats such as a chronological timeline, dependency view, vertical execution sequence or chronological day-plan remain mandatory while reusing the shared card components
- deliberate whitespace that creates grouping and breathing room instead of decorative emptiness

### NPF-first visual composition

Every slide must pass a quick-scan test:
- one dominant purpose is recognizable within a few seconds
- the eye has a clear entry point and reading direction
- no more than one primary visual emphasis competes for attention
- related information is spatially grouped
- unrelated information is visibly separated
- recurring symbols, colors and component positions keep the same meaning
- decorative elements never compete with data or provenance
- dense content is paginated instead of compressed

The deck must feel **predictable and structurally consistent**:
- stable header, palette, card language, provenance grammar and grid behavior
- the same card system is reused across meeting points
- the normal slide-level composition is responsive card/grid **only when the meeting-point authority does not define a stricter format**
- meeting-point-specific geometry is stable semantics, not decoration, and must survive refactoring
- examples include point ② chronological timeline, point ⑥ dependency structure, point ⑨ vertical execution sequence and point ⑫ chronological day/plan sequence when required by their active contracts
- no arbitrary redesign from one slide to the next

One work/information item = one card unless a compact grouped card is explicitly allowed by the slide-content authority.

### Stable slide zones — NPF predictability

Every rendered meeting slide uses the same three spatial zones:

1. **Header zone** — meeting-point title, optional subordinate subtitle and local page counter.
2. **Content zone** — content using the geometry required by the active meeting-point contract; use the responsive grid only as the fallback when no stricter geometry is registered.
3. **Source/footer zone** — compact provenance/source summary and quiet operational metadata when required.

Hard rules:
- the three zones keep the same top-to-bottom order across the deck;
- content never intrudes into the header or footer zone;
- footer/source content never competes visually with the main content;
- continuation slides preserve the same zone geometry;
- decorative elements may not create a false fourth primary zone.

### Five-second scan test — NPF design gate

A slide must be understandable at a glance before detailed reading.

Within approximately five seconds, a viewer should be able to identify:
- which meeting point they are on;
- the slide's one main purpose;
- the most important card/group;
- the intended reading order;
- whether the content is fact, status, analysis or proposal where that distinction matters.

If this is not possible, reduce competing emphasis, simplify grouping, increase
whitespace, lower card density or continue onto another slide.

The five-second test does not justify removing required provenance or project-value
microcopy; it is a hierarchy/composition test, not a content-deletion rule.

---

## 1B. GLOBAL DESIGN INHERITANCE AND PROJECT OVERRIDES — HARD RULE

Global presentation design is the default for every project.

A project may add project-specific composition, semantics or visual rules. A project
may also intentionally override a global design rule, but such a conflicting
override is never applied silently or automatically.

When a project rule conflicts with an active global design rule:
1. stop before rendering or changing the effective design;
2. show the concrete global rule and the conflicting project rule;
3. explain the visible consequence of choosing either;
4. ask the user an explicit control question;
5. apply the project override only after the user explicitly approves that deviation.

Without explicit approval, the global design wins by default.

An approved override is scoped to the project unless the user explicitly says the
global framework itself should change. Accessibility, source integrity, conflict
handling and other non-design safety/quality authorities remain governed by their
own authority rules.

## 2. CANONICAL PALETTE

| Element | Hex | Role |
|---|---|---|
| Slide background — upper tone | `#1E274A` | modern navy field; never black |
| Slide background — lower tone | `#111A33` | deeper navy field; never black |
| Card surface | `#263352` | frosted-glass primary tint |
| Alternate card surface | `#2E3B5F` | optional frosted-glass variation |
| Glass highlight / border | `#60769B` | subtle luminous separation, non-semantic |
| Meaningful neutral divider | `#91A0BC` | structural meaning when needed |
| Main text | `#F7FAFF` | titles / primary content |
| Secondary text | `#D8E2F2` | supporting information |
| Metadata text | `#C3D0E3` | metadata |
| Quiet microcopy/timestamp | `#B9C6DA` | tertiary content, still WCAG-safe |

### Four-level text-color hierarchy

| Priority | Content | Palette role |
|---:|---|---|
| 1 | Issue title, assignee | Main text |
| 2 | `⭐ AI-förslag` and proposed new issues | Main/secondary text with proposal symbol and controlled emphasis |
| 3 | Merge/review, pedagogical explanation, `🔎 AI-analys` | Secondary text |
| 4 | Sources/provenance, branch, timestamp, technical metadata | Metadata or quiet microcopy |

Level 4 is the least prominent treatment, but its rendered text must still meet
WCAG 2.2 AA. Do not lower opacity or contrast until it nearly disappears.

### School/submission-task priority palette

Priority color is permitted specifically for school assignments, submission
tasks and course deadlines when paired with an explicit priority symbol/text.

- **Priority 1 / critical:** red `#EF4444`
- **Priority 2 / important upcoming:** orange `#F59E0B`
- **Priority 3 / lower urgency:** green `#22C55E`

Required visible form: symbol + text, e.g. `● PRIORITET 1`.
Never show a colored dot/bar without the text meaning.
Do not reuse team colors as priority colors.
Red remains reserved for critical/high-consequence semantics.

The canonical school-task metadata symbols are:
`🎯 task · 🕒 time · 📍 place · 💡 purpose · 🛠 method`.
These symbols replace repeated text labels such as `VAD / NÄR / VAR / VARFÖR / HUR`
on school/submission cards, while the underlying five meanings remain mandatory.

### Background rendering contract — mandatory

The canonical background is a **modern rounded glass-look navy field**, never
black, charcoal-black or near-black.

Canonical background treatment:
- use a restrained navy gradient from approximately `#1E274A` to `#111A33`;
- the lighter `#1E274A` tone should remain visible enough that the deck reads as
  blue/navy rather than almost black;
- the darker `#111A33` tone provides depth but must not dominate the entire slide;
- the gradient may be linear or softly radial, but must remain calm and low-glare.

Required behavior:
- the rendered slide must visibly read as **blue/navy**, not neutral black;
- tonal variation stays subtle and non-semantic;
- cards remain visually distinct from the background while preserving WCAG contrast;
- if an implementation cannot render the gradient reliably, fall back to a solid
  navy sampled from the canonical range, preferably `#18213E`; never fall back to black;
- no rendered slide may use `#15182E` as a hard lock if doing so makes the result
  visually darker than the approved modern navy range.

Forbidden:
- `#000000` or visually black slide backgrounds;
- charcoal/graphite fields that read as black;
- black-to-navy gradients;
- high-glare neon/bright gradients;
- decorative texture that reduces text legibility.

Palette rules:
- same modern navy/glass family across the entire deck;
- no black/high-glare cards;
- transparency must preserve contrast;
- actual rendered colors must pass WCAG 2.2 AA;
- normal text contrast must be >= **4.5:1**;
- WCAG large text contrast must be >= **3:1**;
- on dark/navy cards and slide backgrounds, primary/secondary/metadata text must
  use the approved light palette roles; **black or near-black text is forbidden**;
- dark text is permitted only on an explicitly light surface where the resulting
  contrast independently passes WCAG;
- when a text-color choice is ambiguous on a dark surface, use the approved light
  text role rather than a dark neutral;
- priority must never be communicated by color alone; size/weight/spacing and labels support the hierarchy

---

## 3. CARD SURFACE — GLOBAL APPEARANCE ONLY

### Shape
- rounded corners, visually around **16–20 px**
- content-driven height
- subtle shadow/depth
- no fixed height that forces clipping

### Rendered card-surface fidelity — hard gate

The words **glass-like**, **rounded** and **responsive** are render requirements,
not optional mood-board language. A deck fails visual verification when its cards
collapse to flat rectangular panels merely to increase density.

Every ordinary rendered card must preserve:
- a visibly rounded silhouette equivalent to approximately **16–20 px** corner radius;
- a modern **frosted-glass / glassmorphism** surface distinct from the navy canvas and from opaque flat panels;
- a semi-transparent blue/navy tint visually equivalent to the `#263352` / `#2E3B5F` family;
- a restrained light edge/highlight, approximately the `#60769B` family, to create the frosted-glass boundary;
- subtle depth through restrained shadow + highlight and/or tonal/transparency layering while preserving WCAG contrast;
- no heavy black shadow, no opaque charcoal slab and no flat-black card fallback;
- primary text on the glass surface uses `#F7FAFF` or an equivalent verified light text role; supporting text uses the approved lighter secondary/metadata roles;
- black or near-black card text on these dark glass surfaces is a visual failure;
- content-driven responsive geometry: card height/width adapts to wrapped content and required bottom zones;
- all required text remains inside the visible rounded card bounds with approved padding; no text may touch/cross the rounded edge;
- density changes may resize/reflow cards, but MUST NOT remove corner rounding, glass/depth treatment, padding, required rows or readable hierarchy.

A platform that cannot apply a true backdrop blur MUST still reproduce the
**visual effect** of frosted glass through semi-transparent navy tint, restrained
highlight/border, soft depth and controlled tonal layering. True blur is not
required; the perceived frosted-glass treatment is.

For any project-owned card geometry, **design fidelity is part of fit**. If the
registered geometry fits only by removing the project's required visual treatment,
reducing required padding, clipping text or degrading typography, the render has
failed. Follow the project's pagination/continuation rule rather than silently
changing its visual contract.

### Team accent and issue/PR identifiers
Team ownership is shown with a narrow left accent and, on issue/PR cards, the
the same team color on the `#NUMBER`. Team labels, team colors and the neutral
accent are resolved from the selected project's registered team visual identity.
This generic authority must not embed project-specific mappings.

Do not use full team-colored outlines or team-colored card fills.
Color is supplementary: the visible team column/section or a text label must
also identify ownership. Every colored identifier must meet WCAG 2.2 AA.

All internal card rules are delegated to `CARD_COMPONENT_STANDARD.md`.

---

## 4. GLOBAL TYPOGRAPHY

### One primary font family per deck

All presentation-authored text uses one primary readable sans-serif font family
throughout the deck.

Allowed exception:
- a fallback font may be used only when the primary font cannot render a required
  symbol/glyph correctly;
- the fallback must be visually compatible and limited to the affected glyph/run.

Forbidden:
- switching font families between meeting points for decoration;
- using a different font family to make text fit;
- mixing decorative/display fonts into ordinary meeting content.

Font-family consistency is an NPF predictability rule. Fit problems are solved by
wording, geometry, density or pagination — never by font-family substitution.



This file owns only slide-level roles:
- slide title/header: **36 pt**, bold — this is both the preferred and minimum size
- section header: **24 pt minimum**, bold
- ordinary slide/card body text should normally render at **20 pt or larger**
- supporting metadata should normally render at **18 pt or larger**

The body/metadata values above are presentation-level readability targets.
Component-specific authorities may require larger text. They must not be used to
justify shrinking required component text below its owning hard minimum.

### Distance-readability rule — mandatory

A meeting presentation is designed to be read on a shared screen, not only on
the author's laptop.

If ordinary content would need to become smaller than the readability targets:
1. shorten non-essential wording without removing meaning;
2. reduce cards/items on the physical slide;
3. enlarge the card/content area;
4. create continuation slides.

**More slides are preferred to smaller text.** Dense dashboard-style layouts
that technically fit but require close reading are a render failure.

### Slide-title hard rule

Slide titles are **never a responsive fit variable**.

Never shrink a slide title below 36 pt because content is crowded.
Never use automatic shrink-to-fit on slide titles.

If a title does not fit at 36 pt:
1. shorten the wording without losing meaning
2. widen or reposition the title zone
3. reduce slide content density
4. create a continuation slide

For every card-internal role, including title, pedagogical explanation, assignee/developer, operational metadata and timestamp, use **only** `CARD_COMPONENT_STANDARD.md` plus the hard readability minima in `READABILITY_HARD_RULES.md`.

Do not duplicate those numeric card-internal rules here.

---

## 4A. MEETING-POINT HEADER HIERARCHY

Rendered meeting slides use a two-level header hierarchy.

### Primary header — meeting point only
- contains the ordinary Arabic meeting-point number + canonical meeting-point title
- examples: `✏️ 1. Avklarat sedan förra mötet`, `✏️ 2. Nuläge och deadlines`
- the continuation letter does **not** belong in this primary header
- primary header remains 36 pt minimum

### Secondary subtitle — physical page topic
- sits directly below the primary header
- smaller and calmer than the meeting-point header
- continuation letter belongs here, not beside the meeting-point number
- examples:
  - `Mergat till {COLLECTION_BRANCH_A}`
  - `Mergat till {COLLECTION_BRANCH_B}`
  - `Teamsammanfattning till mötesprotokollet`

### Per-meeting-point page counter
- show a compact counter at the far right of the primary-header row
- format: `(x/y)`, where x = this physical page within the meeting point and y = total physical pages belonging to that meeting point
- example: `(4/6)`
- this counter uses **visual priority level 4**: quiet, readable metadata
- it must never compete with the meeting-point title
- count only physical pages belonging to that meeting point
- do not use the deck-wide slide number for this counter

Canonical example:

```text
✏️ 1. Avklarat sedan förra mötet                            (4/6)
Teamsammanfattning till mötesprotokollet
```

---

## 4B. POINT 2 — CHRONOLOGICAL TIMELINE FORMAT

Meeting point 2 follows the stricter Monday-meeting content/structure authority.
Its primary visual is a **true chronological course/project timeline** covering
the registered course/project period required by `SLIDE_DETAIL_SPEC.md` and
`COMPOSITION_ARCHITECTURE.md`.

The global card system still governs the appearance of timeline nodes/cards, but
it MUST NOT replace the timeline with an ordinary 2×2, 3×2 or other generic grid.

Required:
- chronological direction is visually explicit through a line/axis/connector and ordered nodes;
- dates/times are visible at the relevant timeline positions;
- the current week/sprint position is visibly marked;
- status uses symbol + text + semantic color;
- the nearest consequential deadline receives stronger hierarchy;
- continuation slides preserve chronological continuity when needed.

If the timeline becomes dense, paginate or segment the chronology. Never solve
density by converting it into an unrelated dashboard/grid.


---

## 5. CARD GRIDS — MAXIMUM DENSITY, NOT TARGET

### Meeting-point geometry precedence — hard rule

Before choosing a slide layout, resolve the active meeting-point contract.

Precedence:
1. meeting-point-specific geometry in the Monday-meeting structure/content authorities;
2. registered slide-level exceptions;
3. global responsive card/grid fallback.

The global design authority may style a specialized format but may not replace
its semantic geometry. A timeline remains a timeline; a dependency view remains
a dependency view; a vertical priority sequence remains vertical; a
chronological day/plan sequence remains chronological.

### Meeting point 9: vertical priority sequence

Meeting point 9 is an explicit slide-level exception to the general responsive
grid. It uses vertically stacked execution groups in this order:

1. `Prioritering först`
2. `Parallellt`
3. `Backlog — lägre prioritet`
4. `Förslag framåt — finns ännu inte / behöver korrigeras`

Cards remain the component language inside each group.

Hard rules:
- execution groups read top-to-bottom;
- a 2×2/four-quadrant arrangement of the four groups is forbidden;
- priority remains clear without relying on color alone;
- paginate when needed instead of shrinking below readability minima.


### Meeting point 1
- card capacity, slot orientation and pagination are owned by the active project presentation authority when registered
- team-summary AI cards are required content in the final point-1 subsection, not filler
- point-1 subsection meaning comes from its canonical subtitle/verified merge target, never from a hard-coded continuation letter
- never create unrelated filler cards merely to satisfy a visual slot count
- never omit a grounded item because of density
- global readability, source-footer, overlap and clipping gates remain mandatory regardless of project geometry

### ②–⑧, ⑩–⑫ and ⑭
- maximum 4 cards unless slide authority is stricter
- lower density when text length requires it

The registered vertical execution-group exception above governs meeting point 9,
not the ninth physical slide in the deck.

### ⑬ next steps
- 4×1 only when each card remains readable
- otherwise 2×2 or continuation

### ⑥A dependency diagram
- graph allowed
- maximum 3–4 chains per slide
- nodes remain card components

---

## 6. PROJECT-VALUE EXPLANATION

Issue/PR/Merge cards, dependency nodes and action/next-step cards must explain what the work contributes when source evidence supports it.

Content rule:
- short, grounded, plain Swedish
- directly connected to the title
- answer what it concerns and why it matters to the project
- no invented impact

**Placement, font size and spacing are owned by `CARD_COMPONENT_STANDARD.md` and `READABILITY_HARD_RULES.md`.**

Evidence grounding order:

Issue:
1. issue title/body/acceptance criteria
2. linked PR
3. verified branch/commits

PR:
1. PR title/body
2. changed files/diff
3. linked issue
4. commits

Merged PR:
1. merged PR title/body + changed files
2. linked issue
3. commits

---

## 7. PROVENANCE

Source identity is owned by `PROVENANCE_AND_AI_LABELING.md`.

Color may support source/status meaning but never replace icon + text where provenance must be visible.

---

## 8. STATUS VISUALS

Status must use symbol + text when status is shown.

For meeting point 2 status semantics, the stable status colors are:
- green = completed/passed
- orange = checkpoint/feedforward/intermediate milestone
- red = critical deadline/major delivery

The active-sprint locator is neutral and separate from these status colors.

Examples:
- ✅ klart/merged
- ◐ pågår
- ⏳ väntar/beroende
- 🔴 blockerad/kritisk
- ? oklar

Do not use color alone.

Evidence strength levels from `ACTIVE_WORK_DETECTION_MODEL.md` are **internal data classification**, not visible status labels.

---

## 9. RESPONSIVE FIT ORDER

When content is dense:
1. keep slide title fixed at 36 pt
2. keep required content
3. wrap naturally
4. start normal/card text at preferred sizes and reduce only when required
5. follow card-specific typography/spacing rules in `CARD_COMPONENT_STANDARD.md` and `READABILITY_HARD_RULES.md`
6. let cards grow
7. reduce grid density
8. paginate

Forbidden:
- shrinking slide titles
- clipping
- overlap
- missing content
- automatic shrink-to-fit
- typography below the owning component minimum
- contrast below WCAG AA
- removing required provenance
- removing pedagogical explanation to save space

---

## 10. TEXT BOX RULE

Ordinary slide titles, captions and footers:
- transparent fill
- no decorative border
- no unnecessary panel behind text

### Reserved source footer

Every physical slide reserves a bottom footer container for the sources used on
that slide. The content canvas and all cards end above this container. The
footer may wrap and grow upward only after card layout has been recalculated;
it may never overlay cards or extend outside the slide.

Verified sources retain their canonical symbols. Expected sources that could
not be verified use `⚠`, explicit failure text and a struck-through source name.
The footer is priority level 4 but remains WCAG-readable.

Visible card surfaces are reserved for actual information components.

---

## 11. RENDER GATE HANDOFF

Detailed mechanical checks live only in `verification/RENDER_GATE_CHECKLIST.md`.

This file requires globally:
- canonical palette consistent
- card system consistent
- WCAG AA pass
- no high-glare surfaces
- no full team outlines
- slide titles remain at 36 pt or larger
- slide titles are never shrunk for fit
- slide-level typography minimums respected
- background visibly modern navy in the approved `#1E274A` → `#111A33` family; black/near-black fallback count = 0
- dark-surface black/near-black text count = 0; primary/secondary/metadata text uses approved light palette roles
- cards preserve the global rounded frosted-glass/glassmorphism treatment, subtle light edge/depth and global contrast/readability gates
- distance-readability pass: ordinary body text targets >= 20 pt and metadata targets >= 18 pt; paginate before compression
- school/submission cards containing the five required meanings use the canonical symbols `🎯 🕒 📍 💡 🛠` rather than repeated VAD/HUR/VARFÖR/NÄR/VAR labels
- every rendered urgency/priority state uses both semantic text/symbol and the canonical red/orange/green urgency color

Do not duplicate the full render-gate checklist here.

---

## CORE PRINCIPLE

**Modern navy canvas + rounded frosted-glass cards + clear hierarchy + responsive geometry + WCAG-safe light text.**

Card internals are governed by `CARD_COMPONENT_STANDARD.md`; global design must not redefine them.

---

**Status:** PRODUCTION
**Version:** 5.2
**Last updated:** 2026-09-17
