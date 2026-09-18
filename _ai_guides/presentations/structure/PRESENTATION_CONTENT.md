---
name: presentation_content
description: RETIRED — superseded by monday_meeting/design/SLIDE_DETAIL_SPEC.md
metadata:
  type: retired_reference
  status: retired
  version: 1.0
---

# 📊 PRESENTATION CONTENT — 14 Mötespunkter (①-⑭)

> **RETIRED. DO NOT USE FOR PRODUCTION.** This file uses an older meeting-point
> structure. The only active content authority is
> `monday_meeting/design/SLIDE_DETAIL_SPEC.md`.

**Denna fil definierar ENBART presentationens innehål — vad som ska visas.**

**Denna fil definierar INTE:**
- Hur AI ska tänka (se `AI_BUILD_CHECKLIST.md`)
- Design-regler (se `VISUAL_DESIGN_MANDATORY.md` och `ACCESSIBILITY_NEURODIVERSITY.md`)
- AI-process (se `AI_VERIFICATION_WORKFLOW.md`)

---

## 🚨 ÖVERGRIPANDE REGEL: Presentationen Lär & Samarbetar

Presentationen fyller TRE syften:

1. **TEAMTÄNK** — Inte individuell evaluering
   - Fokus: Vägen till gemensam leverans
   
2. **BRANSCHPEDAGOGIK** — Lär domänvokabulär medan vi arbetar
   - Förklara bara ord som står på sliden
   - Varje branschterm markeras 📚 för att visa lärmål
   
3. **ACTIONBAR HANDLINGSPLAN** — Konkreta nästa steg
   - Punkt ⑬ är en faktisk handlingsplan med ansvarig och tidsram

---

## 📝① SEDAN FÖRRA MÖTET (1-2 slides)

**Syfte:** Vad blev FAKTISKT klart denna vecka?

**MÅSTE INNEHÅLLA:**
- ✅ Konkreta merged PRs denna vecka (alla team)
- ✅ Commits per team-medlem (5-7 dagar tillbaka)
- ✅ Active branches (brancher som haft aktivitet senaste veckan)
- ✅ Stale branches (>3 dagar utan push) — risk-identifiering
- ✅ **ALLA 7 team-medlemmar måste synas** — antingen med arbete eller "Ingen issue denna vecka"

**DATA-KÄLLOR (MANDATORY):**
- Merged PRs denna vecka (GitHub)
- Commits denna vecka (GitHub)
- Branches develop + active (GitHub)

**FORMAT: Tabell per team, INTE checklist**

### ①A: Frontend — Levererat denna vecka
```
| Issue | Titel | Assignad | Status | Merged |
|-------|-------|----------|--------|--------|
| #95 | Security review + merge | Zaida Wiss | ✓ DONE | 2026-09-13 |
| #87 | Test foundation | Björn Boman | ✓ DONE | 2026-09-12 |
```

### ①B: Backend — Levererat denna vecka
```
| Issue | Titel | Assignad | Status | Merged |
|-------|-------|----------|--------|--------|
| #80 | Drift banner merge | Erik Berglund | ✓ DONE | 2026-09-11 |
```

### ①C: Native — Levererat denna vecka
```
| Issue | Titel | Assignad | Status | Merged |
|-------|-------|----------|--------|--------|
| (0 items denna vecka) | — | Pär Lundh, Henrik W. | — | — |
```

**REGEL:** Om någon team-medlem är utan arbete denna vecka, visa:
```
Zaida Wiss — Tilldelads ingen ny issue denna vecka (stöd möjlig)
```

---

## 📝② SPRINTMÅL (1 slide)

**Syfte:** Vad är målet för denna sprint? Vad löser vi?

**MÅSTE INNEHÅLLA:**
- ✅ Övergripande mål (1-2 meningar)
- ✅ Koppling till projekt-roadmap
- ✅ Deadline/CTO-demo-datum

**FORMAT:**
```
SPRINTMÅL DENNA VECKA:

Bekräfta API-kontrakt Frontend ↔ Backend innan slut på vecka.
Etablera testramverk för end-to-end-flow.

DEADLINE: Fredag 17 september (CTO-demo-körning)
```

---

## 📝③ NULÄGE (1 slide)

**Syfte:** Var står vi nu? Progress check.

**MÅSTE INNEHÅLLA:**
- ✅ Procent-färdig per team-område
- ✅ Tidsplan (är vi i tid?)
- ✅ Vad saknas?
- ✅ Blocker-status

**FORMAT:**
```
PROGRESS DENNA SPRINT:

Frontend: ████████░░ 80% (API-kontrakt väntar på Backend)
Backend:  ██████░░░░ 60% (Fokus denna vecka)
Native:   ███████░░░ 70% (Blockerad på Backend-kontrakt)

TIDSPLAN:
• Senaste då vi kan fastslå kontrakt: idag
• Senaste då vi kan börja integrering: i morgon
• Deadline leverans: fredag

KRITISKA SAKNADE BITAR:
  🔴 Backend API-definition
  🟠 Test-ramverk
```

