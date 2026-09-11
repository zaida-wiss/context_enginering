# Sprint Planering - Team 1 Vägledning

**Denna guide hjälper dig planera sprintar som är fokuserade, realistiska och levererar värde.**

---

## 📋 Sprintplanering Checklist - KÖR DETTA VARJE VECKA

### 🟢 FÖRE PLANERING (Måndag morgon)

**Tid:** 60 minuter före sprintmöte  
**Ansvarig:** Team Lead / Scrum Master / AI

---

## 🔴 KRITISKT — AI MÅSTE LÄSA ALLT DETTA:

**Innan AI presenterar status, måste den läsa i denna ordning:**

```
1. 📋 MÖTESPROTOKOLLET (SENASTE)
   Länk: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/
   ├─ Vad diskuterades förra veckan?
   ├─ Vilka beslut togs? (B = beslut)
   ├─ Vilka action items? (I = information)
   ├─ Feedback från PL/CTO?
   ├─ Risker som identifierades?
   └─ Vad sa vi skulle fokuseras denna vecka?

2. 📊 GIT LOG (denna vecka)
   $ git log --oneline --since="1 week ago"
   ├─ Vilka commits kom in?
   ├─ Vilka PRs mergades?
   └─ Vad blev klart?

3. 📈 GITHUB PROJECT BOARD (denna vecka)
   ├─ Vilka issues är Done?
   ├─ Vilka är In Progress?
   ├─ Vilka blockers finns?
   └─ Status för denna veckas fokus?

4. ⏰ DEADLINES & FOKUS (från SPRINT_FOCUS_TIMELINE.md)
   ├─ Vilken vecka är det?
   ├─ Vad är fokus denna vecka?
   ├─ Vilka deadlines gäller?
   └─ Vad måste vi leverera?

5. 🚨 RISKER (från mötesprotokollet + Google Sheets)
   ├─ Vilka risker identifierades förra veckan?
   ├─ Är de lösta?
   ├─ Nya risker denna vecka?
   └─ Vilka är kritiska?
```

---

- [ ] **1. Läs Mötesprotokollet FÖRST (via RAW-LÄNK)**
  - **🔴 KRITISKT:** AI måste kunna läsa mötesprotokollet direkt
  - Google Docs länk: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/
  - **RAW-EXPORT LÄNK (för AI):** `https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt`
  
  **🟢 OPTIMAL: Dela Raw-länken med AI**
  ```
  Du: "Läs detta mötesprotokollet från raw-länken:
  https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt
  
  Sedan: Förbered FÖR mandagsmötet"
  ```
  
  **FÖRDELAR MED RAW-LÄNK:**
  ✅ AI kan läsa direkt (ingen copy-pasta behövs)
  ✅ Alltid aktuell (AI läser senaste version)
  ✅ Öppen för alla som har länken
  ✅ Snabbare och enklare

  ---

  **🔴 KRITISKT: AI MÅSTE SÄGA OM DEN INTE KAN LÄSA MÖTESPROTOKOLLET!**

  **Om AI inte kan läsa mötesprotokollet, måste den TYDLIGT säga:**
  
  ```
  ❌ "Jag kan inte läsa mötesprotokollet från länken (behöver autentisering).
  
  🔴 UTAN mötesprotokollet kan jag inte förbered mötet ordentligt!
  
  LÖSNING: Copy-pasta helt innehållet från Google Docs här, så kan jag:
  - Se vilka BESLUT som togs
  - Se vilka ACTION ITEMS som ska följas upp
  - Se feedback från PL/CTO
  - Förstå överenskomna prioriteringar
  
  Väntar på mötesprotokollet innan jag fortsätter."
  ```

  **AI SKA ALDRIG:**
  - ❌ Fortsätta utan mötesprotokollet
  - ❌ Låtsas att den läst det
  - ❌ Gissa vad som diskuterades
  - ❌ Skapa sprint-plan baserad på git log ensamt

  **AI SKA ALLTID:**
  - ✅ Säga tydligt "Jag behöver mötesprotokollet"
  - ✅ Förklara VARFÖR det är kritiskt
  - ✅ Vänta på mötesprotokollet
  - ✅ SEDAN förbered mötet med full kontext
  
  - Format: I = Information, B = Beslut
  - **DETTA är källan till vad som diskuterades förra veckan**
  - Vilka action items har vi?
  - Vilka beslut togs? (MÅSTE respekteras denna vecka!)
  
