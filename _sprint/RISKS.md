# Risk Register - Team 1

**Risk-matrix och mitigation strategies. Uppdatera denna när nya risker identifieras.**

---

## 🚨 Critical Risks (Red)

### Risk #1: Back-Testing Performance > 2 Seconds
- **Impact:** 🔴 CRITICAL
- **Probability:** 🟡 MEDIUM (50%)
- **Severity:** 9/10
- **Description:** Native C++ back-testing motor kanske inte klarar 500 instrument × 5 år under 2 sekunder
- **Why It Matters:** CTO deadline V6 kräver prestanda-specifikation. Om vi missar denna, är vi inte tävlings-ready.
- **Current Status:** WIP - FX-modul är långsam, inte optimerad än
- **Mitigation:**
  - [ ] Benchmarka denna vecka (V3) med 50 instrument, 500 instrument, 5 år data
  - [ ] Profile C++ kod för hotspots (Valgrind, gprof)
  - [ ] Om > 2s: Optimera memory allocation, use caching för FX-rates
  - [ ] Fallback: Pre-compute FX-rates offline om online-lookup är bottleneck
- **Owner:** Native-team
- **Review Date:** V6 (24 Sep) - Måste rapportera resultat till CTO

---

### Risk #2: Backend-Frontend Integration Fails
- **Impact:** 🔴 CRITICAL
- **Probability:** 🟡 MEDIUM (40%)
- **Severity:** 8/10
- **Description:** Frontend mockar data, backend skriver API, men när vi ansluter är det breaking changes eller API-kontrakt-mismatch
- **Why It Matters:** Kärnflödet kraschar om portfoliö-data inte läses rätt. Detta är "show-stopper" för demo.
- **Current Status:** Parallel development - BE och FE jobbar på samma features utan att snacka
- **Mitigation:**
  - [ ] Define API contract this week (JSON schema for /api/portfolio)
  - [ ] Frontend läser specn, implementerar typing
  - [ ] Backend implementerar exakt spec
  - [ ] Weekly sync between BE and FE owners (15 min, each Monday)
  - [ ] E2E test för whole flow (FE calls BE, gets data, displays it)
- **Owner:** Backend Lead + Frontend Lead
- **Review Date:** V4 (start of testing) - Must pass E2E test before V6

---

### Risk #3: PostgreSQL Schema Not Migration-Ready
- **Impact:** 🔴 CRITICAL
- **Probability:** 🟡 MEDIUM (30%)
- **Severity:** 7/10
- **Description:** Database schema är ad-hoc, inga Flyway migrations. Produktion-deployment misslyckas.
- **Why It Matters:** CTO feedback kommer kräva reproducible database setup. Utan migrations kan vi inte deploy.
- **Current Status:** Schema exists locally, men migrations inte committa
- **Mitigation:**
  - [ ] Write Flyway migration for current schema (V1__initial_schema.sql)
  - [ ] Test migration: drop database, run migration, verify schema
  - [ ] CI/CD hook: Run migrations before each test
  - [ ] Document schema in README (entity relationships)
- **Owner:** Backend-team
- **Review Date:** V3 (this week) - Must be merged before V4

---

## 🟡 High-Priority Risks (Yellow)

### Risk #4: Native Team Blocked on Architecture Decision
- **Impact:** 🟡 HIGH
- **Probability:** 🟡 MEDIUM (50%)
- **Severity:** 6/10
- **Description:** Native-team vet inte hur FX-modul ska anropas från Backend (REST endpoint? Shared library? RPC?)
- **Why It Matters:** Native jobbar på FX-modul utan att veta hur den integreras. Kan resultera i omarbete.
- **Current Status:** Design-möte inte genomfört än
- **Mitigation:**
  - [ ] Schedule architecture meeting this week (BE + Native)
  - [ ] Decide on integration pattern:
    - **Option A:** REST endpoint (BE calls Native via HTTP) - simple but slower
    - **Option B:** Shared library (Native exposes C++ via JNI/wrapper) - fast but complex
    - **Option C:** Message queue (async FX calculations) - decoupled but delayed
  - [ ] Document decision in DECISIONS.md
  - [ ] Create interface spec (API contract)
- **Owner:** Architecture Owner / Team Lead
- **Review Date:** V3 (end of this week)

---

