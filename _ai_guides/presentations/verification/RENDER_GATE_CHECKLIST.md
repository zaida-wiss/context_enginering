---
name: render_gate_checklist
description: Mechanical checklist for when a Monday Meeting presentation may be rendered and delivered
metadata:
  type: process
  critical: true
  version: 4.0
---

# 🚨 RENDER-GATE CHECKLIST

A presentation may be delivered only when BOTH data integrity and rendered-artifact quality pass.

Self-report from the generator is not evidence. Inspect the actual rendered PPTX/PDF.

---

## 1. DATA AUDIT

Create a data audit for the reporting period.

Required totals:
- total merged PRs
- total open PRs
- total commits to develop
- total open issues with activity

Required work-area classification:
- Frontend
- Backend
- Native
- Cross-team
- Other

For each area record:
- merged PR IDs
- open PR IDs
- active issue IDs

Required checks:

```text
COUNT: sum(classified merged PR counts) == repository merged PR total
SET: classified PR IDs == repository merged PR ID set
UNIQUENESS: each PR appears in exactly one work area
TEAM: all team identities verified
```

Any failure → STOP.

---

## 2. DATA ACCURACY

Verify:
- issue/PR numbers are real
- state is accurate
- assignee is verified or explicitly unknown
- developer attribution follows project rules
- reviewer/merger identities use actual evidence
- timestamps are actual source timestamps
- contribution microcopy is grounded in repository evidence
- no fabricated status, branch, owner, reviewer, merge identity or code effect

---

## 3. WCAG 2.2 AA — ABSOLUTE DELIVERY GATE

The deck MUST pass WCAG 2.2 AA.

Verify at minimum:
- normal text contrast >= **4.5:1**
- WCAG large text contrast >= **3:1**
- meaningful borders/components >= **3:1**
- color is never the only information carrier
- muted text remains compliant against the actual rendered surface
- no text becomes inaccessible because of transparency/glass effects

Required:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
```

Any non-zero count = FAIL. No design/layout exception may override this gate.

---

## 4. AUTHORITY ORDER

Use:

1. `ACCESSIBILITY_NEURODIVERSITY.md`
2. `VISUAL_DESIGN_MANDATORY.md`
3. `CARD_COMPONENT_STANDARD.md`
4. `PROVENANCE_AND_AI_LABELING.md`
5. `LAYOUT_OVERFLOW_GUARD.md`
6. `SLIDE_DETAIL_SPEC.md` for slide content
7. `TEMPLATE_REFERENCE.html` as reference only

If stale examples conflict with these authorities, ignore the stale visual form and fix the lower-authority wording when practical.

---

## 5. MODERN CARD SYSTEM

Every item-based information/work item must use a card unless explicitly defined as a diagram/group.

FAIL on:
- plain text work-item rows
- table rows as primary layout
- horizontal list bands
- unrelated items merged into one card to save space
- inconsistent flat boxes replacing the card system on later slides

Every card should show:
- dark glass-like surface
- rounded corners
- subtle depth
- coherent padding
- team color as **left accent only** where applicable
- clear text hierarchy

Required:

```text
full_team_outline_count == 0
card_system_inconsistency_count == 0
```

---

## 6. RESPONSIVE TYPOGRAPHY

Use role-specific ranges from `CARD_COMPONENT_STANDARD.md`.

Current minima:
- slide title: 32 pt
- section header: 22 pt
- card title: 18 pt
- owner/team: 12 pt
- contribution/supporting text: 11 pt
- operational metadata: 10 pt
- timestamp/source/provenance: 10 pt

The renderer MAY deliberately select smaller sizes within the allowed range when a slide is dense.

The renderer MAY NOT:
- use automatic shrink-to-fit
- go below role minimums
- reduce contrast
- hide required fields

Required:

```text
font_below_component_minimum_count == 0
auto_shrink_enabled_count == 0
```

---

## 7. EVEN SPACING / RESPONSIVE GEOMETRY

Verify:
- wrapped lines use natural line spacing
- no visually colliding lines
- content is top-aligned in cards
- timestamps/source metadata are consistently anchored where appropriate
- rows are NOT vertically distributed across the entire card height
- card height/width responds to actual content
- dense content changes grid density or paginates

Required:

```text
uneven_row_spacing_caused_by_vertical_justification == 0
fixed_height_text_clipping_count == 0
```

---

## 8. MERGED PR CARD FORMAT

Verify merged cards use:

```text
Merged: [name] | Review: [name/status]
```

and timestamp:

```text
14 sep
10:16
```

FAIL on:
- `Merged by:`
- `Reviewed by:`
- `Mergad` prefix before bottom timestamp
- one-line timestamp where the component rule requires two-line compact form

Required:

```text
legacy_merged_by_label_count == 0
legacy_reviewed_by_label_count == 0
merged_timestamp_prefix_count == 0
```

---

## 9. CONTRIBUTION MICROCOPY

Every Issue, open PR and merged PR card contains a grounded explanation directly below the title.

Required characteristics:
- short
- plain Swedish
- grounded in verified evidence
- not vague process language

If evidence is insufficient, use:

`Bidrag till koden behöver verifieras.`

Required:

```text
missing_contribution_microcopy_count == 0
unsupported_contribution_claim_count == 0
```

---

## 10. PROVENANCE — FACT VS TEAM VS AI

Every inferred/recommended item must be visibly distinguished from verified source content.

Canonical labels:
- `📅 Schemafakta`
- `✅ Mötesprotokoll` / equivalent verified team label
- `? AI-förslag`
- `? AI-analys`
- `⚠ Källa behöver verifieras`

Rules:
- color may support but never replace icon + text
- red is NOT a fact color
- mixed cards label each block independently

Especially verify slides ⑫, ⑬ and ⑭.

Required:

```text
sprint_plan_fact_without_source_label_count == 0
sprint_plan_ai_suggestion_without_question_icon_count == 0
next_step_card_without_provenance_count == 0
pl_question_card_without_provenance_count == 0
ai_generated_item_without_question_icon_count == 0
unverified_item_presented_as_confirmed_count == 0
mixed_provenance_card_without_block_labels_count == 0
```

---

## 11. OVERFLOW / COLLISION

The rendered artifact must satisfy:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
missing_required_card_row_count == 0
plain_row_work_item_count == 0
```

