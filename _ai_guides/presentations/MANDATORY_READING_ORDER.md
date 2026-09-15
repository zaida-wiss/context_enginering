---
name: mandatory_reading_order
description: THE ONLY instruction — read and follow SYSTEM_CONTRACT.yaml
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER

## 🚨 CRITICAL — ALLOWLIST GATE: ALLOWED vs FORBIDDEN

**🚫 THESE ACTIONS ARE ABSOLUTELY FORBIDDEN — NO EXCEPTIONS:**

❌ **Search the public web** (Google, Bing, DuckDuckGo, web search engines, any general search)  
❌ **Clone GitHub repository** (`git clone` — requires credentials, often fails)  
❌ **Download external files** (design specs, templates, tutorials, guides, examples from web)  
❌ **Use unregistered websites** (blogs, forums, Stack Overflow, Medium, dev.to, Notion, Figma links, etc)  
❌ **Substitute arbitrary web sources** as fallback when registered sources fail  
❌ **Use model training data or knowledge cutoff** as replacement for actual data  

**Why:** Web search is how AI models bypass data governance. If a source is unavailable, the presentation STOPS — it does not render with guessed or substituted data.

---

**✅ THESE ACTIONS ARE ALLOWED — AND ONLY THESE:**

✅ **Read local files** from this repository (`_ai_guides/presentations/`, `_memory/`, etc)  
✅ **Fetch GitHub data** via any available platform tool that implements these access methods:
   - **GitHub REST API** access method: `https://api.github.com/repos/chas-challenge-2026/avanza-team1/...`
     (May be implemented via GitHub Connector, WebFetch, or other HTTP tool)
   - **GitHub web** access method: `https://github.com/chas-challenge-2026/avanza-team1/...` (direct navigation)
     (May be implemented via web access, WebFetch, or GitHub Connector)
   - **Individual PR/issue pages**: `https://github.com/chas-challenge-2026/avanza-team1/pull/[NUMBER]`
   
   **IMPORTANT:** The repository specifies ACCESS METHODS (what endpoint/source), not tool names. 
   Any platform tool that can fetch the registered endpoint is allowed. Example: 
   - If access_method is "GitHub API", use any available tool (GitHub Connector, WebFetch, etc) to call `api.github.com`
   - Do NOT reject an access_method because a specific tool name is missing if another tool can implement it
   
✅ **Access registered external sources** from [`_memory/EXTERNAL_SOURCES.yaml`](../../_memory/EXTERNAL_SOURCES.yaml) ONLY  
✅ **Use documented fallback chain** (GitHub API → GitHub web → Sheets → Board → Issues → Protocol)  
   - Fallbacks are tried IN ORDER
   - Each fallback is listed in `DATA_ACQUISITION_CONTRACT.yaml`
   - If all fallbacks fail, mark dataset INCOMPLETE and STOP

---

**If data cannot be found in allowed sources:**
- Do NOT search the web
- Do NOT improvise a substitute source
- Report which source is unavailable
- Follow documented fallback order
- If all fallbacks fail, mark dataset INCOMPLETE
- **STOP rendering** (incomplete data is reported, not hidden)

**🚨 CRITICAL: Before declaring TOOL_UNAVAILABLE, verify actual availability:**
1. Do not assume a tool (GitHub Connector, Google Drive Connector, WebFetch) is unavailable without attempting to use it
2. A missing tool NAME does not equal missing access METHOD — if multiple tools can implement the same access method (e.g., GitHub API via WebFetch or GitHub Connector), try the available option
3. Only mark a data source TOOL_UNAVAILABLE after confirming that NO available platform tool can implement the required access method from EXTERNAL_SOURCES.yaml
4. Example: If GitHub API is required and GitHub Connector is unavailable, try WebFetch on the api.github.com endpoint. Only if all HTTP tools fail → mark TOOL_UNAVAILABLE

**See [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml) sections `external_sources_policy` and `step_1c` (ALLOWLIST GATE) for full details.**

---

## 1️⃣ EXECUTION RECEIPT GATE (this file + SYSTEM_CONTRACT.yaml)

Before ANYTHING else: SYSTEM_CONTRACT.yaml defines which files MUST be read in THIS execution.

See `execution_receipt` section in SYSTEM_CONTRACT.yaml:
- Every file listed must be READ in this execution
- Previous context, memory, or earlier runs DO NOT count
- You must confirm: "I have read file X"

