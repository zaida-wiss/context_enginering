---
name: slide_detail_spec
description: MANDATORY — content blueprint for Monday Meeting slides ⓪–⑭
metadata:
  type: critical_specification
  version: 3.3
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

## Meeting-point headers — fixed meeting-point title + page subtitle

Slides 1–14 always preserve the **official meeting-point title** as the primary
slide heading. A page-specific description is a separate subtitle and must
never replace the meeting-point heading.

Canonical two-level structure:

```text
✏️ [MEETING POINT NUMBER]. [OFFICIAL MEETING-POINT TITLE]
[PAGE-SPECIFIC SUBTITLE]
```

Example for meeting point 1:

```text
✏️ 1. Avklarat sedan förra mötet
{PRIMARY_INTEGRATION_SUBTITLE}
```

Another page in the same meeting point:

```text
✏️ 1. Avklarat sedan förra mötet
{COLLECTION_BRANCH_SUBTITLE}
```

Hard rules:
- the meeting-point number and its official title are mandatory on every slide belonging to that meeting point
- the page-specific content label is always subordinate: subtitle/section label, never the primary heading
- never replace `Avklarat sedan förra mötet` with `{PRIMARY_INTEGRATION_SUBTITLE}`, `Påbörjat arbete`, `Teamsammanfattning` or any other page content label
- continuation/subsection markers may be shown as secondary navigation, but they do not replace the official meeting-point number/title
- every continuation slide repeats the full official meeting-point heading
- the pen and meeting-point number remain one semantic header identity
- never render `✏️` without the meeting-point number
- cover ⓪ has no pen/meeting-point header

## Card identity / timestamp content rule

For work/action cards, content must not require legacy labels such as:
- `Utvecklat av`
- `Developed by`
- `Developer:`
- `Assigned to:`

When person/team identity is shown, provide separate verified renderer fields,
for example `person: {PERSON}` and `team: {TEAM}`.

Rendering rule:
- dedicated team slide whose primary header names the team: show `{PERSON}` only;
  do not repeat `Frontend` inside the card
- mixed-team slide: show the explicit non-color cue `{PERSON} · {TEAM}`
- the narrow left team accent remains supplementary in both cases

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

### Four-perspective planning coverage

Planning analysis must consider these perspectives when relevant:

- Frontend
- Backend
- Native/System
- Cross-team

This is a **coverage requirement**, not a page-layout requirement.

Meeting point 9 renders vertically stacked execution groups as an explicit
exception to the general card/grid slide composition. Team/layer ownership may
be shown inside those groups when it helps the meeting. The slide must not use
a four-column or 2×2 execution-group layout.

Do not duplicate the same work item under both a team/layer label and
`Cross-team`. Use `Cross-team` only when the work genuinely spans or unlocks
multiple teams.

`📌` is a workflow-status symbol, not provenance; every item still retains the
applicable `✅`, `🔎`, `⭐`, `📅` or `⚠` source/provenance meaning.

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

## School-task priority indicator

School/submission task cards may show priority with a **symbol + text + color**.
Color is supportive only and never carries the meaning alone.

Canonical levels:
- `● PRIORITET 1` — critical / nearest consequential deadline — red accent
- `● PRIORITET 2` — important upcoming task/checkpoint — orange accent
- `● PRIORITET 3` — lower urgency / later school task — green accent

Use priority only when it is grounded in an explicit deadline, consequence or
course sequence. If priority is model-derived, label the reasoning `🔎 AI-analys`.
Do not use this school-task priority scale on ordinary issue/PR cards.


`PL-fokus` must match the actual upcoming PL meeting theme/agenda when that source exists. Do not replace a concrete agenda such as `CTO-underlag` with a generic inferred summary such as testing/documentation unless the latter is explicitly part of the registered agenda. AI interpretation may be added separately with provenance.

### PL meeting card — merge focus into the meeting card

When the cover contains a scheduled `Teamavstämning med PL` or equivalent PL meeting, do **not** create a separate duplicated `PL-fokus` card next to it. The PL focus belongs inside the PL meeting card itself.