- [ ] **2. Se över vad som är gjort** (från mötesprotokollet + git)
  - Kör `git log --oneline --since="1 week ago"`
  - Vilka commits kom in förra sprinten?
  - Matcherar commits med mötesprotokollets action items?
  - Vad blev inte klart? (Lägg tillbaka i backlog)
  
- [ ] **3. Granska denna veckas fokus** (från mötesprotokollet + SPRINT_FOCUS_TIMELINE.md)
  - Vad sa vi skulle fokuseras denna vecka? (se mötesprotokollet)
  - Matchar mötesprotokollet med SPRINT_FOCUS_TIMELINE.md?
  - Vilka deadlines gäller denna vecka?
  
- [ ] **4. Uppdatera Project Board status**
  - Rapportera vad som är gjort (mark issues Done)
  - Notera blockers från förra sprinten (use labels)
  - Uppdatera fokus-område för denna vecka (add labels)
  - **Verifiera att status i Project Board matchar mötesprotokollet**

- [ ] **5. Kolla deadlines & risker**
  - Vilka deadlines nämnde mötesprotokollet?
  - Vilka risker identifierades förra veckan?
  - Är de lösta? Nya denna vecka?
  - Canvas-inlämningar denna vecka?

---

### 🟡 SPRINTPLANERING (Måndag 09:00-12:00)

**Deltagare:** Hela Team 1 (backend, frontend, native)  
**Resultat:** Sprint backlog i GitHub/Project board

---

## 🎯 STRUKTUR: NULÄGE → MÅL → FRAMGÅNGSKRITERIER

**Varje sprintmöte MÅSTE innehålla dessa tre delar (i denna ordning):**

### 📊 DEL 1: NULÄGE (Status från förra sprint) — 10 min

Team Lead presenterar:
```
NULÄGE:
├─ Vad blev klart förra veckan? (commits från git log)
├─ Vad blev INTE klart? (varför? vilka blockers?)
├─ Vilka risker identifierades förra veckan?
├─ Vilken feedback fick vi från PL/CTO?
└─ Hur är vi ställda mot deadlines?

EXEMPEL:
✅ Login form fungerar (från PR #46)
❌ Risk metrics inte klara (blocked by API)
⚠️ Performance metrics försämrades (Lighthouse 75→70)
📝 Feedback: "Vi behöver mer tests"
📅 CTO-deadline: 24 sep (11 dagar kvar, på rätt väg)
```

### 🎯 DEL 2: MÅL FÖR DENNA SPRINT (Vad ska vi försöka uppnå?) — 15 min

Team Lead presenterar:
```
MÅL DENNA SPRINT (Vecka X):

Från SPRINT_FOCUS_TIMELINE.md:
"V6: Kunna visa CTO att kärnflödet fungerar"

För att nå det måste vi denna vecka:
1. ✅ Risk metrics (backend) - MÅSTE vara klart
2. ✅ FX converter (backend) - MÅSTE vara klart
3. ✅ Test coverage 70% - MÅSTE vara klart
4. 🟡 Portfolio optimization (frontend) - om tid

Resultat om vi lyckas:
- Vi kan demot kärnflödet för CTO
- Vi har 70%+ test coverage
- Vi är redo för CTO-feedback session

Resultat om vi INTE lyckas:
- Vi missar CTO deadline → Sämre intryck
- Vi är i backlog och måste in nästa vecka igen
- Vi kan inte gå vidare till kvaldemo-prep
```

### ✅ DEL 3: FRAMGÅNGSKRITERIER (Hur vet vi att vi lyckades?) — 5 min

```
FRAMGÅNGSKRITERIER - Sprint är LYCKAT om:

✅ Risk metrics är 100% klara (PR merged, tests pass)
✅ FX converter är 100% klara (PR merged, tests pass)
✅ Test coverage är 70%+ (CI rapporterar det)
✅ Kärnflödet kan demos (login → portfolio → allocate)
✅ All dokumentation uppdaterad (README, decisions)
✅ Git history är tydlig (commits i rätt format)

VARNING-TECKEN (Sprint är i risk om):
⚠️ Risk metrics eller FX-converter är < 80% klara
⚠️ Test coverage sjunker (< 60%)
⚠️ Blockers identifieras utan mitigation
⚠️ Pull requests inte reviewade i tid

MISSLYCKANDE (Sprint är FAILED om):
❌ Risk metrics eller FX-converter inte klara
❌ Test coverage < 60%
❌ Kärnflödet kan INTE demoas
❌ Git history är rörig/omorganiserad
```

