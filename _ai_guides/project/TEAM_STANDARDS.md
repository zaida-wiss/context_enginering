---
name: team_standards
description: Canonical project workflow and team operating standards
version: 2.0
metadata:
  type: project_authority
  status: active
  last_updated: 2026-09-18
---

# Team standards

## Purpose

This file describes **how work moves through the project**.

The goal is not only to complete issues. The goal is to practice a professional
workflow that makes work understandable, reviewable, testable and safe to change.

Detailed rule areas have their own owners:

- testing strategy → `TESTING.md`
- completion criteria → `DEFINITION_OF_DONE.md`
- team communication → `TEAM_TONE_AND_COLLABORATION.yaml`
- people/conflict support → `HR_AND_TEAM_SUPPORT.yaml`
- confirmed decisions → `docs/decisions/`
- current project facts → registered data sources

## Rule status

To avoid turning AI suggestions into invented team rules, this repository uses
three kinds of guidance:

### Project standard

A workflow the context repository currently expects project work to follow.

### External requirement

A requirement backed by a course, customer, platform or other registered source.

### Recommended practice

Industry-aligned guidance that is useful for learning but is not treated as a
confirmed team decision until the team explicitly adopts it.

When a recommendation becomes a team decision, record the decision and update
the owning standard.

---

# 1. Issue-to-Done workflow — project standard

## Step 1 — Understand the issue

Before implementation, make the work understandable.

The issue should make clear:

- what problem or need is being addressed
- what outcome is expected
- Acceptance Criteria
- relevant dependencies or contracts
- a concrete Testing section based on `TESTING.md`
- known risks or uncertainties when they are already visible

### Why

Clear issues reduce hidden assumptions and make review easier because everyone
can compare the implementation with the same intended result.

## Step 2 — Implement on the work branch

Work in small, understandable changes connected to the issue.

Commits should help another developer understand the history of the change.

### Why

Small coherent changes are easier to review, debug and revert than one large
unstructured change.

## Step 3 — Capture decisions

When the work creates or confirms a meaningful technical/process decision,
record it in `docs/decisions/`.

The issue or PR should link the relevant decision.

Examples:
- choosing one API contract over another
- changing architecture or data flow
- adopting a testing/tooling strategy
- changing an established project workflow

If the issue required no decision, it can be marked as not applicable.

### Why

A decision without its reasoning is easily rediscovered and debated later.
Decision records preserve the **why**, not only the final code.

## Step 4 — Update risk analysis when the issue reveals a risk

When implementation, testing or review identifies a new risk or materially
changes an existing risk, record that information in the project's canonical
risk source.

The issue/PR should state what was found and where it was recorded.

If no relevant new or changed risk was found, mark that explicitly rather than
inventing one.

### Why

Risk analysis is most useful when it grows from real engineering work rather
than being updated only before a meeting or deadline.

## Step 5 — Sync with develop before opening the PR

Bring the current `develop` branch into the work branch before the pull request
is considered ready for review.

Resolve integration conflicts in the work branch and rerun the tests/checks
affected by the integration.

### Why

A branch can work perfectly while isolated and still conflict with newer team
work. Synchronizing before review lets the reviewer examine something closer to
what will actually be integrated.

## Step 6 — Verify the change

Run the issue-specific checks defined by `TESTING.md`.

Verification should answer:
- does the intended behavior work?
- did an important existing behavior break?
- are relevant boundary/failure cases handled?
- do affected team/system contracts still match?

### Why

"Code is written" and "change is verified" are different states.

## Step 7 — Open the pull request

The PR should make review efficient by explaining:

- what changed
- why it changed
- linked issue
- how it was tested
- relevant decisions
- new/changed risks
- known limitations or follow-up work

## Step 8 — Review collaboratively

Review the change against:
- issue intent and Acceptance Criteria
- relevant tests/evidence
- project standards
- affected contracts
- clarity and maintainability

Feedback follows `TEAM_TONE_AND_COLLABORATION.yaml`.

### Why

Code review is both a quality check and knowledge-sharing mechanism.

## Step 9 — Apply Definition of Done

Use `DEFINITION_OF_DONE.md` as the final completion gate.

Any remaining work that matters should be visible as a follow-up issue rather
than hidden in conversation or memory.

## Step 10 — Merge and move the issue to Done

Once the accepted PR is merged and the Definition of Done is satisfied:

- confirm the issue reflects the final outcome
- link the merged PR
- move/close the issue as Done according to the project board workflow

### Why

The issue tracker should describe reality. "Done" should mean the team can rely
on the work as integrated, verified project state.

---

# 2. Issue body standard — project standard

New implementation issues should contain these sections when applicable:

```markdown
## Why
[What problem/value does this address?]

## Acceptance Criteria
- [ ] Observable outcome 1
- [ ] Observable outcome 2

## Dependencies / contracts
[Relevant issue, API, branch, team or "None known"]

## Testing
**Risk this change introduces**
- [What could break?]

**Verify**
- [ ] [Specific check]
- [ ] [Boundary/failure/contract check if relevant]

**Test level**
- [Unit / Component / Integration / E2E / Manual quality check]

## Decisions
- [Decision record link, or "No new decision identified"]

## Risk analysis
- [Risk record/update link, or "No new/changed risk identified"]

## Completion reminder
- [ ] Acceptance Criteria verified
- [ ] Relevant tests/checks complete
- [ ] Relevant decisions documented
- [ ] New/changed risks documented
- [ ] Branch synchronized with current develop before PR
- [ ] PR reviewed and accepted
- [ ] Definition of Done satisfied
- [ ] PR merged
- [ ] Issue moved to Done
```

The body adapts to the issue. A documentation issue does not need fake runtime
tests; a cross-team integration issue should contain explicit contract checks.

---

# 3. Git history — recommended practice unless separately decided

A readable commit convention is useful because Git history becomes searchable
project documentation.

A common convention is:

```text
type(scope): short imperative description (#issue)
```

Examples:

```text
feat(frontend): add allocation validation (#88)
fix(backend): reject unauthorized holding access (#97)
test(native): add boundary cases for risk calculation (#73)
docs(api): clarify portfolio response contract (#120)
```

Common types include `feat`, `fix`, `test`, `refactor`, `docs`, `build`
and `chore`.

This format is educational guidance until an explicit team decision records the
exact required commit convention.

---

# 4. Branch naming — recommended practice unless separately decided

Useful branch names connect work to intent, for example:

```text
feature/88-critical-interactions
fix/97-holdings-authorization
docs/120-api-contract
```

The important professional principle is traceability: another developer should
be able to connect branch → issue → PR → decision/test evidence.

The exact syntax is a team convention and can change through a documented
decision.

---

# 5. Code standards — authority principle

Technology-specific style should preferably come from:
1. formatter/linter/compiler configuration in the actual project repository
2. documented team decisions
3. framework/language conventions as recommended practice

This file does not invent mandatory TypeScript, Java or C++ style rules when no
team decision or project configuration establishes them.

### Why

Tool-enforced standards are more reliable than prose, and separating mandatory
rules from recommendations prevents an AI-generated suggestion from becoming an
accidental team policy.

---

# 6. Working with AI

AI should use these standards to **teach the reasoning behind the workflow**, not
only produce checklists.

When helping create an issue, PR description, review or implementation plan:

1. resolve the relevant project standards through `CONTEXT_REGISTRY.yaml`
2. use current project facts from registered sources
3. explain why the suggested process helps
4. distinguish project standards from recommended practices
5. avoid presenting an unrecorded recommendation as a team decision

---

**Status:** ACTIVE
**Version:** 2.0
**Last updated:** 2026-09-18
