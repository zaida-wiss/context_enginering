# 📱 Avanza Team 1 — Context & Process Documentation

This repository is the **single source of truth** for:
- how AI should work on Avanza Team 1
- how presentations are built and validated
- team standards and decision logs
- external data sources and access methods

Do not derive presentation rules from the project repository.

---

## 🎯 What do you want to do?

### 👤 Regular project work
→ [`_memory/PROJEKTKONTEXT_AVANZA.md`](_memory/PROJEKTKONTEXT_AVANZA.md)

### 🎨 Create a presentation
→ [`_ai_guides/presentations/MANDATORY_READING_ORDER.md`](_ai_guides/presentations/MANDATORY_READING_ORDER.md)

### 📚 Project facts
→ [`_memory/README.md`](_memory/README.md)

### 🤖 AI guidelines
→ [`_ai_guides/README.md`](_ai_guides/README.md)

---

## 📍 Authority Map — one owner per rule category

| Question | Authority |
|---|---|
| How does the presentation pipeline work? | [`SYSTEM_CONTRACT.yaml`](_ai_guides/presentations/SYSTEM_CONTRACT.yaml) |
| What data sources are allowed? | [`_memory/EXTERNAL_SOURCES.yaml`](_memory/EXTERNAL_SOURCES.yaml) |
| What are the absolute WCAG/NPF boundaries? | [`ACCESSIBILITY_NEURODIVERSITY.md`](_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md) |
| How does the deck look globally? | [`VISUAL_DESIGN_MANDATORY.md`](_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md) |
| How must cards behave internally? | [`CARD_COMPONENT_STANDARD.md`](_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md) |
| How do facts/team input differ from AI suggestions? | [`PROVENANCE_AND_AI_LABELING.md`](_ai_guides/presentations/design/PROVENANCE_AND_AI_LABELING.md) |
| How is responsive fit/pagination handled? | [`LAYOUT_OVERFLOW_GUARD.md`](_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md) |
| What slides exist and what data belongs on them? | [`SLIDE_DETAIL_SPEC.md`](_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md) |
| How is active work detected? | [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md) |
| How is the final artifact validated? | [`RENDER_GATE_CHECKLIST.md`](_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md) |
| Where should new rules be placed? | [`DESIGN_AUTHORITY.md`](_ai_guides/presentations/design/DESIGN_AUTHORITY.md) + [`ARCHITECTURE.md`](_ai_guides/presentations/ARCHITECTURE.md) |

Do not add competing presentation rules outside this map. A rule should be defined once by its owning authority and referenced elsewhere.

---

## 🚨 Conflict Rule

Use this order when instructions conflict:

1. `SYSTEM_CONTRACT.yaml` — orchestration/gates
2. `ACCESSIBILITY_NEURODIVERSITY.md` — absolute accessibility boundary
3. `VISUAL_DESIGN_MANDATORY.md` — global visual rules
4. `CARD_COMPONENT_STANDARD.md` — card internals
5. `PROVENANCE_AND_AI_LABELING.md` — source/fact/AI identity
6. `LAYOUT_OVERFLOW_GUARD.md` — responsive fit/pagination
7. `SLIDE_DETAIL_SPEC.md` — slide content
8. `TEMPLATE_REFERENCE.html` — reference only

If two authorities appear to own the same rule and disagree, fix the documentation before rendering.

---

## 🆕 Current card contract

The detailed values live only in `CARD_COMPONENT_STANDARD.md`. At a high level:

- pedagogical explanation sits directly under the title
- verified assignee/developer is visually prominent
- separate semantic text blocks always keep minimum spacing
- internal evidence labels such as `GitHub · nivå 1` are not shown in meeting cards
- merger/reviewer names are printed only when verified; unknown values stay blank
- timestamps are compact, one line, discreet and right-aligned
- automatic shrink-to-fit is forbidden
- if accessible content does not fit, cards reflow or the slide paginates

This README intentionally does not duplicate numeric card spacing/type rules.

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Context repo:** https://github.com/zaida-wiss/context_enginering
