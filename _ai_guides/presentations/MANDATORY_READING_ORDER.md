---
name: mandatory_reading_order
description: Exact order AI must read files before rendering presentation — NO EXCEPTIONS
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER — INNAN PRESENTATION RENDERAS

**DENNA FIL MÅSTE LÄSAS FÖRE PRESENTATION.**

**Om denna ordning inte följs → presentation blir inkomplett eller bryter mot regler.**

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

- [ ] Branches från develop — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/branches`
  
- [ ] Commits denna vecka — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/commits/develop`
  
- [ ] **CLOSED ISSUES denna vecka** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/issues?q=is:closed+closed:2026-09-06..2026-09-13`
  
- [ ] **MERGED PRs denna vecka** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is:merged+merged:2026-09-06..2026-09-13`
  
- [ ] **PR DETAILS (review/approval info)** — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/pull/[PR_NUMBER]`
  Hämta för varje merged PR: approver, commits, linked issues
  
- [ ] Open PRs med aktivitet — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/pulls`
  
- [ ] Open issues med aktivitet — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/chas-challenge-2026/avanza-team1/issues`
  
- [ ] Project Board status — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://github.com/orgs/chas-challenge-2026/projects/31/views/1`
  Fallback: Använd PR/issue status från GitHub istället
  
- [ ] Meeting protocol denna vecka — LIVE_VERIFIED eller FALLBACK_VERIFIED
  URL: `https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt`
  
- [ ] DoD denna vecka — LIVE_VERIFIED eller FALLBACK_VERIFIED
  Källa: PR descriptions + review approvals (från PR DETAILS ovan)
  
- [ ] Team roster — LIVE_VERIFIED + IDENTITY_VERIFIED
  File: `_ai_guides/presentations/data/TEAM_ROSTER.md`

**Om NÅGON källa är MISSING:** → STOPP. Gör inte presentation.
**Om någon team-medlem inte kunde IDENTITY_VERIFIED:** → STOPP. Gör inte presentation.

---

### STEG 3: FÖRSTÅ STRUKTUR & REGLER & VISUELL DESIGN (10 min — nu kan du läsa detta)

#### 3a. structure/PRESENTATION_STRUCTURE.md
   - De 14 mötespunkterna
   - Vad varje punkt ska innehålla
   - Obligatoriska element per punkt

#### 3b. content/PRESENTATION_SPEC.md
   - Vad sliderna måste innehålla
   - Färg-semantik
   - Issue-format

#### 3c. design/PRESENTATION_CONSISTENCY_FRAMEWORK.md
   - Visuell konsistens
   - Röda trådar
   - Varning-signaler

#### 3d. **design/VISUAL_DESIGN_MANDATORY.md** ← 🚨 KRITISK
   - SYMBOL + FÄRG + TEXT (denna ordning)
   - NPF/dyslexia-vänlig design
   - PowerPoint-implementering
   - WCAG-kontrast

---

## FASE 2: DESIGN & FORM (5 min)

Dessa styr VISUELLa regler.

### 4. **design/PRESENTATION_STYLE.md**
   - Färger (semantisk BARA)
   - Typografi
   - Layout
   - NPF-regler

### 5. **design/PRESENTATION_CONSISTENCY_FRAMEWORK.md**
   - Visuell konsistens
   - Innehålls-konsistens
   - Röda trådar
   - Varning-signaler

### 6. **design/DESIGN_AUTHORITY.md**
   - Designkällor
   - Vad måste åsidosättas från verktyg-defaults

---

## FASE 3: INNEHÅL PER PUNKT (10-15 min)

Läs den relevanta för vilken punkt du bygger.

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

