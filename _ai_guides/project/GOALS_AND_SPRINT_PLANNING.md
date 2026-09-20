---
name: goals_and_sprint_planning
description: Canonical reasoning and provenance standard for project goals, sprint goals, milestones and planning proposals
version: 1.1
metadata:
  type: project_authority
  status: active
  last_updated: 2026-09-18
---

# Goals and sprint planning

## Purpose

This standard teaches how project goals and sprint planning should be understood,
verified and improved without inventing current project state.

It separates:

- **what is currently decided**
- **what evidence shows about progress**
- **what the AI proposes next**

That distinction is essential for both day-to-day work and presentations.

## Core principle

```text
verified source → current decided state
verified project evidence → progress / deviation
AI reasoning → analysis
AI proposal → possible future state
```

The AI may be proactive about the future while remaining strict about the present.

## Goal hierarchy

Use the smallest relevant level:

```text
project purpose
  ↓
project goals / major outcomes
  ↓
milestones
  ↓
sprint goal(s)
  ↓
planned outcomes / work packages
  ↓
issues
  ↓
implementation tasks
```

Every lower level should be explainable in relation to a higher-level purpose.

### Why

A team can be busy while still moving in the wrong direction. Goal traceability
helps distinguish activity from progress.

## Current-state source resolution

### 1. Explicit sprint planning source

Resolve the registered conditional source `GOOGLE_SPRINT_PLANNING`.

When the Team Avanza 1 spreadsheet contains an accessible worksheet/tab named
exactly `Sprintplanering`, use that source as the primary source for the
**decided sprint purpose, sprint goals and planned focus** represented there.

The AI reads the actual values from the source. It does not infer missing cells.

When `GOOGLE_SPRINT_PLANNING` reports `UNAVAILABLE_NOT_YET_CREATED`, continue
to confirmed meeting decisions and registered milestone/course sources. GitHub
activity may explain progress but does not become a decided sprint goal by
inference.

### 2. Confirmed meeting decisions

Use the registered meeting protocol for:
- confirmed changes made after the plan was written
- clarified priorities
- agreed scope adjustments
- confirmed blockers/constraints that changed the plan

A later confirmed decision can supersede an earlier plan when the source clearly
shows that the team changed the decision.

### 3. Registered milestones / course requirements

Use registered milestones, deadlines and course requirements to explain why a
goal matters or what boundary the plan must respect.

These sources do not automatically define the sprint goal unless the team or
planning source connects them to the sprint.

### 4. GitHub project evidence

Issues, pull requests, branches and commits show execution and progress.

They are evidence of what is being worked on; they do not automatically redefine
the decided sprint goal.

## Source truth vs proposal

### Decided goal

A decided goal is supported by a verified planning/meeting source.

Render/describe it as a source-backed project fact.

### AI analysis

Use `🔎 AI-analys` when the model interprets the relationship between:
- current goal
- progress
- dependencies
- risks
- capacity
- milestone pressure
- cross-layer integration state

Analysis explains; it does not silently replace the plan.

### AI proposal

Use `⭐ AI-förslag` when the model recommends:
- a different sprint goal
- a changed priority
- a new milestone
- a different sequence
- additional or changed issues
- reduced scope
- a clearer success criterion

## Proposal contract

Every proposal that changes an existing plan states:

```yaml
proposal:
  current_state: "[verified existing goal/plan]"
  proposed_change: "[exactly what would change]"
  from: "[old wording/scope/order when known]"
  to: "[proposed wording/scope/order]"
  why: "[evidence-based reason]"
  expected_effect: "[what improves or becomes safer/clearer]"
  tradeoff: "[what is delayed, reduced or costs more, if applicable]"
  evidence:
    - "[verified source]"
  provenance: "⭐ AI-förslag"
```

The user/team should be able to see immediately:
1. **what** AI wants to change
2. **why**
3. **what consequence** the change has

## Project planning calendar and hard constraints

Before proposing sprint scope, work distribution, sequencing or capacity, load
the selected project's registered sprint cadence, work calendar and hard
planning constraints.

Project-specific workdays or non-workdays must never be inferred from this
generic authority. When a selected project marks a day as unavailable for
project work, do not allocate, recommend or count project work on that day.

A count of eligible workdays does not imply a fixed number of hours. Numeric
hours, percentages, velocity or individual capacity require verified project
sources. If they are unavailable, keep numeric capacity unknown and use only
verified qualitative planning evidence.

## Proposing future sprint planning

When asked what the next sprint should focus on, the AI should actively help.

Use verified current information to propose:
- a sprint purpose
- 1–3 meaningful sprint goals when that fits the project
- candidate milestones/checkpoints
- success evidence
- necessary dependencies
- candidate issues required to reach the goal
- work that can proceed in parallel
- work that should wait
- risks/unknowns that need validation

Each future item remains `⭐ AI-förslag` until the team confirms it.

### Quality test for a proposed sprint goal

A useful goal should answer:

- What outcome should be different by the end of the sprint?
- Why is that outcome valuable now?
- How will the team know it happened?
- Which important dependency/risk constrains it?
- Which issues plausibly contribute to it?

Prefer outcome language over activity language.

Example distinction:

```text
Activity: "Jobba på tester"
Outcome:  "Kärnflödet har verifierade tester för de riskfyllda integrationspunkterna"
```

The example illustrates form only; it is not project data.

## Milestones

A milestone represents a meaningful checkpoint in the path toward a larger
project outcome.

Good milestone candidates often correspond to:
- an integrated capability
- an external review/deadline
- a critical contract becoming stable
- a demoable end-to-end flow
- a major risk being reduced enough to proceed
- a release/readiness checkpoint

AI may suggest a milestone when evidence shows a useful checkpoint is missing.
It labels the milestone `⭐ AI-förslag` until confirmed.

## From goal to issues

When proposing issues from a goal:

1. identify the outcome
2. identify necessary capabilities/contracts
3. identify dependencies
4. inspect existing issues before suggesting duplicates
5. propose only the missing work
6. use the `issue_creation` task bundle for the issue body
7. explain how each proposed issue contributes to the goal

A proposed issue should never be presented as existing work until verified in
the project tracker.

## Progress and deviation

Compare verified execution evidence with the decided goal.

Useful states:

```yaml
aligned:
  meaning: "work evidence supports the decided goal"

needs_clarification:
  meaning: "relationship between current work and goal is unclear"

deviation:
  meaning: "verified work direction materially differs from the decided goal"

proposal:
  meaning: "AI recommends changing the plan based on evidence"
```

A deviation is not automatically a failure. It may indicate:
- a deliberate adaptation
- new information
- an unresolved dependency
- a changed risk
- scope drift
- a plan that should be updated

The AI should investigate which explanation is supported before recommending
action.

## Learning mode

When helping a student/team member, explain the professional reasoning:

- why goals are outcomes rather than task lists
- why sprint goals should constrain prioritization
- why issues should trace to an outcome
- why plans may change when evidence changes
- why a changed plan should be explicit rather than silently drifting

The goal is to teach planning judgment, not only fill in fields.

## Presentation integration

Presentations use this standard to distinguish:
- decided sprint goals
- progress evidence
- `🔎 AI-analys` of alignment/deviation
- `⭐ AI-förslag` for a better next plan

The presentation may challenge the current plan, but it shows the original
source-backed plan and the proposed change separately.

---

**Status:** ACTIVE
**Version:** 1.1
**Last updated:** 2026-09-18
