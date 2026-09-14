---
name: mandatory_reading_order
description: Exact order AI must read files before rendering presentation — NO EXCEPTIONS
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER — INNAN PRESENTATION RENDERAS

**DENNA FIL MÅSTE LÄSAS FÖRE PRESENTATION.**

🔗 **NOTE:** Alla externa URLs (Google Sheets, Google Docs, GitHub) är centraliserade i [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md). Se den filen för aktuella IDs och fallback-URLs.

**Om denna ordning inte följs → presentation blir inkomplett eller bryter mot regler.**

---

## 🚨 KRITISK REGEL #0 — LÄSA INSTRUKTIONER ≠ VISA INSTRUKTIONER

**INNAN du läser NÅGOT annat:**

```
⭐ DENNA REGEL ÄR TVINGANDE ⭐

Du ska LÄSA dessa instruktioner för att FÖRSTÅ vad presentationen behöver.
Du ska ANVÄNDA dessa instruktioner för att BYGGA presentationen.
Du ska ALDRIG VISA dessa instruktioner ON SLIDES.

EXEMPEL:

🔴 FEL:
  Slide visar: "Repo-first: visa bara det som går att koppla till PR, commit..."
  Slide visar: "Måste räknas mot develop"
  Slide visar: "Ej live-låst här"
  → Dessa är instruktioner för DIG, inte innehål för mötet

✅ RÄTT:
  Slide visar: "#95 Security review · Zaida · ✓ DONE · merged 2026-09-13"
  Slide visar: "🔴 API-kontrakt inte låst — Frontend blockerad"
  Slide visar: "Backend måste leverera API-spec idag"
  → Dessa är RESULTAT av att följa instruktionerna

MECKANISK KONTROLL (efter rendering):
  För varje slide:
    Q: "Skulle en projektledare säga detta till teamet?"
    Ja → texten får vara på sliden
    Nej → ta bort texten

RENDER-GATE CHECK:
  ☐ Presentationen innehåller INGEN instruktioner?
  ☐ Presentationen innehåller INGEN checklista?
  ☐ Presentationen innehåller INGEN AI-process?
  
  Om något är NEJ → STOPP, ta bort det innan rendering
```

