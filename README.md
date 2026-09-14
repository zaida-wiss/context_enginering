# 📱 Avanza Team 1 — Context & Process Documentation

**Team process, AI guidelines, and decision logs.**  
**Project code:** https://github.com/chas-challenge-2026/avanza-team1

🔗 **Alla externa datakällor:** Se [`_memory/EXTERNAL_SOURCES.md`](_memory/EXTERNAL_SOURCES.md) för centraliserad register över Google Sheets, Google Docs, GitHub och alla fallback-URLs.

---

## 🚨 START HERE — Enligt vad du gör

### Om du gör ett vanligt arbete:
→ **[PROJEKTKONTEXT_AVANZA.md](_memory/PROJEKTKONTEXT_AVANZA.md)** ← MANDATORY
- HOW to work with this project
- WHERE to get data
- WHAT to do if something fails

### Om du skapar en PRESENTATION:
→ **STEG 1:** Läs [`_memory/README.md`](_memory/README.md) först (projektkontexten)  
→ **STEG 2:** Läs **[_ai_guides/presentations/MANDATORY_READING_ORDER.md](_ai_guides/presentations/MANDATORY_READING_ORDER.md)** ← ENDA körordningen
- Innehåller STEG 0 (läs _memory/) + STEG 1-4 (presentation)
- NPF/Dyslexia/Autism-vänlig design AUTOMATIC
- 14 mötespunkter, datainsamling, verifikation — allt här
- **DU BEHÖVER INTE SÖKA LÄNGRE** — följ bara denna ordning

### För all projektinformation (_memory/):
→ **[_memory/README.md](_memory/README.md)** ← CENTRAL HUB
- Alla projektfakta, deadlines, standarder
- Auktoritativt för projektet
- Länka till specifik fil från denna index

### För allt annat:
→ **[_ai_guides/README.md](_ai_guides/README.md)** ← Övriga guider

---

## 🎯 SINGLE EXECUTION PATH — INGEN ALTERNATIV:

```
AI MÅSTE följa denna ordning (ALDRIG något annat):

  1️⃣ Root README (denna fil)
  
  2️⃣ OM PRESENTATION:
     _ai_guides/presentations/MANDATORY_READING_ORDER.md
     ↓
     FRÅN DEN FILEN → SLIDE_DETAIL_SPEC (AI_READ_ORDER säger detta)
     FRÅN DEN FILEN → VISUAL_DESIGN_MANDATORY (AI_READ_ORDER säger detta)
     FRÅN DEN FILEN → RENDER_GATE_CHECKLIST (AI_READ_ORDER säger detta)
  
  3️⃣ OM PROJEKTINFO:
     _memory/README.md (central hub för alla projektkällor)

✅ Denna ordning är ABSOLUT — ingen annan ordning tillåten
✅ MANDATORY_READING_ORDER.md är ENDA körordningen för presentations
✅ Ingen fil ska läsa från fler än en plats samtidigt
```

**VIKTIG REGEL:** Om två filer säger olika saker → MANDATORY_READING_ORDER.md VINNER.

---

**För annat arbete:**

**Understanding the project?**
→ **[_memory/TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md)** + **[_memory/DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md)**

**Sharing with another AI?**
→ Link: https://github.com/zaida-wiss/context_enginering (they'll follow the README from top)

**Need help with code?**
→ Read **[_memory/PROJEKTKONTEXT_AVANZA.md](_memory/PROJEKTKONTEXT_AVANZA.md)** then project repo above

---

## 📚 Övriga filer (om du behöver dem)

**För kodning:**
- [_memory/TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md) — Git format, coding rules
- [_memory/DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md) — När är arbetet klart?
- [_memory/PROJEKTKONTEXT_AVANZA.md](_memory/PROJEKTKONTEXT_AVANZA.md) — Projekt-overview & AI-instruktioner

**För presentationer (läs MANDATORY_READING_ORDER.md — den säger allt):**
- Alla presentationsfiler länkas från MANDATORY_READING_ORDER.md
- Gå INTE direkt till dessa — följ ordningen i MANDATORY_READING_ORDER.md istället

---

## 🚨 CRITICAL RULES

**For presentations — DATA ACCESS:**
- ✅ Use ONLY these sources: GitHub (github.com), Google Docs/Sheets, raw.githubusercontent.com, GitHub API
- ❌ **NEVER use `git clone`, `git ls-remote`, or shell commands**
- ❌ **NEVER search Google/Bing/web for Avanza data** — this is a security boundary violation
- ❌ **NEVER use external APIs** (cryptocurrency exchanges, stock markets, blockchain explorers, etc.)
- ✅ Use GitHub Connector/API or web browser only
- ✅ If a source fails → use fallback URL (DATA_SOURCES.md), NOT web search

**For presentations — QUALITY:**
- Verify all data sources before rendering
- Ensure all 7 team members are represented and identity-verified
- No example names in output

**For team members:**
- Follow TEAMSTANDARDS for commits & code
- Read DEFINITION_OF_DONE before marking issues complete
- Decisions → BESLUT.md files (Frontend, Backend, Native)

**For AI building presentations:**
Read **MANDATORY_READING_ORDER.md** first. It contains:
- 4-step execution workflow (clear path to render)
- Data collection requirements
- Identity verification gate (7 team members)
- Render gate checklist (13 mandatory checkpoints)
- Design rules (Symbol + Färg + Text)
- Final verification before delivery

**CRITICAL RULE FOR AI — NO META-INSTRUCTIONS ON SLIDES:**
- 🚨 READ the instructions to UNDERSTAND what presentation needs
- 🚨 USE the instructions to BUILD the presentation
- 🚨 NEVER SHOW the instructions ON the slides themselves
- 🚨 Only show RESULTS (GitHub data, team status, decisions, blockers)
- 🚨 HIDE all AI-process, checklists, rules, and verification steps
  
See: [PRESENTATION_SPEC.md — NO META-INSTRUCTIONS ON SLIDES](_ai_guides/presentations/content/PRESENTATION_SPEC.md#L219)
See: [RENDER_GATE_CHECKLIST.md — KRITISK: INGEN AI-INSTRUKTIONER PÅ SLIDES](_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md)

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Meeting notes:** https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit

---

---

**Last updated:** 2026-09-14 — Orchestration fixed: single execution path for all  
**Team repos:**
- Team process & AI guides: https://github.com/zaida-wiss/context_enginering
- Project code: https://github.com/chas-challenge-2026/avanza-team1