The PL meeting card uses exactly three information meanings:
- `🎯 Vad/fokus` — what the meeting must focus on, including the verified PL agenda/topic
- `🕒 När` — verified meeting date and time
- `💡 Varför` — documented purpose or verified reason the meeting matters now

Do **not** show `Var` or `Hur` on the PL meeting card. Location/format such as Slack Huddle may remain in quiet source metadata only when useful, but it is not part of the primary card content.

This three-part PL structure is intentionally shorter than the school-assignment/deadline structure below.

## Mandatory verified school-task information block

This five-part structure applies specifically to **school assignments, submission
tasks and school deadlines**. It is not a generic card template for ordinary
project issues, PRs or the PL meeting card.

**Exception:** scheduled PL/teamavstämning topics use the shorter three-part
`🎯 Vad/fokus → 🕒 När → 💡 Varför` structure defined above.

Do not render the repeated words `VAD`, `NÄR`, `VAR`, `VARFÖR`, `HUR`
as labels on every card. Use the canonical icon grammar instead:

- `🎯` = what the school/submission task is
- `🕒` = when it happens / deadline
- `📍` = where it takes place or is submitted
- `💡` = why it exists / documented purpose or consequence
- `🛠` = how it is carried out or submitted

Canonical visual order:
`🎯 → 🕒 → 📍 → 💡 → 🛠`

For every school task, submission task and deadline shown on the cover, all five
meanings must still be answered from registered `_memory` and presentation-data
documentation:

1. `🎯` exact task/deliverable or PL/course topic
2. `🕒` verified date, time and applicable week/sprint
3. `📍` verified place, channel or submission platform
4. `💡` documented purpose, learning/project objective or verified consequence
5. `🛠` documented submission method, meeting format, required artefact or execution instructions

Each answer retains source-level provenance. Do not derive `Varför` or `Hur`
from the task title alone. Search the registered schedule, milestones, roadmap,
current-sprint context and other registered `_memory`/data documentation.

If one answer remains unavailable after source acquisition, keep the task on the
cover and retain the corresponding icon with an explicit warning, for example:
`🛠 ⚠ kunde inte verifieras`. Never omit a missing field and never replace it
with an AI guess. An AI interpretation may appear only as a separate
`🔎 AI-analys` block, not as the verified five-question answer.

The cover prioritizes current-week PL focus and deadlines over decorative or
generic status text. If multiple school items require more space, reflow the
cover and use a `⓪a` continuation rather than reducing readability or dropping
any of the five answers.

Sprint-period boundary:
- resolve the selected project's sprint cadence from its registered `context.sprint_cadence` authority
- resolve the active sprint containing the request timestamp using that cadence's timezone, start boundary and interval semantics
- display the full scheduled date range on the cover even when the request is made before sprint end
- factual content uses the actual verified data cutoff, never a future sprint endpoint

Do not include design-process explanations.

---

# ① AVKLARAT SEDAN FÖRRA MÖTET

Official meeting-point title shown on **every** slide in this section:

`✏️ 1. Avklarat sedan förra mötet`

Page-specific descriptions resolved from the selected project's registered repository-flow authority — including its primary integration subtitle and each registered collection-branch subtitle — plus `Teamsammanfattning`, are subtitles,
never replacements for the official meeting-point title.

Use the active sprint resolved from the request timestamp. Meeting point 1
covers the active interval from `SPRINT_START` to `DATA_CUTOFF` according to the selected project's registered sprint-cadence interval semantics. It may not claim work after the actual
data cutoff merely because the cover displays the full scheduled sprint end.

## Scope: only completed work

Meeting point 1 is the completed-work section. Detailed work cards here show
only work already completed according to verified delivery evidence.

It MUST NOT contain:
- decisions that still need to be made
- open questions or decision candidates
- future actions or prioritization proposals
- backlog or unstarted work
- ordinary work-in-progress cards
- AI proposals about what the team should do next

Those belong to later meeting points, especially ③–⑤, ⑨, ⑩, ⑬ and ⑭.

A decision may appear in meeting point 1 only when it was **already made** during
the covered period and is verified by an approved source. Never include a
planned decision, a decision candidate, an unresolved question or an AI-suggested
decision here.

