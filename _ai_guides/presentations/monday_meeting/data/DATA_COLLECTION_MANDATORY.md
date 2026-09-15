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
Method: Read TEAM_ROSTER.md file
Format: [Name, GitHub username, team designation]
Verify: All 7 members present
```

### 2. Merged PRs (reporting period)
```
Method 1 (primary): GitHub PRs API or web
  https://github.com/chas-challenge-2026/avanza-team1/pulls

Method 2 (fallback): Google Sheets
  https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/

Method 3 (fallback): Individual PR pages
  https://github.com/chas-challenge-2026/avanza-team1/pull/[NUMBER]

Collect: PR#, title, author, assignee, merged_at timestamp, base branch
Verify: timestamp is within reporting period (SYSTEM_CONTRACT.yaml)
```

### 3. Active Issues (reporting period)
```
Method 1 (primary): GitHub Issues API or web
  https://github.com/chas-challenge-2026/avanza-team1/issues

Method 2 (fallback): Google Sheets
  https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/

Method 3 (fallback): Reconstruct from Project Board
  https://github.com/orgs/chas-challenge-2026/projects/31/

Collect: Issue#, title, assignee, updated_at timestamp, labels
Verify: has assignee, recent activity (comment or update in reporting period)
```

---

## Optional Enrichment (non-blocking)

See [`SYSTEM_CONTRACT.yaml`](../SYSTEM_CONTRACT.yaml) for optional_enrichment list.

Collect if available. If unavailable, note in footer with ⚠️. Never stop rendering.

### Commits (optional)
```
Derive from: merged PR metadata (each PR contains commits)
If additional commits needed: https://github.com/chas-challenge-2026/avanza-team1/commits/develop
```

### Branches (optional)
```
Derive from: active PR and issue data (branches are from these)
If direct list needed: https://github.com/chas-challenge-2026/avanza-team1/branches
```

### Project Board (optional)
```
Source: https://github.com/orgs/chas-challenge-2026/projects/31/
Fallback: Reconstruct from Issues and PRs
```

### Meeting Protocol (optional)
```
Source: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/
Use for: context only, never influences required-information collection
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
3. If all fail, report to SYSTEM_CONTRACT.yaml execution logic (step_2 rule)
   - SYSTEM_CONTRACT.yaml decides: STOP or CONTINUE
   - This file does NOT make that decision

---

**This file is ONLY HOW. SYSTEM_CONTRACT.yaml owns WHAT and WHETHER.**

**Version:** 2.0 (simplified to execution only)
**Status:** PRODUCTION
