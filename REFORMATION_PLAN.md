# 🔧 REFORMATION PLAN — Systemet blir mekaniskt och klart

**Feedback från ChatGPT:** Systemet har för många överlappande instruktioner och motsägelser. Fokus: gör det linjärt, maskinläsbart, och motsägelsefritt.

**Status:** Planning & Implementation
**Estimated work:** 2-3 hours

---

## PRIORITY 1 — YAML Contract (Maskinläsbar struktur)

**Current state:** Långt naturligt språk som är svårt att tolka

**Goal:** Överst i MANDATORY_READING_ORDER.md — en YAML-block som helt definierar systemet

**What to do:**
```yaml
task: monday_meeting_presentation
version: 1.0

authoritative_sources:
  content: monday_meeting/design/SLIDE_DETAIL_SPEC.md
  visual: design/VISUAL_DESIGN_MANDATORY.md
  data_collection: monday_meeting/data/DATA_COLLECTION_MANDATORY.md
  team_roster: ../../../_memory/TEAM_ROSTER.md
  external_urls: ../../../_memory/EXTERNAL_SOURCES.md

execution_sequence:
  - step1_read_mandatory_files
  - step2_fetch_live_data
  - step3_verify_all_7_members
  - step4_build_slides
  - step5_verify_render_gate
  - step6_timestamp_and_deliver

reporting_period:
  rule: "previous Monday 00:00 → previous Sunday 23:59"
  timezone: "Europe/Stockholm"
  definition: "Not 'last 7 days' from generation time"

hard_rules:
  - never_invent_data
  - never_use_example_values_from_docs
  - merged_means_merged_to_develop_in_reporting_period
  - issue_closed_without_merge_not_equals_delivered
  - all_7_team_members_must_be_accounted_for
  - if_required_data_missing_stop_before_render
  - if_github_unreachable_report_and_stop
  - npf_design_mandatory_no_tables
  - timestamp_every_slide

definitions:
  delivered:
    - PR merged into develop during reporting period
  in_progress:
    - Open PR with recent activity (commits, comments)
    - Open issue with assignee and activity
  branch_only:
    - Branch without PR or issue = NOT work status
  commit_only:
    - Commit proves work happened but NOT delivery status

deprecated_files:
  - PRESENTATION_FORMAT_GUIDE.md (DELETE OR ARCHIVE)
  - PRESENTATION_CONSISTENCY_FRAMEWORK.md (DELETE OR ARCHIVE)
  - PRESENTATION_DESIGN_SPEC.md (DELETE OR ARCHIVE)
  - (ALL references removed from active instructions)

fact_vs_assessment:
  fact: "Comes only from verified live source (GitHub, etc)"
  derived: "Mechanically calculated from FACT (e.g., count)"
  assessment: "AI analysis/interpretation — NEVER presented as fact"
  rule: "Assessment can never be shown as status"
```

**Files to create:**
- [ ] `SYSTEM_CONTRACT.yaml` (in root of presentations/)

**Files to update:**
- [ ] `MANDATORY_READING_ORDER.md` (add YAML at top)

---

## PRIORITY 2 — Clean Deprecated Files

**Current state:** PRESENTATION_FORMAT_GUIDE referenced in 3+ places, creating confusion

**Goal:** Either DELETE or ARCHIVE every deprecated file, remove ALL references

**What to do:**

1. **Search for all references:**
   - [ ] PRESENTATION_FORMAT_GUIDE.md
   - [ ] PRESENTATION_CONSISTENCY_FRAMEWORK.md
   - [ ] PRESENTATION_DESIGN_SPEC.md

2. **Decision per file:**
   - [ ] DELETE if truly unused
   - [ ] Or ARCHIVE as `.archived/OLD_NAME.md` with comment: "ARCHIVED — do not use. See SLIDE_DETAIL_SPEC.md instead."

3. **Remove ALL references** from:
   - [ ] MANDATORY_READING_ORDER.md
   - [ ] AI_VERIFICATION_WORKFLOW.md
   - [ ] SLIDE_DETAIL_SPEC.md
   - [ ] Any other file mentioning them

**Files to update:**
- [ ] MANDATORY_READING_ORDER.md (remove all refs)
- [ ] AI_VERIFICATION_WORKFLOW.md (remove all refs)
- [ ] Any file with deprecated file mention

---

## PRIORITY 3 — Single Linear Execution Sequence

**Current state:** Multiple overlapping descriptions (STEG 0-4, then FASE 1-3, then separate workflow)

**Goal:** ONE clear sequence from start to finish

**What to do:**

Replace all multi-phase descriptions with ONE sequence:

```
START
  → Step 1: Read mandatory files (MANDATORY_READING_ORDER, SLIDE_DETAIL_SPEC, TEMPLATE_REFERENCE)
  → Step 2: Fetch LIVE data (5 GitHub URLs from DATA_COLLECTION_MANDATORY)
  → Step 3: Verify all 7 members accounted for
  → Step 4: Build slides following SLIDE_DETAIL_SPEC exactly
  → Step 5: Verify design follows VISUAL_DESIGN_MANDATORY
  → Step 6: Verify render-gate checklist
  → Step 7: Timestamp every slide with data-fetch time
  → Step 8: Deliver presentation
DONE
```