---

## 📝④ FRONTEND (1-3 slides)

**Syfte:** Vad jobbar Frontend på? Vad behövs härnäst?

**MÅSTE INNEHÅLLA:**
- ✅ Issues denna sprint per medlem
- ✅ Blockad-status (väntar på vad?)
- ✅ Nästa steg

**FORMAT:**

### ④A: Frontend — Denna sprint
```
| Issue | Titel | Assignad | Status | Blocker |
|-------|-------|----------|--------|---------|
| #88 | Critical interactions | Björn Boman | ◐ PÅG | API-kontrakt |
| #89 | E2E happy path | Tomac Barin | ◐ PÅG | API-kontrakt |
| #85 | Responsive header/nav | Zaida Wiss | ✓ DONE | — |
```

### ④B: Frontend — Operativ handlingsplan (om behövs)
```
NÄSTA STEG:
1. Björn ↔ Backend (Erik): API-kontrakt möte på 14:00 idag
2. Tomac pairing med Zaida: Testa happy path mot mock-API
3. Zaida: Code review #85 innan merge
```

### ④C: Frontend — Beroenden & risker (om behövs)
```
VÄNTAR PÅ:
  🔴 Backend API-definition för #88, #89

RISK:
  🟠 Om API inte klart i morgon → 1 dag försening
```

---

## 📝⑤ BACKEND (1-3 slides)

**Syfte:** Vad jobbar Backend på? Vad är blockerande andra teams?

**MÅSTE INNEHÅLLA:**
- ✅ Issues denna sprint per medlem
- ✅ Blockad-status (väntar på vad?)
- ✅ API-kontrakt-status (definierat? Dokumenterat?)
- ✅ Nästa steg

**FORMAT:**

### ⑤A: Backend — Denna sprint
```
| Issue | Titel | Assignad | Status | Blocker |
|-------|-------|----------|--------|---------|
| #95 | Security review + merge | Erik Berglund | ✓ DONE | — |
| #87 | Test foundation | Rasha Knifdi | ◐ PÅG | — |
| — | API-definition #88-#89 | Erik Berglund | ✓ DONE | — |
```

### ⑤B: Backend — API-kontrakt (om behövs)
```
KONTRAKT-STATUS:
  ✅ POST /user/login — Definierat & dokumenterat
  ✅ GET /user/portfolio — Definierat & dokumenterat
  🟠 POST /transaction/execute — I review, Frontend väntar

NÄSTA STEG:
  Erik: Slutför #99 API-definition idag
```

### ⑤C: Backend — Operativ handlingsplan (om behövs)
```
1. Erik: Avsluta Security review, merge denna dag
2. Rasha: Starta Test foundation, referera design från #87
3. Erik ↔ Frontend möte 14:00 — formalisera API-kontrakt
```

---

## 📝⑥ NATIVE (1-3 slides)

**Syfte:** Vad jobbar Native på? Är de blockerade?

**MÅSTE INNEHÅLLA:**
- ✅ Issues denna sprint per medlem
- ✅ Blockad-status (väntar på vad?)
- ✅ Nästa steg
- ✅ JNA-kontrakt-status (Backend ↔ Native)

**FORMAT:**

### ⑥A: Native — Denna sprint
```
| Issue | Titel | Assignad | Status | Blocker |
|-------|-------|----------|--------|---------|
| #86 | Responsive dashboard | Henrik Westerlund | ◐ PÅG | API-kontrakt |
| — | Ingen ny issue | Pär Lundh | — | — |
```

### ⑥B: Native — JNA-kontrakt (om behövs)
```
VÄNTAR PÅ:
  🔴 Backend API-kontrakt för #86

RISK:
  🟠 Ingen arbete denna vecka (Pär). Kan andra hjälpa med något annat?
```

### ⑥C: Native — Operativ handlingsplan (om behövs)
```
1. Henrik: Vänta på API-kontrakt, planera implementation
2. Pär: Möjlig support på Frontend #88-#89 medan väntar
3. Erik ↔ Native möte imorgon — JNA-kontrakt-uppdatering
```

---

## 📝⑦ BEROENDEN & BLOCKERS (1-2 slides)

**Syfte:** Vilka är blockade? Vilka är kritiska? Vilka risker finns i koden?

**MÅSTE INNEHÅLLA:**
- ✅ Alla aktiva blockers (röd lista)
- ✅ Alla deldependenser (gult — kan lösas denna vecka)
- ✅ Code-review-resultat från alla aktiva branches

**FORMAT: Blockerträd (map-format)**

