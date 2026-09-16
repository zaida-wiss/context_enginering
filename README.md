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
| **What are the WCAG/accessibility requirements?** | [`ACCESSIBILITY_NEURODIVERSITY.md`](_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md) |
| **What data must be collected and how?** | [`DATA_ACQUISITION_CONTRACT.yaml`](_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml) |
| **How is "active work" detected from GitHub?** | [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md) |
| **Where should new rules be placed?** | [`ARCHITECTURE.md`](_ai_guides/presentations/ARCHITECTURE.md) |

**Do NOT create new policy files.** All rules belong in one of the files above.

---

## 🆕 Latest Changes (Version 2.0)

**What changed:**
- Typography enforcement (see [`VISUAL_DESIGN_MANDATORY.md`](_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md))
- New slide ①E for assigned-but-not-started issues (see [`SLIDE_DETAIL_SPEC.md`](_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md))
- Clear LEVEL 3/4 boundaries for evidence classification (see [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md))

All rules, definitions, and specific values live in the authority files above. This is just an entry point.

---

## 🚨 Critical Rule

If two authoritative files appear to contradict each other: **STOP. Do not choose the interpretation that seems most reasonable.**

Report the conflict instead.

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Team repos:**
  - This one: https://github.com/zaida-wiss/context_enginering
  - Code: https://github.com/chas-challenge-2026/avanza-team1
