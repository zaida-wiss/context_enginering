---
name: slide_detail_spec
description: MANDATORY — content blueprint for Monday Meeting slides ⓪–⑭
metadata:
  type: critical_specification
  version: 2.5
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
3. `READABILITY_HARD_RULES.md`
4. `CARD_COMPONENT_STANDARD.md`
5. `PROVENANCE_AND_AI_LABELING.md`
6. `LAYOUT_OVERFLOW_GUARD.md`

Any visual example in this file is descriptive only.

---

# GLOBAL CONTENT RULES

## Meeting-point headers — atomic identity

Slides ①–⑭ use the complete pattern:

`✏️ [MEETING POINT] [TITLE]`

Examples:
- `✏️ ⑨ Prioritering & scope`
- `✏️ ⑬ Nästa steg`
- continuation: `✏️ ⑨a Prioritering & scope`

Hard rules:
- the pen and meeting-point number are one semantic header identity
- never render `✏️` without the meeting-point number
- never drop the meeting-point number while keeping the pen/title
- continuation slides preserve the same meeting-point identity
- cover ⓪ has no pen/meeting-point header

## Card identity / timestamp content rule

For work/action cards, content must not require legacy labels such as:
- `Utvecklat av`
- `Developed by`
- `Developer:`
- `Assigned to:`

When person/team identity is shown, provide only the verified identity value for the card renderer, e.g. `Zaida · Frontend`.

Timestamp content must be meeting-relevant:
- merged PR cards use merge time
- active/open work does not automatically require PR-created/latest-commit timestamps
- include activity time only when it materially helps explain current status

Visual treatment of these fields is owned by `CARD_COMPONENT_STANDARD.md`.

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
- `👥 ✅ Mötesprotokoll` / approved team input = explicitly stated by team/source
- `🔎 AI-analys` = model-derived interpretation, synthesis or assessment
- `⭐ AI-förslag` = model-derived recommendation, suggested action or suggested question
- `⚠ Källa behöver verifieras` = origin unclear

Analysis and proposals must not share the same AI icon.

## Mandatory planning support

A Monday-meeting deck is not complete if it only reports status. It must also help the team plan the next work period.

For **Frontend, Backend, Native and Cross-team**, derive an actionable planning recommendation from verified project data whenever enough evidence exists.

The recommendation must answer, as far as evidence permits:
1. **Vad bör tas först?** — work that removes a blocker, unlocks another team, protects a deadline, or closes a critical core-flow gap.
2. **Vem kan lämpligen ta det?** — based on verified assignee, branch ownership, recent relevant work, current active work and review load. This is a suggestion, never a reassignment presented as fact.
3. **Vad kan göras parallellt?** — independent work that does not wait for the same dependency or touch the same bottleneck unnecessarily.
4. **Vad bör vänta?** — lower-value or dependency-blocked work that risks increasing WIP before critical flow is stable.
5. **Vilken blocker/risk styr ordningen?** — cite the verified dependency/risk that motivates the suggested order.
6. **Hur påverkar kapacitet/estimering planen?** — use numeric capacity/estimate only when explicitly available in registered sources; otherwise use qualitative load-balancing only.

Use `🔎 AI-analys` for the reasoning and `⭐ AI-förslag` for the recommended action/order.

### Canonical four-team format for meeting point 9

Every physical slide for point 9 MUST use these columns in this exact order:

| Frontend | Backend | Native | Cross-team |
|---|---|---|---|
| Team-specific items | Team-specific items | Team-specific items | Work that genuinely spans or unlocks multiple teams |

Content rules:
- the columns identify team ownership/impact; they are not workflow stages
- do not duplicate an item in both a team column and `Cross-team`
- keep an empty column visible and state the verified empty state
- use continuation slides instead of hiding items or shrinking below readable minima
- `📌` is a workflow-status symbol, not provenance; every item still needs the applicable `✅`, `🔎`, `⭐`, `📅` or `⚠`

### Required team planning format

When there is enough verified data, each team should have a compact planning block using this logical order:

