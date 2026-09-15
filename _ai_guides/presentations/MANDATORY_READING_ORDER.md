---
name: mandatory_reading_order
description: THE ONLY instruction — read and follow SYSTEM_CONTRACT.yaml
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER

## 🚨 EXECUTION ENTRY POINT

**You are here because a user asked for a presentation.**

Follow this order exactly. Do not skip.

---

## 1️⃣ READ SYSTEM_CONTRACT.yaml

**Location:** [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml)

This file contains:
- Authority hierarchy (who owns what)
- Execution sequence (step-by-step actions)
- All gates and their pass/fail criteria
- Data validation rules
- Delivery rules (PDF default, PPTX if requested)

**Action:** Read SYSTEM_CONTRACT.yaml in full before proceeding.

---

## 2️⃣ FOLLOW EXECUTION_SEQUENCE FROM SYSTEM_CONTRACT.yaml

**Location:** `execution_sequence` section in SYSTEM_CONTRACT.yaml

The execution_sequence tells you exactly what to do next. Follow it step by step. Do not skip. Do not deviate.

**Next step after this file:** Go to SYSTEM_CONTRACT.yaml and begin `step_1`.

---

## REGISTERED DATA SOURCES & ACCESS PATHS

**For presentations, data comes from these sources in this order:**

### Required Dataset 1: team_roster
- **Source:** GITHUB_TEAM_ROSTER (local file)
- **Access method:** local_file
- **Action:** Read _memory/TEAM_ROSTER.md
- **On success:** Continue to next dataset
- **On missing:** STOP (cannot proceed without team identity)

### Required Dataset 2: merged_prs
- **Source:** GITHUB_MERGED_PRS
- **Access method:** github_rest_api
- **Canonical URL:** https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?state=closed&base=develop&per_page=100
- **Preferred tool:** GitHub Connector (or any available tool implementing GitHub REST API)
- **Action:** Call GitHub REST API endpoint
- **On success:** Continue to next dataset
- **On tool unavailable:** Try registered fallback #1 (Google Sheets per EXTERNAL_SOURCES.yaml)
- **If Sheets unavailable or stale:** Try registered fallback #2 (GitHub web per EXTERNAL_SOURCES.yaml)
- **If all fail:** Mark merged_prs as INCOMPLETE, proceed to data_audit

### Required Dataset 3: active_issues
- **Source:** GITHUB_OPEN_ISSUES
- **Access method:** github_rest_api
- **Canonical URL:** https://api.github.com/repos/chas-challenge-2026/avanza-team1/issues?state=open&per_page=100
- **Preferred tool:** GitHub Connector (or any available tool implementing GitHub REST API)
- **Action:** Call GitHub REST API endpoint
- **On success:** Continue to data_audit
- **On tool unavailable:** Try registered fallback #1 (Google Sheets per EXTERNAL_SOURCES.yaml)
- **If Sheets unavailable or stale:** Try registered fallback #2 (GitHub web per EXTERNAL_SOURCES.yaml)
- **If all fail:** Mark active_issues as INCOMPLETE, proceed to data_audit

---

## IMPORTANT: Tool Selection

For each source, EXTERNAL_SOURCES.yaml specifies:
- The canonical endpoint (what data)
- Permitted tool implementations (how to access it)
- The fallback chain (in order if primary fails)

**You may use ANY tool that implements the access_method specified in EXTERNAL_SOURCES.yaml.**

Example: If access_method is "github_rest_api", you may use:
- GitHub Connector
- WebFetch
- Any HTTP tool that can call api.github.com

**Do NOT:** Use a tool not listed in the access_method's `allowed_implementations`.

---

## FORBIDDEN IMPLEMENTATIONS

These tool substitutions are NOT permitted:

- Shell network commands: `git ls-remote`, `git clone`, `git fetch`
- Shell HTTP tools: `curl`, `wget`
- Generic web search: Google, Bing, DuckDuckGo, search engines
- Unregistered URLs or arbitrary sources
- Model training data or knowledge cutoff as source

**Why:** If a source is unavailable, the presentation STOPS with INCOMPLETE data. It does not render with substituted or guessed data. These forbidden paths circumvent that gate.

---

## CRITICAL: Data Completeness

**Presentation rendering only proceeds if ALL required datasets are COMPLETE.**

- If team_roster is INCOMPLETE: STOP
- If merged_prs is INCOMPLETE: STOP
- If active_issues is INCOMPLETE: STOP

**Incomplete data is reported to the user. Presentation is not generated.**

**See SYSTEM_CONTRACT.yaml sections `data_audit` and `build_gate` for gate definitions.**

---

## NEXT STEP

👉 **Go to [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml) and start with `step_1` in the `execution_sequence` section.**

The execution_sequence will guide every action from here onward.
