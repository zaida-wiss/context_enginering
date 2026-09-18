---
name: mandatory_reading_order
description: THE ONLY instruction — read and follow SYSTEM_CONTRACT.yaml
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER

## EXECUTION ENTRY POINT

Before creating any presentation, follow this order exactly.

Read `AUTHORITY_REGISTRY.yaml` first. It is the canonical list of active,
validation, reference and retired files. Never load a retired guide during a
production presentation run.

**PRE-MEETING CONTEXT:** This presentation is risk-focused preparation for the CTO Feed Forward task (Sept 24 video, Sept 28 feedback). Risk analysis must show concrete impact on THIS WEEK's decisions, not just list concerns.

### Commitment gate

You must commit to all of these:

- Never guess on data.
- Never hallucinate assignees, PRs, branches, statuses, reviewers, merger identities, times or source facts.
- Never skip required authority files or validation gates.
- Never present AI inference as verified fact or team decision.
- Never violate WCAG 2.2 AA for any reason, including layout pressure.
- Never clip, overlap or hide required content.
- Never use automatic shrink-to-fit.
- Slide titles must never be shrunk to solve layout pressure.
- Start normal text at the preferred/larger size and reduce only when required, never below the role minimum.
- Keep multiline text at the minimum line spacing defined by `READABILITY_HARD_RULES.md` / `CARD_COMPONENT_STANDARD.md`.
- Render meeting-point headers with ordinary digits (`✏️ 1.`, `✏️ 2.`, `✏️ 13.`), never circled-number glyphs.
- Keep name/identity and verification/provenance in the bottom information zone of every card when those fields exist.
- For every merged PR, perform the dedicated merger + submitted-review lookup before rendering `Merged:` / `Review:`.
- Never use `requested_reviewers` as evidence that an actual review happened.
- If content still does not fit at the accessible minimum, change card geometry, reduce card density or paginate.

If these conditions cannot be met: STOP.

---

## 0️⃣ READ `INTEGRITY_CONSTRAINT.md`

Data integrity rules are non-negotiable.

Capacity is meeting data, not invented data.

PRE-MEETING:
- capacity may be missing
- show `○ Kapacitet fastställs under mötet`
- never estimate hours

POST-MEETING:
- capacity must be present
- otherwise STOP

---

## 1️⃣ READ `SYSTEM_CONTRACT.yaml`

This owns orchestration:
- execution sequence
- gates
- STOP/CONTINUE decisions
- data validation
- delivery rules

Follow `execution_sequence` exactly.

---

## 2️⃣ READ PRESENTATION AUTHORITIES BEFORE COMPOSITION

Read in this order:

1. [`AUTHORITY_REGISTRY.yaml`](AUTHORITY_REGISTRY.yaml)
2. [`design/ACCESSIBILITY_NEURODIVERSITY.md`](design/ACCESSIBILITY_NEURODIVERSITY.md)
3. [`design/VISUAL_DESIGN_MANDATORY.md`](design/VISUAL_DESIGN_MANDATORY.md)
4. [`design/READABILITY_HARD_RULES.md`](design/READABILITY_HARD_RULES.md)
5. [`design/CARD_COMPONENT_STANDARD.md`](design/CARD_COMPONENT_STANDARD.md)
6. [`design/PROVENANCE_AND_AI_LABELING.md`](design/PROVENANCE_AND_AI_LABELING.md)
7. [`data/PR_MERGE_REVIEW_IDENTITY.md`](data/PR_MERGE_REVIEW_IDENTITY.md)
8. [`monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md`](monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md)
9. [`monday_meeting/design/SLIDE_DETAIL_SPEC.md`](monday_meeting/design/SLIDE_DETAIL_SPEC.md)
10. [`monday_meeting/design/TEMPLATE_REFERENCE.html`](monday_meeting/design/TEMPLATE_REFERENCE.html) — reference only

### Authority order for conflicts

1. **Accessibility / WCAG 2.2 AA** — absolute boundary
2. **Global visual design** — theme and global slide roles
3. **Readability hard rules** — fixed slide-title size, dyslexia-friendly type, ordinary meeting-point digits, larger text minima, line spacing, pedagogical microcopy, dependency-aware order
4. **Card component standard** — card internals, bottom information zone and card role hierarchy
5. **Provenance standard** — fact/team/AI source identity
6. **PR merge/review identity contract** — actual merger + submitted review acquisition
7. **Overflow guard** — responsive fit, grid density, pagination
8. **Slide detail spec** — content fields and semantic slide purpose
9. **Template reference** — example only

### Meeting-point notation clarification

`SLIDE_DETAIL_SPEC.md` may use symbols such as `①`, `⑬` in documentation as **semantic section identifiers only**. They are not rendered typography.

Rendered meeting headers must follow `READABILITY_HARD_RULES.md`:
- `✏️ 1. ...`
- `✏️ 2. ...`
- `✏️ 13. ...`

This is not a conflict: semantic document identifiers and rendered presentation labels are separate roles.

No lower authority may weaken WCAG, readability, required identity lookup or provenance.

---

## 3️⃣ RESPONSIVE FIT RULE

For every slide/card:

