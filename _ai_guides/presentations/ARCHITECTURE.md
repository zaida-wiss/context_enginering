---
name: presentation_architecture
description: Design architecture — Single Source of Truth for presentation system
metadata:
  type: critical_specification
  version: 2.0
---

# 📐 PRESENTATION ARCHITECTURE — Single Source of Truth

This document defines where presentation rules belong and how conflicts are resolved.

---

## 1. AUTHORITY HIERARCHY

### LEVEL 1 — SYSTEM_CONTRACT.yaml
Owns orchestration:
- execution sequence
- gates
- STOP/CONTINUE decisions
- delivery rules

### LEVEL 2 — ACCESSIBILITY_NEURODIVERSITY.md
Owns the absolute accessibility boundary:
- WCAG 2.2 AA
- contrast
- color redundancy
- readability
- neurodiverse-friendly constraints

**WCAG may never be weakened by layout convenience, density or visual preference.**

### LEVEL 3 — VISUAL_DESIGN_MANDATORY.md
Owns global visual implementation:
- theme
- typography roles/ranges
- card-grid limits
- spacing
- colors
- global responsive behavior

### LEVEL 4 — CARD_COMPONENT_STANDARD.md
Owns card internals:
- card typography ranges
- metadata sizes
- timestamp format
- owner/review/merge layout
- internal spacing
- team accent treatment

### LEVEL 5 — PROVENANCE_AND_AI_LABELING.md
Owns source identity:
- fact vs team input vs AI inference
- schema facts
- meeting facts
- AI suggestion/analysis labels
- mixed-card source labeling

### LEVEL 6 — SLIDE_DETAIL_SPEC.md
Owns slide content:
- what appears on each slide
- required data fields
- sort order
- slide purpose
- content exclusions

It does NOT override accessibility, visual design, card component or provenance rules.

### DATA AUTHORITIES
- `DATA_ACQUISITION_CONTRACT.yaml` — how data is acquired
- `ACTIVE_WORK_DETECTION_MODEL.md` — how active work is classified
- `_memory/EXTERNAL_SOURCES.yaml` — allowed external sources/access methods

---

## 2. VALIDATION / REFERENCE FILES

### LAYOUT_OVERFLOW_GUARD.md
Mechanical responsive fit, density, pagination and collision rules.

### RENDER_GATE_CHECKLIST.md
Pre/post-render validation, including WCAG and provenance.

### TEMPLATE_REFERENCE.html
Visual example only. Never authoritative.

---

## 3. CANONICAL VISUAL LANGUAGE

The presentation uses one coherent **modern glass-card system**.

Core rule:

> ONE ITEM = ONE CARD

Required characteristics:
- dark navy canvas
- glass-like dark card surface
- rounded corners
- subtle depth
- readable responsive typography
- team ownership shown by a **narrow left accent only**
- no full-card team-colored outline/fill
- consistent internal hierarchy

This system applies throughout the deck, including sprintplan, next steps and PL questions.

---

## 4. RESPONSIVE TYPOGRAPHY MODEL

The system no longer treats every card text role as 18–20 pt.

Instead:
- every role has a preferred size and an explicit minimum
- dense cards may deliberately step down within that range
- automatic shrink-to-fit remains forbidden
- WCAG 2.2 AA remains mandatory
- if content still does not fit at the minimum, geometry/density changes or pagination are required

Role-specific ranges live in `CARD_COMPONENT_STANDARD.md`.

---

## 5. RESPONSIVE CARD MODEL

Cards adapt to their content.

Allowed:
- natural wrapping
- content-driven height
- lower grid density
- wider cards
- 2×2 → 2×1 → 1×1 where appropriate
- continuation slides

Forbidden:
- clipping
- overlap
- hiding fields
- shrinking below minimum
- reducing WCAG contrast
- color-only meaning
- fixed-height boxes that crop wrapped text

---

## 6. PROVENANCE MODEL

Every derived claim must clearly show its origin.

Canonical source classes:
- `📅 Schemafakta`
- `✅ Mötesprotokoll` / verified team input
- `? AI-förslag`
- `? AI-analys`
- `⚠ Källa behöver verifieras`