“Done” means a verified merge during the sprint window to either the registered primary integration branch or one of the collection branches resolved from the selected project's `context.repository_flow` authority. Project-board `Done` is a consistency check,
not a substitute for merge evidence. Show mismatches instead of guessing.
Deduplicate work promoted through multiple branches.

Mandatory content order:
1. registered primary integration branch
2. every registered collection branch, in repository-flow order
3. AI-proposed team summaries for the meeting protocol

Every registered delivery target above gets its own physical slide sequence, in the stated order.
Each registered collection-branch page is mandatory even when the verified
merge result is empty: render a grounded empty state, or an explicit incomplete
state when acquisition failed. A merge to a registered collection branch must
never be folded into the primary-integration slide or only summarized in a team-summary card.

Six cards is the standard capacity per physical slide, never a total limit.
Create as many continuation slides as required and never omit grounded completed
work.

## Subtitle — {PRIMARY_INTEGRATION_SUBTITLE}

Primary heading remains:
`✏️ 1. Avklarat sedan förra mötet`

Subtitle:
`{PRIMARY_INTEGRATION_SUBTITLE}`

Show every PR actually merged to the registered primary integration branch during the sprint window. Sort
oldest first. Each card contains verified PR number/title, grounded contribution,
actual contributor(s), team, merger/reviewer when verified and merge timestamp.
Do not include collection-branch-only merges here.

All continuation slides for this target keep the same subtitle exactly:
`{PRIMARY_INTEGRATION_SUBTITLE}`. Do not render generic subtitles such as `Mergat under
sprinten`, `del 2`, `merged work` or equivalent.

## Subtitle — Mergat till {COLLECTION_BRANCH_A}

Primary heading remains:
`✏️ 1. Avklarat sedan förra mötet`

Canonical branch: `{COLLECTION_BRANCH_A}`. Show every verified merge to this branch during
the sprint window after the primary-integration pages. Use the same evidence fields as
above where available.

This collection branch always gets its own physical slide sequence. When verified
merge evidence is empty, show `Inga verifierade merges till {COLLECTION_BRANCH_A} under perioden`;
when acquisition is incomplete, show the source-specific warning instead. The slide
subtitle must be exactly `Mergat till {COLLECTION_BRANCH_A}`.

## Subtitle — Mergat till {COLLECTION_BRANCH_B}

Primary heading remains:
`✏️ 1. Avklarat sedan förra mötet`

Canonical branch: `{COLLECTION_BRANCH_B}`. Show every verified merge to
this branch during the sprint window after `{COLLECTION_BRANCH_A}`. Use the same evidence
fields as above where available.

This collection branch always gets its own physical slide sequence. When verified
merge evidence is empty, show `Inga verifierade merges till {COLLECTION_BRANCH_B} under perioden`;
when acquisition is incomplete, show the source-specific warning instead. The slide
subtitle must be exactly `Mergat till {COLLECTION_BRANCH_B}`.

## Subtitle — Teamsammanfattning till mötesprotokollet

Primary heading remains:
`✏️ 1. Avklarat sedan förra mötet`

This section always comes last in meeting point 1. Create one meaningful summary
card for each team represented in the sprint evidence. The summary is primarily
a summary of **what has been completed**.

Each card is ready to copy into the meeting protocol and contains separate
blocks:
- `🔎 AI-analys` — concise synthesis of verified completed work
- `⭐ AI-förslag` — polished proposed protocol wording
- relevant **already-made verified decisions** only when they materially explain the completed outcome
- `👥 ✅ Mötesprotokoll` only after the team has confirmed/copied the wording; before confirmation it remains an AI proposal

The proposed protocol wording is approximately 1–10 complete sentences per team
summary. It must:
- begin with what the team completed and how it moved the project forward
- include every team member's first name and their verified contribution during the relevant sprint period
- include verified review/help/integration work that contributed to completed delivery, not only authored code
- include only decisions that were already made and verified
- never include a decision still to be taken, an open meeting question, a future action or an AI-suggested decision
- mention a member with no verified completed contribution neutrally as `Ingen verifierad avklarad aktivitet i underlaget för perioden`; never infer performance or absence

