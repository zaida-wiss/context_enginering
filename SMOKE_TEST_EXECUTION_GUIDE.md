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

### Step 3: Give Fresh AI Minimal Instruction (Realistic Test)

**The test is most valuable when the AI gets the LEAST help.**

Give ONLY this:

```
Read this repository:
https://github.com/zaida-wiss/context_enginering/blob/cleanup/README.md

Create the presentation for Monday's team meeting (09:00 Stockholm time).

That's the task. Follow what the repo tells you to do.
```

**That's it. Nothing else.**

No instructions about:
- Entry points
- Pipeline steps  
- Gate logging
- What to verify

Just: README link + task.

This tests whether README alone is sufficient to guide you through the entire system.
```

### Step 4: Wait for Test Completion
The fresh AI will:
- Read through authority files
- Collect data
- Pass or fail gates
- Report detailed results

**Do NOT help, guide, or correct the AI.** If it fails, that's data about what needs fixing.

### Step 5: Evaluate Against Concrete Criteria

**Do NOT just read what the AI claims. Actually look at the presentation.**

Verify these real, visual/data criteria:

**Data Completeness:**
- [ ] All 7 team members checked (or marked "no activity")?
- [ ] Team collection branches actually scanned (develop, Java-Development-Environment, etc)?
- [ ] Clear distinction: merged to develop vs pågår work?
- [ ] Verified activity for Zaida, Erik, Björn, Henrik, Pär, Rasha, Tomac?
- [ ] No unverified data fabricated (marked as "unverified" or "no data" instead)?

**Slide ①A (Merged):**
- [ ] Chronological order (oldest first)?
- [ ] Balanced across teams?
- [ ] No duplicates (same work on multiple slides)?

**Slide ①D (Pågår denna vecka: Team-based):**
- [ ] Team separation clear (Frontend | Backend | Native)?
- [ ] Active PRs and issues shown per team?

**Slide ①E (Pågår denna vecka: Cross-team + Backlog):**
- [ ] Cross-team work clearly separated from backlog?
- [ ] LEVEL 4 (assigned without branch) shown in section B?

**Visual Design:**
- [ ] Cards rounded (corners visible, not sharp rectangles)?
- [ ] Padding inside cards (text doesn't touch borders)?
- [ ] Responsive height (cards grow with content)?
- [ ] No text clipping or truncation?
- [ ] Dark navy background (#0F1830)?
- [ ] Soft appearance (calm, not technical/boxy)?

**Slide ⑥A (Blockers):**
- [ ] Actual dependency diagram (not just text list)?
- [ ] Nodes with arrows (pilar showing blocking)?
- [ ] Status markers visible (✅ ◐ ⏳ 🔴)?
- [ ] Flow direction clear?

**Colors:**
- [ ] Team colors (teal/hot pink/purple) on borders only?
- [ ] Status symbols (✅ ◐ 🔴) shown, not colored boxes?
- [ ] No overlap of team color with status color?
- [ ] Green ≠ team, only ✅ status?

**Rendering:**
- [ ] Presentation actually rendered to PPTX or viewable format?
- [ ] AI visually checked every slide (not just generated)?
- [ ] Issues with layout/spacing noted?

**If ANY of these fails:**
```
❌ Evaluate: Is this a data problem or a rule problem?

If DATA problem (missing person, branch not scanned):
  → Fix data acquisition in SYSTEM_CONTRACT or DATA_ACQUISITION_CONTRACT
  → Re-test with fresh session

If RULE problem (README didn't explain how to do X):
  → Fix README or authority files to be clearer
  → Re-test with fresh session

If DESIGN problem (rule exists but AI didn't follow it):
  → Make rule more explicit/clearer in VISUAL_DESIGN
  → Re-test with fresh session

Do NOT: Manually fix the presentation. That's not a pass.
```

**If ALL criteria pass:**
```
✅ System is self-contained
✅ README sufficient to guide AI
✅ All rules followed without help
✅ Presentation actually follows specs
→ Merge cleanup → main is safe
```

---

## 📋 Expected Smoke Test Output

The fresh AI should produce a **complete presentation artifact** (PPTX or viewable format).

The test output is the presentation itself — not a log or report.

**To evaluate:**
1. Open/view the presentation
2. Check it against the 11 concrete criteria above
3. Document what passes and what fails
4. If all pass: system is ready
5. If any fail: identify the root cause and fix it

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

## ⚠️ The Test Must Be Realistic

This test simulates real usage. Keep it honest:

- ❌ Do NOT use prior conversation context from cleanup work
- ❌ Do NOT give extra instructions beyond "README link + task"
- ❌ Do NOT help the AI if it gets stuck
- ❌ Do NOT fix issues manually in the presentation
- ❌ Do NOT claim PASS because AI says so — verify visually
- ❌ Do NOT modify the system to make the test pass

**The point:**
If the system requires special instructions or help to work, it's not ready.
If the README alone doesn't guide the AI, the README needs fixing.
If rules aren't followed, the rule needs to be clearer.

This is what real usage looks like: user gives task, system executes or fails.

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
