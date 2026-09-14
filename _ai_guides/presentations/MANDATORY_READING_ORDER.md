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

## 🚀 AI EXECUTION WORKFLOW — DENNA ORDNING MÅSTE FÖLJAS

**DENNA FIL SÄGER DEN EXAKTA ORDNINGEN för AI:**

👉 **LÄS FÖRST:** [AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)

Den filen säger:
- FASE 1: Datainsamling & Identity verification → RAPPORT
- FASE 2: Render gate check → RAPPORT
- FASE 3: Bygga presentation & final verification → RAPPORT
- Människan ser ALLA rapporter FÖRE presentationen

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

### STEG 1: LÄSA INSTRUKTIONER (5 min — MÅSTE göras först)

#### 1a. README.md (denna mapp)
   - Vad är presentations-systemet?
   - Var finns vad?

#### 1b. DATA_COLLECTION_MANDATORY.md (denna mapp)
   - INNAN något annat — läs detta
   - Checklista för komplett datainsamling
   - Fallback-hierarki
   - Render-gate (slides får INTE genereras utan denna)

#### 1c. data/DATA_SOURCES.md (denna mapp)
   - Vilka sources finns för varje datatyp
   - Fallback-ordning
   - Canonical URLs

#### 1d. data/TEAM_ROSTER.md (denna mapp)
   - Vilka är de 7 team-medlemmarna
   - Coverage-validation

---

### STEG 2A: IDENTITY VERIFICATION (5 min — FÖRE datainsamling)

🚨 **DETTA STEG MÅSTE GÖRAS FÖRE STEG 2B — annars kan team-medlemmar försvinna**

**IDENTITY RESOLUTION GATE:**

För varje team-medlem i TEAM_ROSTER.md:
- [ ] Verifiera Display Name
- [ ] Verifiera verifierad email (från git commits)
- [ ] Verifiera GitHub handle (från commits, INTE gissat)
- [ ] Dokumentera några exempel-commits från denna medlem

**REGEL: GitHub-handlenamn får ALDRIG konstrueras från personens namn.**

Exempel på FEL matching:
- ❌ Erik Berglund → "erik-backend" (gissat)
- ❌ Rasha Knifdi → "rasha-dev" (gissat)
- ✅ Erik Berglund → verifierad från commits som "rikexhx" eller "Svartakatten"

**Om någon medlem INTE kan matchas:**
- Rapportera: "Identity unresolved for X — investigate commit history"
- STOPP — rendering tillåts INTE

---

### STEG 2B: SAMLA ALL DATA (10-30 min — EFTER identity verification)

**Denna steg måste slutföras FULLSTÄNDIGT innan du går vidare.**

- [ ] **Branches från develop** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  PRIMARY URL: `https://github.com/chas-challenge-2026/avanza-team1/branches`
  FALLBACK: GitHub web-sida (WebFetch compatible)
  DATA NEEDED: branch names, last commit date, last contributor
  
- [ ] **Commits denna vecka (sept 6-13)** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  PRIMARY URL: `https://github.com/chas-challenge-2026/avanza-team1/commits/develop`
  FILTER: commits from Sept 6-13, 2026
  FALLBACK: GitHub web history, then git log from local repo
  DATA NEEDED: author, date, message, linked issues/PRs per commit
  
- [ ] **CLOSED ISSUES denna vecka** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/issues?q=is:closed+closed:2026-09-06..2026-09-13`
  
- [ ] **MERGED PRs denna vecka** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is:merged+merged:2026-09-06..2026-09-13`
  
