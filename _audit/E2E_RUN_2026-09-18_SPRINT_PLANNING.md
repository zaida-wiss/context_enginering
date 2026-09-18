# End-to-end run — Sprint Planning

**Date:** 2026-09-18  
**Context ref:** `dev`  
**Test case:** `_audit/END_TO_END_TEST_CASES.md` → Test 3

## Test prompt

> Hjälp oss planera nästa sprint. Vad bör sprintmålen, milestones och issues vara?

## Exact sources checked

- `GOOGLE_SPRINT_PLANNING` discovery against Team Avanza 1 spreadsheet metadata
- `GOOGLE_MEETING_PROTOCOL`
- `data/manual/course/CTO_FEED_FORWARD.md`
- GitHub repository state for `chas-challenge-2026/avanza-team1`
- GitHub issue #3
- frontend portfolio decisions and API adapter state
- `GOOGLE_RISK_REGISTER`, including R-24

## Verified current planning state

### Sprintplanering source

The Team Avanza 1 spreadsheet does **not** currently contain a worksheet named
exactly `Sprintplanering`.

Result:

```text
GOOGLE_SPRINT_PLANNING = UNAVAILABLE_NOT_YET_CREATED
```

This is not an error. The planning authority correctly falls back to confirmed
meeting decisions and registered milestone/course sources.

### Meeting protocol

For the upcoming/current meeting section:

- `Sprintmål` is empty
- `Sprintplan` is empty
- `Prioritering` is empty
- `Blockers` is empty
- Capacity contains one documented qualitative constraint:
  `Frontend: Zaida bortrest onsdag och torsdag (ledig)`

No verified numeric capacity is present.

### Consequence

There is currently **no verified decided sprint goal** in the inspected planning
sources.

GitHub activity can show current work and dependencies, but it must not be
relabelled as the team's decided sprint goal.

## Correct AI response shape

### Verified fact

> Inget beslutat sprintmål kunde verifieras i `Sprintplanering` eller i den
> aktuella delen av mötesprotokollet.

### Capacity state

```yaml
capacity_state: "unknown_numeric_capacity"
verified_constraint:
  frontend:
    - "Zaida bortrest onsdag och torsdag (ledig)"
behavior:
  - "Do not convert this into guessed hours or percentages."
```

## 🔎 AI-analys

Three pieces of verified evidence create a useful planning direction:

1. Backend issue #3 remains open for `GET /api/portfolio`.
2. Frontend already depends on a stable `Portfolio` contract and risk R-24
   tracks mismatch between frontend mock and Java API.
3. CTO Feed Forward has a verified deadline on 2026-09-24 at 16:00 and explicitly
   requires evidence of how risk work changed real decisions.

## ⭐ AI-förslag — next sprint purpose

> **Stabilisera integrationsvägen Frontend ↔ Backend samtidigt som teamet
> färdigställer verifierbart CTO-underlag från faktisk riskhantering.**

This is a proposal, not a decided team goal.

### Why

It connects the most immediate integration dependency with the nearest verified
course deliverable.

### Expected effect

- lower integration uncertainty around the portfolio contract
- better evidence for CTO Feed Forward
- fewer late changes when mock mode is replaced by live backend data

### Trade-off

Lower-value independent work may need to wait if it consumes capacity needed for
contract clarification, backend integration or the CTO deliverable.

## ⭐ AI-förslag — sprint goals

### Goal 1 — Portfolio contract ready for live integration

**Outcome:** Frontend and Backend share an explicit, testable portfolio response
contract and the backend work reflects the fields the frontend actually consumes.

**Evidence:**
- issue #3
- frontend `Portfolio` type
- R-24

**Success evidence:**
- agreed field/type/null/error contract
- issue #3 corrected/clarified where needed
- integration/contract verification exists before `VITE_USE_MOCK=false`

### Goal 2 — Allocation-save backend path is explicitly owned

**Outcome:** The existing frontend `PUT /api/allocation` stub has a confirmed
backend scope/issue or a documented decision to defer it.

**Evidence:**
- frontend issue #83 / adapter
- no matching backend issue found in the issue searches used by this run

**Success evidence:**
- existing backend issue is linked, or
- `⭐ AI-förslag` to create a new backend issue is accepted by the team

### Goal 3 — CTO Feed Forward is ready with decision-impact evidence

**Outcome:** The team can show a few concrete examples of:

```text
risk → trade-off/mitigation → technical/planning decision → verification
```

**Evidence:**
- CTO Feed Forward instructions
- canonical risk register

**Success evidence:**
- selected examples are source-backed
- mitigations are realistic and verifiable
- remaining uncertainty is stated
- video is ready/submitted before the verified deadline

## ⭐ AI-förslag — milestones/checkpoints

1. **Portfolio contract checkpoint**
   - full response shape confirmed between FE and BE
2. **Backend integration checkpoint**
   - `GET /api/portfolio` returns the agreed contract in an integration-ready path
3. **Allocation-save ownership checkpoint**
   - backend scope for `PUT /api/allocation` is explicit
4. **CTO evidence checkpoint**
   - 2–3 risk-to-decision examples selected and verified
5. **CTO submission**
   - 2026-09-24 16:00

Only the CTO submission is an externally verified deadline; the earlier
checkpoints are AI proposals.

## ⭐ AI-förslag — issue handling

### Correct existing work before creating duplicates

- **Issue #3:** clarify/correct response contract so it matches the fields the
  frontend is expected to consume.
- **Allocation save:** search again for existing backend work before creating a
  new issue. If none exists, propose a backend issue for the required save path.
- **Contract verification:** if no existing issue owns FE↔BE contract testing,
  propose one only when the team confirms it is missing.

## Test verdict

**PASS**

The flow correctly:

- refused to invent a decided sprint goal
- discovered that `Sprintplanering` does not yet exist
- preserved missing numeric capacity as unknown
- used a documented qualitative availability constraint without converting it
  into guessed hours
- generated future sprint goals as `⭐ AI-förslag`
- linked proposals to verified project evidence
- avoided duplicate issue creation where existing work could be corrected first

## Context improvement discovered and implemented

A dedicated conditional source `GOOGLE_SPRINT_PLANNING` was added to
`data/SOURCES.yaml`.

It dynamically checks whether the exact `Sprintplanering` worksheet exists.
When it appears in the future, it becomes the primary source for decided sprint
planning without requiring another context-rule rewrite.

---

**Status:** PASS