**Move everything else to separate files:**
- Design details → VISUAL_DESIGN_MANDATORY.md
- Data fetching → DATA_COLLECTION_MANDATORY.md
- Verification → RENDER_GATE_CHECKLIST.md

**Files to update:**
- [ ] MANDATORY_READING_ORDER.md (replace with 8-step sequence)

---

## PRIORITY 4 — Authoritative Slide Spec Only

**Current state:** Slide info in SLIDE_DETAIL_SPEC, PRESENTATION_STRUCTURE, WEEKLY_PROGRESS_MODEL

**Goal:** ONE file determines slides. Others only reference it.

**What to do:**

- [ ] SLIDE_DETAIL_SPEC.md = only source for slide content
- [ ] PRESENTATION_STRUCTURE.md = only says WHY points exist and ORDER, not WHAT they contain
- [ ] Remove duplicate slide descriptions from all other files
- [ ] Add header to SLIDE_DETAIL_SPEC: "This file is authoritative. If other files describe slide content, this wins."

**Files to update:**
- [ ] PRESENTATION_STRUCTURE.md (remove slide content, keep structure)
- [ ] WEEKLY_PROGRESS_MODEL.md (if it exists)
- [ ] Any other file with slide descriptions

---

## PRIORITY 5 — Mechanistic GitHub Status Definitions

**Current state:** "Pågår" is vague, "branch ensam" gets misinterpreted as work

**Goal:** Clear rules that prevent misclassification

**What to do:**

Add to DATA_COLLECTION_MANDATORY.md:

```
GITHUB STATUS DEFINITIONS (mechanical, no interpretation):

DELIVERED:
  ✅ PR merged to develop in reporting period
  ✅ Issue linked to merged PR
  ❌ Closed issue without merge = NOT delivered
  ❌ Branch name alone = NOT delivered

IN PROGRESS:
  ◐ Open PR with commits this week
  ◐ Open issue with assignee + recent activity
  ◐ Branch with commits but no PR yet
  ❌ Old branch with no recent commits = NOT in progress
  ❌ Comment alone = NOT activity (must be commit or PR update)

NOT A STATUS:
  ❌ Branch existence
  ❌ Single commit
  ❌ Issue comment without assignee
```

**Files to update:**
- [ ] DATA_COLLECTION_MANDATORY.md (add definitions section)

---

## PRIORITY 6 — Remove Example Data That Looks Real

**Current state:** AI_VERIFICATION_WORKFLOW has sample reports with real team names, PR numbers

**Goal:** Replace with clear placeholders AI won't copy

**What to do:**

Search for example sections and replace:
```
BEFORE: "PR #90 Login page · Zaida Wiss · ✓ DONE · 2026-09-13"
AFTER: "PR <PR_NUMBER> <ISSUE_TITLE> · <TEAM_MEMBER> · <STATUS> · <MERGE_DATE>"

OR mark blocks:
[NON-DATA EXAMPLE — DO NOT COPY VALUES INTO OUTPUT]
```

**Files to update:**
- [ ] AI_VERIFICATION_WORKFLOW.md (sanitize all examples)

---

## PRIORITY 7 — Fix Human Verification Contradiction

**Current state:** "AI does everything" vs "human reviews and iterates"

**Goal:** One clear workflow

**Decision:** AI generates complete presentation. Human review optional after.

**What to do:**

- [ ] Update MANDATORY_READING_ORDER: "AI renders presentation. Optional: human quality review after."
- [ ] Remove "human must confirm data" language
- [ ] Keep "human can request changes after delivery"

**Files to update:**
- [ ] MANDATORY_READING_ORDER.md (clarify AI-solo workflow)

---

## PRIORITY 8 — Fix SLIDE_DETAIL_SPEC Link (if broken on GitHub)

**Current state:** ChatGPT reported 404 on link

**Goal:** Verify link works from GitHub

**What to do:**

- [ ] Test link: `monday_meeting/design/SLIDE_DETAIL_SPEC.md` from presentations/
- [ ] If broken, fix path in MANDATORY_READING_ORDER
- [ ] Verify all cross-links work

**Files to update:**
- [ ] MANDATORY_READING_ORDER.md (if links need fixing)

---

## IMPLEMENTATION ORDER

1. **First:** Create SYSTEM_CONTRACT.yaml + add to MANDATORY_READING_ORDER
2. **Second:** Clean deprecated files and remove all references
3. **Third:** Replace multi-phase workflow with 8-step sequence
4. **Fourth:** Make SLIDE_DETAIL_SPEC only source
5. **Fifth:** Add GitHub status definitions
6. **Sixth:** Sanitize example data
7. **Seventh:** Fix human verification language
8. **Eighth:** Verify all links

---

**Next:** Start with PRIORITY 1 — Create SYSTEM_CONTRACT.yaml
