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
  ✅ Slide ③④⑤: Table format (issue-status-blockers)
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
  ✅ Slide ①A: Merged PRs match GitHub (dates within period)
  ✅ Slide ①B: Collection branch PRs identified (if any)
  ✅ Slide ①C-①D: Open PRs with recent activity
  ✅ Slide ③④⑤: Team issues match GitHub status + blockers
  ✅ No PR shown twice (deduplication verified)

DESIGN & STRUCTURE COMPLIANCE:
  ✅ Slide ①A: 3×2 grid (6 max), soft cards, team borders
  ✅ Slide ①B-①D: Full-width stacked cards, responsive height
  ✅ Slide ③④⑤: Table format (Issue | Assignee | Status | Blockers)
  ✅ All cards: 12–18px corners, 16–20px padding, NO text clipping
  ✅ All cards: Dark navy background #0F1830, soft appearance
  ✅ Team colors: Borders only (not backgrounds)
  ✅ Status symbols: ✅ ◐ 🔴 ? consistent meaning everywhere
  ✅ Typography: Headers 28pt BOLD, body 13pt regular, metadata 12pt
  ✅ Colors: Team borders correct, status symbols clear, WCAG 4.5:1 contrast

VISUAL QUALITY (rendered PPTX):
  ✅ All text fully visible (no clipping or overflow)
  ✅ Responsive card heights working correctly
  ✅ Whitespace adequate (60-70% minimum)
  ✅ Slide density reasonable (split if compressed)

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
