# Sprint Planering - Team 1 Vägledning

**Denna guide hjälper dig planera sprintar som är fokuserade, realistiska och levererar värde.**

---

## 📋 Sprintplanering Checklist - KÖR DETTA VARJE VECKA

### 🟢 FÖRE PLANERING (Måndag morgon)

**Tid:** 60 minuter före sprintmöte  
**Ansvarig:** Team Lead / Scrum Master

- [ ] **1. Verifiera schemat**
  - Öppna SCHEDULE.md och Canvas-kalendern
  - Finns det workshops, blockers eller deadlines denna vecka?
  - Är mötetider korrekt? (Tisdag 12:30-14:00 är fast)
  
- [ ] **2. Se över vad som är gjort**
  - Kör `git log --oneline --since="1 week ago"`
  - Vilka commits kom in förra sprinten?
  - Vad blev inte klart? (Lägg tillbaka i backlog)
  
- [ ] **3. Granska denna veckas fokus** (från SCHEDULE.md)
  - V2: MVP, backlog, arbetsstruktur
  - V3-V5: Fungerande delar, teststatus, README
  - V6: CTO-underlag (arkitektur, beslut)
  - V7: CTO-feedback, scope
  - V9: Kvaldemo-plan + stabilitet
  - V11: Omtag + dokumentation
  - V12: Slutcheck
  
- [ ] **4. Uppdatera Project Board status**
  - Rapportera vad som är gjort (mark issues Done)
  - Notera blockers från förra sprinten (use labels)
  - Uppdatera fokus-område för denna vecka (add labels)

- [ ] **5. Kolla deadlines**
  - Finns det Canvas-inlämningar denna vecka?
  - V6 → 24 sep kl 16:00 (CTO-underlag)
  - V9 → 15 okt kl 17:00 (Demo-plan)
  - V12 → 4 nov kl 15:00 (SLUTLEVERANS)
  - Lägg in i backlog om relevant denna vecka

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

#### Steg 1: Presentera Fokus (10 min)
Team Lead presenterar:
- **NULÄGE:** Vad blev klart/ej klart förra veckan?
- **MÅL:** Vad ska vi försöka uppnå denna vecka?
- **FRAMGÅNGSKRITERIER:** Hur vet vi att vi lyckades?
- Vilka deadlines gäller?
- Vilka risker identifieras? (Se Google Sheets Risker eller mötesprotokollet)

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