If any file is unread → STOP and report which files are missing.

**🚨 CLARIFICATION on initial restrictions:**
- You ARE allowed to read files from this GitHub repository (context_enginering) during execution_receipt
- You ARE allowed to read from the project repository (avanza-team1) if that is part of the execution path
- You are NOT allowed to start fetching project data (PRs, issues, commits) UNTIL the execution_receipt gate is complete
- In other words: read the GitHub files needed to establish execution path, but don't start the DATA_ACQUISITION step until authorized by execution_sequence

## 2️⃣ READ SYSTEM_CONTRACT.yaml
Location: [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml)

This file contains:
- ✅ non_negotiable_execution (read-audit-build-render-deliver sequence)
- ✅ execution_receipt gate (which files must be read)
- ✅ artifact_gate (prevents premature artifact generation)
- ✅ Authority hierarchy (who owns what domain)
- ✅ Execution sequence (what you do in order, step by step)
- ✅ Data validation checksums
- ✅ Delivery rules (PDF default, PPTX only if requested)

## 3️⃣ FOLLOW EXECUTION_SEQUENCE FROM SYSTEM_CONTRACT.yaml

The `execution_sequence` section tells you exactly what to do next.

Follow it step by step. Do not skip. Do not deviate.

⚠️ If any gate fails (execution_receipt, data_audit, render_gate, artifact_gate):
   - STOP immediately
   - Report which gate failed and why
   - Do not generate any artifact

---

## 🚨 CRITICAL: Paths in SYSTEM_CONTRACT are repo-relative

All file paths in SYSTEM_CONTRACT.yaml are relative to repo root: `_ai_guides/presentations/`

Example:
- `presentations/MANDATORY_READING_ORDER.md` → `_ai_guides/presentations/MANDATORY_READING_ORDER.md`
- `monday_meeting/design/SLIDE_DETAIL_SPEC.md` → `_ai_guides/presentations/monday_meeting/design/SLIDE_DETAIL_SPEC.md`

---

## 🔗 External URLs

All external URLs (GitHub, Google Sheets, Google Docs) are in: [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md)

---

---

## 🚨 CRITICAL: When to STOP for Incomplete Data

**STOP presentation rendering if and only if:**
- A REQUIRED dataset (team_roster, merged_prs, or active_issues) cannot be acquired
- ALL documented access methods and fallbacks have been attempted
- And NO available platform tool can implement any of the remaining access methods

**Do NOT stop if:**
- A specific tool name is missing (if another tool implements the same access method, use it)
- A single endpoint fails (try registered fallbacks first)
- Optional enrichment data is unavailable (commits, branches, board metadata)

**Exact rule:** Mark dataset INCOMPLETE only when: (access_method in EXTERNAL_SOURCES.yaml) AND (all platform tools implementing that method have been attempted) AND (all are unavailable).

---

## THIS Execution — Definition

**An execution:**
- **STARTS** when user requests new presentation
- **RECEIVES** unique execution_id (e.g., `exec_20260916_001`)
- **CONTINUES** through subsequent chat turns until DELIVER, STOP, or RESTART
- **INVALIDATES** any resume after STOP — next request = NEW execution from README
- **DOES NOT REUSE** old receipts, old execution_ids, or prior execution contexts

---

## Resume Policy

- **STOP**: Terminates execution_id. Next presentation request = NEW execution from README.
- **PAUSE**: Preserves execution_id. Next request resumes WITH SAME RECEIPT and DATA_AUDIT.
- **RESTART**: Explicit keyword to invalidate current execution_id and start NEW.

---

## 🚨 KEY PRINCIPLE: Positive Construction Instructions (for Design)

**Design instructions focus on WHAT TO DO, never on WHAT NOT TO DO.**

Instead of: "Don't make a dashboard, don't use cards, don't compress text"  
We say: "Use CANONICAL LAYOUT: 1 header + 1 message + 1–3 fullwidth blocks, vertically stacked, with fixed spacing."

This prevents misinterpretation. AI builds to the positive spec, not away from negatives.

**Note:** Process and security gates still use explicit negative rules (FORBIDDEN, NEVER, STOP) — these are not design instructions and must be unambiguous.

---

**Version:** 4.0 (Minimal — everything else is in SYSTEM_CONTRACT.yaml)  
**Status:** PRODUCTION — THE ONLY reading order