### Required ending — Påbörjat men inte avklarat

At the **very end of each team summary**, after all completed work, add a short
ending introduced as `Påbörjat men inte avklarat` when qualifying work exists.

An unfinished item may be mentioned here only when BOTH are true:
1. verified development/review activity occurred during the sprint interval, and
2. that activity already produced a concrete, source-grounded value even though the overall item is not completed.

For each such item, state:
- what has already been done
- what concrete value that completed portion already provides
- explicitly that the overall item is still not completed

Acceptable examples include:
- tests already implemented in an unmerged PR
- a working skeleton/bridge/API layer already implemented but not finished
- verified responsive behavior already implemented on an active branch
- reviewed partial integration not yet merged to the delivery branch

Do NOT include:
- merely assigned work with no implemented value
- backlog or future plans
- a branch name alone as proof of value
- open decisions/questions
- what the team should do next

There is **no separate work-in-progress subsection inside meeting point 1**.
Detailed unfinished work belongs to points ③–⑤ and ⑨. Meeting point 1 may only
mention valuable unfinished progress in the final lines of the relevant team
summary.

Nothing in meeting point 1 may describe work outside the active sprint start to
data-cutoff interval. Backlog, future plans, open decisions and work with no
verified completed or partial value belong to later meeting points.

---

# ② CURRENT STATE & DEADLINES

Purpose: orient the team in **where we are in the full course period**, which
deadlines/checkpoints are already passed, and what deserves extra attention next.

## Primary visual: chronological course/project timeline — mandatory

Meeting point 2 uses a true chronological timeline as its primary visual. A card
grid alone is not sufficient. The timeline must cover the **entire registered
course/project period**, from course start to final delivery, in left-to-right or
top-to-bottom chronological reading order. Course weeks, project phases, sprint
boundaries and verified milestones share one time axis.

Blockers, dependencies and risks are forbidden on this timeline and remain in
meeting points ⑥ and ⑦. Do not turn point 2 into a blocker map, dependency map or
priority board.

Each milestone/deadline card should show, when verified:
- phase/checkpoint/deadline name
- exact date/time
- status
- why it matters
- provenance

### Mandatory current-sprint position

The current sprint must be clearly identifiable inside the card/grid system.

Use an explicit card/badge/section label such as:
`AKTUELL SPRINT` / `Vi är här`

Show the complete registered sprint date range and place a visually unambiguous
current-week marker at the correct position on the time axis. Never shift the
registered sprint start to the meeting date.

### Status color semantics

Use:
- **Green = completed / passed / already carried out**
- **Orange = upcoming checkpoint/feedforward/intermediate milestone**
- **Red = critical deadline / major delivery with material consequence if missed**

Color must always be paired with text/symbol.

### Nearest-focus cards

Add 1–3 concise cards for the nearest upcoming items the team needs to track now.

When a nearest-focus card describes a school/submission/deadline task, use:
- `🎯` what
- `🕒` when
- `📍` where
- `💡` why
- `🛠` how
- `→` immediate preparation/action from verified data

Do not spell out repeated `VAD / NÄR / VAR / VARFÖR / HUR` labels.

### Overflow behavior for point 2

Keep chronological card order.
If all content does not fit readably, continue to `2a.`, `2b.` etc.
Never shrink below readability limits to avoid continuation slides.

## Content requirements

For each priority/deadline item included in the focus layer, include when evidence exists:
- exact verified deadline/checkpoint
- current verified status
- why it matters
- verified blocker/risk
- confirmed action if documented
- immediate preparation need

If consequence is AI-derived, mark it `🔎 AI-analys`.
If an action is AI-derived, mark it `⭐ AI-förslag`.

Do not invent progress percentages, days of delay or actions.

---

# ③ FRONTEND

Purpose: show the complete verified forward-looking Frontend work state for the upcoming period.

Include all verified Frontend work relevant to the upcoming period:
- active unfinished work verified from GitHub/issues/PRs/branches during the sprint interval
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
for local team context, ownership, reactivation, deferral or closure. Do not
invent estimates or assignments. Every card answers `Vad är läget och vad är
nästa lokala rörelse?`.

