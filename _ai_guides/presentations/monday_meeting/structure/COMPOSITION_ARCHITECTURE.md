---
name: monday_meeting_composition_architecture
description: MANDATORY — composition order, meeting-point continuity, empty states and cross-slide red threads
metadata:
  type: structural_authority
  critical: true
  version: 1.2
---

# MONDAY MEETING COMPOSITION ARCHITECTURE

This file owns **how the complete Monday-meeting deck is composed across slides**.

It owns:
- mandatory meeting-point order ⓪ → ① → … → ⑭
- whether a point renders content, a verified empty state or a continuation
- cross-slide continuity / red threads
- meeting-point page sequencing
- composition completeness before delivery

It does **not** own:
- the detailed content fields inside each point — owned by `SLIDE_DETAIL_SPEC.md`
- colors, typography or card visuals — owned by the design authorities
- provenance semantics — owned by `PROVENANCE_AND_AI_LABELING.md`
- data acquisition — owned by `DATA_ACQUISITION_CONTRACT.yaml`

## 1. CANONICAL MEETING ORDER

The deck always follows this sequence:

```text
⓪ Cover
① Avklarat sedan förra mötet
② Nuläge och deadlines
③ {REGISTERED_TEAM_1}
④ {REGISTERED_TEAM_2}
⑤ {REGISTERED_TEAM_3}
⑥ Blockers och beroenden
⑦ Risker
⑧ Kapacitet och estimering
⑨ Prioritering och scope
⑩ Tekniska beslut
⑪ Sprintmål
⑫ Sprintplan
⑬ Nästa steg
⑭ Frågor till PL
```

No custom thematic section may replace, reorder or silently skip an official meeting point.

A point may use multiple physical slides when required for readability. Continuation slides preserve the same official meeting-point identity.

Meeting point ① has a mandatory physical-page sequence:
`{PRIMARY_INTEGRATION_BRANCH} → {REGISTERED_COLLECTION_BRANCHES_IN_PROJECT_ORDER} → Teamsammanfattning`.
Render the primary integration subsection, one subsection for every registered collection branch, and the team-summary subsection. Verified-empty or source-incomplete branch pages are explicit rather than silently omitted.

## 2. PRESENCE / EMPTY-STATE RULE

For each point ①–⑭, exactly one of these must be true:

1. verified content is rendered;
2. a verified empty/unknown state is rendered when the point still matters to the agenda;
3. omission is explicitly permitted by the owning slide rule and recorded in the render audit.

Silently skipping a point is forbidden.

Examples of acceptable empty states:
- `Inga verifierade blockers i det kontrollerade underlaget`
- `Inga nya tekniska beslut verifierade`
- `Sprintmål saknas i registrerad källa — behöver bekräftas`

### Verified empty versus incomplete — hard rule

A verified empty state is allowed only when acquisition succeeded for the
applicable dataset and the verified result contains zero matching records.

A missing, failed or incomplete source is not an empty result. Render it as an
explicit unknown/incomplete state with `⚠`, name the missing source and follow
the incomplete-source user-decision gate in `SYSTEM_CONTRACT.yaml`. Never use
phrases such as `Inga blockers` or `Inget arbete` when the source is incomplete.

Every empty or incomplete state preserves provenance and never invents certainty.

## 3. CROSS-SLIDE RED THREADS

The deck must preserve these connected reasoning chains when relevant evidence exists.

### Work thread
① completed work → ③–⑤ current/remaining registered-team work → ⑨ priority → ⑪ goals → ⑫ plan → ⑬ next steps.

This is a progressive funnel, not permission to duplicate the same content:
- ③–⑤ own the complete verified forward-looking work state for the registered team assigned to each team slot
- ⑨ owns project-wide selection, priority and execution order
- ⑬ owns the concise executable action output
- an item may reappear only when its function changes between these stages

### Dependency thread
③–⑤ registered-team blockers → ⑥ dependency view → ⑨ execution order → ⑫ plan/fallback → ⑬ next actions.

### Risk thread
⑦ risk → ⑧ realistic capacity constraint when applicable → ⑨ changed priority/order → ⑪ goal pressure/alignment → ⑫ mitigation in plan → ⑬ concrete action.

### Capacity thread
③–⑤ registered-team workload evidence → ⑧ verified/qualitative capacity → ⑨ WIP/order choice → ⑪ realistic goal → ⑫ feasible plan.

A later slide must not ignore a verified blocker/risk/capacity fact that materially changes execution order.

Do not invent numeric hours, percentages or estimates to make a thread look complete.

## 4. SHARED VISUAL COMPOSITION

The deck uses a consistent card system as its primary visual language.

Default slide-level composition is a responsive card/grid system:
- ②: a chronological course/project timeline with an explicit current-week marker
- ⑥: blocker/dependency cards with optional arrows/connectors
- ⑦: risk cards that expose risk → mitigation → planning impact
- ⑫: day/plan cards ordered chronologically
- ⑬: concise action cards

Point ② boundary:
- blockers, dependencies and risks are excluded from the timeline/map and belong to ⑥/⑦
- the active sprint interval is displayed from its actual start date, not the meeting date

Registered slide-level exception:
- ⑨ uses vertically stacked execution groups in the order
  `Prioritering först → Parallellt → Backlog → Förslag framåt`.
  Cards remain the component language inside each group.

Use fewer/wider cards and continuation slides when needed. No other meeting
point may introduce a different slide-level composition without an explicit
registered rule/decision.

## 5. MEETING-POINT HEADER IDENTITY

Every physical slide belonging to meeting points 1–14 renders:

```text
✏️ [ordinary Arabic number]. [official title]
[optional subordinate subtitle]
```

Canonical rendered identities are `1.` through `14.`.
Circled symbols may remain internal documentation identifiers but are not used
as the rendered meeting-point identity.

Cover ⓪ is the only exception and does not use the pen header.

## 6. POINT-LOCAL PAGE COUNTER

When a meeting point spans multiple physical slides, show a quiet page counter:
`(x/y)`

The counter is local to the meeting point, not the whole deck.

It never replaces the meeting-point symbol/title.

## 7. COMPOSITION GATE

Before delivery verify:

```text
official_meeting_points_in_order == true
silent_meeting_point_skip_count == 0
unrecorded_omission_count == 0
cross_slide_thread_break_count == 0
default_card_grid_missing_without_registered_exception_count == 0
point9_vertical_sequence_missing_count == 0
meeting_point_header_identity_failure_count == 0
point1_mandatory_subsection_missing_count == 0
point2_not_chronological_timeline_count == 0
point2_current_week_marker_missing_count == 0
point2_blocker_or_risk_card_count == 0
```

Any failure → STOP and correct the owning context rule or renderer before delivery.