**Se även:**
- [PRESENTATION_SPEC.md — NO META-INSTRUCTIONS ON SLIDES](content/PRESENTATION_SPEC.md#L219)
- [RENDER_GATE_CHECKLIST.md — KRITISK: INGEN AI-INSTRUKTIONER PÅ SLIDES](verification/RENDER_GATE_CHECKLIST.md)

---

---

## 🚀 AI EXECUTION WORKFLOW — DENNA ORDNING MÅSTE FÖLJAS

**DENNA FIL SÄGER DEN EXAKTA ORDNINGEN för AI:**

👉 **LÄS FÖRST:** [AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)

Den filen säger:
- FASE 1: Datainsamling & Identity verification
- FASE 2: Render gate check
- FASE 3: Bygga presentation & final verification
- **AI gör ALLT — levererar presentation KLAR (ingen human-loop)**

**UTAN denna ordning → presentation blir felaktig eller ej verifierad.**

---

## 📚 SYSTEMÖVERSIKT — FÖRENKLAD ARKITEKTUR (NYT)

**Presentationssystemet är nu konsoliderat för att undvika konflikter:**

```
🎯 SOURCE OF TRUTH (Läs dessa):
  ├─ design/SLIDE_DETAIL_SPEC.md ⭐
  │  └─ "EXAKT innehål för VARJE SLIDE ①-⑭"
  │  └─ Kolumner, format, regler, data-sources, footer PER SLIDE
  │
  ├─ design/VISUAL_DESIGN_MANDATORY.md
  │  └─ "SYMBOL + FÄRG + TEXT, NPF-vänlig, PowerPoint-regler"
  │
  ├─ design/PRESENTATION_RED_THREADS.md ⭐ NYT
  │  └─ "Röda trådar, varning-signaler, checklista"
  │
  └─ design/DESIGN_AUTHORITY.md
     └─ "Designkällor, deprecated filer, vad vinner vid konflikt"

📚 REFERENSFILER (För kontext, INTE authoritative):
  ├─ structure/PRESENTATION_STRUCTURE.md
  │  └─ "14 mötespunkter i ordning"
  │
  ├─ content/PRESENTATION_SPEC.md
  │  └─ "Innehålls-regler, färg-semantik"
  │
  └─ data/DATA_SOURCES.md
     └─ "Vilka GitHub-URLs och fallback-sources"

🚫 DEPRECATED (LÄS INTE DESSA):
  ├─ design/PRESENTATION_CONSISTENCY_FRAMEWORK.md ❌
  │  └─ "Gamla kolumn-regler, använd SLIDE_DETAIL_SPEC.md istället"
  │
  ├─ design/PRESENTATION_FORMAT_GUIDE.md ❌
  │  └─ "Överflödiga, använd SLIDE_DETAIL_SPEC.md + VISUAL_DESIGN_MANDATORY.md istället"
  │
  └─ design/PRESENTATION_DESIGN_SPEC.md ❌
     └─ "Överflödiga, använd VISUAL_DESIGN_MANDATORY.md istället"
```

**REGEL: Om två filer säger olika saker → SLIDE_DETAIL_SPEC.md och VISUAL_DESIGN_MANDATORY.md VINNER.**

---

## 🚨 SINGLE EXECUTION SEQUENCE — ALDRIG FÖR IN DENNA ORDNING

**Du måste följa DENNA ordning. Avvikelse = presentation blir felaktig.**

**DENNA SEKVENS ÄR ABSOLUT OCH FÅR INTE ÄNDRAS:**

### STEG 1: LÄS DESSA FILER (i ordning)

**Läs INTE något mer — dessa filer säger allt:**

1. **[README.md](README.md)** — Vad är presentations-systemet?
2. **[monday_meeting/README.md](monday_meeting/README.md)** — 14 mötespunkter overview
3. **[monday_meeting/data/DATA_COLLECTION_MANDATORY.md](monday_meeting/data/DATA_COLLECTION_MANDATORY.md)** — Datainsamling & identity-verifikation
4. **[data/DATA_SOURCES.md](data/DATA_SOURCES.md)** — Vilka GitHub-URLs, fallback-ordning

**Sedan gå till STEG 2 (nedan).**

---

### STEG 2: VERIFIERA & RENDERA

**Läs dessa filer:**

1. **[verification/AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)** — AI gör ALLT (hämta → verifiera → leverera)
2. **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)** — KAN presentationen renderas?
3. **[monday_meeting/design/SLIDE_DETAIL_SPEC.md](monday_meeting/design/SLIDE_DETAIL_SPEC.md)** — EXAKT innehål per slide
    • Commit-meddelande (första raden)
    • Länkade PR-nummer (om någon)
    • Länkade issue-nummer (om någon)
  PRESENTATION USE: Slide ①D — visar vem som faktiskt gjort vad denna vecka
  VARNING: Om INGA commits denna vecka → teamet har inte pushat (möjligt blockeringsproblem)
  
- [ ] **Project Board status** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  PRIMARY URL: `https://github.com/orgs/chas-challenge-2026/projects/31/views/1`
  ⚠️ NOTE: This URL may return 404 or require auth via WebFetch
  MANDATORY FALLBACK: Rekonstruera status från:
    - GitHub Issues API (open/closed status)
    - GitHub PRs API (merged status)
    - Issue labels (status field)
  → Use PR/Issue status as source of truth instead of Project Board
  DATA NEEDED: Per issue: status (to do/in progress/done), priority, assignee
  
