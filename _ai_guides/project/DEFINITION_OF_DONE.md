---
name: definition_of_done
description: Final completion criteria for project issues
version: 2.2
metadata:
  type: project_authority
  status: active
  last_updated: 2026-09-18
---

# Definition of Done

## Purpose

Definition of Done answers one question:

> What must be true before the team can rely on this issue as completed work?

It is a **completion gate**, not the place where testing strategy, Git conventions
or detailed implementation rules are defined.

Those details are owned by:
- workflow → `TEAM_STANDARDS.md`
- testing → `TESTING.md`
- risk reasoning → `RISK_MANAGEMENT.md`
- communication/review tone → `TEAM_TONE_AND_COLLABORATION.yaml`

## Issue-specific application

The full Definition of Done is the canonical set of completion concerns.

When an issue is created, the AI selects the criteria that actually apply to
that issue's scope and renders those as the issue's **Applicable Definition of
Done**.

Selection rules:
- include criteria that are materially affected by the change
- make every selected criterion concrete and verifiable
- explain briefly why the selected criterion applies when the connection is not obvious
- omit non-applicable criteria rather than copying the full DoD mechanically
- never invent a new project rule merely to make the checklist look complete

Core completion concerns such as verified Acceptance Criteria, appropriate
verification, accepted review/integration and truthful final issue state remain
relevant to implementation work. Other areas such as README, architecture,
contracts, risk updates or decision records are included when the issue affects
them.

## Acceptance Criteria

- [ ] The issue's Acceptance Criteria are satisfied and verified.
- [ ] The final behavior matches the intended outcome described by the issue.

## Verification

- [ ] The issue-specific tests/checks selected according to `TESTING.md` have been completed.
- [ ] Relevant checks pass after the work branch has been synchronized with current `develop`.
- [ ] Important known limitations are visible rather than hidden.

A task uses the test levels that fit its risk. Done does not automatically mean
that every issue needs unit, integration and E2E tests.

## Decisions

- [ ] Any meaningful technical/process decision created by the work is recorded in `docs/decisions/`.
- [ ] The issue or PR links the relevant decision record.
- [ ] If no new decision was needed, that is stated explicitly.

## Risk analysis

- [ ] Any new risk or material change to an existing risk discovered during the issue is handled according to `RISK_MANAGEMENT.md` and recorded in the canonical risk source when confirmed.
- [ ] The issue or PR links the risk update when one was made.
- [ ] If no new or changed risk was found, that is stated explicitly.

## Documentation

Relevant documentation is current when the issue changes something another
person needs to understand.

Select the applicable documentation criterion for the issue, for example:

- **README** — when the change affects setup, installation, commands, usage,
  configuration, project structure or another behavior the README is expected
  to explain
- **API/contract documentation** — when request/response shape, fields, types,
  errors, units, compatibility or an integration boundary changes
- **architecture/decision documentation** — when the issue changes an important
  technical direction or records reasoning future developers need
- **user/developer workflow documentation** — when the way a person uses,
  tests, runs or maintains the system changes
- **known constraints/limitations** — when the issue introduces or changes a
  limitation another person needs to understand

If none of these areas is affected, the issue-specific DoD should not contain a
documentation checkbox merely as boilerplate.

The documentation requirement is proportional to the change.

## Review and integration

- [ ] The pull request explains what changed, why, and how it was verified.
- [ ] Review feedback required for acceptance has been addressed.
- [ ] The accepted pull request is merged into the intended integration branch.
- [ ] Any important follow-up work is represented by a visible issue rather than an informal promise.

## Issue state

- [ ] The issue links the merged pull request or final evidence.
- [ ] The final issue state reflects what was actually delivered.
- [ ] The issue is moved/closed as Done only after the completion criteria above are satisfied.

## Why this matters

A reliable Definition of Done keeps three states separate:

```text
implemented
    ↓
verified + reviewed + integrated
    ↓
Done
```

This makes the project board more trustworthy and reduces the amount of hidden
work that appears later as surprises.

## What this file intentionally does not own

- a fixed coverage percentage
- a requirement to run every test level for every issue
- branch naming syntax
- commit-message syntax
- Definition of Ready
- detailed coding style

If the team wants any of those to become binding project rules, record the
decision and update the authority that owns that rule.

---

**Status:** ACTIVE
**Version:** 2.2
**Last updated:** 2026-09-18
