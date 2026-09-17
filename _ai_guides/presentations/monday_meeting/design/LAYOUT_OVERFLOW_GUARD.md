---
name: layout_overflow_guard
description: Hard render rules that prevent text overlap, clipping, and accidental multi-column compression
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 1.0
---

# 🚨 LAYOUT OVERFLOW GUARD — No Overlap, No Compression

This file is a HARD RENDER GATE for Monday meeting presentations.

If this file conflicts with an older example, mockup, template, or slide-specific wording, this file wins together with `VISUAL_DESIGN_MANDATORY.md` and `ACCESSIBILITY_NEURODIVERSITY.md`.

---

## 1. Absolute rule

When content does not fit on one physical slide:

> Create a continuation slide. Never shrink, overlap, clip, compress, or reduce spacing.

A presentation with one extra slide is correct.
A presentation with overlapping text is invalid.

---

## 2. Allowed layout families

### Grid is allowed ONLY for these slides

- `①A` — merged PRs to develop: 3 × 2, max 6 cards per slide
- `①B` — Backend collection-branch merges: 3 × 2, max 6 cards per slide
- `①C` — Native collection-branch merges: 3 × 2, max 6 cards per slide
- `⑬` — next steps: 4 × 1, max 4 cards per slide

### Everything else is single-column stacked by default

For all other slides, including `①D`, `①E`, `②`, `③`, `④`, `⑤`, `⑥`, `⑦`, `⑧`, `⑨`, `⑩`, `⑪`, `⑫`, and `⑭`:

- Use one full-width card per row.
- Do not use two-column or three-column card grids.
- Do not split one team’s cards into two columns.
- Do not place cards side by side to save space.

Exception: `⑥A` may use a dependency diagram, but its nodes must still pass the overlap checks below.

---

## 3. Maximum card density

These are maximums, not targets.

| Slide type | Max cards per physical slide | Required action if more content exists |
|---|---:|---|
| `①A`, `①B`, `①C` | 6 | Create `①A-2`, `①B-2`, `①C-2`, etc. |
| `⑬` | 4 | Create `⑬B` if needed |
| Single-column stacked slides | 4 | Create continuation slide |
| Cards with long titles or metadata | 3 | Create continuation slide |
| Dependency diagrams | 3–4 chains | Create continuation slide |

For `①D` and `①E` specifically:

- Max 4 cards per physical slide.
- If a section has more than 4 items, create `①D-2`, `①D-3`, `①E-2`, `①E-3`, etc.
- Do not use columns as a fallback.

---

## 4. Mechanical fit test before placing each card

Before adding a card to a slide, calculate its required height:

```text
required_card_height =
  top_padding
  + title_line_count × title_line_height
  + body_line_count × body_line_height
  + metadata_line_count × metadata_line_height
  + internal_gaps
  + bottom_padding
```

Use the minimum typography from `VISUAL_DESIGN_MANDATORY.md`:

- Slide title: 32 pt minimum
- Section header: 22 pt minimum
- Main content: 20 pt minimum
- Secondary text: 18 pt minimum
- Small labels/footer: 12–14 pt only
- Card padding: 16–20 px minimum
- Line height: 1.8 for readable content

If `current_y + required_card_height > content_bottom_y`, start a new continuation slide before placing the card.

---

## 5. Forbidden fixes

Never solve overflow by doing any of these:

- Reducing main content below 20 pt
- Reducing secondary text below 18 pt
- Reducing card padding below 16 px
- Using shrink-to-fit or auto-shrink
- Using fixed-height cards when text can wrap
- Moving a line upward until it visually overlaps another line
- Turning a stacked slide into a two-column grid
- Placing more than the allowed maximum card count on a slide
- Letting title, owner, status, branch, or footer overlap

---

## 6. Artifact inspection gate

After rendering, inspect the produced PPTX/PDF itself.

The presentation FAILS if any of the following are true:

```text
text_overlap_count > 0
card_overlap_count > 0
text_outside_card_count > 0
text_clipping_count > 0
out_of_bounds_element_count > 0
unapproved_grid_slide_count > 0
font_below_minimum_count > 0
```

A self-report like “checks passed” is not evidence.
The rendered artifact must be inspected.

---

## 7. Special correction for stale examples

`TEMPLATE_REFERENCE.html` is a visual example only.
It may never override:

1. `VISUAL_DESIGN_MANDATORY.md`
2. `ACCESSIBILITY_NEURODIVERSITY.md`
3. `LAYOUT_OVERFLOW_GUARD.md`
4. `SLIDE_DETAIL_SPEC.md`

If an older template says 3 × 4 cards, 12 cards per slide, 13 pt text, 11 pt metadata, small corner radius, or fixed-height cards, that example is invalid.

---

## 8. Required failure response

If the renderer cannot fit the content without overlap:

1. Stop the render.
2. Report which slide failed.
3. Report which content item caused overflow.
4. Create continuation slides and rerender.

Do not deliver the deck until all overlap and clipping checks are zero.

---

**Status:** REQUIRED
**Last updated:** 2026-09-17
