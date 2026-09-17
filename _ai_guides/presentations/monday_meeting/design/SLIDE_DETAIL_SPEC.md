---
name: slide_detail_spec
description: MANDATORY — content blueprint for Monday Meeting slides ⓪–⑭
metadata:
  type: critical_specification
  version: 2.2
---

# 📊 SLIDE DETAIL SPECIFICATION — CONTENT ONLY

This file owns **what each slide contains**.

It does NOT own:
- font sizes
- colors
- card geometry
- borders
- padding
- grid density
- timestamp styling
- provenance styling

Those are owned by the higher authorities:
1. `ACCESSIBILITY_NEURODIVERSITY.md`
2. `VISUAL_DESIGN_MANDATORY.md`
3. `CARD_COMPONENT_STANDARD.md`
4. `PROVENANCE_AND_AI_LABELING.md`
5. `LAYOUT_OVERFLOW_GUARD.md`

Any visual example in this file is descriptive only.

---

# GLOBAL CONTENT RULES

## Meeting-point headers

Slides ①–⑭ use:

`✏️[MEETING POINT] [TITLE]`

Cover ⓪ has no pen/meeting-point header.

## No guessing

Never invent:
- issue/PR IDs
- branches
- assignees
- reviewers
- merge identities
- timestamps
- deadlines
- schedule purposes
- capacity/hours
- numeric estimates

## Provenance

Every inferred recommendation/analysis follows `PROVENANCE_AND_AI_LABELING.md`.

Especially:
- `📅 Schemafakta` = explicitly in registered school schedule
- `✅ Mötesprotokoll` / approved team input = explicitly stated by team/source
- `? AI-förslag` / `? AI-analys` = model-derived
- `⚠ Källa behöver verifieras` = origin unclear

## Mandatory planning support

A Monday-meeting deck is not complete if it only reports status. It must also help the team plan the next work period.

For **Frontend, Backend and Native**, derive an actionable planning recommendation from verified project data whenever enough evidence exists.

The recommendation must answer, as far as evidence permits:
1. **Vad bör tas först?** — work that removes a blocker, unlocks another team, protects a deadline, or closes a critical core-flow gap.
2. **Vem kan lämpligen ta det?** — based on verified assignee, branch ownership, recent relevant work, current active work and review load. This is a suggestion, never a reassignment presented as fact.
3. **Vad kan göras parallellt?** — independent work that does not wait for the same dependency or touch the same bottleneck unnecessarily.
4. **Vad bör vänta?** — lower-value or dependency-blocked work that risks increasing WIP before critical flow is stable.
5. **Vilken blocker/risk styr ordningen?** — cite the verified dependency/risk that motivates the suggested order.
6. **Hur påverkar kapacitet/estimering planen?** — use numeric capacity/estimate only when explicitly available in registered sources; otherwise use qualitative load-balancing only.

The recommendation must be visibly labeled `? AI-förslag` or `? AI-analys`.

### Required team planning format

When there is enough verified data, each team should have a compact planning block using this logical order:

```text
? AI-förslag — planeringsordning
1. Först: [issue/work item] — [suggested person if supportable]
   Varför: [blocker/dependency/deadline/core-flow reason]
2. Parallellt: [issue/work item] — [suggested person if supportable]
   Varför: [independent path / load balancing]
3. Därefter / vänta: [issue/work item]
   Varför: [depends on earlier item / lower priority]
Kapacitet/estimat: [verified value OR qualitative note that numeric data is missing]
```

Do not force a person recommendation when evidence is weak. In that case use wording such as:
- `Lämplig ägare behöver bekräftas i teamet`
- `Tillgänglig teammedlem efter review/merge`

Do not infer skill, performance or availability from absence of GitHub activity.

## Conditional slides

A conditional slide may be omitted only when its dataset is verified empty or its condition is not met.
Record the reason in audit.

## Continuation slides

Continuation slides preserve the same meeting-point identity, e.g. `①A-2`, `③-2`, `⑭-2`.
Visual density/pagination is controlled by the visual/overflow authorities.

