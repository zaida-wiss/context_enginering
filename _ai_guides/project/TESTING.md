---
name: testing_standard
description: Risk-based testing standard for project issues and pull requests
version: 1.1
metadata:
  type: project_authority
  status: active
  last_updated: 2026-09-20
---

# Testing standard

## Why we test

Testing is a way to reduce uncertainty before a change is integrated.

A good test answers a useful question, for example:

- Does the core logic still produce the expected result?
- Can a user complete the intended interaction?
- Do two components or services still agree on their contract?
- Does the system handle a realistic failure or boundary case?
- Did a bug stay fixed after the code changed?

The goal is not to collect tests for their own sake. The goal is confidence that
matches the risk of the change.

## Start with risk

For every issue, ask:

1. What behavior is changing?
2. What could break because of this change?
3. Who or what would be affected?
4. Which test level gives the clearest evidence with reasonable effort?
5. Are there non-functional risks such as accessibility, security, performance,
   data integrity or cross-team contracts?

The issue body should contain a **Testing** section that answers these questions
concretely for that issue.

## Test levels

### Unit test

Use when isolated logic can be verified without a larger system.

Typical examples:
- calculations
- validation
- parsing and transformation
- pure utility functions
- business rules
- boundary conditions

Useful checks normally include:
- expected case
- relevant boundary/edge case
- relevant invalid/failure input

### Component / interaction test

Use for UI behavior where the user interacts with a component or page.

Typical examples:
- rendering the important information
- clicking buttons
- changing inputs
- submitting forms
- validation messages
- loading/success/empty/error states
- keyboard interaction when relevant

Prefer testing what the user can observe rather than internal implementation
details.

### Integration test

Use when correctness depends on two or more parts working together.

Typical examples:
- frontend adapter ↔ API response contract
- controller ↔ service
- service ↔ persistence layer
- Java ↔ Native/JNA boundary
- authentication/filter chain
- serialization/deserialization
- database migrations and queries

### End-to-end / workflow test

Use for a small number of critical flows where several layers must work together.

Typical multi-layer examples:
- authenticate → load portfolio
- read holdings → calculate/display portfolio state
- change target allocation → save → reload
- Java → Native call for a critical calculation path

E2E tests are most valuable for core workflows; they do not need to duplicate
every lower-level test.

## Technology examples — apply only when relevant

The examples below are reusable testing patterns, not declarations about the selected project's stack. Apply a section only when the selected project actually uses that technology or boundary, as verified by its repository/configuration or registered project context.

### Example: frontend — React / TypeScript

For an issue that changes frontend behavior, consider:
- user-visible rendering
- user interaction
- form validation
- state transitions
- loading / success / empty / error states
- API-adapter behavior
- responsive behavior when layout is affected
- keyboard and accessibility behavior when interaction is affected

Pure transformation or calculation logic is often best covered with unit tests.
User interactions are normally better covered with component/interaction tests.

### Example: backend — Java

For backend changes, consider:
- business/service rules
- input validation
- authorization/authentication behavior
- controller request/response contracts
- expected HTTP status and error behavior
- persistence behavior when data access changes
- serialization and integration boundaries

Security-sensitive behavior should include both an allowed case and a relevant
denied/invalid case.

### Example: native/system — C/C++

For native or calculation changes, consider:
- deterministic calculation results
- numeric boundaries
- malformed/invalid input
- data parsing
- memory/resource handling when relevant
- C/C++ exported function signatures
- Java/JNA interoperability when the public boundary changes

For financial/risk calculations, use known input/output examples so regressions
are easy to detect.

### Cross-team contracts

When an issue changes data shared between teams, test the contract explicitly.

Examples:
- request/response shape
- names and types
- null/optional behavior
- error representation
- function signatures
- units/currency/precision assumptions

A contract change should identify which other component must be verified.

## Change-type guidance

### Feature

Test the new acceptance behavior and the important failure/boundary paths.

### Bugfix

Add or update a **regression test** that would fail for the bug and pass after
the fix whenever that is technically reasonable.

Why: a bugfix test converts a discovered failure into permanent project knowledge.

### Refactor

Existing behavior should remain stable.

Use existing tests as a safety net and add tests first when the affected behavior
is important but currently unprotected.

### Documentation-only change

Code tests may be unnecessary. Verify links, commands, examples or documented
behavior that the change affects.

### Build/configuration change

Verify the affected build, lint, test or runtime path rather than adding an
unrelated unit test.

## Non-functional verification

Select these when the issue creates the relevant risk:

- accessibility
- security
- performance
- data integrity
- compatibility
- resilience/error recovery

These are issue-specific quality checks, not automatic boilerplate for every
change.

## Coverage

Coverage numbers can reveal untested areas but are not the definition of quality.

This project uses coverage as evidence, not as a universal pass/fail percentage,
unless the team records a separate explicit decision that sets a threshold.

A smaller set of tests that verifies important behavior can be more valuable than
high coverage of low-risk implementation details.

## What belongs in an issue

Every implementation issue should contain a concrete section similar to:

```markdown
## Testing

**Risk this change introduces**
- [what could break]

**Verify**
- [ ] [specific behavior]
- [ ] [relevant boundary/failure behavior]
- [ ] [integration/contract behavior if applicable]

**Test level**
- Unit / Component / Integration / E2E / Manual quality check

**Why this level**
- [short explanation]
```

Only include tests that fit the issue. The section is generated from the change,
not copied as a generic checklist.

## Pull request verification

Before merge, the PR should make it easy for a reviewer to answer:

- What behavior changed?
- What evidence shows it works?
- What important failure or boundary case was checked?
- Did this change affect a cross-team contract?
- Are any relevant risks still unverified?

## Relationship to other standards

- `TEAM_STANDARDS.md` owns the overall issue-to-Done workflow.
- `DEFINITION_OF_DONE.md` owns the final completion criteria.
- This file owns test selection and test reasoning.
- Risk discoveries are recorded according to the team's risk-analysis process.

## Learning principle

Professional testing is risk-based reasoning.

The important skill is being able to explain:

> What could fail, how would we notice, and what evidence gives us enough
> confidence to integrate this change?

---
**Status:** ACTIVE
**Version:** 1.1
**Last updated:** 2026-09-20