---

#### Steg 1: Presentera Fokus (15 min)
Team Lead presenterar:
- **NULÄGE:** Vad blev klart/ej klart förra veckan?
- **MÅL:** Vad ska vi försöka uppnå denna vecka?
- **FRAMGÅNGSKRITERIER:** Hur vet vi att vi lyckades?
- **RISK DASHBOARD:** Status per team (färgkodad)
- Vilka deadlines gäller?

---

### 🚨 RISK DASHBOARD (Per Team + Färgkodning)

**Presenteras på mötet som ett tydligt dashboard:**

```
┌─────────────────────────────────────────────────────────┐
│           🚨 RISK DASHBOARD — Vecka 6                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  FRONTEND TEAM                    Status               │
│  ├─ LoginForm: ✅ 100% DONE        🟢 ON TRACK        │
│  ├─ Portfolio Overview: 80% done   🟠 SLIGHT DELAY    │
│  ├─ Test Coverage: 45% (need 70%)  🔴 CRITICAL        │
│  ├─ Performance (Lighthouse): 75   🟠 NEEDS WORK      │
│  └─ Blockers: Waiting on CSS vars  🟠 MINOR BLOCKER   │
│                                                         │
│  BACKEND TEAM                     Status               │
│  ├─ Risk Metrics: 40% done         🔴 CRITICAL        │
│  ├─ FX Converter: 30% done         🔴 CRITICAL        │
│  ├─ API Endpoints: 60% done        🟠 ON TRACK        │
│  ├─ Blockers: Swagger docs missing 🔴 BLOCKER         │
│  └─ DB Migrations: Not started     🟠 RISK            │
│                                                         │
│  NATIVE TEAM                      Status               │
│  ├─ Volatility Calc: 50% done      🟢 ON TRACK        │
│  ├─ Max Drawdown: 30% done         🟠 SLIGHT DELAY    │
│  ├─ Performance: Good              🟢 ON TRACK        │
│  ├─ Blockers: None                 🟢 CLEAR           │
│  └─ Tests: 80% coverage            🟢 GOOD            │
│                                                         │
│  OVERALL SPRINT STATUS:            🟠 AT RISK         │
│  (Backend kritisk, andra ok)                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

#### Förklaring av Färgkoder:

| Färg | Betydelse | Vad Det Betyder | Åtgärd |
|------|-----------|-----------------|--------|
| 🟢 GRÖN | ON TRACK | Ligger i fas, ingen risk | Fortsätt så! |
| 🟠 ORANGE | SLIGHT DELAY | Börjar bli lite bråttom | Fokusera denna vecka |
| 🔴 RÖD | CRITICAL | Kritisk, riskerar blocker | MÅSTE prioritera NU |

**Exempel på varje nivå:**

```
🟢 GRÖN — LoginForm 100% done
   Status: Klart, testat, merged, inga blockers
   Risk: 0%
   Åtgärd: Ingen, gå vidare

🟠 ORANGE — Portfolio Overview 80% done
   Status: Nästan klart men slow progress
   Risk: Kan bli blocker om inte fokuseras
   Åtgärd: Allokera extra timmar denna vecka

🔴 RÖD — Risk Metrics 40% done (MÅSTE klart denna vecka!)
   Status: Långt bakom, blockar andra
   Risk: Kommer ALDRIG klart om ingenting ändras
   Åtgärd: ALLT team fokuserar på detta IDAG
          Pausera allt annat
          Pair programming if needed
          Escalera till PL om ej löst
```

---

#### Vilka Risker Ska Visas?

**Per team, visa:**
- 📊 Varje issue + progress (% done)
- 🎯 Beräknad färg (🟢/🟠/🔴)
- 🚫 Blockers (explicit)
- ⏱️ Estimat vs faktisk tid använd
- 📅 Tid kvar till deadline

**Exempel Risk-Analys:**

```
BACKEND: Risk Metrics

📊 Status: 40% done (12h använt av 16h estimat)
⏱️ Tid kvar: 3 dagar
✅ Estimat vs faktisk: OK så långt (12h vs 12h)
🚫 Blocker: Swagger docs från API team (ORANGE)
🎯 Färg: 🔴 RÖD (kommer inte klart om ingenting ändras)

