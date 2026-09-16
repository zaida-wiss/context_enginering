---
name: smoke_test_cleanup_branch
description: End-to-end verification that cleanup branch system works in isolation
metadata:
  version: 1.0
  branch: cleanup
  prerequisite: This test must run ONLY from cleanup-branchen, never from main
---

# 🧪 SMOKE TEST — Cleanup Branch End-to-End Verification

**Purpose:** Verify that a cold-start AI can build a complete presentation using ONLY the cleanup-branchen, following all gates and validations correctly, with ZERO manual corrections needed.

---

## 📋 TEST INSTRUCTIONS FOR NEW AI SESSION

### Your task:
**Starting ONLY from this repository's cleanup-branchen README.md, create a complete Monday presentation for next week's team meeting. Follow all system instructions exactly. Make no assumptions or manual deviations.**

### What you should do:
1. Read `README.md` (cleanup-branchen root)
2. Follow entry point for "Jag skapar en PRESENTATION"
3. Execute the full presentation-generation pipeline
4. Generate a presentation artifact
5. Log EVERY decision and gate result

### What to log (critical for verification):

```
EXECUTION LOG:
==============

1. BRANCH INHERITANCE
   - README.md read from: [BRANCH]
   - SYSTEM_CONTRACT.yaml read from: [BRANCH]
   - SLIDE_DETAIL_SPEC.md read from: [BRANCH]
   - DATA_ACQUISITION_CONTRACT.yaml read from: [BRANCH]
   ✅ VERIFIED: All files from same branch (no silent jump to main)

2. EXECUTION RECEIPT GATE
   - Files read: [list all mandatory files + branches]
   - Status: [PASS/FAIL]
   - If FAIL: [reason]

3. DATA ACQUISITION GATE
   - Merged PRs found: [count + sample issue numbers]
   - Active issues found: [count + sample issue numbers]
   - Team branches scanned: [develop, Java-Development-Environment, others]
   - Commits collected: [count per branch]
   - Team members verified: [count/7]
   - Status: [PASS/FAIL]
   - If FAIL: [reason]

4. DATA AUDIT GATE
   - Checksums: COUNT[merged_prs], SET[unique_pr_ids], TEAM_COMPLETENESS
   - Status: [PASS/FAIL]
   - If FAIL: [reason]

5. RENDER GATE CHECKS
   - WCAG 2.2 AA compliance: [PASS/FAIL]
   - Color semantics (no team=status overlap): [PASS/FAIL]
   - No text boxes have visible borders: [PASS/FAIL]
   - GitHub entity provenance verified: [PASS/FAIL]
   - Code inspection done: [PASS/FAIL]
   - Team collection branch coverage: [PASS/FAIL]
   - Analysis layer present: [PASS/FAIL]
     - Priority ranking: [YES/NO]
     - Dependency chain: [YES/NO]
     - Team split recommended: [YES/NO]
     - Completion estimate: [YES/NO]
     - Actionable next steps: [YES/NO]
   - Status: [PASS/FAIL]
   - If FAIL: [which checks failed]

6. FINAL PRESENTATION
   - Format: [PDF/PPTX]
   - Slides generated: [count + list slide names]
   - Status: [DELIVERED/BLOCKED]

NO MANUAL CORRECTIONS MADE: [YES/NO]
```

---

## ✅ SUCCESS CRITERIA

The test **PASSES** if:
- ✅ All files read from cleanup-branchen (never main)
- ✅ execution_receipt gate PASSED
- ✅ data_audit gate PASSED
- ✅ render_gate PASSED
- ✅ Presentation generated without errors
- ✅ NO manual corrections needed from user
- ✅ ALL gates documented in execution log

The test **FAILS** if:
- ❌ Any file jumped to main branch
- ❌ Any gate failed without explanation
- ❌ User had to say "read this file too" or "fix the data"
- ❌ Design/WCAG violations found
- ❌ Presentation not generated
- ❌ Manual correction was needed

---

## 🔍 HOW TO RUN THIS TEST

1. **New AI session** (totally fresh, no context from earlier work)
2. **Start from:** cleanup-branchen root README.md
3. **Instruction:** "Follow SMOKE_TEST.md instructions"
4. **Result:** Either PASS (all gates pass, presentation delivered) or FAIL (report what broke and why)

---

## 📊 INTERPRETATION

- **PASS** → cleanup-branchen is ready to merge to main
- **FAIL** → Fix the identified issue on cleanup-branchen, re-run test

---

**Test created:** 2026-09-16  
**For branch:** cleanup  
**Purpose:** Verify end-to-end system functionality before merge to main