### Risk #5: Test Coverage Too Low for CTO Review
- **Impact:** 🟡 HIGH
- **Probability:** 🔴 HIGH (70%)
- **Severity:** 6/10
- **Description:** Vi är på ~20% test coverage totalt. CTO förväntar sig 70%+ backend, 60%+ frontend.
- **Why It Matters:** CTO deadline V6 kräver "production-ready" code. Low coverage sägs nej till koden.
- **Current Status:** Tests written ad-hoc, inte systematisk coverage
- **Mitigation:**
  - [ ] Week V3: Allocate 8h per developer för test-writing
  - [ ] Week V4: Hit 50% coverage goal
  - [ ] Week V5: Hit 70% coverage goal
  - [ ] Parallel: Write tests AS you develop (not after)
  - [ ] Setup CI/CD to report coverage (SonarQube, Codecov)
  - [ ] Add pre-commit hook: "Fail if coverage drops below 50%"
- **Owner:** All teams
- **Review Date:** V6 (24 Sep) - Must report coverage to CTO

---

### Risk #6: CTO Feedback V7 Comes Late, Delays Omtag
- **Impact:** 🟡 HIGH
- **Probability:** 🟡 MEDIUM (40%)
- **Severity:** 5/10
- **Description:** CTO-feedback publiceras sent i V7, vi hinner inte bearbeta innan kvaldemo V10
- **Why It Matters:** Vi ska visa en demo V10 men feedback från V7 kanske förändrar prioriteringar
- **Current Status:** Timing är tight (V7 feedback → V8-V9 bearbetning → V10 demo)
- **Mitigation:**
  - [ ] Submit CTO-underlag by 24 Sep, 15:00 (1 hour buffer before 16:00 deadline)
  - [ ] CTO feedback is expected V7 Monday
  - [ ] Schedule "feedback analysis" meeting torsdag V7
  - [ ] Identify "must-change" vs "nice-to-have" feedback
  - [ ] Only implement must-changes before demo
  - [ ] Track all feedback in DECISIONS.md
- **Owner:** Team Lead / PL
- **Review Date:** V8 (5 Oct)

---

## 🟢 Medium Risks (Yellow-Green)

### Risk #7: Fredags LIA-sök Tar För Mycket Energi
- **Impact:** 🟢 MEDIUM
- **Probability:** 🟡 MEDIUM (60%)
- **Severity:** 4/10
- **Description:** Fredagar är helgade för LIA-sök. Utveckling pausar. Kan påverka momentum innan deadlines.
- **Why It Matters:** Två helt pausade dagar / vecka reducerar kapacitet med ~30%. Framför CTO-deadline kan detta bli problem.
- **Current Status:** Fredagar är obligatoriska per kursschema, inte flexibla
- **Mitigation:**
  - [ ] Plan längre features before fredagar (så momentum inte brytes)
  - [ ] Document solutions torsdag (skapa notes för nästa vecka)
  - [ ] Pair-programming for longer issues (två personer, samma blockers)
  - [ ] Pre-compute torsdag vad fredags-pausering påverkar nästa vecka
- **Owner:** Team Lead (capacity planning)
- **Review Date:** Ongoing (monitor each week)

---

### Risk #8: README Architecture Section Not Updated
- **Impact:** 🟢 MEDIUM
- **Probability:** 🟡 MEDIUM (50%)
- **Severity:** 3/10
- **Description:** README visar v1-arkitektur, inte v2. Förvirrande för nya läsare och CTO-bedömare.
- **Why It Matters:** CTO läser README som första sak. Förväxlad arkitektur = dåligt första intryck.
- **Current Status:** README är 40% done. Arkitektur-sektion är tom.
- **Mitigation:**
  - [ ] Update README section: "System Architecture"
    - Include: Frontend → Backend → Native → Database stack diagram
    - Include: Data flow for portfolio-data and FX-conversion
    - Include: Where each component runs
  - [ ] Add architecture diagram (even ASCII is ok, visual is better)
  - [ ] Link to DECISIONS.md for detailed rationale
- **Owner:** Backend Lead (kan skriva arkitektur-delen)
- **Review Date:** V5 (20 Sep) - Must be done 4 days before CTO deadline

---