```
🔴 KRITISKA KEDJOR:

[Foundation Issue]
   ├──→ [Dependent Issue A]
   └──→ [Dependent Issue B]
             ↑
        [Förprovision C] måste mergas först
```

**Eller som tabell:**

```
Issue | Blockerats av | Låser upp | Prioritet | Status
------|---------------|-----------|-----------|--------
#XX   | Ingenting     | #YY, #ZZ  | 🔴 Hög   | ◐ PÅG
#YY   | #XX           | #AA       | 🔴 Hög   | ⏳ Väntar
```

---

## 📝⑧ PRIORITERING & SCOPE (1-2 slides) — FAS-BASERAD ORDNING

**Syfte:** Vad gör vi FÖRST? Vad kommer senare? Vem gör vad? I VILKEN ORDNING?

**MÅSTE INNEHÅLLA:**
- ✅ Fas-baserad ordning (Fas 1 → 2 → 3)
- ✅ **VARJE ITEM: Team + Assignad person**
- ✅ **Varför denna ordning?** (blockers, beroenden, konfliktrisker)
- ✅ Teamregel: "Max 1 aktiv + 1 queued per person"

**FORMAT:**

```
📅 PLANERAD ORDNING (Fas-baserad, blockers + beroenden):

Fas     | Person A          | Person B          | Person C          | Varför denna ordning?
--------|-------------------|-------------------|-------------------|-------------------------------------------
1. Nu   | #87 Test (Zaida)  | #43 API (Tomac)   | #81 Link (Björn)  | Tre kedjor, låg konflikt. #43/#87 låser upp mycket.
2. Merge| #88 Tests (Zaida) | #82 Portfolio     | #85 Responsive    | #82 kräver #43 merged. #85 kan parallelleras.
3. Stab | Stabilisering #88 | #83 Allocation    | #86 Dashboard     | #83 kan startas när #81 mergad (ingen konflikt).
```

---

## 📝⑨ KAPACITET & ESTIMERING (1 slide)

**Syfte:** Passar detta i veckans tid? Är vi överbelastade?

**MÅSTE INNEHÅLLA:**
- ✅ Tillgänglig kapacitet per team
- ✅ Planerat arbete denna vecka
- ✅ Bild: OK? Stramt? Överbelastat?
- ✅ Rekommendation om justering behövs

**FORMAT:**

```
KAPACITET DENNA VECKA:

Frontend:
  Tillgängligt: 45 timmar (3 × 15h/vecka)
  Planerat: 48 timmar (#88, #89, #85, overhead)
  Status: 🟠 LITE STRAMT — kan gå om möten hålls kort

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

---

## 📝⑩ RISKER (1-2 slides)

**Syfte:** Vilka risker kan göra sprintplanen misslyckas? Vad kan gå fel?

**MÅSTE INNEHÅLLA:**
- ✅ Risken (vad kan gå fel?)
- ✅ Sannolikhet & konsekvens
- ✅ Hantering/mitigation (vad gör vi åt det?)
- ✅ Code-review-fynd som klassificeras som risker

**FORMAT:**

```
🔴 RISK — API-kontrakt inte klart denna vecka
   SANNOLIKHET: Låg (Erik redan på väg)
   KONSEKVENS: Frontend + Native får 2 dagar försening
   MITIGATION: Erik + Björn möte IDAG 14:00 för att fastslå kontrakt
   BACKUP: Mockad API redan tillgänglig för Björn att testa mot

