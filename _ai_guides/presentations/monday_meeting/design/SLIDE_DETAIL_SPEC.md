---
name: slide_detail_spec
description: Exakt innehål för varje slide i presentationen (①-⑭) — format, kolumner, regler
metadata:
  type: critical_specification
  version: 1.0
---

# 📊 SLIDE DETAIL SPECIFICATION — Exakt Innehål per Slide

**Denna fil säger EXAKT vad varje slide ska innehålla — ingen gissning.**

🔗 **VISUELL REFERENS:** Se [`TEMPLATE_REFERENCE.html`](TEMPLATE_REFERENCE.html) för hur varje slide ska se ut visuellt (färger, fonts, spacing, rundade hörn).

Se [PRESENTATION_STRUCTURE.md](../structure/PRESENTATION_STRUCTURE.md) för punkt-nivå-overview.

---

## 🎨 COLOR PALETTE & DESIGN CONSTANTS

**Dessa värden används överallt i presentationen:**

### Färger (RGB)
```
MERGED-sektion bakgrund:     RGB 76, 175, 80     (🟢 Grön)
PÅGÅR-sektion bakgrund:      RGB 255, 152, 0     (🟡 Orange)
VÄNTAR PÅ REVIEW bakgrund:   RGB 255, 152, 0     (🟡 Orange) eller RGB 244, 67, 54 (🔴 Röd)
Text på färgad bakgrund:     Vit (RGB 255, 255, 255)
Neutral bakgrund:            Ljusgrå (RGB 245, 245, 245)
Header text:                 Mörkgrå (RGB 50, 50, 50)
Body text:                   Mörkgrå (RGB 100, 100, 100)
```

### Font & Spacing
```
Section headers:             Arial 14pt BOLD
Issue nummer & titel:        Arial 13pt regular
Meta-text (datum/branch):    Arial 12pt regular
Row height (tabeller):       24px MINIMUM (NPF för dyslektiker)
Padding per cell:            12px
Margin mellan sektioner:     8px minimum
Corner radius (textboxar):   6-8px (rundade hörn)
Kontrast minimum:            4.5:1 (WCAG AA)
```

---

---

## 📝① AVKLARAT SEDAN FÖRRA MÖTET (1-3 slides)

**Rubriker per team (måste matcha mötesprotokollet):**
- Slide ①A: **"Avklarat sedan förra mötet — Frontend"**
- Slide ①B: **"Avklarat sedan förra mötet — Backend"**
- Slide ①C: **"Avklarat sedan förra mötet — Native"**

### SLIDE ①A: Avklarat sedan förra mötet — Frontend

**FORMAT:** Tabell med tre grupper (Merged | Pågår | Väntar på review)

**FORMAT OCH STRUKTUR:**

Din presentation måste innehålla:
- ✅ MERGED DENNA VECKA (faktiska merged PRs från GitHub denna vecka)
- ✅ PÅGÅR DENNA VECKA (faktiska branches med commits från GitHub denna vecka)
- ✅ VÄNTAR PÅ REVIEW (faktiska öppna PRs från GitHub utan approval)

**MÅSTE VISAS VISUELLT:**
- 🔵 Team-märke (Frontend/Backend/Native) per rad — från TEAM_ROSTER.md
- ✓ Assignad-status — namn om assignad, gul highlight + 🔄 UNASSIGNED om ingen
- 📅 Tidsstämpel — "Data från 2026-09-14 14:00:32 UTC"

**ALDRIG ANVÄND EXEMPEL-DATA I FAKTISK PRESENTATION.**
Alla data måste hämtas LIVE från GitHub när presentationen byggas.

Referens-tabell-FORMAT (använd denna som struktur, INTE som data):

| Team | Issue # | Titel | Assignad | Status | Merged/Branch |
|------|---------|-------|----------|--------|---------------|
| [från TEAM_ROSTER] | #[GitHub] | [GitHub] | [GitHub eller 🔄 UNASSIGNED] | ✓/◐/⏳ | [GitHub] |

**REGLER:**
- **Del 1: Merged denna vecka** (sortera på merge-datum, äldst först — veckan börjar överst, slutar längst ner)
  - Visa ALLA merged PRs denna vecka
  - Status = ✓ DONE
  - Datum = merge-datum (YYYY-MM-DD)

