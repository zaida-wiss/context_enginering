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

## 🚨 KRITISK REGEL — MÖTESPUNKTS-SYMBOLER

**VARJE slide-rubrik MÅSTE börja med mötespunkts-symbolen så det är OMEDELBAR VISUELL klar vilken mötespunkt sliden tillhör.**

```
❌ FEL:   "Avklarat sedan förra mötet — Frontend"
✅ RÄTT:  "① Avklarat sedan förra mötet — Frontend"

❌ FEL:   "Aktuell status"
✅ RÄTT:  "② Aktuell status"

❌ FEL:   "Frontend"
✅ RÄTT:  "③ Frontend"
```

**REGLER:**
- Symbolen måste vara FÖRST i rubriken
- Två mellanslag mellan symbol och rubrik-text
- Samma symbol för alla sub-slides (t.ex. ①A, ①B, ①C använder alla ①)
- Font: Arial 14pt BOLD (samma som andra headers)

**VARFÖR:** NPF-designen kräver att läsaren omedelbar ser STRUKTUR. Symbolen är visuell ankare.

---

---

## 📝① AVKLARAT SEDAN FÖRRA MÖTET (1-3 slides)

**Rubriker per team (måste matcha mötesprotokollet):**
- Slide ①A: **"Avklarat sedan förra mötet — Frontend"**
- Slide ①B: **"Avklarat sedan förra mötet — Backend"**
- Slide ①C: **"Avklarat sedan förra mötet — Native"**

### SLIDE ①A: Avklarat sedan förra mötet — Frontend

🚨 **NO POWERPOINT TABLES** — Use visual rows/status cards instead (NPF requirement)

**FORMAT:** Visuella rader klassificerad i tre serier: Merged | Pågår | Väntar på review

**STRUKTUR-REFERENS** (Markdown för att visa layout, ALDRIG som PowerPoint-tabell):

| Team | Issue # | Titel | Assignad | Status | Merged/Branch |
|------|---------|-------|----------|--------|---------------|
| [från TEAM_ROSTER] | #[GitHub] | [GitHub] | [GitHub eller 🔄 UNASSIGNED] | ✓/◐/⏳ | [GitHub] |

**RENDERING:** Varje rad visas som ett status-card eller visuell box, INTE som cellerna i en PowerPoint-tabell.

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
  - Exempel: ✅ "#95 Security review · [PERSON_A]" ([PERSON_A] ÄGde det)
  - Exempel: ❌ "#95 Security review · [PERSON_B]" ([PERSON_B] reviewade det, men [PERSON_A] ägde det)

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

**FORMAT:** Visuella rader (identisk struktur som ①A — NO POWERPOINT TABLES)

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

**FORMAT:** Visuella rader (identisk struktur som ①A — NO POWERPOINT TABLES)

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
🔴 KRITISK (Idag 14:00) — [MILESTONE_A]
   VAD: [TEAM_A] + [TEAM_B] fastslår [DECISION]
   VARFÖR: Låser upp [FEATURE_1], [FEATURE_2], [FEATURE_3]
   STATUS: ⏳ INGEN AKTIVITET än
   RISK: Om inte klart idag → [N] dagar försening för [M] teams
   ACTION: [PERSON] möte 14:00 — kan vi unblockera NU?

🟠 HÖGT (Imorgon) — [MILESTONE_B]
   VAD: Formell dokumentation i issue #XX ([FORMAT], [DETAILS])
   VARFÖR: [TEAM_C] + [TEAM_D] behöver detta för [PHASE]
   STATUS: ⏳ Beror på idag's möte
   RISK: [N] dag sen → [IMPACT]
   ACTION: Vilka kan hjälpa [PERSON] med [TASK]?

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

## 📝③ FRONTEND (2-3 slides per mötespunkt)

### MÖTESPUNKT ③ — FRONTEND: DENNA SPRINT & NULÄGE

🚨 **KRITISK: Denna mötespunkt visar ALLA issues denna sprint — både kommande backlog + pågående arbete + blockers + risker**

🚨 **NO POWERPOINT TABLES** — Use visual cards/rows instead (NPF requirement)

**FORMAT:** Visuella status-cards klassificerad på dependencies + status

**STRUKTUR:**

