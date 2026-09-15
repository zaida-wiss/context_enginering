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

## 📋 Google Sheets (Fallback Data)

### Sheet 1: Project Data Fallback (Commits, PRs, Issues, Board)
**Primary:** GitHub  
**Fallback:** Google Sheets

| Format | URL |
|--------|-----|
| **View** | https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/ |
| **CSV Export** | https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/export?format=csv |
| **Excel Export** | https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/export?format=xlsx |

**Sheet ID:** `1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI`

**Tabs/GIDs:**
- Commits: `gid=743460023`
- Issues: `gid=77162861`
- PRs: `gid=743460023`
- Project Board: `gid=869242669`

---

### Sheet 2: Risk & Asset Register (Risk Management)
**Primary:** Team Risk Register (project-maintained)  
**Fallback:** Google Sheets

| Format | URL |
|--------|-----|
| **View** | https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/ |
| **CSV Export — Risks** | https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=1796827285 |
| **CSV Export — Assets** | https://docs.google.com/spreadsheets/d/1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F/export?format=csv&gid=684132349 |

**Sheet ID:** `1A8XHxyAdbyrWlHSWTNgtwkKACdSiUr3F`

**Tabs/GIDs:**
- Risk-Management: `gid=1796827285`
- Assets: `gid=684132349`

---

## 📄 Google Docs

### Meeting Protocol & Decisions
**Primary:** Google Docs (real-time editable)

| Format | URL |
|--------|-----|
| **View & Edit** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit |
| **TXT Export** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt |
| **PDF Export** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=pdf |
| **HTML Export** | https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=html |

**Doc ID:** `1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8`

**Purpose:** Mötesprotokollet — weekly sprint planning decisions, blockers, action items

---

## 🔗 GitHub Sources

### Primary
| Resource | URL |
|----------|-----|
| **Project Repo** | https://github.com/chas-challenge-2026/avanza-team1 |
| **Issues (ALL)** | https://github.com/chas-challenge-2026/avanza-team1/issues?q=is%3Aissue |
| **Issues (OPEN)** | https://github.com/chas-challenge-2026/avanza-team1/issues?q=is:issue+is:open |
| **Pull Requests (ALL)** | https://github.com/chas-challenge-2026/avanza-team1/pulls |
| **Merged PRs (API — CANONICAL)** | https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?state=closed&base=develop&per_page=100 |
| **Merged PRs (API — notes)** | Filter by merged_at ≠ null and within REPORTING_PERIOD. Use assignees[] for work owner attribution. Paginate until < 100 results. |
| **Merged PRs (Web fallback)** | https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is%3Apr+is%3Amerged |
| **Merged PRs (Repo home)** | https://github.com/chas-challenge-2026/avanza-team1 → navigate to /pulls tab |

### Project Board & Fallback
| Resource | Primary | Fallback | Notes |
|----------|---------|----------|-------|
| **Project Board** | https://github.com/orgs/chas-challenge-2026/projects/31 | Issues URL (above) | If Board API unavailable → read Issues directly |
| **Merged PRs** | `pulls?q=is:pr+is:merged+merged:>=[DATE]` | [All merged PRs](https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is%3Apr+state%3Amerged) → then filter by date | If date filter fails → use all-merged link, then manually filter by week |
| **Commits** | GitHub commits API | Sheets commits tab | If API unavailable → Sheets data |

### Reference
| Resource | URL |
|----------|-----|
| **Context Engineering** | https://github.com/zaida-wiss/context_enginering |

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
