# End-to-end context test cases

These tests are intended to be run from a fresh AI conversation against the
`dev` README/context entrypoint.

They verify model behavior, not only repository structure.

---

## Test 1 — Coding assistance with system awareness

### Prompt

> Jag jobbar i frontend och ska börja använda ett nytt portfolio-API. Hjälp mig
> med koden och kontrollera om det finns något i backend/native eller på aktiva
> brancher som jag behöver stämma av innan jag bygger vidare.

### Expected behavior

The AI should:

- help with the immediate coding task
- identify the relevant integration boundary
- look for an existing contract before proposing a new one
- inspect relevant active branches when access permits
- distinguish verified compatibility/mismatch from early analysis
- use `🔎 AI-analys` for inferred system-level signals
- use `⭐ AI-förslag` for recommended synchronization/contract actions
- surface relevant dependency, risk or technical-debt signals
- explain why the wider check matters
- avoid unrelated project-wide analysis

### Failure examples

- only answers the local React/code question
- assumes `develop` represents all active work
- invents an API contract as if it were decided
- calls unfinished branch work “technical debt” without evidence

---

## Test 2 — Issue creation with adaptive Definition of Done

### Prompt A — small UI change

> Skapa en issue för att fixa spacing i mobilmenyn.

Expected:
- issue-specific Acceptance Criteria
- suitable visual/responsive verification
- short Applicable Definition of Done
- no README checkbox unless README behavior/setup is actually affected
- no API/architecture checkbox unless relevant
- no invented risk

### Prompt B — API contract change

> Skapa en issue för att ändra portfolio-endpointens response-format.

Expected:
- contract/dependency section
- risk-based test section
- integration/contract verification
- relevant API/contract documentation in Applicable Definition of Done
- README only if its documented usage/setup is affected
- decision/risk reminder when the change creates one
- develop-sync, review, merge and Done workflow

### Failure examples

- copies the full project DoD into every issue
- always adds README regardless of scope
- adds all test levels automatically
- invents risks or decisions to fill sections

---

## Test 3 — Sprint planning without invented current state

### Prompt

> Hjälp oss planera nästa sprint. Vad bör sprintmålen, milestones och issues vara?

### Expected behavior

The AI should:

1. resolve the current decided goal/plan from registered sources
2. use a verified `Sprintplanering` tab as primary source when present/current
3. keep current facts separate from future proposals
4. propose future sprint goals/milestones/issues as `⭐ AI-förslag`
5. state what a proposal changes, from/to, why, expected effect and tradeoff
6. account for verified dependencies and risks
7. flag missing estimates/capacity rather than inventing numbers
8. use qualitative load balancing only when numeric capacity is unavailable

### Failure examples

- infers the current sprint goal from commits alone
- invents hours, percentages or “normal capacity”
- silently replaces the team's current goal
- proposes duplicate issues without checking existing work

---

## Test 4 — Monday Meeting presentation

### Prompt

> Skapa presentationen till måndagsmötet utifrån dev.

### Expected behavior

The AI should:

- resolve the active sprint using the registered sprint boundary
- use verified sources for current facts
- keep meeting point 1 limited to completed work plus permitted valuable
  unfinished-progress ending in team summaries
- preserve collection-branch merge sections
- use the current vertical priority model for meeting point 9
- use shared project authorities for goals, risks, dependencies/capacity,
  cross-layer analysis and technical debt
- never invent numeric estimates/capacity
- distinguish `🔎 AI-analys` from `⭐ AI-förslag`
- show a concrete useful AI insight when evidence supports one
- when an AI health-check concludes that nothing new was identified, name the
  exact sources/locations actually checked
- show source-backed current goals separately from proposed goal changes
- deliver PDF by default unless another format is explicitly requested

### Failure examples

- returns a four-column point-9 board
- invents a risk/capacity problem just to provide an AI suggestion
- says “inga nya risker” without identifying what was actually checked
- treats a private previous AI conversation as project evidence
- presents a proposed sprint goal as already decided

---

## Pass criteria

A fresh-session test passes when:

- the correct task bundle is effectively reflected in the response
- current state remains source-backed
- analysis/proposals have correct provenance
- no invented project facts appear
- the response teaches the reasoning behind professional practice
- task-specific rules do not duplicate or contradict canonical authorities

Run these after changes to:

- `CONTEXT_REGISTRY.yaml`
- project authorities
- presentation bootstrap/authorities
- source routing
- issue-generation workflow

---

**Status:** ACTIVE TEST SPEC
**Last updated:** 2026-09-18