- [ ] **Meeting protocol denna vecka** — TRY → REPORT → FALLBACK (INTE blocker)
  PRIMARY URL: `https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt`
  
  **KRITISK REGEL: Mötesprotokollet är CONTEXT, inte DATA**
  
  🔴 OM du INTE kan nå det:
    → Rapportera: "Kunde inte nå mötesprotokollet. Kan du klistra in texten från mötet?"
    → VÄNTA på användarens svar
    → ELLER bygga presentationen utan detta (använd GitHub-data)
  
  ✅ FALLBACK (om mötet inte nås):
    - Använd GitHub Issues/PRs som faktisk källa
    - Använd möte-context från cache om tillgängligt
    - Presentationen renderas ÄNDÅ (mötet är inte obligatoriskt)
  
  DATA BEHÖVS (om tillgängligt): beslut fattade, blockers identifierade, action items, nästa prioriteter
  
- [ ] DoD denna vecka — LIVE_VERIFIED eller FALLBACK_VERIFIED
  Källa: PR descriptions + review approvals (från PR DETAILS ovan)
  
- [ ] Team roster — LIVE_VERIFIED + IDENTITY_VERIFIED
  File: `_ai_guides/presentations/data/TEAM_ROSTER.md`

**Om NÅGON källa är MISSING:** → STOPP. Gör inte presentation.
**Om någon team-medlem inte kunde IDENTITY_VERIFIED:** → STOPP. Gör inte presentation.

---

### STEG 3: DESIGN & SPECIFIKATION

**Läs DESSA filer (de innehåller ALLT):**

1. **[design/SLIDE_DETAIL_SPEC.md](monday_meeting/design/SLIDE_DETAIL_SPEC.md)** ⭐ AUKTORITATIV
   - EXAKT innehål för VARJE SLIDE (①-⑭)
   
2. **[design/VISUAL_DESIGN_MANDATORY.md](design/VISUAL_DESIGN_MANDATORY.md)** ⭐ DESIGN
   - Symbol + Färg + Text (NPF/dyslexia-vänlig)
   
3. **[structure/PRESENTATION_STRUCTURE.md](monday_meeting/structure/PRESENTATION_STRUCTURE.md)**
   - 14 mötespunkter (①-⑭) definitioner

**Om två filer motsäger varandra:** SLIDE_DETAIL_SPEC.md VINNER.

---

### STEG 4: VERIFIERA PRESENTATION FÖRE RENDERING

Läs: **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)**
- KAN presentationen renderas?
- 13 checkpoints MÅSTE passeras

### ❌ VISA INTE (detta är AI-instruktioner, inte möte-innehål):

- ❌ "Verifieringslåge innan status"
- ❌ "Team roster: 7 medlemmar verifierade"
- ❌ "GitHub PRs inte läsbart via API"
- ❌ "Render gate checklist"
- ❌ "Verification report"
- ❌ "Identity verification status"
- ❌ "Data collection status"
- ❌ "AI process information"

### ✅ ANVÄND DENNA DATA (men VISA INTE verifikations-info):

- Commits denna vecka → från data (VISA det faktiska arbetet)
- Merged PRs → från data (VISA vad som blev klart)
- Team roster (för att VERIFIERA namn) → VISA bara namn + arbete, inte "verifierat"
- Fallback-strategier → använd om primär källa failas, men VISA inte att fallback användes
- Data sources (GitHub) → ANVÄND dem för presentationen, VISA inte käll-status

### 🎯 MÖTE-PRESENTATIONEN ska visa:

✅ Vad som arbetades med denna vecka  
✅ Vem som var ansvarig för vad  
✅ Vad som blev klart  
✅ Vad som är pågår  
✅ Vad som blockerar oss  
✅ Nästa prioriteringar  

❌ INTE: AI-verifikations-process, data-samlings-status, eller verifikations-rapporter

---

## CRITICAL RULES SUMMARY

**Från denna läsning, dessa är NOT-negotiable:**

