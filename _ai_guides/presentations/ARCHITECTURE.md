---
name: presentation_architecture
description: Design architecture — Single Source of Truth for presentation system
metadata:
  type: critical_specification
  version: 1.1
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
- Theme
- Which layout families are valid

If a renderer needs to know HOW something looks or is positioned, this is the master visual authority.

### LEVEL 4 — SLIDE_DETAIL_SPEC.md
Owns slide content:
- What appears on each slide
- Required data fields
- Sort order
- Slide purpose
- Content exclusions

It must not override visual/accessibility minimums.

### DATA AUTHORITIES
- `DATA_ACQUISITION_CONTRACT.yaml` — how data is acquired
- `ACTIVE_WORK_DETECTION_MODEL.md` — how active work is classified
- `_memory/EXTERNAL_SOURCES.yaml` — allowed external sources and access methods

---

## 2. Validation/reference files

These files do NOT create competing design policy. They mechanically validate or illustrate the authority files.

### LAYOUT_OVERFLOW_GUARD.md
Purpose: mechanical pagination/overflow validation.

It enforces existing visual/accessibility rules by answering:
- Does the content fit without shrinking?
- Must a continuation slide be created?
- Is an unapproved grid being used?
- Does the rendered artifact contain overlap or clipping?

It may never reduce typography, spacing, or accessibility minimums.

### RENDER_GATE_CHECKLIST.md
Purpose: pre/post-render verification.

### TEMPLATE_REFERENCE.html
Purpose: visual example only.

**TEMPLATE_REFERENCE.html is never authoritative.** If it conflicts with any authority file or validation guard, ignore the template and follow the authority files.

---

## 3. Canonical layout rule

Default layout is **single-column, full-width, stacked cards**.

Approved exceptions:
- `①A` — 3 × 2 grid, max 6 cards
- `①B` — 3 × 2 grid, max 6 cards
- `①C` — 3 × 2 grid, max 6 cards
- `⑥A` — dependency diagram
- `⑬` — 4 × 1 next-step grid, max 4 cards

Everything else must remain stacked unless `VISUAL_DESIGN_MANDATORY.md` explicitly defines another exception.

**Important correction:** `①D` and `①E` are stacked layouts. They must paginate instead of switching to columns.

---

## 4. Overflow rule

When required content does not fit:

1. Keep required font sizes.
2. Keep required padding and line height.
3. Keep the approved layout family.
4. Create a continuation slide.

Never solve overflow by:
- Shrinking text
- Reducing padding below minimum
- Clipping text
- Overlapping text
- Using fixed-height cards that cannot grow
- Changing a stacked slide into two/three columns

Extra slides are preferable to unreadable slides.

---

## 5. File responsibilities

| File | Responsibility |
|---|---|
| `SYSTEM_CONTRACT.yaml` | Execution + gates |
| `ACCESSIBILITY_NEURODIVERSITY.md` | Accessibility boundaries |
| `VISUAL_DESIGN_MANDATORY.md` | Visual rules |
| `SLIDE_DETAIL_SPEC.md` | Slide content |
| `DATA_ACQUISITION_CONTRACT.yaml` | Data acquisition |
| `ACTIVE_WORK_DETECTION_MODEL.md` | Activity evidence model |
| `LAYOUT_OVERFLOW_GUARD.md` | Mechanical fit/pagination validation |
| `RENDER_GATE_CHECKLIST.md` | Artifact verification |
| `TEMPLATE_REFERENCE.html` | Example only |

Do not create `_V2`, `_UPDATED`, `_NEW`, or alternative policy files.
A new validation file is permitted only when it validates an existing authority category rather than redefining it, and it must be added to this architecture + mandatory reading order in the same change.

---

## 6. Propagation rules

### Change visual design
1. Update `VISUAL_DESIGN_MANDATORY.md`.
2. Update validation rules if required.
3. Update `TEMPLATE_REFERENCE.html` to illustrate the new design.

### Change slide content
1. Update `SLIDE_DETAIL_SPEC.md`.
2. Update `DATA_ACQUISITION_CONTRACT.yaml` if additional data is required.
3. Do not add visual constants to the content spec.

### Change accessibility boundary
1. Update `ACCESSIBILITY_NEURODIVERSITY.md`.
2. Update `VISUAL_DESIGN_MANDATORY.md` implementation.
3. Add/adjust render validation.

---

## 7. Conflict handling

If two instructions conflict:

1. STOP before rendering.
2. Identify which file owns the rule category.
3. Follow the owner according to the hierarchy above.
4. Fix the stale lower-level reference so the conflict does not recur.

Known stale-example patterns that must never win:
- 11–14 pt readable meeting content
- Fixed-height cards
- 3 × 4 / 12-card merge boards
- Two-column fallback for `①D` or `①E`
- Shrink-to-fit

---

## 8. Render acceptance

A deck is not complete until the rendered artifact passes:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
unapproved_grid_slide_count == 0
font_below_minimum_count == 0
```

Any non-zero count means: fix layout → rerender → reinspect.

---

**Last updated:** 2026-09-17
**Status:** Production architecture
