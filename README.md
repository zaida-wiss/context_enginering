# 📱 Avanza Team 1 — Context & Process Documentation

This repository is the **single source of truth** for:
- how AI should work on Avanza Team 1
- how presentations are built and validated
- team standards and decision logs
- external data sources and access methods

Do not derive presentation rules from the project repository.

---

## 🧭 Global AI framework

Before any task-specific routing, apply
[`_ai_guides/AI_FRAMEWORK.yaml`](_ai_guides/AI_FRAMEWORK.yaml).

Its conflict-decision gate applies to every AI task in this repository. When
active rules genuinely contradict each other, the AI must stop, show the
conflicting rules and consequences, and ask the user to decide **before** it
changes the rules or continues the affected task.

## 🧭 Context registry

Machine-readable paths and task bundles are registered in
[`CONTEXT_REGISTRY.yaml`](CONTEXT_REGISTRY.yaml). Use it as the central path
atlas when files move or when an AI task needs to resolve its dependencies.

## 🎯 What do you want to do?

### 👤 Regular project work
→ [`_ai_guides/project/PROJECT_CONTEXT_ROUTER.md`](_ai_guides/project/PROJECT_CONTEXT_ROUTER.md)

### 🎨 Create a presentation
→ [`_ai_guides/presentations/MANDATORY_READING_ORDER.md`](_ai_guides/presentations/MANDATORY_READING_ORDER.md)

### 💬 Improve presentations through feedback
→ Update the owning instruction in the context repository. Do not alter an
existing presentation unless the user explicitly asks for that artifact to be
updated or regenerated.

If new feedback contradicts an active rule, the AI must show both rules and ask
which one has priority before changing the context. The latest wording never
silently wins by default.

WCAG 2.2 AA cannot be deprioritized. A conflicting request must be explained
and converted into the closest accessible alternative instead.

When the user requests a contradiction audit, findings are first discussed in
chat without changing files. Context rules are cleaned up only after the user
chooses the intended result, except where WCAG already determines the outcome.

### 📚 Project facts
→ [`_memory/README.md`](_memory/README.md)

### 🤖 AI guidelines
→ [`_ai_guides/README.md`](_ai_guides/README.md)

---

## 📍 Authority Map — one owner per rule category

| Question | Authority |
|---|---|
| Which files are active authorities? | [`AUTHORITY_REGISTRY.yaml`](_ai_guides/presentations/AUTHORITY_REGISTRY.yaml) |
| How does the presentation pipeline work? | [`SYSTEM_CONTRACT.yaml`](_ai_guides/presentations/SYSTEM_CONTRACT.yaml) |
| What data sources are allowed? | [`data/SOURCES.yaml`](data/SOURCES.yaml) |
| What are the absolute WCAG/NPF boundaries? | [`ACCESSIBILITY_NEURODIVERSITY.md`](_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md) |
| How does the deck look globally? | [`VISUAL_DESIGN_MANDATORY.md`](_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md) |
| What are the hard readability/typography rules? | [`READABILITY_HARD_RULES.md`](_ai_guides/presentations/design/READABILITY_HARD_RULES.md) |
| How must cards behave internally? | [`CARD_COMPONENT_STANDARD.md`](_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md) |
| How do facts/team input differ from AI suggestions? | [`PROVENANCE_AND_AI_LABELING.md`](_ai_guides/presentations/design/PROVENANCE_AND_AI_LABELING.md) |
| How is responsive fit/pagination handled? | [`LAYOUT_OVERFLOW_GUARD.md`](_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md) |
| What slides exist and what data belongs on them? | [`SLIDE_DETAIL_SPEC.md`](_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md) |
| How is active work detected? | [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md) |
| How is the final artifact validated? | [`RENDER_GATE_CHECKLIST.md`](_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md) |
| Where should new rules be placed? | [`DESIGN_AUTHORITY.md`](_ai_guides/presentations/design/DESIGN_AUTHORITY.md) + [`ARCHITECTURE.md`](_ai_guides/presentations/ARCHITECTURE.md) |

Do not add competing presentation rules outside this map. A rule should be defined once by its owning authority and referenced elsewhere.

After changing presentation instructions, run:

```bash
python3 _audit/validate_presentation_authorities.py
```

---

## 🚨 Conflict Rule

Global conflict behavior is normatively owned by
[`_ai_guides/AI_FRAMEWORK.yaml`](_ai_guides/AI_FRAMEWORK.yaml).

**Do not resolve a genuine contradiction by applying an authority ranking.**
Authority maps identify ownership and absolute boundaries; they do not replace
the user's decision when two active project intentions are incompatible.

For a genuine conflict:
1. STOP the affected work.
2. Show the conflicting rules and owning files.
3. Explain the consequence of each option.
4. Ask the user to decide.
5. Update the owning context rule(s) and regression test after the decision.
6. Continue only when the context is consistent.


## 🧭 Presentation rules — where to change what

README is the human entry point. Presentation behavior is defined by the owning
authority files, so a rule is maintained in one canonical place.

Use the Authority Map above to locate the owner before changing presentation
behavior. In particular:

- execution and delivery → `SYSTEM_CONTRACT.yaml`
- accessibility → `ACCESSIBILITY_NEURODIVERSITY.md`
- global visual design → `VISUAL_DESIGN_MANDATORY.md`
- readability → `READABILITY_HARD_RULES.md`
- card internals → `CARD_COMPONENT_STANDARD.md`
- fact/team/AI labeling → `PROVENANCE_AND_AI_LABELING.md`
- Monday Meeting slide content → `SLIDE_DETAIL_SPEC.md`
- source registry → `data/SOURCES.yaml`

The presentation router determines which authorities are loaded for a task.
README explains the map; it does not duplicate the detailed rules.

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Context repo:** https://github.com/zaida-wiss/context_enginering
