---
name: ai_verification_workflow
description: Explicit ordning för AI-verifikation FÖRE presentation visas — med rapport till människan
metadata:
  type: process
  critical: true
  required_before: rendering
---

# 🔍 AI VERIFICATION WORKFLOW — Innan Presentation Visas

**DENNA FIL SÄGER EXAKT ORDNINGEN för AI-verifikation.**

**Resultat: Människan ser RAPPORT (✅/❌) FÖRE presentationen, så hon/han vet vad som är verifierat.**

---

## 🚀 WORKFLOW I TRE FASER

### FASE 1: DATAINSAMLING & IDENTITETSVERIFIKATION (15-20 min)

**AI:s uppgift:**

```
Läs MANDATORY_READING_ORDER.md STEG 1-2:
  ✅ STEG 1: Instruktioner (5 min)
  ✅ STEG 2A: Identity verification (5 min)
  ✅ STEG 2B: Datainsamling (10-30 min)

För varje data-källa — NOTERA STATUS:
  ☐ Branches (develop)
  ☐ Commits denna vecka
  ☐ Merged PRs
  ☐ Open PRs
  ☐ Open issues
  ☐ Project Board
  ☐ Meeting protocol (Google Docs)
  ☐ DoD checklist
  ☐ Team roster

STATUS FÖR VARJE:
  ✅ LIVE_VERIFIED (hämtad från GitHub/web direkt)
  ⚠️ FALLBACK_VERIFIED (Google Sheets eller annat)
  ❌ NOT_FOUND (kan inte nå källan)
```

**AI:s rapport till människan EFTER FASE 1:**

```
═══════════════════════════════════════════════════════════
VERIFICATION REPORT — FASE 1: DATA & IDENTITY
═══════════════════════════════════════════════════════════

IDENTITY VERIFICATION (7 team members):
  ✅ Zaida Wiss (zaida-wiss) — verified from commits
  ✅ Björn Boman (bjorneboman) — verified from commits
  ✅ Tomac Barin Jansson (TomacBarin) — verified from commits
  ✅ Rasha Knifdi (rashaknifdi) — verified from commits
  ✅ Erik Berglund (rikexhx / Svartakatten) — verified from commits
  ✅ Pär Lundh (lundhpargmailcom / pargmailcom) — verified from commits
  ✅ Henrik Westerlund (Henrik-Westerlund) — verified from commits

DATA SOURCES VERIFICATION:
  ✅ Branches (develop) — LIVE_VERIFIED
     Last commit: 2026-09-13 by Erik
     Active branches: 5 (feature/*, bugfix/*)
     
  ✅ Commits denna vecka — LIVE_VERIFIED
     7 commits Sept 8-13 from 4 members (Zaida, Björn, Erik, Rasha)
     Range: Sept 6-13 (7 days)
     
  ✅ Merged PRs — LIVE_VERIFIED
     5 merged PRs this week
     (#95, #87, #80, ...)
     
  ✅ Open PRs — LIVE_VERIFIED
     3 open PRs waiting for review
     (#88, #89, ...)
     
  ✅ Open issues — LIVE_VERIFIED
     12 open issues, 5 new this week
     All have assignee
     
  ✅ Project Board — LIVE_VERIFIED
     52 items across columns
     Status matches git (verified)
     
  ⚠️ Meeting protocol — FALLBACK_VERIFIED
     Google Docs not accessible
     Will use: Slack summary + meeting notes from GitHub
     
  ✅ DoD checklist — LIVE_VERIFIED
     Read from: _memory/DEFINITION_OF_DONE.md
     All slides will check against this
     
  ✅ Team roster — LIVE_VERIFIED
     7 members, all identity-verified
     All verified from git commits (not guessed)

═══════════════════════════════════════════════════════════
RESULT: ✅ FASE 1 PASSED — OK to proceed to FASE 2
═══════════════════════════════════════════════════════════
```

---

### FASE 2: RENDER GATE VERIFICATION (5 min)

**AI:s uppgift:**

```
Före presentation byggs — PASS dessa 3 checks:

CHECK 1: DATA COMPLETENESS
  ✅ All 9 data sources accessible? (or have fallback)
  ✅ All 7 team members identity-verified?
  ✅ Any data MISSING? → STOP (report problem)

CHECK 2: TEAM COVERAGE
  Active roster: 7 members
  Expected in presentation: 7 (alla måste synas)
  Will presentation cover all 7? YES/NO?
  ☐ If NO → STOP (figure out who's missing, why)
  
CHECK 3: DESIGN RULES UNDERSTOOD
  ✅ Read VISUAL_DESIGN_MANDATORY.md?
  ✅ Understood Symbol + Färg + Text?
  ✅ Read ACCESSIBILITY_NEURODIVERSITY.md?
  ☐ If NO → go read it before building slides
```

**AI:s rapport till människan EFTER FASE 2:**

```
═══════════════════════════════════════════════════════════
RENDER GATE CHECKLIST — PASS/FAIL
═══════════════════════════════════════════════════════════

DATA COMPLETENESS:
  ✅ All 9 sources verified or fallback available
  ✅ All 7 team members identity-verified from git
  ✅ No critical missing data

TEAM COVERAGE:
  Active members: 7
  Will show in presentation: 7 (all with work or "Ingen issue denna vecka")
  Coverage: 7/7 ✅

DESIGN RULES:
  ✅ Symbol + Färg + Text rules understood
  ✅ Dyslexi/ADHD-vänlighet understood
  ✅ Color semantics: 🟢 done, 🟡 pågår, 🔴 blocked, ⚪ unknown
  ✅ Whitespace: 6-8px zwischen issues, 12px mellan färgbar+text
  ✅ Font sizes: 28pt title, 14pt content, 24px line-height

═══════════════════════════════════════════════════════════
RESULT: ✅ RENDER GATE PASSED — OK to build presentation
═══════════════════════════════════════════════════════════
```

