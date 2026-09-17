---
name: render_gate_checklist
description: Mechanical checklist for when a Monday Meeting presentation may be rendered and delivered
metadata:
  type: process
  critical: true
  version: 3.0
---

# 🚨 RENDER-GATE CHECKLIST

A presentation may be delivered only when BOTH data integrity and rendered-artifact quality pass.

Self-report from the generator is not evidence. Inspect the rendered PPTX/PDF.

---

## 1. DATA_AUDIT — BEFORE SLIDES

Create a DATA_AUDIT for the reporting period.

Required repository totals:

```text
Total merged PRs
Total open PRs
Total commits to develop
Total open issues with activity
```

Required work-area classification:

```text
Frontend
Backend
Native
Cross-team
Other
```

For each area record:
- merged PR IDs
- open PR IDs
- active issue IDs

Required team coverage:
- All 7 members identity-verified
- Members without active work represented using the approved availability wording

Required checksums:

```text
COUNT: sum(classified merged PR counts) == repository merged PR total
SET: classified PR IDs == repository merged PR ID set
UNIQUENESS: each PR appears in exactly one work area
TEAM: all team identities verified
```

If any checksum fails → STOP.

---

## 2. DATA ACCURACY

Before rendering verify:

- Issue/PR numbers are real GitHub entities
- State is accurate (open/closed/merged)
- Assignee is actual GitHub assignee, or `??` when genuinely absent
- Developer attribution follows the project rules
- `Reviewed by` uses actual GitHub review evidence
- `Merged by` uses actual GitHub merged_by identity when available
- Timestamps are actual GitHub timestamps
- No fabricated status, branch, owner, reviewer or merge identity

Optional enrichment may be missing without blocking, but required data may not be guessed.

---

## 3. CONTENT COMPLETENESS

Every required work item must be accounted for.

For open assigned issues:

```text
open_assigned_issues ==
  issues_shown_on_①D
  + issues_shown_on_①E
  + explicitly_documented_exclusions
```

No issue may silently disappear.

No PR may appear twice.

Zero work for one team is valid if verified.

---

## 4. VISUAL AUTHORITY

Use:

1. `ACCESSIBILITY_NEURODIVERSITY.md`
2. `VISUAL_DESIGN_MANDATORY.md`
3. `LAYOUT_OVERFLOW_GUARD.md`
4. `SLIDE_DETAIL_SPEC.md` for content only

If a content example contains stale visual language such as rows, lists, stacked bands or tables, ignore that visual form and use the current card system from `VISUAL_DESIGN_MANDATORY.md`.

---

## 5. MODERN CARD SYSTEM — MUST PASS

### Work-item representation

Every work/information item that is item-based must be an individual card.

FAIL if a slide uses:

- plain text rows for issues/PRs
- table rows as the main layout
- horizontal list bands
- multiple unrelated items merged into one card to save space

### Canonical physical layouts

| Slide | Required/default layout | Maximum |
|---|---|---:|
| ①A | 3 × 2 cards | 6 |
| ①B | 3 × 2 cards | 6 |
| ①C | 3 × 2 cards | 6 |
| ①D | 2 × 2 cards | 4 |
| ①E | 2 × 2 cards | 4 |
| ①F | 2 × 2 or 2 × 1 cards | 4 |
| ②–⑤ | modern card grid | 4 |
| ⑥ | cards; ⑥A may be dependency graph | 4 cards / 3–4 chains |
| ⑦–⑫ | modern card grid | 4 |
| ⑬ | 4 × 1 or 2 × 2 cards | 4 |
| ⑭ | grouped modern cards | 4 before continuation |

If content is too long for the default density, use FEWER cards on that physical slide and create a continuation slide.

---

## 6. MODERN CARD APPEARANCE

Inspect the actual rendered cards.

Each card must visibly have:

