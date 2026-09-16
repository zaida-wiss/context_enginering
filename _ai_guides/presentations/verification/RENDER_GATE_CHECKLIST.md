---
name: render_gate_checklist
description: Korrekt checklist för när presentation KAN/INTE KAN renderas
metadata:
  type: process
  critical: true
  version: 2.0
---

# 🚨 RENDER-GATE CHECKLIST — Korrekt Version

**DENNA CHECKLIST avgör om presentationen får renderas eller inte.**

**Uppdaterad:** 2026-09-14 med användarens korrektioner

---

## 🔍 STEG 1: MANDATORY DATA_AUDIT (FÖRE ALLA SLIDES)

**OBLIGATORISK mellanresultat — måste fullörs innan slides byggs.**

**Generera denna DATA_AUDIT struktur för användaren:**

```
DATA_AUDIT — Week of [REPORTING_PERIOD_START] to [REPORTING_PERIOD_END]

REPOSITORY TOTALS:
  Total merged PRs: N
  Total open PRs: N
  Total commits to develop: N
  Total open issues with activity: N

WORK AREAS (Classification):
  Frontend:
    Merged PRs: [#XX, #YY, #ZZ] (count: N)
    Open PRs: [#XX, #YY] (count: N)
    Active issues: [#XX, #YY, #ZZ] (count: N)
  
  Backend:
    Merged PRs: [#XX, #YY] (count: N)
    Open PRs: [#XX] (count: N)
    Active issues: [#XX, #YY] (count: N)
  
  Native:
    Merged PRs: [#XX] (count: N)
    Open PRs: [] (count: 0)
    Active issues: [#XX] (count: N)
  
  Cross-team:
    Merged PRs: [#XX] (count: N, work affecting multiple teams)
    Open PRs: [#XX] (count: N)
    Active issues: [#XX] (count: N)
  
  Other:
    Merged PRs: [#XX] (count: N, docs/infra/chores)
    Open PRs: [] (count: 0)
    Active issues: [] (count: 0)

TEAM MEMBER COVERAGE:
  Expected: 7
  Verified: N/7 (list: Person1, Person2, ... or "Ingen aktivitet denna vecka" if 0 work)

CHECKSUMS (ALL MUST PASS):
  ✅ COUNT: sum(Frontend + Backend + Native + Cross_team + Other) == repository_total_merged_prs
  ✅ SET: repository_merged_pr_ids == union(all work_areas)
  ✅ UNIQUENESS: No PR ID appears in multiple work_areas (each PR classified exactly once)
  ✅ TEAM: All 7 members identity-verified or marked "no activity"
  
  EXAMPLE FAILURE:
    ❌ Repository shows 12 merged PRs (#90, #79, #72, #66, #53, #50, #95, #87, #80, #75, #60, #55)
    ❌ Frontend: 6 + Backend: 4 + Native: 2 = 12 ✅ count passes
    ❌ BUT #90 is missing from union (appears in Frontend list but forgotten in total)
    ❌ OR #95 appears in both Backend AND Cross_team (counted twice)
    ✅ ID-SET CHECK FAILS → RENDER GATE FAIL
```

**Failure detection (RENDER GATE FAIL if):**
- ❌ DATA_AUDIT checksum fails (merged_pr_count, merged_pr_set, activity_union, team_completeness mismatch)
- ❌ Required information unavailable from ANY allowed source (required_information from SYSTEM_CONTRACT.yaml cannot be verified)
- ❌ Any team member from TEAM_ROSTER cannot be found in GitHub

**SUCCESS criteria (mechanical only):**
- ✅ All DATA_AUDIT checksums pass (per SYSTEM_CONTRACT.yaml)
- ✅ All required_information verified from GitHub or allowed fallback
- ✅ All 7 members verified or marked "Ingen aktivitet denna vecka"
- ✅ Zero work for a team is valid (repository audit confirms it)

---

## 🔍 STEG 2: SLIDE CONTENT VERIFICATION (after data verified)

**Verify that slide content is accurate and derived from authoritative data:**

### Critical verifications (MUST PASS):

1. ✅ **Data matches GitHub source**
   - Issue-nummer på slide = faktisk GitHub-ID?
   - Timestamps = faktisk merge-datum eller update-datum?
   - Data kommer från GitHub (eller allowed fallback, INTE lokala branches)?

