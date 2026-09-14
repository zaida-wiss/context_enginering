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
  
  🎯 SLIDE-LEVEL SPECIFICATION (NEW — AUTHORITATIVE):
  1️⃣ _ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md 
     (EXAKT innehål per slide — format, kolumner, regler, data-sources, footer)
  
  🎨 DESIGN RULES (apply to all slides):
  2️⃣ _ai_guides/presentations/design/PRESENTATION_STYLE.md (typografi, layout, spacing)
  3️⃣ _ai_guides/presentations/design/VISUAL_DESIGN_MANDATORY.md (PowerPoint-tekniska regler)
  4️⃣ _ai_guides/presentations/design/REFERENCE_SLIDES/ (visual examples)
  
  ⚠️ DEPRECATED/CONFLICTING (DO NOT USE — see SYSTEM_CONTRACT.yaml):
  
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

### Before you write ANY slide code:

1. ✅ Read PRESENTATION_STYLE.md (rules 0-6)
2. ✅ Read REFERENCE_SLIDES/ folder (visual examples)
3. ✅ Read PRESENTATION_SPEC.md (content rules)
4. ✅ Read DATA_COLLECTION_MANDATORY.md (data rules)

### When making ANY design choice:

1. ✅ Is it in PRESENTATION_STYLE.md? Use it.
2. ✅ Is it shown in a REFERENCE_SLIDE? Copy it.
3. ✅ Is it the tool's default? Override it if PRESENTATION_STYLE.md says to.
4. ✅ Is it from avanza-team1? FORBIDDEN. Use context_enginering design only.
5. ✅ Is it your own design taste? FORBIDDEN. PRESENTATION_STYLE.md is authoritative.

### If there's a conflict between:

- ✅ PRESENTATION_STYLE.md vs tool defaults → PRESENTATION_STYLE wins
- ✅ REFERENCE_SLIDES vs tool suggestions → REFERENCE_SLIDES win
- ✅ PRESENTATION_SPEC.md vs PRESENTATION_STYLE.md → Both apply (content & design together)
- ❌ avanza-team1 design vs context_enginering rules → NEVER use avanza-team1 design

---

## 🚨 CHECKLIST: Design Authority Compliance

Before any presentation is delivered:

```
☐ PRESENTATION_STYLE.md rules followed
☐ NO default tool template used
☐ NO avanza-team1 styling imported
☐ Borders: colored (status) vs black/white (neutral info) — correct usage
☐ Whitespace: 60-70% empty space on each slide
☐ Colors: semantic only (green/orange/red for status, never decorative)
☐ Typography: hierarchy clear (title > subtitle > body)
☐ Symbols: 📝①②③ etc. present and consistent
☐ Visual identity: standalone presentation, not product-UI mockup
☐ Data: from context_enginering data sources ONLY
```

---

**This file IS the design authority.**

**Do not negotiate with presentation tool defaults.**

**Do not borrow from avanza-team1.**

**context_enginering owns presentation design. Full stop.**

---

**Last updated:** 2026-09-13
