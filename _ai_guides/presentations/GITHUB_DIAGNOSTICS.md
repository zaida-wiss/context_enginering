---
name: github_diagnostics
description: Isolated GitHub connectivity tests to diagnose data acquisition failures
metadata:
  type: diagnostic
  version: 1.0
---

# 🔧 GITHUB DIAGNOSTICS — Isolated Testing

**Purpose:** Isolate which GitHub operation fails and why.

GitHub-connectorn fungerar för context_enginering-repot, men avanza-team1-repot får DNS-fel. Denna diagnostik isolerar problemet.

---

## Test 1: Context Engineering Repo (Baseline — Known Working)

**Test:** Can you read README.md from this repo?

```
Repository: https://github.com/zaida-wiss/context_enginering
Path: README.md
Method: GitHub connector read
Expected: SUCCESS (this is the baseline that works)
```

**If this passes:** GitHub connector is functional. Problem is specific to avanza-team1 or its endpoints.

---

## Test 2: Avanza Team 1 — Repo Metadata

**Test:** Can you read basic repo metadata?

```
Repository: https://github.com/chas-challenge-2026/avanza-team1
Endpoint: GET /repos/chas-challenge-2026/avanza-team1
Method: GitHub API
Expected: SUCCESS (repo info, license, etc)
Record: HTTP status, response time, any error message
```

**If this fails with DNS:** Problem is repo-level access, not endpoint-specific.  
**If this passes but PR endpoint fails:** Problem is endpoint-specific rate limiting or restriction.

---

## Test 3: Avanza Team 1 — Merged PRs (Canonical Endpoint)

**Test:** Can you fetch merged PRs?

```
Repository: https://github.com/chas-challenge-2026/avanza-team1
Endpoint: GET /repos/chas-challenge-2026/avanza-team1/pulls?state=closed&base=develop&per_page=100
Method: GitHub API
Expected: SUCCESS (list of merged PRs)
Record: HTTP status, number of PRs returned, any error message
```

**If this fails:** Record exact error (DNS, 403, 429 rate limit, timeout, etc).

---

## Test 4: Avanza Team 1 — Web Fallback

**Test:** Can you read GitHub web page?

```
URL: https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is:pr+is:merged
Method: Raw HTML fetch
Expected: SUCCESS (web page loads, contains PR data)
Record: Page status, whether PR data can be extracted
```

**If this fails:** Record exact error (DNS, 403, timeout, page structure changed).

---

## Test 5: Avanza Team 1 — Open Issues

**Test:** Can you fetch open issues?

```
Repository: https://github.com/chas-challenge-2026/avanza-team1
Endpoint: GET /repos/chas-challenge-2026/avanza-team1/issues?state=open&per_page=100
Method: GitHub API
Expected: SUCCESS (list of open issues)
Record: HTTP status, number of issues returned, any error message
```

---

## Diagnostic Output Format

For each test, record:

```
TEST: [name]
Status: SUCCESS | FAILURE
HTTP Status: [200 | 403 | 404 | 429 | 500 | null/DNS-error]
Error Message: [exact error text]
Response Time: [ms, if available]
Attempted At: [ISO 8601 timestamp]
Attempted Via: [GitHub API | GitHub web | Connector | other]
```

---

## Interpretation Guide

| Test 1 | Test 2-5 | Likely Problem |
|--------|----------|-----------------|
| ✅ PASS | ❌ FAIL DNS | avanza-team1 repo or entire host unreachable from ChatGPT |
| ✅ PASS | ✅ PASS repo metadata | Problem is endpoint-specific (rates, perms, structure) |
| ✅ PASS | ✅ PASS API | Problem is web fallback (page structure, selector, timeout) |
| ✅ PASS | 403/429 | Rate limiting or permission issue (GitHub token, API quota) |

---

## Next Steps After Diagnosis

**If repo unreachable:** Possible GitHub/CloudFlare blocking ChatGPT IPs. May need manual intervention or alternative data source.

**If endpoint-specific:** May be GitHub API changes, rate limiting, or permission scoping. Can test pagination, different filters, or authentication.

**If web fallback fails:** May be page structure changed, selector mismatch, or timeout. Can test with alternative scraping method.

**If auth-related (401/403):** Verify GitHub token validity, connector configuration, and repository permissions.

---

**Status:** Ready to run  
**Last updated:** 2026-09-15
