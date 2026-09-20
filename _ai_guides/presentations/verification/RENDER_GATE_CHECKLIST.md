---
name: render_gate_checklist
description: Mechanical checklist for when a Monday Meeting presentation may be rendered and delivered
metadata:
  type: process
  critical: true
  version: 5.5
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
- total relevant commits to the selected project's registered integration/collection branches
- total open assigned/active issues

Required classification:
- every team/workstream registered by the selected project
- cross-team/integration work when applicable
- other/unclassified only when evidence cannot map the item safely

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
mixed_team_card_color_only_identity_count == 0
dedicated_team_slide_missing_text_team_context_count == 0
dedicated_team_card_repeats_team_name_count == 0
mixed_team_card_missing_explicit_team_text_count == 0
verified_empty_state_from_incomplete_source_count == 0
```

Also verify:
- normal text contrast >= 4.5:1
- large text contrast >= 3:1
- meaningful component contrast >= 3:1
- transparency does not reduce effective contrast
- on dedicated team slides, the primary slide header explicitly names the team; cards do not need to repeat the team name
- on mixed-team slides, every relevant card includes an explicit non-color team label
- person and team are separate verified renderer fields; dedicated team cards show first name only, while mixed-team cards show person + team
- a verified empty state is used only after successful acquisition returns zero matching records
- missing/incomplete sources render `⚠` unknown states and never `Inga ...`
- team accent color is supplementary and never the sole ownership cue when no surrounding text identifies the team

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
- header, content and source/footer zones are visibly stable from slide to slide
- no content card enters the footer/source zone
- no footer/source text competes with primary content

### Five-second scan check

Required:

```text
five_second_scan_failure_count == 0
slide_zone_predictability_failure_count == 0
competing_primary_focus_count == 0
unclear_reading_direction_count == 0
inconsistent_primary_font_family_count == 0
```

For each rendered slide, inspect the actual PDF/image and verify font-family
consistency visually.

Then verify that within approximately five seconds a viewer can identify:
- meeting point;
- one primary purpose;
- primary card/group;
- reading order;
- provenance class when the slide mixes fact/analysis/proposal.

Any failure → reduce density/emphasis, reflow or paginate and rerender.

---

## 5. MEETING-POINT HEADER INTEGRITY

Slides 1–14 must render the meeting-point prefix and number as one coherent header identity.

Required:

```text
meeting_point_number_missing_count == 0
pen_without_meeting_point_number_count == 0
meeting_point_header_malformed_count == 0
rendered_circled_meeting_point_number_count == 0
point_1_develop_subtitle_not_exact_count == 0
point_1_collection_branch_slide_missing_count == 0
point_1_collection_branch_subtitle_not_exact_count == 0
point_1_mandatory_subsection_missing_count == 0
official_meeting_point_title_missing_count == 0
page_subtitle_replacing_meeting_point_title_count == 0
```

Manual checks:
- no slide may show `✏️` without its meeting-point number
- the meeting-point number must be an ordinary Arabic number with period, e.g. `1.` through `14.`
- the primary heading always contains the official meeting-point number + official meeting-point title
- page-specific descriptions are rendered as a separate subtitle beneath the official heading
- a subtitle such as `Mergat till develop` may never replace `✏️ 1. Avklarat sedan förra mötet`
- continuation/subsection markers may be secondary navigation, but every slide repeats the full official meeting-point heading
- numeric continuation suffixes such as `9-2` are forbidden; use the registered continuation convention

Any failure → STOP.

## Cover: current-week PL focus and school tasks

Required:

```text
cover_wrong_week_count == 0
cover_sprint_period_not_based_on_request_timestamp_count == 0
point2_timeline_not_chronological_count == 0
point2_full_course_period_missing_count == 0
point2_course_start_anchor_missing_count == 0
point2_final_delivery_anchor_missing_count == 0
point2_current_position_marker_missing_count == 0
point2_near_term_only_timeline_count == 0
point2_current_week_marker_missing_count == 0
point2_blocker_or_risk_card_count == 0
meeting_point_1_fact_after_data_cutoff_count == 0
current_week_pl_topic_missing_count == 0
current_week_deadline_missing_count == 0
pl_meeting_card_missing_target_time_purpose_count == 0
cover_generic_status_displacing_required_content_count == 0
school_task_missing_five_question_field_count == 0
school_task_answer_without_source_count == 0
school_task_unverified_answer_presented_as_fact_count == 0
```

Manual checks:
- the cover names the current sprint/week and the verified topic to handle with PL
- when a current-week PL/teamavstämning is verified, its primary card visibly contains all three meanings `🎯 Vad/fokus`, `🕒 När`, `💡 Varför`
- generic cards such as `Syfte`, `AI-läge`, `Viktigt nu`, status metrics or decorative summaries may appear only after all mandatory PL/school/deadline content is present; they never replace it
- the sprint period is resolved from the selected project's registered sprint-cadence authority using the request timestamp
- meeting point 2 renders a chronological course/project timeline with an explicit current-week marker
- the point-2 timeline visibly spans the **entire registered course/project period**, not only the current or next sprint
- the first visible timeline anchor corresponds to the registered course/project start
- the final visible timeline anchor corresponds to the registered final delivery/end milestone
- the current week/sprint marker is positioned between those anchors according to verified dates
- course weeks/phases, sprint boundaries and material verified milestones share the same chronological axis; continuation slides may segment the axis but may not omit its beginning or end
- a near-term-only timeline (for example current sprint + next deadline) fails even when its local dates are correct
- the point-2 timeline contains no blocker, dependency or risk cards; those remain in points ⑥ and ⑦
- boundary behavior follows the selected project's registered cadence exactly; regression fixtures may test concrete timestamps without making those dates global presentation rules
- meeting point 1 contains no factual activity after the actual acquisition cutoff
- the deck is framed as `Sprint in progress`, not as a retrospective for a closed sprint
- points 3–5 and 9 cover actionable remaining work through the displayed sprint end
- future facts and AI-proposed actions remain visibly distinct
- every school task/deadline in or affecting the week answers `Vad`, `När`, `Var`, `Varför`, `Hur`
- deadline meaning/consequence is visible under `Varför`
- submission, meeting or execution method is visible under `Hur`
- each answer is grounded in the selected project's registered context/data sources
- any missing answer remains visible as `⚠ [fält] kunde inte verifieras`
- an AI interpretation is separated as `🔎 AI-analys` and never substitutes for a verified answer
- if the cover cannot fit accessibly, the five-question content continues on `⓪a`; it is never dropped

---

### Meeting point 1 card standard

Required:

```text
point_1_separate_wip_slide_count == 0
point_1_verified_collection_merge_without_own_slide_count == 0
point_1_unverified_collection_activity_presented_as_merge_count == 0
```

- every physical slide repeats the primary heading `✏️ 1. Avklarat sedan förra mötet`
- the selected project's registered primary-integration subtitle, every registered collection-branch subtitle, and `Teamsammanfattning` are subtitles only
- every primary-integration page, including continuations, uses the exact subtitle registered by the selected project's repository-flow config; generic replacement subtitles are forbidden
- every collection branch registered by the selected project's repository-flow config gets its own physical slide sequence after the primary integration sequence, in registered project order, using its registered exact subtitle; use a verified empty/incomplete state when needed
- collection-branch slide inclusion is decided from verified merge evidence for that target branch in the sprint interval; ordinary direct commits/branch activity are not relabeled as merges
- if a collection branch has relevant direct work but no verified merge, that work may inform later active-work/planning slides but does not create a false `Mergat till ...` point-1 slide
- collection-branch merges may not be folded into the primary-integration sequence when the selected project's repository-flow rule requires a separate sequence pages or only mentioned in the team summary
- no page-specific subtitle may replace the official meeting-point heading
- detailed cards in meeting point 1 contain completed work only
- six cards is the capacity of one physical slide, not a total cap for meeting point 1
- all grounded completed items remain present across as many continuation slides as required
- fewer cards require insufficient grounded items or a documented WCAG/readability fit reason
- backlog, future plans, ordinary WIP, open questions and undecided proposals do not appear as detailed point-1 work cards
- a physical point-1 slide/subsection titled `Påbörjat men inte avklarat` is forbidden; qualifying unfinished value appears only at the end of the relevant team-summary card
- team summaries primarily summarize completed work
- a team summary may end with `Påbörjat men inte avklarat` only when verified activity already produced concrete partial value
- valuable unfinished work is never presented as completed
- detailed unfinished work belongs to points ③–⑤ and ⑨
- every team summary contains approximately 1–10 complete sentences
- every summary names all team members using first names and states only verified contributions
- review/help/integration work is included when verified
- every included decision was already made and verified; decisions still to be taken are forbidden in point 1
- open decision candidates belong to point ⑩ and unresolved PL questions belong to point ⑭
- a member without verified completed activity uses neutral evidence-limited wording, never a performance inference

### Forward planning in points 3–5

- each team/workstream registered into meeting points 3–5 includes its verified active, backlog, future and older inactive work
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
timestamp_not_quiet_microcopy_color_count == 0
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
- relevant timestamp uses the quiet microcopy/timestamp color defined by the global palette and remains deliberately subordinate to title/body content
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
merged_pr_merge_review_row_missing_count == 0
merged_pr_merge_review_row_not_bottom_zone_count == 0
merged_pr_merge_timestamp_missing_count == 0
verified_merger_omitted_from_card_count == 0
```

