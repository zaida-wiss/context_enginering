---
name: definition_of_done
description: Final completion criteria for project issues
version: 2.0
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
- communication/review tone → `TEAM_TONE_AND_COLLABORATION.yaml`

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

- [ ] Any new risk or material change to an existing risk discovered during the issue is recorded in the canonical risk source.
- [ ] The issue or PR links the risk update when one was made.
- [ ] If no new or changed risk was found, that is stated explicitly.

## Documentation

Relevant documentation is current when the issue changes something another
person needs to understand, for example:
- setup or configuration
- API/contract behavior
- architecture or decision rationale
- user-facing workflow
- known constraints

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
**Version:** 2.0
**Last updated:** 2026-09-18
