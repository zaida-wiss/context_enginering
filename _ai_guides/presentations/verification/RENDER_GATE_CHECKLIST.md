---
name: render_gate_checklist
description: Mechanical checklist for when a Monday Meeting presentation may be rendered and delivered
metadata:
  type: process
  critical: true
  version: 4.5
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

## 5. MEETING-POINT HEADER INTEGRITY

Slides ①–⑭ must render the meeting-point prefix and number as one coherent header identity.

Required:

```text
meeting_point_number_missing_count == 0
pen_without_meeting_point_number_count == 0
meeting_point_header_malformed_count == 0
```

Manual checks:
- no slide may show `✏️` without its meeting-point number
- the canonical pattern is `✏️ ⑨ Prioritering & scope` or equivalent title text
- continuation slides preserve the identity with lowercase letters, e.g. `✏️ ⑨a ...`
- numeric continuation suffixes such as `⑨-2` are forbidden

Any failure → STOP.

### Meeting point 1 card standard

- every physical slide in `①–①d` targets six cards when at least six grounded items exist and all six remain readable
- six cards is the capacity of one physical slide, not a total cap for meeting point 1
- all grounded items remain present across as many lowercase-letter continuation slides as required
- fewer cards require insufficient grounded items or a documented WCAG/readability fit reason
- required `①d` team-summary AI cards are substantive content; unrelated filler cards are forbidden
- order is `① develop` → `①a Backend collection` → `①b Native collection` → `①c active in window` → `①d AI team summaries`
- every item in meeting point 1 has verified merge/activity evidence inside the sprint window
- backlog, future plans and dormant older work do not appear in meeting point 1
- every `①d` team summary contains approximately 1–10 complete sentences
- every `①d` summary names all team members using first names and states only verified contributions
- review/help/integration work is included when verified
- every included decision is verified and distinguished from future questions/proposals
- a member without verified activity uses neutral evidence-limited wording, never a performance inference

### Forward planning in points 3–5

- Frontend, Backend and Native each include their verified active, backlog, future and older inactive work
- every item has a visible verified state and a concrete next-step field
- older inactive work uses neutral wording and shows last verified activity when available
- decisions appear when they materially govern upcoming work and retain their verified source
- AI-derived ordering, ownership, reactivation, deferral or closure uses `🔎 AI-analys` and/or `⭐ AI-förslag` as applicable
- completed work is not duplicated from point 1 unless needed as a short dependency reference

---

## 6. CARD-INTERNAL SYSTEM — ALL CARDS

Validate against `CARD_COMPONENT_STANDARD.md` and `READABILITY_HARD_RULES.md`.

Required:

```text
font_below_component_minimum_count == 0
auto_shrink_enabled_count == 0
card_block_spacing_violation_count == 0
pedagogical_line_not_directly_under_title_count == 0
next_step_card_missing_project_value_microcopy_count == 0
legacy_developed_by_label_count == 0
legacy_identity_prefix_count == 0
unnecessary_activity_timestamp_count == 0
identity_row_not_primary_color_count == 0
timestamp_not_primary_color_count == 0
secondary_text_too_prominent_count == 0
assignee_not_visually_emphasized_count == 0
visible_evidence_level_label_count == 0
unverified_identity_commentary_count == 0
timestamp_not_single_line_count == 0
timestamp_not_right_aligned_count == 0
```

Manual visual checks across **every card type**:
- card title uses primary text color
- person/team identity row, when present, uses the same primary text color as the title
- relevant timestamp, when present, uses the same primary text color as the title
- pedagogical explanation is calmer/secondary
- branch/status/provenance/ordinary metadata is quieter than the explanation while still WCAG-AA compliant
- no card displays `Utvecklat av`, `Developed by`, `Developer:` or `Assigned to:` before the identity row
- every next-step/action card explains what the action concerns and why it matters to the project
- separate semantic blocks have the minimum required vertical spacing
- no text rows visually touch
- block spacing is not compressed merely to fit more cards

If card content cannot fit while preserving the required spacing and type sizes, reduce density or paginate.

---

## 7. MERGE / REVIEW METADATA

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

## 8. TIMESTAMP RELEVANCE

When rendered, timestamp must follow `CARD_COMPONENT_STANDARD.md`.

Merged PR cards:
- use merge timestamp
- do not replace it with PR creation or latest commit time

Active/open cards:
- do not show PR-created/latest-commit/issue-created timestamps automatically
- show time only when it materially helps meeting status understanding

Required:

```text
timestamp_two_line_count == 0
timestamp_prefix_count == 0
timestamp_not_right_aligned_count == 0
unnecessary_activity_timestamp_count == 0
merged_pr_wrong_timestamp_type_count == 0
```

Example:

```text
14 sep · 10:16
```

---

## 9. ACTIVE-WORK EVIDENCE

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

## 10. CONTRIBUTION / PROJECT-VALUE EXPLANATION

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

