---
project: avanza
type: project_presentation_authority
version: 1.8
status: active
scope: projects/avanza
---

# Avanza Presentation System

This file owns Avanza-specific presentation composition and project semantics.
Global presentation design is inherited by default, including the current navy/glass
visual foundation. Avanza rules may add or specialize behavior without needing to
duplicate the global design.

If an Avanza-specific design rule would conflict with an active global design rule,
the AI must stop and ask an explicit control question before applying that project
override. Without explicit approval for the deviation, the global design remains
effective.

Global authorities also continue to own WCAG/accessibility, source integrity,
overflow safety, evidence semantics and conflict handling.

## 0. Content boundary — what may become visible meeting text

User-facing Avanza slides may contain only:
- verified Avanza project facts from registered project sources;
- verified course/schedule/deadline facts from registered course sources;
- verified team/person/branch/PR/commit/review facts from GitHub or registered team sources;
- explicitly labelled `🔎 AI-analys` when the slide needs analysis for a meeting decision;
- explicitly labelled `⭐ AI-förslag` when the slide needs a suggested action/question.

Framework text is control input, not slide content. Do not render phrases such as
`hierarki`, `debug`, `QA`, `renderkontroll`, `dev-regler`, `versionen bygger på`,
`content boundary`, `whitespace är bättre än fejdata`, or similar process notes as
ordinary meeting content.

Presentation rules may influence selection, ordering, status labels, symbols and
layout. They may not become the subject of the meeting deck unless the requested
meeting itself is about the presentation framework.

## 0A. Symbol layer is semantic content

Canonical symbols are part of the information architecture and survive every
simplification, refactor and render pass.

Avanza consumes the complete canonical symbol grammar from
`PROVENANCE_AND_AI_LABELING.md`.

Required classes include:
- task meaning: `📅 🎯 🕒 📍 💡 🛠 👤`
- provenance/reasoning: `👥 ✅ 🔎 ⭐ ⚠`
- GitHub verification: GitHub icon + `✅`
- workflow: `📌 🔗 🔀`
- risk analysis: `⚡ 📈 💥 🛡 👤 ↘`
- project team symbols from `TEAM_VISUAL_IDENTITY.yaml`

A symbol may be rendered with a symbol-capable font or as a native/vector icon,
but its meaning must remain visible in the exported PDF. Symbol loss is a render
failure, not an acceptable visual simplification.

For cards with provenance meaning, keep the inline symbol at the relevant content
block and the matching symbol + text in the card-bottom provenance row as defined
by the global provenance authority.

## 0B. Team colors and criticality are separate semantic layers

Use `projects/avanza/design/TEAM_VISUAL_IDENTITY.yaml` for team identity:
- Frontend = turquoise accent + `🖥`
- Backend = pink accent + `🗄`
- Native/System = purple accent + `⚙`
- Cross-team = orange accent + `🔗`

Team identity uses a stable visual pair: **team accent + team symbol**.  
Criticality is a separate layer:
- `🔴 Kritisk` = blocks deadline/demo/core flow or requires decision now
- `🟠 Viktig` = affects current sprint or unlocks another team soon
- `🟢 Stabil` = useful/trackable but not currently blocking

On a dedicated team slide, the slide header already names the team. Cards therefore
use the team accent and symbol without repeating `Frontend`, `Backend` or
`Native/System` as ordinary card text.

On mixed-team slides, each card uses the team symbol + accent and the slide contains
a compact legend mapping symbols to teams. This supplies a non-color cue without
repeating the full team name inside every card.

Criticality always uses symbol + text + color and remains independent of team identity.

## 0C. Collection-branch completion semantics

For meeting point 1, each registered delivery target owns its own completed-work page.

Primary integration branch (`develop`):
- completed evidence = verified merge to `develop` during the active interval.

Collection branches such as `Java-Development-Environment` and `C/C++-Native`:
- completed-on-that-branch evidence = any verified merge, rebase result, or direct commit/push that lands on the collection branch during the active interval;
- a PR into `develop` is not required for the collection-branch page;
- work shown on a collection-branch page must clearly state the target branch and evidence type: `merge`, `rebase`, `direct commit` or `branch push`;
- once it is on that collection branch, it is considered avklarat for that branch page even if not yet merged onward to `develop`.

Collection branch work must never disappear merely because it lacks a PR to `develop`.

## 0D. Mandatory bottom fields for meeting point 1 cards

