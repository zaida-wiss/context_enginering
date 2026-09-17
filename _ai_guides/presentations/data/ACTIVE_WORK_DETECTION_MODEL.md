---
name: active_work_detection_model
description: Evidence hierarchy for detecting active work without exposing internal evidence labels in the deck
metadata:
  type: specification
  critical: true
  version: 1.1
---

# 🔍 ACTIVE WORK DETECTION MODEL

This file defines **internal evidence classification** for determining what someone is actually working on.

It owns:
- evidence levels
- correlation of issues, PRs, branches and commits
- classification of active vs assigned work
- completeness accounting

It does **not** own card styling or visible card metadata.

Visible card treatment belongs to `design/CARD_COMPONENT_STANDARD.md`.

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

## 1. EVIDENCE HIERARCHY — INTERNAL ONLY

### LEVEL 1 — strongest
Open PR + linked issue + verified assignee.

Conclusion: definite active work.

### LEVEL 2 — very strong
Open issue + matching branch + recent commits.

Conclusion: very likely active work.

### LEVEL 3 — strong
Open issue + matching branch, but no recent commit in reporting period.

Conclusion: possibly active or paused.

### LEVEL 4 — moderate
Open assigned issue with no matching active branch.

Conclusion: assigned/backlog, not safely treated as active implementation.

### LEVEL 5 — weak
Recent commits without verified issue/PR linkage.

Conclusion: unconfirmed work; do not present as confirmed issue work.

### LEVEL 6 — weakest
Project Board status alone.

Conclusion: insufficient as primary evidence; verify with GitHub signals.

---

## 2. PRESENTATION EXPOSURE POLICY

Evidence levels exist to drive **selection and confidence internally**.

Do **not** render labels such as:
- `GitHub · nivå 1`
- `GitHub nivå 2`
- `Level 1 evidence`
- `Strong GitHub evidence`

The meeting audience should see the useful work state, not the internal scoring model.

Use visible status only when it helps the meeting, for example:
- `Öppen PR`
- `Väntar på review`
- `Branch aktiv`
- `Tilldelad · ingen branch`

The exact visible card formatting is owned by `CARD_COMPONENT_STANDARD.md`.

Do not replace the evidence-level text with a special evidence-level color. Color must not expose internal classification as a second hidden legend.

A normal work-status symbol may be used when useful, but evidence level itself stays internal.

---

## 3. ACTIVITY DETECTION ALGORITHM

For each team member:

<<<<<<< HEAD
CONCLUSION: ⚠️ POSSIBLY active work (or paused)
STATUS: "Pågår — branch aktiv, senaste commit utanför vecka"
```
=======
1. collect all open assigned issues
2. collect authored/assigned open PRs
3. collect branches and recent commits
4. correlate PR ↔ issue ↔ assignee ↔ branch ↔ commit
5. deduplicate into one activity record per work item/person
6. classify using Levels 1–6
7. decide placement from classification and team/cross-team scope
8. ensure all open assigned issues are accounted for
>>>>>>> d8ba888 (docs(presentations): keep evidence levels internal)

Placement logic:
- Level 1 → active work slide
- Level 2 → active work slide
- Level 3 → active work slide, with useful visible state if uncertainty matters
- Level 4 → assigned/backlog section
- Level 5 → do not present as confirmed issue work
- Level 6 alone → do not use as primary evidence

---

## 4. COMPLETENESS RULE

Every open assigned issue must be either:
- shown in active/assigned slides, or
- explicitly excluded in the internal audit with a valid reason

<<<<<<< HEAD
CONCLUSION: 🤔 POSSIBLY assigned, maybe not started
STATUS: "Tilldelad — arbete tidigt eller ännu inte påbörjat"
=======
Required equality:

```text
open_assigned_issues == rendered_assigned_or_active_issues + explicit_exclusions
>>>>>>> d8ba888 (docs(presentations): keep evidence levels internal)
```

Any mismatch stops rendering.

Allowed exclusion reasons must be factual and documented, for example:
- outside current sprint scope
- blocked and intentionally excluded by slide-specific rule
- stale/wrong assignment requiring GitHub cleanup

---

## 5. TEAM ACCOUNTING

<<<<<<< HEAD
```
Commit 16 sep · Erik · "Fix JWT refresh token issue"
├── no PR found
├── no issue reference in message
└── branch: backend/jwt-fix

CONCLUSION: ❓ UNCONFIRMED work
STATUS: "Arbete detekterat — behöver länkas till issue"
```
=======
All registered team members must be accounted for.

For each person, determine whether they have:
- merged work
- active work
- assigned/backlog work
- no verified work in the reporting period
>>>>>>> d8ba888 (docs(presentations): keep evidence levels internal)

If no verified work is found, use the approved meeting wording from the slide/content authority rather than inventing activity.

---

## 6. DATA INTEGRITY

<<<<<<< HEAD
```
Project Board status: "In Progress"
├── but no corresponding issue found
├── no PR
├── no commits
└── Board last updated: 30 aug

CONCLUSION: ❌ UNRELIABLE
```

**Use case:** Never use Project Board as primary source; always verify with GitHub
=======
Never infer:
- assignee from commit author alone
- issue number solely from a branch name without verification
- active status from Project Board alone
- reviewer from requested reviewer alone
- merger from PR author alone

Use the registered data acquisition rules and source hierarchy.
>>>>>>> d8ba888 (docs(presentations): keep evidence levels internal)

---

## 7. CODE INSPECTION

Git signals show activity, not code quality.

<<<<<<< HEAD
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
=======
When code inspection is available, it may help identify:
- obvious mismatch with issue scope
- stalled/incomplete implementation
- technical blocker

Do not convert that inspection into unsupported claims about a person.

If code cannot be inspected, do not add noisy `not inspected` text to ordinary cards unless a slide/content rule explicitly requires it.
>>>>>>> d8ba888 (docs(presentations): keep evidence levels internal)

---

## 8. RENDER HANDOFF

<<<<<<< HEAD
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
=======
Before rendering active/backlog slides verify internally:

```text
all_open_prs_accounted_for == true
all_open_assigned_issues_accounted_for == true
all_team_members_accounted_for == true
visible_evidence_level_label_count == 0
```

Card appearance and visible metadata are then rendered according to `CARD_COMPONENT_STANDARD.md`.

---

**Status:** PRODUCTION
**Version:** 1.1
**Last updated:** 2026-09-17
>>>>>>> d8ba888 (docs(presentations): keep evidence levels internal)
