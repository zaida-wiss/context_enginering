# Avanza Portföljhälsa - Team 1 Extended Challenge

**En portföljövervakningsapp som hjälper kunder att förstå sitt sparande, upptäcka driftningar och fatta bättre beslut.**

---

## 📚 Dokument Guide - Två Repos Samarbete

**Denna repo (`context_enginering`) innehåller teamdokumentation och AI-guider.  
Projekt-arbetet finns i `avanza-team1`.**

---

### 🧠 `_memory/` - MINNE-DOKUMENT (Statisk Referens)
**Läs för kontext. AI uppdaterar INTE dessa. Ändras sällan.**

```
_memory/
├── PROJEKTKONTEXT.md       ← Kundens behov (Anna), varför vi bygger det
├── TEAMSTANDARDS.md        ← Kodstandarder, Git workflow, regler
├── DEFINITION_OF_DONE.md   ← Acceptance criteria för godkänt
└── DECISIONS.md            ← Arkitektur-beslut (varför gjorde vi det så?)
```

👉 Använd dessa filer som referensmaterial när du behöver förstå **bakgrund & principer**.

**📍 För projekt-KONTEXT, läs från avanza-team1-repot:**
- **Projekt-övergripande kontext:** https://github.com/chas-challenge-2026/avanza-team1/tree/main
- **Alla filer uppdateras där** (denna repo är enbart för team-process)

---

### 📊 `_sprint/` - LEVANDE DOKUMENT (Real-Time Tracking)
**Uppdateras varje möte. AI läser OCH uppdaterar dessa. Finns i denna repo (context_enginering).**

```
context_enginering/_sprint/
├── CURRENT_STATUS.md       ← Levande data: Sprint tracking (uppdateras EFTER varje möte)
├── RISKS.md                ← Levande data: Risk-register (uppdateras VECKOVIS)
├── SCHEDULE.md             ← Plan-data: Sprint-schema & vecko-fokus
└── SPRINT_PLANNING.md      ← Guide-data: Planerings-guide (referens)
```

👉 **Viktigt:** Läs **[_ai_guides/UPDATE_SCHEDULE.md](_ai_guides/UPDATE_SCHEDULE.md)** för exakt uppdaterings-schema.

**Snabb sammanfattning:**
- Torsdag efter möte: 10 min (CURRENT_STATUS + RISKS)
- Måndag efter möte: 10 min (CURRENT_STATUS + RISKS)
- Tisdag: 5 min (RISKS check)
- **Total: ~25 min/vecka**

---

### 🤖 `_ai_guides/` - AI-GUIDE DOKUMENT (Instruktioner & Möten)
**Använd när du kör möten eller ber AI om hjälp. AI läser för att veta vad den ska göra.**

```
_ai_guides/
├── WHAT_CAN_I_HELP_WITH.md ← START HÄR! Meny - "Vad kan du göra?"
├── HOW_TO_RUN_MEETINGS.md  ← Två mötes-workflows (Web + VS Code)
├── UPDATE_SCHEDULE.md      ← 🆕 NÄR & HUR uppdatera dokument (25 min/vecka)
├── PREPARE_MEETING.md      ← Förbered möte från git log
├── AI_TEAMLEADER.md        ← Universal AI-facilitator prompt
├── MEETING_THURSDAY.md     ← Torsdag: Vecko-slutabstämning (30 min)
├── MEETING_MONDAY.md       ← Måndag: Sprintplanering (3 tim)
├── TEAM_MEETING_TEMPLATE.md ← Team-specifika möten (Backend/Frontend/Native)
└── BACKLOG_TEMPLATE.md     ← Issue-templates för GitHub Project
```

**Start här:** Fråga AI "Vad kan du hjälpa mig med?" → AI visar **WHAT_CAN_I_HELP_WITH.md**

**Mötes-Workflow:**

**VÄLJ DIN METOD:**
- **Web-Based AI** (ChatGPT, claude.ai, Gemini): 👉 Läs **HOW_TO_RUN_MEETINGS.md** (Metod 1)
- **VS Code + Claude Code** (Lokal): 👉 Läs **HOW_TO_RUN_MEETINGS.md** (Metod 2 - AUTO-UPDATE!)

