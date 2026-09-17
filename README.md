# 📱 Avanza Team 1 — Context & Process Documentation

This repository is the **single source of truth** for:
- How AI should work on Avanza Team 1
- How presentations are built and validated
- Team standards and decision logs
- External data sources and access methods

**Do NOT derive AI workflow or presentation rules from the project repository.** That lives here only.

---

## 🎯 What do you want to do?

### 👤 I'm doing regular project work
→ **[_memory/PROJEKTKONTEXT_AVANZA.md](_memory/PROJEKTKONTEXT_AVANZA.md)**

### 🎨 I'm creating a presentation
→ **[_ai_guides/presentations/MANDATORY_READING_ORDER.md](_ai_guides/presentations/MANDATORY_READING_ORDER.md)**

### 📚 I need project facts
→ **[_memory/README.md](_memory/README.md)**

### 🤖 I'm looking for AI guidelines
→ **[_ai_guides/README.md](_ai_guides/README.md)**

---

## 📍 Authority Map — Where each rule lives

| Question | Authority |
|---|---|
| **How does the presentation pipeline work?** | [`SYSTEM_CONTRACT.yaml`](_ai_guides/presentations/SYSTEM_CONTRACT.yaml) |
| **What data sources are allowed?** | [`_memory/EXTERNAL_SOURCES.yaml`](_memory/EXTERNAL_SOURCES.yaml) |
| **What slides exist and what data belongs on them?** | [`SLIDE_DETAIL_SPEC.md`](_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md) |
| **What are the absolute WCAG/NPF boundaries?** | [`ACCESSIBILITY_NEURODIVERSITY.md`](_ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md) |
| **How does the deck look globally?** | [`VISUAL_DESIGN_MANDATORY.md`](_ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md) |
| **How must cards behave internally?** | [`CARD_COMPONENT_STANDARD.md`](_ai_guides/presentations/design/CARD_COMPONENT_STANDARD.md) |
| **How do facts/team input differ from AI suggestions?** | [`PROVENANCE_AND_AI_LABELING.md`](_ai_guides/presentations/design/PROVENANCE_AND_AI_LABELING.md) |
| **How is responsive fit/pagination handled?** | [`LAYOUT_OVERFLOW_GUARD.md`](_ai_guides/presentations/monday_meeting/design/LAYOUT_OVERFLOW_GUARD.md) |
| **How is the final artifact validated?** | [`RENDER_GATE_CHECKLIST.md`](_ai_guides/presentations/verification/RENDER_GATE_CHECKLIST.md) |
| **What data must be collected and how?** | [`DATA_ACQUISITION_CONTRACT.yaml`](_ai_guides/presentations/data/DATA_ACQUISITION_CONTRACT.yaml) |
| **How is active work detected?** | [`ACTIVE_WORK_DETECTION_MODEL.md`](_ai_guides/presentations/data/ACTIVE_WORK_DETECTION_MODEL.md) |
| **Where should new rules be placed?** | [`ARCHITECTURE.md`](_ai_guides/presentations/ARCHITECTURE.md) |

Do not add competing presentation rules outside the authority map. New rule categories must be added to the architecture and mandatory reading order at the same time.

---

## 🆕 Current Presentation Contract — Version 2.2

### 1. WCAG is absolute
- The deck must never violate WCAG 2.2 AA.
- Normal text contrast: at least 4.5:1.
- WCAG large text: at least 3:1.
- Meaningful components/borders: at least 3:1.
- Color is never the sole information carrier.
- If a design cannot remain accessible, the layout changes or paginates.

### 2. Responsive cards
- All item-based content uses the same modern glass-card system.
- Cards are content-driven and responsive.
- Text uses preferred sizes plus defined minimum sizes.
- Dense slides may deliberately use smaller sizes within the allowed range.
- Automatic shrink-to-fit is forbidden.
- If minimum accessible sizes still do not fit, use fewer cards or continuation slides.

### 3. Card styling
- Team color is a narrow left accent only.
- No full team-colored outline or fill.
- Natural top-to-bottom flow; no vertical distribution that creates irregular gaps.
- Merge metadata uses `Merged:` and `Review:`.
- Merge/activity timestamp uses compact two-line format where applicable.

### 4. Source provenance
- `📅 Schemafakta` = explicitly present in registered school schedule.
- `✅ Mötesprotokoll` / equivalent = explicitly supplied or confirmed by the team.
- `? AI-förslag` / `? AI-analys` = inferred or proposed by AI.
- `⚠ Källa behöver verifieras` = origin cannot be verified.
- Mixed cards label each block separately.
- Red is not a fact color; red remains blocker/critical.

### 5. Applies to the whole deck
These rules apply to merged work, active work, backlog, team details, risks, sprint plan, sprint goals, next steps, PL questions and all other card-based slides.

---

## 🚨 Conflict Rule

Use this order when instructions conflict:

1. `SYSTEM_CONTRACT.yaml` — orchestration/gates
2. `ACCESSIBILITY_NEURODIVERSITY.md` — absolute WCAG/accessibility boundary
3. `VISUAL_DESIGN_MANDATORY.md` — global visual rules
4. `CARD_COMPONENT_STANDARD.md` — card internals
5. `PROVENANCE_AND_AI_LABELING.md` — source/fact/AI identity
6. `LAYOUT_OVERFLOW_GUARD.md` — responsive fit/pagination
7. `SLIDE_DETAIL_SPEC.md` — slide content
8. `TEMPLATE_REFERENCE.html` — reference only

**Mechanical fit rule:** start at preferred sizes, reduce deliberately only inside approved component ranges, preserve WCAG AA, then adapt card geometry/density. If the content still does not fit at the accessible minimum, create continuation slide(s). Never clip, overlap or omit required information.

---

## 🔗 Project Links

- **Project code:** https://github.com/chas-challenge-2026/avanza-team1
- **Project Board:** https://github.com/orgs/chas-challenge-2026/projects/31
- **Context repo:** https://github.com/zaida-wiss/context_enginering
