---
name: project_work_analysis
description: Global evidence-driven project analysis for implementation, planning, review and reporting
version: 1.2
metadata:
  type: global_ai_authority
  scope: all_projects
  status: active
---

# Project work analysis

This authority owns reusable reasoning about current project work. Project-specific
facts remain in the selected project's registered context. Presentation rules
consume this analysis; they do not redefine it.

## Mandatory project bird's-eye orientation

Before a material project answer, recommendation or implementation change, build
or refresh a lightweight current project map. This is the baseline context, not
an optional deep audit.

Orient across:
- system architecture and major layers;
- core user/data/execution flows relevant to the product;
- registered team ownership and integration boundaries;
- currently active branches and pull requests across the project;
- current backlog, issues and work that can materially intersect the requested area;
- important dependencies, blockers, risks and technical debt;
- relevant project constraints, tests and delivery/integration flow.

The purpose is to notice what is working well as well as what may require a
change, coordination, sequencing adjustment or challenge to an assumption.

Do not read every file or every historical commit by default. First establish
the current bird's-eye map, then deepen only the areas that can materially
change the answer.

Trivial, low-risk questions may use an already-current project map when no
material project interaction can change the answer.

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

## Issue planning gate

Before proposing new issues, first reconstruct the current planning picture from
the selected project's registered current sources.

Required baseline:
- current backlog and existing open/relevant issues;
- active branches and pull requests;
- architecture, core flows and integration boundaries;
- registered team ownership;
- dependencies, blockers and likely collisions;
- relevant delivery constraints and available project capacity when planning a sprint;
- current technical debt and debt risks touched by the proposed work.

Before suggesting a new issue, check whether the work:
- already exists in the backlog or as an issue;
- is already being implemented or reviewed;
- duplicates or conflicts with active work;
- depends on work that should happen first;
- can safely proceed in parallel;
- is obsolete because the architecture or project state changed;
- should instead be a refinement, split or consolidation of existing work;
- exposes technical debt that needs explicit treatment.

The backlog is evidence, not unquestionable truth. Identify stale, duplicate,
poorly sequenced or architecture-incompatible backlog items when supported by
current project evidence.

### Technical-debt early warning

Detect technical debt as early as planning, then keep evaluating it during
implementation and review.

For each material proposal, classify the relevant debt effect as one of:
- no_known_debt;
- debt_risk;
- creates_debt;
- reduces_debt.

When debt exists or may be introduced, explain the concrete shortcut, fragility
or maintenance cost and its likely consequence. Prefer preventing avoidable debt
before it becomes embedded.

Technical debt is not an automatic stop condition. A deliberate temporary
compromise may be reasonable, but it must be visible, justified and trackable:
record why it is accepted, its consequence, and the condition or timing for
repayment. Do not create cleanup work merely for aesthetic preference.

### Canonical new-issue proposal table

New issue proposals must first be delivered in a decision-friendly comparison
table using these columns, in this order:

| Priority | Issue proposal | Core flow | Dependencies | Risk/collision | Technical debt | Recommended order | Why now? |
| --- | --- | --- | --- | --- | --- | --- | --- |

The table is the proposal layer, not the final GitHub issue body. Do not present
an AI proposal as an already-decided team commitment.

After the user/team selects a proposal for creation, expand it into the
project's applicable issue format, including clear purpose/problem, scope,
measurable acceptance criteria, relevant technical context, dependencies and
readiness information when applicable.

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

## Pedagogical system understanding

Teach the system before the detail.

Prioritize the mental model that is most important for understanding the task,
especially:
1. core flows — how user actions, data or execution move through the system;
2. responsibility boundaries — which component/layer/team owns what;
3. cause and consequence — why something exists and what changes upstream or downstream;
4. dependencies and sequence — prerequisites, safe parallel work and timing;
5. engineering principle — the reusable reason behind the recommended approach.

When relevant, make the explanation sufficient for the user to understand:
- **What** is happening or being changed;
- **Where** it belongs in the system;
- **Why** it exists or is recommended;
- **How** it works or should be implemented;
- **When** it matters, should happen, or becomes safe/useful.

These are comprehension dimensions, not mandatory headings. Do not mechanically
repeat five labels when a shorter explanation teaches the important model more
clearly. Explain the highest-value concepts first and avoid repeating context the
user already understands.

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
