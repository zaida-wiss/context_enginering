# 📱 Avanza Team 1 — Context & Process Documentation

This repository is the **single source of truth** for:
- How AI should work on Avanza Team 1
- How presentations are built and validated
- Team standards and decision logs
- External data sources and access methods

**Do NOT derive AI workflow or presentation rules from the project repository.** That lives here only.

---

## 🎯 What do you want to do?

### 👤 I'm doing regular project work (coding, issues, etc)
→ **[_memory/PROJEKTKONTEXT_AVANZA.md](_memory/PROJEKTKONTEXT_AVANZA.md)**

### 🎨 I'm creating a presentation
→ **[_ai_guides/presentations/MANDATORY_READING_ORDER.md](_ai_guides/presentations/MANDATORY_READING_ORDER.md)**

### 📚 I need project facts (deadlines, standards, etc)
→ **[_memory/README.md](_memory/README.md)**

### 🤖 I'm looking for AI guidelines
→ **[_ai_guides/README.md](_ai_guides/README.md)**

---

## 📍 Authority Map — Where each rule lives

| Question | Answer |
|----------|--------|
| **How does the presentation system work?** | [`SYSTEM_CONTRACT.yaml`](_ai_guides/presentations/SYSTEM_CONTRACT.yaml) |
| **What data sources are allowed?** | [`_memory/EXTERNAL_SOURCES.yaml`](_memory/EXTERNAL_SOURCES.yaml) |
| **What slides exist and what's on them?** | [`SLIDE_DETAIL_SPEC.md`](_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md) |
| **How do slides look (colors, fonts, layout)?** | [`VISUAL_DESIGN_MANDATORY.md`](_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md) |
| **How is overflow/pagination handled?** | [`LAYOUT_OVERFLOW_GUARD.md`](_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md) |
| **What are the WCAG/accessibility requirements?** | [`ACCESSIBILITY_NEURODIVERSITY.md`](_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md) |
| **What data must be collected and how?** | [`DATA_ACQUISITION_CONTRACT.yaml`](_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml) |
| **How is "active work" detected from GitHub?** | [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md) |
| **Where should new rules be placed?** | [`ARCHITECTURE.md`](_ai_guides/presentations/ARCHITECTURE.md) |

**Do not add competing presentation rules outside the authority map.** If a genuinely new rule category is needed, add it to the authority map and reading order at the same time.

---

## 🆕 Latest Changes (Version 2.1)

**What changed:**
- Hard overflow/pagination guard: extra slide is mandatory before text can overlap or shrink.
- Grid is now explicitly restricted to ①A–①C and ⑬; ⑥A remains the diagram exception.
- ①D and ①E are single-column stacked and paginate instead of switching to multi-column layouts.
- Render verification must fail on overlap, clipping, out-of-card text, or fonts below minimum size.
- `TEMPLATE_REFERENCE.html` is illustrative only and may never override authority files.

Existing rules remain:
- Typography enforcement in [`VISUAL_DESIGN_MANDATORY.md`](_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md)
- Slide content in [`SLIDE_DETAIL_SPEC.md`](_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md)
- Evidence classification in [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md)

---

## 🚨 Critical Conflict Rule

If two authoritative files appear to contradict each other: **STOP before rendering.** Do not silently choose a layout.

For layout-density conflicts specifically, use this order:

1. `ACCESSIBILITY_NEURODIVERSITY.md` — accessibility boundary
2. `VISUAL_DESIGN_MANDATORY.md` — typography, card geometry, theme
3. `LAYOUT_OVERFLOW_GUARD.md` — fit, pagination, allowed grid layouts
4. `SLIDE_DETAIL_SPEC.md` — content and slide-specific fields
5. `TEMPLATE_REFERENCE.html` — example only, never authoritative

**Mechanical rule:** if content does not fit with the required typography and spacing, create a continuation slide. Never shrink, overlap, clip, or change a stacked slide into a multi-column layout.

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Team repos:**
  - This one: https://github.com/zaida-wiss/context_enginering
  - Code: https://github.com/chas-challenge-2026/avanza-team1
