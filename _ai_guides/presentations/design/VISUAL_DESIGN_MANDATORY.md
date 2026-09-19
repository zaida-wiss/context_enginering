---
name: visual_design_mandatory
description: MANDATORY — Canonical global slide layout and visual constants
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 5.2
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

The deck uses:
- calm deep navy canvas
- soft dark glass-like cards
- rounded corners
- subtle depth/shadow
- low-glare surfaces
- clear hierarchy
- responsive cards
- cards and responsive card grids as the primary visual language across the deck
- chronology, dependencies and risk normally communicated within the shared card/grid grammar through ordering, grouping, headings, symbols and optional connectors
- meeting point 9 priority uses its registered vertical execution-group exception while retaining the same card components
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
- the normal slide-level composition is responsive card/grid
- meeting point 9 is the explicit registered exception: its execution groups are vertically stacked top-to-bottom while still using the same card components
- no arbitrary redesign from one slide to the next

One work/information item = one card unless a compact grouped card is explicitly allowed by the slide-content authority.

### Stable slide zones — NPF predictability

Every rendered meeting slide uses the same three spatial zones:

1. **Header zone** — meeting-point title, optional subordinate subtitle and local page counter.
2. **Content zone** — card-based content using the default responsive grid or a registered slide-level exception such as point 9.
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

## 2. CANONICAL PALETTE

| Element | Hex | Role |
|---|---|---|
| Slide background | `#15182E` | calm deep navy canvas |
| Card surface | `#1E233B` | primary card surface |
| Alternate card surface | `#252A45` | optional subtle variation |
| Decorative card edge | `#33405D` | non-semantic separation |
| Meaningful neutral divider | `#7F8AA6` | structural meaning when needed |
| Main text | `#F7F8FC` | titles / primary content |
| Secondary text | `#D2D7E4` | supporting information |
| Metadata text | `#B0B8CC` | metadata |
| Quiet microcopy/timestamp | `#A2ABC0` | tertiary content, still WCAG-safe |

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

Palette rules:
- same background/card family across the entire deck
- no black/high-glare cards
- transparency must preserve contrast
- actual rendered colors must pass WCAG
- priority must never be communicated by color alone; size/weight/spacing and labels support the hierarchy

---

## 3. CARD SURFACE — GLOBAL APPEARANCE ONLY

### Shape
- rounded corners, visually around **16–20 px**
- content-driven height
- subtle shadow/depth
- no fixed height that forces clipping

### Team accent and issue/PR identifiers
Team ownership is shown with a narrow left accent and, on issue/PR cards, the
same team color on the `#NUMBER`:
- Frontend `#2DD4BF`
- Backend `#FF4FA3`
- Native `#A855F7`
- Cross-team `#CBD5E1`
- Neutral `#94A3B8`

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
- section header: **22 pt minimum**, bold

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
  - `Mergat till C/C++-Native`
  - `Mergat till Java-Development-Environment`
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

## 4B. POINT 2 — SHARED CARD/GRID COMPOSITION

Meeting point 2 uses the same responsive card/grid language as the rest of the deck.

Chronology is communicated by:
- left-to-right or top-to-bottom card order;
- clear date/time labels inside each card;
- compact phase/month headings when useful;
- status symbol + text + color;
- an explicit `AKTUELL SPRINT` card/badge when current position needs emphasis.

Do not require a full-slide timeline. If chronology needs more space, paginate
into continuation slides while preserving card order.

Nearest-focus items use the same card component standard, with stronger hierarchy
for the nearest consequential deadline.


---

## 5. CARD GRIDS — MAXIMUM DENSITY, NOT TARGET

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
- six cards is the standard capacity per physical slide; meeting point 1 has no total card or slide limit
- use six when at least six grounded items exist and all six remain readable
- team-summary AI cards are required content in the final point-1 subsection, not filler
- point-1 subsection meaning comes from its canonical subtitle/verified merge target, never from a hard-coded continuation letter
- never create unrelated filler cards merely to reach six
- preferred layout may be 3×2 when readable; card geometry remains responsive
- if more than six grounded items exist, create as many lowercase-letter continuation slides as required
- if six cards do not fit within WCAG/readability rules, use fewer per physical slide and continue; never omit a grounded item because of density

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

Do not duplicate the full render-gate checklist here.

---

## CORE PRINCIPLE

**Calm navy canvas + soft cards + clear hierarchy + responsive geometry + accessible rendering.**

Card internals are governed by `CARD_COMPONENT_STANDARD.md`; global design must not redefine them.

---

**Status:** PRODUCTION
**Version:** 5.2
**Last updated:** 2026-09-17
