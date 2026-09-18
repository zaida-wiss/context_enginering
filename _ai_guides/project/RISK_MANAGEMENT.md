---
name: risk_management
description: Canonical project risk-management reasoning standard aligned with the team's risk workbook and CTO assignment
version: 1.0
metadata:
  type: project_authority
  status: active
  canonical_register: "GOOGLE_RISK_REGISTER"
  last_updated: 2026-09-18
---

# Risk management

## Purpose

This standard teaches how to identify, assess, respond to and monitor project
risks using the team's existing risk workbook.

The context repository owns the **method and reasoning**.

The registered `GOOGLE_RISK_REGISTER` owns the **current risk records**.

This keeps one risk register while still giving AI enough structure to help the
team work like a mature engineering organization.

## The project's actual method

The registered workbook defines a five-step flow:

```text
1. Identify
2. Assess
3. Prioritise
4. Mitigate
5. Monitor
```

It also starts with an asset/system inventory because a team can reason more
clearly about risk when it knows what system, data, contract or capability may
be affected.

## Risk vs problem vs blocker

### Risk

A risk is an uncertain event or condition that **may happen** and would affect
an objective if it occurs.

Useful form:

```text
Because [cause/vulnerability],
there is a possibility that [event],
which could lead to [consequence/impact].
```

### Problem / issue

A problem has already happened or is already true.

It may create new risks, but it should not be disguised as future uncertainty.

### Blocker

A blocker is a current condition preventing or materially delaying work.

A blocker may be caused by a realised risk, but not every blocker belongs in
the risk register.

### Technical debt

Technical debt is a design/implementation compromise whose future cost may
increase.

Debt can create risk, but debt and risk are not the same concept.

### Why the distinction matters

If every inconvenience becomes a risk, the register stops helping the team
prioritise.

Risk management should focus attention on uncertain events with meaningful
consequences.

## Canonical risk fields

The current workbook uses these fields:

```yaml
risk:
  id:
  asset_or_system:
  category:
  what_could_go_wrong:
  cause_or_vulnerability:
  consequence_or_impact:
  likelihood_1_to_5:
  impact_1_to_5:
  risk_score:
  risk_level:
  response:
  mitigation_or_control:
  owner:
  likelihood_after_fix:
  impact_after_fix:
  residual_score:
  residual_level:
  status:
```

The workbook calculates the score/level fields. AI should reason about the
inputs and should not replace spreadsheet formulas with invented values.

## Asset first

Before adding a risk, identify the affected asset/system when possible.

Examples of asset types can include:
- application/service
- database/data store
- API or contract
- external dependency
- authentication mechanism
- CI/CD or infrastructure
- user-facing capability
- important documentation/knowledge

Use the actual ASSETS worksheet for current project assets.

If the correct asset is missing, AI may propose adding one, clearly marked as
`⭐ AI-förslag`.

## 1. Identify

A useful risk statement separates:

- what could go wrong
- why it could happen
- what the consequence would be

Weak:
```text
API contract risk
```

Stronger form:
```text
What could go wrong: Frontend and Backend implement incompatible portfolio fields.
Cause: The shared API contract is not agreed before parallel implementation.
Consequence: Integration requires rework and can delay the core flow.
```

This example demonstrates structure only. Current project risk content must come
from verified project evidence.

## AI candidate-risk rule

AI may identify a **candidate risk** from:
- an issue
- active branch work
- code or contract divergence
- dependency analysis
- test results
- external feedback
- planning uncertainty

Until the team/register confirms it, present it as:

```text
🔎 AI-analys — möjlig risk
```

and provide the evidence.

If proposing a new register entry, use:

```yaml
candidate_risk:
  asset_or_system: "[verified/proposed]"
  what_could_go_wrong: "[future uncertain event]"
  cause_or_vulnerability: "[evidence-based cause]"
  consequence_or_impact: "[project consequence]"
  suggested_category: "[only if supported]"
  evidence:
    - "[source]"
  next_step: "Team verifies/scorers/registers"
  provenance: "⭐ AI-förslag"
```

AI does not silently turn its own analysis into a confirmed risk record.

## 2. Assess

The workbook uses:

```text
Risk score = Likelihood × Impact
```

with 1–5 scales.

### Likelihood

Use the workbook's defined scale:

- 1 Rare
- 2 Unlikely
- 3 Possible
- 4 Likely
- 5 Almost certain

The score represents probability/frequency judgement, not emotional concern.

### Impact

Use the workbook's defined scale:

- 1 Negligible
- 2 Minor
- 3 Moderate
- 4 Major
- 5 Severe

Impact should be considered against the project objective affected, for example:
- delivery
- security/privacy
- correctness
- customer/user value
- integration
- compliance
- recoverability