2. ✅ **Assignment is accurate**
   - Assignee på slide = faktisk GitHub assignee?
   - Issue är öppen eller stängd såsom angiven?
   - Namn från TEAM_ROSTER.md (eller "??") om assignee saknas?

### Information details (OPTIONAL — only verify if SLIDE_DETAIL_SPEC requires):

3. ⚠️ **Acceptance Criteria** (enrichment only if SLIDE_DETAIL_SPEC says)
   - If slide includes AC: Is AC defined and testable?

4. ⚠️ **Test Coverage** (enrichment only if SLIDE_DETAIL_SPEC says)
   - If slide includes tests: Are tests merged? Which types?

5. ⚠️ **PR Review Status** (enrichment only if SLIDE_DETAIL_SPEC says)
   - If slide includes review: Who approved? Status: approved/pending/changes?

### Verification results:
```
✅ PASS: Data accurate → slide renders
❌ FAIL: Data mismatch → FIX before rendering
⚠️ WARN: Optional details missing → OK, mark with ⚠️ footer note
```

---

## 🚨 KRITISK: DESIGN & CONTENT COMPLIANCE CHECK

**Refer to authoritative files — do NOT repeat their rules:**

- 📊 **Content rules** → see [`SLIDE_DETAIL_SPEC.md`](../../monday_meeting/design/SLIDE_DETAIL_SPEC.md)
- 🎨 **NPF/accessibility rules** → see [`ACCESSIBILITY_NEURODIVERSITY.md`](../../design/ACCESSIBILITY_NEURODIVERSITY.md)
- 🖼️ **Design rules** → see [`VISUAL_DESIGN_MANDATORY.md`](../../design/VISUAL_DESIGN_MANDATORY.md)

**Mechanical check before rendering:**

Q: **Is every slide derived from DATA_AUDIT and SLIDE_DETAIL_SPEC?**
- ✅ Yes → continue
- ❌ No → STOP, fix slides first

Q: **Does the slide follow VISUAL_DESIGN_MANDATORY?**
- ✅ Yes → continue
- ❌ No → STOP, fix design first

Q: **Is all required data verified from an allowed source (GitHub primary, Sheets/Protocol fallback)?**
- ✅ Yes → continue
- ❌ No (data is from unallowed source) → STOP, use allowed sources only

---

## ✅ PRESENTATION KAN RENDERAS om:

### 1. MINST EN SOURCE HAR DATA DENNA VECKA

```
MÅSTE ha minst ETT av dessa:
✅ Minst 1 merged PR denna vecka
✅ Minst 1 commit denna vecka  
✅ Minst 1 open issue med aktivitet denna vecka

OM INGET av detta finns:
❌ "Inget arbete denna vecka — presentationen blir tom"
→ STOPP, rendering INTE tillåten
```

### 2. ASSIGNEE PÅ VARJE ISSUE/PR

```
VISAR MED ASSIGNEE:
✅ (#XX - Namn) — PR/issue har assignee

VISAR MED "??":
✅ (#XX - ??) — PR/issue saknar assignee, men är ändå valid

REGEL: Saknad assignee är ALDRIG blocker. Visa alltid "??" istället.
```

### 3. DATA ÄR VERIFIERAD FRÅN TILLÅTNA KÄLLOR

```
MÅSTE uppfyllas:
✅ Alla siffror från GitHub, Google Sheets, eller mötesprotokollet (EXTERNA_SOURCES.md allowlist)
✅ Alla namn från TEAM_ROSTER.md
✅ Ingen gissad data ("vi förväntar oss...", "normalt skulle...")
✅ Ingen inference utan verifiering ("baserat på...")

OM VERIFIERING SAKNAS:
❌ "Denna slide innehåller ogodkänd data"
→ STOPP, använd endast verifierad data från allowlisted sources
```

### 4. MÖTESPROTOKOLLET — OPTIONAL CONTEXT (INTE BLOCKERANDE)

```
🟡 Mötesprotokollet är CONTEXT, inte DATA → aldrig blockerande

OM du kan nå Google Docs:
   → Läs det för bakgrundskontext
   → Använd för att validera GitHub-data
   
OM du INTE kan nå mötesprotokollet:
   → Byggpresentationen ÄNDÅ (ingen väntan på användare)
   → Använd GitHub data som primär källa
   → Visa i footer: "GitHub data verifierat, mötesprotokollet ej nåbar"

✅ RESULTAT: Presentation renderas ALLTID
   (Mötesprotokollet är optional context, fallback = GitHub data)
```