- [ ] **PR DETAILS (review/approval info)** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/pull/[PR_NUMBER]`
  Hämta för varje merged PR: approver, commits, linked issues
  
- [ ] **OPEN PRs denna vecka (NULÄGE)** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  PRIMARY URL: `https://github.com/chas-challenge-2026/avanza-team1/pulls`
  DATA NEEDED PER PR:
    • PR-nummer
    • Titel
    • Författare (GitHub handle)
    • Vilka reviewers är assignerade? (KRITISK — ofta tomt)
    • Status: open/draft/ready for review
    • Länkade issues (#XX)
    • Skapningsdatum
  PRESENTATION USE: Slide ①D eller ②A — visa vad som väntar på review/merge
  
- [ ] **OPEN ISSUES denna vecka (NULÄGE)** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  PRIMARY URL: `https://github.com/chas-challenge-2026/avanza-team1/issues`
  DATA NEEDED PER ISSUE:
    • Issue-nummer
    • Titel
    • Assignerad till (vem jobbar med det?)
    • Labels (team-område: frontend, backend, native)
    • Status (öppen, pågår)
    • Uppdaterad senast (när var senaste aktivitet?)
  PRESENTATION USE: Slide ①D — visa aktiv arbete per team-medlem
  SORTERING: Sortera per assignee för att se vem som jobbar med vad
  
- [ ] **COMMITS DENNA VECKA (FAKTISK ARBETE)** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  PRIMARY URL: `https://github.com/chas-challenge-2026/avanza-team1/commits/develop`
  FILTER: Senaste 7 dagar
  DATA NEEDED PER COMMIT:
    • Datum
    • Författare (GitHub handle + namn)
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

### STEG 3: FÖRSTÅ STRUKTUR & REGLER & VISUELL DESIGN (20 min — KRITISK LÄSNING)

**🚨 DESSA FEM FILER MÅSTE LÄSAS I DENNA ORDNING:**

#### 3a. [design/SLIDE_DETAIL_SPEC.md](design/SLIDE_DETAIL_SPEC.md) — 🚨 AUTHORITATIVE (LÄS FÖRST!)
   - **EXAKT innehål för VARJE SLIDE (①-⑭)**
   - **KOLUMNER per slide** (Issue # | Titel | Assignad | Status | Merged/Branch)
   - **DATA-SOURCES per slide** (varifrån hämtas data?)
   - **MÅSTE/FÅR INTE innehålla** (regler per slide)
   - **FOOTER per slide** (vad ska stå längst ned?)
   - **REGLER för sortering, filtrering, visuell markering**
   - ⚠️ **KRITISK:** Om denna fil säger X och en annan fil säger Y → denna fil VINNER
   - **LÄNK:** Denna fil säger EXAKT format för VARJE SLIDE

#### 3b. [structure/PRESENTATION_STRUCTURE.md](structure/PRESENTATION_STRUCTURE.md) — OBLIGATORISK
   - De 14 mötespunkterna (①-⑭) i logisk ordning: retrospekt → status → plan → åtgärd
   - Ny ordning: Avklarat → Nuläge → Teams → Blockers → Risker → Kapacitet → Prioritering → Tekniska beslut → Sprintmål → Sprintplan → Nästa steg → Frågor
   - Vad varje punkt **MÅSTE** innehålla
   - Vilka data-kilder att hämta
   - Varje punkt kan ha 1-3+ slides
   - Obligatoriska element per punkt
   - **LÄNK:** Här säger vi VILKA GitHub-URLs att använda

#### 3c. [design/VISUAL_DESIGN_MANDATORY.md](design/VISUAL_DESIGN_MANDATORY.md) — 🚨 KRITISK (LÄS TIDIGT!)
   - SYMBOL + FÄRG + TEXT (denna ordning)
   - NPF/dyslexia-vänlig design
   - PowerPoint konkreta inställningar
   - WCAG AA kontrast (4.5:1 minimum)
   - Font-storlekar för tabeller
   - **LÄNK:** Här säger vi HUR (visuellt) slidorna ska se ut

#### 3d. [content/PRESENTATION_SPEC.md](content/PRESENTATION_SPEC.md) — OBLIGATORISK
   - Issue-format (TVINGANDE)
   - Färg-semantik (strikt regel)
   - Risk/Blocker/Dependency-definitioner
   - Preflight-validator
   
#### 3e. [design/PRESENTATION_FORMAT_GUIDE.md](design/PRESENTATION_FORMAT_GUIDE.md) — REFERENS (GAMMAL)
   - ⚠️ DEPRECATED: Många regler överlappar SLIDE_DETAIL_SPEC.md
   - DENNA FIL MÅ UPPDATERAS eller RADERAS för att undvika konflikter
   - **LÄS INTE DENNA innan du läst 3a-3d ovan**

---

## FASE 2: RÖDA TRÅDAR & DESIGN AUTHORITY (5 min)

### 4. **design/PRESENTATION_RED_THREADS.md** — NYTT (LÄSGRÄS DENNA)
   - Röda trådar (Arbete, Blockers, Risker, Kapacitet)
   - Varning-signaler (vad saknas = presentationen är felaktig?)
   - Checklista för röda trådar
   - Exempel på röda trådar i action

### 5. **design/PRESENTATION_STYLE.md**
   - Färger (semantisk BARA)
   - Typografi
   - Layout
   - NPF-regler

### 6. **design/DESIGN_AUTHORITY.md**
   - Designkällor (SLIDE_DETAIL_SPEC är #1)
   - Deprecated filer (PRESENTATION_CONSISTENCY_FRAMEWORK.md, PRESENTATION_FORMAT_GUIDE.md, etc)
   - Vad måste åsidosättas från verktyg-defaults

### ❌ DEPRECATED FILER (LÄS INTE DESSA)
   - ❌ `design/PRESENTATION_CONSISTENCY_FRAMEWORK.md` — gamla kolumn-regler, använd SLIDE_DETAIL_SPEC.md istället
   - ❌ `design/PRESENTATION_FORMAT_GUIDE.md` — använd SLIDE_DETAIL_SPEC.md och VISUAL_DESIGN_MANDATORY.md istället
   - ❌ `design/PRESENTATION_DESIGN_SPEC.md` — använd VISUAL_DESIGN_MANDATORY.md och DESIGN_AUTHORITY.md istället

---

## FASE 3: INNEHÅL PER PUNKT (10-15 min)

**HUVUDKÄLLA:** SLIDE_DETAIL_SPEC.md innehåller ALLT. Dessa är referensfiler.

### 7. **content/PRESENTATION_SPEC.md**
   - ALLA regler för innehål
   - Issue-format
   - Färger och status
   - NO META-INSTRUCTIONS on slides
   - PROJECT LEAD REVIEW checklist

### 8. **models/WEEKLY_PROGRESS_MODEL.md**
   - Två slides för ① (Levererat + Byggde vidare)
   - Hur klassificera arbete

### 9. **models/REPO_FIRST_RECONSTRUCTION.md**
   - Varför repo-first (inte issue-first)
   - Mekaniska regler

**Notering:** WEEKLY_PROGRESS_MODEL.md och REPO_FIRST_RECONSTRUCTION.md kan överlappar med SLIDE_DETAIL_SPEC.md. Om det finns en konflikt → SLIDE_DETAIL_SPEC.md VINNER.

---

## FASE 4: DATA & KÄLLOR (5 min)

Läs detta INNAN du försöker samla data.

### 10. **data/DATA_SOURCES.md**
   - Vilken information behövs
   - Fallback-ordning
   - Canonical URLs
   - Failure handling

### 11. **data/TEAM_ROSTER.md**
   - Vem tillhör vilka team
   - Coverage validation
   - Alla team-medlemmar måste kontrolleras

### 12. **data/SOURCE_CHECK.md**
   - Hur verifiera att data är från rätt källa
   - Timestamps
   - GitHub-länk struktur

---

## FASE 5: VERIFIERING (5 min)

Läs innan du renderar final version.

### 13. **verification/VERIFICATION_SYSTEM.md**
   - QA-process
   - Vad kontrollera

### 14. **verification/VERIFICATION_THIS_WEEK.md**
   - Denna veckas specifika verifiering
   - Vilka rules gäller nu

---

## 🚨 RENDER GATE — PRESENTATION FÅR INTE GENERERAS UTAN DETTA

**Före rendering, verifiera att ALLA dessa är LIVE_VERIFIED eller FALLBACK_VERIFIED:**

```
RENDER_GATE_CHECKLIST (10 SOURCES + 2 DESIGN RULES + 2 QA CHECKS):

DATA SOURCES (dessa 9 måste verifiera):
  ☐ Branches (develop) — status?
  ☐ Commits denna vecka — status?
  ☐ Merged PRs — status?
  ☐ Open PRs med aktivitet — status?
  ☐ Open issues med aktivitet — status?
  ☐ Project Board — status?
  ☐ Meeting protocol — status?
  ☐ DoD — status?
  ☐ Team roster — status? + IDENTITY_VERIFIED?

DESIGN RULES (MÅSTE LÄSAS):
  ☐ VISUAL_DESIGN_MANDATORY.md — Läst & förstått
     (Symbol + Färg + Text, NPF/dyslexia-vänligt)
  ☐ TEAM_ROSTER.md — IDENTITY VERIFICATION completed for all 7 members

QA CHECKS (MÅSTE PASSERAS):
  ☐ TEAM COVERAGE CHECK:
     Active roster: 7 (Tomac, Björn, Zaida, Erik, Rasha, Pär, Henrik)
     People represented in presentation: ?
     Missing: ? (måste vara 0)
     
  ☐ UNKNOWN NAME CHECK:
     Scan entire presentation for human names.
     Every name MUST exist in TEAM_ROSTER.
     Unknown names: ? (måste vara 0)

FAILURE CRITERIA:
  ❌ Any data source MISSING → RENDER GATE CLOSED
  ❌ Any team member NOT identity-verified → RENDER GATE CLOSED  
  ❌ TEAM COVERAGE < 7 → RENDER GATE CLOSED (someone missing)
  ❌ UNKNOWN NAMES > 0 → RENDER GATE CLOSED (example names in presentation)
  ❌ VISUAL_DESIGN not read → RENDER GATE CLOSED

SUCCESS CRITERIA:
  ✅ All 9 data-sources VERIFIED
  ✅ All 7 team members IDENTITY_VERIFIED
  ✅ TEAM COVERAGE = 7/7
  ✅ UNKNOWN NAMES = 0
  ✅ VISUAL_DESIGN read & understood
  
  → RENDER GATE OPEN → OK to generate slides
```

**DENNA GATEN ÄR OBLIGATORISK. INGEN UNDANTAG. DESSA QA-CHECKS ÄR MÅSTA-FEL.**

---

## 🚨 UNKNOWN_NAME_GATE — FINAL VERIFICATION (innan output)

**INNAN presentationen levereras måste denna sista gate passeras:**

```
UNKNOWN_NAME_GATE:

1. Extract every human name from the final presentation
   (Ctrl+F search för första/efternamn-mönster)

2. For EACH name found:
   ☐ Exists in TEAM_ROSTER.md active members? 
   
3. Allowed names ONLY:
   ✅ Tomac Barin Jansson
   ✅ Björn Boman
   ✅ Zaida Wiss
   ✅ Erik Berglund (also "rikexhx", "Svartakatten")
   ✅ Rasha Knifdi
   ✅ Pär Lundh
   ✅ Henrik Westerlund

4. NOT allowed names (render FAIL):
   ❌ <EXAMPLE_MEMBER_A/B/C/D/E> (placeholder names)
   ❌ Lisa, Marco, Ali, Anna, Jan (example names)
   ❌ Any other human name not in TEAM_ROSTER

FAILURE CRITERIA:
  If ANY unknown name found → presentation is INVALID
  Remove the name or verify it against TEAM_ROSTER
  Do NOT render unknown names
  
PASS CRITERIA:
  Only names from TEAM_ROSTER display names (or aliases like "Svartakatten" for Erik)
  Zero example placeholder names
  → OK to output presentation
```

**DENNA GATE MÅSTE PASSERAS. INGEN UNDANTAG.**

---

## 🎬 STEG 4: RENDER PRESENTATION (20-30 min — EFTER ALLA GATES)

**🚨 KRITISK REGEL: PRESENTATION = BARA ARBETESRESULTAT, INTE AI-PROCESS**

Efter att RENDER_GATE_CHECKLIST och UNKNOWN_NAME_GATE har **PASSERAT**:

### ✅ RENDER DESSA SLIDES (från [PRESENTATION_STRUCTURE.md](structure/PRESENTATION_STRUCTURE.md)):

**Se [PRESENTATION_STRUCTURE.md](structure/PRESENTATION_STRUCTURE.md) för AUKTORITATIV definition av alla 14 mötespunkter (①-⑭).**

Kort översikt:
- ① SEDAN FÖRRA MÖTET (1-2 slides)
- ② SPRINTMÅL (1 slide)
- ③ NULÄGE (1 slide)
- ④-⑥ TEAM-SLIDES: Frontend, Backend, Native (1-3 slides var)
- ⑦ BEROENDEN & BLOCKERS (1-2 slides)
- ⑧ PRIORITERING & SCOPE (1-2 slides)
- ⑨ KAPACITET & ESTIMERING (1 slide)
- ⑩ RISKER (1-2 slides)
- ⑪ TEKNISKA BESLUT (1 slide)
- ⑫ SPRINTPLAN (1-2 slides)
- ⑬ NÄSTA STEG (1-2 slides)
- ⑭ FRÅGOR TILL PL (1 slide)

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

