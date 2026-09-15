---
name: design-authority
description: MANDATORY — Design authority hierarchy. context_enginering owns presentation design ONLY
metadata:
  type: process
  critical: true
---

# 🎨 DESIGN AUTHORITY — Var Comes Design From

**This file establishes SOURCE OF TRUTH for presentation design.**

---

## 🚨 RULE 0: DESIGN AUTHORITY HIERARCHY

**PRESENTATION DESIGN comes ONLY from context_enginering repo.**

```
DESIGN AUTHORITY (ranked by priority):
  
  🎯 RENDERING-LEVEL SPECIFICATION (MANDATORY):
  1️⃣ _ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md 
     (CANONICAL LAYOUT: header + message + 1–3 fullwidth blocks; NPF rules; typography fixed; render-gate rules)
  
  🎯 SLIDE-LEVEL SPECIFICATION (CONTENT AUTHORITY):
  2️⃣ _ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md 
     (EXAKT innehål per slide — format, data-sources, footer, what goes where)
  
  🎨 DESIGN CONTEXT (reference/understanding only):
  3️⃣ _ai_guides/presentations/design/ACCESSIBILITY_NEURODIVERSITY.md (why design rules exist)
  4️⃣ _ai_guides/presentations/design/REFERENCE_SLIDES/ (visual examples)
  5️⃣ _ai_guides/presentations/design/PRESENTATION_STYLE.md (historical reference — deprecated for rendering)
  
  ⚠️ DO NOT USE FOR RENDERING:
  
NOT FROM:
  ❌ avanza-team1 repo (project repo, data source ONLY)
  ❌ avanza-team1 styling, CSS, component library, or design tokens
  ❌ presentation tool's default template or auto-styling
  ❌ "what looks good" or general design trends
  ❌ imitation of Avanza-app visual identity
```

**CRITICAL RULE:** If SLIDE_DETAIL_SPEC.md says X and another file says Y → SLIDE_DETAIL_SPEC.md WINS.

**Reason:** SLIDE_DETAIL_SPEC.md is the ONLY file with:
- Explicit KOLUMNER (columns) for each slide
- Explicit DATA-SOURCES (where to fetch real data)
- Explicit MÅSTE/FÅR INTE (what must/must not appear)
- FOOTER specifications per slide
- REGLER (how to sort, how to filter, visual markers)

---

## 🚨 RULE 1: PROJECT REPO BOUNDARY

**CLEAR SEPARATION: context_enginering = design, avanza-team1 = data only**

### ALLOWED: Read from avanza-team1 for DATA ONLY

```
✅ GitHub Issues (what's being worked on)
✅ PRs & commits (who did what)
✅ Project Board status (Done/In Progress/Backlog)
✅ Technical architecture decisions
✅ Sprint goals & prioritization
✅ Team structure & roles
```

### FORBIDDEN: Extract design from avanza-team1

```
❌ Copy visual styling from avanza-team1 UI
❌ Use avanza-team1's component library for presentation
❌ Mirror avanza-team1's design tokens or color scheme
❌ Follow avanza-team1's layout patterns
❌ Import CSS or design system from project repo
❌ Assume presentation should "look like Avanza-app"
```

**Why:** Presentation is a COMMUNICATION TOOL, not a showcase of the product.
The two serve different purposes and need different visual identities.

---

## 🎨 RULE 2: PRESENTATION VISUAL IDENTITY (DEFINED IN THIS REPO)

**Presentations MUST have their own visual identity, separate from Avanza-app.**

### Visual Principles

✅ **Modern tech presentation** (like Figma, Stripe, or modern startup decks)  
✅ **Generous whitespace** (60-70% empty is good)  
✅ **Hierarchical typography** — clear primary/secondary/tertiary  
✅ **Semantic color ONLY** — green/orange/red for status, never decorative  
✅ **Avanza brand awareness** (acknowledgement that this is Avanza work) — but NOT mimicry  

### What "Avanza-feeling" means in presentations:

```
✅ Modern, clean, professional
✅ Data-driven (numbers, progress, clarity)
✅ Problem-focused (what's blocking us, how we solve)
✅ Respectful of audience time (no fluff)

❌ NOT: Dark mode + gradient hero-slides like Avanza product
❌ NOT: Product component library used for slides
❌ NOT: Avanza-app color scheme in presentation
❌ NOT: Mimicking the visual style of product UI
```

The presentation should feel like a **professional business deck**,
not like "a screenshot of the Avanza-app presentation feature."

---

## 🚨 RULE 3: DESIGN TOOL DEFAULTS ARE NOT AUTHORITY

**If presentation tool has default templates, default card layouts, or auto-coloring:**

**PowerPoint default theme → context_enginering PRESENTATION_STYLE.md wins**  
**Google Slides default template → context_enginering PRESENTATION_STYLE.md wins**  
**Figma default design → context_enginering PRESENTATION_STYLE.md wins**

```
WHEN THERE IS A CONFLICT:
- Default tool styling: "Use our template"
- PRESENTATION_STYLE.md: "Use this layout"

RESULT: PRESENTATION_STYLE.md is AUTHORITATIVE.
```

