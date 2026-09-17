---
name: card_component_standard
description: MANDATORY — Canonical internal layout for all presentation cards
metadata:
  type: design-specification
  critical: true
  required_before: rendering
  version: 1.2
---

# 🎴 CARD COMPONENT STANDARD

This file defines the **canonical internal structure of presentation cards** and applies to **all card-based slides**.

## Absolute accessibility boundary

`ACCESSIBILITY_NEURODIVERSITY.md` and WCAG 2.2 AA are an absolute hard boundary.

**No responsive fit rule may ever weaken WCAG compliance.**

Every card must satisfy at minimum:
- normal text contrast: **4.5:1**
- large text contrast: **3:1** where WCAG large-text definition applies
- information-bearing component/accent contrast: **3:1**
- color is never the sole information carrier; pair color with symbol/text
- no clipping, overlap, hidden text or illegible compression

If content cannot fit while remaining WCAG-compliant and readable, use fewer cards or a continuation slide.

---

# 1. CARD SURFACE — CALM GLASS STYLE

All cards use the same visual language throughout the deck:

- slide background `#15182E`
- primary card surface `#1E233B`
- optional alternate surface `#252A45`
- rounded corners
- soft shadow/depth
- subtle low-glare appearance
- **team color appears ONLY as a narrow vertical accent line on the left**
- team color must NOT outline the whole card
- team color must NOT fill the card

## Team accent colors

- Frontend: `#2DD4BF`
- Backend: `#FF4FA3`
- Native: `#A855F7`
- Cross-team: `#CBD5E1`
- Other / neutral: `#94A3B8`

Recommended left accent width: visually equivalent to **4–6 px**.

The card itself stays calm navy regardless of team/status/source.

---

# 2. RESPONSIVE TYPOGRAPHY — DELIBERATE, NEVER AUTO-SHRINK

The goal is that **every required line fits with even spacing and remains accessible**.

Each text role has a preferred size and a minimum size. On dense slides, the renderer may deliberately step down within the permitted range.

Do NOT use PowerPoint shrink-to-fit / automatic font reduction.

When a card becomes tight, reduce typography in this order:

1. timestamp / evidence / provenance text
2. review / merged / branch metadata
3. owner + team line
4. contribution/supporting text
5. card title only as a last resort

Never remove required information to make a card fit.

## Canonical responsive ranges

### Card title
- preferred: **18–20 pt**
- minimum: **18 pt**
- bold
- high contrast (`#F7F8FC`)
- wraps naturally

### Contribution / project-value microcopy
- preferred: **11–12 pt**
- minimum: **11 pt**
- regular
- use a WCAG-AA-safe muted color such as `#B0B8CC` or `#A2ABC0`
- normally 1–2 visual lines
- answers **what this solves/contributes in the project**

### Owner / assignee + team
Examples:
- `Tomac · Frontend`
- `Rasha · Backend`
- `Henrik · Native`

Style:
- preferred: **13–14 pt**
- minimum: **12 pt**
- semibold or bold
- high-contrast secondary color (`#D2D7E4`)

### Operational metadata
Examples:
- `Merged: Zaida | Review: Björn`
- `Branch: frontend/#83-save-allocation`
- `Öppen PR · väntar på review`

Style:
- preferred: **11–12 pt**
- minimum: **10 pt**
- regular
- WCAG-AA-safe secondary color (`#B0B8CC`)
- keep short metadata on one line when practical

For merge cards use EXACT labels:

`Merged: [name] | Review: [name/status]`

Do NOT use:
- `Merged by:`
- `Reviewed by:`

### Timestamp / provenance / source labels
Style:
- preferred: **10–11 pt**
- minimum: **10 pt**
- WCAG-AA-safe muted color
- no pill/background required

**Never go below 10 pt in this component system.** If 10 pt does not fit or is not comfortably readable in the actual rendered/projected context, change layout or paginate.

---

# 3. TIMESTAMP STANDARD

For merged items, timestamp is bottom-left and exactly two lines:

```text
14 sep
10:16
```

Do NOT prefix it with:
- `Merged`
- `Mergad`
- `Senaste commit`

For active work / PR / issue cards, the relevant verified activity timestamp may use the same two-line structure:

```text
17 sep
09:19
```

The semantic meaning comes from the surrounding card content.

---

# 4. CANONICAL MERGED-PR CARD

```text
#80 · Drift från live target
Beräknar drift från aktuell målallokering i stället för mock-flagga.

Tomac · Frontend
Merged: Zaida | Review: ej verifierat

14 sep
10:16
```