VARFÖR RÖD?
- 40% done × 3 dagar = max 50-60% done
- Vi behöver 100% klart för CTO deadline
- Blockern (Swagger) förhindrar full progress

ÅTGÄRD:
1. API team: PRIORITY! Swagger docs idag
2. Backend team: Pair programming imorgon
3. Cut scope om needed: Enbart kritiska metrics
4. Update PL if still at risk på tisdag
```

---

### 👥 VAD FÅR VARJE LITET TEAM VID MÖTET?

**De tre små teamen (Frontend, Backend, Native) får TEAM-STATUS för sitt område:**

---

## FRONTEND TEAM — DIN TEAM STATUS:

**ISSUES & STATUS:**
```
Issue #24 - LoginForm
  └─ Status: ✅ 100% DONE
     ├─ Tests: Pass
     ├─ Code review: Approved
     └─ Merged: Yes

Issue #42 - Portfolio Overview
  └─ Status: 75% done (ON TRACK)
     ├─ Estimat: 16h
     ├─ Använt: 12h
     ├─ Blockers: Väntar CSS vars från design
     └─ Next: Tests this week

Issue #50 - Test Coverage
  └─ Status: 45% done (RISK)
     ├─ Estimat: 20h (totalt)
     ├─ Använt: 10h
     ├─ Problem: Tests tar längre än estimerat
     └─ Impact: May not hit 70% target
```

**HUR VI KAN HJÄLPA:**
```
Blockrar:
├─ Design CSS vars - Vem kan prioritera från design IDAG?
├─ Tests komplexare - Vem kan pair programming imorgon?
└─ Performance work - Native team kan support (de är klara)

Lösningar:
├─ Pair programming på tests (intern eller external help?)
├─ Omfördela: Vem tar vad denna vecka?
├─ Cut scope: Skip nice-to-have polish denna vecka?
└─ Support: Backend team kan review CSS när den kommer

Fokus denna vecka: Tests är viktiga för DoD
```

---

## BACKEND TEAM — DIN TEAM STATUS:

**ISSUES & STATUS:**
```
Issue #52 - Risk Metrics
  └─ Status: 40% done (🔴 KRITISK!)
     ├─ Estimat: 16h
     ├─ Använt: 12h
     ├─ BLOCKER: Swagger docs saknas från API team
     └─ Impact: MÅSTE klart för CTO deadline
     
Issue #53 - FX Converter
  └─ Status: 30% done (🟠 AT RISK)
     ├─ Estimat: 12h
     ├─ Använt: 4h
     ├─ Blockers: Risk Metrics får prioritet
     └─ Impact: May slip to next week

Issue #47 - API Endpoints
  └─ Status: 60% done (ON TRACK)
```

**HÖG PRIORITET DENNA VECKA:**
```
🔴 Risk Metrics MÅSTE klart för CTO deadline
   - API team: Swagger docs ASAP?
   - Backend: Pair programming om Swagger kommer?
   - Native: Kan ni verify calculations?
   - Frontend: Kan ni test Risk Metrics API?
```

**HUR VI KAN HJÄLPA:**
```
Blockers:
├─ Swagger docs saknas - Vem fixar? Idag?
└─ Risk Metrics komplexare - Behöver support?

Lösningar:
├─ Pair programming med Native om Swagger klara?
├─ Frontend kan help test API endpoints
├─ Native kan verify calculations
├─ Omfördela: Cut FX scope denna vecka?
└─ Fokus: Risk Metrics är #1 prioritet

Observation: Risk Metrics är CRITICAL för deadline
```

---

## NATIVE TEAM — DIN TEAM STATUS:

**ISSUES & STATUS:**
```
Issue #88 - Volatility Calculations
  └─ Status: 50% done (ON TRACK 🟢)
     ├─ Estimat: 16h
     ├─ Använt: 8h
     ├─ Blockers: None
     └─ Tests: 80% coverage (good!)

Issue #89 - Max Drawdown
  └─ Status: 30% done (SLIGHT DELAY 🟠)
     ├─ Estimat: 12h
     ├─ Använt: 4h
     └─ Blockers: None (just slower progress)
```

**HUR VI KAN HJÄLPA ANDRA TEAM:**

```
Status: Du är klar med Volatility snart!
        Kan du hjälpa Backend?

