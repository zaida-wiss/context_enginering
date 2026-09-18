---
name: sources_guide
description: "Guide to registered external sources (see SOURCES.yaml for authoritative registry)"
metadata:
  type: reference
  critical: true
---

# 🔗 External Sources — ALLOWLIST & REGISTRY

**🚨 CRITICAL:** Presentation generation ONLY uses registered sources. No web search. No unregistered websites.

## Single Source of Truth

**All URLs, IDs, access methods, and classifications are defined in:**  
→ **[`data/SOURCES.yaml`](data/SOURCES.yaml)** ← AUTHORITATIVE REGISTRY

This file (SOURCES.md) is a **human-friendly guide**. For machine-readable definitions, always reference SOURCES.yaml.

---

## 📋 Classification Overview

See **SOURCES.yaml** for complete registry.

**REQUIRED sources** (presentation STOPS if unavailable):
- GitHub API: Merged PRs, Open Issues  
- Local file: Team Roster

**FALLBACK sources** (try if primary fails):
- GitHub web: Merged PR page, Issues page
- Google Sheets: Project data (requires Google Connector)
- Google Docs: Meeting protocol (requires Google Connector)

**OPTIONAL sources** (nice-to-have, do not block):
- GitHub Project Board
- Risk & Asset register (Google Sheets)

## 🚀 How to Reference External Sources

**DO THIS:**
```yaml
source_id: "GITHUB_MERGED_PRS"
reference: "See SOURCES.yaml: GITHUB_MERGED_PRS"
```

**DO NOT DO THIS (examples of what NOT to do):**
```yaml
# ❌ WRONG: Hardcoded raw URL instead of source_id
url: "https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?..."

# ❌ WRONG: Hardcoded raw sheet ID instead of source_id
sheet_id: "1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI"
```

**The registry owns all URLs and IDs. Reference by source_id only.**

---

**Last updated:** 2026-09-18  
**Maintained by:** Team process maintainer  
**Linked from:** DATA_SOURCES.md, MANDATORY_READING_ORDER.md, presentations data collection guides
