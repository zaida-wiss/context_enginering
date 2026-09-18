---
name: issue_body_template
description: Reusable issue body aligned with project workflow, testing and Definition of Done
version: 2.1
metadata:
  type: template
  status: active
  last_updated: 2026-09-18
---

# Issue body template

Use this structure when creating a new implementation issue. Keep only sections
that are relevant to the actual change.

```markdown
## Why
[What problem, need or project value does this address?]

## Outcome
[Short description of the intended result.]

## Acceptance Criteria
- [ ] [Observable result 1]
- [ ] [Observable result 2]

## Dependencies / contracts
- [Issue/API/team/branch/decision this depends on, or "None known"]

## Testing

**Risk this change introduces**
- [What could break?]

**Verify**
- [ ] [Specific expected behavior]
- [ ] [Relevant boundary/failure case]
- [ ] [Integration/contract check if applicable]

**Test level**
- [Unit / Component / Integration / E2E / Manual quality check]

**Why this level**
- [Short reasoning based on the change and its risk]

## Decisions
- [Link to docs/decisions/... if a decision is made]
- [Otherwise: No new decision identified]

## Risk analysis
- [Link to risk update if a new/changed risk is found]
- [Otherwise: No new/changed risk identified]

## Applicable Definition of Done
Only include criteria from the canonical Definition of Done that are relevant to
this issue's scope.

- [ ] [Concrete applicable DoD criterion]
- [ ] [Concrete applicable DoD criterion]
- [ ] [README/docs criterion only when the issue actually affects that documentation]
- [ ] [Contract/architecture/risk/decision criterion only when applicable]

## Completion reminder
- [ ] Acceptance Criteria verified
- [ ] Relevant tests/checks complete
- [ ] Relevant decisions documented
- [ ] New/changed risks documented
- [ ] Work branch synchronized with current develop before PR
- [ ] Relevant checks rerun after synchronization
- [ ] PR reviewed and accepted
- [ ] Definition of Done satisfied
- [ ] PR merged
- [ ] Issue moved to Done
```

## Why the issue contains these sections

The issue is a shared working agreement, not only a task title.

- Acceptance Criteria define observable success.
- Testing turns risk into evidence.
- Decision records preserve important reasoning.
- Risk updates connect implementation work to project risk management.
- Applicable Definition of Done turns the canonical DoD into a short,
  issue-specific completion checklist instead of copying irrelevant criteria.
- The completion reminder reduces forgotten process steps.

The canonical requirements remain in the owning standards; this template is a
short operational reminder.

---

**Status:** ACTIVE
**Version:** 2.1
**Last updated:** 2026-09-18


## AI selection rule

When generating an issue body, select the applicable DoD criteria from
`../DEFINITION_OF_DONE.md` after examining the issue scope.

Examples:
- a CSS spacing fix may need visual/responsive verification but no README update
- an API contract change normally needs contract verification/documentation
- a setup/configuration change normally needs the relevant README/setup
  instructions updated

These examples demonstrate selection logic only; they are not project facts.