Points ③–⑤ do not decide the project-wide execution order and do not reproduce
the final action list. Cross-team ranking belongs to ⑨; the concise executable
action output belongs to ⑬.

Verified decisions summarized in the point-1 `Teamsammanfattning` subsection
may reappear here only when they materially control future work. Present the verified decision as fact and the resulting next action
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

Dependency classification, verification semantics, early synchronization signals
and sequencing logic are owned by:

`../../../project/DEPENDENCIES_AND_CAPACITY.md`

This slide applies that authority rather than redefining dependency planning.

## ⑥A Dependency cards

Include only critical dependency chains as cards.

Every dependency card MUST contain, in this logical order:
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
#ISSUE_ID · concise verified work title
Flyttar auth till säkrare cookie-baserad lösning.
⏳ efter integration
```

Optional arrows/connectors between cards may represent verified dependency direction.

If dependency direction is inferred by AI rather than explicitly supported, mark the interpretation `🔎 AI-analys`.

The dependency cards must feed the planning recommendations on ③–⑤, ⑨ and ⑬. If a blocker appears here but does not influence proposed ordering anywhere, re-check the prioritization logic.

## Pre-meeting cross-team contract review

Before the meeting, inspect verified integration surfaces that materially connect work areas or teams when such interfaces exist in the current work period.

This is a planning and verification step, not permission to invent a problem. Record only source-grounded findings.

Route each relevant finding forward instead of leaving it as isolated review metadata:
- blocking mismatch or unresolved dependency → ⑥ Blockers & dependencies
- risk created by the mismatch → ⑦ Risks
- contract/technical choice that needs a team decision → ⑩ Technical decisions
- concrete follow-up work → ⑬ Next steps
- external/PL decision needed → ⑭ Questions to PL

If no relevant integration contract exists for the sprint, record the check as not applicable in the audit rather than manufacturing a contract review.


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

Capacity, missing-estimate and qualitative-load reasoning are owned by:

`../../../project/DEPENDENCIES_AND_CAPACITY.md`

This slide presents that analysis using verified project evidence.

PRE-MEETING:
- do not estimate hours
- show documented availability constraints if registered sources contain them
- render only the planning consequence of personal availability, for example `begränsad tillgänglighet onsdag–torsdag`; omit personal reasons such as travel, health or private circumstances
- generalize private/health reasons to `limited availability`
- explain missing numeric capacity in project-facing language such as `Numerisk kapacitet saknas — planera kvalitativt`; do not expose internal AI-policy wording such as `Vad AI inte får göra` on the slide
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

## Support, pairing and shared blocker ownership

Verified support, pairing, review and knowledge transfer are legitimate sprint work when they help complete, unblock or safely integrate sprint-critical work. Do not treat them as invisible or optional merely because they are not the primary authored issue.

When a person or team is blocked, planning should evaluate whether another team member can help remove the blocker, review, pair, transfer knowledge or take independent parallel work. Frame the blocker as a delivery constraint for the team, not as an individual performance judgment.

Any proposed support/pairing remains `⭐ AI-förslag` until confirmed. Do not invent availability, skill or ownership.


---

# ⑨ PRIORITIZATION & SCOPE

Purpose: give the team a **compact, immediately usable execution order** for
the remaining sprint work.

Point ⑨ selects and orders work from the evidence in ③–⑧. It does not repeat
the complete team inventories from ③–⑤. Each selected work item appears once
in ⑨, inside the single execution group that reflects its current priority.

Meeting point 9 uses cards inside a **mandatory vertical execution sequence**.
The slide-level structure is optimized for fast scanning and clear priority and
is an explicit exception to the general shared-grid composition.

## Mandatory execution groups

Render these groups in this logical order:

1. **Prioritering först**
2. **Parallellt**
3. **Backlog — lägre prioritet**
4. **Förslag framåt — finns ännu inte / behöver korrigeras**

The first three groups describe existing verified work. The fourth group
contains model-proposed work that does not yet exist as a usable issue, or an
existing issue that needs correction before it can guide implementation.

Important exception:
**A proposal is NOT forced to stay in group 4.**
If a missing/corrective issue is necessary to remove a blocker, protect a
critical deadline, restore a broken core flow, resolve an important risk, or
correct misleading scope, that proposal may be promoted directly into
**Prioritering först** or **Parallellt**.

When promoted, it must remain visibly labeled as a proposal:
`⭐ AI-förslag — skapa issue` or `⭐ AI-förslag — korrigera issue`.

## 1. Prioritering först

This is the strongest section and contains the work that should be handled
first because it removes a blocker, protects a deadline, unlocks another team,
closes a critical core-flow gap, or corrects a misleading/insufficient issue.

Place items in strict priority order from top to bottom within the vertical execution sequence.

For existing work, each item is intentionally compact:

```text
#[ISSUE]  [kort pedagogisk förklaring]  [verifieringssymbol]
```

For a missing/corrective issue promoted into this group:

```text
⭐ skapa/korrigera issue  [kort förklaring]  [verifieringssymbol]
```

Required content for existing issue:
- verified issue number
- one short pedagogical explanation of what the work contributes / why it is first
- one visible provenance/verification symbol

Required content for promoted proposal:
- proposal label
- concise proposed issue purpose/correction
- why it must happen before or alongside current work
- visible `⭐ AI-förslag` provenance
- reference to the verified gap/risk/dependency that caused the proposal

Do NOT add:
- assignee rows
- branch rows
- timestamps
- long status sentences
- separate AI-analysis paragraphs per row
- duplicated titles when the issue number + explanation is sufficient

If ordering is AI-derived, one short group-level `🔎 AI-analys` is enough.
Do not repeat the same label on every existing issue row.

## 2. Parallellt

Below the first-priority group, show work that can proceed independently while
the first-priority path is being handled.

Use the same compact row structure for existing work:

```text
#[ISSUE]  [kort pedagogisk förklaring]  [verifieringssymbol]
```

A missing/corrective issue may also be placed here when it can be created or
clarified independently without blocking the primary path.

Order parallel items by usefulness to the active sprint.

Do not imply that "parallel" means lower value; it means the item does not need
to wait for the same dependency.

## 3. Backlog — lägre prioritet

Place this group below active execution work in the vertical sequence.

This group is deliberately the most compact. It preserves scope awareness
without competing with current execution.

Show only:
- issue number
- very short issue title when needed for recognition
- verification/provenance symbol

Example:

```text
#ISSUE_A · verified item  ✅
#ISSUE_B · verified item  ✅
#ISSUE_C · verified item  ✅
```

No pedagogical explanation is required in the backlog group.
No AI rationale, assignee, branch, timestamp or expanded metadata is shown here.

## 4. Förslag framåt — finns ännu inte / behöver korrigeras

This is a compact final group for useful work that is not yet represented by a
good actionable issue.

Include only suggestions that add real project value.

Two valid proposal types:

### A. Skapa ny issue
Use when:
- an important implementation/decision/task is missing from the board
- a verified gap, blocker, risk or dependency has no adequate issue
- work is likely to be forgotten because it exists only in notes/analysis

Compact format:

```text
⭐ Skapa issue: [kort namn] — [en kort rad om varför]
```

### B. Korrigera befintlig issue
Use when:
- the current issue scope is outdated, misleading, incomplete or no longer
  matches the actual architecture/work
- acceptance criteria need correction before the issue can guide work
- an issue duplicates another and should be clarified/merged/closed

Compact format:

```text
⭐ Korrigera #ISSUE_ID — [kort vad som behöver ändras]
```

Do not create filler proposals.
Check existing issues/PRs first to avoid duplicates.

For ordinary future proposals, this group stays last.

### Promotion rule — critical

Before rendering group 4, evaluate every proposal against current blockers,
deadlines, risks and dependencies.

If a proposal is required **now** to:
- remove a blocker
- unlock another team
- protect the nearest critical deadline
- restore/complete a core flow
- correct an issue whose current wording would direct the team incorrectly
- capture a high-priority risk mitigation that otherwise has no owner/work item

then **promote it** to `Prioritering först` or `Parallellt` instead of leaving
it at the bottom.

Its proposal status must remain visible even after promotion.

## Ordering rules

Top-to-bottom order must be grounded in slides ③–⑧ and verified project data.

Priority logic:
1. missing/corrective issue required to make the plan valid
2. blocker/dependency removal
3. critical deadline protection
4. core-flow/integration completion
5. review/merge work needed to unlock others
6. useful independent parallel work
7. lower-priority verified backlog
8. non-urgent future proposals

When a dependency is verified, its prerequisite must appear above the work it
unlocks. If dependency direction is AI-interpreted rather than explicit, mark
the group-level rationale `🔎 AI-analys`.

Do not invent numeric estimates or availability.

## Team ownership

Team ownership is secondary on this slide.

Do not split the slide into fixed project-specific team columns.
The priority order across the whole project is the primary organizing principle.

### Vertical execution geometry — mandatory

On each physical point-9 slide, the execution groups are arranged as a genuine
top-to-bottom sequence:

```text
Prioritering först
        ↓
