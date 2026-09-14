---
name: ai_verification_workflow
description: AI gör ALLT — hämtar data, verifierar från olika källor, analyserar, levererar presentation
metadata:
  type: process
  critical: true
  required_before: rendering
---

# 🔍 AI VERIFICATION WORKFLOW — End-to-End AI Process

**DENNA FIL SÄGER VAD AI MÅSTE GÖRA, FRÅN START TILL SLUT:**

1. **AI hämtar data** från GitHub + fallback-källor
2. **AI verifierar datan** FRÅN FLERA KÄLLOR (triangulation)
3. **AI analyserar datan** (vad betyder det? vilka mönster?)
4. **AI levererar presentation** (KLAR, inte för redigering)

**Poängen:** AI gör ALLT själv. Presentationen är KLAR utan att invänta godkännande. Människan kan korrigera efteråt om något är fel.

---

## 🎯 END-TO-END AI PROCESS — FRÅN START TILL SLUT

```
┌────────────────────────────────────────────────────────────┐
│                   AI STARTS HERE                          │
│                                                            │
│  STEG 1: HÄMTA DATA från GitHub + fallback-sources       │
│  ├─ Branches (develop status)                             │
│  ├─ Commits denna vecka (från vilka team-medlemmar?)     │
│  ├─ Merged PRs (vad var klart?)                          │
│  ├─ Open PRs (vad väntar?)                               │
│  ├─ Open issues (vad jobbar folk på?)                    │
│  ├─ Project Board (status per kolumn)                    │
│  ├─ Meeting protocol (om nåbar)                          │
│  └─ DoD checklist (definition of done)                   │
│                                                            │
│  STEG 2: VERIFIERA DATAN mot FLERA KÄLLOR (triangulation)│
│  ├─ Datum från Git matchar med GitHub issue-dates?       │
│  ├─ Assignee från GitHub matchar issue-tilldelning?      │
│  ├─ Status från Project Board matchar Git-reality?       │
│  ├─ Team-medlemmar identifierade från git commits?       │
│  └─ Noll okända namn? (bara TEAM_ROSTER.md-medlemmar)   │
│                                                            │
│  STEG 3: ANALYSERA DATAN                                 │
│  ├─ Vad blev klart denna vecka? (commits + PRs)          │
│  ├─ Vad pågår? (open issues + branches)                  │
│  ├─ Vad är blockerat? (dependencies + blockers)          │
│  ├─ Vilka risker syns i koden? (code review)             │
│  └─ Hur många timmar kvar? (kapacitet vs planerat)       │
│                                                            │
│  STEG 4: LEVERERA PRESENTATION                           │
│  ├─ 14 mötespunkter enligt PRESENTATION_STRUCTURE.md    │
│  ├─ Design enligt VISUAL_DESIGN_MANDATORY.md            │
│  ├─ Pedagogiska förklaringar (📚 ord markerade)          │
│  ├─ Små käll-referenser (footer, ej fokus)              │
│  ├─ Färg+Symbol+Text (dyslexi/ADHD-vänlig)              │
│  └─ OM källa inte nåbar → visa i presentationen         │
│     Exempel: "Mötesprotokollet: ⚠️ INTE NÅBAR"          │
│                                                            │
│                    ✅ PRESENTATION KLAAR                 │
│                  (Klar för möte, inte för edit)          │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**AI gör ALLT — Levererar färdig presentation utan väntan:**
- ✅ AI verifierar från FLERA KÄLLOR (triangulation)
- ✅ AI analyserar vad datan betyder
- ✅ AI levererar presentation KLAR
- ✅ Presentation är färdig för möte omedelbar (ingen väntan på godkännande)
- ✅ Människan kan korrigera efteråt om något ändå är fel

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
  ✅ All required sources attempted (primary + fallbacks)?
  ✅ All 7 team members identity-verifiable from GitHub? (can we prove they exist in repo?)
  ⚠️ If source fails, fallback used automatically — only STOP if primary + ALL fallbacks fail

CHECK 2: TEAM COVERAGE
  Active roster: 7 members
  Expected in presentation: 7 (alla måste visas)
  Can all 7 be identity-verified (GitHub profile/commits/issues exist)? YES/NO?
  ☐ If NO → STOP (someone cannot be found in GitHub at all)
  ☐ If YES → continue (show all 7, including those with "Ingen aktivitet denna vecka")
  
  NOTE: "Ingen aktivitet denna vecka" (sick leave, vacation, no work assigned) = OK, not STOP
        STOP ONLY if person cannot be identity-verified (not in GitHub, unknown person)
  
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
  SLIDE_DETAIL_SPEC.md (konkreta slide-specifikationer)
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

## 📋 EFTER AI LEVERERAR — Valfri mänsklig efterkontroll

**AI levererar presentationen. Därefter kan människan (valfritt):**

```
1. Läser presentationen
   → AI har redan verifierat varje slide
   → Kan fokusera på innehål, inte på "stämmer detta?"

2. Om något är fel → Meddela AI
   → "Denna datum är fel, det var 12 sept inte 13 sept"
   → "Denna person är inte assignad, det är någon annan"
   
3. AI korrigerar och levererar uppdaterad version
```

**VIKTIGT:** Denna feedback är VALFRI, inte obligatorisk:
- AI levererar färdig presentation omedelbar
- Människan kan använda presentationen direkt
- Om korrigering behövs, kan den göras efteråt
- AI kan iterera tills det är perfekt, men blockerar inte mötet

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
