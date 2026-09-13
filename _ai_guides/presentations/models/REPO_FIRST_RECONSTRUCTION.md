---
name: repo-first-reconstruction
description: Repo-first methodology for reconstructing weekly work — collect all activity first, classify second
metadata:
  type: process
  critical: true
---

# 📊 REPO-FIRST RECONSTRUCTION — Alla Commits/PRs Först, Sen Klassificering

**RULE: Weekly work reconstruction must start with COMPLETE repository activity, not with issues or person-first approach.**

---

## ❌ WRONG APPROACH (causes missing work)

```
❌ Issue-first:
   1. List open/closed issues
   2. Pick relevant ones
   3. Try to find commits that match
   Result: Commits without issues are MISSED (like Björn's design system)

❌ Person-first:
   1. Go through each person
   2. Find their issues
   3. Report those
   Result: Work that person contributed to but didn't "own" is MISSED

❌ PR-first:
   1. List merged PRs
   2. Only look at their titles
   3. Stop when done
   Result: Multiple commits/PRs per person per work area get collapsed
```

---

## ✅ CORRECT APPROACH (repo-first)

**Step 1: COLLECT EVERYTHING**

```
From GitHub, fetch COMPLETE dataset for exact time window
(from previous Monday meeting to this Monday meeting):

☐ ALL commits on develop branch
  - Include author name, hash, message, date
  - Do NOT limit to "top N" or "recent"
  
☐ ALL merged PRs (merged during period)
  - Include author, title, description, merge date
  - Include linked issues (if any)
  
☐ ALL open PRs with activity during period
  - Comments, reviews, code changes
  
☐ ALL issues with activity during period
  - Closed issues (when closed)
  - Open issues with commits/PR updates (NOT just comments)
```

**Step 2: RECONSTRUCT WORK AREAS**

Group by file paths and problem domain:

```
frontend/**              → Frontend work area
backend/**               → Backend work area
native/**, c/**, cpp/** → System/Native work area
docs/**                  → Associate with primary area (who's it documenting?)
shared/*                 → Cross-team
```

**Step 3: IDENTIFY CONTRIBUTORS**

For each commit/PR:
```
- Extract author GitHub login
- Map to real name via TEAM_ROSTER.md
- Assign to team (Frontend/Backend/System)
- Assign to work area (Auth, Dashboard, Risk Motor, etc)
```

**Step 4: CLUSTER INTO WORK AREAS**

Group commits/PRs by work area, showing all contributors:

```
Frontend – Auth & Login:
  ✅ PR #90 Login Page (Zaida)
    - 4 commits by Zaida
    - Merged 2026-09-10
  ✅ PR #91 Password Reset (Zaida)
    - 2 commits by Zaida
    - Merged 2026-09-11

Frontend – Design System:
  ✅ PR #79 Design System Foundation (Björn)
    - 15 commits by Björn
    - 26 files changed
    - Merged 2026-09-10
    - Includes: CSS variables, Panel refactor, topbar rebuild
```

**Step 5: VALIDATE COVERAGE**

Check TEAM_ROSTER.md:

```
Frontend: Zaida ✅, Jan [?], Marco [?]
Backend: Anna [?], Kiran [?], Tomac [?]
System: Björn ✅, Sam [?]

Who's missing? ← If anyone is missing, report explicitly
```

**Step 6: BUILD SLIDES**

Only after ALL data is collected and classified.

---

## Mechanical Rules

### Rule 1: No Activity Disappears

```
EVERY commit/PR from time window MUST appear somewhere:

IF commit is on develop/relevant branch
  AND timestamp is within period
  THEN it MUST be reported in presentation

UNLESS: Excluded by documented fallback (e.g., "revert commit", "ci/cd-only")
```

### Rule 2: Contributor-Based Clustering

```
DO NOT:
  "issue #42 was done" (implies one person)

DO:
  "auth work area: Zaida (4 commits, PR #90), Jan (review, 1 commit)"
```

### Rule 3: File Path Authority

```
If file path unclear, use this hierarchy:
  1. PR description / commit message
  2. File paths changed
  3. Issue title/description
  4. Team knowledge (backend person usually works in backend/)
```

### Rule 4: Multiple Small PRs = One Work Area

```
DO NOT list:
  PR #80 Dashboard mock
  PR #81 Dashboard refactor
  PR #82 Dashboard styles
  (as three separate items)

DO cluster:
  Frontend – Dashboard
  ✅ PR #80 #81 #82 (Tomac, 3 commits each)
```

### Rule 5: Work Without Issues Still Counts

```
Björn's design system work:
  - No GitHub issue explicitly labeled "design system"
  - But 15 commits on frontend/components/
  - And PR #79 with full description
  - STILL counts as major work area
  
Presentation MUST show it.
```

---

## Time Window Calculation

```
THIS WEEK:
  Starts: Previous Monday 09:00 (when sprint meeting ended)
  Ends: This Monday 09:00 (when sprint meeting starts)
  
Example: 
  Previous meeting: Monday 2026-09-08 09:00
  This meeting: Monday 2026-09-15 09:00
  Window: All activity 2026-09-08 09:00 — 2026-09-15 09:00
  
RULE: EXACT timestamp required. "Last 7 days" is NOT precise enough.
```

---

## Completeness Gate

**Before Slide ①A and ①B are rendered:**

```
✅ All commits in time window accounted for
✅ All merged PRs in time window accounted for
✅ All open PRs with activity in time window accounted for
✅ All open issues with activity (commits/PR-updates, NOT comments) accounted for
✅ Every team member in TEAM_ROSTER.md checked
✅ Coverage report generated (who had activity, who didn't)
✅ No work area is empty in a team that had activity
```

---

## Why Repo-First Works

```
Issue-first:          "What issues were closed?"
                      → Misses work without issues

Person-first:         "What did Jan do?"
                      → Misses work Jan contributed to but didn't own

Repo-first:           "What changed in the repo?"
                      → Captures EVERYTHING
                      → Then assign to person/team/area
                      → Nothing gets lost
```

---

## Example: Why Björn's Work Didn't Disappear with Repo-First

```
Repo-first approach:
  1. Collect all PRs merged 2026-09-08 to 2026-09-15
     → Found PR #79 (design system)
  2. Extract author: björnb → Björn
  3. Classify by path: frontend/components/* → Frontend
  4. Group: Frontend – Design System
  5. Report: "Björn: Design System (15 commits, PR #79)"

Issue-first approach (what happened):
  1. List GitHub issues from backlog
  2. See issue #40 (login) is closed
  3. Focus on that
  4. Never found that Björn also worked on design system
     (because design system wasn't a separate issue)
  5. Result: Björn's work missing from presentation
```

---

**Senast uppdaterad:** 2026-09-13
