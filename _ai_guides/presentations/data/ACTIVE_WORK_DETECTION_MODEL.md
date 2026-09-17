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

1. collect all open assigned issues
2. collect authored/assigned open PRs
3. collect branches and recent commits
4. correlate PR ↔ issue ↔ assignee ↔ branch ↔ commit
5. deduplicate into one activity record per work item/person
6. classify using Levels 1–6
7. decide placement from classification and team/cross-team scope
8. ensure all open assigned issues are accounted for

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

Required equality:

```text
open_assigned_issues == rendered_assigned_or_active_issues + explicit_exclusions
```

Any mismatch stops rendering.

Allowed exclusion reasons must be factual and documented, for example:
- outside current sprint scope
- blocked and intentionally excluded by slide-specific rule
- stale/wrong assignment requiring GitHub cleanup

---

## 5. TEAM ACCOUNTING

All registered team members must be accounted for.

For each person, determine whether they have:
- merged work
- active work
- assigned/backlog work
- no verified work in the reporting period

If no verified work is found, use the approved meeting wording from the slide/content authority rather than inventing activity.

---

## 6. DATA INTEGRITY

Never infer:
- assignee from commit author alone
- issue number solely from a branch name without verification
- active status from Project Board alone
- reviewer from requested reviewer alone
- merger from PR author alone

Use the registered data acquisition rules and source hierarchy.

---

## 7. CODE INSPECTION

Git signals show activity, not code quality.

When code inspection is available, it may help identify:
- obvious mismatch with issue scope
- stalled/incomplete implementation
- technical blocker

Do not convert that inspection into unsupported claims about a person.

If code cannot be inspected, do not add noisy `not inspected` text to ordinary cards unless a slide/content rule explicitly requires it.

---

## 8. RENDER HANDOFF

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