Unknown identity remains blank in the meeting card only after the dedicated lookup has been performed; uncertainty stays in the internal audit.

---

## 8. TIMESTAMP RELEVANCE

When rendered, timestamp must follow `CARD_COMPONENT_STANDARD.md`.

Merged PR cards:
- use merge timestamp
- render it as the **bottom-most row of the card**, single-line and right-aligned/lower-right where card geometry permits
- keep `Merged: … | Review: …` immediately above the timestamp inside the reserved bottom information zone
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
relevant_cross_team_contract_check_missing_count == 0
contract_review_finding_not_routed_count == 0
confirmed_support_work_omitted_from_plan_count == 0
confirmed_post_meeting_repo_action_missing_count == 0
```

Manual check:
- `⑥` dependency/blocker information feeds `⑨` prioritization and `⑬` next steps
- relevant integration contracts/interfaces between work areas or teams are checked before the meeting when applicable; non-applicable cases are recorded in the audit
- verified contract-review findings are routed to ⑥/⑦/⑩/⑬/⑭ according to their consequence instead of remaining isolated
- proposed order distinguishes `Först`, `Parallellt`, `Därefter` / `Vänta` where evidence permits
- every ordering step includes a short reason
- verified support/pairing/review/knowledge-transfer work that materially helps sprint delivery is represented as legitimate sprint work
- blockers are handled as team delivery constraints; the deck does not turn them into individual performance judgments
- confirmed meeting changes that require repository follow-up become concrete ⑬ actions with provenance
- AI-derived order uses `🔎 AI-analys` for reasoning and `⭐ AI-förslag — planeringsordning` for the recommendation

---

## 12. PROVENANCE

Validate against `PROVENANCE_AND_AI_LABELING.md`.

Required:

```text
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
rendered_missing_glyph_count == 0
rendered_replacement_glyph_count == 0
canonical_symbol_render_mismatch_count == 0
canonical_symbol_ascii_transliteration_count == 0
waiting_pr_pushpin_missing_before_identifier_count == 0
waiting_pr_bottom_pushpin_label_missing_count == 0
unverified_item_presented_as_confirmed_count == 0
content_block_provenance_symbol_missing_count == 0
slide_margin_source_full_label_missing_count == 0
inline_symbol_slide_margin_source_mismatch_count == 0
ai_no_finding_without_exact_checked_sources_count == 0
ai_check_trace_source_not_actually_inspected_count == 0
provenance_symbol_replaced_by_tag_count == 0
provenance_text_without_canonical_symbol_count == 0
ai_suggestion_without_star_count == 0
ai_analysis_without_magnifying_glass_count == 0
```

Manual checks:
- validation is performed on the final rendered/exported artifact, not only on source text
- no canonical symbol renders as an empty square, replacement character, unrelated glyph or invisible character
- no canonical symbol is transliterated to ASCII, including `📌 → |`, `✅ → +`, `🔎 → ~`, `⭐ → *`, `⚠ → !` or `📅 → #`
- every open/waiting PR card shows a visible pushpin before its PR identifier and repeats `📌 Väntar i PR` in the card-bottom row
- each symbol uses the primary font only when that font demonstrably renders it; otherwise the affected glyph/run uses a verified symbol-capable fallback
- each semantic content block starts with its canonical provenance symbol only
- each factual content block uses its canonical source symbol inline, close to the statement it supports
- the physical slide margin/footer deduplicates the used source symbols and expands each to its full readable source name/explanation
- ordinary cards do not repeat long source names merely to satisfy provenance; the inline symbol maps to the slide-margin explanation
- inline symbols and slide-margin source explanations agree exactly
- no tag, chip, badge, color or `?` replaces `⭐` or `🔎`
- when an AI health-check reports that no new signal was identified, any
  `🔎 AI-kontroll` trace lists the exact sources/locations actually inspected
