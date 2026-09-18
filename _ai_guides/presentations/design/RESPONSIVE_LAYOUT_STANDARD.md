---
name: responsive_layout_standard
description: RETIRED — responsive rules moved to LAYOUT_OVERFLOW_GUARD.md and active authorities
metadata:
  type: retired_reference
  status: retired
  version: 1.0
---

# 📐 RESPONSIVE LAYOUT STANDARD

> **RETIRED. DO NOT USE FOR PRODUCTION.** Mechanical fit is owned by
> `monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md`; global layouts are owned by
> `VISUAL_DESIGN_MANDATORY.md`.

This file applies to **every slide in the presentation**.
Its purpose is simple: all required content must fit cleanly, with even spacing, without clipping or awkward empty gaps.

## 1. CORE RULE

Slides are responsive systems, not fixed screenshots.

For every slide:
- text size adapts to the amount of content
- cards/boxes adapt their width and height to content
- grid density adapts before content is clipped
- all required rows remain visible
- spacing remains even and intentional

When a slide has a lot of text, use the **defined minimum text sizes deliberately** instead of keeping oversized text that causes clipping or uneven spacing.

Do NOT use automatic PowerPoint shrink-to-fit. Font sizes must be chosen explicitly.

---

## 2. GLOBAL ADAPTIVE TYPOGRAPHY

Use the largest size that fits comfortably. If the slide/card is dense, reduce stepwise down to these minimums.

| Element | Preferred | Dense slide minimum |
|---|---:|---:|
| Slide title | 30–32 pt | **26 pt** |
| Section heading | 20–22 pt | **18 pt** |
| Card title / key question | 18–20 pt | **16 pt** |
| Important body / action text | 14–16 pt | **12 pt** |
| Owner / team / important metadata | 12–14 pt | **11 pt** |
| Secondary metadata / branch / review | 11–12 pt | **10 pt** |
| Timestamp / evidence / source label | 10–11 pt | **9 pt** |
| Footer | 10–11 pt | **9 pt** |

WCAG contrast requirements remain mandatory at every size.

### Reduction order

When content is tight, reduce in this order:
1. timestamp / footer / evidence
2. secondary metadata
3. owner/team metadata
4. normal body text
5. card title
6. section heading
7. slide title only if necessary

Never make tertiary metadata larger than needed while body text is clipping.

---

## 3. RESPONSIVE CARDS / BOXES

All card-based slides must calculate layout from content length.

### Card behavior
- height is content-driven
- width adapts to the selected grid
- text wraps naturally
- no fixed internal text-box height that can clip
- top padding and bottom padding remain visually balanced
- rows use normal flow; do not vertically justify rows across the entire card
- timestamps may anchor bottom-left when that card schema uses timestamps

### Grid behavior
Start from the slide's preferred layout, then adapt if text is dense:

`3×2 → 2×2 → 2×1 / 1×2 → 1×1 → continuation slide`

Use the layout that gives the content enough room at or above the dense-slide minimum sizes.

The slide-specific maximum item count still applies, but there is no requirement to fill every available grid cell.

---

## 4. FIT DECISION ALGORITHM — ALL SLIDES

For every physical slide:

1. Render at preferred typography.
2. If any required text wraps badly, clips, collides or creates visibly uneven spacing, reduce typography stepwise within the allowed ranges.
3. Recalculate card height/width and grid.
4. If everything fits cleanly at or above minimums: use that layout.
5. If it still does not fit: reduce card count and create a continuation slide.

A continuation slide is the final response, not the first response.

---

## 5. EVEN SPACING

All slides must use a consistent vertical rhythm.

Inside cards:
- title → body/microcopy: 4–6 px
- wrapped lines: normal line spacing, no extra paragraph gap
- body → owner/primary metadata: 6–10 px
- adjacent metadata rows: 4–7 px
- card content must not be spread using `space-between`/vertical justification

Between cards:
- use consistent gaps across the grid
- cards in the same row should align visually where practical
- a short card may contain natural unused space, but text rows must not be artificially spread apart

---

## 6. ALL REQUIRED CONTENT MUST FIT

A slide fails if any required line is:
- clipped
- outside its card
- hidden behind another element
- omitted because the card was too small
- forced into an unreadably tight line-height

A slide also fails if oversized text creates large irregular blank gaps while required lines are crowded elsewhere.

---

## 7. APPLIES TO EVERY SLIDE TYPE

This standard applies to:
- cover information blocks
- merged PR cards
- active work cards
- backlog/cross-team cards
- team detail cards
- blockers and dependencies
- risk cards
- capacity cards
- prioritization cards
- technical decisions
- sprint goals
- sprint plan
- next-step cards
- PL-question cards
- dependency nodes

No slide may opt out merely because an older example used fixed text sizes.

---

## 8. RENDER GATE

Before delivery verify:

```text
text_clipping_count == 0
text_overlap_count == 0
text_outside_card_count == 0
missing_required_row_count == 0
font_below_dense_minimum_count == 0
uneven_row_spacing_caused_by_vertical_justification == 0
responsive_card_fit_pass == true
```

If a slide fails:
1. reduce text deliberately within allowed ranges
2. resize/reflow cards
3. reduce grid density if needed
4. add continuation slide only if still necessary
5. rerender and inspect again

---

**Status:** PRODUCTION
**Version:** 1.0
**Last updated:** 2026-09-17