### Evidence before numbers

A numerical score should have a reason.

AI should explain what evidence supports a suggested likelihood/impact score.

When evidence is insufficient:
- describe the uncertainty
- propose what to verify
- avoid manufacturing confidence through a number

## 3. Prioritise

The workbook defines:

- 16–25 Critical
- 10–15 High
- 5–9 Medium
- 1–4 Low

Use the workbook's score to guide attention, while also considering:
- imminent milestone/deadline
- dependencies
- whether the risk affects the core flow
- whether mitigation must happen before more work continues
- cost of delaying mitigation

A high numerical score is useful evidence, but planning still requires
engineering judgement.

## 4. Respond / mitigate

The workbook uses the four T's:

### Treat

Reduce likelihood and/or impact with a concrete control.

### Tolerate

Consciously accept the risk.

Tolerate is a decision, not the same as forgetting the risk.

### Transfer

Shift responsibility/exposure through an external party, agreement or service
when that is actually possible.

### Terminate

Stop or avoid the risky activity.

## A good mitigation

A mitigation should answer:

- What exactly changes?
- Who owns it?
- How will we know it was implemented?
- How will we know it reduced the risk?
- Is the mitigation effort proportionate to the risk?

Prefer concrete controls over vague statements.

Weak:
```text
Be careful with authentication.
```

Stronger structure:
```text
Implement [specific control], verify through [specific evidence/test],
owned by [role/person].
```

## 5. Monitor and residual risk

After a mitigation is implemented, re-assess:

- likelihood after fix
- impact after fix

The workbook calculates:
- residual score
- residual level

Residual risk is the risk that remains **after** the control.

This is valuable because mitigation usually reduces risk rather than making it
disappear completely.

## Risk lifecycle during issue work

When working on an issue:

```text
understand issue
  ↓
identify meaningful uncertainty
  ↓
is it a real candidate risk?
  ├─ no → continue normal engineering workflow
  └─ yes
       ↓
  check existing risk register for duplicate/related risk
       ↓
  update existing risk OR propose new risk
       ↓
  define/adjust mitigation when appropriate
       ↓
  connect mitigation to issue/test/decision
       ↓
  re-assess residual risk after evidence exists
```

The issue should link the risk update when risk work is relevant.

## Relationship to testing

Testing can be:
- evidence that a mitigation works
- a control itself
- evidence that likelihood is lower than previously believed
- evidence revealing a new candidate risk

Use `TESTING.md` to choose the right test level.

## Relationship to goals and planning

Risk changes planning when it materially affects:
- sequence
- scope
- WIP
- dependencies
- confidence in a milestone
- what should be verified before continuing

Use `GOALS_AND_SPRINT_PLANNING.md` to show whether the current plan should
remain, be clarified or receive a transparent `⭐ AI-förslag`.

## Relationship to decisions

If a risk causes the team to change architecture, scope, technology, contract or
workflow, capture the meaningful decision in `docs/decisions/`.

This creates traceability:

```text
risk → trade-off → decision → implementation → verification → residual risk
```

## CTO Feed Forward connection

The CTO assignment explicitly asks the team to demonstrate how risk analysis
changed real project decisions.

Strong CTO evidence therefore follows this chain:

```text
identified risk
  ↓
risk assessment
  ↓
trade-off / mitigation decision
  ↓
actual technical or planning change
  ↓
evidence that the control is realistic/verifiable
  ↓
remaining uncertainty / residual risk
```

For CTO preparation, prefer a few well-supported examples that demonstrate
decision impact over a long list of risks.

The source-backed course requirements include:

- trade-offs caused by identified risks
- realistic/verifiable mitigations
- impact on technical solution/architecture/approach
- remaining uncertainties that need investigation/testing
- later prioritisation of CTO feedback based on impact and feasibility

## Professional learning questions

When helping the team learn, ask questions such as:

- What objective does this risk threaten?
- What evidence makes this more than a vague concern?
- Is the cause different from the consequence?
- Is this risk already represented elsewhere?
- What is the cheapest useful mitigation?
- What evidence would show the mitigation works?
- What risk remains afterwards?
- Does this risk justify changing the current sprint plan?
- Did this risk cause a decision worth documenting?

## Presentation integration

Presentations use the canonical risk register for current risk facts.

Use:
- verified register facts as source-backed content
- `🔎 AI-analys` for interpretation of consequence/planning impact
- `⭐ AI-förslag` for a proposed mitigation, priority change or new candidate risk

A presentation should show risk as a decision input, not as an isolated list.

---

**Status:** ACTIVE
**Version:** 1.0
**Last updated:** 2026-09-18
