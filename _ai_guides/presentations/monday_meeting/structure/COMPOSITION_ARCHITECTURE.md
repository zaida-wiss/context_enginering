---
name: monday_meeting_composition_architecture
description: MANDATORY — composition order, meeting-point continuity, empty states and cross-slide red threads
metadata:
  type: structural_authority
  critical: true
  version: 1.0
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
③ Frontend
④ Backend
⑤ Native/System
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

An empty state must preserve provenance and must never invent certainty.

## 3. CROSS-SLIDE RED THREADS

The deck must preserve these connected reasoning chains when relevant evidence exists.

### Work thread
① completed work → ③–⑤ current/remaining team work → ⑨ priority → ⑪ goals → ⑫ plan → ⑬ next steps.

### Dependency thread
③–⑤ team blockers → ⑥ dependency view → ⑨ execution order → ⑫ plan/fallback → ⑬ next actions.

### Risk thread
⑦ risk → ⑧ realistic capacity constraint when applicable → ⑨ changed priority/order → ⑪ goal pressure/alignment → ⑫ mitigation in plan → ⑬ concrete action.

### Capacity thread
③–⑤ workload evidence → ⑧ verified/qualitative capacity → ⑨ WIP/order choice → ⑪ realistic goal → ⑫ feasible plan.

A later slide must not ignore a verified blocker/risk/capacity fact that materially changes execution order.

Do not invent numeric hours, percentages or estimates to make a thread look complete.

## 4. VISUAL VARIETY BY INFORMATION TYPE

The deck must not collapse every point into the same generic card grid.

Use the owning visual rules for the information type:
- ②: full-course horizontal timeline + nearest-focus callouts
- ⑥: dependency flow/graph when dependencies exist
- ⑦: risk blocks that expose risk → mitigation → planning impact
- ⑨: vertical priority sequence
- ⑫: chronological day/plan structure
- ⑬: concise action sequence/cards

Cards remain the shared component language, but the **slide-level composition must match the information problem**.

## 5. MEETING-POINT HEADER IDENTITY

Every physical slide belonging to ①–⑭ renders:

```text
✏️ [canonical circled meeting-point symbol] [official title]
[optional subordinate subtitle]
```

Canonical symbols:
`① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭`

The symbol must be visibly rendered in the final PDF/image. Missing-glyph squares fail validation.

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
generic_grid_replacing_required_visual_count == 0
meeting_point_header_identity_failure_count == 0
```

Any failure → STOP and correct the owning context rule or renderer before delivery.