```text
🔎 AI-analys
[Short evidence-based explanation of the blocker/risk/order]

⭐ AI-förslag — planeringsordning
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

Continuation slides preserve the same meeting-point identity and use lowercase
letters. When a point already has a lowercase subsection, append another
lowercase letter: `①a`, `①aa`, `①ab`; `①b`, `①ba`, `①bb`. Never use numeric
suffixes for continuation.
Visual density/pagination is controlled by the visual/overflow authorities.

---

# ⓪ COVER — MANDATORY

Purpose: orient the meeting quickly and state exactly what must be handled with
PL during the current week.

Content:
- meeting date
- `Avanza Team 1`
- active sprint period resolved from the request timestamp
- sprintfokus, grounded in verified project data
- every verified school task/deadline that falls in or materially affects the current week
- PL focus topics grounded in the actual registered schedule/agenda for the current week
- compact snapshot/source footer

`PL-fokus` must match the actual upcoming PL meeting theme/agenda when that source exists. Do not replace a concrete agenda such as `CTO-underlag` with a generic inferred summary such as testing/documentation unless the latter is explicitly part of the registered agenda. AI interpretation may be added separately with provenance.

## Mandatory verified five-question block

For every school task, deadline and PL topic shown on the cover, answer all five
questions from registered `_memory` and presentation-data documentation:

1. **Vad?** — exact task/deliverable or PL topic
2. **När?** — verified date, time and applicable week/sprint
3. **Var?** — verified place, channel or submission platform
4. **Varför?** — documented purpose, learning/project objective or verified consequence
5. **Hur?** — documented submission method, meeting format, required artefact or execution instructions

Each answer retains source-level provenance. Do not derive `Varför` or `Hur`
from the task title alone. Search the registered schedule, milestones, roadmap,
current-sprint context and other registered `_memory`/data documentation.

If one answer remains unavailable after source acquisition, keep the task on the
cover and write the missing field explicitly, for example:
`⚠ Hur kunde inte verifieras`. Never omit a missing field and never replace it
with an AI guess. An AI interpretation may appear only as a separate
`🔎 AI-analys` block, not as the verified five-question answer.

The cover prioritizes current-week PL focus and deadlines over decorative or
generic status text. If multiple school items require more space, reflow the
cover and use a `⓪a` continuation rather than reducing readability or dropping
any of the five answers.

Sprint-period boundary:
- resolve the active sprint containing the request timestamp in `Europe/Stockholm`
- sprint start is Monday 09:00; sprint end is the following Monday 09:00
- display the full scheduled date range on the cover even when the request is made before sprint end
- example: request Monday 21 September at 08:58 → `Sprintperiod 14 september–21 september`
- factual content uses the actual verified data cutoff, never the future 09:00 endpoint

Do not include design-process explanations.

---

# ① SPRINT IN PROGRESS — COMPLETED + STARTED SO FAR

Use the active sprint resolved from the request timestamp. Meeting point 1
covers `SPRINT_START inclusive → DATA_CUTOFF inclusive`, where sprint boundaries
are Monday 09:00 in `Europe/Stockholm`. It may not claim work after the actual
data cutoff merely because the cover displays the full scheduled sprint end.
Six cards is the standard capacity per physical slide, never a total limit.
Create as many lowercase-letter continuations as required and never omit
grounded work.

“Done” means a verified merge during the sprint window to either `develop` or
the owning team's registered collection branch. Project-board `Done` is a
consistency check, not a substitute for merge evidence. Show mismatches instead
of guessing. Deduplicate work promoted through multiple branches.

Mandatory order:
1. `①` — merged to `develop`
2. `①a` — merged to Backend collection branch
3. `①b` — merged to Native collection branch
4. `①c` — started but not yet done
5. `①d` — AI-proposed team summaries for the meeting protocol

Continuation naming:
- Backend: `①a`, `①aa`, `①ab`, ...
- Native: `①b`, `①ba`, `①bb`, ...
- Started work: `①c`, `①ca`, `①cb`, ...
- Team summaries: `①d`, `①da`, `①db`, ...

## ① — Merged to `develop`

Show every PR actually merged to `develop` during the sprint window. Sort
oldest first. Each card contains verified PR number/title, grounded contribution,
contributor, team, merger/reviewer when verified and merge timestamp. Do not
include collection-branch-only merges here.

## ①a — Backend collection-branch merges

Canonical branch: `Java-Development-Environment`. Show every verified merge to
this branch during the sprint window, after all `develop` pages. Use the same
evidence fields as ① where available.

## ①b — Native collection-branch merges

Canonical branch: `C/C++-Native`. Show every verified merge to this branch
during the sprint window, after all Backend pages. Use the same evidence fields
as ① where available.

## ①c — Started but not yet done

Show only unfinished work with verified development/review activity during the
sprint window that had not reached `develop` or its team collection branch by
Monday 09:00. Work may have originated earlier, but it belongs here only when
the source proves that work was actually performed during this period. Do not
include unstarted backlog, dormant older work or completed work. Review work
counts as work when the review activity occurred inside the window.

## ①d — AI proposal for meeting-protocol team summaries

This section always comes last in meeting point 1. Create one meaningful
summary card for each team represented in the sprint evidence. These cards are
not filler.

Each card is ready to copy into the meeting protocol and contains separate
blocks:
- `🔎 AI-analys` — concise synthesis of verified completed and started work
- `⭐ AI-förslag` — polished proposed protocol wording
- relevant verified decisions integrated into the wording with their source
- `👥 ✅ Mötesprotokoll` only after the team has confirmed/copied the wording;
  before confirmation it remains an AI proposal

The proposed protocol wording is approximately 1–10 complete sentences per
team summary. It must:
- explain what the team did to move the project forward, grounded in verified evidence
- include every team member's first name and their verified contribution/work during the relevant sprint period
- include verified review/help/integration work, not only authored code
- integrate verified decisions that affected the team's work, with source/date when available
- distinguish decisions already made from upcoming meeting questions or undecided proposals
- mention a member with no verified contribution neutrally as `Ingen verifierad aktivitet i underlaget för perioden`; never infer performance or absence

Summarize what the team completed, what remained started at cutoff, how the work
advanced the project and any verified decision that materially explains the
outcome. Never invent progress, decisions, contribution or impact. Use `①da`,
`①db` and so on when summaries need more space.

Nothing in meeting point 1 may describe work outside the active sprint start to
data-cutoff interval. Backlog, future plans and work with no verified activity
during the period belong to later meeting points.

The deck remains a forward-working sprint document:
- point 1 establishes verified progress so far in the active sprint
- points 3–5 turn remaining team work into concrete next actions
- point 9 prioritizes the remaining sprint horizon from data cutoff to sprint end
- future scheduled facts use their verified source symbol
- AI-proposed future actions remain marked `⭐ AI-förslag`; they are never presented as completed facts

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

If consequence is AI-derived, mark it `🔎 AI-analys`.
If an action is AI-derived, mark it `⭐ AI-förslag`.

Do not invent progress percentages, days of delay or actions.

---

# ③ FRONTEND

Purpose: define what Frontend should do next.

Include all verified Frontend work relevant to the upcoming period:
- active unfinished work carried forward from ①c
- assigned backlog not yet started
- future work already documented in the board/roadmap
- older open work with no verified recent activity
- open PR/review work
- blockers/dependencies
- verified decisions that govern upcoming Frontend work

Classify every item visibly as `Pågår`, `Backlog`, `Framtida`, `Äldre/inaktiv`,
`📌 Väntar i PR` or another verified state. For `Äldre/inaktiv`, show the last
verified relevant activity when available and use neutral wording; never imply
poor performance. Each work item keeps its source symbol.

When evidence permits, add separate `🔎 AI-analys` and `⭐ AI-förslag` blocks
for order, parallel work, ownership, reactivation, deferral or closure. Do not
invent estimates or assignments. Every card answers `Vad bör hända härnäst?`.

Decisions summarized in ①d may reappear here only when they materially control
future work. Present the verified decision as fact and the resulting next action
as confirmed or `⭐ AI-förslag` according to evidence.

---

# ④ BACKEND

Purpose: define what Backend should do next.

Use the complete forward-looking content logic from ③, including backlog,
future work, older inactive work and governing decisions. Include verified API/contract/integration
status when relevant and make cross-team unlocking work explicit. Keep facts,
analysis and suggestions visually distinct.

---

# ⑤ NATIVE

Purpose: define what Native should do next.

Use the complete forward-looking content logic from ③, including backlog,
future work, older inactive work and governing decisions. Include verified JNA/native integration status
when relevant. Keep independent mock/module work separate from work that waits
for integration. Never invent numeric estimates, capacity or ownership.

---

# ⑥ BLOCKERS & DEPENDENCIES

Purpose: show the critical dependency chains affecting current work.

## ⑥A Dependency graph

Include only critical chains.

Every dependency node MUST contain, in this logical order:
- issue number when one exists
- short title
- **short grounded project-value explanation directly under the title** answering `Vad löser detta i projektet?`
- team
- verified state/status

Project-value explanation rules:
- one short sentence, normally 6–14 words
- grounded in issue/PR/dependency evidence
- never invent technical impact
- if evidence is insufficient, use exactly: `Bidrag till projektet behöver verifieras.`

Canonical content example:

```text
API-kontrakt
Definierar endpoints + payload för integrationen.
🔴 behöver låsas
```

```text
Riktig Java HTTP
Byter mock mot riktig Backend-kommunikation.
⏳ väntar
```

```text
#106 HttpOnly auth
Flyttar auth till säkrare cookie-baserad lösning.
⏳ efter integration
```

Arrows represent verified dependency direction.

If dependency direction is inferred by AI rather than explicitly supported, mark the interpretation `🔎 AI-analys`.

The dependency graph must feed the planning recommendations on ③–⑤, ⑨ and ⑬. If a blocker appears here but does not influence proposed ordering anywhere, re-check the prioritization logic.

## Optional review findings

Show only verified code-review findings relevant to the meeting.

Fields:
- affected PR/work item
- finding category
- verified status
- next confirmed action, or `⭐ AI-förslag` when model-derived

---

# ⑦ RISKS

Purpose: surface relevant current risks and show concrete impact on THIS WEEK's decisions.

**This slide prepares the CTO Feed Forward task** (due Sept 24):
- Show which risks drove trade-offs this week
- Show which mitigations are implemented/tested
- Show which technical choices were altered to reduce risk

Per risk:
- risk statement grounded in evidence
- evidence/source
- consequence if explicitly supported
- **mitigation actually implemented or tested this week**
- owner if confirmed
- status
- **IMPACT ON THIS WEEK:** How did this risk change our planning/priorities/approach?

If risk consequence is model-derived, mark it `🔎 AI-analys`.
If mitigation is model-derived, mark it `⭐ AI-förslag`.

**Critical rule:** Current risks must influence planning suggestions when they materially change sequence, WIP or parallelization. Do not list risks as isolated information if they should change what the team does next.

**For CTO preparation:** Choose risks that show *actual decision impact*, not just theoretical concern.

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

AI may suggest qualitative load-balancing only when based on verified inputs and labeled `⭐ AI-förslag`; reasoning behind that suggestion may be `🔎 AI-analys`.

Required qualitative planning questions when numeric data is missing:
- Is one person already carrying the critical-path task plus reviews?
- Is another person verifiably free for independent work or review/help?
- Can work be split to reduce dependency waiting?
- Would starting another issue increase WIP without unlocking the core flow?

Never translate these questions into invented hours, percentages or velocity.

---

# ⑨ PRIORITIZATION & SCOPE

Purpose: produce a usable team plan, not only a generic priority statement.

Every physical slide belonging to meeting point ⑨ uses the canonical four-team columns:
`Frontend | Backend | Native | Cross-team`.

Each physical slide within meeting point ⑨ uses a fixed `1×4` structure:
`Frontend | Backend | Native | Cross-team`. Cards and labeled text blocks stack
vertically inside their owning team column.

The number of cards/text blocks is content-driven. If the content does not fit
accessibly, continue as `⑨a`, `⑨b`, `⑨c`, `⑨d`, `⑨e` and so on. Never change
the fixed four-column structure, and never clip or hide content.

### Open pull requests

Every verified open PR contains the dynamic format `📌 #[PR_NUMBER]`; the
number uses the owning team's canonical accessible color. It also contains a grounded contribution
sentence directly below, verified author/owner, review state, confirmed next
action when documented and applicable provenance. `📌` never replaces the
source symbol. Do not combine unrelated PRs.