---

# ⓪ COVER — MANDATORY

Purpose: orient the meeting quickly.

Content:
- meeting date
- `Avanza Team 1`
- reporting period
- sprintfokus, grounded in verified project data
- critical verified deadline/milestone if available
- PL focus topics grounded in the actual registered schedule/agenda for the coming week; otherwise AI-derived focus must be labeled
- compact snapshot/source footer

`PL-fokus` must match the actual upcoming PL meeting theme/agenda when that source exists. Do not replace a concrete agenda such as `CTO-underlag` with a generic inferred summary such as testing/documentation unless the latter is explicitly part of the registered agenda. AI interpretation may be added separately with provenance.

Do not include design-process explanations.

---

# ① COMPLETED + CURRENT WORK OVERVIEW

## ①A — Merged to `develop`

Purpose: show all PRs actually merged to `develop` during the reporting period.

Content per merge card:
- PR number + title
- short grounded contribution explanation
- actual code contributor/developer attribution according to project evidence model
- team
- merger identity when verified
- actual approving reviewer(s) when verified
- merge timestamp

Sort: chronological, oldest first.

Do not include collection-branch-only merges here.

Unknown reviewer/merger must be explicitly marked unknown/unverified.

## Collection-branch lifecycle — applies equally to Backend and Native

The Backend and Native collection slides are **state views**, not merely reporting-period event logs.

Canonical collection branches:
- Backend: `Java-Development-Environment`
- Native: `C/C++-Native`

A work item belongs on its collection-branch slide when verified work has been merged into that team's collection branch **and the same work has not yet been promoted to the final delivery branch**.

Lifecycle:

```text
assigned / started, not merged to collection branch
  → active work (①D/①E)

merged to team collection branch, not yet promoted
  → collection-branch merged (①B/①C)

promoted onward to final delivery branch
  → remove from ①B/①C; final delivery is represented on the final-delivery merge view
```

Do not keep the same work simultaneously as active work and collection-branch merged work.
Do not keep collection-branch items after promotion onward.
Deduplicate by issue/PR/work identity, not merely by merge-commit count.

## ①B — Backend collection-branch merges

Canonical branch: `Java-Development-Environment`.

Purpose: show all verified Backend work currently accumulated in the Backend collection branch and not yet promoted onward to the final delivery branch.

Include work even if the merge into the collection branch occurred before the current reporting period, as long as it still remains unpromoted.

Fields: same evidence fields as ①A where available, plus linked issue/work identity when verified.
Sort: chronological by collection-branch merge time.

If verified count = 0, omit or show empty-state according to audit decision; record reason.

## ①C — Native collection-branch merges

Canonical branch: `C/C++-Native`.

Purpose: show all verified Native work currently accumulated in the Native collection branch and not yet promoted onward to the final delivery branch.

Include work even if the merge into the collection branch occurred before the current reporting period, as long as it still remains unpromoted.

Fields: same evidence fields as ①A where available, plus linked issue/work identity when verified.
Sort: chronological by collection-branch merge time.

If verified count = 0, record omission/empty-state reason.

## ①D — Active team work

Purpose: show verified assigned/started work owned primarily by one team that has **not yet been merged to that team's collection branch or final delivery branch**.

Include:
- issue number + title
- contribution/intended contribution explanation grounded in issue/PR evidence
- assignee/owner
- team
- matching active branch when verified
- open PR when verified
- latest relevant activity timestamp
- blocker/dependency when verified

`På gång` means assigned and/or started work that is still pre-merge for its team's collection branch. A work item stops being `På gång` as soon as it is verified merged to the applicable collection branch.

Do not classify an old open issue as actively worked merely because it remains open.
Use `ACTIVE_WORK_DETECTION_MODEL.md`.

### Team member with no verified active work

Use neutral wording:

`[Name] — Ny issue eller tillgänglig för hjälp i [teamet]`

But review work counts as work. If the person is actively reviewing, show review activity rather than availability.

This is capacity visibility, not performance assessment.

## ①E — Assigned/backlog + cross-team work

