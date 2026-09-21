# End-to-end run — Coding Assistance

**Date:** 2026-09-18  
**Context ref:** `dev`  
**Test case:** `_audit/END_TO_END_TEST_CASES.md` → Test 1

## Test prompt

> Jag jobbar i frontend och ska börja använda ett nytt portfolio-API. Hjälp mig
> med koden och kontrollera om det finns något i backend/native eller på aktiva
> brancher som jag behöver stämma av innan jag bygger vidare.

## Routing verified

Fresh-entry routing resolved:

```text
README.md
  → PROJECT_CONTEXT_ROUTER.md
  → CONTEXT_REGISTRY.yaml
  → tasks.coding_assistance
```

The coding bundle loaded the registered project authorities for:

- team workflow
- testing
- goals/planning
- risk management
- dependencies/capacity
- cross-layer awareness
- technical debt
- team communication

## Exact project sources inspected

### Context sources

- `README.md`
- `CONTEXT_REGISTRY.yaml`
- `_ai_guides/project/PROJECT_CONTEXT_ROUTER.md`
- `_ai_guides/project/CROSS_LAYER_AWARENESS.yaml`
- `_ai_guides/project/DEPENDENCIES_AND_CAPACITY.md`
- `_ai_guides/project/RISK_MANAGEMENT.md`
- `_ai_guides/project/TECHNICAL_DEBT.md`
- `data/SOURCES.yaml`

### GitHub project state

Repository:
`chas-challenge-2026/avanza-team1`

Relevant branches inspected included:

- `frontend/#82-use-portfolio`
- `frontend/#83-save-allocation`
- `frontend/#43-api-client-mock-adapter`
- `Java-Development-Environment`
- `C/C++-Native`
- relevant older Java feature/refactor branches for activity comparison
- `develop`

Relevant implementation/docs inspected included:

- `frontend/src/types/portfolio.ts`
- `frontend/src/api/portfolioApi.ts`
- `frontend/src/api/adapters/httpPortfolioApi.ts`
- `frontend/src/hooks/usePortfolio.ts`
- `frontend/src/hooks/useSaveAllocation.ts`
- `backend/.../controller/DashboardController.java`
- `backend/.../service/PortfolioService.java`
- `backend/.../entity/TargetAllocation.java`
- `backend/.../api/NativeBridgeModule.java`
- `native/backtestbridge/backtestbridge.cpp`
- `docs/v2-targets.md`
- `frontend/README.md`
- `docs/frontend/BESLUT.md`
- GitHub issues #3, #43, #82 and #83
- related pull requests
- registered `GOOGLE_RISK_REGISTER`

## Verified current state

- Frontend has a stable `Portfolio` TypeScript shape and adapter/hook boundary.
- The HTTP adapter explicitly states that `GET /api/portfolio` is not wired yet.
- Frontend also has a stub for `PUT /api/allocation`.
- Backend issue #3 exists for `POST /api/auth/login` and `GET /api/portfolio`.
- Issue #3 currently describes the portfolio response as accounts, holdings and
  total value.
- The frontend `Portfolio` contract additionally contains `userName`, `fx`,
  `allocation` and `alerts`.
- No implemented REST `@RestController` for the portfolio endpoint was found in
  the inspected current Java code.
- No backend issue for the frontend's `PUT /api/allocation` stub was found in
  the issue searches used by this test.
- Native/JNA currently exposes backtest result fields; no evidence inspected in
  this run made Native a direct prerequisite for the basic frontend
  `GET /api/portfolio` read contract.
- Existing risk R-24 already tracks frontend mock/Java portfolio-contract
  divergence and is currently marked `In progress`.

## Correct AI classification

### 🔎 AI-analys — needs synchronization

This is **not yet a verified implementation mismatch**, because the backend REST
endpoint is not implemented in the inspected code.

There is, however, a verified contract-specification gap:

- frontend has a richer concrete `Portfolio` shape
- backend issue #3 does not currently enumerate the complete frontend shape

This should be synchronized before backend implementation is treated as ready
for frontend HTTP integration.

### Existing risk, not a new risk

The analysis maps to existing risk **R-24**.

The AI should update/check that risk rather than propose a duplicate risk.

### ⭐ AI-förslag — smallest useful synchronization step

Before further live API integration:

1. compare issue #3 response requirements against the current frontend
   `Portfolio` type
2. explicitly decide the minimum JSON contract for every required field
3. decide whether `PUT /api/allocation` belongs in issue #3 or a separate
   backend issue
4. add contract/integration verification before switching
   `VITE_USE_MOCK=false`

## Technical debt result

No verified technical debt was declared solely because the HTTP adapter is a
stub or because backend work is incomplete.

That is currently planned incomplete work.

The analysis would become a debt signal if incompatible/duplicated contract
assumptions begin spreading into more implementations without synchronization.

## Test verdict

**PASS**

The context system caused the AI to:

- answer beyond the local frontend surface
- inspect relevant active branches
- find an existing contract and existing backend issue
- detect a contract need before late integration
- distinguish incomplete work from technical debt
- check the canonical risk register before proposing a risk
- avoid inventing a duplicate risk
- propose a small synchronization step rather than a broad rewrite

## Improvement discovered by the test

The underlying project appears to need explicit synchronization of:

- full `GET /api/portfolio` response shape
- ownership/scope for `PUT /api/allocation`

This is a project-work finding, not a new context-repository rule.

---

**Status:** PASS
