---
name: project_work_analysis
description: Global evidence-driven project analysis for implementation, planning, review and reporting
version: 1.0
metadata:
  type: global_ai_authority
  scope: all_projects
  status: active
---

# Project work analysis

This authority owns reusable reasoning about current project work. Project-specific
facts remain in the selected project's registered context. Presentation rules
consume this analysis; they do not redefine it.

## Evidence reconstruction

Start from the smallest sufficient current evidence set and expand only when it
can materially change the conclusion.

Correlate, when relevant:
- issue and acceptance criteria
- pull requests and reviews
- branches and commits
- changed paths and interfaces
- registered project architecture and constraints
- declared ownership
- targeted history

Do not infer:
- assignee from commit author alone
- ownership from commit count alone
- active implementation from a project-board status alone
- current intent from historical activity alone
- issue linkage from a branch name alone without verification

Distinguish:
- declared ownership
- observed contribution
- integration boundaries
- verified facts
- historical facts
- AI inference
- AI recommendation

## Dependency and collision analysis

Before material implementation or sequencing advice, identify relevant:
- explicit issue dependencies
- code/interface dependencies
- open or recent work touching the same integration surface
- duplicated-work risk
- likely merge or contract collisions
- blockers that prevent downstream work
- technical debt that materially changes the implementation choice

Shared files or nearby activity are signals to inspect, not proof of a collision.

## Sequencing

Recommend ordering from verified dependencies and project constraints rather
than distributing work merely for apparent fairness.

Prefer, when supported by evidence:
1. work that removes a verified blocker or establishes a required contract;
2. independent work that can safely proceed in parallel;
3. dependent work after its prerequisite is sufficiently available;
4. lower-value or dependency-blocked work later when starting it would create
   unnecessary work in progress or rework.

A merge is not universally required before dependent work can begin. Use the
selected project's actual integration rules, interface stability, test strategy
and risk. Mocks, stubs or contract tests may permit safe parallel work within
each team's ownership boundary.

Do not invent fixed WIP limits, mandatory phase counts, per-person issue quotas,
or universal branch/merge rituals. Such constraints require project evidence or
an explicit team decision.

## Ownership-aware recommendations

Resolve implementation responsibility from the selected project's registered
ownership context when available. Supplement it with current repository evidence
and targeted history when necessary.

Historical specialization can inform a recommendation but never becomes
permanent personal ownership automatically.

Cross-team dependencies change coordination and sequencing, not ownership.
Respect the global hard team-ownership boundary in AI_FRAMEWORK.yaml.

## Pre-implementation use

The pre-implementation gate in AI_FRAMEWORK.yaml delegates its project-work
analysis to this authority.

Before starting a new issue, automatically perform the lightweight relevant
checks. Escalate to targeted history or broader project context when that is
material to correctness. If broader analysis is useful but not required, it may
be offered with an explanation of what additional evidence it could add.

## Reuse by outputs

Coding assistance, issue work, review, sprint planning and reporting artifacts
should consume the same project analysis rather than implementing competing
reasoning models.

Presentation-specific authorities may define:
- which findings belong in a meeting;
- slide ordering and meeting-point semantics;
- visual treatment;
- provenance symbols and labels;
- pagination and accessibility.

They must not redefine general dependency, ownership, collision, historical or
sequencing reasoning.

---
status: ACTIVE