**SPRINT MÖTEN (Hela teamet):**
1. 👉 **FÖRBERED:** Använd **PREPARE_MEETING.md** → AI läser git log + status
2. 👉 **FACILITERA:** Kopiera **AI_TEAMLEADER.md** + relevant möte-fil (MEETING_THURSDAY / MEETING_MONDAY)
3. 👉 **DOKUMENTERA:** AI uppdaterar automatiskt (VS Code) eller du copy-pastas (Web)

**TEAM-SPECIFIKA MÖTEN (Endast ett team):**
1. 👉 **FÖRBERED:** Be AI: "Förbered [Backend/Frontend/Native]-möte" 
2. 👉 **FACILITERA:** Använd **TEAM_MEETING_TEMPLATE.md** + **AI_TEAMLEADER.md**
3. 👉 **DOKUMENTERA:** AI sammanfattar beslut och action items

---

### 🎯 Quick Navigation - ALLT UTGÅR FRÅN DENNA README

**DU BÖR BÖRJA MED:**

1. **Fråga AI:** "Vad kan du hjälpa mig med?"  
   → Copy-pasta detta i AI (Web-based):
   ```
   https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/WHAT_CAN_I_HELP_WITH.md
   ```
   → Eller läs direkt: **[WHAT_CAN_I_HELP_WITH.md](_ai_guides/WHAT_CAN_I_HELP_WITH.md)**

2. **För Möten - Kopiera Dessa Raw-Länkar Till AI:**
   - **"Kör torsdags-möte":**
     ```
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/AI_TEAMLEADER.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/MEETING_THURSDAY.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_sprint/CURRENT_STATUS.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_sprint/RISKS.md
     ```
   
   - **"Kör sprintplanering":**
     ```
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/AI_TEAMLEADER.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/MEETING_MONDAY.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_sprint/CURRENT_STATUS.md
     https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_sprint/RISKS.md
     ```

3. **Välja Vad Du Vill Göra:**
   - "Kör möte" → [HOW_TO_RUN_MEETINGS.md](_ai_guides/HOW_TO_RUN_MEETINGS.md)
   - "Status-rapport" → [CURRENT_STATUS.md](_sprint/CURRENT_STATUS.md)
   - "Vilka risker?" → [RISKS.md](_sprint/RISKS.md)
   - "Vanlig uppgift" → [WHAT_CAN_I_HELP_WITH.md](_ai_guides/WHAT_CAN_I_HELP_WITH.md)

**REFERENSMATERIAL (Läs När Du Behöver):**

**Vad bygger vi och varför?**  
→ **[_memory/PROJEKTKONTEXT.md](_memory/PROJEKTKONTEXT.md)**

**Vilka är kodstandarder?**  
→ **[_memory/TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md)**

**Vilka är arkitektur-beslut?**  
→ **[_memory/DECISIONS.md](_memory/DECISIONS.md)**

**Vad är godkänt (Definition of Done)?**  
→ **[_memory/DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md)**

**🎨 UI Design Mockups (För Frontend)?**  
→ **[_memory/UI_DESIGN_REFERENCE.md](_memory/UI_DESIGN_REFERENCE.md)** + **[_docs/DESIGN_MOCKUPS_README.md](_docs/DESIGN_MOCKUPS_README.md)**

---

## 🤖 AI-Instruktioner

**Alla AI-assistenter läser denna README först och följer instruktionerna nedan:**

### ⚡ FRONTEND-KOD (Viktigast!)

**REGEL:** Varje gång du frågar om frontend-kod ska AI:

1. ✅ Läsa [`_ai_guides/FRONTEND_AI_INSTRUCTIONS.md`](_ai_guides/FRONTEND_AI_INSTRUCTIONS.md)
2. ✅ Läsa [`_memory/UI_DESIGN_REFERENCE.md`](_memory/UI_DESIGN_REFERENCE.md)
3. ✅ Kolla mockupbilderna i `_docs/`:
   - `01_login.webp`
   - `02_overview.webp`
   - `03_target_allocation.webp`
   - `04_holdings_table.webp`
