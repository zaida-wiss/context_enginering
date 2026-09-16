---
name: smoke_test_execution_guide
description: Instructions for running SMOKE_TEST.md — must be executed in FRESH AI session with zero prior context
metadata:
  version: 1.0
  date: 2026-09-16
  prerequisite: Fresh AI session only (no context from prior cleanup work)
  purpose: Prove system works end-to-end in isolation
---

# 🧪 SMOKE TEST EXECUTION GUIDE

## ⚠️ CRITICAL: FRESH SESSION REQUIRED

**This test MUST be run in a NEW AI session with ZERO context from the cleanup-branch development work.**

Why? We need to prove that a cold-start AI, given only the instructions and the cleanup-branchen repository, can:
1. Read README
2. Follow authority hierarchy
3. Collect data correctly
4. Apply all rules
5. Generate a presentation
6. Pass all gates

**without help, hints, or prior context.**

---

## 🎯 How to Run This Test

### Step 1: Start Fresh Session
```
Open new Claude Code session (completely new, no context carried over)
Do NOT load previous conversation or memory
```

### Step 2: Set Repository and Branch
```bash
cd /Users/zaidawiss/Desktop/projekt/context_enginering
git checkout cleanup
git log --oneline -3  # verify you're on cleanup branch
```

### Step 3: Give Fresh AI This Instruction
```
You are starting cold on the cleanup-branchen of context_enginering.

Read the file: README.md (root)
Follow the entry point for: "Jag skapar en PRESENTATION"
Execute the full presentation-generation pipeline exactly as specified.

Your task:
1. Generate a Monday meeting presentation for next week's team meeting
2. Follow ALL system instructions and gates
3. Log EVERY decision and gate result (use SMOKE_TEST.md as template)
4. Generate a presentation artifact when ready
5. Report PASS/FAIL with details

Failure criteria:
- File read from wrong branch
- Any gate failed without explanation
- Data gaps or fabricated information
- Design violations
- Manual corrections needed
- Presentation not delivered

Success criteria:
- All files read from cleanup-branchen only
- All gates PASS
- Presentation generated without errors
- NO manual corrections needed
- Execution log complete
```

### Step 4: Wait for Test Completion
The fresh AI will:
- Read through authority files
- Collect data
- Pass or fail gates
- Report detailed results

**Do NOT help, guide, or correct the AI.** If it fails, that's data about what needs fixing.

### Step 5: Analyze Results

**If test PASSES:**
```
✅ System is production-ready
✅ All gates work correctly
✅ All rules are consistent
✅ Fresh AI can execute without help
→ Merge cleanup → main is safe
```

**If test FAILS:**
```
❌ Note WHICH gate failed and why
❌ Note ANY file it read from wrong branch
❌ Note ANY rule violation or ambiguity
→ Fix the revealed issue on cleanup
→ Run smoke test again (fresh session)
→ Repeat until PASS
```

---

## 📋 Expected Smoke Test Output

The fresh AI should produce something like this:

```
EXECUTION LOG — cleanup-branchen smoke test
===========================================

BRANCH INHERITANCE CHECK
✅ README read from: cleanup
✅ SYSTEM_CONTRACT.yaml read from: cleanup
✅ SLIDE_DETAIL_SPEC.md read from: cleanup
✅ DATA_ACQUISITION_CONTRACT.yaml read from: cleanup
✅ VISUAL_DESIGN_MANDATORY.md read from: cleanup
✅ RENDER_GATE_CHECKLIST.md read from: cleanup
✅ All files from SAME branch (no jump to main)

EXECUTION RECEIPT GATE
✅ Files verified: [list]
✅ Authority hierarchy verified
✅ Status: PASS

DATA ACQUISITION GATE
✅ Merged PRs found: N (from GitHub)
✅ Active issues found: N (from active work detection)
✅ Team branches scanned: [develop, Java-Development-Environment, ...]
✅ Status: PASS

DATA AUDIT GATE
✅ Team checksums aligned
✅ No deduplication violations
✅ Status: PASS

RENDER GATE CHECKS
✅ WCAG 2.2 AA compliance: PASS
✅ Color semantics: PASS
✅ No text box borders: PASS
✅ GitHub entity provenance: PASS
✅ Code inspection (pågår): PASS
✅ Soft card surfaces: PASS
✅ Dependency diagrams: PASS
✅ Status: PASS

PRESENTATION GENERATED
✅ Format: PPTX
✅ Slides: ①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭
✅ Status: DELIVERED

FINAL RESULT: ✅ PASS
- All gates passed
- No manual corrections needed
- Fresh AI successfully generated valid presentation
- System is production-ready
```

