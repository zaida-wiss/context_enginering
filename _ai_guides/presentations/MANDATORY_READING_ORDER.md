---
name: mandatory_reading_order
description: THE ONLY execution order for generating presentations — machine-readable contract + orchestration
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER — ORCHESTRATION + CONTRACT

## 📋 MACHINE-READABLE CONTRACT (PARSE THIS FIRST)

```yaml
presentation_contract:
  # Authority hierarchy
  orchestration_authority: this_file
  system_truth_authority: SYSTEM_CONTRACT.yaml
  content_authority: design/SLIDE_DETAIL_SPEC.md
  design_authority: design/VISUAL_DESIGN_MANDATORY.md
  data_authority: data/DATA_SOURCES.md
  verification_authority: verification/RENDER_GATE_CHECKLIST.md
  workflow_authority: verification/AI_VERIFICATION_WORKFLOW.md
  
  # Meeting definition
  meeting_type: monday_team_meeting
  reporting_period: previous_calendar_week (Monday 00:00 - Sunday 23:59 Europe/Stockholm)
  reporting_period_calculation: dynamic (never hardcoded)
  
  # Requirements
  required_team_coverage: 7/7 (all members or explicit "no activity")
  required_data_verification: FAS_1_and_FAS_2_reports_before_slides
  required_design_compliance: NPF_mandatory (Symbol + Färg + Text)
  
  # Blocking behavior
  render_gate_behavior:
    closes_on_missing_blocking_source: true
    closes_on_missing_optional_source: false
    allow_fallback_substitution: true
  
  # Data validation
  data_validation:
    - name: DATA_AUDIT_COUNT
      rule: "sum(Frontend + Backend + Native + Cross + Other) == repository_total"
      consequence: "If false → RENDER GATE FAIL"
    
    - name: DATA_AUDIT_SET
      rule: "repository_merged_pr_ids == union(all work_area IDs)"
      consequence: "If false → RENDER GATE FAIL"
    
    - name: DATA_AUDIT_UNIQUENESS
      rule: "No PR ID in multiple work_areas"
      consequence: "If false → RENDER GATE FAIL"
  
  # Forbidden content
  forbidden_on_slides:
    - progress_percentages_without_github_source
    - estimates_or_forecasts
    - ai_instructions_or_meta_commentary
    - example_data_from_documentation
    - fabricated_numbers
  
  # Files to never read
  deprecated_files_must_not_be_read:
    - PRESENTATION_FORMAT_GUIDE.md
    - PRESENTATION_CONSISTENCY_FRAMEWORK.md
    - PRESENTATION_DESIGN_SPEC.md
```

---

## 🤖 EXECUTION SEQUENCE — FOLLOW THIS EXACTLY

**This is the ONLY sequence. No variations. No alternatives.**

### STEP 1: READ AUTHORITIES (in order)
1. ✅ `SYSTEM_CONTRACT.yaml` — machine-readable system definition
2. ✅ `presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md` — what each slide contains
3. ✅ `presentations/design/VISUAL_DESIGN_MANDATORY.md` — how slides look
4. ✅ `presentations/verification/AI_VERIFICATION_WORKFLOW.md` — what you do

### STEP 2: EXECUTE FAS 1 (Data collection + identity verification)
- Fetch all BLOCKING_SOURCES (GitHub commits, PRs, issues, team roster)
- Use fallbacks if primary fails
- Generate and show: DATA_AUDIT report with triple checksums
- Stop if any BLOCKING_SOURCE + fallback fails

### STEP 3: EXECUTE FAS 2 (Render gate verification)
- Verify all 7 team members (identity-verified or explicit "no activity")
- Verify DATA_AUDIT triple checksums pass
- Generate and show: RENDER_GATE_VERIFICATION report
- If any REQUIRED check fails → STOP, do not build presentation

### STEP 4: EXECUTE FAS 3 (Build presentation)
- Build slides ONLY from DATA_AUDIT object (never re-query GitHub)
- Verify against SLIDE_DETAIL_SPEC (structure must match exactly)
- Verify against VISUAL_DESIGN_MANDATORY (design must match exactly)
- Generate and show: FINAL_VERIFICATION report

### STEP 5: DELIVER
- If all steps passed: present slides
- If any step failed: report failure + reason (do not present)

---

## 🔗 EXTERNAL SOURCES

All external data URLs are in: [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md)

**Do NOT hardcode URLs. Reference EXTERNAL_SOURCES.md instead.**

---

## 🚨 CRITICAL RULES (Non-negotiable)

```
BLOCKING_SOURCES (STOP if both primary + fallback fail):
  • GitHub commits to develop
  • GitHub merged PRs
  • GitHub issues
  • Team roster (7 members)
  → If blocked: report "RENDER GATE FAIL — [source] unavailable"

OPTIONAL_CONTEXT (never stop, always use fallback):
  • Project Board → fallback: Issues API
  • Meeting protocol → fallback: GitHub notes
  → If fallback used: show "ℹ️ [source] unavailable — using fallback"

DATA VALIDATION:
  1. COUNT checksum: sum(areas) == total
  2. SET checksum: repository_IDs == union(areas)
  3. UNIQUENESS: no PR in multiple areas
  → If ANY checksum fails: STOP

CONTENT RULES:
  • No percentages without GitHub source
  • No estimates or forecasts
  • No AI instructions on slides
  • Missing assignee shows "??" (never blocks rendering)
  • All 7 members shown (work or "no activity")

DESIGN RULES:
  • NPF mandatory: Symbol + Färg + Text
  • No tables
  • All slides per SLIDE_DETAIL_SPEC exactly
```

---

## 📋 WHAT EACH FILE OWNS (do NOT duplicate)

| File | Owns |
|------|------|
| `SYSTEM_CONTRACT.yaml` | Definitions, hard rules, checksums |
| `SLIDE_DETAIL_SPEC.md` | Content for slides ①–⑭ (only source of truth for content) |
| `VISUAL_DESIGN_MANDATORY.md` | Layout, colors, fonts, NPF rules (only source of truth for design) |
| `DATA_SOURCES.md` | All GitHub/Google URLs, fallback chains (only source of truth for data) |
| `RENDER_GATE_CHECKLIST.md` | Verification checkpoints (only source of truth for render gate) |
| `AI_VERIFICATION_WORKFLOW.md` | What AI does step-by-step (only source of truth for process) |
| **This file** | Orchestration + contract (only source of truth for order) |

**RULE: If a rule appears in two files, the authoritative file listed above wins. Remove the duplicate.**

---

**Version:** 3.0 (Refactored: removed contradictions, added machine-readable contract)  
**Status:** PRODUCTION — THE ONLY execution order for presentations  
**Last updated:** 2026-09-15
