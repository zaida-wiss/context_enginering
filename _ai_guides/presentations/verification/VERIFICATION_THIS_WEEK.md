---
name: verification-this-week
description: RETIRED — execution receipts are defined by SYSTEM_CONTRACT.yaml
metadata:
  type: retired_reference
  status: retired
---

# 🔍 VERIFICATION REPORT — Data Sources This Week

> **RETIRED. DO NOT USE FOR PRODUCTION.** Use the current execution and data
> acquisition receipts instead.

**Status: PARTIAL — Waiting for you to provide final sources**

This shows what CAN and CANNOT be verified from available local sources.

---

## ✅ SOURCES READ — What We Can Verify

### 1. Git Commits (avanza-team1)
- ✅ Latest commits fetched
- ✅ Branch structure visible (feature/#40-login-page, etc)
- ✅ Active branches identified
- **Finding:** Tomac's work on #28 (wire mock data) confirmed via commit history

### 2. Frontend BIDRAG.md (Local)
- ✅ Read from: `docs/frontend/BIDRAG.md`
- ✅ **Tomac — 2026-09-08:**
  - #28 Wire mockPortfolio into dashboard (PR confirmed)
  - Components: header, navbar, accounts, holdings, allocation 75/25
  - Status: DONE (merged in latest commits)

### 3. Active Branches
- ✅ `feature/#40-login-page` — Login work (Zaida expected)
- ✅ `structure/frontend-establish-design-system-issue-44` — Design system (Björn expected)
- ✅ `Build/frontend/#26-dashboard-panels` — Dashboard work (ongoing)

---

## ❌ SOURCES NOT YET VERIFIED — What's Missing

### 1. **Project Board** ❌
- **Source:** https://github.com/orgs/chas-challenge-2026/projects/31/views/1
- **Status:** NOT READ (requires GitHub auth or web access)
- **What it would show:**
  - Which issues are DONE / IN PROGRESS / BACKLOG
  - Current state of all tracked work
  - Who's assigned to what

### 2. **Meeting Protocol** ❌
- **Source:** See EXTERNAL_SOURCES.yaml: GOOGLE_MEETING_PROTOCOL
- **Status:** NOT READ (requires Google Docs auth)
- **What it would show:**
  - Sprint goals for this week
  - Team priorities
  - Known blockers
  - Decisions made
  - Deadlines

### 3. **Closed Issues This Week** ❌
- **Expected from:** GitHub Issues API
- **Status:** NOT VERIFIED
- **What we need:**
  - Which issues were closed this week?
  - By whom?
  - Which PRs linked to them?

### 4. **Merged PRs This Week** ❌
- **Expected from:** GitHub PRs API
- **Status:** NOT VERIFIED
- **What we need:**
  - Which PRs merged this week?
  - Authors?
  - Linked issues?

---

## 📋 WHAT WE NEED FROM YOU

**To complete verification, provide:**

### Option A: Share the actual sources
- Project Board screenshot or export (status of all issues)
- Meeting Protocol (key decisions, sprint goals)

### Option B: Give us the summary
For THIS WEEK (specify: which week exactly?), tell us:

```
CLOSED ISSUES:
- #40 Login Page — Zaida — Status: ✅
- #44 Design System — Björn — Status: ✅
- #45 Top Bar — Björn — Status: ✅
- (list others)

MERGED PRs:
- PR #90 Login — merged when?
- PR #95 Design System — merged when?
- PR #96 Top Bar — merged when?
- (list others)

COMMITS:
- Zaida: X commits on login
- Björn: X commits on design
- Tomac: X commits on dashboard
- (list others)

PROJECT BOARD STATUS:
- Frontend: (X/Y done)
- Backend: (X/Y done)
- Native: (X/Y done)

SPRINT GOALS:
- What was the focus for this week?
- Any blockers?
- Any deadlines?
```

---

## 🔗 WHY THIS MATTERS

**The issue you identified:** "Login, designsystem, topbar work was hidden"

**Root cause:** Data collection was incomplete (didn't read closed issues/merged PRs)

**This verification report shows:**
- What we CAN read locally ✅
- What we CANNOT read without your input ❌
- Exactly what data is needed to fill the gap

**To fix it:** You provide the three sources (Project Board, Meeting Protocol, closed issues),
and we'll verify the presentation captures ALL of it.

---

## ✅ CHECKLIST — What Needs to Happen

Before ANY presentation is generated for this week, verify:

```
☐ Project Board read and screenshotted/exported
☐ Meeting Protocol reviewed for sprint goals & blockers
☐ Closed issues list created (with assignees & dates)
☐ Merged PRs list created (with authors & dates)
☐ Commits counted per team member
☐ Data entered into TEAM_WORK_OVERVIEW.md template
☐ Presentation generated from verified data
```

---

**Next step:** You provide the three sources (or the summary above),
and we'll verify the presentation data completeness.

**This ensures:** Login-arbete, designsystem, topbar — nothing gets hidden again.

---

**Created:** 2026-09-13
**Status:** Waiting for source data