Möjligheter:
├─ Backend: Verify Risk Metrics calculations?
├─ Backend: Pair program på Risk Metrics?
├─ Frontend: Performance optimization support?
└─ Support: Du kan vara "force multiplier" för andra

Fokus denna vecka: 
├─ Finish Volatility (du ligger bra till)
└─ Support Backend Risk Metrics (kritisk för deadline)
```
```

---

### 🤝 TEAM-FOKUSERAD ÅTGÄRD (Inte personlig)

**Istället för personlig feedback, fokusera på HUR VI HJÄLPER VARANDRA:**

```
PROBLEM: Risk Metrics kommer inte klart

PERSONLIG FEEDBACK (❌ UNDVIK):
"Marcus, du är bakom. Du måste fokusera bättre."
→ Defensivt, demotiverande, löser inget

TEAM-FOKUSERAD ÅTGÄRD (✅ GÖR DET HÄR):
"Risk Metrics är KRITISK. Hur kan vi hjälpa?
 ├─ API team: Priority Swagger docs IDAG?
 ├─ Backend team: Pair programming imorgon?
 ├─ Native: Kan ni hjälpa verify calculations?
 ├─ Frontend: Kan ni test Risk Metrics API?
 └─ Alla: Risk Metrics är högsta prioritet denna vecka"

→ Samarbete, lösnings-fokus, gemensamt ansvar

---

PROBLEM: Frontend tests tar längre tid

PERSONLIG FEEDBACK (❌ UNDVIK):
"Alex, du är ineffektiv. Tests borde vara snabbare."
→ Kritiserande, löser inget

TEAM-FOKUSERAD ÅTGÄRD (✅ GÖR DET HÄR):
"Tests tar längre än estimerat. Hur kan vi lösa?
 ├─ Pair programming: Vem kan paja tests imorgon?
 ├─ Omfördela: Kan Native/Backend hjälpa test-arbete?
 ├─ Cut scope: Kan vi skip niceto-have tests denna vecka?
 └─ Support: Vad behövs för att gå snabbare?"

→ Samarbete, lösnings-fokus, "vi löser detta tillsammans"
```

---

#### Steg 1b: Risk Dashboard Presentation (5 min extra)

#### Steg 2: Diskutera Backlog (20 min)
- Vilka 5-7 topprioritet-issues ska vi göra denna vecka?
- Finns det beroenden mellan frontend/backend/native?
- Vilka blockers finns redan? (Se GitHub Project Board eller mötesprotokollet)
- Vilka väntar på feedback från förra vecka?

**Använd denna prioriteringsmall:**
```
🔴 KRITISK - Måste vara klart denna vecka (deadline, blocker)
🟡 HÖG - Bör vara klart denna vecka (MVP, risk)
🟢 MEDIUM - Gör om tid (dokumentation, polish)
🔵 LÅG - Nästa sprint (nice-to-have, future)
```

#### Steg 3: Estimera Kapacitet (15 min)
- Hur många timmar jobbar var och en denna vecka? (40h totalt, minus möten)
- Fredagar = 0h kod (LIA-sök + dialoger)
- Tisdagar = 1,5h möte (12:30-14:00)
- Måndagar = 3h sprintplanering + kickoff
- **Realistisk kodtid = ~35h per vecka per person**

**Exempel för 3-personersteam:**
- Backend (1 person): 35h = 2-3 issues à 10-15h
- Frontend (1 person): 35h = 2-3 issues à 10-15h
- Native (1 person): 35h = 1-2 issues à 15-20h (komplexare)

#### Steg 4: Tilldela Issues (10 min)
- Vilken issue jobbar vem på?
- Är det klar-definierad? (Acceptance criteria, beroenden)
- Vem granskar PRn när det är klart?

**Använd denna template för varje issue:**
```
## [Issue Title]
- **Owner:** @person
- **Scope:** Frontend / Backend / Native
- **Acceptance Criteria:** (3-5 checkboxes)
- **Blockers:** (Väntar på X från Y)
- **Estimate:** 8h / 12h / 16h / 20h
- **Definition of Ready:** Klart-definierad? ✅/❌
```

#### Steg 5: Kickoff (5 min)
- Sammanfattning: Vi gör DETTA denna vecka för att nå DETTA
- Vem kontaktar vem om frågor?
- Nästa möte: Torsdag 14:00 (standup/blockers)
- Push alla issues till Project board

