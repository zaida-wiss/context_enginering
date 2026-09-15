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

### `fixtures/merged_prs_sample.json`

```json
{
  "execution_mode": "TEST_MODE",
  "merged_prs": [
    {
      "number": 42,
      "title": "Fix login flow security",
      "assignees": ["Rasha Knifdi"],
      "merged_at": "2026-09-12T14:30:00Z",
      "base": { "ref": "develop" }
    },
    {
      "number": 45,
      "title": "Update design tokens",
      "assignees": ["Björn Boman"],
      "merged_at": "2026-09-13T09:15:00Z",
      "base": { "ref": "develop" }
    }
    // ... 5+ more PRs covering all 7 team members
  ]
}
```

### `fixtures/active_issues_sample.json`

```json
{
  "execution_mode": "TEST_MODE",
  "active_issues": [
    {
      "number": 108,
      "title": "Implement rate limiting",
      "assignees": ["Erik Berglund"],
      "updated_at": "2026-09-14T10:00:00Z",
      "state": "open"
    },
    {
      "number": 112,
      "title": "Native app crash on login",
      "assignees": ["Henrik Westerlund"],
      "updated_at": "2026-09-13T16:45:00Z",
      "state": "open"
    }
    // ... more issues covering all 7 team members
  ]
}
```

---

## Test Mode Footer

All slides in TEST MODE presentations must include:

```
⚠️ TEST MODE — Fixture data. For production: use live GitHub sources.
Generated: 2026-09-15 | Commit: [SHA] | Test fixtures version: 1.0
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
- [ ] All 7 team members represented in ① Avklarat
- [ ] Modular composition created correct slides (①, ②, ③④⑤, ⑥-⑭)
- [ ] Design rules followed (28pt headers, CANONICAL LAYOUT, NPF rules)
- [ ] Render gate passed (VISUAL_DESIGN_MANDATORY verified)
- [ ] PDF delivered with TEST MODE footer
- [ ] No production data leaked into presentation

---

**Status:** Ready for testing  
**Last updated:** 2026-09-15