---

## ❌ PRESENTATION KAN INTE RENDERAS om:

### 1. NOLL ARBETE DENNA VECKA

```
❌ STOPP om:
   - 0 commits denna vecka
   - 0 merged PRs denna vecka
   - 0 open issues med aktivitet

   Presentationen blir tom → ingen poäng att rendrera
```

### 2. FABRICERAD DATA

```
❌ STOPP om:
   "Vi förväntar oss..." — gissningar
   "Normalt skulle..." — AI:s eget kunnande
   "Baserat på..." — inference utan verifiering
   
   Endast verifierad data från GitHub/mötesprotokollet
```

---

## ✅ TEAM-MEDLEMMAR UTAN ARBETE — INTE EN BLOCKER

**GAMMALT (BRUTEN REGEL):**
```
❌ "[PERSON] är inte i issues → STOPP, rendering nekad"
→ Orsakade att [PERSON] "försvann" från presentationer
```

**NYTT (KORREKT):**
```
✅ [PERSON] är inte i open issues denna vecka
   → Visas som: "[PERSON NAME] — Tilldelads ingen ny issue denna vecka"
   → INFORMATION, inte blocker
   → Presentationen renderas ändå

✅ FOKUS: PROJEKTET (vad gjordes)
   INTE: Individer (var är alla)

✅ Transparens: "Ingen issue denna vecka" är OK
```

---

## 📊 EXEMPEL — KAN RENDERAS

```
STATUS denna vecka:
- [N>0] merged PRs ✅
- [N>0] commits denna vecka ✅
- [N>0] open issues med aktivitet ✅
- Alla issues har assignee (eller ??) ✅
- External sources nåbara ✅
- Data verifierad från GitHub ✅

RESULTAT: ✅ PRESENTATION RENDERAS
```

---

## 📊 EXEMPEL — KAN INTE RENDERAS

**SCENARIO 1: Noll arbete**
```
STATUS denna vecka:
- 0 merged PRs ❌
- 0 commits denna vecka ❌
- 0 open issues med aktivitet ❌

RESULTAT: ❌ STOPP
Meddelande: "Inget arbete denna vecka — presentationen blir tom"
```

**SCENARIO 2: Mötesprotokollet inte nåbar — MEN OK**
```
STATUS denna vecka:
- [N] merged PRs ✅
- [N] commits ✅
- External protocol/document inte nåbar 🟡
- Issue #XX SAKNAR assignee (OK — visas som ??)

RESULTAT: ✅ PRESENTATION RENDERAS (med fallback)
Meddelande: "Kunde inte nå [EXTERNAL_SOURCE]. 
            Kan du klistra in data från [SOURCE]?"
```

**Notering:** Missing assignee (shown as `??`) är ALDRIG blocker. Presentationen renderas ändå.

---

## 🚨 KRITISKA ÄNDRINGAR FRÅN GAMLA SYSTEMET

| Gammalt (BRUTEN) | Nytt (KORREKT) | Varför |
|------------------|----------------|--------|
| Erik saknar issue → STOPP | Erik → "Ingen issue denna vecka" | Fokus PROJEKT, inte individer |
| Möte MÅSTE nås → STOPP | Möte: try/report/fallback | Mötet är CONTEXT, inte kritisk DATA |
| Alla 7 MÅSTE synas | Alla 7 accounted for — arbete OR "Ingen issue denna vecka" | Fokus PROJEKT; person utan arbete = neutral info |
| Presentationen om INDIVIDER | Presentationen om PROJEKTET | Ändrar fokus från bedömning till framsteg |

---

## ✅ MECHANICAL RENDER-GATE CHECKLIST (Before Rendering)

**DATA COMPLETENESS:**
```
  [ ] DATA_AUDIT generated and passed (all checksums: COUNT, SET, UNIQUENESS, TEAM_COMPLETENESS)
  [ ] Minimum 1 verified activity this week (from GitHub, Sheets, or allowed fallback)
  [ ] All 7 team members accounted for (with work OR marked "no activity")
  [ ] All data from allowlisted sources (EXTERNAL_SOURCES.md), no fabricated data
  [ ] If GitHub endpoint failed, fallback source (Sheets/Protocol) successfully used
```

