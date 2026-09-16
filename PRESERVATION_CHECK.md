---
name: preservation_check
description: Main vs cleanup file comparison before merge — identifies rules removed from main
metadata:
  version: 1.0
  date: 2026-09-16
  branch: cleanup
  purpose: Ensure no valuable rules were accidentally lost during refactoring
---

# 🔍 PRESERVATION CHECK — Main vs Cleanup Comparison

**Status:** cleanup is 22 commits ahead of main (has all of main + 22 new)  
**Task:** Identify rules that exist in main but were removed/weakened in cleanup

---

## 📊 File Comparison Summary

| File | Main Lines | Cleanup Lines | ±Lines | Status |
|------|-----------|---------------|--------|--------|
| SYSTEM_CONTRACT.yaml | 287 | 341 | +54 | ✅ Additions (good) |
| DATA_ACQUISITION_CONTRACT.yaml | 187 | 231 | +44 | ✅ Additions (good) |
| SLIDE_DETAIL_SPEC.md | 1156 | 1063 | -93 | ⚠️ See below |
| VISUAL_DESIGN_MANDATORY.md | 416 | 416* | ~0 | ✅ Redesigned (not removed) |
| ACCESSIBILITY_NEURODIVERSITY.md | 89 | 130 | +41 | ✅ Additions (good) |
| RENDER_GATE_CHECKLIST.md | 168 | 204 | +36 | ✅ Additions (good) |

*VISUAL_DESIGN_MANDATORY.md was restructured (removed light-theme gray palette, added dark navy + soft cards). Net lines ~same but content reorganized.

---

## 🚨 CRITICAL FINDINGS

### ❌ Rule Removed: DEDUPLICATION & CHECKSUMS (was in main, NOT in cleanup)

**In main (SLIDE_DETAIL_SPEC.md):**
```markdown
**DEDUPLICATION RULE:**
- Same work MUST NOT appear twice (e.g., issue + branch + PR)
- If issue has linked PR and branch → show as ONE row
- If issue has no PR yet but has active branch → show as ONE row
- If branch has no PR and no issue → show as ONE row
- Count only ONCE in audit and slides

**TEAM CHECKSUMS (RENDERED IN AUDIT REPORT):**
Frontend: verified_activity_count (audit) == representation_count (slides)
Backend: verified_activity_count (audit) == representation_count (slides)
[etc for all teams]
If mismatch → both audit and slides note discrepancy. Never silently drop data.
```

**Status in cleanup:** NOT FOUND in any file

**Assessment:** 🔴 IMPORTANT RULE LOST
- This rule prevents duplicate work appearing on multiple slides
- It enforces audit accuracy (checksums)
- It's not mentioned anywhere else in cleanup
- **Recommendation:** Restore to cleanup before merge

**Where should it go?**
- Primary: RENDER_GATE_CHECKLIST.md (validation rule before rendering)
- Secondary: DATA_ACQUISITION_CONTRACT.yaml (data audit section)

---

### ⚠️ Rule Removed: VERIFIED ACTIVITY DEFINITION

**In main (SLIDE_DETAIL_SPEC.md):**
```markdown
**CRITICAL RULE:** Point ① completeness = union of ALL verified activity during reporting period, not merged PRs alone.

**VERIFIED ACTIVITY = {merged PRs, closed issues, open issues with activity, active branches, open PRs with activity, relevant commits}**
```

**Status in cleanup:** NOT FOUND in SLIDE_DETAIL_SPEC. Partially covered in ACTIVE_WORK_DETECTION_MODEL.md but less explicit.

**Assessment:** 🟡 PARTIALLY ADDRESSED
- ACTIVE_WORK_DETECTION_MODEL.md (new in cleanup) covers this conceptually
- But the explicit definition "verified_activity = union of X, Y, Z" is lost
- SLIDE_DETAIL_SPEC no longer states the completeness rule clearly

**Recommendation:** Consider adding back the explicit definition in SLIDE_DETAIL_SPEC as context for slide builders.

---

### ⚠️ Design Palette Removed: Light-theme colors