✅ **Data-insamling:** ALL data från GitHub denna vecka (repo-first)
✅ **VISUAL DESIGN:** 🚨 Symbol + Färg + Text (denna ordning, innan rendering)
   - NPF/dyslexia-vänligt
   - WCAG-kontrast (minimum 4.5:1)
   - DoD-status med ✅/◐/✕/? symbolen
   - Whitespace: minimum 8px mellan element
   - Font-size: minimum 12pt
✅ **Mötespunktsmarkörer:** Varje slide har 📝[NUM][TITLE] överst
✅ **Team-struktur:** Två slides per team (Var är vi? + Vad behöver vi göra?)
✅ **Färger:** Semantiska BARA (🟢 klart, 🟡 pågår, 🔴 blockerat, ⚪ neutral)
   - ALDRIG färg ensam (måste ha symbol + text)
   - ALDRIG dekorativ färg
✅ **Namn:** BARA verifierade namn från GitHub denna vecka
✅ **Issue-tabeller:** Issue | Vad | Ägare | Status | AC | Tests | Review | Docs | PR
✅ **Handlingsplan:** Fyra separata tabeller (arbete, väntar på, blockerar, risker)
✅ **Blockers:** Issue | Väntar på | Påverkar | Äger | Sannolikhet | Fallback
✅ **Risker:** Risk | Typ | Sannolikhet | Konsekvens | Åtgärd | Ansvar | Tid
✅ **DoD:** Läs från issue-description, ALDRIG gissat
✅ **Point ①:** ALLA PRs denna vecka, inget får utelämnas för plats
✅ **Point ⑪:** Sprintmål EFTER kapacitet och prioritering
✅ **Point ⑫:** Senior PL-granskning, plan-bedömning 🟢/🟡/🔴
✅ **Point ⑬:** Beslut → konkreta GitHub-åtgärder
✅ **VISUELL CHECKLIST:** Innan rendering — se VISUAL_DESIGN_MANDATORY.md

---

## DEPRECATED FILER (läs INTE dessa)

❌ SPRINT_PRESENTATION_STRUCTURE.md (old version)
❌ SPRINT_PROTOCOL_NUMBERED.md (old version)
❌ Gamla examples från innan-context-restructure

---

## VAD OM JAG INTE HINNER LÄSA ALLT?

**Minimum (10 min, 3 slides):**
1. README.md
2. DATA_COLLECTION_MANDATORY.md
3. PRESENTATION_STRUCTURE.md

**Rekomenderad (20 min, full presentation):**
1-5 ovan + PRESENTATION_SPEC.md + DATA_SOURCES.md + TEAM_ROSTER.md

**Full (30 min, senior presentation):**
Alla 1-14 ovan

---

## KONTROLL: Är du redo?

Innan du börjar rendera, svara på dessa:

```
Läst DATA_COLLECTION_MANDATORY.md?          [ ] Ja [ ] Nej — STOP om nej
Läst PRESENTATION_STRUCTURE.md?             [ ] Ja [ ] Nej — STOP om nej
Läst PRESENTATION_SPEC.md?                  [ ] Ja [ ] Nej — STOP om nej
Läst DATA_SOURCES.md?                       [ ] Ja [ ] Nej — STOP om nej
Läst TEAM_ROSTER.md?                        [ ] Ja [ ] Nej — STOP om nej
Läst PRESENTATION_CONSISTENCY_FRAMEWORK.md? [ ] Ja [ ] Nej — STOP om nej

Vet du vilka 7 team-medlemmar som finns denna vecka?  [ ] Ja [ ] Nej — STOP om nej
Vet du vilka 14 mötespunkter som finns?              [ ] Ja [ ] Nej — STOP om nej
Vet du reglerna för mötespunktsmarkörer?             [ ] Ja [ ] Nej — STOP om nej
Vet du fallback-hierarkin för data?                  [ ] Ja [ ] Nej — STOP om nej
```

**Om alla är Ja → du kan börja.**
**Om något är Nej → läs det filen först.**

---

**Denna fil uppdaterades:** 2026-09-13
**Senast följd:** [Du måste fylla detta innan rendering]