1. Start at preferred typography sizes.
2. Keep slide titles at **36 pt minimum**; they are never a fit variable.
3. Wrap text naturally.
4. Keep dyslexia-friendly type weight and minimum line spacing.
5. Reduce normal/card text deliberately only inside the permitted role-specific range.
6. Maintain WCAG AA contrast and symbol+text redundancy.
7. Keep natural line spacing and the hard minimum block gaps from `READABILITY_HARD_RULES.md`.
8. Keep the top content group separate from the card's bottom identity/verification zone.
9. Let cards grow or reduce grid density when required.
10. If content still does not fit at the permitted accessible minimum, create a continuation slide.

Forbidden:
- shrinking slide titles below 36 pt
- clipping
- overlaps
- missing rows
- automatic shrink-to-fit
- fonts below component/readability minimum
- compressed line spacing or block spacing below the hard minimum
- heavy/black heading weight used to compensate for weak hierarchy
- circled-number glyphs in rendered meeting-point headers
- moving bottom-anchored identity/verification into the body area merely to make a card fit
- contrast below WCAG AA
- color-only meaning
- provenance removed to save space
- pedagogical/project-value explanation removed to save space

---

## 4️⃣ PROVENANCE RULE

Whenever content is not explicitly present in a registered source, label it.

Use:
- `📅 Schemafakta` — explicitly in registered school schedule
- `👥 ✅ Mötesprotokoll` / equivalent — explicitly supplied or confirmed by team
- `🔎 AI-analys` — AI interpretation, synthesis or assessment of verified evidence
- `⭐ AI-förslag` — AI recommendation, suggested action or suggested question
- `⚠ Källa behöver verifieras` — origin cannot be verified

Do not use the same icon for analysis and proposals.

This applies globally, especially to sprintplan, sprintmål, prioritering, nästa steg and frågor till PL.

---

## 5️⃣ MERGER + REVIEW LOOKUP RULE

For every merged PR shown in ①, ①a or ①b:

1. Fetch PR metadata.
2. Resolve the actual merger (`merged_by` first; registered fallback evidence only if needed).
3. Fetch **submitted PR reviews**.
4. Collect unique reviewers whose submitted review state is `APPROVED`.
5. Render verified display names in `Merged:` and `Review:`.
6. Leave a value blank only after the dedicated lookup has actually been performed and produced no verifiable identity.

Do not populate `Review:` from `requested_reviewers`.
Do not assume PR author, assignee or commit author is the merger.

Follow [`data/PR_MERGE_REVIEW_IDENTITY.md`](data/PR_MERGE_REVIEW_IDENTITY.md) exactly.

---

## 6️⃣ FOLLOW `execution_sequence`

Continue from `SYSTEM_CONTRACT.yaml` and execute every step in order.

---

## REQUIRED DATASETS

### team_roster
- Source: `GITHUB_TEAM_ROSTER`
- Access: `_memory/TEAM_ROSTER.md`
- Missing → STOP

### merged_prs
- Source: `GITHUB_MERGED_PRS`
- Preferred access: GitHub Connector/API
- Follow registered fallback order only
- **For every included merged PR, merger identity + submitted reviews are required lookup operations**
- All fallbacks fail → INCOMPLETE → gate decides STOP

### active_issues
- Source: `GITHUB_OPEN_ISSUES`
- Preferred access: GitHub Connector/API
- Follow registered fallback order only
- All fallbacks fail → INCOMPLETE → gate decides STOP

---

## FORBIDDEN IMPLEMENTATIONS

Do not use:
- shell network commands (`git clone`, `git fetch`, `curl`, `wget`)
- generic web search for registered project data
- unregistered URLs/sources
- model knowledge as source
- `requested_reviewers` as proof of an actual submitted review

---

## RENDER COMPLETENESS

Before delivery, the rendered artifact must satisfy:

```text
wcag_aa_violation_count == 0
color_only_information_count == 0
text_overlap_count == 0
card_overlap_count == 0
text_outside_card_count == 0
text_clipping_count == 0
out_of_bounds_element_count == 0
font_below_component_minimum_count == 0
slide_title_below_36pt_count == 0
slide_title_shrunk_for_fit_count == 0
body_text_below_role_minimum_count == 0
card_block_spacing_violation_count == 0
text_line_spacing_below_minimum_count == 0
meeting_point_uses_circled_number_count == 0
meeting_point_number_missing_count == 0
excessively_heavy_heading_weight_count == 0
identity_not_bottom_anchored_count == 0
verification_not_bottom_anchored_count == 0
bottom_information_zone_overlap_count == 0
missing_required_card_row_count == 0
next_step_card_missing_project_value_microcopy_count == 0
verified_dependency_not_reflected_in_plan_count == 0
uneven_row_spacing_caused_by_vertical_justification == 0
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
merged_pr_without_merger_lookup_count == 0
merged_pr_without_submitted_reviews_lookup_count == 0
review_field_populated_from_requested_reviewers_count == 0
verified_approving_reviewer_omitted_from_card_count == 0
verified_merger_omitted_from_card_count == 0
```

If any check is non-zero:
1. STOP delivery.
2. Fix typography/layout/provenance/data lookup.
3. Add continuation slide(s) where required.
4. Rerender.
5. Reinspect the actual artifact.

---

## NEXT STEP

Go to `SYSTEM_CONTRACT.yaml`, then follow the authorities above before rendering.