- separate dark card surface from the slide background
- rounded corners approximately 16–20 px
- generous internal padding approximately 18–22 px
- minimum 20 px visual gap between cards
- subtle border/accent
- subtle box-shadow/depth when renderer supports it
- team color used as accent, not full-card fill
- clear title/body/metadata hierarchy

The deck should feel like a modern dashboard translated into a calm meeting presentation.

---

## 7. TYPOGRAPHY — HARD MINIMUMS

FAIL if any meeting-readable text violates:

- Slide title < 32 pt
- Section header < 22 pt
- Card title/main text < 20 pt
- Secondary meeting information < 18 pt
- Metadata/footer outside 12–14 pt range when small text is appropriate

Also FAIL if:

- shrink-to-fit is enabled
- auto-reduce-font is used
- padding is reduced to force another card onto a slide
- line spacing causes visual collision

---

## 8. OVERFLOW & PAGINATION

When a card does not fit:

1. Let card height grow to fit wrapped content
2. Reduce cards on that physical slide
3. Move remaining cards to continuation slide

Required continuation examples:

```text
①A-2, ①A-3
①D-2, ①D-3
①E-2, ①E-3
③-2
⑭-2
```

FAIL if the renderer responds to overflow by:

- shrinking text
- reducing padding
- clipping text
- overlapping cards
- converting cards into rows
- adding extra rows beyond the allowed grid density

---

## 9. ARTIFACT COLLISION CHECK

The rendered artifact must satisfy:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_minimum_count == 0
plain_row_work_item_count == 0
```

Any non-zero count = FAIL.

---

## 10. COVER SLIDE ⓪

Verify:

- No meeting-point header / pen symbol
- Meeting date visible
- Team identifier visible
- Reporting period visible
- Sprintfokus visible
- Deadline visible and accented
- PL-fokus visible
- Compact source/snapshot footer visible
- No unnecessary bordered text boxes

---

## 11. MERGE BOARDS ①A–①C

Verify:

- 3 × 2 cards by default
- max 6 cards per physical slide
- chronological order where required
- team accent visible
- actual developer/reviewer/merger identities shown where required
- continuation slides exist if >6
- no third row

If a card cannot remain readable in 3 columns, reduce density for that physical slide rather than shrinking text.

---

## 12. ACTIVE WORK ①D–①E

Verify:

- ①D uses cards, default 2 × 2, max 4
- ①E uses cards, default 2 × 2, max 4
- each issue/work item has its own card
- branch/status/owner remain inside the card
- fifth item starts a continuation slide
- no row/list presentation

---

## 13. TEAM DETAIL ③④⑤

Verify:

- identical modern card geometry across Frontend/Backend/Native
- only team accent differs
- no tables
- no rows
- one work item per card
- max 4 cards per physical slide
- continuation slides when needed

---

## 14. DEPENDENCY DIAGRAM ⑥A

Verify:

- each node is a rounded card
- arrows clearly indicate dependency direction
- no crossing/overlapping labels
- nodes do not clip text
- split to continuation slide if graph becomes dense

---

## 15. EXPLICIT OMISSIONS

If a conditional slide is omitted, record the verified reason.

Examples:

```text
①B omitted — 0 verified Backend collection-branch merges
①C omitted — 0 verified Native collection-branch merges
①F omitted — 0 verified decisions/candidates
```

A slide may not disappear merely because layout is inconvenient.

---

## 16. FINAL DELIVERY GATE

Deliver only when:

```text
DATA_AUDIT == PASS
CONTENT_COMPLETENESS == PASS
VISUAL_CARD_SYSTEM == PASS
TYPOGRAPHY == PASS
OVERFLOW == PASS
ARTIFACT_COLLISION_CHECK == PASS
```

If any check fails:

1. Fix the slide
2. Add continuation slides if needed
3. Rerender
4. Reinspect the actual artifact
5. Deliver only after all checks pass

---

**Status:** PRODUCTION
**Version:** 3.0
**Last updated:** 2026-09-17
