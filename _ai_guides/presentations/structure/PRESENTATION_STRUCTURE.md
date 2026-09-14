---
name: presentation_structure
description: 14 mötespunkter (①-⑭) — ny struktur med team-vyer och tydlig ansvar-indelning
metadata:
  type: reference
  critical: true
  version: 3.0
---

# 📋 PRESENTATION STRUCTURE — 14 Mötespunkter (①-⑭)

**🚨 ÖVERGRIPANDE REGEL: Presentationen Lär & Samarbetar, Rapporterar & Bygger Teamtänk**

Presentationen fyller TRE syften:

1. **TEAMTÄNK** — Inte individuell evaluering
   - Huvudansvarig får ALDRIG betyda ENSAM ansvarig
   - Presentationen ska undersöka: Hur kan teammedlemmar hjälpa, avlasta, paira eller täcka upp för varandra?
   - Fokus: **Vägen till gemensam leverans, inte individuella prestationer**

2. **BRANSCHPEDAGOGIK** — Lär domänvokabulär medan vi arbetar
   - Förklara bara ord som står på sliden
   - Varje branschterm markeras 📚 för att visa lärmål
   - Möten blir lärtillfällen, inte bara statusrapporter

3. **ACTIONBAR HANDLINGSPLAN** — Konkreta nästa steg
   - Punkt ⑬ är inte en checklista utan en faktisk **handlingsplan med ansvarig och tidsram**
   - Allt som sägs ska kunna omsättas direkt på GitHub

---

## 🚨 KRITISKA REGLER

**En mötespunkt ≠ en slide**
- En mötespunkt kan motsvaras av 1-3 (eller fler) slides
- Varje slide märks med samma 📝-symbol för mötespunkten den tillhör
- Presentationen kan ha 20-30 slides — antalet varierar per vecka

**Innan presentationen skapas: Obligatorisk Cross-Team Code & Contract Review**
- Granska actual code i alla aktiva branches/PRs
- Verifiera API-kontrakt (Frontend ↔ Backend)
- Verifiera JNA-kontrakt (Backend ↔ Native)
- Dokumentera avvikelser i relevanta mötespunkter (⑦, ⑩, ⑪)

**VIKTIGT: Team + Assignad ALLTID synlig**
- Varje issue/PR måste visa: `#XX Titel (Team: Frontend/Backend/Native) — Assignad: Namn`
- Inget arbete utan tydlig ägare och team-tillhörighet
- Fallback: Om assignad saknas → "Ej assignad — behöver ägare"

**Ingen checklista — bara faktisk data**
- Slidorna fylls med verklig GitHub-data, inte tomma checkboxes
- Se [MANDATORY_READING_ORDER.md](../MANDATORY_READING_ORDER.md) för vilka GitHub-åtgärder som behövs

---

## 🎬 FRAMSIDA (Ingen 📝-symbol)

**Syfte:** Mötet börjar här. Rena fokus.

**MÅSTE INNEHÅLLA:**
- ✅ Möte-header: "SPRINTPLANERING · TEAM 1" + datum/tid
- ✅ PL-fokus denna vecka (1-2 meningar)
- ✅ Footer: Underlag kontrollerat inför mötet (context_engineering, avanza-team1, Git-status, Issues & PRs, Project Board, Code review-status, Mötesprotokollet)

**FORMAT:**
```
HEADER: SPRINTPLANERING · TEAM 1 | Måndag 14 september · 09:00–10:30

MAIN (70% tom yta):

Fokus denna vecka:
Säkerställa veckans prioriteringar, beroenden
och vägen mot CTO-demo.

FOOTER (litet, 10-12pt):
Underlag: context_engineering ✓ | avanza-team1 ✓ | Git-status ✓ |
Issues & PRs ✓ | Project Board ✓ | Code review: [status] |
Mötesprotokollet: [status]
```

**DESIGN:**
- ✅ 70% tom yta
- ✅ Max 3 textblock
- ✅ Ingen agenda, inga kort, ingen extra info
- ✅ Fokus ligger på PL-fokus-texten

---

## 📝① SEDAN FÖRRA MÖTET (1-2 slides)

**Syfte:** Vad blev FAKTISKT klart denna vecka?

**MÅSTE INNEHÅLLA:**
- ✅ Konkreta merged PRs denna vecka (alla team)
- ✅ Commits per team-medlem (5-7 dagar tillbaka)
- ✅ Active branches (brancher som haft aktivitet senaste veckan, även om det ännu inte mergats till develop, eller inte gjorts någopn PR/rewiew)
- ✅ Stale branches (>3 dagar utan push) — risk-identifiering
- ✅ **ALLA 7 team-medlemmar måste synas** — antingen med arbete eller "Ingen issue denna vecka"