---

## 🎯 Definition of Ready (DoR) - Innan Vi Börjar

En issue är **ready** när den har:

- [ ] **Tydlig titel** - "Add portfolio overview dashboard" (inte "dashboard")
- [ ] **Beskrivning** - Vad är problemet? Vad bygger vi?
  ```
  ## Problem
  Vi saknar en portföljöversikt som visar alla sparformer

  ## Lösning
  Build en dashboard med följande paneler: Total value, allocation chart, risk metrics

  ## Acceptance Criteria
  - [ ] Dashboard visar ISK, KF, depå tillsammans
  - [ ] Värden är konverterade till SEK
  - [ ] Komponenten är TypeScript-typed
  ```

- [ ] **Acceptance Criteria** - 3-5 mätbara checkboxes (inte "make it work")
- [ ] **Scope** - Frontend, Backend, Native, eller combo?
- [ ] **Blockers** - Väntar denna issue på något annat?
  - "Väntar på: Backend API för portfolio-data"
  - "Väntar på: FX-konvertering från Native"
  
- [ ] **Estimat** - Hur många timmar? (8/12/16/20h)
- [ ] **Länk till design** - Om UI: länk till mockup/Figma
- [ ] **Länk till arkitektur-beslut** - Om teknisk: länk till DECISIONS.md

**Exempel på READY issue:**
```
## feat(frontend): Add portfolio overview dashboard (#26)

### Problem
User cannot see total portfolio value across all savings forms

### Solution
Build a dashboard that shows:
- Total value (ISK + KF + depå + pension)
- Allocation chart (aktier % vs stabilt %)
- Risk metrics (volatilitet, Sharpe-ratio)
- Values converted to SEK

### Acceptance Criteria
- [ ] Dashboard displays all portfolio data
- [ ] Values are correctly converted to SEK
- [ ] Chart shows allocation breakdown
- [ ] Components are TypeScript-typed
- [ ] CSS modules used (no inline styles)
- [ ] E2E test covers happy path

### Blocks
- Waiting for: Backend portfolio API (#20)
- Waiting for: FX-conversion in native (#17)

### Estimate
16 hours
```

---

## ✅ Definition of Done (DoD) - För PR/Merge

En feature är **klar** när:

### Code
- [ ] Acceptanskriterier är uppfyllda
- [ ] Commits följer format: `type(scope): message (#issue)`
- [ ] Ingen `console.log()`, `TODO`, `FIXME` i kod
- [ ] Linting passerar (`npm run lint`, `mvn clean verify`)

### Testing
- [ ] Unit tests skrivna (min 70% backend, 60% frontend)
- [ ] Integration tests för backend-changes
- [ ] E2E test för user-facing features
- [ ] Alla tests passerar lokalt

### Documentation
- [ ] README uppdaterad (om arkitektur ändrades)
- [ ] Arkitektur-beslut loggat i DECISIONS.md
- [ ] API dokumenterat (Swagger/OpenAPI om ny endpoint)
- [ ] Eventuella gotchas documenterade

### Review
- [ ] PR är granskat av annan teammedlem
- [ ] Granskare är **INTE** samma som skribent
- [ ] Feedback är adresserad
- [ ] PR är uppdaterad med feedback

### Performance
- [ ] Database-queries är optimerade (ingen N+1)
- [ ] Back-testing < 2 sekunder för 500 instrument
- [ ] UI rendererar snabbt (< 1s initial load)

---

## 🔄 Vecko-Rytm för Sprint Execution

### Måndag
- **09:00-12:00:** Sprintplanering (se ovan)
- **13:00-17:00:** Kickoff + börja jobba på första issue

### Tisdag
- **09:00-12:30:** Utveckling
- **12:30-14:00:** PL-möte (ca 1,5h)
- **14:00-17:00:** Utveckling

### Onsdag
- **09:00-12:00:** Utveckling
- **13:00-17:00:** Utveckling eller individuella möten

### Torsdag
- **09:00-14:00:** Utveckling
- **14:00-15:00:** Standup/blocker-löpning
  - Vem är stuck? Vem kan hjälpa?
  - Kommer något block att påverka slutklocket?
  - Behöver vi skriva saker på detta klart före vecka-slutet?

### Fredag
- **08:00-17:00:** LIA-sök + dialoger (KOD FÖRBJUDET!)
- Dock kan du dokumentera feedback från veckan

