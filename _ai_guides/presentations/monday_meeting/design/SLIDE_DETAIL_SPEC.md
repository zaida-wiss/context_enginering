---
name: slide_detail_spec
description: MANDATORY — content blueprint for Monday Meeting slides ⓪–⑭
metadata:
  type: critical_specification
  version: 2.0
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
- team decisions

## Provenance

Every inferred recommendation/analysis follows `PROVENANCE_AND_AI_LABELING.md`.

Especially:
- `📅 Schemafakta` = explicitly in registered school schedule
- `✅ Mötesprotokoll` / approved team input = explicitly stated by team/source
- `? AI-förslag` / `? AI-analys` = model-derived
- `⚠ Källa behöver verifieras` = origin unclear

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
- PL focus topics if grounded in registered source; otherwise AI-derived focus must be labeled
- compact snapshot/source footer

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

---

## ①B — Backend collection-branch merges

Canonical branch: `Java-Development-Environment`.

Purpose: show verified PRs merged to the Backend collection branch during the reporting period that are not already represented as final `develop` delivery in a way that would double-count the same delivery.

Fields: same evidence fields as ①A.

Sort: chronological.

If verified count = 0, omit or show empty-state according to audit decision; record reason.

---

## ①C — Native collection-branch merges

Canonical branch: `C/C++-Native`.

Purpose: show verified PRs merged to the Native collection branch during the reporting period without double-counting final delivery.

Fields: same evidence fields as ①A.

Sort: chronological.

If verified count = 0, record omission/empty-state reason.

---

## ①D — Active team work

Purpose: show verified active work owned primarily by one team.

Include:
- issue number + title
- contribution/intended contribution explanation grounded in issue/PR evidence
- assignee/owner
- team
- matching active branch when verified
- open PR when verified
- latest relevant activity timestamp
- blocker/dependency when verified

Do not classify an old open issue as actively worked merely because it remains open.
Use `ACTIVE_WORK_DETECTION_MODEL.md`.

### Team member with no verified active work

Use neutral wording:

`[Name] — Ny issue eller tillgänglig för hjälp i [teamet]`

But review work counts as work. If the person is actively reviewing, show review activity rather than availability.

This is capacity visibility, not performance assessment.

---

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

Every open assigned issue must appear on ①D, ①E or in explicit audit exclusion.

---

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

Purpose: detailed Frontend status for the current sprint/period.

Include relevant cards for:
- verified active issues
- assigned upcoming issues
- open PR/review work
- blockers/dependencies
- people with no verified active/review work using approved availability wording

Each work-item card includes the verified fields available from issue/PR/branch data.

Optional Frontend operational suggestions may be shown, but AI-derived actions must be labeled `? AI-förslag`.

---

# ④ BACKEND

Purpose: detailed Backend status.

Use the same content logic as ③.

May additionally include verified API-contract/integration status when relevant:
- endpoint/contract item
- state
- what is blocked by it, when verified
- next confirmed action or AI-labeled suggestion

---

# ⑤ NATIVE

Purpose: detailed Native status.

Use the same content logic as ③.

May additionally include verified JNA/native integration status:
- dependency
- current state
- blocked dependent work
- confirmed action or AI-labeled suggestion

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

Do not invent probability, numeric impact or delay duration.

---

# ⑧ CAPACITY & ESTIMATION

Purpose: show verified capacity/planning information only.

PRE-MEETING:
- do not estimate hours
- show documented availability constraints if registered sources contain them
- generalize private/health reasons to `limited availability`
- if no relevant verified capacity data exists, use the approved placeholder/omission behavior from `SYSTEM_CONTRACT.yaml`

POST-MEETING:
- capacity values must come from confirmed meeting/team planning data
- if required values are missing, STOP according to system contract

AI may suggest qualitative load-balancing only when based on verified inputs and labeled `? AI-förslag`.

---

# ⑨ PRIORITIZATION & SCOPE

Purpose: show confirmed priority/scope where it exists and clearly separated AI prioritization where it does not.

Verified section may include:
- team-confirmed order
- sprint scope
- confirmed dependency sequence

AI-derived section may include:
- suggested order based on verified dependencies
- suggested scope trade-off
- suggested parallel work

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

Do not state feasibility as fact unless based on verified capacity data.
AI feasibility analysis must be labeled `? AI-analys`.

---

# ⑫ SPRINT PLAN

Purpose: show what is actually scheduled and, separately, any proposed project focus around it.

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
ai_generated_item_without_question_icon_count == 0
unverified_item_presented_as_confirmed_count == 0
```

---

**Status:** PRODUCTION
**Version:** 2.0
**Last updated:** 2026-09-17