4. ✅ **Svara med:** "Enligt mockup XX.webp behöver komponenten..."
5. ✅ **Länka till:** [`UI_DESIGN_REFERENCE.md`](_memory/UI_DESIGN_REFERENCE.md)

### 📋 Andra AI-Instruktioner

- **Mötes-facilitering?** → [`_ai_guides/HOW_TO_RUN_MEETINGS.md`](_ai_guides/HOW_TO_RUN_MEETINGS.md)
- **Osäker vad du kan göra?** → [`_ai_guides/WHAT_CAN_I_HELP_WITH.md`](_ai_guides/WHAT_CAN_I_HELP_WITH.md)
- **Alla AI-instruktioner?** → Alla filer i [`_ai_guides/`](_ai_guides/)

**Fråga:** Vad hände på mötet förra veckan?  
→ Öppna **[Mötesprotokollet](https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit?tab=t.d1i0rhhuog1q)**

---

## 🚀 SNABBSTART - Hur Du Använder Systemet

### **Scenario 1: Du Vill Köra Ett Möte (Web-Based AI)**

1. Öppna ChatGPT, Claude.ai, eller vilken AI-modell som helst
2. Kopiera denna text:
```
Läs dessa instruktioner:
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/AI_TEAMLEADER.md

Sedan läs denna guide för mötet (välj en):
- Torsdags-möte: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/MEETING_THURSDAY.md
- Sprintplanering: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/MEETING_MONDAY.md

Sedan kopiera denna data (uppdatera från context_enginering-repot):
[Paste innehållet från: _sprint/CURRENT_STATUS.md]
[Paste innehållet från: _sprint/RISKS.md]

Nu: Kör mötet!
```

3. AI faciliterar mötet
4. Du copy-pastas sammanfattning tillbaka till filerna i context_enginering-repot

### **Scenario 2: Du Vill Köra Ett Möte (VS Code - SNABBARE!)**

1. Öppna VS Code → Claude Code (Alt+K)
2. Kopiera samma som ovan
3. AI frågar: "Uppdatera dokumenten direkt?"
4. Du klickar "Ja"
5. AI uppdaterar automatiskt ✨

### **Scenario 3: Du Vet Inte Vad Du Ska Göra**

1. Kopiera denna länk till AI:
```
https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/WHAT_CAN_I_HELP_WITH.md
```
2. Fråga: "Vad kan du göra?"
3. AI visar meny med 20+ möjligheter

---

## 🚀 Snabbstart - Välj Din Roll

---

## 🤖 AI Model Instructions

**Om du är en AI-modell som läser denna README:**

Du läser dokumentationen för Team 1's Avanza Portföljhälsa projekt. Här är hur du bör agera när du hjälper teamet:

### Grundläggande kontext från context_enginering:
1. **[_memory/PROJEKTKONTEXT.md](_memory/PROJEKTKONTEXT.md)** - Kundens behov (Anna), vad vi bygger, MVP-features
2. **[_memory/TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md)** - Kodstandarder, commit-format, Git workflow
3. **[_memory/DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md)** - Godkänd-krav och acceptance criteria

### Ge vägledning utifrån rätt fil:
- **"Hjälp mig planera sprint"** → [_sprint/SPRINT_PLANNING.md](_sprint/SPRINT_PLANNING.md) (steg-för-steg guide)
- **"Vad är aktuell sprint-status?"** → [_sprint/CURRENT_STATUS.md](_sprint/CURRENT_STATUS.md) (tracking)
- **"Vilka risker finns?"** → [_sprint/RISKS.md](_sprint/RISKS.md) (risk-register + mitigations)
- **"Vilken issue ska jag göra?"** → https://github.com/chas-challenge-2026/avanza-team1 (GitHub Project backlog)
- **"Varför gjorde vi det så?"** → [_memory/DECISIONS.md](_memory/DECISIONS.md) (arkitektur-beslut)

### Viktiga regler att följa:
✅ **Commit-format:** `type(scope): message (#ISSUE)` (t.ex. `feat(backend): add portfolio API (#52)`)  
   → Se **[_memory/TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md)** för format
