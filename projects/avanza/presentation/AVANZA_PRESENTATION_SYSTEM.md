---
project: avanza
type: project_presentation_authority
version: 1.0
status: active
scope: projects/avanza
---

# Avanza Presentation System

This file owns the Avanza-specific presentation identity and meeting-point composition.
Global authorities still own WCAG/accessibility, source integrity, overflow safety,
evidence semantics and conflict handling.

## 1. Visual identity — Avanza only

The rendered deck must visibly read as modern dark navy, never black.

- canvas: #15182E as the recognizable navy base
- card family: #1E233B / #252A45
- ordinary cards: dark frosted/glass-like surface
- rounded silhouette: approximately 16–20 px equivalent
- restrained shadow, edge highlight and tonal depth
- decorative/translucent layers always behind text and never across text bounds
- generous whitespace and predictable alignment
- team/status accent is supplementary; color never carries meaning alone
- no flat black/charcoal substitution
- if tonal/gradient rendering is unreliable, fall back to solid #15182E

A render fails Avanza visual identity if the background looks black, cards lose
their rounded glass character, or decorative layers obscure content.

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

- 2 columns × 3 rows
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

### ③ Frontend
Show current/remaining Frontend work, what should happen next and local
blockers/dependencies that affect execution.

### ④ Backend
Show current/remaining Backend work, what should happen next and cross-team
unlocking work explicitly.

### ⑤ Native/System
Show current/remaining Native/System work, integration readiness and local
blockers/dependencies.

### ⑥ Blockers och beroenden
Use a dependency map/graph when verified dependency direction exists.
Show what blocks what, affected team/work, consequence, required action and
fallback productive work where evidence allows it. Connectors stay outside cards.

### ⑦ Risker
Make the chain visible:
risk -> consequence -> mitigation -> impact on this week's plan.
A material risk must influence later planning rather than exist as an isolated list.

### ⑧ Kapacitet och estimering
Use verified numeric capacity only when sourced. Otherwise reason qualitatively
about load, WIP, availability and opportunities to unblock or parallelize work.

### ⑨ Prioritering och scope
Use a vertical project-wide execution sequence:
Prioritering först -> Parallellt -> Backlog -> grounded AI proposals when needed.
Prerequisites appear before work they unlock.

### ⑩ Tekniska beslut
Show verified decision, affected area/team and source. Do not promote a code
pattern into a confirmed team decision without evidence.

### ⑪ Sprintmål
Separate source-backed goals from AI proposals. Goals must remain realistic in
light of verified blockers, risks and capacity.

### ⑫ Sprintplan
Use chronological plan structure. Make dependency order, fallback work,
availability and risk-driven sequencing visible.

### ⑬ Nästa steg
Concrete actions continue the dependency-aware order from ⑨ and plan from ⑫.
Each action explains what it concerns and why it matters.

### ⑭ Frågor till PL
Each material unresolved question gets a clear question block/card and a grounded
reason the answer matters to scope, priority, dependency, acceptance criteria or plan.

## 6. Red threads — mandatory cross-slide continuity

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
- ordinary card page not preserving the 2×3 six-slot geometry
- one/few cards expanding merely because slots are unused
- missing meeting-point title
- special diagram/timeline flattened into generic cards
- dependency/blocker information not carried forward into priority/plan/actions
- required bottom operational row, verified merger identity or verified merge timestamp lost through simplification
- redundant MERGED/MERGAD tag/stamp added to a card whose containing page already communicates merge state

The historical presentation rules are recovery evidence, not active authority.
This file records the reconciled Avanza behavior after refactoring.
