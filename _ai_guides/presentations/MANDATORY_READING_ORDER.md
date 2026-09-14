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

**See SYSTEM_CONTRACT.yaml `external_sources_policy` for full details.**

---

## 1️⃣ READ THIS FILE
You are reading it now.

## 2️⃣ READ SYSTEM_CONTRACT.yaml
Location: [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml)

This file contains:
- ✅ Machine-readable contract
- ✅ Authority hierarchy (who owns what domain)
- ✅ Execution sequence (what you do in order)
- ✅ Hard rules (non-negotiable)
- ✅ Data validation checksums
- ✅ Forbidden content
- ✅ Deprecated files (do NOT read)

## 3️⃣ FOLLOW EXECUTION_SEQUENCE FROM SYSTEM_CONTRACT.yaml

The `execution_sequence` section tells you exactly what to do next.

Follow it. Nothing else.

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

**Version:** 4.0 (Minimal — everything else is in SYSTEM_CONTRACT.yaml)  
**Status:** PRODUCTION — THE ONLY reading order