✅ **Branch naming:** `type/#ISSUE-description` (t.ex. `feature/#52-portfolio-api`)
✅ **Code standards:** TypeScript interfaces (FE), SOLID + DI (BE), safe memory (Native)
✅ **Pull requests:** Feature branch → PR → review by other team member → merge
✅ **Definition of Done:** Acceptance criteria, tests, documentation, code review  
   → Se **[_memory/DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md)**
✅ **NOT:** `console.log()`, `TODO`, `FIXME`, inline styles, mock data i prod-kod

### När du guidar team-medlemmar:
1. **Referera alltid till dokumentation** (länka till TEAMSTANDARDS, PROJEKTKONTEXT, etc.)
2. **Använd samma struktur** som dokumentationen föreslår
3. **För nya issues:** Använd template från BACKLOG.md
4. **För sprintplanering:** Följ steg från SPRINT_PLANNING.md
5. **För risker:** Uppdatera RISKS.md med ny risk eller mitigation

### Kritisk information:
⚠️ **Tävlingen ≠ Betyget** — Fokusera på kursmål och slutleverans
⚠️ **CTO Deadline:** 24 september 16:00 — kärnflödet + dokumentation klar
⚠️ **Team:** Backend (1), Frontend (1), Native (1) — 3 issues/vecka per person är realistiskt


### 👨‍💻 Backend Developer (Java)

**📍 Kod finns i:** https://github.com/chas-challenge-2026/avanza-team1

1. **Installera:**
   ```bash
   # Prerequisites: Java 21, PostgreSQL 12
   brew install java@21 postgresql
   
   # Clone repo
   git clone https://github.com/chas-challenge-2026/avanza-team1.git && cd avanza-team1
   
   # Setup database
   createdb avanza_dev
   
   # Run migrations
   mvn flyway:migrate
   
   # Start backend
   mvn spring-boot:run
   ```

2. **Första uppgift:**
   - Läs [_memory/PROJEKTKONTEXT.md i context_enginering](_memory/PROJEKTKONTEXT.md) - förstå kundproblemet
   - Läs issues på https://github.com/chas-challenge-2026/avanza-team1/issues - vilka är prioriterade?
   - **Start:** Issue #52 (Portfolio Data API) eller #51 (Migrations)
   - Commit format: `feat(backend): message (#ISSUE)` (se [TEAMSTANDARDS](_memory/TEAMSTANDARDS.md))

3. **Testa lokalt:**
   ```bash
   # Start backend
   mvn spring-boot:run
   
   # Run tests
   mvn test
   
   # Check API
   curl http://localhost:8080/api/portfolio
   ```

4. **Granska kod:**
   - SOLID principles
   - Dependency injection
   - SQL injection prevention
   - Proper exception handling

---

### 🎨 Frontend Developer (React)

**📍 Kod finns i:** https://github.com/chas-challenge-2026/avanza-team1

1. **Installera:**
   ```bash
   # Prerequisites: Node 18+
   node --version  # Should be v18+
   
   # Setup
   cd avanza-team1/frontend
   npm install
   npm run dev
   ```

2. **Första uppgift:**
   - Läs [_memory/PROJEKTKONTEXT.md i context_enginering](_memory/PROJEKTKONTEXT.md) - förstå Annas problem
   - Läs issues på https://github.com/chas-challenge-2026/avanza-team1/issues
   - **Start:** Issue #54 (Connect Dashboard to API) eller #55 (Target Allocation UI)
   - Commit format: `feat(frontend): message (#ISSUE)` (se [TEAMSTANDARDS](_memory/TEAMSTANDARDS.md))

3. **Testa lokalt:**
   ```bash
   npm run dev      # Start dev server
   npm run build    # Build for production
   npm run test     # Run tests
   npm run lint     # Check code style
   ```

4. **Granska kod:**
   - All components: TypeScript interfaces for props
   - All functions: explicit return types
   - CSS: .module.css files (no inline styles)
   - Naming: PascalCase components, camelCase variables

---

### 🔧 Native Developer (C++)

**📍 Kod finns i:** https://github.com/chas-challenge-2026/avanza-team1