**CONTENT INTEGRITY:**
```
  [ ] Each work item has owner (#XX - Name or ## - ??)
  [ ] Team members without work: explicit "Ingen issue denna vecka"
  [ ] Presentation focuses on PROJECT work, not individual evaluation
  [ ] All 14 meeting points (①-⑭) present in structure
  [ ] Each slide header starts with meeting-point symbol (①②③ etc)
```

**ANALYSIS & RECOMMENDATIONS (Beyond Status Reporting):**
```
Presentation must include FORWARD-LOOKING analysis, not just status reporting.

  [ ] PRIORITY RANKING — Which issues should be done first?
      ✅ Issues ranked by: impact + risk + dependencies
      ✅ Not just "5 things are open" — "do THESE 3 first because [X] blocks [Y]"
      ✅ Example: "#67 API (first — blocks 2 teams)" vs "#84 DB (third — independent)"

  [ ] DEPENDENCY CHAIN — What blocks what?
      ✅ #X blocks #Y blocks #Z visualized
      ✅ Allows parallelization: "Frontend does this while Backend does that"
      ✅ Critical path identified: "Feature ready in N days if no delays"

  [ ] TEAM CAPACITY & SPLIT — How should we divide work?
      ✅ Recommendation: Frontend takes [X], Backend takes [Y], Native takes [Z]
      ✅ Avoids: Everyone on same thing, or idle capacity
      ✅ Example: "Zaida: #72 (depends on #67) | Erik: #84 (parallel)"

  [ ] ESTIMATED COMPLETION — When will work actually be DONE?
      ✅ Not "started" — DONE (merged, ready to ship)
      ✅ Includes: review time, merge wait time, testing
      ✅ Risk flagged: "If API review takes 2 days → 6 days total instead of 5"

  [ ] ACTIONABLE NEXT STEPS — What do we DO after this meeting?
      ✅ TODAY: Erik starts #67 (priority 1), Zaida preps #84
      ✅ AFTER #67: Zaida starts #72, Pär starts #89
      ✅ By Friday: All work merged, ready for CTO demo

FAIL GATE if:
  ❌ Only status reported (passive, backward-looking)
  ❌ Recommendations vague ("do better", "go faster")
  ❌ No specific team assignment
  ❌ No actionable next steps
  ❌ Team capacity not addressed (might be idle)
```

**CODE INSPECTION FOR PÅGÅR-ISSUES (QUALITY GATE):**
```
  [ ] For each "Pågår" issue displayed (①B, ①C slides):
      - Branch/PR link is clickable (inspectable)
      - Spot-check: Code looks like it's progressing toward issue goal?
      - Code matches issue description (not going in wrong direction)?
      - Any obvious blockers or stalled sections visible?
  
  [ ] If code inspection reveals problems:
      - Add note: "Code needs review — [specific concern]"
      - Don't hide problems; surface them for team discussion
      - Better to flag in meeting than discover at merge time
  
  [ ] If you cannot inspect code (no access):
      - Mark issue: "Code not inspected — [reason]"
      - Transparency is important (don't pretend you checked)
```

**TEAM COLLECTION BRANCH COVERAGE (CRITICAL for risk/blocker analysis):**
```
  [ ] Risk/blocker/capacity analysis examined ALL team collection branches?
      ✅ develop (primary)
      ✅ Java-Development-Environment (Backend collection)
      ✅ Any other team-specific collection branches?
  
  [ ] Report lists which branches were scanned (transparency)
      Example: "Scanned: develop, Java-Development-Environment | 16 sep 14:00"
  
  [ ] If risk analysis examined ONLY develop: ❌ INCOMPLETE
      Must rescan with team collection branches
      
  WHY: Work often waits on team branches before reaching develop.
       Blocking, capacity, risk analysis is incomplete otherwise.
```

