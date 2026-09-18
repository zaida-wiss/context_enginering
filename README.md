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
| What data sources are allowed? | [`_memory/EXTERNAL_SOURCES.yaml`](_memory/EXTERNAL_SOURCES.yaml) |
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

Use this order when instructions conflict:

1. `SYSTEM_CONTRACT.yaml` — orchestration/gates
2. `ACCESSIBILITY_NEURODIVERSITY.md` — absolute accessibility boundary
3. `VISUAL_DESIGN_MANDATORY.md` — global visual rules
4. `READABILITY_HARD_RULES.md` — hard typography, line spacing and meeting-number readability
5. `CARD_COMPONENT_STANDARD.md` — card internals
6. `PROVENANCE_AND_AI_LABELING.md` — source/fact/AI identity
7. `PR_MERGE_REVIEW_IDENTITY.md` — merger/reviewer identity
8. `LAYOUT_OVERFLOW_GUARD.md` — responsive fit/pagination
9. `SLIDE_DETAIL_SPEC.md` — slide content
10. `TEMPLATE_REFERENCE.html` — reference only

If two authorities appear to own the same rule and disagree, fix the documentation before rendering.

---

## 🆕 Current card + readability contract

The detailed values live in `READABILITY_HARD_RULES.md` and `CARD_COMPONENT_STANDARD.md`. At a high level:

- pedagogical explanation sits directly under the title
- titles use a clear sans-serif and must not become visually extra-heavy
- ordinary body/support text is regular weight with open line spacing
- meeting-point headers use **ordinary digits**, e.g. `✏️ 2. Nuläge ...`; circled-number glyphs such as `②` are not rendered
- verified person identity uses first name only and is visually easy to scan
- **name/identity and verification/provenance are anchored at the bottom of every card when present**
- separate semantic text blocks always keep minimum spacing and multiline text keeps natural line height
- internal evidence labels such as `GitHub · nivå 1` are not shown in meeting cards
- merger/reviewer names are printed only when verified; unknown values stay blank
- timestamps are compact, one line, discreet and bottom-most when present
- automatic shrink-to-fit is forbidden
- if accessible content does not fit, cards reflow, grid density is reduced or the slide paginates
- meeting point 1 shows only work performed in the preceding Monday 09:00–current Monday 09:00 sprint window, using six cards as standard capacity per physical slide
- a Monday-meeting protocol is always dated/named for the current week that begins that Monday
- meeting points 3–5 remain the separate team sections: Frontend, Backend and Native
- meeting point 9 uses four team columns: `Frontend`, `Backend`, `Native`, `Cross-team`
- meeting point 9 keeps a fixed `1×4` structure with content-driven blocks and lettered continuations such as `9a`, `9b`
- point 9 shows open PRs as `📌 #[PR-number]`, remaining issues, order, dependencies, AI allocation and proposed missing issues
- source identity always keeps its canonical symbol; tags never replace `📅`, `✅`, `🔎`, `⭐` or `⚠`
- authoritative conflicts produce a rule-conflict receipt and stop rendering; they are never silently overwritten
- rendered delivery fails if text overlaps, line spacing is compressed or the bottom information zone collides with body text

This README intentionally does not duplicate numeric card spacing/type rules.

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Context repo:** https://github.com/zaida-wiss/context_enginering
