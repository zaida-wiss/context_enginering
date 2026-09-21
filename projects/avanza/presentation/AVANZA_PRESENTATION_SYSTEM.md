---
project: avanza
type: project_presentation_authority
version: 1.4
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

## 5. Meeting-point narrative contract

### ① Avklarat sedan förra mötet
Completed work only in detailed work cards.
Keep separate subtitles/pages for relevant collection branches such as develop,
Java-Development-Environment and C/C++-Native, followed by team summary.
Do not turn the page subtitle into the meeting-point title.

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
Use chronological plan structure. Make dependency order, fallback work,
availability, grounded capacity and risk-driven sequencing visible.

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
- the verified merge timestamp

Developer and merger are different semantic roles even when the same person
happens to fill both roles. Do not collapse one into the other.

The merger identity belongs in the card's lower information zone. The merge
timestamp belongs in the lower-right card zone and represents the merge event,
not PR-open time or latest-commit time. It must not collide with the
developer/delivery row, merger identity or source/footer content.

Avanza additionally requires operational bottom information with meeting value
(for example request/push information when verified and required by the active
meeting data contract) to remain present rather than being deleted for visual
simplification.

## 8. Visual QA

Before delivery, inspect the rendered output, not only source code.

Avanza-specific failures include:
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
- required bottom operational row, verified merger identity or verified merge timestamp lost through simplification
- redundant MERGED/MERGAD tag/stamp added to a card whose containing page already communicates merge state

The historical presentation rules are recovery evidence, not active authority.
This file records the reconciled Avanza behavior after refactoring.