**DATA-KÄLLOR (MANDATORY):**
- 📊 [Merged PRs denna vecka](../data/DATA_SOURCES.md) — GitHub
- 📊 [Commits denna vecka](../data/DATA_SOURCES.md) — GitHub
- 📊 [Branches develop + active](../data/DATA_SOURCES.md) — GitHub

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

**REGEL:** Om någon team-medlem är utan arbete denna vecka, visa det här:
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

## 📝⑦ BEROENDEN & BLOCKERS (1-2 slides, inkl. code-review)

**Syfte:** Vilka är blockade? Vilka är kritiska? Vilka risker finns i koden?

**MÅSTE INNEHÅLLA:**
- ✅ Alla aktiva blockers (röd lista)
- ✅ Alla deldependenser (gult — kan lösas denna vecka)
- ✅ Code-review-resultat från alla aktiva branches

**DATA-SOURCES:**
- 📊 GitHub Project Board
- 🔍 Code review från alla aktiva branches/PRs

**FORMAT:**

### ⑦A: Blockers & Dependencies
```
KRITISKA BLOCKERS (MÅSTE LÖSAS):
  🔴 #88 Frontend väntar på Backend API-definition
       → Löses idag 14:00 (Erik-möte)

  🔴 #86 Native väntar på Backend API-kontrakt
       → Löses imorgon (JNA-möte)

DELBEROENDEN (GÅR ATT ARBETA RUNT):
  🟠 #87 Test foundation väntar på design-review
       → Rasha kan börja implementation, design-review imorgon

LÖSTA BLOCKERS:
  ✅ #95 Security review — mergad
  ✅ #85 Responsive header — mergad
```

### ⑦B: Code Review Findings (om behövs)
```
KRITISKA FYND FRÅN CODE REVIEW:

🔴 RISK — Backend PR #95:
   FYND: SQL-injection risk i user_id-parameter
   STATUS: Erik åtgärdad + testning igång
   LÖST: Ja, ready för merge

🟠 VARNING — Frontend PR #88:
   FYND: Länkad till Backend-API som inte är dokumenterad
   STATUS: Väntar på Erik API-definition
   NÄSTA: Björn reviewar igen när API klart

REKOMMENDATION:
   Låsa PR #88 från merge tills API är formell dokumenterad
```

---

## 📝⑧ PRIORITERING & SCOPE (1 slide)

**Syfte:** Vad gör vi FÖRST? Vad kommer senare? Vem gör vad?

**MÅSTE INNEHÅLLA:**
- ✅ MUST denna vecka (måste göras denna vecka)
- ✅ NEXT nästa vecka (nästa prioritet)
- ✅ LATER (kan vänta)
- ✅ **VARJE ITEM: Team + Assignad person**

**FORMAT:**

```
🔴 MUST DENNA VECKA (Måste göras):

  #95 Security review + merge (Backend, Assignad: Erik) ✓
  #87 Test foundation (Backend, Assignad: Rasha) ◐
  #88 Critical interactions (Frontend, Assignad: Björn) ◐
  CTO-underlag dokumentation (Backend, Assignad: Erik)

🟠 NEXT VECKA (Nästa prioritet):

  #89 E2E happy path (Frontend, Assignad: Tomac)
  #86 Responsive dashboard (Native, Assignad: Henrik)
  Backend/Frontend API-kontrakt (Backend ↔ Frontend, Ägare: Erik)

⚪ LATER (KAN VÄNTA):

  #84 Asset allocation chart (Frontend, Assignad: —)
  #85 Responsive header (Frontend, Assignad: Zaida) [nästan klar]
  Extra polish om demo stabil (Native, Ägare: Pär)
```

**REGEL:**
- Varje item visar: `#XX Titel (Team: X, Assignad: Namn) Status`
- Om assignad saknas → `(Team: X, Assignad: —)`
- Statusmarkörer: ✓ DONE, ◐ PÅG, ? BLOCKERAD, — EJ STARTAD

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

## 📝⑩ RISKER (1-2 slides, inkl. code-review)

**Syfte:** Vilka risker kan göra sprintplanen misslyckas? Vad kan gå fel?

**MÅSTE INNEHÅLLA:**
- ✅ Risken (vad kan gå fel?)
- ✅ Sannolikhet & konsekvens
- ✅ Hantering/mitigation (vad gör vi åt det?)
- ✅ Code-review-fynd som klassificeras som risker

**DATA-KILDER:**
- 🔍 Code review findings (från punkt ⑦)
- 📊 [Risk Register](../../_memory/RISK_REGISTER.md) (om finns)
- 📊 GitHub Project Board divergens (Board status ≠ faktisk Git-status)

**FORMAT:**

### ⑩A: Risk-register
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

🟠 RISK — SQL-injection i #95 review (från code-review)
   SANNOLIKHET: Låg (redan åtgärdad)
   KONSEKVENS: Säkerhetshål om mergad utan test
   MITIGATION: Erik klar med säkerhetstesting idag innan merge
   STATUS: Redan löst, ready för merge