1. **Installera:**
   ```bash
   # Prerequisites: C++17, CMake, Jansson
   brew install cmake jansson
   
   # Build native module
   cd avanza-team1/native
   mkdir build && cd build
   cmake ..
   make
   ```

2. **Första uppgift:**
   - Läs [_memory/PROJEKTKONTEXT.md i context_enginering](_memory/PROJEKTKONTEXT.md) - förstå FX-requirements
   - Läs issues på https://github.com/chas-challenge-2026/avanza-team1/issues
   - **Start:** Issue #56 (FX Conversion) eller #57 (Back-testing)
   - Commit format: `feat(native): message (#ISSUE)` (se [TEAMSTANDARDS](_memory/TEAMSTANDARDS.md))

3. **Testa:**
   ```bash
   make test        # Run unit tests
   ./bench          # Performance benchmark
   ```

4. **Granska kod:**
   - Safe memory management (no leaks)
   - Destructors cleanup
   - snake_case for functions
   - Defensive coding (nil checks, error handling)

---

## 🏗️ System Architecture

**📍 Detaljerad arkitektur finns i:** https://github.com/chas-challenge-2026/avanza-team1/blob/main/README.md

```
┌─────────────────────────────────────────────────────────────┐
│                    WEB BROWSER (React)                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Dashboard │ Target Allocation │ Risk Metrics │ Chart │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────┬────────────────────────────────────────────┘
               │ REST API (JSON)
               ▼
┌─────────────────────────────────────────────────────────────┐
│              BACKEND (Java + Spring Boot)                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Controllers │ Services │ Repositories │ Models       │   │
│  │ - PortfolioController                                │   │
│  │ - RiskMetricsService                                 │   │
│  │ - AuthService                                        │   │
│  │ - UserRepository                                     │   │
│  └──────────────────────────────────────────────────────┘   │
└──────────────┬────────────────────────────────────────────┘
               │ JNI / REST Call
               ▼
┌──────────────────────────────────────┐  ┌──────────────────┐
│  NATIVE (C++)                         │  │  DATABASE        │
│  ┌────────────────────────────────┐   │  │  (PostgreSQL)    │
│  │ FX Converter                    │   │  │                  │
│  │ - Convert USD/EUR/GBP to SEK    │   │  │ Users            │
│  │ - Handles historical rates      │   │  │ Accounts         │
│  │ - Performance optimized         │   │  │ Holdings         │
│  │ - < 100ms for 1000 conversions  │   │  │ Prices           │
│  └────────────────────────────────┘   │  │ FX Rates         │
│  ┌────────────────────────────────┐   │  └──────────────────┘
│  │ Back-testing Engine             │   │
│  │ - Test strategies over 5 years  │   │
│  │ - Calculate: return, volatility │   │
│  │ - Sharpe ratio, max drawdown    │   │
│  │ - 500 instruments, < 2 seconds  │   │
│  └────────────────────────────────┘   │
└──────────────────────────────────────┘
```

### Data Flow: Hur Data Flödar Genom Systemet

1. **User Login**
   - Frontend → Backend (POST /auth/login)
   - Backend validates credentials
   - Returns JWT token

2. **Portfolio View**
   - Frontend → Backend (GET /api/portfolio)
   - Backend queries database for user's accounts + holdings
   - For each holding, gets current price + FX rate
   - Calls Native FX Converter to convert to SEK
   - Returns consolidated portfolio

3. **Risk Metrics**
   - Frontend → Backend (GET /api/portfolio/metrics)
   - Backend calls Native Back-testing Engine
   - Engine calculates volatility, Sharpe ratio, max drawdown
   - Returns metrics to backend, frontend displays

4. **Back-testing**
   - User sets "60/40 allocation" and clicks "Test"
   - Frontend → Backend (POST /api/backtest with parameters)
   - Backend loads 5 years of historical data
   - Calls Native Back-testing Engine
   - Engine simulates portfolio evolution
   - Returns results (total return, CAGR, etc)

---

## 📂 Folder Structure

