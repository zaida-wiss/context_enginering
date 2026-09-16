---
name: ai_verification_workflow
description: What reports AI must generate at each phase (phase structure is in SYSTEM_CONTRACT.yaml)
metadata:
  type: process
  critical: true
---

# 🔍 AI VERIFICATION WORKFLOW — Report Templates

**The execution phases are defined in [`SYSTEM_CONTRACT.yaml`](../SYSTEM_CONTRACT.yaml)**

**This file shows WHAT REPORTS AI must generate at each phase.**

---

## PHASE 1: DATA COLLECTION & IDENTITY VERIFICATION

**AI must generate and show this report:**

```
═══════════════════════════════════════════════════════════
VERIFICATION REPORT — PHASE 1: DATA & IDENTITY
═══════════════════════════════════════════════════════════

IDENTITY VERIFICATION (7 team members):
  ✅ [Member name] ([GitHub username]) — verified from [source]
  ✅ [Member name] ([GitHub username]) — verified from [source]
  ... (all 7 members)

DATA SOURCES VERIFICATION:
  ✅ Branches (develop) — LIVE_VERIFIED
     Last commit: [date] by [person]
     Active branches: N
     
  ✅ Commits this week — LIVE_VERIFIED
     N commits in reporting period
     From team members: [names]
     
  ✅ Merged PRs — LIVE_VERIFIED
     N merged PRs this week
     
  ✅ Open PRs — LIVE_VERIFIED
     N open PRs with activity
     
  ⚠️ [Source] — FALLBACK_VERIFIED
     Primary unavailable, using: [fallback]
     
  ❌ [Source] — NOT_FOUND
     Will use: [fallback]

═══════════════════════════════════════════════════════════
RESULT: ✅ PHASE 1 PASSED — OK to proceed to PHASE 2
═══════════════════════════════════════════════════════════
```

---

## PHASE 2: DEDUPLICATION & ATTRIBUTION VERIFICATION

**AI must generate and show this report:**

```
═══════════════════════════════════════════════════════════
DEDUPLICATION & ATTRIBUTION VERIFICATION — PHASE 2A
═══════════════════════════════════════════════════════════

DEDUPLICATION CHECK (collection branches vs develop):
  ✅ Java-Development-Environment PRs scanned: N total
  ✅ C/C++-Native PRs scanned: N total
  ✅ Dedup by linked_issue_ids: M conflicts resolved
  ✅ Dedup by commit_sha_ancestry: K conflicts resolved
  ✅ Final count: Develop=[X], Collection-only=[Y], Deduplicated=[Z]
  
ATTRIBUTION VERIFICATION:
  ✅ Developed-by uses commit authors (primary): N% 
  ✅ Developed-by fallback to assignees: M%
  ✅ Reviewed-by includes APPROVED: N reviews
  ✅ Reviewed-by includes CHANGES_REQUESTED: M reviews
  ✅ Reviewed-by includes COMMENTED: K reviews
  ✅ Merged-by verified from pr.merged_by.login: all X PRs

═══════════════════════════════════════════════════════════
RESULT: ✅ ATTRIBUTION VERIFIED — OK to proceed
═══════════════════════════════════════════════════════════
```

---

## PHASE 3: RENDER GATE VERIFICATION

**AI must generate and show this report:**

```
═══════════════════════════════════════════════════════════
RENDER GATE VERIFICATION — PHASE 3
═══════════════════════════════════════════════════════════

DATA INTEGRITY CHECKSUMS:
  ✅ TOTAL: Develop PRs + Collection PRs (deduplicated) = repository_activity_total
  ✅ UNIQ: No PR shown twice (dedup applied)
  ✅ TEAM_COVERAGE: All 7 members appear (work or "available")
  ✅ COLLECTION_BRANCH_COVERAGE: Java-Development-Environment + C/C++-Native scanned

SLIDE COMPLIANCE:
  ✅ Slide ①A: 3×2 grid format (max 6 cards)
  ✅ Slide ①B: Full-width cards (if collection branches exist)
  ✅ Slide ①C-①D: Full-width stacked cards
  ✅ Slide ③④⑤: Compact vertically stacked cards (NOT tables, NOT horizontal bands)
  ✅ Design: Dark navy, soft cards 12-18px, responsive height, no clipping

BLOCKING SOURCES:
  ✅ Team roster: 7 members verified
  ✅ GitHub Develop PRs: LIVE or FALLBACK verified
  ✅ GitHub Collection branches: LIVE or FALLBACK verified
  ✅ Commits (attribution): LIVE or FALLBACK verified
  ✅ Reviews (all states): LIVE or FALLBACK verified

═══════════════════════════════════════════════════════════
RESULT: ✅ RENDER GATE PASSED — OK to build presentation
═══════════════════════════════════════════════════════════
```

---

## PHASE 3.5: ARTIFACT PRECONDITION CHECK

**Before attempting to render/export:**

```
═══════════════════════════════════════════════════════════
ARTIFACT PRECONDITION CHECK — PHASE 3.5
═══════════════════════════════════════════════════════════

  ✅ Source artifact path selected
  ✅ Source artifact file created (exists on disk)
  ✅ File size > 0 bytes (not empty)
  ✅ HTML is well-formed (can be parsed)
  ✅ All required assets inline or embedded
  ✅ Ready for render → PPTX conversion

═══════════════════════════════════════════════════════════
If ANY check fails: STOP. Report ARTIFACT_BUILD_ERROR.
Do NOT attempt to render a non-existent or empty file.
═══════════════════════════════════════════════════════════
```

---

## PHASE 4: FINAL VERIFICATION (after slides built & rendered to PPTX)

**AI must generate and show this report:**