**WCAG 2.2 AA & COLOR SEMANTIC COMPLIANCE (CRITICAL — NEW):**
```
  [ ] NO ordinary text boxes have visible borders, outlines, or fills
      → Headers, titles, dates, subtitles, captions, metadata = plain text ONLY
      → Exceptions: Only designated cards, team containers, status components (per VISUAL_DESIGN_MANDATORY.md)
  
  [ ] NO team color is used as a status color (CRITICAL SEPARATION)
      → Frontend (teal) ≠ any status color
      → Backend (hot pink) ≠ any status color
      → Native (purple) ≠ any status color
      → Cross-team (light slate) ≠ any status color
      → Orange ONLY means status ◐ "pågår", NEVER team
      → Green ONLY means status ✅ "merged", NEVER team
      → Red ONLY means status 🔴 "blocked", NEVER team
  
  [ ] All visible text + information-carrying graphics WCAG 2.2 AA compliant
      → Normal text: 4.5:1 contrast minimum
      → Large text (18pt+ or 14pt bold): 3:1 contrast minimum
      → UI components, borders: 3:1 contrast minimum
      → No dark navy (#0F1830) + black (#000000) borders (0:1 contrast = invisible)
      → Color never the sole information carrier (MUST pair with symbol + text)
  
  [ ] GITHUB ENTITY PROVENANCE — Every issue/PR number verifiable
      → Each #XX on slide corresponds to verified GitHub object
      → Not inferred, guessed, or translated from branch name
      → If work exists but issue unverified: display "Behöver issue" / "Issue ej verifierat" instead of number
      → Per github_entity_identity rule in SYSTEM_CONTRACT.yaml
```

**LAYOUT COMPLIANCE — CANONICAL FORM ONLY:**
```
  [ ] Every slide has exactly: 1 header + 1 main message + 1–3 content blocks
  [ ] No horizontal layouts (all content stacked vertically)
  [ ] No small cards in grid (all blocks are 100% width)
  [ ] No compression of typography or spacing (use FIXED values from VISUAL_DESIGN_MANDATORY)
  [ ] If slide has 4+ work items → continues automatically to ①A.1, ①A.2 (never summarized)
  [ ] All block dimensions match spec: 18pt title, 14pt effect, 12pt owner
  [ ] Whitespace: 20px margin between blocks, 16px padding around content
```

**RENDERED OUTPUT VERIFICATION (MANDATORY BEFORE DELIVERY):**

🚨 **YOU MUST RENDER PPTX AND VISUALLY CHECK EVERY SLIDE.**

Do not skip this. Do not claim "it looks good in theory". Render it.

```
STEP A: Render presentation to PPTX (PowerPoint/Google Slides export)

STEP B: Open PPTX file and page through every slide visually. For each slide:
  
  [ ] Header is at top (symbol first)
  [ ] Main message is clearly visible below header
  [ ] Content blocks stack vertically (never side-by-side)
  [ ] No blocks pushed off-slide or cut at bottom
  [ ] No text clipping or overlap
  [ ] All text fully visible in its block (no truncation)
  [ ] Work items display as single lines (not wrapped into grid)
  [ ] Spacing between blocks matches spec (20px visual gap visible)
  [ ] Slide is NOT dense/cramped (60-70% whitespace visible)
  [ ] Slide does NOT look like dashboard/grid/card-layout
  
STEP C: If ANY check fails:
  [ ] Fix the content (split to continuation slide ①A.1, etc.)
  [ ] Re-render PPTX
  [ ] Re-check visually
  [ ] Repeat until all checks pass
  
STEP D: Only after ALL slides pass visual check:
  [ ] Presentation is ready for delivery
```

**IF YOU FIND PROBLEMS DURING VISUAL CHECK:**
- Text clipping → reduce text length, split to new slide
- Block overflow → split to continuation slide automatically
- Dense layout → already at max 3 blocks per slide; if still dense → reformat work items as single lines
- Dashboard appearance → check that blocks are 100% width and stacked vertically, not in grid

**NEVER deliver a presentation without rendering it to PPTX and visually checking every single slide.**

**FINAL CHECK — ALWAYS RENDER:**
```
  If ALL checkboxes passed:
    ✅ Render and deliver (full verification)
  
  If REQUIRED data present but some enrichment missing:
    ⚠️ Mark missing sources in footer, then render anyway
    Example: "GitHub verified ✅ | Board unavailable ⚠️ | Commits derived ✅"
  
  If REQUIRED sources all failed (no fallback worked):
    ⚠️ Mark all sources as UNVERIFIED, render with ⚠️ WARNING
    Example: "⚠️ All data sources unavailable this week"
  
  NEVER: Stop rendering because "data is incomplete"
  ALWAYS: Render with whatever data exists + mark accuracy in footer
```

---

**Version:** 2.0 (Uppdaterad med användarens korrektioner)  
**Senast uppdaterad:** 2026-09-14  
**Status:** PRODUCTION — Rätt render-gate för presentationen
