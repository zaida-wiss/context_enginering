---
name: render_gate_checklist
description: Mechanical checklist for when a Monday Meeting presentation may be rendered and delivered
metadata:
  type: process
  critical: true
  version: 4.4
---

# 🚨 RENDER-GATE CHECKLIST

A presentation may be delivered only when both data integrity and the actual rendered artifact pass.

This checklist validates existing authorities. It must not redefine their rules.

Authority order:
1. `SYSTEM_CONTRACT.yaml`
2. `ACCESSIBILITY_NEURODIVERSITY.md`
3. `VISUAL_DESIGN_MANDATORY.md`
4. `READABILITY_HARD_RULES.md`
5. `CARD_COMPONENT_STANDARD.md`
6. `PROVENANCE_AND_AI_LABELING.md`
7. `LAYOUT_OVERFLOW_GUARD.md`
8. `SLIDE_DETAIL_SPEC.md`
9. `TEMPLATE_REFERENCE.html` — reference only

---

## 1. DATA AUDIT

Required totals:
- total merged PRs
- total open PRs
- total commits to develop
- total open assigned/active issues

Required classification:
- Frontend
- Backend
- Native
- Cross-team
- Other

Checks:

```text
classified_merged_pr_set == repository_merged_pr_set
all_open_prs_accounted_for == true
all_open_assigned_issues_accounted_for == true
all_registered_team_members_accounted_for == true
```

Any failure → STOP.

---

## 2. DATA ACCURACY

Verify:
- real issue/PR IDs
- accurate state
- assignee verified or internally unknown
- merger/reviewer identity based on actual source evidence
- timestamp from source data
- contribution explanation grounded in issue/PR/diff/commit evidence
- no invented branch, owner, reviewer, merger, deadline or code effect

Internal uncertainty must not be converted into false certainty.

---

## 3. WCAG 2.2 AA