If content is too dense:
1. step down within the permitted typography range
2. adapt spacing to canonical compact values
3. grow/reflow cards
4. reduce grid density
5. paginate

Never clip or hide content.

---

## 12. COVER SLIDE ⓪

Verify:
- no meeting-point pen/number header
- meeting date visible
- team identifier visible
- reporting period visible
- sprintfokus visible
- deadline visible
- PL-fokus visible
- compact source/snapshot footer visible
- no unnecessary bordered boxes

---

## 13. MERGE BOARDS ①A–①C

Verify:
- chronological order where required
- one merge per card
- max 6 per physical slide
- use fewer cards when 3-column layout is not readable
- team left accent only
- contribution microcopy present
- merger/reviewer/developer evidence shown as required
- compact timestamp format used

---

## 14. ACTIVE / BACKLOG ①D–①E

Verify:
- one work item per card
- default max 4 per physical slide
- branch/status/owner remain visible
- all required rows fit
- card density reduces when content is long
- no row/list layout

---

## 15. TEAM DETAIL ③④⑤

Verify:
- identical card system for Frontend/Backend/Native
- only justified team accent differs
- no tables
- contribution text appears on Issue/PR cards
- responsive grid density

---

## 16. SPRINTPLAN ⑫

Every day card must separate:
- verified school schedule facts
- verified meeting/team actions
- AI-derived planning suggestions

Example structure:

```text
Tisdag 22 sep
📅 Schemafakta
PL-avstämning 12:30–14:00.

? AI-förslag
Ta med tydlig status på integration och test.
```

Do not blend source fact and recommendation into one unlabeled statement.

---

## 17. NEXT STEPS ⑬

Every card has provenance.

Priority of evidence:
1. meeting-protocol actions
2. approved/prefilled team actions
3. AI suggestions

AI suggestions use visible `?` and proposal wording where practical.

---

## 18. QUESTIONS TO PL ⑭

Every question is a modern card and includes provenance.

Distinguish:
- actual team question
- AI-suggested question

Cards adapt responsively to question length. Do not use oversized text that clips impact/source content.

---

## 19. EXPLICIT OMISSIONS

Conditional slides may only be omitted with a verified reason recorded in audit.

A slide may not disappear because layout is inconvenient.

---

## 20. FINAL DELIVERY GATE

Deliver only when:

```text
DATA_AUDIT == PASS
WCAG_2_2_AA == PASS
CONTENT_COMPLETENESS == PASS
VISUAL_CARD_SYSTEM == PASS
RESPONSIVE_TYPOGRAPHY == PASS
PROVENANCE_AND_AI_LABELING == PASS
OVERFLOW == PASS
ARTIFACT_COLLISION_CHECK == PASS
```

If any gate fails:
1. fix
2. rerender
3. reinspect actual artifact
4. deliver only after all gates pass

---

**Status:** PRODUCTION
**Version:** 4.0
**Last updated:** 2026-09-17
