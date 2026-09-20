---
name: test_mode
description: Explicit test-mode with fixtures for verifying success path without live GitHub/Sheets
metadata:
  type: process
  critical: false
  version: 1.0
---

# 🧪 TEST MODE — Fixture-Based Testing

**TEST MODE is used ONLY to verify the success path (modular composition through delivery) without live GitHub/Sheets access.**

⚠️ **CRITICAL RULES:**

- ❌ **TEST MODE CANNOT BE ACTIVATED IMPLICITLY** — requires explicit flag in prompt
- ❌ **Fixtures are NEVER production fallback** — if real sources fail, STOP (do not use fixtures as substitute)
- ✅ **Test mode ONLY when explicitly requested by user** with keyword "test", "fixture", "mock-data", or "TEST_MODE"

---

## How to Activate TEST MODE

**User must explicitly request test mode:**

```
Skapa en presentation till måndagsmötet. Använd TEST_MODE.

(OR)

Skapa en presentation till måndagsmötet med test-fixtures.

(OR)

TEST_MODE: kör presentationen med mock-data för merged_prs och active_issues.
```

**If user does NOT explicitly mention test/fixture/mock:** use PRODUCTION MODE (require live sources).

---

## Test Mode Behavior

When explicitly requested:

1. **execution_receipt** — records TEST_MODE activation
2. **step_2 (Fetch Data)** — uses fixtures from `fixtures/merged_prs_sample.json` and `fixtures/active_issues_sample.json`
3. **DATA_ACQUISITION_RECEIPT** — records source as "FIXTURE (test mode)" with status SUCCESS
4. **DATA_AUDIT** — checksums verify fixture data
5. **Modular composition** — builds slides from fixture data
6. **Render gate** — verifies visual design
7. **Delivery** — exports PDF with footer note: "⚠️ This presentation was generated in TEST MODE with fixture data. For production, use live GitHub/Sheets sources."

---

## Fixture Data Structure

The canonical fixture payloads live in:

- `fixtures/merged_prs_sample.json`
- `fixtures/active_issues_sample.json`

They use deterministic **synthetic identities, teams, dates and work items**. Do not duplicate fixture payloads in this guide; read the fixture files directly so documentation cannot drift from the test data.

Fixture coverage is defined by the fixture metadata, not by any real project's roster.

---

## Test Mode Footer

All slides in TEST MODE presentations must include:

```
⚠️ TEST MODE — Fixture data. For production: use live GitHub sources.
Generated: [runtime date] | Commit: [SHA] | Test fixtures: canonical fixture files
```

---

## Production Mode (Default)

If user does NOT request TEST_MODE:

1. Use PRODUCTION MODE
2. Require live sources: GitHub API, GitHub web, Google Sheets
3. **STOP if any required source fails** (do not fall back to fixtures)
4. Report DATA_ACQUISITION_RECEIPT with real source diagnostics

---

## Test Checklist (after running TEST_MODE presentation)

After TEST_MODE completes, verify:

- [ ] Presentation rendered successfully (no STOP at gates)
- [ ] Synthetic fixture identities represented according to the fixture metadata/coverage
- [ ] Modular composition created correct slides (①, ②, ③④⑤, ⑥-⑭)
- [ ] Design rules followed (28pt headers, CANONICAL LAYOUT, NPF rules)
- [ ] Render gate passed (VISUAL_DESIGN_MANDATORY verified)
- [ ] PDF delivered with TEST MODE footer
- [ ] No production data leaked into presentation

---

**Status:** Ready for testing  
**Last updated:** 2026-09-20
