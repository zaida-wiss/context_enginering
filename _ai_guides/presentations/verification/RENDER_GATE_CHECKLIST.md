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

## 🔍 FÖRVÄGSTÄMMNING PER SLIDE (OBLIGATORISK FÖRE RENDERING)

**Innan en slide visas måste data VERIFIERAS:**

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

### 2. ASSIGNEE PÅ VARJE ISSUE

```
MÅSTE uppfyllas:
✅ Varje open issue: (#XX - Namn)
✅ Varje merged PR: (#XX - Namn)

OM SAKNAS:
❌ "Issue #XX har ingen assignee — vem äger det?"
→ STOPP, lägg till assignee i GitHub först
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

### 4. MÖTESPROTOKOLLET — TRY → REPORT → FALLBACK

```
🟡 OM du INTE kan nå mötesprotokollet:
   → Rapportera: "Kunde inte nå Google Docs. Kan du klistra in texten?"
   → VÄNTA på användarens svar
   → OM user ger texten: använd den
   → OM user säger "skippa": bygga utan mötet

✅ FALLBACK: Presentationen renderas ÄNDÅ
   (mötet är CONTEXT, inte DATA)
   
✅ RESULTAT: Presentation klar, men med notering:
   "Mötesprotokollet verifierat från: [GitHub data]"
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

### 2. ISSUE UTAN ASSIGNEE

```
❌ STOPP om:
   Issue #XX saknar assignee
   
   Varje issue MÅSTE ha ägare
   (Assignee kan läggas till i GitHub innan rendering)
```

### 3. FABRICERAD DATA

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