---

## 📊 Sprint Metrics - Mät Framsteg

### Burndown Chart
Spåra detta under veckan:
- **Måndag 09:00:** Antal öppna issues
- **Mittväg (onsdag):** Hur många är stängda?
- **Fredag 16:00:** Burndown klart? Hur många issues stängda?

**Mål:** Ingen issues ska ta mer än 16h, så om du planerar 5 issues à 12h bör 2-3 vara stängda vid mittväg

### Velocity (Om Du Vill)
```
Sprint 2: 40 story points gjorda
Sprint 3: 45 story points gjorda
Sprint 4: 50 story points gjorda
→ Team blir snabbare när de får ritm
```

### Blockers & Risks
- **Tracking:** Spåra alla blockers i GitHub Project Board (labels: blockers, risk)
- **Lösa:** Dedikera tid att lösa blockers samma dag (inte nästa vecka!)
- **Preventera:** Om samma blocker uppstår två gånger, åtgärda root cause

---

## 🚨 Vad Gör Vi Om Vi Inte Hinner?

### Mitten av Veckan (Onsdag)
Om vi märker att vi inte hinner:

1. **Identifiera:** Vilka issues kommer inte bli klara?
2. **Prioritera:** Vilka är KRITISKA för denna veckas fokus?
3. **Minska:** Vad kan vi skjuta till nästa vecka?
4. **Ajustera:** Lägg om prioriteringar torsdag morgon

### Torsdag Kvall
- Några issue ska **INTE PUSHES** som half-done
- Bättre: Stäng 4 issues helt än 5 issues at 80%
- Flytta incomplete issues EXPLICIT tillbaka till backlog

### Rapporterad till PL
Tisdags-mötet ska vi kunna säga:
- "Vi gjorde THIS denna vecka ✅"
- "Vi skipade THAT för att fokusera på THIS ✅"
- "Nästa vecka gör vi THAT istället ✅"

**Inte:** "Vi jobbar på X men den är inte klar än" → detta är halvklar arbete

---

## 🏆 Sprint Retro - Efter Sprinten (Frivilligt)

**Tid:** 15 minuter, Fredag 16:30 (efter LIA-sök) eller Måndag 08:00

Frågor:

1. **Vad gick bra denna vecka?**
   - "Vi löste dependencyn snabbt"
   - "Bra kommunikation mellan frontend och backend"

2. **Vad gick dåligt?**
   - "Issue var inte ready-definierad, tog 2 timmar att förstå"
   - "Native-modulen var langsam, vi ska benchmarka tidigare"

3. **Vad bör vi prova nästa vecka?**
   - "Mer detaljerade acceptance criteria"
   - "Pair-programming för komplicerade features"
   - "Daglig 10-min standup för att fånga blockers tidigt"

**Notera:** Inte alla sprintar behöver retro. Bara när något kändes väldigt off.

---

## 📚 Mall: Sprint Backlog för Git Project Board

**Använd denna struktur när du skapar issues i GitHub:**

```markdown
## [TYPE] [Scope]: [Issue Title]

### Description
[Vad bygger vi? Varför?]

### Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

### Blockers
- Waiting for: #20 (Backend API)
- Waiting for: #17 (Native FX module)

### Scope
- Frontend: [x] / [ ]
- Backend: [ ] / [x]
- Native: [ ] / [ ]

### Estimate
8h / 12h / 16h / 20h

### Ready Checklist
- [x] Issue is clearly defined
- [x] AC are measurable
- [x] No hidden dependencies
- [x] Team member assigned

### Branch
feature/#ISSUE-description

### Related
- Design: [Figma link]
- Architecture: DECISIONS.md [ref]
- Similar issue: #XX
```

---

## 🎓 Viktigt: Tävlingen ≠ Betyget

Din betyg BYGGER PÅ:
- Slutleverans (vad du gjort)
- 17 Kursmål (hur bra du gjort det)
- Din Git-historia (vem gjorde vad)

Tävlingsresultatet påverkar **INTE** betyget.

**Fokusera på att:**
1. ✅ Uppfylla alla kursmål
2. ✅ Leverera fungerande system
3. ✅ Dokumentera ordentligt
4. ✅ Spåra individuella bidrag i Git

Vinna tävlingen är bonus, inte målet.

---

**Senast uppdaterad:** 2026-09-04  
**Ansvarig:** Team 1
