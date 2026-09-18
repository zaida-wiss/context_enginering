---
name: verification_report_template
description: RETIRED — superseded by current receipts and render gate
metadata:
  type: retired_reference
  status: retired
  version: 1.0
---

# 🟡 VERIFICATION REPORT TEMPLATE — Struktur för AI:s Rapporter (UNDER REVIEW)

> **RETIRED. DO NOT USE FOR PRODUCTION.**

**⚠️ STATUS:** Denna fil är markerad för granskning i nästa cleanup-pass.  
Syfte är oklart — inte länkad någonstans och inte aktivt använd.  
Behålls för nu men kan tas bort om ingen använder den.

---

## Ursprungligt innehål:

**Denna fil visar STRUKTUREN på rapporter som AI ger till människan.**

**Rapporterna är INTE för mötet — de är för att människan kan verifiera AI:s arbete.**

---

## 📝 FASE 1: DATA & IDENTITY VERIFICATION REPORT

**Denna rapport presenteras FÖRE presentationen byggs.**

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
     Read from: _ai_guides/project/DEFINITION_OF_DONE.md
     All slides will check against this
     
  ✅ Team roster — LIVE_VERIFIED
     7 members, all identity-verified
     All verified from git commits (not guessed)

═══════════════════════════════════════════════════════════
RESULT: ✅ FASE 1 PASSED — OK to proceed to FASE 2
═══════════════════════════════════════════════════════════
```

### Rapporten Visar:
- **Vilka 7 medlemmar** som är identitetsverifierade från git (inte gissade)
- **Vilka 9 data-Källor** som är tillgängliga (eller fallback)
- **STATUS för varje källa:** ✅ LIVE_VERIFIED, ⚠️ FALLBACK_VERIFIED, ❌ NOT_FOUND

---

## 📝 FASE 2: RENDER GATE VERIFICATION REPORT

**Denna rapport presenteras FÖRE presentation byggs.**

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
  ✅ Whitespace: 6-8px between issues, 12px mellan färgbar+text
  ✅ Font sizes: 28pt title, 14pt content, 24px line-height

═══════════════════════════════════════════════════════════
RESULT: ✅ RENDER GATE PASSED — OK to build presentation
═══════════════════════════════════════════════════════════
```

### Rapporten Visar:
- **DATA COMPLETENESS:** Alla sources tillgängliga?
- **TEAM COVERAGE:** Alla 7 medlemmar representerade?
- **DESIGN RULES:** Designregler förstådda?

---

## 📝 FASE 3: FINAL VERIFICATION REPORT

**Denna rapport presenteras efter presentationen är byggd, INNAN den visas för mötet.**

```
═══════════════════════════════════════════════════════════
FINAL VERIFICATION REPORT — Presentation Ready
═══════════════════════════════════════════════════════════

SLIDES GENERATED:
  Total slides: 24
  Mötespunkter representerade: ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭
  All 7 team members shown: YES ✅

DATA VERIFICATION (per slide):
  Slide ①A (Merged to develop):
    ✅ All PRs merged to develop match GitHub
    ✅ All assignees exist in TEAM_ROSTER
    ✅ Dates match actual merge-dates
    
  Slide ①B (Collection branches):
    ✅ All PRs merged to collection branches identified
    ✅ Deduplication verified (no double-count to develop)
    
  Slide ③ (Frontend denna vecka):
    ✅ Issue #88, #89, #85 match GitHub
    ✅ Assignees verified
    ✅ Blockers match actual dependencies
    
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

SOURCE TRANSPARENCY:
  ✅ All data sources disclosed (footer or slide)
  ✅ Fallback sources marked (⚠️)
  ✅ Unreachable sources noted (❌)

═══════════════════════════════════════════════════════════
RESULT: ✅✅✅ PRESENTATION VERIFIED & READY TO SHOW
═══════════════════════════════════════════════════════════
```

### Rapporten Visar:
- **Slide count & coverage:** Hur många slides, alla 14 mötespunkter?
- **Data verification:** Per-slide data-check mot GitHub
- **Name verification:** Noll okända namn?
- **Design compliance:** Design-regler följda?
- **Source transparency:** Vilka sources är verifierade, vilka är fallback, vilka nåbara?

---

## 🎯 RAPPORTERNAS SYFTE

**Rapporterna är för att människan kan se:**

1. **VAD AI verifierade** (vilka sources lästa, vilka medlemmar identifierade)
2. **VILKA DATA som är säkra** (LIVE_VERIFIED vs FALLBACK_VERIFIED vs NOT_FOUND)
3. **OM PRESENTATIONEN ÄR KLAR** (✅ alla checks passar eller ❌ något misslyckades)

---

## 📋 RAPPORT-CHECKLIST

**Varje rapport MÅSTE innehålla:**

### FASE 1-rapport:
```
☐ Lista på alla 7 team-medlemmar identitetsverifierade
☐ Lista på alla 9 data-källor + status (LIVE/FALLBACK/NOT_FOUND)
☐ RESULTAT: ✅ eller ❌
```

### FASE 2-rapport:
```
☐ DATA COMPLETENESS check
☐ TEAM COVERAGE check (7/7?)
☐ DESIGN RULES check
☐ RESULTAT: ✅ eller ❌ (om ❌ → stanna här)
```

### FASE 3-rapport:
```
☐ Slide count & mötespunkter representerade
☐ Per-slide data-verifikation (sample av slides)
☐ Name verification (noll okända namn?)
☐ Design compliance check
☐ Source transparency (vilka sources visade i presentationen)
☐ RESULTAT: ✅✅✅ eller ❌
```

---

## 🚨 RAPPORT-REGLER

**Rapporten är ALDRIG för mötet.**

Rapporten är för att människan kan:
- Verifiera att AI gjorde sitt jobb
- Stänga presentationen innan mötet börjar (om något är fel)
- Förstå vilka sources som är verifierade vs fallback

**Aldrig visa rapport-innehål i presentationen.**
**Aldrig säga "enligt rapporten" på mötet.**

---

**Version:** 1.0  
**Status:** MANDATORY  
**Senast uppdaterad:** 2026-09-14