- the AI check trace never lists a source that was not inspected
- an expected source that could not be checked is shown with `⚠` rather than
  being implied as analysed

## 12A. CAPACITY — PROJECT-FACING CONTENT

Required:

```text
capacity_personal_reason_exposed_count == 0
capacity_internal_ai_policy_visible_count == 0
capacity_missing_numeric_state_not_explicit_count == 0
```

Manual checks:
- availability is phrased as planning impact, not personal background
- health, travel or other private reasons are omitted from the deck
- the slide explains what the team can and cannot plan from the verified data
- internal model instructions such as `Vad AI inte får göra` are not shown to the audience
- when numeric capacity is unavailable, the audience sees that it is missing and
  that planning therefore uses qualitative constraints

---

## 12B. POINT 9 — VERTICAL PRIORITY VIEW

Required:

```text
point9_missing_priority_first_group_count == 0
point9_missing_parallel_group_count == 0
point9_missing_backlog_group_count == 0
point9_proposal_without_star_count == 0
point9_ai_order_without_analysis_label_count == 0
point9_dependency_not_reflected_in_order_count == 0
point9_duplicate_item_across_groups_count == 0
point9_team_coverage_gap_without_reason_count == 0
point9_vertical_sequence_missing_count == 0
point9_group_vertical_order_violation_count == 0
point9_side_by_side_group_count == 0
point9_meta_layout_language_visible_count == 0
suggested_issue_without_goal_link_count == 0
unverified_owner_presented_as_fact_count == 0
```

