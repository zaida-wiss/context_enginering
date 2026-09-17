---
name: layout_overflow_guard
description: Hard render rules that prevent overlap, clipping, inaccessible compression and stale fixed layouts
metadata:
  type: process
  critical: true
  required_before: rendering
  version: 3.0
---

# 🚨 LAYOUT OVERFLOW GUARD — Responsive Cards, WCAG First

This is a HARD RENDER GATE.

Global visual authority: `VISUAL_DESIGN_MANDATORY.md`  
Card internals: `CARD_COMPONENT_STANDARD.md`  
Accessibility boundary: `ACCESSIBILITY_NEURODIVERSITY.md`

---

## 1. ABSOLUTE RULE

Content must fit **without violating WCAG 2.2 AA**.

A slide is invalid if it solves space pressure by:
- clipping text
- overlapping text/cards
- hiding required content
- using color alone for meaning
- lowering contrast below WCAG AA
- reducing text below its component minimum
- automatic PowerPoint shrink-to-fit

When content is dense, responsive adaptation is required before pagination.

---

## 2. RESPONSIVE FIT SEQUENCE

For every card/slide, use this order:

1. Start at preferred typography sizes.
2. Wrap text naturally.
3. Step down deliberately within the role-specific ranges in `CARD_COMPONENT_STANDARD.md`.
4. Tighten spacing only to the canonical minimums; never collapse line spacing.
5. Let card height grow when space permits.
6. Reduce grid density so cards become wider/taller.
7. Move remaining cards to continuation slide(s).

A continuation slide is mandatory when content still does not fit at the defined accessible minimums.

---

## 3. CARDS ARE MANDATORY

For item-based content:

> ONE ITEM = ONE CARD

Forbidden:
- plain issue/PR rows
- table rows as primary layout
- horizontal list bands
- multiple unrelated work items inside one card merely to save space

`⑥A` may use a dependency graph, but each graph node remains a card.

---

## 4. GRID LIMITS — MAXIMUMS, NOT TARGETS

| Slide type | Default | Maximum |
|---|---|---:|
| `①A`, `①B`, `①C` | 3 × 2 | 6 |
| `①D`, `①E` | 2 × 2 | 4 |
| `①F` | 2 × 2 / 2 × 1 | 4 |
| `②`–`⑤` | 2 × 2 | 4 |
| `⑥`–`⑫`, `⑭` | 2 × 2 | 4 |
| `⑬` | 4 × 1 only when readable; otherwise 2 × 2 | 4 |
| `⑥A` | dependency graph | 3–4 chains |

If cards are text-heavy, use fewer cards than the maximum.

Examples:
- 4 long cards may become 2 cards + 2 cards on continuation
- 6 merge cards may become 4 + 2 if the 3-column cards cannot remain readable

---

## 5. CONTENT-DRIVEN CARD HEIGHT

Calculate required height from actual wrapped content.

Conceptually:

```text
required_card_height =
  top_padding
  + title_block_height
  + supporting_block_height
  + primary_detail_height
  + metadata/provenance_height
  + internal_gaps
  + bottom_padding
```

Do not assume equal text height merely because cards share a grid.

If equal outer card heights are used:
- align primary content from the top
- anchor timestamp/source metadata consistently near bottom when relevant
- let middle whitespace vary naturally
- do not distribute each row evenly from top to bottom

---

## 6. RESPONSIVE TYPOGRAPHY BOUNDARIES

Use `CARD_COMPONENT_STANDARD.md` exactly.

Current component minima:
- slide title: 32 pt
- section header: 22 pt
- card title: 18 pt
- owner/team: 12 pt
- contribution/supporting text: 11 pt
- operational metadata: 10 pt
- timestamp/source/provenance: 10 pt

These are component minima, not targets.

**Never go below them.**

All text must also satisfy WCAG AA contrast and remain visually readable in the actual rendered artifact.

If a technically WCAG-compliant minimum still looks too small/unreadable in the actual presentation context, increase the size and reduce density/paginate.

---

## 7. PADDING / SPACING BOUNDARIES

Use canonical values from the visual/card standards.

Do not solve overflow by removing the visual separation required to distinguish lines/cards.

Hard rules:
- no text collision
- no overlapping text zones
- no negative spacing
- no line-height compression that causes glyph/rule collision
- card gap remains visually clear

---

## 8. SOURCE / PROVENANCE MUST FIT

Provenance labels from `PROVENANCE_AND_AI_LABELING.md` are required content.

Do not remove:
- `📅 Schemafakta`
- `✅ Mötesprotokoll` / team source
- `? AI-förslag` / `? AI-analys`
- `⚠ Källa behöver verifieras`

to save space.

If a card contains both facts and AI interpretation, each block remains separately labeled.

---

## 9. FORBIDDEN FIXES

Never:
- automatic shrink-to-fit
- fonts below component minimums
- text clipping
- text/card overlap
- required content outside its card
- contrast below WCAG AA
- color-only meaning
- hidden provenance
- full team-colored card outline instead of the canonical left accent
- fixed-height card that cuts wrapped text

---

## 10. ARTIFACT INSPECTION GATE

Inspect the actual rendered PPTX/PDF.

The deck FAILS if:

```text
wcag_aa_violation_count > 0
color_only_information_count > 0
text_overlap_count > 0
card_overlap_count > 0
text_outside_card_count > 0
text_clipping_count > 0
out_of_bounds_element_count > 0
font_below_component_minimum_count > 0
missing_required_card_row_count > 0
uneven_row_spacing_caused_by_vertical_justification > 0
plain_row_work_item_count > 0
```

---

## 11. REQUIRED FAILURE RESPONSE

When a slide fails:

1. identify the exact overflowing/colliding block
2. verify the correct role-specific typography range
3. adapt deliberately within that range
4. adapt card geometry/grid density
5. paginate if still required
6. rerender
7. reinspect

Do not deliver until all hard-failure counts are zero.

---

**Status:** REQUIRED
**Version:** 3.0
**Last updated:** 2026-09-17