Purpose:
- show assigned issues that are not yet verified as active
- show verified cross-team active work
- make upcoming work/capacity visible

Assigned/backlog fields:
- issue number + title
- assignee
- board/status if verified
- dependency/blocker if verified
- whether matching active branch is verified
- last issue activity timestamp when relevant

Cross-team fields:
- issue number + title
- involved teams
- owner(s)
- branch/PR if verified
- latest verified activity
- dependency/blocker if verified

Every open assigned issue must appear on ①D, ①E, ①B/①C when already merged to a collection branch, or in explicit audit exclusion.

## ①F — Decisions since last meeting

Two content types may appear:

### Verified decisions
Source: formal decision log / meeting protocol / registered decision source.

Fields:
- decision title
- concise decision statement
- documented date/source
- affected area/team when relevant

### Decision candidates
These are AI suggestions and MUST use `? AI-förslag`/`? AI-analys` provenance.

Fields:
- question-form candidate
- verified evidence suggesting the practice/choice exists
- why documenting it would matter

Never state a candidate as a decision already made.

Omit ①F if both datasets are verified empty.

---

# ② CURRENT STATE & DEADLINES

Purpose: summarize the most important verified current state, deadlines and risks.

For each priority item include when evidence exists:
- what the milestone/deadline is
- exact verified deadline
- current verified status
- why it matters, if source explicitly supports the consequence
- verified blocker/risk
- confirmed action if documented

If consequence/action is AI-derived rather than explicitly sourced, mark that block `? AI-analys` or `? AI-förslag`.

Do not invent progress percentages, days of delay or actions.

---

# ③ FRONTEND

Purpose: detailed Frontend status **and actionable next-work planning** for the current sprint/period.

Include relevant cards for:
- verified active issues
- assigned upcoming issues
- open PR/review work
- blockers/dependencies
- people with no verified active/review work using approved availability wording

Each work-item card includes the verified fields available from issue/PR/branch data.

### Mandatory Frontend planning recommendation

When enough evidence exists, include a `? AI-förslag — planeringsordning` block that:
- prioritizes pending review/merge and blocker-removing work before starting unnecessary new WIP
- identifies a suggested person only when supported by assignee/branch/recent-work evidence
- identifies parallel independent work for another available person when possible
- explicitly states what should wait if it depends on Backend/API/integration or another unfinished item
- incorporates verified tests, integration readiness, deadline and risk information
- uses verified numeric estimate/capacity only when available; otherwise says that numeric capacity/estimate is not verified

---

# ④ BACKEND

Purpose: detailed Backend status **and actionable dependency-aware planning**.

Use the same content logic as ③.

May additionally include verified API-contract/integration status when relevant:
- endpoint/contract item
- state
- what is blocked by it, when verified
- next confirmed action or AI-labeled suggestion

### Mandatory Backend planning recommendation

When enough evidence exists, include a `? AI-förslag — planeringsordning` block that:
- puts work that unlocks Frontend/Native or the critical end-to-end flow before isolated cleanup
- considers API contract/endpoints, auth/security chain, JNA bridge and integration dependencies when present
- suggests parallel ownership only when tasks can proceed independently without creating avoidable merge/code-area contention
- calls out work that should wait because its prerequisite is not ready
- relates the order to verified deadline/risk/blocker evidence
- uses numeric capacity/estimation only when verified

---

# ⑤ NATIVE

Purpose: detailed Native status **and actionable dependency-aware planning**.

Use the same content logic as ③.

May additionally include verified JNA/native integration status:
- dependency
- current state
- blocked dependent work
- confirmed action or AI-labeled suggestion

### Mandatory Native planning recommendation

When enough evidence exists, include a `? AI-förslag — planeringsordning` block that:
- prioritizes interface/JNA/contract work that enables integration before expanding non-critical module scope when the dependency evidence supports that order
- proposes a sensible split between independent module work (for example backtest vs FX/risk) when verified assignments and dependencies permit it
- identifies what can continue with mocks while waiting and what truly depends on integration
- includes verified risk/deadline/capacity/estimate information and never invents numeric values