```
PÅGÅR DENNA VECKA (fortsätt från senaste mötet):
  #XX | [FEATURE_A] | [PERSON_A] | ◐ PÅG | Blocker: [FEATURE_B] (#YY)
  #YY | [FEATURE_C] | [PERSON_B] | ◐ PÅG | Blocker: Backend API (#ZZ)

KOMMANDE DENNA SPRINT (från backloggen):
  #AA | [FEATURE_D] | [PERSON_C] | ⏳ BACKLOG | Beror på: #XX
  #BB | [FEATURE_E] | ?? | ⏳ BACKLOG | Beror på: #XX (review)
  #CC | [FEATURE_F] | ?? | ⏳ BACKLOG | Beror på: External blocker

INTE TILLDELAT (Förslag baserat på tidigare arbete):
  [PERSON_X]: [FEATURE_G] — nära tidigare arbete denna område
  [PERSON_Y] + [PERSON_Z]: [FEATURE_H] — pairing för snabbare progress
  [PERSON_W]: Flexibel support — täcka blockers om de dyker upp
```

**KOLUMNER:** Issue # | Titel | Assignad | Status | Blocker/Beroenden

**STATUS-MÄRKEN:**
- ✓ DONE (redan mergad denna vecka)
- ◐ PÅG (aktivt arbete nu)
- ⏳ BACKLOG (väntar på detta sprint, ej startat ännu)
- ?? UNASSIGNED (vi föreslår assignee baserat på tidigare mönster)

**REGLER:**
- Sortera på DEPENDENCIES (vad måste göras först?)
- Visa ALLA issues denna sprint, klassificerat per status
- **Assignad = vem som ÄGer arbetet**
  - Om redan assignad i GitHub: visa namn
  - Om INTE assignad: visa "??" + förslag baserat på tidigare commits
- "Blocker" = vad väntar vi på (issue-nummer eller PR)
- **BEROENDEN MÅSTE VISAS** — använd "Beror på: #X" för clarity

