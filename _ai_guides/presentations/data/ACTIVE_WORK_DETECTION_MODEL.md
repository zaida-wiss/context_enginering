---
name: active_work_detection_model
description: Evidence hierarchy for detecting active work — without relying solely on Project Board
metadata:
  type: specification
  critical: true
  version: 1.1
---

# 🔍 ACTIVE WORK DETECTION MODEL

**This file defines HOW to determine "what is someone actually working on?" using evidence from GitHub.**

**Problem:** Project Board is often stale or inaccessible. Commits + branches + issues + PRs together tell a more accurate story.

**Solution:** Use a **proof hierarchy** — combine multiple signals to determine active work status.

---

## 🔁 TEAM COLLECTION-BRANCH LIFECYCLE — MANDATORY

Backend and Native use team collection branches before final delivery.

Canonical branches:
- Backend: `Java-Development-Environment`
- Native: `C/C++-Native`

The lifecycle is the same for both teams:

```text
1. Assigned / started, not merged to collection branch
   → ACTIVE / PÅ GÅNG

2. Merged to team collection branch, not yet promoted onward
   → COLLECTION-BRANCH MERGED

3. Promoted onward to final delivery branch
   → REMOVE from collection-branch merged view
   → treat as final delivered work
```

Rules:
- A work item MUST NOT remain in `På gång` after it has been verified merged to its team's collection branch.
- A work item MUST remain visible on the team's collection-branch merge slide while it is present there and not yet promoted onward.
- Once the same work is promoted onward, it MUST disappear from the collection-branch slide.
- Backend and Native MUST use identical lifecycle logic.
- Deduplicate by linked issue / PR / work identity, not by raw merge-commit count alone.
- A collection-branch item may have been merged before the current reporting period and still MUST be shown if it remains unpromoted.

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

**Use case:** Show on slide ①D (team-based) or ①E (cross-team) "PR väntar på review"

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

**Use case:** Show on slide ①D (team-based) or ①E (cross-team) "Pågår denna vecka utan PR"

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
```

**Use case:** Include but flag as uncertain

**Show on:** ①D (team-based) or ①E (cross-team)

---

### LEVEL 4 — Moderate Evidence: Open Assigned Issue Alone

```
Open issue #89
├── title: "Refactor database layer"
├── assignee: Rasha
└── no matching branch found
└── no recent commits found

CONCLUSION: 🤔 POSSIBLY assigned, maybe not started
STATUS: "Tilldelad — arbete tidigt eller ännu inte påbörjat"
```

**Use case:** Include to track who has capacity, but lower priority

---

### LEVEL 5 — Weak Evidence: Recent Commits Without Issue Link

```
Commit 16 sep · Erik · "Fix JWT refresh token issue"
├── no PR found
├── no issue reference in message
└── branch: backend/jwt-fix

CONCLUSION: ❓ UNCONFIRMED work
STATUS: "Arbete detekterat — behöver länkas till issue"
```

**Use case:** Suggest linking to issue, don't show on slide without verification

---

### LEVEL 6 — Weakest Evidence: Project Board Status Alone

```
Project Board status: "In Progress"
├── but no corresponding issue found
├── no PR
├── no commits
└── Board last updated: 30 aug

CONCLUSION: ❌ UNRELIABLE
```

**Use case:** Never use Project Board as primary source; always verify with GitHub

---

## 🔄 ACTIVITY DETECTION ALGORITHM

For each team member, follow this sequence:

```text
1. Collect:
   ├─ All open issues (assigned or authored by person)
   ├─ All open PRs (authored or assigned)
   ├─ All branches (created by or with commits from person)
   ├─ All recent commits (by person in REPORTING_PERIOD)
   ├─ All merges into Backend/Native collection branches
   ├─ Evidence that collection-branch work has been promoted onward
   └─ Project Board status for each issue

2. Correlate:
   ├─ For each issue: find linked PRs, matching branches, recent commits, Board status
   ├─ For each PR: find linked issue, commits, head branch, base branch
   ├─ For each branch: infer issue number, find commits, find PR
   ├─ For each collection-branch merge: identify linked issue/PR/work identity
   └─ For each collection item: determine whether same work is already promoted onward

3. Deduplicate:
   └─ Combine all evidence into one activity record per work item/person