```
avanza-team1/
├── README.md                    ← Du är här
├── PROJEKTKONTEXT.md           ← Kundens behov
├── TEAMSTANDARDS.md            ← Regler + Git workflow
├── DEFINITION_OF_DONE.md       ← Acceptance criteria
├── SCHEDULE.md                 ← Sprint schema
├── SPRINT_PLANNING.md          ← Sprintplanerings-guide
├── CURRENT_STATUS.md           ← Sprint tracking
├── RISKS.md                    ← Risk matrix
├── BACKLOG.md                  ← Prioriterad backlog
├── DECISIONS.md                ← Arkitektur-beslut
│
├── backend/                    ← Java + Spring Boot
│   ├── src/main/java/
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── repositories/
│   │   └── models/
│   ├── src/main/resources/
│   │   └── db/migration/       ← Flyway migrations
│   ├── pom.xml
│   └── README.md
│
├── frontend/                   ← React + TypeScript
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── styles/
│   │   └── App.tsx
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md
│
└── native/                     ← C++
    ├── src/
    │   ├── fx_converter.cpp
    │   ├── backtesting.cpp
    │   └── sharpe_ratio.cpp
    ├── include/
    ├── CMakeLists.txt
    └── README.md
```

---

## 🔄 Git Workflow (i avanza-team1-repot)

**📍 Denna information gäller för:** https://github.com/chas-challenge-2026/avanza-team1

### Branches
- **main** = production (stable, tested)
- **develop** = integration (default branch)
- **feature/\***, **fix/\*** = work branches

### Commit Format
```
type(scope): message (#ISSUE)

Examples:
- feat(backend): add portfolio data API (#52)
- fix(frontend): resolve dashboard loading bug (#54)
- refactor(native): optimize FX conversion (#56)
- test(backend): add integration tests (#61)
- docs(all): update README architecture (#62)
```

Se **[_memory/TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md)** för full detaljer.

### PR Process
1. Create feature branch: `git checkout -b feature/#52-portfolio-api`
2. Commit with format above
3. Push and create PR
4. Another team member reviews
5. Address feedback
6. Merge (only when approved)

**Reviewer Cannot Merge Their Own PR** ✅

---

## 🧪 Testing (i avanza-team1-repot)

**📍 Run tests i:** https://github.com/chas-challenge-2026/avanza-team1

### Run Tests

**Backend (Java):**
```bash
cd avanza-team1/backend
mvn test                  # All tests
mvn test -Dtest=UserServiceTest  # Single test
```

**Frontend (React):**
```bash
cd avanza-team1/frontend
npm test                  # Watch mode
npm run test:ci          # CI mode
```

**Native (C++):**
```bash
cd avanza-team1/native
mkdir build && cd build
cmake ..
make test
```

### Coverage Goals
- **Backend:** ≥ 70%
- **Frontend:** ≥ 60%
- **Native:** Key functions 100%

---

## 🚨 Critical Deadlines

| Datum | Milestone | Dagen | I Dag (Sep 4) |
|-------|-----------|-------|--------------|
| **Sep 24, 16:00** | CTO-underlag deadline | 20 dagar | 🔴 KRITISK |
| Oct 15, 17:00 | Demo-plan deadline | 41 dagar | 🟡 Högt |
| Oct 22 | LIVE DEMO | 48 dagar | 🟡 Högt |
| Nov 4, 15:00 | FINAL SUBMISSION | 61 dagar | 🟡 Högt |

**Fokus fram till Sep 24:** Kärnflödet fungerande + dokumentation

---

## ⚠️ Most Important Thing

**Tävlingen ≠ Betyget**

- Du får betyg baserat på slutleverans + 17 kursmål
- **Inte** på tävlingsresultat
- Fokusera på: Kursmål ✅, fungerande system ✅, dokumentation ✅
- Vinna tävlingen = bonus, inte målet

Läs [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) för detaljer.

---

## 🆘 Behöver Du Hjälp?