---

### FASE 3: PRESENTATION BUILDING & FINAL VERIFICATION (20-40 min)

**AI:s uppgift:**

```
Nu börja bygga presentationen enligt:
  PRESENTATION_STRUCTURE.md (14 mötespunkter)
  PRESENTATION_FORMAT_GUIDE.md (konkreta slide-layouts)
  VISUAL_DESIGN_MANDATORY.md (fonts, colors, spacing)

UNDER BUILDING:
  ☐ Varje slide verifieras mot DATA:
     - Är datum från faktisk develop-merge?
     - Är issue-status korrekt i GitHub?
     - Är assignee korrekt?
     - Finns AC (Acceptance Criteria)?
     - Finns test-coverage?
     - Finns PR-review status?
     
  ☐ Innan output — SCANNA för okända namn:
     - Vilka namn förekommer i presentationen?
     - Existerar de i TEAM_ROSTER.md?
     - Noll okända namn tillåtet
     
  ☐ Innan output — KONTROLLERA design:
     - Färger: bara 🟢🟡🔴⚪ (status-färger, inte dekoration)
     - Symboler: ✅◐✕?→ (samma betydelse överallt)
     - Whitespace: tillräckligt för ADHD-fokus?
     - Typografi: rätt hierarki (28pt → 14pt → 13pt)?
```

**AI:s rapport INNAN presentationen visas:**

```
═══════════════════════════════════════════════════════════
FINAL VERIFICATION REPORT — Presentation Ready
═══════════════════════════════════════════════════════════

SLIDES GENERATED:
  Total slides: 24
  Mötespunkter representerade: ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭
  All 7 team members shown: YES ✅

DATA VERIFICATION (per slide):
  Slide ①A (Frontend denna vecka):
    ✅ Merged PRs match GitHub develop-merge
    ✅ All assignees exist in TEAM_ROSTER
    ✅ Dates match actual merge-dates
    
  Slide ①B (Backend denna vecka):
    ✅ Issue #95, #87 match GitHub status
    ✅ Assignee Erik (rikexhx) verified
    ⚠️ Issue #80 — test-coverage not yet added (marked "pågår")
    
  [... per slide ...]

NAME VERIFICATION:
  Names found in presentation:
    ✅ Zaida Wiss — exists in TEAM_ROSTER
    ✅ Björn Boman — exists in TEAM_ROSTER
    ✅ Erik Berglund — exists in TEAM_ROSTER
    ✅ Rasha Knifdi — exists in TEAM_ROSTER
    ✅ Tomac Barin Jansson — exists in TEAM_ROSTER
    ✅ Pär Lundh — exists in TEAM_ROSTER
    ✅ Henrik Westerlund — exists in TEAM_ROSTER
    
  Unknown names found: 0 ✅

DESIGN COMPLIANCE:
  ✅ Colors used only for status (🟢🟡🔴⚪)
  ✅ Symbols consistent (✅ = done, ◐ = pågår, etc)
  ✅ Whitespace adequate (ADHD-friendly)
  ✅ Typography hierarchy correct
  ✅ Accessibility-ready (NPF/dyslexia-friendly)

═══════════════════════════════════════════════════════════
RESULT: ✅✅✅ PRESENTATION VERIFIED & READY TO SHOW
═══════════════════════════════════════════════════════════
```

---

## 📋 MÄNNISKANS ROLL (Efter AI visar rapport)

**Människan läser rapporten och:**

```
1. Läser FASE 1-3 rapporter
   → Ser vad som är verifierat (✅) och vad som är osäkert (⚠️)

2. Stämmer resultaten med verkligheten?
   → Ja: "OK, visa presentationen"
   → Nej/Osäker: "Verifiera X igen" eller "Jag hämtar data själv"

3. Ser presentationen
   → Känner sig säker (redan verifierad av AI)
   → Kan fokusera på innehål, inte på "stämmer detta?"

4. Mötet
   → Använda presentation med tillit
   → Veta att varje datum/namn/status är verifierat
```

---

## 🎯 VARFÖR DENNA PROCESS?

**Utan denna ordning:**
- AI bygger presentation utan att säga vad som är verifierat
- Människan undrar "stämmer detta?"
- Möte börjar med datakontroll istället för decision

**Med denna ordning:**
- AI rapporterar: "✅ All data verifierad från GitHub"
- Människan vet: "Datumen är säkra, namnen är säkra, status är säker"
- Möte kan fokusera på: vad gör vi nu?

---

## 🚨 KRITISKA REGLER

**Denna workflow är OBLIGATORISK. INGA UNDANTAG.**

```
❌ AI får INTE bygga presentation utan FASE 1-2 rapport
❌ AI får INTE visa presentation utan FASE 3 rapport  
❌ Människan får INTE använda presentation utan att se rapport
❌ Rapport MÅSTE innehålla: data-status, team-coverage, design-check
```

---

**Version:** 1.0  
**Status:** MANDATORY  
**Senast uppdaterad:** 2026-09-14