For every completed-work card in meeting point 1, preserve the following fields when evidence exists:
- developed/assigned by: first name or verified GitHub login mapped to first name when available;
- delivered by / commit author when no PR exists;
- merged by when the evidence is a PR merge or merge commit;
- approved/reviewed by when an APPROVED review exists;
- latest relevant delivery time: PR open, commit, push, merge or collection-branch landing time;
- target branch;
- evidence type: PR merge, merge commit, rebase/direct commit, branch push.

If a field is unavailable, leave that specific field as unknown or omit only that field. Do not omit the whole bottom zone and do not replace unknown people with guesses.

## 1. Inherited visual identity — global default used by Avanza

Avanza does **not** own its own slide-background palette or card-surface palette.
Those values are inherited from the active global authority
`_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md`.

For the current active global design this means:
- canvas uses the canonical modern navy gradient `#1E274A → #111A33`;
- if gradient rendering is unavailable, use the global fallback defined by the
  global visual authority, never a project-specific replacement;
- ordinary cards use the global frosted/glass-like surface system;
- rounded silhouette, restrained shadow, edge highlight and tonal depth follow
  the global visual authority;
- decorative/translucent layers stay behind text and never cross text bounds;
- generous whitespace and predictable alignment remain mandatory;
- team/status accent is supplementary; color never carries meaning alone.

Global WCAG/NPF/readability rules remain fully binding in Avanza. Avanza may add
project semantics and team identity, but it may not weaken or replace global
accessibility, typography, spacing, contrast, background or card-surface rules
without an explicit user-approved project override recorded in the framework.

A render fails Avanza visual identity if the background looks black/charcoal,
the global gradient is missing without the registered fallback condition, cards
lose their rounded glass character, decorative layers obscure content, or
global WCAG/NPF/readability gates fail.

## 2. Stable page anatomy

Every ordinary meeting page preserves:
1. meeting-point header
2. page-specific subtitle
3. content area
4. quiet operational/source footer

The meeting-point title never disappears when a page-specific subtitle is added.
Continuation pages retain the same anatomy and geometry.

## 3. Ordinary card-page geometry

Ordinary Avanza card pages use a stable SIX-SLOT geometry:

- 3 columns × 2 rows
- the six slots remain spatially reserved even when fewer than six cards exist
- one card occupies one normal slot; it does not expand merely because adjacent slots are empty
- empty slots are visual whitespace, not placeholder cards
- card geometry, alignment and spacing should therefore look as if the page could contain all six cards
- required content may not be shrunk below global readability rules to preserve the grid
- when content genuinely requires a special information structure, use the meeting-point-specific exception below rather than pretending it is an ordinary card page

## 4. Special information structures

The shared visual language remains navy + glass + rounded surfaces, but not every
meeting point is a generic grid.

- ②: chronological course/project timeline with a clear current-sprint locator
- ⑥: dependency/blocker map/graph with explicit direction and explanatory nodes
- ⑨: vertical execution sequence where project-wide order is primary
- ⑫: chronological sprint/day plan
- other points may use a documented special structure only when that structure
  communicates the information more clearly than the ordinary six-slot page

Special structures outrank the generic card renderer. A timeline, dependency map,
vertical sequence or sprint plan must never be flattened into ordinary 3×2 cards.

## 5. Meeting-point narrative contract

### ① Avklarat sedan förra mötet
Completed work only in detailed work cards.
Keep separate subtitles/pages for relevant collection branches such as develop,
Java-Development-Environment and C/C++-Native, followed by team summary.
Do not turn the page subtitle into the meeting-point title.

For collection branches, show every verified branch landing event as completed on
that branch even without a PR to `develop`. Include direct commit/rebase/branch push
evidence when that is the actual delivery path.

### ② Nuläge och deadlines
Show the full registered course/project chronology, not only the current week.
Mark the current sprint at its true chronological position. Nearest deadlines
and school/submission meaning remain grounded in registered course sources.

Make the delivery chain explicit when evidence supports it:
**current position -> remaining/missing work -> roadmap/milestone -> deadline -> consequence**.
Do not invent percentage-complete values when the registered sources do not
support them.

### ③ Frontend
Use a two-step information logic across the point:
1. **Var är vi?** — current/remaining work and per-issue delivery/DoD evidence.
2. **Vad gör vi?** — next work in grounded order, local blockers/dependencies,
   work this team is waiting for, and work other teams are waiting for from Frontend.

DoD is evaluated per issue/work item when the registered project definition and
evidence allow it. Never present one generic DoD state for the whole team.
When grounded estimate/effort evidence exists, carry it forward as input to ⑧;
never invent an estimate merely to populate capacity.

