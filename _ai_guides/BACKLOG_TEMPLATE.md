# 📋 Issue Backlog Templates

**Denna fil innehåller förslagna issues för Team 1 Avanza-projektet.**

**Hur du använder detta:**
1. Kopiera issue-template du vill skapa
2. Gå till GitHub Project
3. Skapa ny issue
4. Paste template-innehållet
5. Uppdatera efter dina behov

---

## 🔴 Critical Path - V3-V6 (Must Do Before CTO Deadline 24 Sep)

### Backend Issues

#### Issue Template #52: Portfolio Data API

```markdown
## feat(backend): Implement portfolio data API endpoint (#52)

### Problem
Frontend currently uses mock data. Backend needs to expose actual portfolio data from PostgreSQL.

### Solution
Implement REST endpoint GET /api/portfolio that:
1. Fetches all accounts for logged-in user
2. Fetches all holdings for each account
3. Fetches current prices and FX rates
4. Returns consolidated portfolio in SEK

### Acceptance Criteria
- [ ] GET /api/portfolio returns portfolio data in JSON
- [ ] Values are correctly converted to SEK (calls FX service)
- [ ] Response includes: `{ total_value_sek, accounts: [...], holdings: [...] }`
- [ ] Endpoint is secured (requires auth token)
- [ ] Response time < 1 second
- [ ] Integration tests pass (uses real DB)

### Technical Details
- Uses Spring Data JPA for queries
- Calls Native FX service via REST
- Returns PortfolioDTO with TypeScript-compatible structure

### Blockers
- Waiting for: FX-service (issue #56) to be callable
- Waiting for: PostgreSQL schema migrations (issue #51)

### Estimate
16 hours

### Definition of Ready
- [x] AC are measurable
- [x] No hidden dependencies
- [x] Assigned to developer
- [ ] Test strategy defined

### Related
- Architecture: DECISIONS.md - "Backend portfolio service"
- Tests: Must include integration test calling real DB
```

---

#### Issue Template #53: Risk Metrics Service

```markdown
## feat(backend): Calculate portfolio risk metrics (#53)

### Problem
User cannot see risk breakdown (allocation %, volatility, Sharpe ratio, max drawdown).

### Solution
Implement RiskMetricsService that calculates:
1. Asset allocation (% stocks, % bonds, % cash)
2. Portfolio volatility (standard deviation)
3. Sharpe ratio (risk-adjusted return)
4. Max drawdown (biggest drop from peak)

### Acceptance Criteria
- [ ] GET /api/portfolio/metrics returns risk metrics
- [ ] Calculation uses actual holdings and prices
- [ ] Supports custom time window (1y, 3y, 5y, all-time)
- [ ] Response time < 2 seconds
- [ ] Unit tests for each metric calculation (70%+ coverage)
- [ ] Integration test with real data

### Technical Details
- Uses historical price data from database
- Calls Native back-testing engine for Sharpe ratio
- Returns MetricsDTO

### Blockers
- Waiting for: Native back-testing service (issue #15)

### Estimate
12 hours

### Related
- Native issue #15: Back-testing engine
- Frontend issue #55: Display metrics in UI
```

---

### Frontend Issues

#### Issue Template #54: Connect Dashboard to Backend API

```markdown
## feat(frontend): Connect Dashboard to Backend portfolio API (#54)

### Problem
Dashboard currently displays mock data. Need to fetch real portfolio data from backend.

### Solution
Replace mock portfolio data with API calls:
1. Call GET /api/portfolio on component mount
2. Display loading state while fetching
3. Show error state if API fails
4. Render actual portfolio data

### Acceptance Criteria
- [ ] Dashboard fetches data from GET /api/portfolio
- [ ] Loading spinner shows while fetching
- [ ] Error boundary handles API failures
- [ ] Data displays correctly (values, allocations, etc)
- [ ] All values shown in SEK
- [ ] Refresh button refetches data
- [ ] TypeScript types match API response

### Technical Details
- Uses React Query or Fetch API
- Error handling for 401 (auth), 500 (server)
- TypeScript interfaces from backend DTO

### Blockers
- Waiting for: Backend API endpoint #52

### Estimate
12 hours

### Definition of Ready
- [x] Backend #52 is DONE (API endpoint ready)
- [x] API contract defined in DECISIONS.md
- [x] TypeScript types ready

### Related
- Backend issue #52: Portfolio API
- Backend issue #53: Risk Metrics API
```

---

#### Issue Template #55: Target Allocation UI Component

```markdown
## feat(frontend): Build target allocation UI component (#55)

### Problem
User needs visual way to set/view target allocation (60% stocks, 40% bonds, etc).

### Solution
Create interactive allocation component:
1. Display current allocation as pie/donut chart
2. Allow user to input target allocation percentages
3. Show delta between current vs target
4. Save target allocation

### Acceptance Criteria
- [ ] Component displays current allocation chart
- [ ] User can input target percentages (stocks, bonds, cash)
- [ ] Delta shown visually (green=goal met, yellow=diff, red=far off)
- [ ] Save button persists target allocation
- [ ] Responsive on mobile
- [ ] TypeScript: all props & state typed
- [ ] Unit tests for calculations

### Technical Details
- Uses React Chart library (Recharts, D3)
- CSS Modules for styling
- Stores allocation in backend (POST /api/portfolio/target)

### Blockers
- Waiting for: Backend portfolio API #52

### Estimate
12 hours

### Related
- Backend issue #52: Portfolio API
- Design: [Link to Figma mockup]
```

