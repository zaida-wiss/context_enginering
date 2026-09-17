---
name: layout_overflow_guard
description: Hard render rules that prevent text overlap, clipping, and accidental layout compression
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 2.0
---

# 🚨 LAYOUT OVERFLOW GUARD — Cards First, No Compression

This is a HARD RENDER GATE for Monday Meeting presentations.

The visual authority is `VISUAL_DESIGN_MANDATORY.md`. This guard enforces fit, pagination and collision rules.

---

## 1. Absolute rule

When content does not fit:

> Create a continuation slide.

Never solve space problems by shrinking text, reducing padding, overlapping elements, clipping text, or replacing cards with text rows.

A deck with more slides is correct.
A deck with unreadable cards is invalid.

---

## 2. Cards are mandatory

For item-based content:

> ONE ITEM = ONE CARD

Forbidden representations:

- plain text rows
- table rows
- horizontal list bands
- issue lists without card surfaces
- multiple unrelated work items inside one card to save space

Dependency slide `⑥A` may use a graph, but every graph node is still a card.

---

## 3. Canonical grid limits

| Slide type | Default card layout | Max cards / physical slide |
|---|---|---:|
| `①A`, `①B`, `①C` | 3 × 2 | 6 |
| `①D`, `①E` | 2 × 2 | 4 |
| `①F` | 2 × 2 or 2 × 1 | 4 |
| `②`, `③`, `④`, `⑤` | 2 × 2 | 4 |
| `⑥`, `⑦`, `⑧`, `⑨`, `⑩`, `⑪`, `⑫`, `⑭` | 2 × 2 | 4 |
| `⑬` | 4 × 1 or 2 × 2 | 4 |
| `⑥A` | dependency graph | 3–4 chains |

These are maximums, not targets.

If cards are text-heavy, use fewer cards on that physical slide.

---

## 4. Mandatory pagination

Examples:

- 8 items on ①E → 4 cards on `①E`, 4 cards on `①E-2`
- 7 merged PRs on ①A → 6 cards on `①A`, 1 card on `①A-2`
- 6 long cards on ③ → e.g. 3 cards on `③`, 3 cards on `③-2`

Never create an extra row merely because there is unused horizontal space.

---

## 5. Mechanical fit test

Before placing a card, calculate its required height from actual wrapped text:

```text
required_card_height =
  top_padding
  + title_lines × title_line_height
  + body_lines × body_line_height
  + metadata_lines × metadata_line_height
  + internal_gaps
  + bottom_padding
```

Card height must be content-driven.

For a grid cell:

```text
if required_card_height > available_cell_height:
    reduce cards on this physical slide
    OR create continuation slide
```

Do not reduce typography or padding.

---

## 6. Binding minimums

Use values from `VISUAL_DESIGN_MANDATORY.md`:

- Slide title: 32 pt minimum
- Section header: 22 pt minimum
- Card title/main text: 20 pt minimum
- Secondary meeting information: 18 pt minimum
- Small labels/footer: 12–14 pt only
- Card padding: 18–22 px
- Gap between cards: 20 px minimum
- Corner radius: 16–20 px

---

## 7. Modern card surface check

Each card must have:

- dark card surface separate from slide background
- rounded corners
- subtle border/accent
- subtle box shadow/depth where supported
- clear internal text hierarchy

A card must visually read as a card, not as a line of text with a border beside it.

---

## 8. Forbidden fixes

Never:

- reduce main text below 20 pt
- reduce secondary text below 18 pt
- reduce card padding to make one more card fit
- use shrink-to-fit or auto-shrink
- use fixed text-box height when content wraps
- overlap title/body/metadata
- place text outside its card
- convert ①D/①E to rows
- put more than 4 cards on ①D/①E
- put more than 6 cards on ①A–①C

---

## 9. Artifact inspection gate

Inspect the rendered PPTX/PDF, not the generator report.

The deck FAILS if:

```text
text_overlap_count > 0
card_overlap_count > 0
text_outside_card_count > 0
text_clipping_count > 0
out_of_bounds_element_count > 0
font_below_minimum_count > 0
plain_row_work_item_count > 0
```

Also fail if ①D or ①E is rendered as a row/list layout instead of cards.

---

## 10. Required failure response

If a slide fails fit or collision checks:

1. Identify the failing slide
2. Identify the card causing overflow
3. Move that card and following cards to a continuation slide
4. Rerender
5. Reinspect

Do not deliver until all collision counts are zero.

---

**Status:** REQUIRED
**Version:** 2.0
**Last updated:** 2026-09-17