---

## 🚀 What Happens After Smoke Test

### If PASS ✅
```
1. Document the successful run
2. Note any minor issues found (even if not blockers)
3. Merge cleanup → main
4. Tag the merge commit
5. Update project board
```

### If FAIL ❌
```
1. Document EXACTLY what failed
2. Which gate? Which file? Which rule?
3. Fix the issue on cleanup-branchen
4. Commit the fix
5. Push to cleanup
6. Run smoke test AGAIN (fresh session)
7. Repeat until PASS

Do NOT:
- Manually override gates
- Modify the test
- Use old context
- Patch around the issue
```

---

## 📌 Key Points for Fresh AI Running Test

**You will be instructed to:**
1. Start from README.md (cleanup-branchen)
2. Follow "Jag skapar en PRESENTATION" entry point
3. Read files as specified
4. Execute gates
5. Log everything

**What this proves:**
- Repository ref policy works (no branch jumping)
- Authority hierarchy is clear and followable
- Data acquisition is complete
- All gates are consistent
- System works in isolation (no special help needed)

**What it does NOT test:**
- Actual GitHub API access (tests use mock or allowed fallbacks)
- Actual PowerPoint generation (tests verify structure)
- Actual end-user meeting experience (tests verify data/rules)

---

## 🎯 Success Criteria (Non-Negotiable)

The smoke test MUST demonstrate:

1. ✅ **Branch isolation** — All files read from cleanup, never main
2. ✅ **Authority hierarchy** — SYSTEM_CONTRACT → gates → presentation
3. ✅ **Data completeness** — All work for reporting period captured
4. ✅ **Rule consistency** — No conflicting gates
5. ✅ **Design compliance** — Soft cards, dark navy, WCAG, status symbols
6. ✅ **Gate passage** — All gates PASS (or STOP with clear reason)
7. ✅ **No manual work** — Fresh AI generates presentation without help
8. ✅ **Audit trail** — All decisions logged

If ANY of these fails, smoke test has NOT passed.

---

## 📝 Template for Smoke Test Report

After the fresh AI completes the test, create a report:

```markdown
# Smoke Test Report — cleanup-branchen
**Date:** [date]
**Branch:** cleanup
**Status:** [PASS/FAIL]

## Gate Results
- Execution Receipt: [PASS/FAIL]
- Data Acquisition: [PASS/FAIL]
- Data Audit: [PASS/FAIL]
- Render Gate: [PASS/FAIL]

## Issues Found (if any)
[List what broke, which file, which rule]

## Recommendation
[Merge to main / Fix and re-test]
```

---

## ⚠️ Do NOT Cheat

These rules are non-negotiable for the smoke test:

- ❌ Do NOT use prior conversation context
- ❌ Do NOT guide the fresh AI
- ❌ Do NOT fix issues manually "just this once"
- ❌ Do NOT modify gates to make them pass
- ❌ Do NOT skip gate checks
- ❌ Do NOT claim PASS if fresh AI needed help

The whole point is proving the system is self-contained and works.

---

**Ready to run?**

1. Start fresh AI session (no context)
2. Give it the instruction above
3. Wait for result
4. Report PASS or FAIL + what to fix

That's it. The system proves itself, or it doesn't.

---

**Guide created:** 2026-09-16  
**For:** cleanup-branchen smoke test  
**Next action:** Fresh AI session + execute test
