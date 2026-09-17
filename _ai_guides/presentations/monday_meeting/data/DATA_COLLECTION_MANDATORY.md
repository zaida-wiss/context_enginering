---
name: data-collection-mandatory
description: HOW to collect required information — follow SYSTEM_CONTRACT.yaml requirements
metadata:
  type: process
  critical: true
---

# 🚨 DATA COLLECTION — MECHANICAL EXECUTION

**This file describes HOW to collect information that SYSTEM_CONTRACT.yaml requires.**

**SYSTEM_CONTRACT.yaml owns WHAT is required and WHETHER to STOP. This file owns HOW.**

---

## Required Information Collection

See [`SYSTEM_CONTRACT.yaml`](../SYSTEM_CONTRACT.yaml) for required_information list.

For each required piece of information, use the source priority listed there:

### 1. Team Roster
```
Source: TEAM_ROSTER.md (local file in this repo)
Format: [Name, GitHub username, team designation]
Requirement: All 7 members verified
```

### 2. Merged PRs (REPORTING_PERIOD)
```
Sources: [`DATA_SOURCES.md`](../../data/DATA_SOURCES.md) section "WORK COMPLETED THIS WEEK"
Primary: GitHub API or web pulls tab
Fallback: Google Sheets (see [`_memory/EXTERNAL_SOURCES.md`](../../../../_memory/EXTERNAL_SOURCES.md) for link)

Collect: PR#, title, author, assignee, merged_at timestamp, base branch
Verify: merged_at is within REPORTING_PERIOD (see [`SYSTEM_CONTRACT.yaml`](../../SYSTEM_CONTRACT.yaml))
```

### 3. Active Issues (REPORTING_PERIOD)
```
Sources: [`DATA_SOURCES.md`](../../data/DATA_SOURCES.md) section "WORK IN PROGRESS"
Primary: GitHub API or web issues tab
Fallback: Google Sheets or reconstructed from Project Board

Collect: Issue#, title, assignee, updated_at timestamp, labels
Verify: has assignee, recent activity (comment/update) in REPORTING_PERIOD
```

---

## 4. Branches

```
Sources: [`DATA_SOURCES.md`](../../data/DATA_SOURCES.md) section "REPOSITORY STRUCTURE"
Primary: GitHub API branches endpoint
Fallback: GitHub web branches page

Collect: All branches in repository (develop, Java-Development-Environment, C/C++-Native, etc.)
Requirement: Branches per SYSTEM_CONTRACT.yaml dataset_5_branches (REQUIRED before GitHub collection complete)
```

## 5. Commits

```
Sources: GitHub API commits endpoint (per branch)
Primary: Query commits for each team branch during REPORTING_PERIOD
Fallback: Derive from merged PR metadata

Collect: Author, timestamp, branch, message
Requirement: Commits per SYSTEM_CONTRACT.yaml dataset_6_commits (REQUIRED before GitHub collection complete)
Note: Risk analysis (slide ②) requires commit history to estimate effort and velocity
```

---

## Optional Enrichment (non-blocking)

See [`SYSTEM_CONTRACT.yaml`](../SYSTEM_CONTRACT.yaml) for optional_enrichment list.

Collect if available. If unavailable, note in footer with ⚠️. Never stop rendering.

### Project Board (optional)
```
Source: See [`_memory/EXTERNAL_SOURCES.md`](../../../../_memory/EXTERNAL_SOURCES.md) for board link
Fallback: Reconstruct from Issues and PRs data
```

### Meeting Protocol (optional)
```
Source: See [`_memory/EXTERNAL_SOURCES.md`](../../../../_memory/EXTERNAL_SOURCES.md) for Google Docs link
Use for: Context only — never influences required-information decisions
```

---

## Data Organization → data_audit

Organize collected data into data_audit format specified in SYSTEM_CONTRACT.yaml.

See `data_audit` section in SYSTEM_CONTRACT.yaml for exact format.

---

## Fallback Strategy

For each required information item:
1. Try primary method
2. If primary fails, try next method in priority list
3. If all fail, report to [`SYSTEM_CONTRACT.yaml`](../../SYSTEM_CONTRACT.yaml) execution logic (step_2 rule)
   - [`SYSTEM_CONTRACT.yaml`](../../SYSTEM_CONTRACT.yaml) decides: STOP or CONTINUE
   - This file does NOT make that decision

---

**This file is ONLY HOW.** [`SYSTEM_CONTRACT.yaml`](../../SYSTEM_CONTRACT.yaml) **owns WHAT and WHETHER.**

**Version:** 2.0 (simplified to execution only)
**Status:** PRODUCTION
