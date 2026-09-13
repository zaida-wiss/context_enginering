---
name: dod_template_concrete
description: Concrete DoD checklist template for new issues — use this when creating GitHub issues
metadata:
  type: template
  critical: true
  usage: Copy this checklist into new GitHub issues
---

# ✅ DEFINITION OF DONE — ISSUE TEMPLATE CHECKLIST

**🚨 VIKTIGT:** Kopiera denna checklist direkt in i din GitHub-issue när du skapar den.  
**Denna checklist MÅSTE fyllas i för att en issue ska kunna markeras DONE.**

---

## Issue-Title Format

```
[Category] Brief description

Examples:
[Feature] User authentication flow
[Bugfix] FX calculation edge case  
[Refactor] Extract API client to shared module
[Test] Unit tests for Risk engine
[Docs] API contract documentation
```

---

## 📋 DEFINITION OF DONE CHECKLIST

**Denna checklist måste FYLLA ✅ för att issue är KLAR.**

### AC — Acceptance Criteria Verified

```
- [ ] All acceptance criteria from issue description are met
- [ ] Code behavior matches specified AC
- [ ] No workarounds or partial implementations
```

**Example:**  
Issue says: "Login must work with Google and GitHub"  
✅ DONE = Both tested, no "login works except GitHub"

### 🧪 Tests Passing

```
- [ ] Unit tests written (minimum 70% coverage for this module)
- [ ] All tests passing locally
- [ ] Integration tests added if touching API contracts
- [ ] No test skips or pending tests (except documented exceptions)
```

**Example:**  
Writing auth API → tests must cover:
- Successful login flow
- Invalid credentials
- Session expiry
- Cross-team contract (Frontend ↔ Backend)

### 👀 Code Review Complete

```
- [ ] Pull request created with descriptive title
- [ ] PR reviewed by at least one team member
- [ ] All comments resolved
- [ ] Reviewer approved and PR merged to `develop`
```

**Example:**  
- PR title: `feature: add risk calculation cache — 40% perf improvement`
- Reviewer: Must be DIFFERENT team or specialization
- Comments: All ✅ resolved before merge

### 📖 Documentation Updated

```
- [ ] Code comments added for non-obvious logic
- [ ] API contracts updated (if changes API)
- [ ] README updated (if new setup/config needed)
- [ ] Architecture decision documented if architectural change
```

**Example checklist per type:**

**Backend feature:**
- ✅ API endpoint documented (what params? what response?)
- ✅ Database schema change documented
- ✅ Error codes documented

**Frontend component:**
- ✅ Component props documented
- ✅ Usage examples in Storybook or docs
- ✅ Accessibility requirements tested

**Native/System:**
- ✅ API changes documented
- ✅ Performance impact documented
- ✅ JNA/C++ interface documented

---

## ⚠️ COMMON MISTAKES (Things That Block DoD)

### ❌ "Tests pass locally but not CI"
→ DoD NOT met — must pass CI pipeline

### ❌ "I did the feature, code review can wait"
→ DoD NOT met — review is BEFORE merge

### ❌ "It's obvious from the code"
→ DoD NOT met — must have at least basic docs

### ❌ "I wrote tests, but skipped one weird edge case"
→ DoD NOT met — document the skip, or test it

### ❌ "My teammate said it looks good in Slack"
→ DoD NOT met — must be GitHub PR review

---

## 📊 HOW TO MARK DONE IN GITHUB

**When ALL checkboxes below are ✅:**

1. Comment on issue: `This is complete per DoD checklist — merge of PR #XYZ`
2. Link the merged PR
3. Move to DONE column on Project Board (or close issue if using auto-close)

**Example:**
```
This is complete per DoD checklist.

Merged: PR #87 (Auth integration)
Tests: ✅ 24 new tests, 85% coverage
Review: ✅ Approved by @rashaknifdi
Docs: ✅ API contract updated, README notes added
```

---

## 🎯 PER-TEAM SPECIFICS

### Frontend (Tomac, Björn, Zaida)

**Extra DoD items:**
- [ ] Responsive design tested (mobile 375px, tablet 768px, desktop 1920px)
- [ ] Accessibility check: WCAG AA (keyboard nav, screen readers)
- [ ] Cross-browser tested (Chrome, Safari, Firefox)
- [ ] No console errors or warnings

### Backend (Erik, Rasha)

**Extra DoD items:**
- [ ] Database migrations tested (schema + data)
- [ ] API contract matches Frontend expectations
- [ ] Error responses consistent format + status codes
- [ ] Performance impact assessed (query time, response size)

### Native/System (Pär, Henrik)

**Extra DoD items:**
- [ ] Performance impact documented (CPU, memory, battery)
- [ ] C++ code follows style guide
- [ ] JNA bindings tested
- [ ] Backwards compatibility maintained (or migration path documented)

---

## 📝 COPY-PASTE TEMPLATE FOR NEW ISSUES

Use this when creating GitHub issues:

```markdown
## Acceptance Criteria
- [ ] AC 1 description
- [ ] AC 2 description

## Definition of Done
- [ ] All AC met
- [ ] Tests passing (70%+ coverage)
- [ ] Code review approved (PR #___)
- [ ] Documentation updated

## Team-Specific
- [ ] [Add team-specific DoD items above]

## Completed By
- PR: #___
- Merged: [date]
- Closed: [date]
```

---

**Version:** 1.0  
**Created:** 2026-09-13  
**Apply from:** Immediately — use for all new issues