## 11. DEPENDENCY-AWARE ORDER

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

## 12. PROVENANCE

Validate against `PROVENANCE_AND_AI_LABELING.md`.

Required:

```text
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
mixed_provenance_card_without_block_labels_count == 0
provenance_symbol_replaced_by_tag_count == 0
provenance_text_without_canonical_symbol_count == 0
ai_suggestion_without_star_count == 0
ai_analysis_without_magnifying_glass_count == 0
```

Manual checks:
- each source label starts with its canonical symbol
- no tag, chip, badge, color or `?` replaces `⭐` or `🔎`
- mixed cards repeat the required symbol inside each relevant block

## 12A. FOUR-TEAM BOARD — POINT 9

Required:

```text
team_column_missing_count == 0
open_pr_without_pushpin_number_count == 0
issue_or_pr_number_without_team_color_count == 0
team_identified_by_color_only_count == 0
open_pr_missing_contribution_text_count == 0
assigned_issue_missing_order_count == 0
assigned_issue_dependency_not_visualized_count == 0
dependency_without_link_symbol_count == 0
ai_dependency_without_both_symbols_count == 0
ai_assignment_without_reason_count == 0
suggested_issue_without_goal_link_count == 0
```

Manual checks:
- every slide for point 9 has exactly `Frontend | Backend | Native | Cross-team`
- meeting point 9 remains a fixed `1×4` team-column layout on every continuation slide
- continuation slides use lowercase letters: `9a`, `9b`, `9c`, `9d`, `9e`
- cards adapt to text length without violating typography minima
- empty team columns remain visible with a verified empty state
- point 9 renders every open PR as `📌 #[PR-number]` with its contribution directly below
- every issue/PR number uses the verified owning team's accessible color
- team ownership also appears through the team column/section or text, never color alone
- point 9 includes all remaining assigned issues, an order marker and a visible directed dependency relation when applicable
- point 9 dependency text and dependency visual agree and retain provenance
- every dependency view/relation starts with `🔗 Beroende`
- every AI-interpreted dependency shows both `🔗 Beroende` and `🔎 AI-analys`
- point 9 separates `🔎 AI-analys` from `⭐ AI-förslag`
- every allocation recommendation names a task/person, motivation and its evidence limits
- every suggested issue identifies a grounded gap/goal and has been checked against existing issues/PRs
- `📌` never replaces the item's provenance symbol

---

## 13. OVERFLOW / COLLISION

Required:

```text
text_overlap_count == 0
card_overlap_count == 0
card_child_container_overlap_count == 0
card_fixed_text_height_count == 0
bottom_zone_intrusion_count == 0
card_priority_hierarchy_violation_count == 0
level_4_contrast_failure_count == 0
slide_missing_source_footer_count == 0
used_source_missing_from_footer_count == 0
unverifiable_source_missing_warning_count == 0
source_footer_overlap_count == 0
meeting_protocol_without_meeting_symbol_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
missing_required_card_row_count == 0
plain_row_work_item_count == 0
```

Never solve density by shrinking slide titles, shrinking below role minima, removing pedagogical explanations or collapsing semantic block spacing.

Container checks:
- body/supporting text uses 1.15 line spacing unless the rendered font requires more
- every semantic block has its own measured child container
- stacked blocks follow vertical flow; no child starts before the previous child's measured bottom plus required gap
- the bottom information zone is measured and reserved before upper content layout
- any child-container intersection fails delivery, even when the text remains technically inside the card

Priority checks:
- issue title and assignee are the strongest level-1 elements
- `⭐ AI-förslag` is level 2
- merge/review, pedagogical explanation and `🔎 AI-analys` are level 3
- sources, branch, timestamp and technical metadata are level 4
- level 4 remains readable, preserves source symbols and passes WCAG contrast
- color is not the only distinction between priority levels

Source-footer checks:
- every physical and continuation slide has a bottom source footer
- the footer lists only deduplicated sources used on that slide
- every verified source has its canonical symbol and readable name
- every meeting-protocol source uses the full label `👥 ✅ Mötesprotokoll`
- every expected but unverifiable source has `⚠`, explicit failure text and a struck-through name
- card/block provenance remains present and agrees with the footer
- the measured footer container does not intersect cards, diagrams or slide bounds

---

## 14. COVER / SLIDE-SPECIFIC CONTENT

Validate slide purpose and required fields against `SLIDE_DETAIL_SPEC.md`.

Conditional slides may only be omitted for a source-grounded reason recorded in the audit.

---

## 15. FINAL DELIVERY GATE

Deliver only when:

```text
DATA_AUDIT == PASS
WCAG_2_2_AA == PASS
CONTENT_COMPLETENESS == PASS
GLOBAL_VISUAL_SYSTEM == PASS
READABILITY_HARD_RULES == PASS
MEETING_POINT_HEADER_INTEGRITY == PASS
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
**Version:** 4.5
**Last updated:** 2026-09-17
