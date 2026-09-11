# 📋 Routine: Keep Living Docs Updated

**Living Docs = Dokumentation som uppdateras löpande, INTE efter allt är klart**

Denna guide visar när och hur ni uppdaterar:
- Risker & Blockers
- Assets
- README
- Arkitektur-beslut  
- AI-användning

---

## 🎯 Två Trigger-Punkter för Uppdateringar

### 1️⃣ UNDER MÖTEN (Monday, Tuesday, Thursday)
Sammanfattningar från vad som diskuterades, beslut som togs, status för veckan.

### 2️⃣ UNDER ISSUE-ARBETE (Continuous)
Medan ni BYGGER, dokumenterar ni samtidigt — inte efter.

---

## 📅 MÖTE → UPPDATERINGAR

### MÖNDAG 09:00 - Sprint Planning Meeting

**Läs från:**
- ✅ Mötesprotokollet (vad diskuterades)
- ✅ Git log förra veckan (vad gjordes)
- ✅ GitHub Project Board (vilka issues blev done/blocked)

**Uppdatera:**

#### 1. RISK_DASHBOARD.md
```markdown
## 🟠 DENNA VECKA — Risk Assessment

### Overall Status: ORANGE — Slight Delay
- Sprint goal: Risk Metrics ✅ | FX Converter 🟠 | Tests 70%+
- Timeline: Torsdag 15:00 deadline
- Capacity: Backend är 60%, behöver support

### Per Team:

🟢 FRONTEND — ON TRACK
- Progress: 80% 
- No blockers
- Can support other teams

🟠 BACKEND — SLIGHT DELAY (recoverable)
- Progress: 60%
- Blocker: Swagger spec unclear (Marco + Jan to clarify idag)
- Action: Pair prog Backend+Frontend tis 14:00

🔴 NATIVE — CRITICAL
- Progress: 40%
- Blocker: Calculation spec missing
- Action: Backend + Native pair prog idag 14:00
- Escalation: Need decision on scope cut if not resolved today
```

**Guiding Questions:**
- ❓ Vilka team ligger bakom tidplanen?
- ❓ Vilka blockers kan vi lösa idag?
- ❓ Behöver vi ändra scope eller allokera resurser?

---

#### 2. DECISIONS.md (Om Arkitektur-beslut Togs)
```markdown
## Denna vecka gjorda beslut:

### Backend API Design — Risk Metrics Endpoint (Tis 13:00 möte)
**Decision:** Returnera aggregated risk metrics från `/api/portfolio/metrics`

**Reasoning:** 
- Enkel för frontend att konsumera
- Backend kan casha aggregation
- Matchar design-mockups

**Alternatives considered:**
- Returnera raw data, let frontend aggregate (rejected: too slow)
- Separate endpoints per metric (rejected: many API calls)

**Who decided:** Marco (Backend lead) + Anna (Frontend lead)

**When implemented:** Start tis, ready for test wed

**Impact:** Frontend kan nu call single endpoint instead of multiple
```

**Guiding Questions:**
- ❓ Vilka arkitektur-val gjordes denna vecka?
- ❓ Vem beslutade och varför?
- ❓ Vilka alternativ overvägs men förkastades?

---