---

# ⑥ BLOCKERS & DEPENDENCIES

Purpose: show the critical dependency chains affecting current work.

## ⑥A Dependency graph

Include only critical chains.

Each node:
- issue number
- short title
- team
- verified state

Arrows represent verified dependency direction.

If dependency direction is inferred by AI rather than explicitly supported, mark the analysis accordingly.

The dependency graph must feed the planning recommendations on ③–⑤ and ⑨. If a blocker appears here but does not influence proposed ordering anywhere, re-check the prioritization logic.

## Optional review findings

Show only verified code-review findings relevant to the meeting.

Fields:
- affected PR/work item
- finding category
- verified status
- next confirmed action, or AI-labeled suggestion

---

# ⑦ RISKS

Purpose: surface relevant current risks, not historical noise.

Per risk:
- risk statement grounded in evidence
- evidence/source
- consequence if explicitly supported
- mitigation if confirmed
- owner if confirmed
- status

If risk consequence or mitigation is model-derived, mark the relevant block `? AI-analys` / `? AI-förslag`.

Current risks must influence planning suggestions when they materially change sequence, WIP or parallelization. Do not list risks as isolated information if they should change what the team does next.

Do not invent probability, numeric impact or delay duration.

---

# ⑧ CAPACITY & ESTIMATION

Purpose: show verified capacity/planning information and connect it to workload decisions.

PRE-MEETING:
- do not estimate hours
- show documented availability constraints if registered sources contain them
- generalize private/health reasons to `limited availability`
- if no relevant verified capacity data exists, use the approved placeholder/omission behavior from `SYSTEM_CONTRACT.yaml`
- still provide qualitative AI load-balancing when enough verified work/dependency evidence exists

POST-MEETING:
- capacity values must come from confirmed meeting/team planning data
- if required values are missing, STOP according to system contract

AI may suggest qualitative load-balancing only when based on verified inputs and labeled `? AI-förslag`.

Required qualitative planning questions when numeric data is missing:
- Is one person already carrying the critical-path task plus reviews?
- Is another person verifiably free for independent work or review/help?
- Can work be split to reduce dependency waiting?
- Would starting another issue increase WIP without unlocking the core flow?

Never translate these questions into invented hours, percentages or velocity.

---

# ⑨ PRIORITIZATION & SCOPE

Purpose: produce a usable team plan, not only a generic priority statement.

Verified section may include:
- team-confirmed order
- sprint scope
- confirmed dependency sequence
- verified estimates/capacity where available

### Mandatory AI planning synthesis

Unless the team already has a complete confirmed sequence, include an AI-labeled recommendation synthesized from slides ③–⑧.

For each team, include where evidence permits:
- **1 — Först:** highest-leverage blocker/deadline/core-flow item
- **2 — Parallellt:** independent work/review/help path
- **3 — Därefter:** follow-up that becomes useful after item 1
- **Vänta:** work that should not increase WIP yet
- **Föreslagen person:** only if supported by verified ownership/activity; otherwise mark owner to confirm
- **Styrande blocker/risk:** why the order is suggested
- **Estimat/kapacitet:** verified value if available, otherwise explicit `ej verifierat` / qualitative load note

AI-derived section may additionally include:
- suggested scope trade-off
- suggested pairing/review support
- suggested handoff between teams

Every AI-derived item uses `? AI-förslag` or `? AI-analys`.

Do not invent numeric estimates.

---

# ⑩ TECHNICAL DECISIONS

Purpose: distinguish decisions already made from decisions needing discussion.

Verified decision fields:
- decision
- owner/decision-maker when documented
- date/deadline when documented
- affected teams/areas when documented
- source

Decision candidate fields:
- question
- evidence
- impact
- `? AI-förslag` if model-derived

Never convert a code pattern into a confirmed decision without source evidence.

---

# ⑪ SPRINT GOALS

Purpose: show the sprint/week goals.