⚪ RISK — Project Board drift (3 issues stämmer inte med Git)
   SANNOLIKHET: Medel
   KONSEKVENS: Oklarhet om prioritering
   MITIGATION: Uppdatera Project Board direkt efter mötet
```

### ⑩B: Rekommendationer (om behövs)
```
ÅTGÄRDER EFTER MÖTET:
1. Erik: Bekräfta API-kontrakt i GitHub issue #99 idag
2. Zaida: Uppdatera Project Board för #88-#89 status
3. Björn + Tomac: Starta pairing-session för #88 denne dag
4. PL: Flytta #85 till Next-kolumnen om framtidskontraktet kräver det
```

---

## 📝⑪ TEKNISKA BESLUT (1 slide, inkl. code-review)

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

CODE-REVIEW-DRIVNA BESLUT:
   • SQL-injection-mitigering i #95 → Fastställd (merge OK)
   • Länking-risk i #88 → Löses när API klart
```

---

## 📝⑫ SPRINTPLAN (1-2 slides)

**Syfte:** Timeplanen veckan. Möten, deadlines, milestones.

**MÅSTE INNEHÅLLA:**
- ✅ Daglig timplan (möten, kritiska milestones)
- ✅ Deadline per issue
- ✅ Demo-tidslinje (CTO-demo fredag?)

**FORMAT:**

### ⑫A: Tidsplan denna vecka
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

VECKA-SLUT:
  18:00+ — Post-mortem + nästa sprint planning förberedelse
```

### ⑫B: Milestones (om behövs)
```
MILESTONES:
  ✅ Monday: API-kontrakt formell (KRITISK)
  ✅ Wednesday: #88-#89 ready för test
  ✅ Friday: CTO-demo körbar
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

IMORGON:
  [ ] Rasha: Starta #87 test-framework-implementation
      Ägare: Rasha
      Verifikation: Branch #87-branch skapad + första commit pushad

  [ ] Tomac: Börja pairing-session med Björn på #88
      Ägare: Tomac + Björn
      Verifikation: Commit pushad från #88-branch

DENNA VECKA:
  [ ] Erik: Genomför JNA-kontrakt-möte med Native (idag eller imorgon)
      Ägare: Erik
      Verifikation: Issue-comment i GitHub med mötes-summering

  [ ] Zaida: Code-review alla inkommande PRs från Frontend
      Ägare: Zaida
      Verifikation: Alla PRs har review-kommentar

  [ ] PL: Verifiera Project Board stämmer med Git-branch-status
      Ägare: PL
      Verifikation: Board-kolumner matchar faktisk arbete
```

**REGEL:** Varje punkt måste kunna verifieras på GitHub. Inte vague "do X", utan specifikt vad-och-hur-vet-vi.

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

❓ PROCESS — Ska mötet nästa vecka starta med Code Review eller Retrospekt?
   VARFÖR VIKTIG: Påverkar agenda
   IDAG-SVAR BEHÖVS: Nej (kan bestämma senare)
```

**REGLER:**
- MAX 5-6 frågor per möte
- Börja med "IDAG-SVAR BEHÖVS: Ja" — de höga prioriteten
- Avsluta med "IDAG-SVAR BEHÖVS: Nej" — diskussions-frågor för framtida möten
- PL måste kunna svara direkt, inte "vi återkommer"

---

## 🔗 SYSTEMÖVERSIKT

```
FÖRE PRESENTATION BYGGS:
  1. Läs MANDATORY_READING_ORDER.md ← allt du behöver
  2. Hämta data från alla GitHub-sources (se DATA_SOURCES.md)
  3. Verifiera alla sources enligt RENDER_GATE_CHECKLIST.md
  4. Code review alla aktiva branches/PRs för punkt ⑦, ⑩, ⑪
  5. Bygg slides enligt denna struktur (①-⑭)
  6. Slutgranskning innan rendering

NÄR PRESENTATIONEN ÄR KLAR:
  ✅ Punkt ① visar ALLA 7 team-medlemmar (arbete eller "ingen issue")
  ✅ Punkt ④-⑥ visar alla issues med Team + Assignad + Blocker
  ✅ Punkt ⑦ visar både blockers OCH code-review-resultat
  ✅ Punkt ⑧ visar MUST/NEXT/LATER med Team + Assignad
  ✅ Punkt ⑩ visar risker driven av code-review-fynd
  ✅ Punkt ⑬ visar konkreta GitHub-åtgärder, inte vague tasks
  ✅ Punkt ⑭ har max 5-6 frågor, prioriterade
  ✅ Alla 14 punkter uppfyllda → RENDERING OK
```

---

**Version:** 3.0 (Ny 14-punkts-struktur)
**Senast uppdaterad:** 2026-09-14
**Status:** PRODUCTION — Ny struktur aligned med användarens krav