#### 3. TEAMSTANDARDS.md — Git Weekly Status (If Changes)
```markdown
## Denna vecka — Git Activity

From `git log --oneline --since="7 days ago"`:

### Frontend (Anna, Marco)
- 5 commits
- Branch: `feature/#47-portfolio-dashboard`
- PR in review (#48)
- Linting: ✅ Pass

### Backend (Marco, Jan)
- 8 commits  
- Branches: `feature/#42-risk-metrics`, `fix/#45-fx-conversion`
- 2 PRs merged (risk metrics, FX tests)
- Linting: ⚠️ One file needs prettier

### Native (Kiran)
- 2 commits
- Waiting on backend spec
```

---

### TISDAG 13:00 - Status Sync Meeting

**Läs från:**
- ✅ Mötesprotokollet (status updates, blockers)
- ✅ GitHub Project Board (issues moved to Done/In Progress/Blocked)
- ✅ Meeting notes från breakout discussions

**Uppdatera:**

#### 1. RISK_DASHBOARD.md — Mid-Week Update
```markdown
## MID-WEEK UPDATE (Tis 13:00 status sync)

### Overall Status Update
- 🟢 Frontend: On track, API integration done ✅
- 🟠 Backend: Risk Metrics 80% (will be done tors)
- 🔴 Native: Still blocked on spec — BUT meeting with Backend idag 14:00

### Actions Taken Since Mön:
- ✅ Backend + Frontend pair prog idag → API contract clear now
- ✅ Swagger docs 80% written
- ⏳ Native waiting for spec to start Sharpe ratio calc

### Revised Thursday Timeline:
- Backend: Risk Metrics 100% (moved from 80%)
- Frontend: Ready to test by wed evening
- Native: Can start dev after 14:00 spec session
```

**Guiding Questions:**
- ❓ Vad moved since Monday? Vilka issues är klara?
- ❓ Vilka blockers lösta?
- ❓ Vilka nya risker dykt upp?

---

#### 2. README.md — Feature Updates (If Completed)
```markdown
### FX Converter Component (NEW — implemented this week)

**Status:** Ready for testing

**How it works:**
- Fetches current rates from [Backend API endpoint]
- Converts ISK/Stocks/Funds to SEK
- Updates when rate data is stale (> 1 hour old)

**Testing:**
- Unit tests: ✅ Pass
- E2E test: ⏳ (native team blocked on spec)

**Known limitations:**
- Rates cached locally (not real-time)
- Does not handle offline mode yet
```

---

### TORSDAG — Sprint Review + Retrospective

**Läs från:**
- ✅ Git log denna vecka (all commits + PRs merged)
- ✅ GitHub Project Board (final status — what's Done, what's Blocked)
- ✅ Team retrospective notes

**Uppdatera:**

#### 1. SPRINT_SUMMARY.md (New or Update)
```markdown
# Sprint Week of Sept 8-12, 2026

## Goals
- [x] Risk Metrics complete
- [x] FX Converter start
- [ ] Tests at 70% (achieved 65% — close)

## Completed
- ✅ Risk Metrics API + Frontend component (Marco + Anna)
- ✅ FX conversion backend logic (Jan)
- ✅ E2E test for portfolio flow (Anna)

## Blocked/At Risk
- 🟠 Native: Sharpe ratio awaiting spec
- 🟠 Tests: 65% not 70% (need 5% more coverage)

## Key Decision
- Decided to merge FX to develop Friday (not wait for native)
- Reason: Portfolio view can show ISK values Monday

## Learnings
- Pair programming helped Backend+Frontend alignment (do this again)
- Spec clarity is blocking native (need spec review process?)

## Next Sprint Focus
- Get native unblocked (spec ready day 1)
- Hit 70%+ test coverage
- Stabilize FX conversion edge cases
```

**Guiding Questions:**
- ❓ Vilka goals nådde vi?
- ❓ Vilka blev blocked och varför?
- ❓ Vad lärdomar tar vi till nästa sprint?

---

## 💻 ISSUE-ARBETE → UPPDATERINGAR

### Scenario 1: Du Bygger En Ny Feature

**Du:** "Jag bygger den nya PortfolioOverview-komponenten"

**Jag frågar:**
- ❓ Behöver vi dokumentera den i README components-listan?
- ❓ Är detta en ny pattern/arkitektur-beslut?
- ❓ Vilka props och state behöver vi dokumentera?

**Du fyller i tillsammans med mig:**

```markdown
### README.md — Frontend Components Update

#### PortfolioOverview Component (NEW)

**Location:** `src/components/PortfolioOverview/index.tsx`

**Purpose:** 
Shows user their total portfolio value across all accounts (ISK, KF, Depå),
with allocation breakdown and risk metrics.

**Props:**
```typescript
interface PortfolioOverviewProps {
  userId: string;
  onAllocationChange: (allocation: Allocation) => void;
  riskMetrics: RiskMetrics; // from backend API
}
```

**State Management:**
- Uses React Context for user portfolio data
- Fetches from `/api/portfolio/summary` endpoint (Backend responsibility)

**Testing:**
- Unit tests in `PortfolioOverview.test.tsx` ✅
- E2E test in portfolio-flow.spec.ts ⏳

**Design Reference:**
See mockups in UI_DESIGN_REFERENCE.md
```

---

### Scenario 2: Du Gör Ett Arkitektur-Beslut

**Du:** "Vi behöver casha portfolio-data lokalt för performance"

**Jag frågar:**
- ❓ Vilka alternativ överväga vi?
- ❓ Varför denna lösning?
- ❓ Vem bestämde det?

**Du fyller i tillsammans med mig:**

```markdown
### DECISIONS.md — Portfolio Data Caching

**Decision:** Cache portfolio data locally for 5 minutes

**Date:** Sept 10, 2026
**Decision Maker:** Marco (Frontend lead) + Kiran (Native lead)

**Problem:** 
- API calls too frequent (every re-render)
- Slows down portfolio view

**Alternatives:**
1. ✅ **CHOSEN:** Local cache (5 min TTL)
   - Pros: Fast, reduces API load, simple
   - Cons: Data might be stale

2. ❌ **Rejected:** Use React Query
   - Pros: Industry standard
   - Cons: New dependency, complexity

3. ❌ **Rejected:** Backend caching
   - Pros: Single source of truth
   - Cons: Backend not ready, network latency same

**Implementation:**
- File: `src/hooks/usePortfolioCache.ts`
- TTL: 5 minutes (configurable via .env)
- Clear cache on: Manual refresh, logout, etc

**Testing:**
- Unit test: Cache expires after 5 min ✅
- E2E test: Fresh data shows when cache expires ⏳

**Future:** Consider React Query if caching gets complex
```

---

### Scenario 3: Du Stöter på En Risk

**Du:** "Backend API är långsam ibland (takes 2+ seconds)"

**Jag frågar:**
- ❓ Hur ofta händer detta?
- ❓ Vilka åtgärder kan vi ta?
- ❓ Behöver vi anpassa UI för detta?

**Du fyller i tillsammans med mig:**

```markdown
### RISK_DASHBOARD.md — New Risk Identified

## 🟠 MEDIUM RISK — Backend Latency Spikes

**Severity:** Medium
**Team Affected:** Frontend (UI feels slow), Native (timeout risk)
**Discovered:** Sept 11 during portfolio load testing

**Description:**
Risk Metrics endpoint occasionally takes 2-3 seconds (target < 500ms).
Happens when database query joins many tables.

**Root Cause:** 
(Unknown — Backend investigating)

**Mitigation:**
- Frontend: Show loading spinner (better UX than frozen UI)
- Backend: Optimize query / add caching / add index?
- Timeline: Need update by Wed so we can test

**Action Items:**
- [ ] Marco: Profile the slow query (deadline: Tue end of day)
- [ ] Jan: Implement query optimization (deadline: Wed)
- [ ] Anna: Add loading state to PortfolioOverview (deadline: Wed)

**Success Criteria:**
- 95th percentile latency < 800ms
- No timeout errors in tests
```

---

### Scenario 4: Du Använder AI för Något

**Du:** "AI hjälpte mig designa error handling"

**Jag säger:**
- "Ska vi dokumentera hur vi använde AI här för framtida team?"

**Du fyller i tillsammans med mig:**

```markdown
### AI_USAGE.md — New Entry

## Error Handling Pattern (Sept 11)

**Task:** Design error handling for FX conversion failures

**How AI helped:**
- Brainstormed error scenarios (network, invalid rate, timeout)
- Suggested pattern: Custom error types + context wrapper
- Generated test scenarios for edge cases

**What worked well:**
- AI helped think through edge cases we missed
- Pattern is cleaner than our first attempt

**What didn't work:**
- AI suggested try-catch but we needed custom errors
- Had to iterate 2x to get right

**Result:**
Error handling now covers:
- Network failures
- Invalid exchange rates  
- Timeout errors
- User-facing messages are clear

**Next time:**
- Show AI the existing error patterns first (it adapted better)
- Have team review AI suggestions before implementing
```

---

## 🤖 Hur Jag Hjälper Till

### Variant A: Du Ber Mig om Hjälp
**Du:** "Jag jobbar på FX Converter. Hjälp mig skriva koden."

**Jag gör:**
1. Läser issue details
2. Frågar: "Behöver vi dokumentera något här? Beslut? Risk? README-uppdatering?"
3. Guidar dig genom både KOD och DOKUMENTATION samtidigt

### Variant B: Du Vill Uppdatera Dokument
**Du:** "Uppdatera README för PortfolioOverview"

**Jag gör:**
1. Läser senaste issue/PR
2. Läser koden för att förstå vad komponenten gör
3. Föreslår TEXT till dig
4. Du reviewar + editerar
5. Vi committar tillsammans

### Variant C: Du Ber om Template
**Du:** "Jag behöver uppdatera RISK_DASHBOARD men vet inte vad jag ska skriva"

**Jag gör:**
1. Läser mötesprotokollet + GitHub Project Board
2. Skriver DRAFT med example-text
3. Du fyller i specifika siffror/namn
4. Done!

---

## ✅ Checklista för Living Docs

**Varje vecka:**
- [ ] Möndag 09:00: Update RISK_DASHBOARD (after sprint planning)
- [ ] Möndag 09:00: Update DECISIONS.md if decisions made
- [ ] Tisdag 13:00: Mid-week RISK update
- [ ] Torsdag: Update SPRINT_SUMMARY.md
- [ ] Ongoing: Update README when feature completes

**Varje issue:**
- [ ] Nya komponenter → README
- [ ] Arkitektur-beslut → DECISIONS.md
- [ ] Nya risker → RISK_DASHBOARD
- [ ] AI-användning → AI_USAGE.md
- [ ] Breaking changes → README + DECISIONS.md

---

**Målet:** Dokumentationen är aldrig "behind" — den växer tillsammans med koden.
