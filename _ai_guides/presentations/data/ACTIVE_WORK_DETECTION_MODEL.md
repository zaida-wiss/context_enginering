---
name: active_work_detection_model
description: Evidence hierarchy for detecting active work — without relying solely on Project Board
metadata:
  type: specification
  critical: true
  version: 1.0
---

# 🔍 ACTIVE WORK DETECTION MODEL

**This file defines HOW to determine "what is someone actually working on?" using evidence from GitHub.**

**Problem:** Project Board is often stale or inaccessible. Commits + branches + issues + PRs together tell a more accurate story.

**Solution:** Use a **proof hierarchy** — combine multiple signals to determine active work status.

---

## 📊 EVIDENCE HIERARCHY (Strongest → Weakest)

### LEVEL 1 — Strongest Evidence: PR + Issue + Assignee

```
Open PR #68
├── linked to issue #67
├── author: Zaida
├── assignee: Zaida
├── requested_reviewers: [Björn]
├── branch: docs/#67-update-readme
└── recent commits: ✓

CONCLUSION: ✅ DEFINITE active work
STATUS: "Väntar på review" (blocker: waiting for Björn)
```

**Use case:** Show on slide ①B "Väntar i PR"

---

### LEVEL 2 — Very Strong Evidence: Issue + Matching Branch + Recent Commits

```
Open issue #67
├── title: "Update README"
├── assignee: Zaida
├── branch: docs/#67-update-readme (exists)
├── recent commits on branch:
│   - Zaida 15 sep
│   - Zaida 16 sep
└── no open PR yet

CONCLUSION: ✅ VERY LIKELY active work
STATUS: "Pågår — arbete slutförs, PR nästa" (still coding)
```

**Use case:** Show on slide ①C "Pågår utan PR"

---

### LEVEL 3 — Strong Evidence: Issue + Matching Branch (No Recent Commits)

```
Open issue #45
├── title: "Add API endpoint"
├── assignee: Erik
├── branch: backend/#45-endpoint (exists)
└── last commit: 5 sep (older than REPORTING_PERIOD)

CONCLUSION: ⚠️ POSSIBLY active work (or paused)
STATUS: "Pågår — branch aktiv, senaste commit utanför vecka"
        (could be paused, or commits on develop instead)
```

**Use case:** Include but flag as uncertain

---

### LEVEL 4 — Moderate Evidence: Open Assigned Issue Alone

```
Open issue #89
├── title: "Refactor database layer"
├── assignee: Rasha
└── no matching branch found
└── no recent commits found

CONCLUSION: 🤔 POSSIBLY assigned, maybe not started
STATUS: "Tilldelad — arbete tidigi eller ännu påbörjad?"
        (needs clarification in meeting)
```

**Use case:** Include to track who has capacity, but lower priority

---

### LEVEL 5 — Weak Evidence: Recent Commits Without Issue Link

```
Commit 16 sep · Erik · "Fix JWT refresh token issue"
├── no PR found
├── no issue reference in message
└── branch: backend/jwt-fix (inferred from message, not verified)

CONCLUSION: ❓ UNCONFIRMED work
STATUS: "Arbete detekterat — behöver länkas till issue"
        (orphaned commit, needs context)
```

**Use case:** Suggest linking to issue, don't show on slide without verification

---

### LEVEL 6 — Weakest Evidence: Project Board Status Alone

```
Project Board status: "In Progress"
├── but no corresponding issue found
├── no PR
├── no commits
└── Board last updated: 30 aug (2 weeks ago)

CONCLUSION: ❌ UNRELIABLE
STATUS: "Boarden är troligtvis inte uppdaterad"
        (ignore Board, use GitHub data)
```

**Use case:** Never use Project Board as primary source; always verify with GitHub

---

## 🔄 ACTIVITY DETECTION ALGORITHM

For each team member, follow this sequence:

```
1. Collect:
   ├─ All open issues (assigned or authored by person)
   ├─ All open PRs (authored or assigned)
   ├─ All branches (created by or with commits from person)
   ├─ All recent commits (by person in REPORTING_PERIOD)
   └─ Project Board status for each issue (Ready, In Progress, To Do)

2. Correlate:
   ├─ For each issue: find linked PRs, matching branches, recent commits, Board status
   ├─ For each PR: find linked issue, commits, branch
   ├─ For each branch: infer issue number, find commits, find PR
   └─ For each commit: link to issue (via message) or PR (via branch)

3. Deduplicate:
   └─ Combine all evidence into one "activity record" per person

4. Classify & Show:
   ├─ IF (open_pr + linked_issue + assignee) → LEVEL 1 → Show on ①B
   ├─ ELSE IF (open_issue + matching_branch + recent_commits) → LEVEL 2 → Show on ①C
   ├─ ELSE IF (open_issue + matching_branch) → LEVEL 3 → Show on ①C
   ├─ ELSE IF (open_assigned_issue) → LEVEL 4 → Show on ①E
   ├─ ELSE IF (recent_commits_unlinked) → LEVEL 5 → Don't show (suggest linking)
   ├─ ELSE IF (no_activity_this_period) → "Ingen aktivitet denna vecka"
   └─ MANDATORY: Every open assigned issue must be accounted for (shown or excluded with reason)
```