### ④ Backend
Use the same two-step logic:
1. **Var är vi?** — current/remaining work and per-issue delivery/DoD evidence.
2. **Vad gör vi?** — next work in grounded order, local dependencies and
   cross-team unlocking work explicitly, including what other teams are waiting
   for from Backend.

DoD is evaluated per issue/work item when evidence allows it, never as one
generic team-wide status. When grounded estimate/effort evidence exists, carry
it forward as input to ⑧; never invent an estimate merely to populate capacity.

### ⑤ Native/System
Use the same two-step logic:
1. **Var är vi?** — current/remaining work, integration readiness and per-issue
   delivery/DoD evidence.
2. **Vad gör vi?** — next work in grounded order, local blockers/dependencies,
   integration prerequisites and work other teams are waiting for from Native/System.

DoD is evaluated per issue/work item when evidence allows it, never as one
generic team-wide status. When grounded estimate/effort evidence exists, carry
it forward as input to ⑧; never invent an estimate merely to populate capacity.

### ⑥ Blockers och beroenden
Use a dependency map/graph when verified dependency direction exists.
Show what blocks what, affected team/work, consequence, required action and
fallback productive work where evidence allows it.

For each material blocker/dependency, resolve when evidence exists:
- prerequisite/root cause
- blocked work/team
- work/team unlocked when resolved
- owner or responsible area
- expected resolution/deadline when verified
- productive fallback work while waiting

Distinguish a dependency from a true blocker: waiting on one prerequisite does
not mean the whole team is blocked if useful independent work remains.
Connectors stay outside cards.

### ⑦ Risker
Make the chain visible:
risk -> likelihood when grounded -> consequence/impact -> mitigation -> fallback/backup -> impact on this week's plan.
Do not manufacture a probability or severity score merely to complete the chain.

A material risk must influence later capacity, priority, sprint-goal and planning
reasoning rather than exist as an isolated list. If a risk does not materially
change execution, keep that distinction visible instead of exaggerating it.

### ⑧ Kapacitet och estimering
Compare **available capacity with grounded planned need** using the unit actually
supported by project evidence (for example verified availability, hours, points,
WIP constraints or another registered measure).

Use verified numeric capacity only when sourced. Never invent hours, velocity or
estimates merely to make the comparison numeric. When numbers are unavailable,
reason qualitatively about load, WIP, availability and opportunities to unblock
or parallelize work.

The point must answer whether the current plan appears feasible from the evidence
available and identify the constraint that would require replanning.

### ⑨ Prioritering och scope
Use a vertical project-wide execution sequence:
Prioritering först -> Parallellt -> Backlog -> grounded AI proposals when needed.
Prerequisites appear before work they unlock.

The sequence must explain **why this order**. Ground the explanation in verified
dependencies, risk, capacity and deadline/scope constraints when they materially
affect the order. Do not manufacture a priority rule when evidence is absent.

### ⑩ Tekniska beslut
Show verified decision, decision owner when verified, affected area/team/work and
source/documentation location. When a decision is still open, show its decision
horizon/deadline only when grounded.

Do not promote a code pattern into a confirmed team decision without evidence.

### ⑪ Sprintmål
Separate source-backed goals from AI proposals. Reconcile the documented goal
against completed/current work, blockers, risks, capacity and priority.

Do not silently rewrite an official sprint goal. If verified evidence makes the
documented goal unrealistic or internally inconsistent, show the mismatch and
the decision needed. AI proposals remain explicitly proposals.

### ⑫ Sprintplan
Use a chronological **project-work** plan structure for eligible project days only.
Make dependency order, fallback work, availability, grounded capacity and
risk-driven sequencing visible.

For Avanza, Friday is a registered non-project day and is therefore omitted entirely
from the sprint-plan sequence. Do not render a Friday card, empty Friday slot,
disabled Friday column or Friday project placeholder. Friday may still appear on
course-schedule/timeline slides when relevant as course context, but it is not part
of project sprint planning.

The plan must remain consistent with the sprint goal and execution order from ⑨.
Do not manufacture a daily timetable where the project sources provide no such
schedule.

### ⑬ Nästa steg
Concrete actions continue the dependency-aware order from ⑨ and plan from ⑫.
Each action states what it concerns, why it matters, the owner and time horizon
when verified/decided, and a verification point: **how will the team know this
action is complete?**

Do not force every next step into a GitHub mutation; the action type follows the
actual work and decision needed.

