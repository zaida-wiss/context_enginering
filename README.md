# 📱 Avanza Team 1 — Context & Process Documentation

**🚨 INSTRUCTION AUTHORITY FOR AI WORK**

This repository (`context_enginering`) is the **sole source of truth** for:
- How AI should work on Avanza Team 1
- Which data sources are allowed
- How to build, verify, and deliver presentations
- Fallback chains, gates, and authority hierarchy

The project code repository (`avanza-team1`) contains:
- Project code, GitHub issues, pull requests, and project board
- Workflow documentation, architecture, and technical decisions
- **NOT** instructions for how AI should acquire or present data

**Do not derive AI workflow, presentation rules, or source authority from the project repository's README.**

**Team process, AI guidelines, and decision logs.**  
**Project code:** https://github.com/chas-challenge-2026/avanza-team1

🔗 **Alla externa datakällor:** Se [`_memory/EXTERNAL_SOURCES.yaml`](_memory/EXTERNAL_SOURCES.yaml) för maskinläsbar register (URLs, IDs, access methods, klassificeringar). Se [`_memory/EXTERNAL_SOURCES.md`](_memory/EXTERNAL_SOURCES.md) för människovänlig introduktion.

---

## 🚨 START HERE — Enligt vad du gör

### 👤 Jag gör vanligt arbete (kodning, issues, etc)
→ **[_memory/PROJEKTKONTEXT_AVANZA.md](_memory/PROJEKTKONTEXT_AVANZA.md)** ← MANDATORY
- HOW to work with this project
- WHERE to get data
- WHAT to do if something fails

### 🎨 Jag skapar en PRESENTATION
→ **[_ai_guides/presentations/MANDATORY_READING_ORDER.md](_ai_guides/presentations/MANDATORY_READING_ORDER.md)** ← START HERE
   - MANDATORY_READING_ORDER.md routes to SYSTEM_CONTRACT.yaml (the only authority for execution order)
   - Follow execution_sequence from SYSTEM_CONTRACT.yaml exactly
   - No presentation artifact may be generated before execution_receipt and data_audit gates pass
   
   **Version Consistency Policy:**
   1. Always read latest files from default branch (no SHA lockdown)
   2. Once a build starts (execution_receipt → data_audit → rendering), use consistent versions within that build
   3. If repo changes mid-build and you need to restart, read fresh from latest default branch
   4. This balances: (a) fixes/improvements visible immediately, (b) no rule-version churn within a single build

### 📚 Jag behöver projektinformation
→ **[_memory/README.md](_memory/README.md)** ← CENTRAL HUB
- Alla projektfakta, deadlines, standarder
- Auktoritativt för projektet

### 🤔 Jag vet inte var jag ska börja
→ **[_ai_guides/README.md](_ai_guides/README.md)** ← Navigationshub för alla guides

---

**För annat arbete:**

**Understanding the project?**
→ **[_memory/TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md)** + **[_memory/DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md)**

**Sharing with another AI?**
→ Link: https://github.com/zaida-wiss/context_enginering (they'll follow the README from top)

**Need help with code?**
→ Read **[_memory/PROJEKTKONTEXT_AVANZA.md](_memory/PROJEKTKONTEXT_AVANZA.md)** then project repo above

---


---

## 🚨 CRITICAL RULES — Överordnade

**For presentations:**
- ✅ **Följ: MANDATORY_READING_ORDER.md → SYSTEM_CONTRACT.yaml → execution_sequence**
- ✅ **Verifiera alla REQUIRED datakällor innan rendering** (se [`_memory/EXTERNAL_SOURCES.yaml`](_memory/EXTERNAL_SOURCES.yaml) för klassificering: REQUIRED/FALLBACK/OPTIONAL)
  - REQUIRED: GitHub API, local team roster → must succeed or STOP
  - FALLBACK: GitHub web, Sheets, Docs → try in order if primary fails
  - OPTIONAL: Project Board, Risk Register → nice-to-have if connector available
- ✅ Alla 7 teammedlemmar måste vara representerade

**For team members:**
- Se **[_memory/README.md](_memory/README.md)** för TEAMSTANDARDS, DEFINITION_OF_DONE, etc

**For AI guides & all other work:**
- Se **[_ai_guides/README.md](_ai_guides/README.md)** för navigation

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Meeting notes:** See `_memory/EXTERNAL_SOURCES.yaml` (GOOGLE_MEETING_PROTOCOL source_id)

---

---

**Last updated:** 2026-09-14 — Orchestration fixed: single execution path for all  
**Team repos:**
- Team process & AI guides: https://github.com/zaida-wiss/context_enginering
- Project code: https://github.com/chas-challenge-2026/avanza-team1
