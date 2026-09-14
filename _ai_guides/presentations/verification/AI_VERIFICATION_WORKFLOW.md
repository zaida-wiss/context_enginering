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

## PHASE 2: RENDER GATE VERIFICATION

**AI must generate and show this report:**

```
═══════════════════════════════════════════════════════════
RENDER GATE VERIFICATION — PHASE 2
═══════════════════════════════════════════════════════════

DATA_AUDIT CHECKSUMS:
  ✅ COUNT: sum(Frontend + Backend + Native + Cross + Other) == repository_total
  ✅ SET: repository_merged_pr_ids == union(all work_areas)
  ✅ UNIQUENESS: No PR ID in multiple work_areas

TEAM COVERAGE:
  ✅ All 7 members identity-verified or marked "no activity"

BLOCKING SOURCES:
  ✅ Team roster: LIVE or FALLBACK verified
  ✅ GitHub Issues/PRs: LIVE or FALLBACK verified
  ✅ Commits: LIVE or FALLBACK verified

═══════════════════════════════════════════════════════════
RESULT: ✅ RENDER GATE PASSED — OK to build presentation
═══════════════════════════════════════════════════════════
```

---

## PHASE 3: FINAL VERIFICATION (after slides built)

**AI must generate and show this report:**

```
═══════════════════════════════════════════════════════════
FINAL VERIFICATION REPORT — PHASE 3: PRESENTATION READY
═══════════════════════════════════════════════════════════

SLIDES GENERATED:
  Total slides: N
  Meeting points covered: ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭
  All 7 team members shown: YES/NO

DATA VERIFICATION (spot check):
  ✅ Slide X: Data from GitHub, dates match merge-dates
  ✅ Slide Y: Issues match GitHub status
  ... (key slides verified)

DESIGN COMPLIANCE:
  ✅ NPF rules followed (Symbol + Färg + Text)
  ✅ No tables (accessibility)
  ✅ Whitespace adequate
  ✅ Colors semantic (status-based)

FORBIDDEN CONTENT CHECK:
  ✅ No percentages without source
  ✅ No AI instructions on slides
  ✅ No estimates/forecasts
  ✅ No unverified names

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
