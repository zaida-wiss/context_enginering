---
name: dependencies_and_capacity
description: Canonical project standard for dependency detection, estimation gaps, capacity awareness and flow planning
version: 1.0
metadata:
  type: project_authority
  status: active
  last_updated: 2026-09-18
---

# Dependencies and capacity

## Purpose

This standard helps the team detect work relationships early enough to avoid
unnecessary waiting, rework and overloaded plans.

It owns the reasoning for:

- dependencies
- blockers
- missing estimates
- known/unknown capacity
- sequencing
- parallel work
- WIP pressure
- synchronization points between people/teams

It does not invent numeric estimates or availability.

## Professional principle

Good planning asks:

```text
What must happen first?
What can safely happen in parallel?
What information is missing?
Who/what is the bottleneck?
What needs synchronization before more work starts?
```

The goal is flow, not simply keeping every person busy.

## Dependency vs blocker

### Dependency

A dependency means one piece of work relies on another condition, artifact,
decision or capability.

A dependency can be healthy and planned.

### Blocker

A blocker is a dependency or condition that currently prevents meaningful
progress on the affected work.

Every blocker is important to surface. Not every dependency is a blocker.

## Dependency types

Classify when evidence allows:

- **technical contract** — API/schema/function/interface must align
- **implementation** — one feature must exist before another can work
- **data** — required data/source is unavailable
- **decision** — work waits for a confirmed choice
- **review/merge** — downstream work needs reviewed/merged code
- **environment/tooling** — build, CI, access or environment prerequisite
- **cross-team** — prerequisite owned by another team
- **external** — vendor/course/customer/external system dependency

Classification helps determine the right response.

## Evidence hierarchy

Strong evidence includes:
- explicit issue links or dependency fields
- issue/PR text
- verified API/contract documentation
- branch/code references
- merge/review state
- confirmed meeting/planning decisions
- current project board relationships

AI may infer a possible dependency from code/branch patterns, but labels it
`🔎 AI-analys` until verified.

## Dependency graph

Represent important chains as:

```text
prerequisite → dependent work → unlocked outcome
```

For each edge, try to answer:

- what depends on what?
- why?
- what evidence proves it?
- what becomes possible when it is resolved?
- who/team owns each side when verified?
- does this currently block progress?

## Early synchronization signal

AI should signal early when parallel work is approaching a shared boundary.

Examples:
- two teams are defining the same data shape differently
- implementation starts before an API contract is stable
- a downstream branch is coding against an assumption not yet confirmed
- several issues need the same unresolved decision
- two branches modify the same integration point in incompatible ways

The first response is usually synchronization/clarification, not blame.

## Missing estimation

An estimate is planning information, not something AI should manufacture.

When meaningful work lacks an estimate:

```yaml
estimation_state: "missing"
signal: "Planning confidence is reduced because this work has no verified estimate."
next_step:
  - "clarify scope/acceptance criteria"
  - "split work if too broad"
  - "ask the owner/team for an estimate"
  - "identify uncertainty that prevents estimation"
```

AI may suggest an **estimation method** or questions to ask.

AI does not present an invented hour/day estimate as project fact.

## Estimation quality

An estimate is easier to trust when:
- scope is clear
- Acceptance Criteria are clear
- important dependencies are known
- technical unknowns are small or explicitly separated
- the person/team doing the work contributed to the estimate

When uncertainty is large, prefer:
- a range provided/confirmed by the team
- a discovery/spike issue
- a checkpoint after more information exists

## Capacity

Capacity means the amount of work a person/team can realistically take on in
the planning period.

### Verified capacity

Numeric capacity may be used when it comes from a registered source such as:
- confirmed sprint planning
- meeting protocol
- documented availability/absence
- team-confirmed estimates and allocation

### Unknown capacity

When numeric capacity is unavailable:

```yaml
capacity_state: "unknown"
meaning: "No verified numeric availability is available."
behavior:
  - "Do not assume normal/full availability."
  - "Do not invent hours, percentages or velocity."
  - "Use qualitative load evidence only."
  - "Ask for/flag missing planning data when it matters."
```

## Qualitative load awareness

Even without numeric capacity, AI can use verified signals such as:
- number of active issues
- active PR/review workload
- branch activity
- known blocker ownership
- known absence/constraint
- multiple critical dependencies centered on one person/team

This supports statements like:

```text
🔎 AI-analys: Backend currently owns several active integration points, so adding
another dependency on Backend may increase bottleneck risk.
```

It does not justify a made-up percentage or hour count.

## Planning order

Prefer work that:

1. removes a blocker
2. unlocks another team or core flow
3. protects an important deadline/milestone
4. reduces a high-consequence risk
5. enables integration/testing
6. delivers useful independent value

This is a reasoning order, not an automatic ranking formula.

## Parallel work

Work is a good parallel candidate when:
- it does not wait for the same prerequisite
- it does not create conflicting assumptions at a shared boundary
- it provides useful sprint/project value
- it does not increase WIP beyond what the team can realistically finish

Parallel does not mean low priority. It means independent enough to proceed.

## WIP awareness

Starting more work has a cost.

AI should signal possible WIP pressure when verified evidence shows:
- many active issues/PRs with little completion
- several branches waiting on the same bottleneck
- repeated context switching
- downstream work starting before prerequisites are stable

A WIP signal is `🔎 AI-analys` unless the team has a documented WIP policy.

## Proposal contract

When AI recommends a change:

```yaml
proposal:
  current_constraint: "[verified dependency/capacity/estimate gap]"
  proposed_action: "[sync/split/wait/parallelize/reassign-discussion/etc.]"
  why: "[evidence]"
  unlocks: "[work/outcome enabled]"
  tradeoff: "[cost or work deferred]"
  provenance: "⭐ AI-förslag"
```

Suggested ownership is a proposal unless explicitly confirmed.

## Cross-team handoff

When work crosses Frontend ↔ Backend ↔ Native/System, identify:
- shared contract/artifact
- producer
- consumer
- readiness condition
- verification method
- synchronization point

This authority defines the dependency/capacity meaning.
A separate cross-layer authority will own deeper code/branch compatibility analysis.

## Relationship to goals

Use `GOALS_AND_SPRINT_PLANNING.md` to decide whether dependency/capacity
information should alter the sprint plan.

A dependency should influence planning when it changes:
- feasible order
- parallelization
- milestone confidence
- required synchronization
- realistic scope

## Relationship to risk

Use `RISK_MANAGEMENT.md` when a dependency/capacity condition creates
uncertainty with meaningful consequence.

A dependency itself is not automatically a risk.

## Relationship to issues

When a dependency needs explicit work:
- link the existing issue if one exists
- propose a missing issue only when verified work is absent
- use the `issue_creation` task bundle
- explain what the issue unlocks

## Learning mode

Teach the user why mature teams:
- make dependencies visible early
- estimate with the people doing the work
- distinguish unknown capacity from free capacity
- limit unnecessary WIP
- synchronize at contracts/interfaces before expensive divergence
- plan around flow rather than equal issue counts per person

---

**Status:** ACTIVE
**Version:** 1.0
**Last updated:** 2026-09-18