🟠 RISK — Zaida överbelastad (5 issues denna vecka)
   SANNOLIKHET: Medel (mycket code-review på #88-#89)
   KONSEKVENS: Retard på #85, eller kvalitetsfall
   MITIGATION: Tomac + Björn pairing på #88 denna vecka
   BACKUP: Flytta #85 till nästa vecka
```

---

## 📝⑪ TEKNISKA BESLUT (1 slide)

**Syfte:** Vilka arkitektur-beslut behövs denna vecka? Vad fastslår vi?

**MÅSTE INNEHÅLLA:**
- ✅ Beslut som måste fattas denna vecka
- ✅ Var beslut påverkar design/scope
- ✅ Code-review-fynd som driver beslut
- ✅ Ägare för varje beslut

**FORMAT:**

```
TEKNISKA BESLUT DENNA VECKA:

🟢 BESLUT ① — API-kontrakt format
   BESLUT: RESTful med JSON request/response (redan validerat)
   ÄGARE: Erik (Backend-lead)
   DATUM: Idag 14:00
   DOKUMENTATION: #99 GitHub issue
   PÅVERKAN: Frontend (#88-#89), Native (#86)

🟠 BESLUT ② — Test-ramverk
   BESLUT: Vitest för unit-test, Playwright för E2E
   ÄGARE: Rasha (Backend-lead)
   DATUM: Denna dag
   DOKUMENTATION: #87 GitHub issue
   PÅVERKAN: Alla teams

🟡 DISKUSSION — Branch-strategi vid merge
   FRÅGA: Merge #95 till main direkt eller via release-branch?
   ÄGARE: Erik + PL
   DEADLINE: Innan #95 klar (idag)
   PÅVERKAN: Release-process, deployment-tidslinje
```

---

## 📝⑫ SPRINTPLAN (1-2 slides)

**Syfte:** Timeplanen veckan. Möten, deadlines, milestones.

**MÅSTE INNEHÅLLA:**
- ✅ Daglig timplan (möten, kritiska milestones)
- ✅ Deadline per issue
- ✅ Demo-tidslinje (CTO-demo fredag?)

**FORMAT:**

```
MÅNDAGEN 14 SEPT:
  09:00-10:30  Sprint Planning-möte
  14:00-14:30  Erik ↔ Frontend API-möte (#99)
  Deadline: #95 security-testing klar

TISDAGEN 15 SEPT:
  10:00-10:30  Erik ↔ Native JNA-kontrakt-möte
  Deadline: API-kontrakt formell dokumenterad i GitHub

ONSDAGEN 16 SEPT:
  08:00-09:00  Code review för #88-#89 (API-version)
  14:00-14:30  Team-synk på progress
  Deadline: #88 ready för user-testing

TORSDAGEN 17 SEPT:
  09:00-12:00  User-testing av #88-#89 flow
  14:00-15:00  Bug-fix session

FREDAGEN 18 SEPT:
  09:00-10:00  Final testing
  14:00-16:00  CTO-DEMO KÖRNING
  Deadline: Allt feature-complete eller känd fallback
```

---

## 📝⑬ NÄSTA STEG (1-2 slides — handlingsplan)

**Syfte:** Konkreta åtgärder efter mötet. Vem gör vad? Tidsram?

**MÅSTE INNEHÅLLA:**
- ✅ Konkreta GitHub-åtgärder (PR, issue, label, move-board)
- ✅ Ägare för varje åtgärd
- ✅ Deadline (samma dag/imorgon/denna vecka)
- ✅ Verifikation-punkt (hur vet vi att det är klart?)

**FORMAT:**

```
HANDLINGSPLAN DIREKT EFTER MÖTET:

INOM 1 TIMMA:
  [ ] Erik: Uppdatera GitHub issue #99 med API-kontrakt
      Ägare: Erik
      Verifikation: Issue-description innehåller JSON-schema

  [ ] Zaida: Uppdatera Project Board — flytta #85 till "Next"
      Ägare: Zaida
      Verifikation: Project Board visar #85 i Next-kolumnen

IDAG (före 14:00 möte):
  [ ] Björn: Review mock-API-setup för #88 testing
      Ägare: Björn
      Verifikation: Björn säger "ready" i #88-kommentarer

  [ ] Erik: Genomför security-testing på #95
      Ägare: Erik
      Verifikation: Erik mergear #95 eller sätter label "blocked-security"
```

---

## 📝⑭ FRÅGOR TILL PL (1 slide — SISTA)

**Syfte:** Öppna frågor som teamet behöver PL för att besvara.

**MÅSTE INNEHÅLLA:**
- ✅ Öppna frågor från teamet
- ✅ PL-beslut som saknas
- ✅ Scope-frågor ("ska vi inkludera X?")
- ✅ Tid för diskussion allokerad

**FORMAT:**

```
ÖPPNA FRÅGOR FÖR PL-SVAR:

❓ SCOPE — Ska #84 (Asset allocation chart) in i denna sprint?
   VARFÖR VIKTIG: Påverkar Frontend-kapacitet
   IDAG-SVAR BEHÖVS: Ja (för att justera prioritering)

❓ PRIORITERING — Om #95 mergea idag, kan vi skippa #87 test-framework?
   VARFÖR VIKTIG: Kan spara 8 timmar Frontend
   IDAG-SVAR BEHÖVS: Ja

❓ SCOPE — Responsive dashboard (#86) — krävs desktop-version också?
   VARFÖR VIKTIG: Påverkar Native-tidsuppskattning
   IDAG-SVAR BEHÖVS: Ja (för definition-clarity)

❓ RISK — Vad gör vi om #88 API inte klart idag?
   VARFÖR VIKTIG: Fallback-plan behövs
   IDAG-SVAR BEHÖVS: Ja (backup-strategi)
```

**REGLER:**
- MAX 5-6 frågor per möte
- Börja med "IDAG-SVAR BEHÖVS: Ja" — de höga prioriteten
- Avsluta med "IDAG-SVAR BEHÖVS: Nej" — diskussions-frågor för framtida möten
- PL måste kunna svara direkt, inte "vi återkommer"

---

**Version:** 1.0  
**Senast uppdaterad:** 2026-09-14  
**Status:** PRODUCTION — Presentationens innehål-specifikation