1. **Teknisk fråga?** → Läs relevant dokumentation (PROJEKTKONTEXT, TEAMSTANDARDS, DECISIONS)
2. **Issue-definition?** → Läs [BACKLOG.md](BACKLOG.md)
3. **Sprint-fråga?** → Läs [SPRINT_PLANNING.md](SPRINT_PLANNING.md)
4. **Blocked?** → Rapportera i [CURRENT_STATUS.md](CURRENT_STATUS.md), diskutera på Tuesday PL-möte
5. **Osäker på arkitektur?** → Läs [DECISIONS.md](DECISIONS.md)

---

## 📚 Linked Resources

**PROJEKTETS ARBETE (avanza-team1) - RAW LINKS:**
- Repo README: `https://raw.githubusercontent.com/chas-challenge-2026/avanza-team1/main/README.md`
- Issues & Backlog: `https://github.com/chas-challenge-2026/avanza-team1/issues`

**PROJECT BOARD (For AI - Try in This Order & Report Source):**

AI ska försöka i denna ordning och **berätta vilken källa den använt:**

1. **First Try:** `https://github.com/orgs/chas-challenge-2026/projects/31/views/1` (GitHub Project Board)
   - Om den lyckas, säg: "Läst från: GitHub Project Board"
   
2. **If Auth Error → Fallback:** `https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/edit?gid=869242669#gid=869242669` (Google Sheets backup)
   - Om den lyckas, säg: "Läst från: Google Sheets backup (GitHub Project Board var otillgänglig)"

**VIKTIGT:** AI måste alltid rapportera vilken källa den använt!

**TEAM-PROCESS (denna repo - context_enginering) - RAW LINKS FÖR AI:**
- Main README: `https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/README.md` ← **START HÄR!**
- Frontend Instructions: `https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/FRONTEND_AI_INSTRUCTIONS.md`
- Design Reference: `https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/UI_DESIGN_REFERENCE.md`
- Team Standards: `https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_memory/TEAMSTANDARDS.md`
- What Can I Help: `https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/WHAT_CAN_I_HELP_WITH.md`

**ANDRA RESURSER:**
- Canvas: https://chasacademy.instructure.com/courses/733/assignments
- Team Zoom: https://us06web.zoom.us/j/7491616766
- Meeting Notes: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit

---

## 🎓 Kursmål Vi Fokuserar På

Projektet är designat för att uppfylla dessa 17 kursmål:

1. **Arkitektur & Design** - System design, beslut
2. **Kod & Standards** - Kodkvalitet, konventioner
3. **Testing** - Unit, integration, E2E tests
4. **Dokumentation** - README, API docs, architecture
5. **Git & Versionskontroll** - History, traceability
6. **Ansvarsfullt AI-bruk** - Transparent, controlled
7. **Professionell kommunikation** - Fredags-dialoger
8. **Agil metodologi** - Sprint planning, retrospectives
9. + 9 more technical/professional objectives

Se [DEFINITION_OF_DONE.md](DEFINITION_OF_DONE.md) för full listan.

---

## 🚀 Senaste Uppdateringar

```
c1cae3b Merge pull request #51 from Refactor/Move-controller-logic-to-service
91ed09d Refactor: refactored AlertController, AuthController to services
3054172 build[frontend]: Dashboard components matching design mockup (#26)
269cc2f refactor[frontend]: Individual CSS modules for Dashboard components (#26)
```

---

---

## 📚 TWO-REPO STRUCTURE SUMMARY

| Repo | Innehål | Ansvar |
|------|---------|--------|
| **context_enginering** | Team-process, AI-guides, minnesdokument, sprint-tracking | Team process & documentation |
| **avanza-team1** | Projektets kod, issues, GitHub Project, commit history | Utveckling & release |

**Integration:**
- ✅ Alla AI-guides pekar till context_enginering
- ✅ Alla projektöversikter pekar till avanza-team1
- ✅ Kod-standarder dokumenterade här, tillämpade där
- ✅ Sprint-status sparas här, issues driven av Project Board där

---

**Senast uppdaterad:** 2026-09-07  
**Repos:** 
- Team Process: https://github.com/zaida-wiss/context_enginering
- Projekt Kod: https://github.com/chas-challenge-2026/avanza-team1

**Start här → [_memory/PROJEKTKONTEXT.md](_memory/PROJEKTKONTEXT.md)**

