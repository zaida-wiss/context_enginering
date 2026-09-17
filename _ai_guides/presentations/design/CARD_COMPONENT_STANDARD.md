---
name: card_component_standard
description: MANDATORY — Canonical internal layout for all presentation cards
metadata:
  type: design-specification
  critical: true
  required_before: rendering
  version: 1.0
---

# 🎴 CARD COMPONENT STANDARD

This file defines the **canonical internal structure of presentation cards**.
It applies to **all slides** that use the modern card system.

This standard exists so cards remain visually consistent, compact, readable and predictable across the entire presentation.

## Authority

For card internals, typography hierarchy, metadata placement, spacing and team-accent treatment, this file is authoritative.

It supplements `VISUAL_DESIGN_MANDATORY.md` and must be read together with `ACCESSIBILITY_NEURODIVERSITY.md`.

If a generic typography example elsewhere conflicts with this component-specific specification, use this file for card internals.

---

# 1. CARD SURFACE — GLASS STYLE

All cards use the same visual language throughout the deck:

- dark navy slide background
- translucent / glass-like dark card surface
- rounded corners
- soft shadow/depth
- subtle neutral card edge only when needed for separation
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

The card surface itself must remain visually consistent regardless of team.

---

# 2. FIT-FIRST TYPOGRAPHY HIERARCHY

The goal is that **every required line fits inside the card with even spacing**.

Do NOT create large blank gaps merely to preserve oversized metadata text.

When a card becomes tight, reduce typography in this order:

1. timestamp / date / evidence text
2. review / merged / branch metadata
3. owner + team line
4. contribution microcopy
5. card title only as a last resort

Never remove required information to make a card fit.

## Canonical sizes

### Card title
- preferred: **18–20 pt**
- bold
- high contrast (`#FFFFFF`)
- may wrap naturally
- do not shrink below **18 pt** merely to preserve a grid

### Contribution microcopy
- preferred: **11–12 pt**
- regular
- muted but WCAG-readable
- normally 1–2 visual lines

### Owner / assignee + team
Examples:
- `Tomac · Frontend`
- `Rasha · Backend`
- `Henrik · Native`

Style:
- **12–14 pt**
- semibold or bold
- high-contrast secondary color (`#CBD5E1` or brighter)
- intentionally compact

This line is important, but it does NOT need to be the same size as the card title.

### Operational metadata
Examples:
- `Merged: Zaida | Review: Björn`
- `Branch: frontend/#83-save-allocation`
- `Öppen PR · väntar på review`

Style:
- **11–12 pt**
- regular
- `#94A3B8` or another WCAG-safe secondary color
- keep short metadata on one line when practical

For merge cards use EXACT labels:

`Merged: [name] | Review: [name/status]`

Do NOT use:
- `Merged by:`
- `Reviewed by:`

### Timestamp
Style:
- **10–11 pt** preferred
- may go to **9 pt** only when the renderer/projector remains clearly readable
- muted WCAG-safe color
- lower-left area of the card
- no pill, badge or background

For merged items, timestamp has exactly two lines:

```text
14 sep
10:16
```

Do NOT prefix the timestamp with:
- `Merged`
- `Mergad`
- `Senaste commit`

The semantic meaning comes from the card/status above.

For active work / PR / issue cards, the timestamp also uses two lines when space benefits from it:

```text
17 sep
09:19
```

This represents the relevant verified activity timestamp (PR update, latest push/commit, or issue activity according to the data model).

---

# 3. CANONICAL MERGED-PR CARD

Use this hierarchy:

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
- `Merged:` + `Review:` on the same metadata row where space allows
- timestamp is bottom-left, two lines
- no `Merged`/`Mergad` prefix before date
- timestamp visually smaller than owner and title

---

# 4. CANONICAL ACTIVE ISSUE / PR CARD

Use this hierarchy:

```text
◐ #88 · Critical interactions
Testar login, målallokering och drift för kritiska MVP-flöden.

Zaida · Frontend
PR #114 · Build/frontend/#88-critical-interactions

17 sep
09:19
```

or for assigned backlog:

```text
⏳ #98 · Historisk FX-lookup
Utökar FX-motorn med historiska valutakurser upp till fem år.

Henrik · Native
Tilldelad · ingen aktiv branch verifierad

14 sep
09:47
```

Owner and timestamp use the same compact typography family as the lower metadata.
Owner keeps stronger contrast to make responsibility easy to scan.

---

# 5. EVEN VERTICAL SPACING — HARD RULE

The screenshot problem this rule prevents is uneven whitespace between lines.

Inside a card, use a predictable vertical rhythm.

Recommended visual spacing:

- title → contribution: **4–6 px**
- wrapped contribution lines: normal line spacing, no extra paragraph gap
- contribution → owner: **8–10 px**
- owner → operational metadata: **5–7 px**
- metadata rows → timestamp area: flexible remaining space
- timestamp line 1 → timestamp line 2: **0–2 px extra gap**

## Bottom anchoring

The timestamp is anchored to the **lower-left content edge** of the card.

This gives cards a stable visual baseline even when titles or microcopy wrap differently.

The content above the timestamp uses normal flow.
Do not vertically justify all rows across the full card height, because that creates large irregular gaps.

## Equal cards

When cards in a grid have equal outer height:

- keep top content aligned from the top
- anchor timestamps consistently at the bottom
- let the natural middle whitespace absorb small content-length differences
- do NOT distribute every text row evenly across the entire height

---

# 6. ALL REQUIRED ROWS MUST FIT

A card passes only when all required information is visible.

Required card fields must never be clipped or omitted only because spacing is tight.

Preferred response to tight content:

1. reduce timestamp / metadata font within this standard
2. tighten paragraph spacing to the canonical values
3. reduce owner text within its allowed range
4. reduce title from 20 pt toward 18 pt if needed
5. use fewer cards / continuation slide only when the card still cannot fit cleanly

This component intentionally allows smaller metadata than generic meeting body text because metadata is tertiary information inside a structured card.

No auto-shrink / PowerPoint shrink-to-fit is allowed. Font sizes must be set deliberately.

---

# 7. CONSISTENCY ACROSS ALL SLIDES

The same card geometry must be used throughout the entire presentation, including:

- merged PR cards
- active work cards
- backlog cards
- team detail cards
- risk cards
- decision cards
- priority/action cards
- PL-question cards
- dependency nodes where applicable

Only the **content schema and team/status accent** may change.

Do not switch from glass cards to flat bordered boxes on later slides.
Do not use full team-colored outlines on some slides and left accents on others.

---

# 8. RENDER CHECKS

Before delivery verify visually:

```text
card_glass_surface_consistent == true
team_color_left_accent_only == true
full_team_outline_count == 0
required_card_rows_missing == 0
uneven_row_spacing_caused_by_vertical_justification == 0
timestamp_bottom_left == true
timestamp_two_lines_when_time_present == true
merged_timestamp_prefix_count == 0
legacy_merged_by_label_count == 0
legacy_reviewed_by_label_count == 0
text_clipping_count == 0
```

Also verify:

- `Merged:` and `Review:` fit on one row when both are short enough
- owner line remains visually more prominent than muted metadata
- date/time remains readable but clearly tertiary
- cards look like one coherent component system across all slides

---

**Status:** PRODUCTION
**Version:** 1.0
**Last updated:** 2026-09-17