Rules:
- title first
- contribution directly below title
- owner/team below contribution
- `Merged:` + `Review:` on the same row when practical
- timestamp lower-left in two lines
- no merge-prefix before date

---

# 5. CANONICAL ACTIVE ISSUE / PR CARD

```text
◐ #88 · Critical interactions
Testar login, målallokering och drift för kritiska MVP-flöden.

Zaida · Frontend
PR #114 · Build/frontend/#88-critical-interactions

17 sep
09:19
```

or:

```text
⏳ #98 · Historisk FX-lookup
Utökar FX-motorn med historiska valutakurser upp till fem år.

Henrik · Native
Tilldelad · ingen aktiv branch verifierad

14 sep
09:47
```

Owner keeps stronger contrast than lower metadata.

---

# 6. CANONICAL DEPENDENCY NODE

Dependency nodes use the same calm card system but may be more compact horizontally.

Required structure:

```text
API-kontrakt
Definierar endpoints + payload för integrationen.
🔴 behöver låsas
```

```text
Riktig Java HTTP
Byter mock mot riktig Backend-kommunikation.
⏳ väntar
```

```text
#106 HttpOnly auth
Flyttar auth till säkrare cookie-baserad lösning.
⏳ efter integration
```

Hard rules:
- title first
- **project-value line immediately below title**
- status/dependency line under that
- value line is mandatory whenever source evidence is sufficient
- if evidence is insufficient, use `Bidrag till projektet behöver verifieras.`
- arrows/connectors sit outside cards and must not overlap text
- compact node layout may use smaller allowed metadata sizes, but not below component minima

---

# 7. EVEN VERTICAL SPACING — HARD RULE

Inside a card, use a predictable vertical rhythm.

Recommended visual spacing:
- title → contribution/project-value line: **4–6 px**
- wrapped text: normal line spacing, no extra paragraph gap between wrapped lines
- contribution → owner/status: **7–10 px**
- owner → operational metadata: **4–7 px**
- metadata → timestamp/provenance area: flexible remaining space
- timestamp line 1 → line 2: **0–2 px** extra gap

Do not vertically justify all rows across the entire card height.

When equal-height cards are used:
- top-align primary content
- bottom-anchor timestamps where applicable
- allow middle whitespace to absorb small content-length differences
- never distribute text rows evenly from top to bottom

---

# 8. RESPONSIVE CARD GEOMETRY — GLOBAL RULE

Cards are content-driven responsive components.

Allowed adaptations:
- natural text wrapping
- card grows in height
- card becomes wider through a lower-density grid
- 2×2 → 2×1 → 1×1 when content requires it
- dependency nodes widen/grow so the project-value line remains readable
- continuation slide when minimum accessible layout still does not fit

Fit order:
1. start with preferred typography
2. reduce only within the explicit ranges above
3. use compact canonical spacing
4. adapt card/grid dimensions
5. paginate

Never:
- clip text
- overlap text
- omit required rows
- omit project-value microcopy from a dependency node to save space
- reduce below component minimums
- reduce contrast below WCAG AA
- use color alone to communicate meaning
- use automatic shrink-to-fit

---

# 9. CONSISTENCY ACROSS ALL SLIDES

The same card geometry and responsive behavior apply throughout the deck, including:

- merged PR cards
- active work cards
- backlog cards
- team detail cards
- risk cards
- decision cards
- sprint-plan cards
- priority/action cards
- next-step cards
- PL-question cards
- dependency nodes

Only content schema and justified status/team/source accents may change.

Do not switch later slides to flat bordered boxes or full team-colored outlines.
Do not switch back to the old navy palette on later slides.

---

# 10. RENDER CHECKS

Before delivery verify:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
card_glass_surface_consistent == true
calm_navy_palette_consistent == true
team_color_left_accent_only == true
full_team_outline_count == 0
required_card_rows_missing == 0
missing_dependency_project_value_microcopy_count == 0
uneven_row_spacing_caused_by_vertical_justification == 0
timestamp_bottom_left == true
timestamp_two_lines_when_time_present == true
merged_timestamp_prefix_count == 0
legacy_merged_by_label_count == 0
legacy_reviewed_by_label_count == 0
font_below_component_minimum_count == 0
text_clipping_count == 0
```

Also verify:
- all muted text still meets **4.5:1** when treated as normal text
- `Merged:` and `Review:` fit on one row when practical
- owner remains more prominent than muted metadata
- dependency nodes contain a readable project-value line
- cards form one coherent component system across all slides

---

**Status:** PRODUCTION
**Version:** 1.2
**Last updated:** 2026-09-17