A mixed card may contain several source classes, but each block must remain labeled.

This is especially important for:
- sprintplan
- sprintmål
- prioritering
- risk analysis
- next steps
- questions to PL

Red is not a fact color. Red remains blocker/critical.

---

## 7. CANONICAL LAYOUT LIMITS

These are maximums, not targets:

- `①A–①C`: max 6 cards, default 3×2
- `①D–①E`: max 4, default 2×2
- `①F`: max 4, responsive 2×2 / 2×1 / 1×1
- `②–⑫`: max 4, responsive card layout
- `⑬`: max 4; 4×1 only when readable, otherwise 2×2/fewer
- `⑭`: max 4 before continuation
- `⑥A`: dependency diagram exception; each node remains a card

If card content is long, use fewer cards.

---

## 8. FILE RESPONSIBILITIES

| File | Responsibility |
|---|---|
| `SYSTEM_CONTRACT.yaml` | execution + gates |
| `ACCESSIBILITY_NEURODIVERSITY.md` | absolute WCAG/accessibility boundary |
| `VISUAL_DESIGN_MANDATORY.md` | global theme + responsive visual rules |
| `CARD_COMPONENT_STANDARD.md` | internal card typography/spacing/metadata |
| `PROVENANCE_AND_AI_LABELING.md` | source fact/team/AI identity |
| `SLIDE_DETAIL_SPEC.md` | slide content only |
| `DATA_ACQUISITION_CONTRACT.yaml` | data acquisition |
| `ACTIVE_WORK_DETECTION_MODEL.md` | activity evidence model |
| `LAYOUT_OVERFLOW_GUARD.md` | responsive fit/pagination validation |
| `RENDER_GATE_CHECKLIST.md` | final artifact validation |
| `TEMPLATE_REFERENCE.html` | example only |

Do not create competing `_V2`, `_UPDATED`, `_NEW` policy variants.

---

## 9. PROPAGATION RULES

### Change accessibility
1. Update `ACCESSIBILITY_NEURODIVERSITY.md` if the boundary itself changes.
2. Propagate to visual/card/overflow/render-gate files.
3. Accessibility remains highest authority.

### Change global design
1. Update `VISUAL_DESIGN_MANDATORY.md`.
2. Update `CARD_COMPONENT_STANDARD.md` if card internals change.
3. Update `LAYOUT_OVERFLOW_GUARD.md`.
4. Update `RENDER_GATE_CHECKLIST.md`.
5. Update reference template when useful.

### Change provenance/source identity
1. Update `PROVENANCE_AND_AI_LABELING.md`.
2. Update reading order/authority map if needed.
3. Update `RENDER_GATE_CHECKLIST.md`.
4. Remove stale source wording in slide spec/examples when practical.

### Change slide content
1. Update `SLIDE_DETAIL_SPEC.md`.
2. Update data acquisition if extra data is required.
3. Do not define conflicting visual constants there.

---

## 10. CONFLICT HANDLING

When instructions conflict:

1. identify which file owns the rule category
2. follow the higher authority
3. fix the stale lower-level wording so the conflict does not recur

Never silently choose the easier layout.

Known stale patterns that must never win:
- 18 pt required for all secondary card metadata
- 20 pt required for every card title regardless of density
- `Merged by:` / `Reviewed by:` labels
- one-line merge timestamp with `Merged` prefix
- full team-colored card outlines
- flat non-glass cards on later slides
- unlabelled AI suggestions
- red used to mean source fact
- `team feedback` used for AI-generated questions
- automatic shrink-to-fit

---

## 11. RENDER ACCEPTANCE

A deck is not complete until the rendered artifact passes:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_component_minimum_count == 0
plain_row_work_item_count == 0
missing_required_card_row_count == 0
uneven_row_spacing_caused_by_vertical_justification == 0
ai_generated_item_without_question_icon_count == 0
unverified_item_presented_as_confirmed_count == 0
```

Any non-zero count means: fix → rerender → reinspect.

---

**Last updated:** 2026-09-17
**Status:** Production architecture
**Version:** 2.0