Required:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
```

Also verify:
- normal text contrast >= 4.5:1
- large text contrast >= 3:1
- meaningful component contrast >= 3:1
- transparency does not reduce effective contrast

Any failure → STOP.

---

## 4. GLOBAL VISUAL + READABILITY SYSTEM

Validate against `VISUAL_DESIGN_MANDATORY.md` and `READABILITY_HARD_RULES.md`:

```text
noncanonical_background_color_count == 0
noncanonical_card_surface_count == 0
high_glare_surface_count == 0
full_team_outline_count == 0
card_system_inconsistency_count == 0
slide_title_below_36pt_count == 0
slide_title_shrunk_for_fit_count == 0
body_text_below_role_minimum_count == 0
```

Manual visual checks:
- every slide title is 36 pt or larger
- no slide title was reduced to solve density
- normal/supporting text starts at the preferred larger size where possible
- smaller normal text is used only when required and remains above the role minimum

---

## 5. CARD-INTERNAL SYSTEM

Validate against `CARD_COMPONENT_STANDARD.md` and `READABILITY_HARD_RULES.md`.

Required:

```text
font_below_component_minimum_count == 0
auto_shrink_enabled_count == 0
card_block_spacing_violation_count == 0
pedagogical_line_not_directly_under_title_count == 0
next_step_card_missing_project_value_microcopy_count == 0
assignee_not_visually_emphasized_count == 0
visible_evidence_level_label_count == 0
unverified_identity_commentary_count == 0
timestamp_not_single_line_count == 0
timestamp_not_right_aligned_count == 0
```

Manual visual checks:
- pedagogical explanation is immediately below title
- every next-step/action card explains what the action concerns and why it matters to the project
- explanation is visibly larger than operational metadata
- verified assignee/developer name is easy to scan and uses the primary title text color
- team label remains secondary
- separate semantic blocks have the minimum required vertical spacing
- no text rows visually touch
- block spacing is not compressed merely to fit more cards

If card content cannot fit while preserving the required spacing and type sizes, reduce density or paginate.

---

## 6. MERGE / REVIEW METADATA

Canonical visible pattern:

```text
Merged: [verified name or blank] | Review: [verified name(s) or blank]
```

Acceptable:
- `Merged: Björn | Review: Zaida`
- `Merged: Björn | Review:`
- `Merged: | Review: Zaida`

Fail visible wording such as:
- `ej verifierat`
- `verifierad`
- `verifierat via merge-commit`
- `faktisk review behöver verifieras`
- `Merged by:`
- `Reviewed by:`

Required:

```text
legacy_merged_by_label_count == 0
legacy_reviewed_by_label_count == 0
unverified_identity_commentary_count == 0
merged_pr_without_merger_lookup_count == 0
merged_pr_without_submitted_reviews_lookup_count == 0
review_field_populated_from_requested_reviewers_count == 0
verified_approving_reviewer_omitted_from_card_count == 0
verified_merger_omitted_from_card_count == 0
```

Unknown identity remains blank in the meeting card only after the dedicated lookup has been performed; uncertainty stays in the internal audit.

---

## 7. TIMESTAMP

When rendered, timestamp must follow `CARD_COMPONENT_STANDARD.md`:
- one compact line
- lower-right aligned where card geometry permits
- quiet WCAG-safe color
- minimum 11 pt
- no semantic prefix

Example:

```text
14 sep · 10:16
```

Required:

```text
timestamp_two_line_count == 0
timestamp_prefix_count == 0
timestamp_not_right_aligned_count == 0
```

---

## 8. ACTIVE-WORK EVIDENCE

Evidence levels from `ACTIVE_WORK_DETECTION_MODEL.md` are internal only.

Fail any visible card containing:
- `GitHub · nivå 1`
- `GitHub nivå 2`
- `Level 1 evidence`
- equivalent evidence-strength label

Use meeting-relevant status instead when useful.

Required:

```text
visible_evidence_level_label_count == 0
```

---

## 9. CONTRIBUTION / PROJECT-VALUE EXPLANATION

Every Issue/PR/Merge card, dependency node and next-step/action card must contain grounded pedagogical microcopy when evidence supports it.

Required:

```text
missing_contribution_microcopy_count == 0
missing_dependency_project_value_microcopy_count == 0
next_step_card_missing_project_value_microcopy_count == 0
unsupported_contribution_claim_count == 0
```

For next-step cards, the explanation must answer:
- what the action concerns
- what it contributes/unlocks in the project or why it matters

---

## 10. DEPENDENCY-AWARE ORDER

When verified dependencies exist, the deck must make their effect on planning visible.

Required:

```text
verified_dependency_not_reflected_in_plan_count == 0
dependency_order_missing_when_evidence_exists_count == 0
```

Manual check:
- `⑥` dependency/blocker information feeds `⑨` prioritization and `⑬` next steps
- proposed order distinguishes `Först`, `Parallellt`, `Därefter` / `Vänta` where evidence permits
- every ordering step includes a short reason
- AI-derived order uses `🔎 AI-analys` for reasoning and `⭐ AI-förslag — planeringsordning` for the recommendation

---

## 11. PROVENANCE

Validate against `PROVENANCE_AND_AI_LABELING.md`.

Required:

```text
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
mixed_provenance_card_without_block_labels_count == 0
```

---

## 12. OVERFLOW / COLLISION

Required:

```text
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
missing_required_card_row_count == 0
plain_row_work_item_count == 0
```

Never solve density by shrinking slide titles, shrinking below role minima, removing pedagogical explanations or collapsing semantic block spacing.

---

## 13. COVER / SLIDE-SPECIFIC CONTENT

Validate slide purpose and required fields against `SLIDE_DETAIL_SPEC.md`.

Conditional slides may only be omitted for a source-grounded reason recorded in the audit.

---

## 14. FINAL DELIVERY GATE

Deliver only when:

```text
DATA_AUDIT == PASS
WCAG_2_2_AA == PASS
CONTENT_COMPLETENESS == PASS
GLOBAL_VISUAL_SYSTEM == PASS
READABILITY_HARD_RULES == PASS
CARD_COMPONENT_STANDARD == PASS
PROVENANCE_AND_AI_LABELING == PASS
OVERFLOW_AND_COLLISION == PASS
DEPENDENCY_AWARE_PLAN == PASS
ACTUAL_RENDER_INSPECTION == PASS
```

If any gate fails:
1. fix the owning authority implementation
2. rerender
3. reinspect the actual artifact
4. deliver only after all gates pass

---

**Status:** PRODUCTION
**Version:** 4.4
**Last updated:** 2026-09-17
