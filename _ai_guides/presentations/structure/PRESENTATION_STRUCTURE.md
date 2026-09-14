---
name: presentation_structure
description: 14 mötespunkter — konkret struktur, data-källor och handlingsplan
metadata:
  type: reference
  critical: true
  version: 2.0
---

# 📋 PRESENTATION STRUCTURE — 14 Mötepunkter (①-⑭)

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

**Ingen checklista — bara faktisk data**
- Slidorna fylls med verklig GitHub-data, inte tomma checkboxes
- Se [MANDATORY_READING_ORDER.md](../MANDATORY_READING_ORDER.md) för vilka GitHub-åtgärder som behövs

---

## 🎬 FRAMSIDA — Extremt enkel & ren (ingen/📝⓪)

```
HEADER:
  Vänster: "SPRINTPLANERING · TEAM 1"
  Höger: "Måndag 14 september · 09:00–10:30"

MAIN CONTENT (mycket whitespace):

Fokus med PL denna vecka

Säkerställa veckans prioriteringar, beroenden
och vägen mot CTO-demo.

FOOTER (litet, 10-12pt, diskret):
Underlag kontrollerat inför mötet:
context_engineering · avanza-team1 · Git-status · Issues & PRs · Project Board
Code review: [status — kontrakt verifierade]
Mötesprotokoll: [status]

DESIGN:
✅ 70% tom yta
✅ Max 3 textblock
✅ Ingen agenda, inga kort, ingen extra info
✅ Fokus ligger på PL-fokus-texten
```

---

## 📝① SEDAN FÖRRA MÖTET — Done/Merged (1-2 slides)

**Syfte:** Vad blev FAKTISKT klart denna vecka?

**MÅSTE INNEHÅLLA:**
- ✅ Vad blev faktiskt klart denna vecka? (ALLA team-medlemmar från 7 dagar)
- ✅ Konkreta commits från GitHub
- ✅ Active branches
- ✅ Stale branches (>3 dagar utan push)
- ✅ Alla 7 team-medlemmar måste synas med arbete

