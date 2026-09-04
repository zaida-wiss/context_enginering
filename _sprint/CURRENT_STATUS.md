# Current Status - Team 1 Sprint Tracking

**Real-time sprint status. Uppdatera denna efter varje PL-möte och vid vecko-slutet.**

---

## 📊 Sprint 37 (v37: 7-13 September 2026)

### 🎯 Sprint Fokus
Enligt SCHEDULE.md V3-V5 fokus:
- **Fungerande delar:** Kompletta backend API:er för portfolio-data
- **Teststatus:** Alla unit tests skrivna, integration-tests runnas
- **README:** Uppdatera arkitektur-sektion

### 📈 Sprintmål
```
[ ] Backend: Portfolio Data API komplett
[ ] Frontend: Connect dashboard to backend
[ ] Native: FX-modul färdig och testerad
[ ] Tests: Min 70% backend coverage
```

### ✅ Issues Planned This Sprint

| Issue | Owner | Scope | Status | Est. | % Done |
|-------|-------|-------|--------|-----|--------|
| [#52] Portfolio Data API | Backend-team | BE | 🔄 WIP | 16h | 30% |
| [#53] Risk Metrics Service | Backend-team | BE | 📋 TODO | 12h | 0% |
| [#54] Connect Dashboard to Backend | Frontend-team | FE | 📋 TODO | 16h | 0% |
| [#55] Target Allocation UI | Frontend-team | FE | 📋 TODO | 12h | 0% |
| [#56] Complete FX Conversion | Native-team | Native | 🔄 WIP | 20h | 45% |
| [#57] Integration Tests | Backend-team | BE | 📋 TODO | 8h | 0% |

**Legend:** 📋 TODO | 🔄 WIP | ✅ DONE | ⏸️ BLOCKED

---

## 🟢 Completed Last Sprint (V36: 31 Aug - 6 Sep)

**Vad blev gjort förra veckan:**

### Frontend ✅
- ✅ Dashboard panel components (issue #26)
- ✅ CSS module refactoring
- ✅ Mock portfolio.json with TypeScript types
- ✅ Navbar + app-shell layout

**Commits:**
```
3054172 build[frontend]: Dashboard components matching design mockup (issue #26)
269cc2f refactor[frontend]: Individual CSS modules for Dashboard components (issue #26)
a274e56 uppdaterad
```

### Backend ✅
- ✅ AlertController → AlertService refactor (issue #51)
- ✅ AuthController → AuthService
- ✅ SOLID principles applied

**Commits:**
```
c1cae3b Merge pull request #51 from chas-challenge-2026/Refactor/Move-controller-logic-to-service
91ed09d Refactor: refactored AlertController, AuthController to corresponding service classes AlertService, AuthService
```

### Native 🟡
- 🟡 FX module WIP - Jansson integration started (issue #17)
- 🟡 Sharpe ratio calculations WIP (issue #15)

**Commits:**
```
bf2029a #17 WIP: Started breaking up FX module into smaller functions.
c7f8bad #13 #15 WIP: Added functionality for sharpe calculations. Also added a separate test-file to test functionalities in set ranges
```

---

## 🔴 Blockers & Risks This Sprint

### Critical Blockers 🚨
**None currently**

### High Priority Risks ⚠️

| Risk | Impact | Mitigation | Status |
|------|--------|-----------|--------|
| **FX-modul langsam** | Back-testing kanske > 2s för 500 instr | Benchmarka denna vecka, optimize om behövs | 🔴 HIGH |
| **Backend-frontend integration** | Dashboard visar mock-data, inte verklig API | Pair-program BE/FE på API-kontraktet | 🟡 MEDIUM |
| **Testing coverage low** | CTO kommer fråga om tests V6 | Skriva tests parallellt med feature-dev | 🟡 MEDIUM |
| **Native team väntar på beslut** | C/C++ integration-point är oklar | Design möte BE + Native denna vecka | 🟡 MEDIUM |

### Medium Priority Risks 📋
- PostgreSQL schema inte helt committed
- No fallback if back-testing fails
- README arkitektur-sektion ligger behind

---

## 📅 Deadlines Tracking

### Denna Vecka (V37)
- **Torsdag:** Standup + blocker-löpning

### Nästa Kritiska Deadlines
| Datum | Milestone | Days Left | Priority |
|-------|-----------|-----------|----------|
| **24 sep, 16:00** | CTO-underlag deadline | 20 days | 🔴 CRITICAL |
| 15 okt, 17:00 | Demo-plan deadline | 41 days | 🟡 HIGH |
| 22 okt | LIVE DEMO | 48 days | 🟡 HIGH |
| 4 nov, 15:00 | FINAL SUBMISSION | 61 days | 🟡 HIGH |

**Fokus fram till V6:** Få kärnflödet 100% fungerande + CTO-ready dokumentation

---

## 👥 Team Capacity This Sprint

### Backend Team (Java/Spring Boot)
- **Availabilty:** 35h coding (minus möten)
- **Capacity:** ~3 issues à 12h
- **Current Load:** 2 issues assigned (40h work planned)
  - ⚠️ **OVER-CAPACITY** - Need to rescope

### Frontend Team (React/TypeScript)
- **Availability:** 35h coding
- **Capacity:** ~2-3 issues à 12h
- **Current Load:** 2 issues assigned (28h work planned)
  - ✅ **OK** - Room for 1 more

### Native Team (C/C++)
- **Availability:** 35h coding
- **Capacity:** ~1-2 issues à 20h (more complex)
- **Current Load:** 1 issue assigned (20h planned), blocked on 1 other
  - ⚠️ **AT CAPACITY** - Needs blocker resolution

---

## 🧪 Test Status

### Backend Testing
- [ ] Unit tests: **30%** written (target: 70%)
  - TODO: Service layer tests
  - TODO: Repository layer tests
  - TODO: Exception handling tests
  
- [ ] Integration tests: **0%** written
  - TODO: API endpoint tests
  - TODO: Database interaction tests
  
- [ ] E2E tests: **0%** written

**Action:** Allocate 8h this sprint for test-writing

### Frontend Testing
- [ ] Unit tests: **10%** written
  - TODO: Component tests
  - TODO: Hook tests
  
- [ ] E2E tests: **0%** written
  - TODO: Dashboard user flow test
  - TODO: Portfolio allocation interaction test

**Action:** Start with Vitest setup + 3 component tests

### Native Testing
- [ ] Unit tests: **20%** written
  - Done: FX conversion tests
  - TODO: Back-testing edge cases
  - TODO: Sharpe ratio tests
  
- [ ] Benchmark tests: **0%** written
  - TODO: 500-instrument performance test
  - TODO: 5-year historical data test

**Action:** Finalize FX tests, start performance benchmarks

---

## 📚 Documentation Status

| Document | Status | % Done | Next Steps |
|-----------|--------|--------|-----------|
| **README.md** | 📋 WIP | 40% | Add architecture section + installation |
| **DECISIONS.md** | ✅ DONE | 100% | Maintain + add new decisions |
| **TEAMSTANDARDS.md** | ✅ DONE | 100% | Reference only |
| **PROJEKTKONTEXT.md** | ✅ DONE | 100% | Reference only |
| **API Documentation** | 📋 TODO | 0% | Create Swagger/OpenAPI spec |
| **Setup Guide** | 🔄 WIP | 30% | Docker compose, local dev setup |

**CTO Deadline V6 (24 sep) requires:** README + Setup guide + DECISIONS complete

---

## 🎯 What's Next This Week

### This Week's Focus (V3-V5 Track)
1. ✅ **Fungerande delar** → Complete Portfolio Data API
2. ✅ **Teststatus** → Write unit + integration tests
3. ✅ **README** → Update architecture + setup sections

### Action Items Due Torsdag (14 Sept)

**Backend Team**
- [ ] Portfolio Data API responds to GET /api/portfolio
- [ ] Integration tests pass locally
- [ ] Service layer dependencies injected properly

**Frontend Team**
- [ ] Dashboard fetches data from backend (not mock)
- [ ] Allocation chart updates when data changes
- [ ] Loading states handled

**Native Team**
- [ ] FX conversion completes without errors
- [ ] Performance benchmark shows < 2s for 500 instruments
- [ ] Error handling for edge cases

**All Teams**
- [ ] Commits follow `type(scope): message (#issue)` format
- [ ] PRs reviewed before merge
- [ ] CURRENT_STATUS.md updated (this file)

---

## 📞 Weekly Check-in

### Tuesday PL-Meeting (Tues 12:30-14:00)
**Preparation:**
1. Update this file before meeting
2. Prepare 3-min summary of this week's progress
3. Bring any blockers or risks to discuss

**Talking Points:**
- "We completed X, we're working on Y"
- "Risk: FX-module performance — we're benchmarking this week"
- "Need help with: [blocker]?"

---

## 📌 How to Use This Document

**For Daily Standups:**
- Check "Blockers & Risks" section
- Update "Issues Planned" table with % Done
- Mark issues DONE when merged

**For Weekly Reviews:**
- Fill in "Completed Last Sprint" section after Monday
- Update "Blockers & Risks" before Tuesday PL-meeting
- Check "Deadlines Tracking" for what's coming

**For Sprint Retro (Optional):**
- Use "What's Next This Week" to plan next sprint
- Note any "lessons learned" in blockers section

**For AI-Agents Reading This:**
- Use "Team Capacity" to understand workload
- Check "Blockers & Risks" before suggesting new work
- Read "Test Status" to know what to prioritize

---

## 🔄 Update Schedule

| When | Who | What |
|------|-----|------|
| **Monday 09:00** | Team Lead | Create new sprint section, set goals |
| **Daily** | Owners | Update % Done on their assigned issues |
| **Tues 12:00** | Team Lead | Refresh status before PL-meeting |
| **Tues 14:00** | After PL | Note feedback/changes from meeting |
| **Thurs 14:30** | Team Lead | Blocker check-in, adjust if needed |
| **Fri 17:00** | Team Lead | Final weekly summary, plan cleanup |

---

**Last Updated:** 2026-09-04 by Zaida Wiss  
**Next Update Due:** 2026-09-08 (Monday before Sprint 37)

---

## Historical Sprint Data (For Velocity Tracking)

| Sprint | Dates | Issues Started | Issues Completed | Velocity (h) |
|--------|-------|-----------------|------------------|-------------|
| V2 | 24-28 Aug | 6 | 3 | 18h |
| V3 | 31 Aug-6 Sep | 8 | 5 | 32h |
| V4 | 7-13 Sep | ? | TBD | ? |
| V5+ | Future | - | - | - |

*Once we have 3-4 sprints of data, we can predict capacity better.*

---

**Ansvarig för uppdateringar:** Team Lead / Scrum Master
**Frågor?** Läs SPRINT_PLANNING.md eller fråga Team Lead
