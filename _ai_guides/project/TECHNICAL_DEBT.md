---
name: technical_debt
description: Canonical project standard for recognizing, explaining and handling technical debt
version: 1.0
metadata:
  type: project_authority
  status: active
  last_updated: 2026-09-18
---

# Technical debt

## Purpose

Technical debt describes a current design or implementation compromise that
creates a likely future cost when the system changes, scales, integrates or is
maintained.

This standard helps AI recognize debt early without treating every imperfection,
unfinished feature or experimental branch as debt.

## Technical debt is not

### Normal unfinished work

A feature that is still being implemented according to plan is not automatically
technical debt.

### A bug

A bug is incorrect behavior. It may be caused by debt or create more debt, but
the concepts are different.

### A blocker

A blocker prevents progress now. Debt usually represents future cost, although
severe debt can become a blocker.

### A risk

A risk is uncertainty about a future event/condition. Debt is a current
technical condition.

Debt can create risk.

## Useful model

```text
current compromise
  ↓
future change/integration/maintenance
  ↓
extra cost, fragility or rework
```

The important question is not "Is this code imperfect?"

The important question is:

> Does this current compromise make future work meaningfully harder, riskier or
> more expensive?

## Debt states

### 1. Normal temporary state

The implementation is incomplete but has a clear near-term completion path.

No debt label is needed.

### 2. Intentional short-term compromise

The team knowingly chooses a simpler or temporary solution to deliver value.

Record:
- what was deferred
- why
- what would trigger revisiting it

This may be reasonable engineering.

### 3. 🔎 AI-analys — möjlig teknisk skuld

AI sees evidence that a current compromise may create future cost, but the team
has not yet confirmed the debt.

Explain:
- evidence
- likely future cost
- affected goal/integration point
- what should be verified

### 4. Confirmed technical debt

The team/project explicitly recognizes the compromise and its consequence.

Track it in the appropriate project work/decision system.

### 5. Debt requiring near-term action

Debt materially threatens:
- integration
- core-flow correctness
- security
- maintainability of active work
- a milestone
- ability of another team to proceed

This can justify priority action.

## Common debt patterns

AI may look for patterns such as:

- duplicated domain/data models drifting apart
- hardcoded data/assumptions spreading through production paths
- undocumented API behavior becoming relied upon
- temporary adapters becoming permanent by accident
- long-lived branches that continuously diverge
- repeated fixes around the same unstable boundary
- missing tests around frequently changed high-risk logic
- duplicated business rules across layers
- manual steps repeatedly compensating for missing automation
- known structural workaround that makes each new change more expensive
- dependency/version constraints repeatedly blocking changes

A pattern is evidence to investigate, not automatic proof.

## Active-branch early detection

When tools/access allow, AI may inspect relevant active branches to detect debt
before merge.

Useful early signals:
- two branches duplicate the same logic differently
- a temporary mock becomes a dependency for more features
- each team adds its own version of a shared model
- repeated merge/conflict resolution around one unstable design
- an undocumented contract accumulates multiple consumers
- workaround code is spreading to additional components/services

Use `CROSS_LAYER_AWARENESS.yaml` for branch/contract evidence.

## Debt record / proposal structure

When proposing that debt should be tracked:

```yaml
technical_debt:
  current_compromise: "[what exists today]"
  why_it_exists: "[known decision/constraint, or unknown]"
  future_cost: "[what becomes harder/riskier]"
  evidence:
    - "[source/code/branch/issue]"
  affected_goal_or_system: "[verified relationship]"
  urgency: "[qualitative, evidence-based]"
  trigger_to_address: "[event/milestone/change that makes action worthwhile]"
  suggested_action: "[refactor/contract/test/decision/etc.]"
  provenance: "⭐ AI-förslag"
```

Do not invent a past team decision to explain why the debt exists.

## Prioritizing debt

Debt should not automatically outrank feature delivery.

Consider:

1. **interest rate** — how quickly does the cost grow as more work builds on it?
2. **frequency** — how often does the team touch this area?
3. **blast radius** — how many layers/teams/features depend on it?
4. **milestone timing** — will upcoming work make it much harder to fix later?
5. **risk** — does it increase security/correctness/integration uncertainty?
6. **cost to address now** vs later
7. **value unlocked** by removing it

## High-interest debt

AI should signal strongly when the team is about to multiply the cost.

Example structure:

```text
🔎 AI-analys — teknisk skuld med växande kostnad

Nu:
[verified compromise]

Om fler delar byggs ovanpå:
[future rework/coupling]

⭐ AI-förslag:
[smallest useful action now]

Varför nu:
[why waiting is more expensive]
```

## Stop-and-sync signal

Sometimes the best professional advice is to pause dependent implementation
briefly and clarify the design/contract.

That is appropriate when:
- several teams are about to build on incompatible assumptions
- the minimum shared contract is cheaper to agree now than to reconcile later
- continued work would knowingly multiply rework

This is a proposal, not an automatic command.

Use:
- `CROSS_LAYER_AWARENESS.yaml` for the mismatch/contract evidence
- `DEPENDENCIES_AND_CAPACITY.md` for sequencing impact
- `RISK_MANAGEMENT.md` if uncertainty/consequence becomes a candidate risk

## Debt vs deliberate trade-off

Good engineering sometimes accepts debt consciously.

A mature trade-off states:

```text
We choose [temporary compromise]
because [current value/constraint].
We accept [future cost].
We will revisit when [trigger].
```

If the reasoning materially affects architecture/process, record it in
`docs/decisions/`.

Unrecorded compromise is more likely to become accidental debt.

## Debt and testing

Missing tests are not always debt.

Test debt becomes meaningful when:
- important frequently changed behavior has no useful safety net
- lack of tests repeatedly slows/refuses refactoring
- integration confidence depends on manual checking every time
- known high-risk logic cannot be changed safely

Use `TESTING.md` to decide what evidence is appropriate.

## Debt and sprint planning

Use `GOALS_AND_SPRINT_PLANNING.md`.

A debt item belongs in near-term planning when addressing it materially:
- protects the sprint goal
- unlocks dependent work
- reduces high-interest future cost
- enables a milestone/integration
- mitigates a significant risk

Otherwise it may remain visible backlog rather than immediate work.

## Learning mode

Teach users that good teams do not aim for zero debt.

They aim to:
- make important debt visible
- understand why it exists
- avoid accidental compounding
- know when interest becomes expensive
- repay debt when the value exceeds the opportunity cost

---

**Status:** ACTIVE
**Version:** 1.0
**Last updated:** 2026-09-18
