---
name: presentation_architecture
description: Design architecture — Single Source of Truth for presentation system
metadata:
  type: critical_specification
  version: 2.2
---

# 📐 PRESENTATION ARCHITECTURE — Single Source of Truth

This document defines where presentation rules belong and how conflicts are resolved.

---

## 1. AUTHORITY OWNERSHIP HIERARCHY

This hierarchy defines ownership/delegation only. Genuine incompatible active
rules are resolved through the user-decision gate in `../AI_FRAMEWORK.yaml`,
never by rank alone.

### LEVEL 1 — SYSTEM_CONTRACT.yaml
Owns orchestration:
- execution sequence
- gates
- STOP/CONTINUE decisions
- delivery rules
- post-delivery feedback routing and artifact mutation permission
- user decision gate when new feedback conflicts with an active rule
- WCAG 2.2 AA as an absolute constraint outside user-selectable trade-offs
- collaborative read-only contradiction audit followed by user-approved cleanup

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
- slide-level typography roles
- card-grid limits
- column/grid structure
- colors
- global responsive behavior

### LEVEL 4 — READABILITY_HARD_RULES.md
Owns hard readability requirements:
- slide-title and body minima
- line spacing
- meeting-point glyph rules
- pedagogical readability

### LEVEL 5 — CARD_COMPONENT_STANDARD.md
Owns card internals:
- card typography ranges
- metadata sizes
- timestamp format
- owner/review/merge layout
- internal spacing
- team accent treatment

### LEVEL 6 — PROVENANCE_AND_AI_LABELING.md
Owns source identity:
- fact vs team input vs AI inference
- schema facts
- meeting facts
- AI suggestion/analysis labels
- mixed-card source labeling

### LEVEL 7 — PR_MERGE_REVIEW_IDENTITY.md
Owns merger and actual submitted-review identity.

### LEVEL 8 — LAYOUT_OVERFLOW_GUARD.md
Owns mechanical fit, pagination and collision prevention.

### LEVEL 9 — SLIDE_DETAIL_SPEC.md
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
- `data/SOURCES.yaml` — allowed external sources/access methods

---

## 2. VALIDATION / REFERENCE FILES

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
- team ownership shown by a narrow left accent; issue/PR numbers also use team color, with team column/section or text as the required non-color cue
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
- `👥 ✅ Mötesprotokoll` / verified meeting-protocol input
- `⭐ AI-förslag`
- `🔎 AI-analys`
- `⚠ Källa behöver verifieras`

The canonical Unicode symbol and its text label together identify the source class. Visual containers such as tags, chips or badges may style that canonical identity while preserving the symbol + text.

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

These are density rules:

- `①–①d`: verified work performed so far in the active sprint; 6 cards is standard capacity per physical slide with unlimited lowercase-letter continuations
- `①` develop merges → `①a` Backend collection merges → `①b` Native collection merges → `①c` unfinished work active in the window → `①d` AI team summaries
- `③–⑤`: separate Frontend, Backend and Native forward-planning sections; they own backlog, future work, older inactive work and governing decisions
- `⑨`: content structure, execution groups and continuation behavior are defined by `SLIDE_DETAIL_SPEC.md`
- `⑨`: visual implementation follows `VISUAL_DESIGN_MANDATORY.md`, `CARD_COMPONENT_STANDARD.md` and `LAYOUT_OVERFLOW_GUARD.md`
- `⑨`: Architecture records ownership only; it does not duplicate the point-9 page layout
- `③–⑤` and `⑨`: plan the remaining active-sprint horizon from data cutoff to sprint end
- `②`, `⑥–⑧` and `⑩–⑫`: max 4, responsive card layout
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
| `READABILITY_HARD_RULES.md` | hard typography, line spacing and readability |
| `CARD_COMPONENT_STANDARD.md` | internal card typography/spacing/metadata |
| `PROVENANCE_AND_AI_LABELING.md` | source fact/team/AI identity |
| `PR_MERGE_REVIEW_IDENTITY.md` | merger and submitted-review identity |
| `SLIDE_DETAIL_SPEC.md` | slide content only |
| `DATA_ACQUISITION_CONTRACT.yaml` | data acquisition |
| `ACTIVE_WORK_DETECTION_MODEL.md` | activity evidence model |
| `LAYOUT_OVERFLOW_GUARD.md` | responsive fit/pagination validation |
| `RENDER_GATE_CHECKLIST.md` | final artifact validation |
| `TEMPLATE_REFERENCE.html` | example only |
| `AUTHORITY_REGISTRY.yaml` | active/validator/reference/retired classification |

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
2. if the files govern different categories, apply both in registry rank order
3. if both claim the same category and cannot both be followed, STOP and emit the conflict receipt
4. fix the stale or duplicate wording so the conflict does not recur

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
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
```

Any non-zero count means: fix → rerender → reinspect.

---

**Last updated:** 2026-09-18
**Status:** Production architecture
**Version:** 2.1