### Risk #9: Google Sheets Risk Matrix Not Accessible
- **Impact:** 🟢 MEDIUM
- **Probability:** 🟡 MEDIUM (50%)
- **Severity:** 2/10
- **Description:** Risk-data ligger i Google Sheets, men länken är privat eller förlorad
- **Why It Matters:** Vi kan inte hämta risk-prioriteringar från customer/PL. Guessar prioriteringar.
- **Current Status:** Du delade länk via Google Sheets, men vi kör detta som GitHub doc nu
- **Mitigation:**
  - [ ] Get link from user / access Google Sheets
  - [ ] Migrate risk-data from Sheets to RISKS.md (this file)
  - [ ] Keep Sheets as single source of truth, update monthly
  - [ ] OR: Use this RISKS.md as master, update Sheets weekly
- **Owner:** Team Lead
- **Action:** Share Google Sheets link or data so we can integrate

---

## 🔵 Low Risks (Green)

### Risk #10: Component Library Not Started
- **Impact:** 🔵 LOW
- **Probability:** 🟢 LOW (20%)
- **Severity:** 2/10
- **Description:** Vi bygger ad-hoc komponenter. Framåt kan det bli design-inkonsistenenser.
- **Why It Matters:** MVP är ok utan design-system. Men om vi vinner demo, behöver vi skalbar arkitektur.
- **Current Status:** Dashboard-komponenter är halvt wiederanvändbara
- **Mitigation:**
  - [ ] Not priority for V2 (focus on MVP)
  - [ ] V3-V5: Dokumentera komponenter (Storybook) om tid
  - [ ] Fallback: Manual component audit before V6, dokumentera
- **Owner:** Frontend Lead (low priority)
- **Review Date:** V5 (optional, only if time)

---

## 🎯 Risk Response Matrix

| Risk ID | Risk Name | Response | Owner | By Date |
|---------|-----------|----------|-------|---------|
| #1 | Back-Testing Performance | MITIGATE - Benchmark & optimize | Native | V6 (24 Sep) |
| #2 | BE-FE Integration | MITIGATE - Define contract, E2E test | BE + FE Leads | V4 (14 Sep) |
| #3 | PostgreSQL Migrations | MITIGATE - Write Flyway migrations | Backend | V3 (13 Sep) |
| #4 | Native Architecture | MITIGATE - Design meeting, document | Arch Owner | V3 (13 Sep) |
| #5 | Test Coverage Low | MITIGATE - Allocate test time | All | V6 (24 Sep) |
| #6 | CTO Feedback Late | MITIGATE - Track & prioritize | Team Lead | V8 (5 Oct) |
| #7 | Friday LIA Capacity | MITIGATE - Plan around it | Team Lead | Ongoing |
| #8 | README Outdated | MITIGATE - Update architecture | Backend Lead | V5 (20 Sep) |
| #9 | Risk Data Not Accessible | RESOLVE - Get link/migrate | Team Lead | Now |
| #10 | Component Library | ACCEPT - Not priority for MVP | Frontend | V3+ |

---

## 📋 How to Use This Document

### For Daily Standups
- Check "Critical Risks" — are we making progress on mitigation?
- Update status on high-impact risks

### For Weekly PL-Meetings
- Bring top 3 risks to discuss
- Report on mitigation progress
- Identify new risks

### For Sprint Planning
- Check risk matrix before estimating
- If risk is HIGH probability, allocate buffer time
- Example: If #2 (BE-FE integration) is MEDIUM, add 4h buffer to estimates

### For CTO Review (V6)
- Risk #1-5 MUST be mitigated or reported
- CTO will ask: "What are your top risks? How are you handling them?"
- Show this doc as proof of risk management

---

## 🔄 Update Cadence

| When | Who | What |
|------|-----|------|
| **Tuesdays 14:00** | Team Lead | Review high-impact risks after PL-meeting |
| **Thursdays 14:30** | Team Lead | Blocker check-in, update risk status |
| **Weekly** | Risk Owners | Report on mitigation progress |
| **Monthly (V6, V9, V12)** | Team | Full risk audit before major deadlines |

---

## Template: Adding New Risk

```markdown
### Risk #N: [Risk Name]
- **Impact:** [RED/YELLOW/GREEN]
- **Probability:** [HIGH/MEDIUM/LOW]
- **Severity:** X/10
- **Description:** [What could go wrong?]
- **Why It Matters:** [What's the business/deadline impact?]
- **Current Status:** [GREEN/YELLOW/RED]
- **Mitigation:**
  - [ ] Action 1
  - [ ] Action 2
- **Owner:** [Person responsible for mitigation]
- **Review Date:** [When to check progress]
```

---

**Last Updated:** 2026-09-04  
**Maintained By:** Team 1  
**Questions?** Läs SPRINT_PLANNING.md eller ask Team Lead