**In main (VISUAL_DESIGN_MANDATORY.md):**
- Gray text colors (#323232, #666666, #f5f5f5)
- Light-theme backgrounds
- Light-theme contrast ratios

**Status in cleanup:** Removed (replaced with dark navy theme)

**Assessment:** ✅ INTENTIONAL REDESIGN (not lost data)
- Cleanup made deliberate choice to dark navy (#0F1830)
- Old light palette was superseded
- Decision documented in new design

**Recommendation:** No action needed (intentional refactoring).

---

### ⚠️ Color Semantics Model Changed

**In main (VISUAL_DESIGN_MANDATORY.md):**
```markdown
## 🎨 COLOR SEMANTICS — What Each Color Means

**STATUS COLORS:**
- Green (#2ecc71) = On Track
- Orange (#ff9800) = In Progress  
- Red (#e74c3c) = Blocked
- Gray (#9e9e9e) = Unknown

**STRUCTURE COLORS:**
- Dark Gray = Main text
- Medium Gray = Metadata
- Light Gray = Backgrounds
```

**Status in cleanup:** Partially changed
- Status colors defined differently (now in TEAM_COLORS section)
- Team colors and status colors still separated (good)
- But semantic explanation less detailed

**Assessment:** 🟡 WEAKENED DOCUMENTATION
- The conceptual model (why colors mean what) is less clear in cleanup
- The rules are there but the reasoning is implied, not explicit

**Recommendation:** Consider restoring the "COLOR SEMANTICS — What Each Color Means" section to VISUAL_DESIGN_MANDATORY for clarity.

---

### ⚠️ Border Rules Removed

**In main (VISUAL_DESIGN_MANDATORY.md):**
```markdown
## 🖼️ BORDER RULES — Status Visualization

**COLORED BORDERS = STATUS ONLY**
- GREEN BORDER (3px) = ON TRACK
- ORANGE BORDER (3px) = IN PROGRESS
- RED BORDER (3px) = CRITICAL
- DARK BORDER (2px) = INFORMATION ONLY

RULE: Never mix status colors with neutral information.
```

**Status in cleanup:** Structure changed
- Cleanup separates Team colors (borders) from Status colors (symbols)
- But doesn't have same explicit "border = status" visual guide

**Assessment:** ✅ INTENTIONAL CHANGE
- Cleanup redesigned border semantics (team = border, status = symbol)
- New model is clearer for multi-team slides
- Old model would have confused cross-team work

**Recommendation:** No action needed (improved design).

---

## 📋 ACTION ITEMS

### 🔴 Must Fix Before Merge

1. **Restore DEDUPLICATION RULE**
   - Add to RENDER_GATE_CHECKLIST.md (as verification check)
   - Add to DATA_ACQUISITION_CONTRACT.yaml (as audit requirement)
   - Ensure unique_id counting is documented

2. **Restore TEAM CHECKSUMS**
   - Add to RENDER_GATE_CHECKLIST.md
   - Make it a PASS/FAIL gate before rendering

### 🟡 Recommended Enhancements

3. **Add back VERIFIED_ACTIVITY definition** (optional but helpful)
   - Clarify in SLIDE_DETAIL_SPEC or ACTIVE_WORK_DETECTION_MODEL
   - Make union-of-sources rule explicit

4. **Expand COLOR SEMANTICS documentation** (optional for clarity)
   - Add brief explanation of why team colors ≠ status colors
   - Restore conceptual section to VISUAL_DESIGN_MANDATORY

---

## ✅ What Cleanup Did Right

- ✅ Moved all visual rules OUT of SLIDE_DETAIL_SPEC into VISUAL_DESIGN (correct)
- ✅ Moved all data rules INTO DATA_ACQUISITION_CONTRACT (correct)
- ✅ Added ACTIVE_WORK_DETECTION_MODEL.md (excellent)
- ✅ Added ACCESSIBILITY_NEURODIVERSITY.md (excellent)
- ✅ Added RENDER_GATE_CHECKLIST.md (excellent)
- ✅ Established SSOT hierarchy (excellent)
- ✅ Fixed color conflicts (dark navy + soft cards, excellent)
- ✅ Added dependency diagram format for ⑥A (excellent)

---

## 🎯 Recommendation

**✅ cleanup is ready to merge, WITH these additions:**

1. Add DEDUPLICATION RULE + TEAM CHECKSUMS back to RENDER_GATE_CHECKLIST.md
2. (Optional) Restore VERIFIED_ACTIVITY definition for clarity
3. (Optional) Restore COLOR SEMANTICS explanation section

**After these additions:**
- Run smoke test on cleanup
- Then merge cleanup → main

---

**Comparison completed:** 2026-09-16  
**Branch base:** main b6fcf4e3... (shared commit)  
**cleanup ahead:** 22 commits  
**Status:** Ready with minor restorations
