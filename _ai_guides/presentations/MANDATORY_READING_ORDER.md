---
name: mandatory_reading_order
description: THE ONLY instruction — read and follow SYSTEM_CONTRACT.yaml
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER

## 🚨 CRITICAL — NO WEB SEARCH

**Never search the public web during presentation generation.**

Only use sources explicitly registered in [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md).  
Only use the two project repositories (project code + context).  
Only use user-provided project files.

If required data cannot be found in allowed sources, report the source as unavailable and follow the documented fallback. Never substitute an arbitrary web source.

**See [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml) `external_sources_policy` for full details.**

---

## 1️⃣ EXECUTION RECEIPT GATE (this file + SYSTEM_CONTRACT.yaml)

Before ANYTHING else: SYSTEM_CONTRACT.yaml defines which files MUST be read in THIS execution.

See `execution_receipt` section in SYSTEM_CONTRACT.yaml:
- Every file listed must be READ in this execution
- Previous context, memory, or earlier runs DO NOT count
- You must confirm: "I have read file X"

If any file is unread → STOP and report which files are missing.

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

## 🚨 KEY PRINCIPLE: Positive Instructions Only

**Instructions focus on WHAT TO DO, never on WHAT NOT TO DO.**

Instead of: "Don't make a dashboard, don't use cards, don't compress text"  
We say: "Use CANONICAL LAYOUT: 1 header + 1 message + 1–3 fullwidth blocks, vertically stacked, with fixed spacing."

This prevents misinterpretation. AI builds to the positive spec, not away from negatives.

---

**Version:** 4.0 (Minimal — everything else is in SYSTEM_CONTRACT.yaml)  
**Status:** PRODUCTION — THE ONLY reading order