**CRITICAL RULE: COMPLETENESS**

Before rendering, validate:
```
open_assigned_issues_from_github == (issues_shown_in_①B_①C_①D_①E + explicit_exclusions)
```

If this fails → presentation generation STOPS and shows which issues are missing.

---

## 🎯 HOW TO SHOW THIS ON SLIDES

### Slide ①A — Merged PRs
**Show:** All merged PRs (all levels of evidence required them to exist → already done)

---

### Slide ①B — Väntar i PR (NEW)
**Show:** Level 1 evidence only
- Open PR + linked issue + assignee ✓
- Include: PR number, issue number, title, assignee, reviewer(s), branch
- Format: `#PR · #ISSUE Title`
- Reviewer field is CRITICAL — shows who is blocking

**Render gate check:**
```
[ ] All open PRs linked to active issues are shown
[ ] All requested_reviewers are visible
[ ] If no reviewers assigned: show "Review: ej tilldelad"
```

---

### Slide ①C — Pågår denna vecka utan PR
**Show:** Level 2 + Level 3 evidence
- Open issue + matching branch + (optional: recent commits)
- Include: issue number, title, assignee, branch
- Format: `#ISSUE Title`
- Branch shows where the work lives

**Render gate check:**
```
[ ] All open issues with active branches shown (not in ①B)
[ ] Branch name visible for context
```

---

### Slide ①D — Pågår denna vecka: Cross-team
**Show:** Level 2 + Level 3 evidence WHERE issue affects multiple teams
- Same as ①C, but filtered to cross-team issues only
- Svart/neutral border indicates multi-team ownership

---

### Slide ①E — Tilldelad / Ej påbörjad (Level 4 + Board Status)
**Show:** Open assigned issues WITHOUT matching branch, classified by Project Board status

**MANDATORY RULE: All open assigned issues must be shown or explicitly excluded.**

If issue is open + assigned to person + no matching branch exists:

```
IF Project Board status = "In Progress" or "Ready":
  → Show on ①E with current status
  → Format: "⏳ #ISSUE Title — [status] — Ingen branch ännu"
  
ELSE IF Project Board status = "To Do" or no status:
  → Show on ①E as capacity info
  → Format: "⏳ #ISSUE Title — Backlog"
  
ELSE:
  → Explicit omission with reason (archived, dependency, etc)
```

**Example card:**
```
⏳ #89 · Add MVP core-flow E2E test
Zaida · No branch yet
Status: Ready to start
```

**Use case:** Track who has assigned work that hasn't started yet. Prevents issues from silently disappearing.

---

## ⚠️ WHAT NOT TO SHOW

❌ **Project Board status alone** — too unreliable
❌ **Level 5 orphaned commits** — until linked to issue
❌ **Old branches with no recent commits** — assume paused/stale
❌ **Closed issues** — belong in slide ①A (merged)

---

## 🔗 INTEGRATION WITH DATA ACQUISITION

**This model is implemented via:**

1. **DATA_ACQUISITION_CONTRACT.yaml**
   - Section: `open_pull_requests` (Level 1 evidence)
   - Section: `repository_branches_and_commits` (Level 2-3 evidence)
   - Section: `active_issues` (foundation for all levels)

2. **DATA_COLLECTION_MANDATORY.md**
   - Checklist: "All PRs linked to issues?"
   - Checklist: "All branches matched to issues?"
   - Checklist: "Correlation complete?"

3. **RENDER_GATE_CHECKLIST.md**
   - Check: "Every person with work is shown in ①A, ①B, ①C, or ①D?"
   - Check: "No open PR is missing from ①B?"

---

## 🔍 CODE INSPECTION — Beyond Git Signals

**Git signals (commits, branches, PRs) show ACTIVITY, but not CODE QUALITY.**

When evaluating "Pågår" issues:

```
GITHUB SIGNALS (Automatic):
  ✅ Branch exists
  ✅ Recent commits found
  ✅ PR is open

HUMAN INSPECTION (Required):
  ? Code looks like it's progressing?
  ? Does it match the issue description?
  ? Any obvious blockers or incomplete sections?
```

**Examples of what code inspection reveals:**

| Git Says | Code Says | Action |
|---|---|---|
| "Pågår — commit today" | "Stalled, incomplete refactor" | Flag as: "Code needs review" |
| "Pågår — 5 commits this week" | "Wrong direction, needs rebase" | Flag as: "Direction unclear" |
| "Pågår — branch active" | "Feature mostly working, minor bugs" | OK — proceeding normally |

**Requirement:**
- Before displaying issue as "Pågår", reviewer SHOULD inspect code
- If concerned: add annotation (not hiding problems, surfacing them)
- If no access to code: mark as "Code not inspected — [reason]"

**This prevents:** Showing work as "on track" when it's actually stalled or wrong

---

## 🚫 COMPLETENESS VALIDATION — MANDATORY RENDER GATE

**Before any presentation is rendered, this check MUST pass:**

```python
# Fetch all open issues assigned to each team member this sprint
open_assigned_issues = github_api.issues(state='open', assignee=person)

# Collect all issues actually rendered in presentation
rendered_issues = (
    issues_on_slide_①B +  # PR waiting (LEVEL 1)
    issues_on_slide_①C +  # Pågår no PR (LEVEL 2-3)
    issues_on_slide_①D +  # Cross-team
    issues_on_slide_①E +  # Assigned no branch (LEVEL 4)
    issues_explicitly_excluded  # with documented reason
)

# VALIDATION
if open_assigned_issues != rendered_issues:
    FAIL("Missing issues:")
    for issue in (open_assigned_issues - rendered_issues):
        print(f"  #{issue.number} {issue.title} — why was this omitted?")
```

**Failure mode:** If ANY open assigned issue is missing from the presentation without explanation → rendering STOPS.

**Allowed exclusions (must be documented):**
- "Outside sprint scope" (document why)
- "Blocked by X" (document blocker)
- "Archived/closed" (should not be open)
- "Wrong assignee cached" (fix GitHub)

**This rule prevents:** Silent disappearance of issues (#88, #89) from presentations.

---

## 📝 EXAMPLE: One Person's Complete Activity Record

```
Zaida Wiss (@zaida-wiss):

LEVEL 1 (PR + Issue + Assignee):
  - #68 · #67 Update README
    ├─ Assignee: Zaida
    ├─ Reviewers: Björn
    ├─ Branch: docs/#67-update-readme
    ├─ Status: Väntar på review (blocker: Björn needs to approve)
    └─ ACTION: Show on ①B "Väntar i PR"

LEVEL 2 (Issue + Branch + Recent Commits):
  - #72 Add analytics dashboard
    ├─ Assignee: Zaida
    ├─ Branch: frontend/#72-analytics
    ├─ Recent commits: 15 sep, 16 sep
    ├─ Status: Pågår — arbete fortsätter, PR nästa
    └─ ACTION: Show on ①C "Pågår denna vecka utan PR"

LEVEL 4 (Assigned Issue):
  - #95 Refactor auth middleware
    ├─ Assignee: Zaida
    ├─ No branch found
    ├─ Status: Tilldelad — arbete inte påbörjat eller branch saknas
    └─ ACTION: Include as capacity info (not shown on ①B/①C, but noted if relevant)

SUMMARY FOR MEETING SLIDE:
  ✅ Mergat: (from slide ①A — PRs merged earlier)
  🟠 Väntar: #68 · #67 · Björn behöver granska
  🟠 Pågår: #72 · Analytics dashboard, branch active

=> Zaida är aktiv denna vecka, blocking point är Björn's review
```

---

## ✅ QUALITY ASSURANCE

**Before rendering presentation:**

```
[ ] All team members accounted for:
    - If active: shown in ①A (merged) or ①B/①C (active)
    - If no work: shown with "Ny issue eller tillgänglig för hjälp"

[ ] Correlation verified:
    - Each issue has a linked branch or PR
    - Each PR has a linked issue
    - Branch names match issue numbers when possible

[ ] Reviewer coverage:
    - All open PRs have reviewers assigned (or show "ej tilldelad")
    - Helps team identify review blockers

[ ] No orphaned work:
    - No commits exist without issue link
    - No branches exist without issue link
    - No PRs exist without issue link
```

---

**Status:** PRODUCTION  
**Version:** 1.0  
**Updated:** 2026-09-16
