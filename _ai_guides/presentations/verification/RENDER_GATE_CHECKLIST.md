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
- ❌ Checksum fails (sum of teams ≠ total)
- ❌ Any team has merged PRs = 0 when work should exist
- ❌ Any team member cannot be found in GitHub
- ❌ Data looks incomplete (sudden jump to 0 in active area)

**SUCCESS criteria:**
- ✅ Checksum passes (totals match)
- ✅ Each active team has visible merged work
- ✅ All 7 members verified or have explicit "no activity"
- ✅ Data matches GitHub when manually spot-checked

---

## 🔍 STEG 2: FÖRVÄGSTÄMMNING PER SLIDE (EFTER DATA VERIFIED)

**Innan en slide visas måste innehål VERIFIERAS:**

### Varje slide måste kontrollera:

1. ✅ **Data stämmer med develop-merges**
   - Issue-nummer i slide = faktisk merged PR i develop?
   - Datum i slide = faktisk merge-datum?
   - INTE data från lokala branches eller outvecklad

2. ✅ **Issues är korrekt öppnade + assignade**
   - Issue är tilldelad någon? (om öppen)
   - Assignee matchar actual GitHub-issue?
   - Är issue fortfarande öppen eller är den redan stängd?

3. ✅ **AC (Acceptance Criteria) är ordentlig**
   - Issue har AC definierade?
   - AC är testbara (inte vaga)?
   - AC matchar faktiskt arbete i PR?

4. ✅ **Test-coverage är tydlig**
   - Finns tester för detta arbete?
   - Vilka test-typer (unit/integration/e2e)?
   - Är tester mergade eller bara planerade?

5. ✅ **PR-review status är uppdaterad**
   - Vem reviewade PR:en?
   - Är review-kommentarer lösta?
   - Status: approved/requested-changes/pending?

### Resultat av verifikation:
```
✅ PASS: Data stämmer → slide visas
❌ FAIL: Data matchar inte → slide UPPDATERAS innan rendering
⚠️ WARN: Data saknas (ex ingen tests än) → slide märks tydligt "pågår"
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

Q: **Are all sources verifiable from GitHub?**
- ✅ Yes → continue
- ❌ No → STOP, remove unverified content

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

### 3. DATA ÄR VERIFIERAD (INTE FABRICERAD)

```
MÅSTE uppfyllas:
✅ Alla siffror från GitHub (commits, PRs, dates)
✅ Alla namn från TEAM_ROSTER.md
✅ Inga gissningar eller "förväntas"

OM FABRICERAD DATA:
❌ "Denna slide innehåller fabricerad data: 'vi förväntar oss...'"
→ STOPP, använd endast verifierad data
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
❌ "Erik är inte i issues → STOPP, rendering nekad"
→ Orsakade att Erik "försvann" från presentationer
```

**NYTT (KORREKT):**
```
✅ Erik är inte i open issues denna vecka
   → Visas som: "Erik Berglund — Tilldelads ingen ny issue denna vecka"
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
- 14 merged PRs ✅
- 8 commits denna vecka ✅
- 3 open issues med aktivitet ✅
- Alla issues har assignee ✅
- Mötesprotokollet nåbar ✅
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

**SCENARIO 2: Issue utan assignee**
```
STATUS denna vecka:
- 5 merged PRs ✅
- 2 commits ✅
- Issue #42 SAKNAR assignee ❌

RESULTAT: ❌ STOPP
Meddelande: "Issue #42 har ingen assignee. Lägg till i GitHub först."
```

**SCENARIO 3: Mötesprotokollet inte nåbar — MEN OK**
```
STATUS denna vecka:
- 5 merged PRs ✅
- 2 commits ✅
- Mötesprotokollet inte nåbar 🟡

RESULTAT: ✅ PRESENTATION RENDERAS (med fallback)
Meddelande: "Kunde inte nå mötesprotokollet. 
            Kan du klistra in texten från mötet?"
```

---

## 🚨 KRITISKA ÄNDRINGAR FRÅN GAMLA SYSTEMET

| Gammalt (BRUTEN) | Nytt (KORREKT) | Varför |
|------------------|----------------|--------|
| Erik saknar issue → STOPP | Erik → "Ingen issue denna vecka" | Fokus PROJEKT, inte individer |
| Möte MÅSTE nås → STOPP | Möte: try/report/fallback | Mötet är CONTEXT, inte kritisk DATA |
| Alla 7 MÅSTE synas | Visa de som hade arbete | Transparens: "Inget" är OK |
| Presentationen om INDIVIDER | Presentationen om PROJEKTET | Ändrar fokus från bedömning till framsteg |

---

## ✅ CHECKLISTA FÖR AI INNAN RENDERING

```
Före du säger "presentationen är klar":

DATA-KILDER:
  [ ] Minst 1 arbete denna vecka (commit/PR/issue)
  [ ] Mötesprotokollet: try/report/fallback (ej blocker)
  [ ] Alla data verifierad från GitHub (ej fabricerad)

INNEHÅL:
  [ ] Varje issue/PR har assignee (#XX - Namn)
  [ ] Team-medlemmar utan arbete: "Ingen issue denna vecka"
  [ ] Fokus på PROJEKT, inte individer

DESIGN:
  [ ] 14 mötespunkter representerade
  [ ] Rätt färger + borders
  [ ] Whitespace 60-70%
  [ ] Fonts enligt VISUAL_DESIGN_MANDATORY

RESULT:
  [ ] Om ALLA checkboxes är OK → RENDERAR
  [ ] Om NÅGON MÅSTE-HA är miss → RAPPORTERAR varför
```

---

**Version:** 2.0 (Uppdaterad med användarens korrektioner)  
**Senast uppdaterad:** 2026-09-14  
**Status:** PRODUCTION — Rätt render-gate för presentationen