Parallellt
        ↓
Backlog — lägre prioritet
        ↓
Förslag framåt
```

Geometry rules:
- each group starts below the previous group's bottom edge;
- groups may span most or all of the usable slide width;
- the four execution groups must not be arranged as a 2×2/four-quadrant matrix;
- cards remain the component language inside each group;
- continuation slides preserve group order;
- if the vertical sequence becomes too dense, paginate rather than shrinking text.


## Open pull requests

Open PRs appear in the appropriate execution group according to what they block
or enable.

Compact form:

```text
📌 #PR_ID  [verifierat arbete] väntar på review/merge  ✅
```

Do not create a separate PR section unless the dataset is unusually large and a
continuation slide is necessary.

## Continuation behavior

Try to fit the complete vertical execution view on one physical slide using
approved card spacing.

If it still does not fit at readable sizes:
- continue as `9a. Prioritering och scope`
- preserve the same execution order
- never split a group in a way that makes priority sequence ambiguous
- repeat group headings on continuation pages when needed

The slide must optimize for **top-to-bottom order visibility and predictable card structure**.

---

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

Purpose: show the current decided sprint goals, how verified execution aligns
with them, and any clearly separated planning proposal.

Goal resolution, source priority, milestone reasoning and AI proposal semantics
are owned by:

`../../../project/GOALS_AND_SPRINT_PLANNING.md`

This slide applies that authority rather than redefining it.

Required presentation meanings:
- the source-backed decided goal(s), when available
- concise evidence of progress/alignment when useful
- `🔎 AI-analys` when interpreting alignment, deviation or pressure
- `⭐ AI-förslag` when recommending a changed/future goal

When a proposal changes an existing goal, show enough information for the team to
understand:
- what would change
- from what
- to what
- why
- expected effect/tradeoff

Do not silently replace a verified decided goal with an AI-generated goal.

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

Purpose: make the concise executable action output clear while preserving provenance and showing risk-driven prioritization.

### Progressive-funnel hard rule

Point ⑬ contains only concrete actions that follow from the ordering in ⑨ or
from verified team decisions and that now require execution, confirmation or
follow-up. It does not reproduce the complete team inventories from ③–⑤ or
copy every priority row from ⑨. When an item returns here, its function must
change from status/priority information into a clear action.

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

## Post-meeting repository actions

When the meeting produces confirmed changes, ⑬ should translate them into concrete repository actions where applicable rather than ending with generic follow-up language.

Valid repository follow-up may include updating or creating work items, adjusting confirmed planning state, documenting dependencies or decisions, and recording confirmed collaboration actions. Keep this rule generic; project-specific examples belong in project data, not in the context framework.

These are presentation/action-plan items; generating the deck does not itself mutate the project repository unless the user separately requests that action.

Every repository action must retain provenance. AI-proposed changes remain `⭐ AI-förslag` until confirmed.


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

Every physical slide, including continuation slides, MUST contain a reserved source footer listing the deduplicated registered sources actually used on that physical slide.

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
point_1_develop_subtitle_not_exact_count == 0
point_1_collection_branch_slide_missing_count == 0
point_1_collection_branch_subtitle_not_exact_count == 0
```

---

**Status:** PRODUCTION
**Version:** 3.3
**Last updated:** 2026-09-18