### Remaining assigned issues, order and dependencies

Include every remaining assigned issue with verified number/title,
contribution, assignee and status. Give it one order marker: `1. Först`,
`2. Parallellt`, `3. Därefter` or `Vänta`. Show dependencies as visible directed
relations headed `🔗 Beroende`, such as `#105 → #108`, with a short reason and
source. Inferred or AI-interpreted dependencies use both labels:
`🔗 Beroende · 🔎 AI-analys`.

Every issue number uses its owning team's canonical accessible color. The
visible team column remains the non-color ownership cue required by WCAG.

### AI work-allocation analysis

Each recommendation includes `🔎 AI-analys`, a separate `⭐ AI-förslag` naming
the person and task, and a concise motivation. Consider verified estimates,
capacity, workload/review load, adjacent component work, dependencies,
continuity with prior verified work, merge-conflict risk and useful pairing.
If numeric data is absent, state `Numeriskt estimat/kapacitet saknas`.

### Suggested issues to create

Each suggestion includes `⭐ AI-förslag — skapa issue`, a short title, the
grounded gap/goal, contribution, team column, dependency, supported owner
suggestion when possible and concise acceptance criteria. Check existing issues
and PRs first; do not suggest duplicates or filler.

Verified section may include:
- team-confirmed order
- sprint scope
- confirmed dependency sequence
- verified estimates/capacity where available