---

### Native Issues

#### Issue Template #56: Complete FX Conversion Module

```markdown
## feat(native): Complete FX currency conversion module (#56)

### Problem
Backend needs fast FX conversion for portfolio values (USD/EUR/GBP → SEK).

### Solution
Implement C++ FX converter that:
1. Loads historical FX rates from JSON
2. Converts single currency → SEK
3. Handles 500 conversions < 100ms
4. Thread-safe for concurrent calls

### Acceptance Criteria
- [ ] Converts USD, EUR, GBP to SEK
- [ ] Handles historical rates (not just current)
- [ ] Performance: 500 conversions < 100ms
- [ ] Thread-safe implementation
- [ ] Proper error handling (null checks, edge cases)
- [ ] Unit tests for all conversion paths
- [ ] Callable from Backend via REST/JNI

### Technical Details
- Uses Jansson for JSON parsing
- Memory-efficient storage of rates
- No external API calls (data pre-loaded)

### Blockers
- Waiting for: Decision on BE-Native integration pattern (REST vs JNI)

### Estimate
20 hours

### Related
- Architecture decision: DECISIONS.md - "BE-Native Integration"
- Backend issue #52: Calls this service
```

---

## 🟡 High Priority - V4-V6 (Important But Not Blocking)

### Issue Template #57: Integration Tests for Backend API

```markdown
## test(backend): Write integration tests for portfolio API (#57)

### Problem
API endpoints exist but no integration tests. Risk of regression.

### Solution
Write integration tests that:
1. Start Spring Test container
2. Call real database
3. Test all API endpoints
4. Verify response structure and values

### Acceptance Criteria
- [ ] Tests for GET /api/portfolio
- [ ] Tests for GET /api/portfolio/metrics
- [ ] Tests for edge cases (empty portfolio, no user)
- [ ] Coverage ≥ 70% of backend code
- [ ] All tests pass locally

### Estimate
8 hours

### Definition of Ready
- [x] API endpoints already implemented (#52, #53)
```

---

### Issue Template #61: Add Unit Tests for Frontend Components

```markdown
## test(frontend): Add unit tests for Dashboard components (#61)

### Problem
Frontend components have no test coverage. CTO expects 60%+.

### Solution
Write unit tests using Vitest:
1. Test component rendering
2. Test data transformations
3. Test error states
4. Test user interactions

### Acceptance Criteria
- [ ] Tests for Dashboard component
- [ ] Tests for Portfolio display
- [ ] Tests for Allocation chart
- [ ] Coverage ≥ 60%
- [ ] All tests pass

### Estimate
12 hours

### Related
- CTO requirement: 60% frontend test coverage
```

---

## 🟢 Medium Priority - V5+ (Nice-To-Have)

### Issue Template #62: Update README with Architecture Diagram

```markdown
## docs(all): Update README with current architecture (#62)

### Problem
README architecture section is outdated (v1 design).

### Solution
Update with current stack:
- Frontend → Backend → Native flow
- Database schema overview
- Integration points

### Acceptance Criteria
- [ ] README section "System Architecture" complete
- [ ] Includes data flow diagrams
- [ ] Documents all 3 layers (FE, BE, Native)
- [ ] Links to DECISIONS.md

### Estimate
4 hours
```

---

### Issue Template #63: Performance Benchmark for Back-Testing

```markdown
## perf(native): Benchmark back-testing engine performance (#63)

### Problem
Need to verify back-testing meets 2-second requirement for 500 instruments/5 years.

### Solution
Create benchmark test:
1. Load 500 instruments
2. Load 5 years historical data
3. Run back-test
4. Measure execution time
5. Profile for hotspots

### Acceptance Criteria
- [ ] Benchmark completes in < 2 seconds
- [ ] 500 instruments tested
- [ ] 5 years historical data
- [ ] Profiling identifies slow functions
- [ ] Optimization plan if needed

### Estimate
8 hours

### Blockers
- Waiting for: Back-testing engine mostly done (#15)
```

---

## 🔵 Future/Backlog - V7+ (Post-MVP)

### Issue Template #100: Component Library / Storybook

```markdown
## docs(frontend): Build Storybook for reusable components (#100)

### Problem
Components are ad-hoc. Difficult to reuse.

### Solution
Create Storybook with:
1. All Dashboard components
2. All chart types
3. All form inputs
4. Usage examples

### Priority: LOW - Not needed for MVP

### Estimate
16 hours (if done)
```

---

## 🎯 How To Use This File

### When Creating New Issues:
1. Find the template that fits your need
2. Copy the `markdown` block
3. Go to GitHub Project
4. Click "Add issue"
5. Paste the template
6. Customize title, description, numbers
7. Add to project board

### When Running Meetings:
1. Do NOT copy-paste issues FROM this file into AI
2. Instead: Copy-paste issues FROM GitHub Project into AI
3. This file is just for CREATING new issues in GitHub

### Important:
- **This file:** Issue templates/suggestions
- **GitHub Project:** Actual issues (single source of truth)
- **AI meetings:** Read issues FROM GitHub Project, NOT from this file

---

## 📚 Related Documents

- **SPRINT_PLANNING.md** - How to plan sprints
- **BACKLOG_TEMPLATE.md** - This file (issue templates)
- **DECISIONS.md** - Why we made certain architecture choices
- **GitHub Project Board** - Real-time sprint tracking

---

*Last Updated: 2026-09-04*  
*Purpose: Issue templates for GitHub Project*  
*Version: v1 - Initial set of MVP issues*
