---
name: external_sources
description: Centralized registry of all external data sources and fallback URLs
metadata:
  type: reference
  critical: true
---

# 🔗 External Sources — ALLOWLIST (NOT JUST REGISTRY)

🚨 **CRITICAL:** Detta är en WHITELIST av godkända externa källor för presentationsgenerering.

**ENDAST källorna i denna fil får kontaktas externt.** Att en URL går att nå betyder INTE att den är tillåten.

Presentation generation:
- ✅ MAY use registered sources listed below
- ❌ MUST NOT use general web search
- ❌ MUST NOT use unregistered websites
- ❌ MUST NOT substitute arbitrary web sources

**Alla externa datakällor, IDs och fallback-strategier ligger här. INGEN annan fil ska ha raw IDs/URLs — länka hit istället.**

---

## 📋 Google Sheets — FALLBACK ONLY (requires Google Connector)

⚠️ **IMPORTANT:** Google Sheets sources require Google Drive Connector. Without it, do NOT attempt CSV/Excel exports — they will fail with safe_open block. Presentation will correctly STOP at DATA_ACQUISITION_RECEIPT if GitHub sources fail AND Google Connector unavailable.

### Sheet 1: Project Data (Commits, PRs, Issues, Board)

| Format | URL | Classification | Access Method | Status |
|--------|-----|-----------------|----------------|--------|
| **View** | https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/ | Fallback | Google Drive Connector REQUIRED | ⚠️ Blocked without connector |
| **CSV Export** | https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/export?format=csv | Fallback | Google Drive Connector REQUIRED | ⚠️ Blocked without connector |
| **Excel Export** | https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/export?format=xlsx | Fallback | Google Drive Connector REQUIRED | ⚠️ Blocked without connector |

**Sheet ID:** `1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI`

**Tabs/GIDs:**
- Commits: `gid=743460023`
- Issues: `gid=77162861`
- PRs: `gid=743460023`
- Project Board: `gid=869242669`

### Sheet 2: Risk & Asset Register

| Format | URL | Classification | Access Method | Status |
|--------|-----|-----------------|----------------|--------|
| **View** | https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/ | Optional | Google Drive Connector REQUIRED | ⚠️ Blocked without connector |
| **CSV Export — Risks** | https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=1796827285 | Optional | Google Drive Connector REQUIRED | ⚠️ Blocked without connector |
| **CSV Export — Assets** | https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=684132349 | Optional | Google Drive Connector REQUIRED | ⚠️ Blocked without connector |

**Sheet ID:** `1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F`

**Tabs/GIDs:**
- Risk-Management: `gid=1796827285`
- Assets: `gid=684132349`

---

## 📄 Google Docs — FALLBACK ONLY (requires Google Connector)

⚠️ **IMPORTANT:** Google Docs sources require Google Drive Connector. Without it, do NOT attempt export URLs — they will fail with safe_open block.

### Meeting Protocol & Decisions

| Format | URL | Classification | Access Method | Status | Purpose |
|--------|-----|-----------------|----------------|--------|---------|
| **View & Edit** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit | Fallback | Google Drive Connector REQUIRED | ⚠️ Blocked without connector | Weekly sprint planning decisions, blockers, action items |
| **TXT Export** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt | Fallback | Google Drive Connector REQUIRED | ⚠️ Blocked without connector | Text export for processing |
| **PDF Export** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=pdf | Fallback | Google Drive Connector REQUIRED | ⚠️ Blocked without connector | PDF export for archive |
| **HTML Export** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=html | Fallback | Google Drive Connector REQUIRED | ⚠️ Blocked without connector | HTML for web publishing |

**Doc ID:** `1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8`

---

## 🔗 GitHub Sources

### REQUIRED for Presentations (must succeed)

| Source | URL | Access Method | Status | Notes |
|--------|-----|----------------|--------|-------|
| **Merged PRs (API)** | https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?state=closed&base=develop&per_page=100 | GitHub Connector OR API | ✅ Working | Canonical method. Filter by merged_at within REPORTING_PERIOD. Use assignees[] for attribution. |
| **Open Issues (API)** | https://api.github.com/repos/chas-challenge-2026/avanza-team1/issues?state=open&per_page=100 | GitHub Connector OR API | ✅ Working | Filter: exclude pull_requests key, assignees.length > 0, updated_at in REPORTING_PERIOD |
| **Team Roster (local)** | _memory/TEAM_ROSTER.md | Local file | ✅ Working | Always available. 7 members, verified via git history. |

### FALLBACK if primary fails (try in order)

| Source | URL | Access Method | Status | Notes |
|--------|-----|----------------|--------|-------|
| **Merged PRs (Web)** | https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is%3Apr+is%3Amerged | GitHub web direct | ✅ Working | Only if API unavailable |
| **Open Issues (Web)** | https://github.com/chas-challenge-2026/avanza-team1/issues?q=is:open | GitHub web direct | ✅ Working | Only if API unavailable |
| **Project Repo home** | https://github.com/chas-challenge-2026/avanza-team1 | GitHub web direct | ✅ Working | Navigation fallback only |

### OPTIONAL — Reference only (not required for presentations)

| Source | URL | Access Method | Status | Purpose |
|--------|-----|----------------|--------|---------|
| **Project Board** | https://github.com/orgs/chas-challenge-2026/projects/31 | GitHub Connector | ⚠️ Untested | Can be derived from Issues if needed |
| **Context Engineering repo** | https://github.com/zaida-wiss/context_enginering | GitHub Connector | ✅ Working | This documentation repository |

---

## 🔧 Utilities & Tools

| Tool | Purpose | URL |
|------|---------|-----|
| WebAIM Contrast Checker | WCAG AA/AAA text contrast validation | https://webaim.org/resources/contrastchecker/ |
| Localhost | Local development server | http://localhost:3000 |

---

## 📝 How to Use This File

**RULE:** Never hardcode external IDs or URLs. Instead:

1. ✅ **Always reference this file** — e.g., "See [Google Sheets (Project Fallback)](EXTERNAL_SOURCES.md#sheet-1-project-data-fallback)"
2. ✅ **Use variable names** — refer to "PROJECT_DATA_SHEET_ID" not raw ID
3. ✅ **Update this file first** — if any external source URL changes, update HERE and everywhere links to it will update
4. ❌ **Never copy/paste IDs** into other files

---

**Last updated:** 2026-09-14  
**Maintained by:** Team process maintainer  
**Linked from:** DATA_SOURCES.md, MANDATORY_READING_ORDER.md, presentations data collection guides