**MÅSTE innehålla:**
- ✅ Issue-nummer (#XX)
- ✅ Titel (2-5 ord)
- ✅ Assignad (namn eller "??" + förslag)
- ✅ Status (✓/◐/⏳)
- ✅ Blocker/Beroenden (tydligt vilken issue som blockerar vilken)
- ✅ **ALLA 7 team-medlemmar — vem gör vad eller "pairing X+Y"**

**FÅR INTE innehålla:**
- ❌ Commit-hash
- ❌ PR-nummer (det är issues vi visar, inte PRs)
- ❌ Estimat i timmar
- ❌ Issues från förra veckan som redan är klara
- ❌ Vaga assignee-förslag ("kanske [PERSON_X]")

**DATA-SOURCES:**
- 📊 **Pågår:** GitHub issues with status "In Progress" + branches with commits senaste 7 dagar
- 📊 **Backlog denna sprint:** GitHub issues labeled "Sprint-X" eller Project Board "Sprint" column
- 📊 **Assignee-förslag:** Git blame + git log för varje issue-kategori (vem jobbade senast på liknande?)
- 📊 **Beroenden:** DEPENDENCY_CHAIN_PLANNING.md klassificering

**FOOTER:** `Källa: GitHub issues + Project Board + Git history ✅ | Assignee-förslag baserat på tidigare arbete`

---

### SLIDE ③B: Frontend — Operativ handlingsplan (om behövs)

**FORMAT:** Numrerad lista

**INNEHÅL:**
```
NÄSTA STEG:
1. [PERSON_A] ↔ Backend ([PERSON_B]): API-kontrakt möte idag 14:00
2. [PERSON_C] pairing med [PERSON_D]: Testa [FEATURE] mot mock-API
3. [PERSON_E]: Code review #XX innan merge
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
  🔴 Backend API-definition för #XX, #YY (blockerar Frontend #AA)
  🟠 Möjlig: [EXTERNAL_RESOURCE] från [TEAM/PERSON]

RISK:
  🟠 Om [BLOCKER] inte klart [WHEN] → [DAYS] dagar försening på [FEATURES]
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

**FORMAT:** Visuella status-cards (identisk som ③A — NO POWERPOINT TABLES)

**KOLUMNER:** Issue # | Titel | Assignad | Status | Blocker

**REGLER:** (identiska som ③A)

---

### SLIDE ④B: Backend — API-kontrakt-status (om behövs)

**FORMAT:** Visuella status-cards med kolumner (NO POWERPOINT TABLES)

**KOLUMNER:**
| Endpoint | Status | Frontend blockar? | Nästa |
|----------|--------|-------------------|-------|
| [ENDPOINT_A] | ✅ Dokumenterad | Nej | Testning |
| [ENDPOINT_B] | 🟠 I review | JA (#XX-#YY) | [PERSON] review idag |

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

**FORMAT:** Visuella status-cards (identisk som ③A — NO POWERPOINT TABLES)

---

### SLIDE ⑤B: Native — JNA-kontrakt-status (om behövs)

**FORMAT:** Text

**INNEHÅL:**
```
VÄNTAR PÅ:
  🔴 Backend API-kontrakt för #XX

MÖJLIG SUPPORT:
  [PERSON_N] kan stödja [TEAM] denna vecka medan väntar
```

---

## 📝⑥ BLOCKERS & DEPENDENCIES (1-2 slides)

### SLIDE ⑥A: Blockerträd — Alla kritiska kedjor

**FORMAT:** ASCII-diagram eller tabell

**INNEHÅL:**
```
🔴 KRITISKA KEDJOR:

[#XX API Foundation]
   ├──→ [#YY Feature A]
   └──→ [#ZZ Feature B]

[#AA Test Foundation]
   └──→ [#BB Feature C]
        └──→ [#CC Feature D]
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

🔴 Backend PR #XX — [SECURITY_ISSUE]
   STATUS: Åtgärdad + testning igång
   LÖST: Ja, ready för merge

🟠 Frontend PR #YY — [DESIGN_ISSUE]
   STATUS: Väntar på [PERSON/TEAM] [DEPENDENCY]
   NÄSTA: [PERSON] reviewar igen när [CONDITION] klart
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
| [RISK_A] ej klart | Låg | [TEAM] får [N]d försening | [PERSON_A] + [PERSON_B] möte idag 14:00 | Pågår |
| [RISK_B] | Medel | [IMPACT] | Pairing [PERSON_C]+[PERSON_D] | Planerat |

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
  Flytta #XX till nästa vecka för att ge [TEAM] andrum.
  [PERSON_N] kan stödja [TEAM] #YY under [BLOCKER]-väntan.
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
  ✅ [PERSON_A]: #XX [FEATURE_A] (låser upp #YY/#ZZ)
  ✅ [PERSON_B]: #AA [FEATURE_B] (låser upp #BB/#CC)
  ✅ [PERSON_C]: #DD [FEATURE_C] (låg konflikt, egen komponent)

  Varför: Tre kedjor, låg mergekonfliktrisk. #XX/#AA låser upp mycket.

🟠 FAS 2 — Efter Fas 1 mergad (pull develop först!):
  [PERSON_A]: #EE [FEATURE_D]
  [PERSON_B]: #FF [FEATURE_E] (kräver #XX merged)
  [PERSON_C]: #GG [FEATURE_F] (kan parallelleras)

  Varför: #FF kräver #XX. #GG oberoende av dataflödet.

🟡 FAS 3+ — Beroenden lösta:
  [PERSON_A]: Stabilisering #EE
  [PERSON_B]: #HH [FEATURE_G] (kan NOW startas)
  [PERSON_C]: #II [FEATURE_H]
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

Exempel ordning för [PERSON_A]:
  1. #XX → merge → pull develop
  2. #YY (depender på #XX) → merge → pull develop
  3. #ZZ (depender på #YY)

Före varje ny issue:
  ☐ Pull/rebase mot develop
  ☐ Kontrollera öppna PRs (vem rör samma komponenter?)
  ☐ Bekräfta dependency är mergad (inte bara "nästan klar")
```

---

## 📝⑩ TEKNISKA BESLUT (1 slide)

### SLIDE ⑩A: Arkitektur-beslut denna vecka

**FORMAT:** Visuella cards/rader (NO POWERPOINT TABLES)

**INNEHÅL:**
```
🟢 BESLUT ① — [DECISION_A]
   FORMAT: [CHOICE_1] (redan validerat)
   ÄGARE: [PERSON_X] (Backend-lead)
   DEADLINE: Idag 14:00
   DOKUMENTATION: #XX GitHub issue
   PÅVERKAN: [TEAM_A] (#YY-#ZZ), [TEAM_B] (#AA)

🟠 BESLUT ② — [DECISION_B]
   FORMAT: [CHOICE_2] + [CHOICE_3]
   ÄGARE: [PERSON_Y] (Backend-lead)
   DEADLINE: Denna dag
   DOKUMENTATION: #BB GitHub issue
   PÅVERKAN: Alla teams

🟡 DISKUSSION — [DECISION_C]
   FRÅGA: [QUESTION] direkt eller via [ALTERNATIVE]?
   ÄGARE: [PERSON_X] + PL
   DEADLINE: Innan #CC klar (idag)
   PÅVERKAN: [IMPACT]
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

✅ Bekräfta [DECISION_A] innan vecka-slut (KRITISK)
   Varför: Låser upp [TEAM_A] och [TEAM_B]
   Ägare: [PERSON_X] ([TEAM_X]) + [PERSON_Y] ([TEAM_Y])
   Deadline: Fredag EOD (eller denna dag för att ha buffer)

✅ Etablera [FOUNDATION_RESOURCE] (FOUNDATION)
   Varför: [TEAM_A] + [TEAM_B] behöver detta för [PHASE]
   Ägare: [PERSON_Z] ([TEAM_Z])
   Deadline: Denna dag eller imorgon

✅ Ge [TEAM_A] + [TEAM_B] möjlighet att börja [NEXT_PHASE]
   Varför: Två teams kan parallellisera när [BLOCKER] är klart
   Ägare: [PERSON_X] + [PERSON_Y] + [PERSON_W]
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
MÅNDAG [DATE_1]:
  09:00-10:30  Sprint Planning-möte
  14:00-14:30  [PERSON_A] ↔ [TEAM_A] [DECISION]-möte
  Deadline: #XX [TASK] klar

TISDAG [DATE_2]:
  10:00-10:30  [PERSON_B] ↔ [TEAM_B] [TASK]-möte
  Deadline: [MILESTONE] formell dokumenterad i GitHub

ONSDAG [DATE_3]:
  08:00-09:00  Code review för #YY-#ZZ ([DESCRIPTION])
  14:00-14:30  Team-synk på progress
  Deadline: #YY ready för [NEXT_PHASE]

TORSDAG [DATE_4]:
  09:00-12:00  [ACTIVITY] av #ZZ flow
  14:00-15:00  [TASK]-session

FREDAG [DATE_5]:
  09:00-10:00  Final [QA]
  14:00-16:00  [DEMO/REVIEW] KÖRNING
  Deadline: Allt [STATE] eller känd fallback

VECKA-SLUT:
  18:00+  [RETROSPECTIVE] + nästa sprint planning förberedelse
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

✅ Idag (Måndag): [MILESTONE_A] avklarat
   Vad: [PERSON_A] + [PERSON_B] fastslår [DECISION]
   Ägare: [PERSON_A]
   Verifikation: #XX issue innehåller [PROOF]

⚠️ Imorgon (Tisdag): [MILESTONE_B] dokumenterad i GitHub
   Vad: Formell dokumentation (inte bara PR)
   Ägare: [PERSON_C]
   Verifikation: [TEAM] kan läsa specifikationen

🟢 Denna vecka (Onsdag): #YY-#ZZ ready för [PHASE]
   Vad: [STATE], inga större bugs
   Ägare: [PERSON_D] + [PERSON_E]
   Verifikation: [ACTIVITY] kan börja onsdag 08:00

🎯 Vecka-slut (Fredag): [DELIVERABLE] körbar
   Vad: [STATE] eller känd fallback
   Ägare: Alla
   Verifikation: [VERIFICATION_METHOD] lyckas
```

---

## 📝⑬ NÄSTA STEG (1-2 slides)

### SLIDE ⑬A: Handlingsplan direkt efter mötet

**FORMAT:** Numrerad lista med tid + verifikation

**INNEHÅL:**
```
HANDLINGSPLAN:

INOM 1 TIMMA EFTER MÖTET:
[ ] 1. [PERSON_A]: Uppdatera GitHub issue #XX med [DECISION]
    Verifikation: Issue-description innehåller [PROOF]

[ ] 2. [PERSON_B]: Uppdatera Project Board — flytta #YY till "[STATUS]"
    Verifikation: Project Board visar #YY i rätt kolumn

IDAG (före [TIDPUNKT] möte):
[ ] 3. [PERSON_C]: Review [RESOURCE] för #ZZ
    Verifikation: [PERSON_C] säger "ready" i GitHub-kommentarer

[ ] 4. [PERSON_D]: Genomför [TASK] på #AA
    Verifikation: [PERSON_D] mergear #AA eller sätter label "[STATUS]"

IMORGON:
[ ] 5. [PERSON_E]: Starta #BB [TASK]-implementation
    Verifikation: Branch #BB-branch skapad + första commit pushad

[ ] 6. [PERSON_F]: Börja pairing-session med [PERSON_G] på #CC
    Verifikation: Commit pushad från #CC-branch

DENNA VECKA:
[ ] 7. [PERSON_H]: Genomför [MEETING] med [TEAM] ([WHEN])
    Verifikation: Issue-comment i GitHub med mötes-summering

[ ] 8. [PERSON_I]: Code-review alla inkommande PRs från [TEAM]
    Verifikation: Alla PRs har review-kommentar

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

1. SCOPE — Ska #XX ([FEATURE_A]) in i denna sprint?
   VARFÖR VIKTIG: Påverkar [TEAM]-kapacitet (+ [N] timmar)
   IMPAKT: Om JA → flytta #YY till nästa vecka

2. PRIORITERING — Om #ZZ mergea idag, kan vi skippa #AA?
   VARFÖR VIKTIG: Kan spara [N] timmar [TASK]
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