**DATA-KÄLLOR (MANDATORY):**
- 📊 [Merged PRs denna vecka](../data/DATA_SOURCES.md#merged-prs) — GitHub URL
- 📊 [Commits denna vecka](../data/DATA_SOURCES.md#commit-history) — GitHub URL
- 📊 [Branches develop + active](../data/DATA_SOURCES.md#github-branches) — GitHub URL
- 📋 [Team-medlemmar](../data/TEAM_ROSTER.md) — verifierade från git commits

**FORMAT (MÅSTE VARA TABELLER, INTE CHECKLISTOR):**

### ①A: Frontend — Levererat denna vecka

| PR | Titel | Författare | Datum | Issues | DoD |
|----|-------|-----------|-------|--------|-----|
| #90 | Login page + token handling | Zaida | Sep 10 | #40 | 🟢 ✅ |
| #79 | Design system + top bar | Björn | Sep 10 | #44, #45 | 🟡 Docs |
| #72 | Save target allocation | Tomac | Sep 9 | #41 | 🟢 ✅ |

**Team-medlemmar denna vecka:**
- Zaida Wiss (2 PRs — login page, dashboard)
- Björn Boman (1 PR — design system)
- Tomac Barin Jansson (2 PRs — allocation, portfolio)

### ①B: Backend — Levererat denna vecka

| PR | Titel | Författare | Datum | Issues | DoD |
|----|-------|-----------|-------|--------|-----|
| #91 | Clean controllers | Rasha | Sep 10 | #76 | 🟢 ✅ |
| #71 | Flyway migration + schema | Rasha | Sep 10 | #56 | 🟢 ✅ |
| #63 | SessionSecurityFilter | Rasha | Sep 7 | #57 | 🟡 Tests |

**Team-medlemmar denna vecka:**
- Rasha Knifdi (5 PRs — security, migrations, controllers)
- Erik Berglund (0 PRs denna vecka)

### ①C: Native/System — Levererat denna vecka

| PR | Titel | Författare | Datum | Issues | DoD |
|----|-------|-----------|-------|--------|-----|
| #92 | Risk-module extensive additions | Pär | Sep 10 | #61, #65, #74 | 🟢 ✅ |
| #64 | FX and risk modules | Henrik | Sep 7 | — | 🟡 Docs |

**Team-medlemmar denna vecka:**
- Pär Lundh (1 PR — risk module)
- Henrik Westerlund (1 PR — FX module)

### ①D: Byggde vidare denna vecka (NULÄGESBILD)

**Öppna PRs (väntar på review):**

| # | Titel | Författare | Reviewer? | Status |
|---|-------|-----------|-----------|--------|
| #95 | Fix SQL-injection | Rasha | ❌ INGEN | 🔴 BLOCKERAD |
| #80 | Drift banner | Tomac | ❌ INGEN | 🔴 BLOCKERAD |
| #68 | Update README | Zaida | ❌ INGEN | 🔴 BLOCKERAD |

**🚨 OBSERVATION:** Alla 3 öppna PRs saknar reviewer — de kan inte mergas!

**Öppna issues denna vecka (aktiv arbete):**

| # | Titel | Assignerad | Team | Upd |
|---|-------|-----------|------|-----|
| #89 | E2E test MVP | Zaida | Frontend | Sep 10 |
| #88 | Täck kritiska interactions | Zaida | Frontend | Sep 10 |
| #93 | SQL-injection (Java) | Rasha | Backend | Sep 10 |
| #78 | Rolling Volatility | Pär | Native | Sep 10 |

**Senaste commits denna vecka:**

| Datum | Författare | Meddelande | Issue |
|-------|-----------|-----------|-------|
| 10 sep | Björn | Merge login-page (#90) | #40 |
| 10 sep | Zaida | Auth integration + logout | #40 |
| 10 sep | Pär | Rolling values-funktioner | #75, #77, #78 |

**⚠️ VARNING:** Senaste commits 10 sep → ingen kod sedan dess (4 dagar)

---

## 📝② SPRINTMÅL (Big picture — 1 slide)

**Syfte:** Vad ska denna sprint åstadkomma?

**MÅSTE INNEHÅLLA:**
- ✅ 1-3 tydliga fokusområden
- ✅ Deadline synlig
- ✅ Koppling till CTO-deadline

**DATA-KÄLLOR:**
- 📊 [Kritiska deadlines](../structure/PRESENTATION_STRUCTURE.md#kritiska-deadlines) från mötet
- 📊 GitHub Project Board (manuell läsning)

**FORMAT:**
```
🎯 SPRINT 4 MÅL (14-20 sep)

1. Säkerställa CTO-underlag klart 24 sep
   - Tekniska risker dokumenterade
   - Arkitektur-beslut fastslagna
   - Kapacitets-plan realistisk

2. Stabilisera Frontend-Backend integration
   - API-kontrakt mellan systemen
   - End-to-end login flow fungerar

3. Native Risk-module production-ready
   - Rolling values-beräkningar verifierade
   - Performance-tests OK

📅 DEADLINE: 24 september 16:00 (CTO-underlag)
```

---

## 📝③ NULÄGE (Dashboard — 1 slide)

**Syfte:** Var står projektet MOT sprintmålet?

**MÅSTE INNEHÅLLA:**
- ✅ Övergripande status: 🟢 ON TRACK | 🟠 DELAY | 🔴 CRITICAL
- ✅ Framsteg denna vecka (från X → Y)

**FORMAT:**
```
PROGRESS: ████████░░░░░░░░░░░░  40% av sprint
BLOCKERS: 3 öppna PRs väntar på review
RISK: CTO-deadline på 10 dagar — många beslut kvar

STATUS: 🟠 SLIGHT DELAY
- Risk-analys inte påbörjad än
- Backend-Frontend API-kontrakt inte fastslaget
```

---

## 📝④ FRONTEND TEAM — VAR ÄR VI? (1-2 slides)

**Team:** Zaida Wiss, Björn Boman, Tomac Barin Jansson

**MÅSTE INNEHÅLLA (Nuläge & Status):**
- ✅ Issues med assignee (#XX – Name)
- ✅ Git-status denna vecka (commits, branches)
- ✅ DoD-status per issue (AC✓ Tests✓ Review✓ Docs✓)
- ✅ Dependencies och blockers
- ✅ Status 🟢🟠🔴 per issue

**DATA-KÄLLOR:**
- 📊 [Open issues](../data/DATA_SOURCES.md#work-in-progress) — GitHub
- 📊 [Commits denna vecka](../data/DATA_SOURCES.md#commit-history) — GitHub
- 📊 [Team-medlemmar](../data/TEAM_ROSTER.md) — TEAM_ROSTER.md

**FORMAT:**
| # | Titel | Assignerad | DoD | Status | Blockers |
|---|-------|-----------|-----|--------|----------|
| #89 | E2E test | Zaida | ◐ Tests | 🟡 PÅGÅR | Väntar på Backend API |
| #84 | Asset chart | Zaida | ✓ | 🟢 KLAR | — |

---

## 📝⑤ FRONTEND TEAM — VAD GÖR VI ÅT DET? (Actionbar guide — 1 slide)

**Format för Junior-Utvecklare — 5-10 sekunder förståelse:**

```
1️⃣ FORTSÄTT — Nästa Steg
   "Tomac fortsätter #43 API-client. Zaida startar #87 testgrund."

2️⃣ BEHÖVER STÄNGAS — Saknad DoD
   "#42 Drift indicator – saknar review, test, docs. Tomac: kan du fixa?"

3️⃣ KAN TAS NU — Oberoende Arbete
   "#87 Frontend test foundation – oberoende av Backend, kan startas nu"

4️⃣ AGERA PÅ — Möte/Decision
   "Frontend + Backend möte: auth-kontrakt kräver avtal på träff tis 14:00"
```

---

## 📝⑥ BACKEND TEAM — VAR ÄR VI? (1-2 slides)

**Team:** Rasha Knifdi, Erik Berglund

**MÅSTE INNEHÅLLA:**
- ✅ Issues med assignee
- ✅ Git-status denna vecka
- ✅ DoD-status per issue
- ✅ Dependencies och blockers
- ✅ Status 🟢🟠🔴

**DATA-KÄLLOR:**
- 📊 [Open issues](../data/DATA_SOURCES.md#work-in-progress) — GitHub
- 📊 [Team-medlemmar](../data/TEAM_ROSTER.md)

---

## 📝⑦ BACKEND TEAM — VAD GÖR VI ÅT DET? (Actionbar guide — 1 slide)

**Format för Junior-Utvecklare:**

```
1️⃣ FORTSÄTT
2️⃣ BEHÖVER STÄNGAS
3️⃣ KAN TAS NU
4️⃣ AGERA PÅ
```

---

## 📝⑧ NATIVE TEAM — VAR ÄR VI? (1-2 slides)

**Team:** Pär Lundh, Henrik Westerlund

**MÅSTE INNEHÅLLA:**
- ✅ Issues med assignee
- ✅ Git-status denna vecka
- ✅ DoD-status per issue
- ✅ Status 🟢🟠🔴

---

## 📝⑨ NATIVE TEAM — VAD GÖR VI ÅT DET? (Actionbar guide — 1 slide)

**Format för Junior-Utvecklare:**

```
1️⃣ FORTSÄTT
2️⃣ BEHÖVER STÄNGAS
3️⃣ KAN TAS NU
4️⃣ AGERA PÅ
```

---

## 📝⑩ BEROENDEN & BLOCKERS (Flödesdiagram — 1-2 slides)

**Syfte:** Vad väntar på vad? VAD BLOCKERAR VAD?

**MÅSTE INNEHÅLLA:**
- ✅ Flödesschema med pilar (VAD → VÄNTAR PÅ → VAD)
- ✅ Förväntad lösning + tid
- ✅ Åtgärd NU (konkret)

**DATA-KÄLLOR:**
- 📊 [Blockers från GitHub issues](../data/DATA_SOURCES.md#blockers--dependencies)
- 🔍 **CODE REVIEW FINDINGS** (MÅSTE INKLUDERAS):
  - API-avvikelser som blockerar
  - Kontrakt-missmatchningar
  - Vilka är påverkade

**FORMAT:**

```
Frontend #89 (E2E test)
    ↓ VÄNTAR PÅ
Backend #XX (Auth-endpoint fungerande)
    ↓ LÖSES AV: Rasha, tis 15 sep

Frontend #84 (Asset chart)
    ↓ VÄNTAR PÅ
Backend API-kontrakt fastslaget
    ↓ LÖSES AV: Frontend+Backend möte, mån 14:00
```

---

## 📝⑪ PRIORITERING & SCOPE (Must/Next/Later — 1 slide)

**Syfte:** Vad gör vi FÖRST? Vad kommer senare?

**MÅSTE INNEHÅLLA:**
- ✅ MUST denna vecka (måste göras)
- ✅ NEXT nästa vecka (prioriterat)
- ✅ LATER (kan vänta)

**DATA-KÄLLA:**
- 📊 GitHub Project Board — manual läsning

**FORMAT:**

```
🔴 MUST DENNA VECKA
   ☐ #93 SQL-injection fix
   ☐ #40 Auth-flow end-to-end
   ☐ CTO-underlag döcumentation

🟠 NEXT VECKA
   ☐ #42 Drift indicator
   ☐ #78 Rolling calculations

⚪ LATER (MÅ VÄNTA)
   ☐ #99 Admin-panel (låg prioritet)
```

---

## 📝⑫ KAPACITET & ESTIMERING (Kapacitetsvy — 1 slide)

**Syfte:** Är mängden planerat arbete realistisk?

**MÅSTE INNEHÅLLA:**
- ✅ Kapacitet per team (available vs needed)
- ✅ "Passar det?" → Ja/Nej/Knapp

**FORMAT:**

```
Frontend: 45h tillgängligt → 48h planerat = 🟠 LITE STRAMT
Backend: 40h tillgängligt → 35h planerat = 🟢 OK
Native: 30h tillgängligt → 32h planerat = 🟠 STRAMT

RESULTAT: Något stramt — kan behöva justeras
```

---

## 📝⑬ RISKER (Risk-kort — 1-2 slides)

**Syfte:** Vilka risker kan göra att sprintplanen misslyckas?

**MÅSTE INNEHÅLLA:**
- ✅ Risken (vad kan gå fel?)
- ✅ Konsekvens (vad händer?)
- ✅ Hantering/mitigation (vad gör vi åt det?)

**DATA-KÄLLOR:**
- 🔍 **CODE REVIEW FINDINGS** (MÅSTE INKLUDERAS):
  - Dubbelarbete-risk (teamen jobbar olika)
  - Ohålbar riktning
  - Framtida tech-skuld
- 📊 [Risk Register](../../_memory/RISK_REGISTER.md)

**FORMAT:**

```
🔴 RISK: Backend API-kontrakt inte klart
   KONSEKVENS: Frontend kan inte integreras
   MITIGATION: Frontend+Backend möte måndag 14:00 för att fastslå kontrakt

🟠 RISK: Zaida överbelastad (9 issues)
   KONSEKVENS: Arbete försenas
   MITIGATION: Björn + Tomac pairing på #89-#91 denna vecka
```

---

## 📝⑭ TEKNISKA BESLUT (Beslutskort — 1 slide)

**Syfte:** Vilka beslut behöver tas denna vecka?

**MÅSTE INNEHÅLLA:**
- ✅ Beslutet (vad behöver fastslås?)
- ✅ Påverkade team
- ✅ Deadline för beslut

**DATA-KÄLLOR:**
- 🔍 **CODE REVIEW FINDINGS** (MÅSTE INKLUDERAS):
  - API-kontrakt som behöver fastslås
  - JNA-kontrakt som behöver dokumenteras
  - Auth-flow som behöver vara samma överallt
- 📋 [BESLUT-filer per team](../../_memory/)

**FORMAT:**

```
🔷 BESLUT 1: Frontend-Backend API-kontrakt
   PÅVERKADE: Frontend, Backend
   DEADLINE: Mån 14 sep 15:00
   DECISION-OWNER: Rasha + Zaida

🔷 BESLUT 2: Error-handling standardisering
   PÅVERKADE: Alla team
   DEADLINE: Tis 15 sep
   DECISION-OWNER: Rasha (Backend leder)
```

---

## 📝⑮ SPRINTPLAN (Vem gör vad? Hur arbetar vi TILLSAMMANS? — 1-2 slides)

**Syfte:** Veckans konkreta uppdrag + teamsamarbete

**🚨 REGEL: Support/pairing är fullt legitimt sprintåtagande.**
Om Björn bäst hjälper sprintmålet genom att stötta Tomac på en kritisk integration, är "support/pair på #43" ett fullt legitimt åtagande. Planen ska optimera teamets LEVERANS, inte maximera individuella arbetuppgifter.

**MÅSTE INNEHÅLLA:**
- ✅ Per-team boxar (Frontend / Backend / Native)
- ✅ Issues + assignee + timmar
- ✅ SYNLIGT: Vilken support/pairing är planerad denna vecka
- ✅ Teamstöd & hållbarhet — Hur hjälps vi åt?

**FORMAT:**

```
Frontend:
- ☐ #42 Portfolio (Zaida - 5h)
- ☐ #43 Risk calc (Tomac - 8h, + Björn support 4h)
- ☐ Stötta Tomac på #43 (Björn - 4h)

Backend:
- ☐ #51 API-spec (Rasha - 3h)
- ☐ #52 Risk endpoint (Erik - 8h)

Native:
- ☐ #60 iOS test (Pär - 5h)
- ☐ #61 Android widget (Henrik - 7h)

🤝 TEAMSAMARBETE & HÅLLBARHET:
✅ BELASTNING: Zaida lite högt — Björn pairing låser in stöd
✅ BLOCKERANDE PERSON: Rasha on API-spec — Erik kan pair för kunskapsöverföring
✅ KUNSKAPSRISK: Risk-calculations bara Pär — Henrik mentorerad
✅ BACKUP: Henrik som backup för Pär om något händer
```

**VISUELLA ELEMENT:**
- ⬛ Svart border per team-box
- ☐ Checkboxes (copy-paste till mötesprotokollet)
- 👥 Assignee på varje rad
- ⏰ Konkreta timmar
- 🤝 Support/pairing tydligt märkt

**DATA-KÄLLA:**
- 📊 GitHub Project Board + manual läsning
- 📋 Team-diskussion under mötet

---

## 📝⑯ NÄSTA STEG (Konkret handlingsplan — 2 slides)

**🚨 DENNA PUNKT ÄR INTE EN CHECKLISTA — DET ÄR HANDLINGSPLAN**

**MÅSTE INNEHÅLLA (8 numrerade sektioner):**

### 1️⃣ TILLDELNING — Vem tar vilken issue?
```
#89 → Zaida
#93 → Rasha
#78 → Pär
etc.
```

### 2️⃣ NYA ISSUES SOM BEHÖVER SKAPAS
```
Ny issue: [namn] — [varför]
Ny issue: [namn] — [varför]
```

### 3️⃣ BEFINTLIGA ISSUES SOM BEHÖVER UPPDATERAS
```
#XX → förtydliga AC
#XX → lägg till dependency på #YY
#XX → uppdatera scope
```

### 4️⃣ ISSUES SOM MÅSTE PAUSAS/FLYTTAS
```
#XX flyttas från MUST till NEXT — [varför]
#XX pausas — [väntar på vad]
```

### 5️⃣ BLOCKERS — LÖSES HUR, NÄR, AV VEM
```
[Blocker] löses av [namn], [dag tid]
[Blocker] löses av [namn], [dag tid]
```

### 6️⃣ PAIRING/SUPPORT SOM BEHÖVER BOKAS
```
[namn] + [namn] pair prog på #XX — [dag tid]
[namn] mentorerar [namn] på #XX — [dag tid]
```

### 7️⃣ TEAMSTÖD & HÅLLBARHET
**Identifiera där teammedlemmar kan hjälpa, avlasta, paira eller täcka upp för varandra:**

```
✅ BELASTNING: Är någon fullbelastad medan någon annan har utrymme?
   → Omfördela eller erbjud stöd

✅ BLOCKERANDE PERSON: Om någon sitter fast, vem kan faktiskt hjälpa?
   → Blockers är teamets problem, inte individens

✅ KUNSKAPSRISK: Finns kritisk kunskap hos bara en person?
   → Pairing, review eller kunskapsöverföring planeras

✅ ÖVERLÄMNINGAR: Behöver Frontend vänta på Backend?
   → Arbeta tillsammans på kontraktet först

✅ BACKUP: Vilka kan täcka upp om huvudansvarig fastnar?
   → Synligt på kritiska uppgifter

✅ ÅTGÄRDER: Varje handlingsplansåtgärd har ansvarig och tidsram
```

**Resultat: Planen är genomförbar OCH hållbar. Vi når målet TILLSAMMANS.**

### 8️⃣ KONTRAKT & BEROENDEN (från Code Review + GitHub)
```
API-spec för #XX → uppdatera i shared doc
JNA-kontrakt för #XX → fastslå och dokumentera
Auth-flow → dokumentera i [länk]
```

**DIREKT EFTER MÖTET:**
```
☐ GitHub Project Board uppdaterad
☐ Assignees satta
☐ Blockers/dependencies dokumenterade
☐ Issues på rätt sprint
☐ Tekniska beslut dokumenterade
```

**DATA-KÄLLOR:**
- 📊 GitHub Issues API
- 📊 GitHub Project Board
- 📊 Mötesprotokollet
- 📋 [BESLUT-filer per team](../../_memory/)

---

## 📝⑰ FRÅGOR FRÅN PL / STAKEHOLDERS (Sista slide — diskussionsarbetsyta)

**🚨 DENNA SLIDE ÄR ABSOLUT SISTA. LIGGER KVAR UNDER MÖTET.**

⚠️ **VIKTIGT:** Dessa är FÖRSLAG på frågor. Teamet formar sina egna frågor baserat på vad som behöver lösas denna vecka.

**LAYOUT:**

```
❓ FÖRESLAGEN FRÅGA 1: Är CTO-deadlinen realistisk givet nuläget?
   Kontext: Vi är 10 dagar bort och risk-analys inte påbörjad
   TEAMETS FRÅGA: ____________________________________
   SVAR: ____________________________________

❓ FÖRESLAGEN FRÅGA 2: Vilka kunskapsrisker (single point of failure) har vi?
   Kontext: Pär ensam på risk-beräkningar, Zaida överbelastad
   TEAMETS FRÅGA: ____________________________________
   SVAR: ____________________________________

❓ FÖRESLAGEN FRÅGA 3: Hur organiserar vi Backend-Frontend integrationsmötet?
   Kontext: API-kontrakt behöver fastslås för framsteg
   TEAMETS FRÅGA: ____________________________________
   SVAR: ____________________________________
```

**DENNA SLIDE LIGGER KVAR under mötet.**
Det är arbetsytan för PL-diskussionen och dokumentation av svar.

**REGEL: Börja med förslagen, låt teamet forma sina egna frågor under mötet.**

---

## 📋 STRUKTUR SUMMARY

**14 mötepunkter (①-⑰), variabel slidantal:**

```
🎬 FRAMSIDA (0)
📝① Sedan förra mötet (1-2)
📝② Sprintmål (1)
📝③ Nuläge (1)
📝④-⑤ Frontend (2-3)
📝⑥-⑦ Backend (2-3)
📝⑧-⑨ Native (2-3)
📝⑩ Beroenden & Blockers (1-2)
📝⑪ Prioritering (1)
📝⑫ Kapacitet (1)
📝⑬ Risker (1-2)
📝⑭ Tekniska Beslut (1)
📝⑮ Sprintplan (1-2)
📝⑯ Nästa Steg (2)
📝⑰ Frågor från PL (1)

TOTALT: ~22-30 slides (varierar per vecka)
```

**MÖTESLOGIK:**
Framsida → ① Bakåt → ② Målbild → ③ Nuläge → ④-⑨ Teams → ⑩ Beroenden → ⑪ Prioritering → ⑫ Kapacitet → ⑬ Risker → ⑭ Beslut → ⑮ Plan → ⑯ Nästa steg → ⑰ PL-frågor (diskussion)

---

## 🔗 LÄNKAD STRUKTUR — Data flödar från dessa filer

| Mötespunkt | Data-källa | Länk |
|-----------|-----------|------|
| ① | Merged PRs, commits, open issues | [MANDATORY_READING_ORDER.md](../MANDATORY_READING_ORDER.md), [DATA_SOURCES.md](../data/DATA_SOURCES.md) |
| ② | CTO-deadline, sprintmål | Mötesprotokollet, GitHub Project Board |
| ③ | Progress-status | GitHub Issues/PRs, commit-historik |
| ④-⑨ | Issues, branches, DoD-status | [TEAM_ROSTER.md](../data/TEAM_ROSTER.md), GitHub Issues |
| ⑩ | Blockers från GitHub + Code Review | [DATA_SOURCES.md](../data/DATA_SOURCES.md#blockers--dependencies) |
| ⑪ | Prioritering från möte | GitHub Project Board, mötesprotokollet |
| ⑫ | Kapacitets-uppskattning | Möte-diskussion, issue-estimat |
| ⑬ | Identifierade risker | Code Review findings, mötesprotokollet |
| ⑭ | Tekniska beslut | Code Review findings, [BESLUT-filer](../../_memory/) |
| ⑮ | Sprint-plan | GitHub Project Board, möte-diskussion |
| ⑯ | Handlingsplan | Möte-resultat, GitHub |
| ⑰ | PL-frågor | Möte-diskussion |

---

**Version:** 2.0  
**Senast uppdaterad:** 2026-09-14  
**Status:** PRODUCTION — Lämnar från detta när all struktur länkad och verifierad