### Mandatory AI planning synthesis

Unless the team already has a complete confirmed sequence, include an AI-labeled recommendation synthesized from slides ③–⑧.

Use `🔎 AI-analys` for why the ordering is sensible and `⭐ AI-förslag` for the proposed order/action.

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
- `⭐ AI-förslag` if model-derived
- `🔎 AI-analys` when explanatory reasoning is model-derived

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
AI feasibility analysis must be labeled `🔎 AI-analys`.
AI-generated goals/recommendations must use `⭐ AI-förslag`.

---

# ⑫ SPRINT PLAN

Purpose: show what is actually scheduled, how it relates to capacity/risk, and why we prioritized this way.

**Reality check against risk:** Does this plan remain realistic given the risks/constraints identified in ⑦?
If a risk has changed sequencing or WIP limits, that decision must be visible here.

Every day card must distinguish source blocks and, where relevant, show risk-driven choices.

Canonical content order:

```text
[Day + date]

📅 Schemafakta
[Only information explicitly present in registered school schedule]

👥 ✅ Mötesprotokoll
[Only if explicitly documented]

🔎 AI-analys
[Optional interpretation of verified project data]

⭐ AI-förslag
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

Never blend schedule facts, AI analysis and AI suggestions into one unlabeled paragraph.

---

# ⑬ NEXT STEPS

Purpose: make the next actions clear while preserving provenance and showing risk-driven prioritization.

**Prioritization rule:** Actions that reduce high-risk or high-consequence threats come first.
Reference the risks from ⑦ that these actions address.

Evidence priority:
1. explicit risk-mitigating actions from meeting protocol
2. explicit approved/prefilled team actions with risk context
3. AI-derived suggestions prioritized by risk impact and verified project data
4. Actions deferred due to risk constraints should be noted as such

Every action card MUST contain its provenance label.

Every action card MUST also contain a grounded pedagogical explanation directly under the action title that answers:
1. what the action concerns
2. what it contributes/unlocks in the project or why it matters

Verified action example source label:
- `👥 ✅ Mötesprotokoll`

AI suggestion source label:
- `⭐ AI-förslag`

AI analytical explanation when useful:
- `🔎 AI-analys`

Fields when available:
- concise action
- pedagogical/project-value explanation
- owner if confirmed
- deadline/timeframe if confirmed
- verification condition if confirmed

When verified dependencies exist, ⑬ must reflect the dependency-aware sequence from ⑨:
- **Först**
- **Parallellt**
- **Därefter / Vänta**
- short `Varför` grounded in blocker/dependency/deadline/core-flow evidence

AI-derived ordering uses `🔎 AI-analys` for reasoning and `⭐ AI-förslag — planeringsordning` for the proposed sequence.

AI next steps should be consistent with the team plan from ⑨ and should name the concrete issue/work item when verified, rather than only saying `fortsätt arbetet`.

AI must not invent owner/deadline merely to make the action look complete.

---

# ⑭ QUESTIONS TO PL

Purpose: collect direct questions that PL can answer during the meeting.

Every question is its own card and must include provenance.

Question sources:
- `✅ Från mötesprotokoll` / `✅ Teamfråga`
- `⭐ AI-förslag till PL` for an AI-generated question
- `🔎 AI-analys av beroenden` for the reasoning/context explaining why a question matters

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
meeting_point_number_missing_count == 0
pen_without_meeting_point_number_count == 0
legacy_developed_by_label_count == 0
unnecessary_activity_timestamp_count == 0
unverified_ids_invented_count == 0
unverified_deadlines_invented_count == 0
unverified_owners_invented_count == 0
unverified_numeric_estimates_invented_count == 0
ai_analysis_without_magnifying_glass_count == 0
ai_proposal_without_star_count == 0
unverified_item_presented_as_confirmed_count == 0
missing_dependency_project_value_microcopy_count == 0
next_step_card_missing_project_value_microcopy_count == 0
team_planning_recommendation_present_when_evidence_allows == true
blockers_and_risks_reflected_in_priority_order == true
numeric_capacity_or_estimate_has_verified_source == true
collection_branch_items_promoted_onward_remaining_count == 0
active_items_already_merged_to_collection_branch_count == 0
```

---

**Status:** PRODUCTION
**Version:** 2.4
**Last updated:** 2026-09-17