- **Del 2: Pågår denna vecka** (sortera på branch-aktivitet, senast pushad först)
  - Visa ALLA öppna branches med commits denna vecka (även utan PR än)
  - Status = ◐ PÅG
  - Branch-kolumn = branch-namn (feature/#88)
  - Verifiera mot Project Board: Issue är "In Progress" ELLER branch har commits senaste 3 dagarna

- **Del 3: Väntar på review** (KRITISK textruta för gruppens uppmärksamhet)
  - Visa ALLA öppna PRs som väntar på review (status: "awaiting review" eller ingen approval än)
  - Status = ⏳ REVIEW (påminn gruppen om att reviewa)
  - Branch-kolumn = PR-nummer (#142, #143)
  - Sortera på skapningsdatum (äldst först — längst väntan)
  - **VISUELL MARKERING:** Denna sektion ska ha en 🟠 orange eller 🔴 röd bakgrund för att dra uppmärksamhet

- **Arbetet från alla 7 team-medlemmar måste synas** (antingen i Merged, Pågår eller Väntar på review)
  - Om medlem har 0 commits denna vecka: Lägg till "Inget arbete i koden denna vecka"

- **Assignad = Ägare av arbetet** (GitHub issue/PR assignee, inte reviewer eller merger)
  - VIKTIGT: Visar VEMS JOBB det är, inte vem som checkade det
  - ASSIGNEE från GitHub = källan (inte reviewer, inte "merged by")
  - Format: GitHub handle + display name (från TEAM_ROSTER.md)
  - Exempel: ✅ "#95 Security review · Zaida Wiss" (Zaida ÄGde det)
  - Exempel: ❌ "#95 Security review · Erik Berglund" (Erik reviewade det, men Zaida ägde det)

**MÅSTE innehålla:**
- ✅ Issue-nummer (#XX)
- ✅ Kort titel (2-5 ord)
- ✅ **Assignad person** (ägaren av arbetet, från GitHub issue/PR assignee) — INTE reviewer
- ✅ Status (✓ DONE eller ◐ PÅG eller ⏳ REVIEW)
- ✅ Datum (merge-datum, branch-namn, eller PR-nummer)
- ✅ ALLA 7 team-medlemmar (även om 0 arbete denna vecka)
- ✅ **Väntar på review-sektion** (ska synas tydligt för gruppens uppmärksamhet)

**FÅR INTE innehålla:**
- ❌ Commit-hash
- ❌ Endast merged (måste visa pågår + review också)
- ❌ Stale branches (>3 dagar utan push)
- ❌ PRs som redan är mergead (de hör hemma i "Merged" sektion)
- ❌ **Reviewer namn som assignee** (visa ägare, inte vem som checkade)

**DATA-SOURCES:**
- 📊 **Merged:** GitHub PRs API (merged till develop denna vecka) — FAKTISK GitHub-data, inte exempel
- 📊 **Pågår:** GitHub branches (commits senaste 7 dagar) + Project Board (status: In Progress) — FAKTISK data
- 📊 **Väntar på review:** GitHub PRs API (open PRs utan approval, skapade denna vecka) — **MÅSTE HÄMTAS FRÅN GITHUB**, inte exempel
  - Sortera på skapningsdatum (längst väntan först)
  - Inkludera ENDAST team-medlemmars PRs (match issue-owner mot TEAM_ROSTER.md)
  - Status: ⏳ REVIEW (ingen approval än)
- 🔍 **Jämförelse:** Branch mot Project Board — visa discrepancy om Board och Git inte stämmer

**FOOTER:** `Källa: GitHub PRs + branches (LIVE från [UTC-TIDSSTÄMPEL]) ✅`

🚨 **KRITISK REGEL:** All data i denna slide MÅSTE hämtas LIVE från GitHub när presentationen byggas. Aldrig från exempel, aldrig från snapshot. Inkludera tidsstämpel (t.ex. "2026-09-14 14:00:32 UTC") så det är tydligt att data är aktuell.

---

### SLIDE ①B: Avklarat sedan förra mötet — Backend

**FORMAT:** Tabell (identisk struktur som ①A)

**KOLUMNER:** Issue # | Titel | Assignad | Status | Merged/Branch

**REGLER:**
- (Identiska som ①A, men ENDAST Backend-issues)
- Filtrera: Visa bara issues där Team = "Backend" (från TEAM_ROSTER.md labels)
- Merged: Backend PRs merged denna vecka
- Pågår: Backend branches med commits denna vecka
- Väntar på review: Backend PRs som väntar på approval

**DATA-SOURCES:**
- 📊 **Merged:** GitHub PRs API (Backend-issues, merged denna vecka)
- 📊 **Pågår:** GitHub branches (Backend-issues, commits senaste 7 dagar)
- 📊 **Väntar på review:** GitHub PRs API (Backend-issues, open, no approval)
- 🔍 **Jämförelse:** Backend-issues mot Project Board — visa discrepancy

**FOOTER:** `Källa: GitHub PRs + branches (Backend denna vecka) + Project Board ✅ | ⏳ Reviews behövs på: [faktiska Backend-issues]`

---

### SLIDE ①C: Avklarat sedan förra mötet — Native

**FORMAT:** Tabell (identisk struktur som ①A)

**KOLUMNER:** Issue # | Titel | Assignad | Status | Merged/Branch

**REGLER:**
- (Identiska som ①A, men ENDAST Native-issues)
- Filtrera: Visa bara issues där Team = "Native" (från TEAM_ROSTER.md labels)
- Merged: Native PRs merged denna vecka
- Pågår: Native branches med commits denna vecka
- Väntar på review: Native PRs som väntar på approval

**DATA-SOURCES:**
- 📊 **Merged:** GitHub PRs API (Native-issues, merged denna vecka)
- 📊 **Pågår:** GitHub branches (Native-issues, commits senaste 7 dagar)
- 📊 **Väntar på review:** GitHub PRs API (Native-issues, open, no approval)
- 🔍 **Jämförelse:** Native-issues mot Project Board — visa discrepancy

**FOOTER:** `Källa: GitHub PRs + branches (Native denna vecka) + Project Board ✅ | ⏳ Reviews behövs på: [faktiska Native-issues]`

---

**JÄMFÖRELSE MELLAN TEAMEN (①A-C):**

Dessa tre slides tillsammans visar gruppens KOMPLETTA bild denna vecka:

| | Frontend | Backend | Native |
|---|----------|---------|--------|
| Merged | X PRs | Y PRs | Z PRs |
| Pågår | X branches | Y branches | Z branches |
| Väntar på review | X PRs | Y PRs | Z PRs |

**Syftet:** Se hur det gick för varje team denna vecka — klart arbete, aktivt arbete, och vad som väntar på uppmärksamhet.

---

## 📝② NULÄGE & DEADLINE (1 slide)

### SLIDE ②A: Nuläge + Deadline Tracker & Risk

**FORMAT:** Två delar: (1) Progress bars per team, (2) Deadline Tracker med Risk-nivå

**INNEHÅL - DEL 1: NULÄGE denna sprint (compact)**

```
PROGRESS:

Frontend:  ████████░░ 80% (API-kontrakt väntar på Backend)
Backend:   ██████░░░░ 60% (Fokus denna vecka)
Native:    ███████░░░ 70% (Blockerad på Backend-kontrakt)
```

**INNEHÅL - DEL 2: DEADLINE TRACKER (fokuserat på risk)**

```
🔴 KRITISK (Idag 14:00) — API-kontrakt fastslås
   VAD: Frontend + Backend fastslår format, endpoints, types
   VARFÖR: Låser upp Frontend #88-#89 + Native #86
   STATUS: ⏳ INGEN AKTIVITET än
   RISK: Om inte klart idag → 2 dagar försening för 2 teams
   ACTION: Erik möte 14:00 — kan vi unblockera NU?

🟠 HÖGT (Imorgon) — API dokumenterad i GitHub
   VAD: Formell dokumentation i issue #99 (JSON-schema, endpoints)
   VARFÖR: Frontend + Native behöver detta för integration-test
   STATUS: ⏳ Beror på idag's möte
   RISK: 1 dag sen → test börjar på onsdag istället
   ACTION: Vilka kan hjälpa Erik dokumentera?

🟡 MEDEL (Fredag) — Feature-complete eller fallback
   VAD: Alla features klara ELLER fallback för CTO-demo
   VARFÖR: CTO-demo denna vecka
   STATUS: 🟢 ON TRACK (Frontend 80%, Backend 60%)
   BUFFER: 1 dag kvar
   ACTION: Hålla fokus på blockers denna vecka
```

**REGLER:**
- **Del 1 (Progress):** Kompakt — progress bars per team, max 3 rader
- **Del 2 (Deadlines):** Primär fokus — vilken deadline, vad innebär den, vilken risk, vad gör vi
- Deadlines i prioritetsordning: 🔴 Kritisk → 🟠 Högt → 🟡 Medel
- Varje deadline: VAD | VARFÖR | STATUS | RISK | ACTION
- STATUS-märken: ⏳ = väntar, 🟢 = on track, 🔴 = behind, 🟠 = risk
- ACTION = konkret nästa steg (inte "vi hoppas")

**MÅSTE innehålla:**
- ✅ Progress % per team
- ✅ Vilka deadlines vi har (prioriterade)
- ✅ VAD varje deadline innebär (inte bara datum)
- ✅ VARFÖR deadline är viktig (påverkan)
- ✅ Nuläge mot deadline (STATUS)
- ✅ RISK om vi missar (KONKRET konsekvens)
- ✅ KONKRET nästa handling (ACTION)

**FÅR INTE innehålla:**
- ❌ Detaljerade issue-listor (se punkt ③-⑤)
- ❌ Historiska data ("förra veckan var vi...")
- ❌ Försäljnings-språk ("Vi är på vägen!")
- ❌ Vaga risks ("vi kan bli sen") — måste vara KONKRET
- ❌ Vaga actions ("vi ska jobba på det") — måste ha ÄGA och TIDRAM

**FOOTER:** `Källa: GitHub issues + Project Board + Sprint planning ✅`

---

## 📝③ FRONTEND (1-3 slides)

### SLIDE ③A: Frontend — Denna sprint

**FORMAT:** Tabell

**KOLUMNER:**
| Issue # | Titel | Assignad | Status | Blocker |
|---------|-------|----------|--------|---------|
| #88 | Critical interactions | Björn Boman | ◐ PÅG | API-kontrakt |
| #89 | E2E happy path | Tomac Barin | ◐ PÅG | API-kontrakt |
| #85 | Responsive header/nav | Zaida Wiss | ✓ DONE | — |

**REGLER:**
- En rad per issue denna sprint (öppen eller pågår)
- Sortera på status (DONE sist)
- Status-märken: ✓ = DONE, ◐ = PÅG, ⏳ = VÄNTAR
- "Blocker" = vad väntar vi på (issue-nummer eller kort beskrivning)
- Om ingen blocker: använd "—"

**MÅSTE innehålla:**
- ✅ Issue-nummer
- ✅ Titel (2-5 ord)
- ✅ Assignad (personens namn)
- ✅ Status (✓/◐/⏳)
- ✅ Blocker (eller "—")

**FÅR INTE innehålla:**
- ❌ Commit-hash
- ❌ PR-nummer (det är issues vi visar)
- ❌ Estimat i timmar
- ❌ "Nästan klart" (antingen DONE eller PÅG)

**FOOTER:** `Källa: GitHub issues + Project Board ✅`

---

### SLIDE ③B: Frontend — Operativ handlingsplan (om behövs)

**FORMAT:** Numrerad lista

**INNEHÅL:**
```
NÄSTA STEG:
1. Björn ↔ Backend (Erik): API-kontrakt möte idag 14:00
2. Tomac pairing med Zaida: Testa happy path mot mock-API
3. Zaida: Code review #85 innan merge
```

**REGLER:**
- Numrerad lista (1, 2, 3...)
- Högst 3-5 actions
- Format: `Namn: Vad, när` eller `Person A ↔ Person B: Möte vad`
- Inkludera tid om relevant ("idag 14:00", "imorgon")

**MÅSTE innehålla:**
- ✅ Vem gör vad
- ✅ Nästa 24-48 timmar
- ✅ Tidsram om kritiskt

**FÅR INTE innehålla:**
- ❌ Generell planering ("vi ska jobba på...")
- ❌ Redan gjorda saker

**FOOTER:** `Baserat på punkt ③A status`

---

### SLIDE ③C: Frontend — Beroenden & Risker (om behövs)

**FORMAT:** Text med färgade markeringar

**INNEHÅL:**
```
VÄNTAR PÅ:
  🔴 Backend API-definition för #88, #89
  🟠 Möjlig: Test-ramverk från Rasha

RISK:
  🟠 Om API inte klart i morgon → 1-2 dagar försening
```

**REGLER:**
- 🔴 = kritisk, 🟠 = måttlig
- "Väntar på" = externa dependencies
- "Risk" = vad kan gå fel denna vecka

**FÅR INTE innehålla:**
- ❌ Gamla problem från förra veckan
- ❌ Spekulationer ("kanske blir det...")

---

## 📝④ BACKEND (1-3 slides)

### SLIDE ④A: Backend — Denna sprint

**FORMAT:** Tabell (identisk som ③A)

**KOLUMNER:** Issue # | Titel | Assignad | Status | Blocker

**REGLER:** (identiska som ③A)

---

### SLIDE ④B: Backend — API-kontrakt-status (om behövs)

**FORMAT:** Tabell

**KOLUMNER:**
| Endpoint | Status | Frontend blockar? | Nästa |
|----------|--------|-------------------|-------|
| POST /user/login | ✅ Dokumenterad | Nej | Testning |
| POST /transaction/execute | 🟠 I review | JA (#88-#89) | Erik review idag |

**REGLER:**
- Status: ✅ = klart, 🟠 = in progress, ❌ = ej påbörjad
- "Frontend blockar?" = JA/Nej (med issue-nummer om JA)
- "Nästa" = nästa steg (en mening)

---

### SLIDE ④C: Backend — Operativ handlingsplan (om behövs)

**FORMAT:** Numrerad lista (samma som ③B)

---

## 📝⑤ NATIVE (1-3 slides)

### SLIDE ⑤A: Native — Denna sprint

**FORMAT:** Tabell (identisk som ③A)

---

### SLIDE ⑤B: Native — JNA-kontrakt-status (om behövs)

**FORMAT:** Text

**INNEHÅL:**
```
VÄNTAR PÅ:
  🔴 Backend API-kontrakt för #86

MÖJLIG SUPPORT:
  Pär kan stödja Frontend denna vecka medan väntar
```

---

## 📝⑥ BLOCKERS & DEPENDENCIES (1-2 slides)

### SLIDE ⑥A: Blockerträd — Alla kritiska kedjor

**FORMAT:** ASCII-diagram eller tabell

**INNEHÅL:**
```
🔴 KRITISKA KEDJOR:

[#43 API Foundation]
   ├──→ [#82 Portfolio reads]
   └──→ [#83 Allocation saves]

[#87 Test Foundation]
   └──→ [#88 Critical interactions]
        └──→ [#89 E2E tests]
```

**REGLER:**
- Visa ENDAST kritiska chains (låser upp mycket)
- Format: ASCII-diagram (pilar → visar beroende)
- Visa issue-nummer (#XX) och kort titel
- Färger: 🔴 = kritisk, 🟠 = måttlig

**MÅSTE innehålla:**
- ✅ Foundation-issues (låser upp mycket)
- ✅ Dependenter (startar när foundation mergad)
- ✅ Vilka är redan lösta (✅ markerade)

**FÅR INTE innehålla:**
- ❌ Alla issues (bara kritiska kedjor)
- ❌ Timmar eller estimat

**FOOTER:** `Källa: Code review + GitHub PR dependencies ✅`

---

### SLIDE ⑥B: Code Review Findings (om behövs)

**FORMAT:** Text med märkningar

**INNEHÅL:**
```
KRITISKA FYND:

🔴 Backend PR #95 — SQL-injection risk
   STATUS: Åtgärdad + testning igång
   LÖST: Ja, ready för merge

🟠 Frontend PR #88 — API saknas dokumentation
   STATUS: Väntar på Erik API-definition
   NÄSTA: Björn reviewar igen när API klart
```

**REGLER:**
- 🔴 = säkerhetsproblem, 🟠 = designproblem
- "STATUS" = vad gör vi åt det?
- "LÖST" = Ja/Nej/I progress

---

## 📝⑦ RISKER (1-2 slides)

### SLIDE ⑦A: Risk-register denna vecka

**FORMAT:** Tabell

**KOLUMNER:**
| Risk | Sannolikhet | Konsekvens | Mitigation | Status |
|------|-------------|-----------|-----------|--------|
| API-kontrakt ej klart | Låg | Frontend får 2d försening | Erik + Björn möte idag 14:00 | Pågår |
| Zaida överbelastad | Medel | Kvalitetsfall | Pairing Tomac+Björn | Planerat |

**REGLER:**
- Sannolikhet: Låg/Medel/Hög
- Konsekvens: En mening om vad som händer
- Mitigation: Konkret åtgärd (inte "vi hoppas...")
- Status: Identifierad/Pågår/Löst

**MÅSTE innehålla:**
- ✅ Vad kan gå fel
- ✅ Vad gör vi åt det (mitigation)
- ✅ Vem gör det

**FÅR INTE innehålla:**
- ❌ Spekulationer
- ❌ Gamla risker från förra veckan

**FOOTER:** `Källa: Code review + kapacitet-analys ✅`

---

## 📝⑧ KAPACITET & ESTIMERING (1 slide)

### SLIDE ⑧A: Kapacitet denna vecka — Passar detta?

**FORMAT:** Tabell + bedömning

**INNEHÅL:**
```
KAPACITET DENNA VECKA:

Frontend:
  Tillgängligt: 45 timmar (3 × 15h/vecka)
  Planerat: 48 timmar (#88, #89, #85, overhead)
  Status: 🟠 LITE STRAMT

Backend:
  Tillgängligt: 40 timmar (2 × 20h/vecka)
  Planerat: 35 timmar (#95, #87, API-def, möte-overhead)
  Status: 🟢 OK

Native:
  Tillgängligt: 30 timmar (2 × 15h/vecka)
  Planerat: 15 timmar (#86, blockerad på API)
  Status: 🟢 OK — extra kapacitet för support

REKOMMENDATION:
  Flytta #85 till nästa vecka för att ge Frontend andrum.
  Pär kan stödja Frontend #88 under API-väntan.
```

**REGLER:**
- Kolumner: Tillgängligt | Planerat | Status
- Status-färger: 🟢 OK / 🟠 STRAMT / 🔴 ÖVERBELASTAT
- Rekommendation = konkret (vilka issues flytta?)
- Timmar = estimates från team-medlemmar

**MÅSTE innehålla:**
- ✅ Kapacitet per team
- ✅ Jämförelse: kan vi klara allt?
- ✅ Rekommendation om justering

**FÅR INTE innehålla:**
- ❌ "Vi löser det" (optimism utan data)
- ❌ Micro-managing per person

**FOOTER:** `Källa: Team estimat (från punkt ③-⑤) ✅`

---

## 📝⑨ PRIORITERING & SCOPE (1-2 slides)

### SLIDE ⑨A: Planerad ordning — Fas 1 → 2 → 3

**FORMAT:** Tabell eller text

**INNEHÅL:**
```
🔴 FAS 1 — Foundation Issues (starta nu):
  ✅ Zaida: #87 Test foundation (låser upp #88/#89)
  ✅ Tomac: #43 API client + mock (låser upp #82/#83)
  ✅ Björn: #81 Linked allocation (låg konflikt, egen komponent)

  Varför: Tre kedjor, låg mergekonfliktrisk. #43/#87 låser upp mycket.

🟠 FAS 2 — Efter Fas 1 mergad (pull develop först!):
  Zaida: #88 Critical interaction tests
  Tomac: #82 usePortfolio (kräver #43 merged)
  Björn: #85 Responsive header (kan parallelleras)

  Varför: #82 kräver #43. #85 oberoende av dataflödet.

🟡 FAS 3+ — Beroenden lösta:
  Zaida: Stabilisering #88
  Tomac: #83 saveAllocation (kan NOW startas utan #81 konflikt)
  Björn: #86 Responsive dashboard
```

**REGLER:**
- Fas 1 = vad gör vi DENNA VECKA
- Fas 2 = när Fas 1 är merged, pull develop först
- Format: Person: Issue + varför denna ordning
- Färger: 🔴 = nästa, 🟠 = sedan, 🟡 = senare

**MÅSTE innehålla:**
- ✅ Ordning (Fas 1 → 2 → 3)
- ✅ Vem gör vad
- ✅ Varför denna ordning (blockers, deps)
- ✅ "Max 1 active + 1 queued per person" regel

**FÅR INTE innehålla:**
- ❌ Slumpmässig ordning
- ❌ "Vi hoppas vi hinner"

**FOOTER:** `Källa: DEPENDENCY_CHAIN_PLANNING + kapacitet ✅`

---

### SLIDE ⑨B: Teamregel — Max 1 active + 1 queued per person

**FORMAT:** Text med exempel

**INNEHÅL:**
```
🚨 MAX 1 ACTIVE + 1 QUEUED PER PERSON

Ingen börjar nästa issue innan dependency är merged i develop.

Exempel ordning för Person A (Zaida):
  1. #87 → merge → pull develop
  2. #88 (depender på #87) → merge → pull develop
  3. #89 (depender på #88)

Före varje ny issue:
  ☐ Pull/rebase mot develop
  ☐ Kontrollera öppna PRs (vem rör samma komponenter?)
  ☐ Bekräfta dependency är mergad (inte bara "nästan klar")
```

---

## 📝⑩ TEKNISKA BESLUT (1 slide)

### SLIDE ⑩A: Arkitektur-beslut denna vecka

**FORMAT:** Tabell

**INNEHÅL:**
```
🟢 BESLUT ① — API-kontrakt format
   FORMAT: RESTful JSON (redan validerat)
   ÄGARE: Erik (Backend-lead)
   DEADLINE: Idag 14:00
   DOKUMENTATION: #99 GitHub issue
   PÅVERKAN: Frontend (#88-#89), Native (#86)

🟠 BESLUT ② — Test-ramverk
   FORMAT: Vitest (unit) + Playwright (E2E)
   ÄGARE: Rasha (Backend-lead)
   DEADLINE: Denna dag
   DOKUMENTATION: #87 GitHub issue
   PÅVERKAN: Alla teams

🟡 DISKUSSION — Branch-strategi vid merge
   FRÅGA: Merge #95 till main direkt eller via release-branch?
   ÄGARE: Erik + PL
   DEADLINE: Innan #95 klar (idag)
   PÅVERKAN: Release-process
```

**REGLER:**
- 🟢 = Beslut fattad, 🟠 = Under granskning, 🟡 = Diskussion behövs
- Format: BESLUT # — Rubrik
- Varje beslut: FORMAT | ÄGARE | DEADLINE | DOKUMENTATION | PÅVERKAN
- Max 3-4 beslut per vecka

**MÅSTE innehålla:**
- ✅ Vad beslutas
- ✅ Vem beslutar
- ✅ Deadline
- ✅ Vem påverkas

**FÅR INTE innehålla:**
- ❌ Tekniska detaljer (spara för GitHub issue)
- ❌ Gamla beslut

**FOOTER:** `Källa: Code review + arkitektur-diskussioner ✅`

---

## 📝⑪ SPRINTMÅL (1 slide)

### SLIDE ⑪A: Sprintmål denna vecka — Härledd från data

**FORMAT:** Text med bullet points

**INNEHÅL:**
```
SPRINTMÅL DENNA VECKA (baserat på prioritering + kapacitet):

✅ Bekräfta API-kontrakt Frontend ↔ Backend innan vecka-slut (KRITISK)
   Varför: Låser upp Frontend #88-#89 och Native #86
   Ägare: Erik (Backend) + Björn (Frontend)
   Deadline: Fredag EOD (eller idag för att ha buffer)

✅ Etablera testramverk för end-to-end-flow (FOUNDATION)
   Varför: Backend + Frontend behöver detta för integration-testning
   Ägare: Rasha (Backend)
   Deadline: Denna dag eller imorgon

✅ Ge Frontend + Native möjlighet att börja integration-testning
   Varför: Två teams kan parallellisera när API är klart
   Ägare: Erik + Björn + Henrik
   Deadline: Vecka-slut

FEASIBILITY-CHECK:
  ✅ Frontend kapacitet stramt men möjligt (47/48 timmar)
  ✅ Backend har kapacitet (35/40 timmar)
  ✅ Native kan stödja Frontend medan väntar
  → MÅL ÄR REALISTISKT med rekommenderade justeringar
```

**REGLER:**
- Mål ska vara HÄRLEDD från data (punkt ①-⑧), inte önskefullhet
- Max 3-4 mål per vecka
- Varje mål: Vad | Varför | Ägare | Deadline
- Feasibility-check: Kan vi faktiskt göra detta?
- Om inte realistiskt: Säg det direkt (🟠 STRAMT, 🔴 OMÖJLIGT)

**MÅSTE innehålla:**
- ✅ Övergripande mål (1-2 meningar)
- ✅ Deadline
- ✅ Varför detta mål (inte bara "vi vill...")
- ✅ Feasibility-bedömning (kan vi göra det?)

**FÅR INTE innehålla:**
- ❌ Mål från förra veckan (vi bygger nytt från ny data)
- ❌ Optimism utan grund

**FOOTER:** `Härledd från punkt ③-⑧ (team-status, kapacitet, prioritering) ✅`

---

## 📝⑫ SPRINTPLAN (1-2 slides)

### SLIDE ⑫A: Daglig tidsplan denna vecka

**FORMAT:** Text med daglig breakdown

**INNEHÅL:**
```
MÅNDAGEN 14 SEPT:
  09:00-10:30  Sprint Planning-möte
  14:00-14:30  Erik ↔ Frontend API-kontrakt-möte
  Deadline: #95 security-testing klar

TISDAGEN 15 SEPT:
  10:00-10:30  Erik ↔ Native JNA-kontrakt-möte
  Deadline: API-kontrakt formell dokumenterad i GitHub

ONSDAGEN 16 SEPT:
  08:00-09:00  Code review för #88-#89 (nya API-versionen)
  14:00-14:30  Team-synk på progress
  Deadline: #88 ready för user-testing

TORSDAGEN 17 SEPT:
  09:00-12:00  User-testing av #88-#89 flow
  14:00-15:00  Bug-fix session

FREDAGEN 18 SEPT:
  09:00-10:00  Final testing
  14:00-16:00  CTO-DEMO KÖRNING
  Deadline: Allt feature-complete eller känd fallback

VECKA-SLUT:
  18:00+  Post-mortem + nästa sprint planning förberedelse
```

**REGLER:**
- Dag för dag breakdown
- Format: Tid - Möte/deadline, Vad
- Deadline = när måste detta vara klart
- Möten = både interna och externa (API möte)

**MÅSTE innehålla:**
- ✅ Kritiska möten denna vecka
- ✅ Deadline per dag
- ✅ CTO-demo tid (om denna vecka)

**FÅR INTE innehålla:**
- ❌ "Slacka", "pausa"
- ❌ Personliga möten

**FOOTER:** `Källa: Kalender + punkt ⑬ (nästa steg) ✅`

---

### SLIDE ⑫B: Milestones (om behövs)

**FORMAT:** Numrerad lista

**INNEHÅL:**
```
MILESTONES:

✅ Idag (Måndag): API-kontrakt möte avklarat
   Vad: Erik + Björn fastslår format, typ, endpoints
   Ägare: Erik
   Verifikation: #99 issue innehåller JSON-schema

⚠️ Imorgon (Tisdag): API dokumenterad i GitHub
   Vad: Formell dokumentation (inte bara PR)
   Ägare: Erik
   Verifikation: Frontend kan läsa specifikationen

🟢 Denna vecka (Onsdag): #88-#89 ready för test
   Vad: Testbar kod, inga större bugs
   Ägare: Björn + Tomac
   Verifikation: User-testing kan börja onsdag 08:00

🎯 Vecka-slut (Fredag): CTO-demo körbar
   Vad: Feature-complete eller känd fallback
   Ägare: Alla
   Verifikation: Demo-körning lyckas
```

---

## 📝⑬ NÄSTA STEG (1-2 slides)

### SLIDE ⑬A: Handlingsplan direkt efter mötet

**FORMAT:** Numrerad lista med tid + verifikation

**INNEHÅL:**
```
HANDLINGSPLAN:

INOM 1 TIMMA EFTER MÖTET:
[ ] 1. Erik: Uppdatera GitHub issue #99 med API-kontrakt
    Verifikation: Issue-description innehåller JSON-schema

[ ] 2. Zaida: Uppdatera Project Board — flytta #85 till "Next"
    Verifikation: Project Board visar #85 i Next-kolumnen

IDAG (före 14:00 möte):
[ ] 3. Björn: Review mock-API-setup för #88 testing
    Verifikation: Björn säger "ready" i #88-kommentarer

[ ] 4. Erik: Genomför security-testing på #95
    Verifikation: Erik mergear #95 eller sätter label "blocked-security"

IMORGON:
[ ] 5. Rasha: Starta #87 test-framework-implementation
    Verifikation: Branch #87-branch skapad + första commit pushad

[ ] 6. Tomac: Börja pairing-session med Björn på #88
    Verifikation: Commit pushad från #88-branch

DENNA VECKA:
[ ] 7. Erik: Genomför JNA-kontrakt-möte med Native (idag eller imorgon)
    Verifikation: Issue-comment i GitHub med mötes-summering

[ ] 8. Zaida: Code-review alla inkommande PRs från Frontend
    Verifikation: Alla PRs har review-kommentar (lgtm eller ändringar)

[ ] 9. PL: Verifiera Project Board stämmer med Git-branch-status
    Verifikation: Board-kolumner matchar faktisk arbete
```

**REGLER:**
- Numrerad lista (1, 2, 3...)
- Tidsgrupp: Inom 1h | Idag | Imorgon | Denna vecka
- Format: Nummer. Namn: Action
- MÅSTE ha verifikation (hur vet vi att det är klart?)
- Verifikation = GitHub-verifierbar (inte "vi tror")

**MÅSTE innehålla:**
- ✅ Konkreta GitHub-åtgärder (issue-update, branch-create, PR-create)
- ✅ Ägare för varje åtgärd
- ✅ Deadline (samma dag, imorgon, denna vecka)
- ✅ Verifikation-punkt (hur vet vi det är klart?)

**FÅR INTE innehålla:**
- ❌ Vague tasks ("vi ska jobba på...")
- ❌ Åtgärder utan ägare
- ❌ "Vi hoppas..." (bara konkreta saker)

**FOOTER:** `Baserat på punkt ③-⑫ (status, prioritering, plan) ✅`

---

## 📝⑭ FRÅGOR TILL PL (1 slide)

### SLIDE ⑭A: Öppna frågor för PL-svar

**FORMAT:** Numrerad lista med prioritering

**INNEHÅL:**
```
ÖPPNA FRÅGOR FÖR PL-SVAR:

IDAG-SVAR BEHÖVS (höga prioriteten):

1. SCOPE — Ska #84 (Asset allocation chart) in i denna sprint?
   VARFÖR VIKTIG: Påverkar Frontend-kapacitet (+ 8 timmar)
   IMPAKT: Om JA → flytta #85 till nästa vecka

2. PRIORITERING — Om #95 mergea idag, kan vi skippa #87?
   VARFÖR VIKTIG: Kan spara 8 timmar Backend-testning
   IMPAKT: Säkerhets-testing vs testramverk-investering

3. SCOPE — Responsive dashboard (#86): krävs desktop-version också?
   VARFÖR VIKTIG: Påverkar Native-tidsuppskattning (+ 12 timmar)
   IMPAKT: Om JA → omöjligt denna vecka

IDAG-SVAR NICE-TO-HAVE (diskussions-frågor):

4. PROCESS — Ska mötet nästa vecka starta med Code Review eller Retrospekt?
   VARFÖR VIKTIG: Påverkar agenda (40min skillnad)

5. PROCESS — Ska vi döpa om branches enligt naming-convention?
   VARFÖR VIKTIG: CI/CD-fokus eller flexibilitet?
```

**REGLER:**
- MAX 5-6 frågor per möte
- Börja med "IDAG-SVAR BEHÖVS" (höga prioriteten)
- Avsluta med "IDAG-SVAR NICE-TO-HAVE" (diskussions-frågor för senare)
- Format: Nummer. KATEGORI — Fråga + VARFÖR VIKTIG + IMPAKT
- PL måste kunna svara direkt (inte "vi återkommer")

**MÅSTE innehålla:**
- ✅ Öppna frågor från teamet
- ✅ PL-beslut som saknas
- ✅ Scope-frågor ("ska vi inkludera X?")
- ✅ Prioritering (vad ska PL svara på IDAG)

**FÅR INTE innehålla:**
- ❌ Retoriska frågor
- ❌ "Vi undrar om..." (bara konkreta frågor)
- ❌ >6 frågor

**FOOTER:** `Källa: Team-feedback under mötet ✅`

---

## 🔗 HUVUD-REGEL: VARJE SLIDE HAR ETT SYFTE

**En slide = ETT av dessa:**
1. Status (vad är klart/pågår)
2. Problem (vad blockerar oss)
3. Plan (vad gör vi härnäst)
4. Åtgärd (vem gör vad, när)

**Om en slide blandar två syften → bryta upp den.**

Exempel:
- ❌ "Punkt ①A visar både merged + commits"
- ✅ "①A visar merged PRs, ①D visar commits"

---

## 🔗 MOTSÄTTA: VERIFIKATION-FOOTER

**Varje slide med data MÅSTE ha footer med källa:**

```
RÄTT:
  "Källa: GitHub PRs (merged denna vecka) ✅"
  "Källa: Code review + kapacitet-analys ✅"
  "Källa: GitHub issues + Project Board ✅"

FEL:
  "Källa: GitHub" (för vag)
  "Källa: Underlag" (från vad?)
  Ingen footer (var kom datan ifrån?)
```

**Format:** `Källa: [Vad] ([Tidsram]) [Status: ✅/⚠️]`

---

**Version:** 1.0
**Status:** KRITISK SPECIFIKATION
**Senast uppdaterad:** 2026-09-14