Manual checks:
- meeting point 9 uses the mandatory vertical execution sequence from `SLIDE_DETAIL_SPEC.md`
- inspect actual rendered geometry: each execution group begins below the previous group's bottom edge
- the four execution groups may not be arranged as a 2×2/four-quadrant matrix
- cards remain the internal components inside each group
- if the vertical sequence becomes dense, paginate instead of shrinking below readability minima
- no visible subtitle/body text explains presentation-layout mechanics such as `inte fyrkolumnstavla`, `vertical layout` or equivalent
- execution groups appear in the canonical logical order:
  1. `Prioritering först`
  2. `Parallellt`
  3. `Backlog — lägre prioritet`
  4. `Förslag framåt — finns ännu inte / behöver korrigeras`
- group 4 may be omitted only when verified empty; proposals that must remove a
  blocker or protect a critical path may be promoted to `Prioritering först`
  or `Parallellt` while retaining `⭐ AI-förslag`
- every selected-project registered team/workstream plus cross-team/integration work is considered as a planning perspective when relevant; this is a coverage check, not a column-layout rule
- team/layer ownership is shown with text/structure when useful and never by
  color alone
- an item appears in only one execution group on a physical planning sequence
- verified dependencies affect ordering when material
- AI-derived ordering uses one concise `🔎 AI-analys` at the useful group/slide
  level rather than repeating it mechanically on every existing issue
- proposed work is visibly `⭐ AI-förslag`
- every proposed issue/correction names the grounded gap, risk, dependency or
  goal that caused the proposal
- numeric capacity/estimate is shown only when source-verified
- missing numeric capacity remains explicit/qualitative rather than guessed
- continuation slides preserve the full meeting-point identity and follow the
  continuation convention owned by `SLIDE_DETAIL_SPEC.md`

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
- inline card/block source symbols remain present and agree exactly with the full source explanations in the slide margin/footer
- the measured footer container does not intersect cards, diagrams or slide bounds

---

## 14. COVER / SLIDE-SPECIFIC CONTENT

School/submission-task card checks:

```text
school_task_text_label_repetition_count == 0
school_task_missing_target_icon_count == 0
school_task_missing_time_icon_count == 0
school_task_missing_place_icon_count == 0
school_task_missing_purpose_icon_count == 0
school_task_missing_method_icon_count == 0
priority_color_without_symbol_text_count == 0
ordinary_project_card_using_school_task_5icon_template_count == 0
pl_meeting_card_missing_target_icon_count == 0
pl_meeting_card_missing_time_icon_count == 0
pl_meeting_card_missing_purpose_icon_count == 0
```

Manual checks:
- school/submission/deadline cards use `🎯 🕒 📍 💡 🛠` instead of repeated
  `VAD / NÄR / VAR / VARFÖR / HUR` labels
- the five-icon grammar is not imposed on ordinary GitHub issue/PR cards
- priority is shown with both visible level text/symbol and color
- priority color passes WCAG and does not replace provenance/status meaning
- red priority is reserved for verified critical/high-consequence school tasks

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
**Version:** 5.4
**Last updated:** 2026-09-17