### What this means in practice:

- Don't use PowerPoint's default "Title + Content" layout unless PRESENTATION_STYLE.md says so
- Don't use Google Slides's default card arrangement unless explicitly instructed
- Don't use the tool's automatic color scheme — use semantic colors from PRESENTATION_STYLE.md
- Don't use the tool's "professional" template if it contradicts PRESENTATION_STYLE.md

**If the tool's default looks better, update PRESENTATION_STYLE.md to document why,
then update the tool. Don't silently deviate.**

---

## ✅ REFERENCE DESIGN: Where Visual Authority Lives

```
🎯 REFERENCE SLIDES ARE NORMATIVE:
  _ai_guides/presentations/design/REFERENCE_SLIDES/
  
These show:
  • Correct border usage (colored for status, black for info)
  • Correct whitespace distribution
  • Correct typography hierarchy
  • Correct progress bar styling
  • Correct team-status card layout
  • Correct issue-list formatting
  
Generated presentations should visually resemble these,
within the bounds of different data.
```

---

## 🔍 VERIFICATION: How to Know Design Authority is Being Followed

**Before any presentation is generated, check:**

```
Q1: Is every color choice explained in PRESENTATION_STYLE.md?
    YES → Proceed
    NO → Revert to PRESENTATION_STYLE.md or update it

Q2: Are there any visual elements not in the REFERENCE_SLIDES?
    YES → Question if they're needed; align or add to REFERENCE_SLIDES
    NO → Good

Q3: Does the presentation use default template styling the tool provides?
    YES → Check PRESENTATION_STYLE.md; override if it says to
    NO → Good

Q4: Are there any design choices borrowed from avanza-team1 repo?
    YES → STOP; design authority is context_enginering ONLY
    NO → Good

Q5: Does the visual style feel like Avanza-app rather than a standalone presentation deck?
    YES → Simplify; make it look like its own communication, not a product feature
    NO → Good
```

---

## 📋 FOR AI MODELS GENERATING PRESENTATIONS

**You MUST follow this hierarchy EXACTLY:**

### Before you render ANY presentation:

1. ✅ Read SYSTEM_CONTRACT.yaml (authority hierarchy)
2. ✅ Read VISUAL_DESIGN_MANDATORY.md (CANONICAL LAYOUT + render rules)
3. ✅ Read SLIDE_DETAIL_SPEC.md (content per slide)
4. ✅ Read ACCESSIBILITY_NEURODIVERSITY.md (why design works this way)

### When making ANY design choice:

1. ✅ Is it in VISUAL_DESIGN_MANDATORY.md? Use it.
2. ✅ Is it in SLIDE_DETAIL_SPEC.md? Apply it.
3. ✅ Is it shown in REFERENCE_SLIDES? Visual reference only (MANDATORY takes precedence).
4. ✅ Is it the tool's default? Override it per VISUAL_DESIGN_MANDATORY.md.
5. ✅ Is it from avanza-team1? FORBIDDEN. Use context_enginering design only.
6. ✅ Is it your own design taste? FORBIDDEN. VISUAL_DESIGN_MANDATORY.md is authoritative.

### If there's a conflict between:

- ✅ VISUAL_DESIGN_MANDATORY.md vs tool defaults → VISUAL_DESIGN_MANDATORY wins
- ✅ SLIDE_DETAIL_SPEC.md vs VISUAL_DESIGN_MANDATORY.md → Both apply (content + rendering rules together)
- ✅ ACCESSIBILITY_NEURODIVERSITY.md rules vs other design rules → NPF rules WIN when they conflict
- ❌ avanza-team1 design vs context_enginering rules → NEVER use avanza-team1 design

---

## 🚨 CHECKLIST: Design Authority Compliance

Before any presentation is delivered:

```
☐ VISUAL_DESIGN_MANDATORY.md rules followed (CANONICAL LAYOUT)
☐ SLIDE_DETAIL_SPEC.md content applied per slide
☐ ACCESSIBILITY_NEURODIVERSITY.md rules respected (NPF takes precedence)
☐ NO default tool template used
☐ NO avanza-team1 styling imported (product UI style is forbidden)
☐ Layout: exactly 1 header + 1 message + 1–3 fullwidth blocks (vertical stack)
☐ Whitespace: 20px margin between blocks, 16px padding inside
☐ Colors: semantic only (green/orange/red for status, never decorative)
☐ Typography: fixed sizes (14pt title, 13pt content, 12pt metadata)
☐ Symbols: ①②③④⑤ meeting-point markers present and consistent
☐ Rendered visually: PPTX must be viewed before delivery (RENDER_GATE mandatory)
☐ Data: from allowlisted project sources (GitHub, Sheets, Docs) per SYSTEM_CONTRACT / DATA_SOURCES only
```

---

**This file IS the design authority.**

**Do not negotiate with presentation tool defaults.**

**Do not borrow from avanza-team1.**

**context_enginering owns presentation design. Full stop.**

---

**Last updated:** 2026-09-13