Priority order:
1. goals explicitly stated in planning/meeting source
2. registered milestone/source goals
3. AI-derived suggested synthesis only when useful and clearly labeled

Each goal should identify:
- goal
- why it matters if source-grounded or separately AI-labeled
- owner if confirmed
- deadline if confirmed

Goals should be consistent with the dependency-aware ordering on ⑨. Do not set a goal that requires blocked work while ignoring its prerequisite.

Do not state feasibility as fact unless based on verified capacity data.
AI feasibility analysis must be labeled `? AI-analys`.

---

# ⑫ SPRINT PLAN

Purpose: show what is actually scheduled and, separately, proposed project focus around it.

Every day card must distinguish source blocks.

Canonical content order:

```text
[Day + date]

📅 Schemafakta
[Only information explicitly present in registered school schedule]

✅ Mötes-/teamfakta
[Only if explicitly documented]

? AI-förslag
[Optional planning suggestion inferred from project data]
```

Examples of `📅 Schemafakta` only when explicitly present in schedule:
- project-work time
- PL meeting time
- named school activity
- location/channel

Examples that are NOT schedule facts unless explicitly stated:
- `Lås scope, kapacitet och ägare`
- `Få svar om CTO-underlaget`
- `Stäng öppna frågetecken`
- suggested priorities for the day

When a day contains project work, the AI suggestion should, where useful, reference the dependency-aware plan from ⑨ instead of using generic phrases such as `jobba vidare`.

Never blend schedule facts and AI suggestions into one unlabeled paragraph.

---

# ⑬ NEXT STEPS

Purpose: make the next actions clear while preserving provenance.

Evidence priority:
1. explicit actions from meeting protocol
2. explicit approved/prefilled team actions
3. AI-derived suggestions based on verified project data

Every action card MUST contain its provenance label.

Verified action example source label:
- `✅ Mötesprotokoll`

AI suggestion source label:
- `? AI-förslag`

Fields when available:
- concise action
- owner if confirmed
- deadline/timeframe if confirmed
- verification condition if confirmed

AI next steps should be consistent with the team plan from ⑨ and should name the concrete issue/work item when verified, rather than only saying `fortsätt arbetet`.

AI must not invent owner/deadline merely to make the action look complete.

---

# ⑭ QUESTIONS TO PL

Purpose: collect direct questions that PL can answer during the meeting.

Every question is its own card and must include provenance.

Question sources:
- `✅ Från mötesprotokoll` / `✅ Teamfråga`
- `? AI-förslag till PL`
- `? AI-analys av beroenden`

Each card contains:
- question
- category when useful (scope, priority, dependency, process, etc.)
- concrete impact/context
- provenance

Urgency grouping may be used:
- `IDAG-SVAR BEHÖVS`
- `NICE-TO-HAVE`

PL questions should be generated from unresolved items that materially affect the plan: scope, deadline interpretation, dependency ownership, integration expectations, acceptance criteria or missing information needed to estimate/plan.

Urgency does not replace provenance.

Do not include rhetorical questions or questions without a concrete reason for asking.

---

# FOOTERS / SOURCES

Slide-level footer may summarize the major registered sources used.

However, footer source text NEVER replaces item-level provenance when a slide mixes:
- source facts
- team-confirmed items
- AI-derived analysis/suggestions

---

# CONTENT COMPLETENESS

Before rendering verify:

```text
all_required_work_items_accounted_for == true
all_conditional_omissions_audited == true
unverified_ids_invented_count == 0
unverified_deadlines_invented_count == 0
unverified_owners_invented_count == 0
unverified_numeric_estimates_invented_count == 0
ai_generated_item_without_question_icon_count == 0
unverified_item_presented_as_confirmed_count == 0
team_planning_recommendation_present_when_evidence_allows == true
blockers_and_risks_reflected_in_priority_order == true
numeric_capacity_or_estimate_has_verified_source == true
collection_branch_items_promoted_onward_remaining_count == 0
active_items_already_merged_to_collection_branch_count == 0
```

---

**Status:** PRODUCTION
**Version:** 2.2
**Last updated:** 2026-09-17