4. Classify & Show:
   ├─ IF work merged to collection branch AND NOT promoted onward → ①B or ①C
   ├─ ELSE IF open_pr + linked_issue + assignee → LEVEL 1 → ①D/①E
   ├─ ELSE IF open_issue + matching_branch + recent_commits + TEAM → LEVEL 2 → ①D
   ├─ ELSE IF open_issue + matching_branch + recent_commits + CROSS_TEAM → LEVEL 2 → ①E
   ├─ ELSE IF open_issue + matching_branch + TEAM → LEVEL 3 → ①D
   ├─ ELSE IF open_issue + matching_branch + CROSS_TEAM → LEVEL 3 → ①E
   ├─ ELSE IF open_assigned_issue + no_branch → LEVEL 4 → ①E
   ├─ ELSE IF recent_commits_unlinked → LEVEL 5 → don't show until verified
   └─ IF collection item promoted onward → remove from ①B/①C and represent as final delivery
```

**CRITICAL RULE: COMPLETENESS**

Before rendering, validate:

```text
open_assigned_issues_from_github ==
  issues_shown_in_①D_①E
  + issues_currently_on_①B_①C
  + explicit_exclusions
```

Additionally:

```text
collection_branch_items_promoted_onward_remaining_count == 0
active_items_already_merged_to_collection_branch_count == 0
```

If any check fails → presentation generation STOPS.

---

## 🎯 HOW TO SHOW THIS ON SLIDES

### Slide ①A — Merged to final integration/delivery branch
**Show:** Work actually promoted to the final delivery branch according to the current presentation contract.
**Evidence:** Already delivered work.

---

### Slide ①B — Backend collection branch
Canonical branch: `Java-Development-Environment`.

**Show:** Backend work merged to the collection branch that has NOT yet been promoted onward.

This is a current state view, not only a reporting-period event list.

---

### Slide ①C — Native collection branch
Canonical branch: `C/C++-Native`.

**Show:** Native work merged to the collection branch that has NOT yet been promoted onward.

This is a current state view, not only a reporting-period event list.

---

### Slide ①D — Pågår denna vecka: Team-based

**Show only pre-collection-merge work:**
- Open PR + issue
- Open issue + matching branch + recent commits
- Open issue + matching branch, older commits

**Never show here:** work already verified merged into `Java-Development-Environment` or `C/C++-Native`.

---

### Slide ①E — Cross-team + Assigned/Backlog

Section A: verified cross-team work not yet merged to collection/final branch.

Section B: assigned issues without verified active branch/PR.

Every open assigned issue must be shown on ①D/①E, represented on ①B/①C if already collection-merged, or explicitly excluded.

---

## ⚠️ WHAT NOT TO SHOW

❌ Project Board status alone as proof of active work
❌ Orphaned commits until linked/verified
❌ Work already merged to a collection branch as `På gång`
❌ Work already promoted onward on ①B/①C
⚠️ Old branches with no recent commits may be shown as uncertain if still pre-merge

---

## 🔗 INTEGRATION WITH DATA ACQUISITION

This model requires:

1. `active_issues`
2. `open_pull_requests`
3. `repository_branches_and_commits`
4. merged PRs / merge evidence for both collection branches
5. promotion evidence from collection branches onward

The acquisition layer must collect enough history to reconstruct the collection-branch state even when a collection merge happened before the current reporting period.

---

## 🚫 COMPLETENESS VALIDATION — MANDATORY RENDER GATE

Before any presentation is rendered:

```text
[ ] Every open assigned issue is accounted for
[ ] No work appears both as På gång and collection-merged
[ ] No promoted work remains on Backend collection slide
[ ] No promoted work remains on Native collection slide
[ ] Backend and Native use identical lifecycle rules
[ ] Collection state is derived by work identity, not just raw merge count
```

Failure of any item → STOP.

---

## ✅ QUALITY ASSURANCE

Before rendering:

```text
[ ] Team members accounted for
[ ] Active work is truly pre-merge
[ ] Collection-branch work is shown while awaiting onward promotion
[ ] Promoted work disappears from collection view
[ ] No duplicate issue appears in multiple lifecycle states
[ ] Branch names and issue links are verified where available
[ ] Reviewer coverage is shown where relevant
```

---

**Status:** PRODUCTION
**Version:** 1.1
**Updated:** 2026-09-17