```
═══════════════════════════════════════════════════════════
FINAL VERIFICATION REPORT — PHASE 4: PRESENTATION READY
═══════════════════════════════════════════════════════════

SLIDES GENERATED:
  Total slides: N
  Meeting points covered: ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭
  All 7 team members shown: YES/NO
  Reporting period: [START] – [END]

DATA VERIFICATION (spot check):
  ✅ Repository SHA verified (matches origin/cleanup HEAD)
  ✅ Slide ①A: Merged PRs match GitHub (dates within period)
  ✅ Slide ①A: Card count <= 6 per physical slide (pagination rule)
  ✅ Slide ①A: If PR count > 6, continuation slides exist (①A-2, ①A-3, etc)
  ✅ Slide ①B: Collection branch PRs OR explicit omission ("0 deliveries")
  ✅ Slide ①C-①D: Open PRs with recent activity OR explicit omission
  ✅ Slide ①E: Decisions verified (see below)
  ✅ Slide ③④⑤: Team issues match GitHub status + blockers
  ✅ No PR shown twice (deduplication verified)

DECISION VERIFICATION (Slide ①E):
  ✅ Verified decisions:
     - Each decision file exists in docs/decisions/ (NOT docs/examples/decisions/)
     - Has valid decision_date field (YYYY-MM-DD format)
     - Date falls within REPORTING_PERIOD
     - status = "confirmed" (not "proposed", not "example")
     - Has "Påverkan" section (impact documented)
     - File path MUST be: docs/decisions/<id>.md (canonical source)
  
  ❌ FORBIDDEN — Examples never in presentation:
     - NEVER read from docs/examples/decisions/
     - NEVER show files marked status: "example"
     - ONLY read from canonical docs/decisions/ path
  
  ✅ Decision candidates:
     - Minimum 2 pieces of evidence (PRs or patterns)
     - Never phrased as "Teamet beslutade..." (always "Förslag på...")
     - Evidence is concrete and verifiable
     - Future impact clearly stated
     - Candidate has 2-3 per slide max
  
  ✅ If no decisions + no candidates:
     - Slide ①E omitted
     - Audit records: "Slide ①E omitted — 0 decisions, 0 candidates"

DESIGN & STRUCTURE COMPLIANCE:
  ✅ Slide ①A: 3×2 grid (6 max), soft cards, team borders
  ✅ Slide ①B-①D: Full-width stacked cards, responsive height
  
  🚨 CRITICAL — TEAM DETAIL CARDS (③④⑤):
     ✅ Slide ③④⑤: Vertically stacked compact cards (NEVER tables)
     ✅ Slide ③④⑤: Centered text horizontally
     ✅ Slide ③④⑤: Responsive height (grows with content)
     ✅ Slide ③④⑤: Identical geometry for all three teams
     ✅ Slide ③④⑤: Only team border color differs (Teal/Hot Pink/Purple)
     ❌ FAILURE if any of ③④⑤ uses PowerPoint table format
     ❌ FAILURE if any of ③④⑤ clips text
     ❌ FAILURE if geometry differs between teams
  
  ✅ Slides ②⑥-⑧⑨–⑭: COMPACT_CARD_STANDARD
     ✅ 2–3 cards per row or vertically stacked
     ✅ Soft rounded corners (12–18px)
     ✅ Responsive height (no fixed dimensions)
     ❌ FAILURE if full-width horizontal bands
     ❌ FAILURE if text clipped
     ❌ FAILURE if ⑧ rendered as table (must be compact cards)
  
  ✅ All cards: 12–18px corners, 16–20px padding, NO text clipping
  ✅ All cards: Dark navy background (#0F1830 slide, #18233D card)
  ✅ Team colors: Borders only (not backgrounds)
  ✅ Status symbols: ✅ ◐ 🔴 ? consistent meaning everywhere
  ✅ Typography (WCAG 2.2 AA compliant): 
     - Headers 28pt BOLD
     - Body text 14pt regular (min — per ACCESSIBILITY_NEURODIVERSITY)
     - Metadata 13pt regular (min)
     ❌ FAILURE if body <14pt or metadata <13pt
  ✅ Colors: Team borders correct, status symbols clear, WCAG 4.5:1 contrast

VISUAL QUALITY (rendered PPTX):
  ✅ All text fully visible (no clipping or overflow)
  ✅ Responsive card heights working correctly
  ✅ Whitespace adequate (60-70% minimum)
  ✅ Slide density reasonable (split if compressed)
  ✅ Team detail cards (③④⑤): Compact vertical layout, centered text
  ✅ Team detail cards: Different heights acceptable (content-driven)
  ✅ Team detail cards: Frontend/Backend/Native use same card system

CONTENT CHECK:
  ✅ All 7 team members appear with work or "available" marker
  ✅ Review work shown (not "available" if actively reviewing)
  ✅ Blockers clearly marked with reason
  ✅ No unverified GitHub entity numbers
  ✅ No percentages, estimates, or forecasts without source
  ✅ No AI instructions or process descriptions on slides

SOURCE PROVENANCE:
  ✅ Framsida footer shows verified sources + timestamp
  ✅ All GitHub data LIVE (not cached/snapshot)
  ✅ Fallbacks used only if primary unavailable (clearly marked ⚠️)

═══════════════════════════════════════════════════════════
RESULT: ✅✅✅ PRESENTATION VERIFIED & READY TO SHOW
═══════════════════════════════════════════════════════════
```

---

## Key Principle

**AI generates reports, not presentations, until Phase 3 report shows OK.**

If any report fails → STOP, don't proceed to next phase.

---

**Version:** 2.0 (Reports only; phase structure in SYSTEM_CONTRACT.yaml)  
**Last updated:** 2026-09-15
