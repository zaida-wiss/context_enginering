---
name: data_sources
description: "Guide to data sources (see EXTERNAL_SOURCES.yaml for authoritative registry)"
metadata:
  type: reference
  updated: 2026-09-15
---

# 📊 DATA SOURCES — Where to Find Information

**AUTHORITATIVE REGISTRY:** [`_memory/EXTERNAL_SOURCES.yaml`](_memory/EXTERNAL_SOURCES.yaml)

This file is a **human-friendly guide** only. For actual URLs, IDs, and access methods, see EXTERNAL_SOURCES.yaml.

---

## Data Requirements for Presentations

### 1. WORK COMPLETED THIS WEEK

**Source:** `GITHUB_MERGED_PRS` (see EXTERNAL_SOURCES.yaml)

Filter: `merged_at` within REPORTING_PERIOD, `base.ref == 'develop'`

Fallback: GitHub web merged PRs page, then Google Sheets if available

### 2. ACTIVE ISSUES (open, with owner)

**Source:** `GITHUB_OPEN_ISSUES` (see EXTERNAL_SOURCES.yaml)

Filter: `state=open`, `assignees.length > 0`, `updated_at` within REPORTING_PERIOD

Exclude: Pull requests (filter `pull_request` key)

Fallback: GitHub web issues page, then Google Sheets

### 3. TEAM ROSTER

**Source:** `GITHUB_TEAM_ROSTER` (local file)

Location: `_memory/TEAM_ROSTER.md`

Required: 7 verified members

### 4. PROJECT BOARD STATUS (optional)

**Source:** `GITHUB_PROJECT_BOARD` (see EXTERNAL_SOURCES.yaml)

Can be derived from open issues if unavailable

### 5. RISK & ASSET REGISTER (optional)

**Source:** `GOOGLE_RISK_REGISTER` (see EXTERNAL_SOURCES.yaml)

Requires Google Drive Connector

### 6. MEETING PROTOCOL (fallback)

**Source:** `GOOGLE_MEETING_PROTOCOL` (see EXTERNAL_SOURCES.yaml)

Requires Google Drive Connector

---

## Access Methods

For each source, see EXTERNAL_SOURCES.yaml for:
- Primary access method (preferred)
- Fallback chain (try in order)
- Forbidden methods (never use)
- Allowed methods (use these only)

---

**Last updated:** 2026-09-15  
**All source URLs, IDs, and methods:** see `_memory/EXTERNAL_SOURCES.yaml`
