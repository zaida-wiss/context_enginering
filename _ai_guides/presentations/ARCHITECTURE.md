---
name: presentation_architecture
description: Design architecture — Single Source of Truth for presentation system
metadata:
  type: critical_specification
  version: 1.2
---

# 📐 PRESENTATION ARCHITECTURE — Single Source of Truth

This document defines where presentation rules belong and how conflicts are resolved.

---

## 1. Authority hierarchy

### LEVEL 1 — SYSTEM_CONTRACT.yaml
Owns orchestration:
- Execution sequence
- Gates
- STOP/CONTINUE decisions
- Delivery rules

### LEVEL 2 — ACCESSIBILITY_NEURODIVERSITY.md
Owns accessibility boundaries:
- WCAG 2.2 AA
- Readability
- Contrast
- Neurodiverse-friendly constraints

Accessibility boundaries may never be weakened by layout convenience.

### LEVEL 3 — VISUAL_DESIGN_MANDATORY.md
Owns visual implementation:
- Typography minimums
- Colors
- Spacing
- Card geometry
- Shadows/depth
- Theme
- Which card-grid layouts are valid

If a renderer needs to know HOW something looks or is positioned, this is the master visual authority.

### LEVEL 4 — SLIDE_DETAIL_SPEC.md
Owns slide content:
- What appears on each slide
- Required data fields
- Sort order
- Slide purpose
- Content exclusions

It does NOT own visual layout. Any legacy words such as "row", "stacked", "columns" or "table" inside content examples are descriptive only and must never override `VISUAL_DESIGN_MANDATORY.md`.

### DATA AUTHORITIES
- `DATA_ACQUISITION_CONTRACT.yaml` — how data is acquired
- `ACTIVE_WORK_DETECTION_MODEL.md` — how active work is classified
- `_memory/EXTERNAL_SOURCES.yaml` — allowed external sources and access methods

---

## 2. Validation/reference files

### LAYOUT_OVERFLOW_GUARD.md
Mechanical fit, pagination and collision validation.

### RENDER_GATE_CHECKLIST.md
Pre/post-render verification.

### TEMPLATE_REFERENCE.html
Visual example only.

**TEMPLATE_REFERENCE.html is never authoritative.**

---

## 3. Canonical visual language

The presentation uses a **modern card system**.

Core rule:

> ONE ITEM = ONE CARD

Plain row/list layouts are not part of the Monday Meeting visual language.

Canonical layouts:

- `①A–①C`: 3 × 2 cards, max 6 per physical slide
- `①D`: 2 × 2 cards, max 4 per physical slide
- `①E`: 2 × 2 cards, max 4 per physical slide
- `①F`: 2 × 2 or 2 × 1 cards, max 4
- `②–⑤`: modern cards, normally 2 × 2, max 4
- `⑥`: cards; `⑥A` may use dependency diagram nodes
- `⑦–⑫`: modern cards, normally 2 × 2, max 4
- `⑬`: 4 × 1 or 2 × 2 cards, max 4
- `⑭`: grouped modern cards, max 4 per physical slide before continuation

If a card needs more room, reduce the number of cards on that physical slide and create a continuation slide.

---

## 4. Modern card style

Cards are the primary surface.

Required visual characteristics:

- Dark navy canvas
- Secondary navy card surface
- Rounded corners 16–20 px
- Generous padding 18–22 px
- Minimum 20 px gap between cards
- Subtle border/accent
- Subtle box shadow/depth
- Team color used as accent, not full-card fill
- Large readable typography

The deck should feel like a modern dashboard translated into a calm meeting presentation.

---

## 5. Overflow rule

When required content does not fit:

1. Keep required font sizes.
2. Keep required padding and spacing.
3. Keep each item as a card.
4. Reduce cards on the physical slide if necessary.
5. Create continuation slide(s).

Never solve overflow by:
- Shrinking text
- Reducing padding below minimum
- Clipping text
- Overlapping text
- Using fixed-height text boxes that cannot grow
- Converting cards into rows or lists
- Hiding required metadata just to preserve geometry

Extra slides are preferable to unreadable slides.

---

## 6. File responsibilities

| File | Responsibility |
|---|---|
| `SYSTEM_CONTRACT.yaml` | Execution + gates |
| `ACCESSIBILITY_NEURODIVERSITY.md` | Accessibility boundaries |
| `VISUAL_DESIGN_MANDATORY.md` | Visual rules + card layout |
| `SLIDE_DETAIL_SPEC.md` | Slide content only |
| `DATA_ACQUISITION_CONTRACT.yaml` | Data acquisition |
| `ACTIVE_WORK_DETECTION_MODEL.md` | Activity evidence model |
| `LAYOUT_OVERFLOW_GUARD.md` | Mechanical fit/pagination validation |
| `RENDER_GATE_CHECKLIST.md` | Artifact verification |
| `TEMPLATE_REFERENCE.html` | Example only |

Do not create `_V2`, `_UPDATED`, `_NEW`, or competing policy files.

---

## 7. Propagation rules

### Change visual design
1. Update `VISUAL_DESIGN_MANDATORY.md`.
2. Update `LAYOUT_OVERFLOW_GUARD.md` if fit rules change.
3. Update `RENDER_GATE_CHECKLIST.md`.
4. Update `TEMPLATE_REFERENCE.html`.
5. Remove stale visual wording from content/reference files when practical.

### Change slide content
1. Update `SLIDE_DETAIL_SPEC.md`.
2. Update `DATA_ACQUISITION_CONTRACT.yaml` if additional data is required.
3. Do not add visual constants to the content spec.

---

## 8. Conflict handling

If two instructions conflict:

1. Identify which file owns the rule category.
2. Follow the owner according to the hierarchy above.
3. Fix the stale lower-level wording so the conflict does not recur.

For visual/layout conflicts, `VISUAL_DESIGN_MANDATORY.md` wins.

Known stale patterns that must never win:
- plain text rows for work items
- full-width row-list slides
- 11–14 pt readable meeting content
- fixed-height cards
- 3 × 4 / 12-card merge boards
- more than 4 cards on ①D/①E
- shrink-to-fit

---

## 9. Render acceptance

A deck is not complete until the rendered artifact passes:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_minimum_count == 0
plain_row_work_item_count == 0
```

Any non-zero count means: fix layout → add continuation slide(s) → rerender → reinspect.

---

**Last updated:** 2026-09-17
**Status:** Production architecture