### ⑭ Frågor till PL
Each material unresolved question gets a clear question block/card and a grounded
reason the answer matters to scope, priority, dependency, acceptance criteria or plan.

When evidence allows, also state the decision horizon:
- answer needed during this meeting / today
- answer can wait

Questions needing an immediate answer appear before questions that can wait.
Do not manufacture urgency when the source does not support it.

## 6. Data continuity and red threads

Acquire and verify shared meeting data once per generation run where the active
source contract allows it, then reuse the same verified facts through ①–⑭.
Do not independently reinterpret the same repository event differently on later
slides. Refresh a fact only when the source contract or freshness requirement
requires a new lookup.

A missing optional fact does not invalidate an entire meeting point. Render the
grounded information that remains useful, expose a meaningful unknown when it
affects a decision, and never fill a missing field with invented data.

### Mandatory cross-slide continuity

### Work thread
① completed work -> ③–⑤ remaining team work -> ⑨ execution order ->
⑪ goals -> ⑫ plan -> ⑬ next actions.

### Dependency thread
③–⑤ local blockers -> ⑥ dependency/blocker map -> ⑨ execution order ->
⑫ plan/fallback -> ⑬ concrete action.

### Risk thread
⑦ risk -> ⑧ realistic capacity constraint when applicable -> ⑨ changed order ->
⑪ goal pressure/alignment -> ⑫ mitigation in plan -> ⑬ concrete action.

### Capacity thread
③–⑤ workload evidence -> ⑧ capacity reasoning -> ⑨ WIP/order choice ->
⑪ realistic goal -> ⑫ feasible plan.

A later slide must not silently ignore a verified blocker, dependency, risk or
capacity fact that materially changes execution.

## 7. Card information zones

Ordinary work cards preserve a stable internal hierarchy:
- title/identifier
- concise contribution/explanation
- deliberate flexible whitespace
- developer/delivery activity row when relevant
- quiet operational/source information at the bottom

For completed merge work, the containing subtitle/section communicates merge
state; do not add a redundant MERGED/MERGAD badge, pill, tag or stamp at the top
of each card merely to repeat that state.

A completed merge card must still preserve the distinct verified identities and
event metadata that matter:
- developer/contributor identity
- delivery activity such as PR/push/commit when required by the active meeting data contract
- the person who actually merged the PR
- the verified approving reviewer(s), based only on submitted APPROVED reviews
- the verified merge timestamp

Developer and merger are different semantic roles even when the same person
happens to fill both roles. Do not collapse one into the other.

The merger and approving-reviewer identities belong in the card's lower
information zone. The merge timestamp belongs in the lower-right card zone and
represents the merge event, not PR-open time or latest-commit time. A verified
reviewer must never disappear merely because the containing page already says
`Mergat till …`. It must not collide with the
developer/delivery row, merger identity or source/footer content.

Avanza additionally requires operational bottom information with meeting value
(for example request/push information when verified and required by the active
meeting data contract) to remain present rather than being deleted for visual
simplification.

## 8. Visual QA

Before delivery, inspect the rendered output, not only source code.

Avanza-specific failures include:
- visible AI/framework instructions as ordinary meeting content
- team colors not matching `TEAM_VISUAL_IDENTITY.yaml`
- criticality shown only by color or mixed with team-color identity
- collection-branch landing events omitted because they lack PRs to `develop`
- visually black/charcoal background
- lost glass/rounded card treatment
- decorative overlay crossing text
- ordinary card page not preserving the 3×2 six-slot geometry
- one/few cards expanding merely because slots are unused
- empty/blank placeholder card surfaces rendered in reserved unused slots; unused slots must remain plain whitespace
- internal QA/debug/render-control slides included in the user-facing meeting deck
- connector arrows/lines or node dots shown on ordinary card slides such as ③–⑤, ⑦–⑧, ⑩–⑪, ⑬–⑭
- low-contrast or overly transparent text that becomes visually faint on the dark navy/glass surfaces
- missing meeting-point title
- special diagram/timeline flattened into generic cards
- dependency/blocker information not carried forward into priority/plan/actions
- required bottom operational row, verified merger identity, verified approving reviewer or verified merge timestamp lost through simplification
- any canonical task/provenance/GitHub/workflow/risk/team symbol lost, substituted or detached from its semantic field
- redundant MERGED/MERGAD tag/stamp added to a card whose containing page already communicates merge state

The historical presentation rules are recovery evidence, not active authority.
This file records the reconciled Avanza behavior after refactoring.
