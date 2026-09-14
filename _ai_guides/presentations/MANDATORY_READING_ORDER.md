---
name: mandatory_reading_order
description: Exact order AI must read files before rendering presentation — NO EXCEPTIONS
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER — INNAN PRESENTATION RENDERAS

**DENNA FIL MÅSTE LÄSAS FÖRE PRESENTATION.**

🔗 **NOTE:** Alla externa URLs (Google Sheets, Google Docs, GitHub) är centraliserade i [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md). Se den filen för aktuella IDs och fallback-URLs.

**Om denna ordning inte följs → presentation blir inkomplett eller bryter mot regler.**

---

## 🚨 KRITISK REGEL #0 — LÄSA INSTRUKTIONER ≠ VISA INSTRUKTIONER

**INNAN du läser NÅGOT annat:**

```
⭐ DENNA REGEL ÄR TVINGANDE ⭐

Du ska LÄSA dessa instruktioner för att FÖRSTÅ vad presentationen behöver.
Du ska ANVÄNDA dessa instruktioner för att BYGGA presentationen.
Du ska ALDRIG VISA dessa instruktioner ON SLIDES.

EXEMPEL:

🔴 FEL:
  Slide visar: "Repo-first: visa bara det som går att koppla till PR, commit..."
  Slide visar: "Måste räknas mot develop"
  Slide visar: "Ej live-låst här"
  → Dessa är instruktioner för DIG, inte innehål för mötet

✅ RÄTT:
  Slide visar: "#95 Security review · Zaida · ✓ DONE · merged 2026-09-13"
  Slide visar: "🔴 API-kontrakt inte låst — Frontend blockerad"
  Slide visar: "Backend måste leverera API-spec idag"
  → Dessa är RESULTAT av att följa instruktionerna

MECKANISK KONTROLL (efter rendering):
  För varje slide:
    Q: "Skulle en projektledare säga detta till teamet?"
    Ja → texten får vara på sliden
    Nej → ta bort texten

RENDER-GATE CHECK:
  ☐ Presentationen innehåller INGEN instruktioner?
  ☐ Presentationen innehåller INGEN checklista?
  ☐ Presentationen innehåller INGEN AI-process?
  
  Om något är NEJ → STOPP, ta bort det innan rendering
```

**Se även:**
- [PRESENTATION_SPEC.md — NO META-INSTRUCTIONS ON SLIDES](content/PRESENTATION_SPEC.md#L219)
- [RENDER_GATE_CHECKLIST.md — KRITISK: INGEN AI-INSTRUKTIONER PÅ SLIDES](verification/RENDER_GATE_CHECKLIST.md)

---

---

## 🚀 AI EXECUTION WORKFLOW — DENNA ORDNING MÅSTE FÖLJAS

**DENNA FIL SÄGER DEN EXAKTA ORDNINGEN för AI:**

👉 **LÄS FÖRST:** [AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)

Den filen säger:
- FASE 1: Datainsamling & Identity verification
- FASE 2: Render gate check
- FASE 3: Bygga presentation & final verification
- **AI gör ALLT — levererar presentation KLAR (ingen human-loop)**

**UTAN denna ordning → presentation blir felaktig eller ej verifierad.**

---

---

### STEG 1: LÄS DESSA FILER (i ordning)

**Läs INTE något mer — dessa filer säger allt:**

1. **[README.md](README.md)** — Vad är presentations-systemet?
2. **[monday_meeting/README.md](monday_meeting/README.md)** — 14 mötespunkter overview
3. **[monday_meeting/data/DATA_COLLECTION_MANDATORY.md](monday_meeting/data/DATA_COLLECTION_MANDATORY.md)** — Datainsamling & identity-verifikation
4. **[data/DATA_SOURCES.md](data/DATA_SOURCES.md)** — Vilka GitHub-URLs, fallback-ordning

**Sedan gå till STEG 2 (nedan).**

---

### STEG 2: VERIFIERA

**Läs dessa filer för verifikations-processen:**

1. **[verification/AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)** 
   - AI gör ALLT: hämta → verifiera → leverera
   
2. **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)** 
   - KAN presentationen renderas? 13 checkpoints MÅSTE passeras

---

### STEG 3: DESIGN & SPECIFIKATION

**Läs DESSA filer (de innehåller ALLT):**

1. **[design/SLIDE_DETAIL_SPEC.md](monday_meeting/design/SLIDE_DETAIL_SPEC.md)** ⭐ AUKTORITATIV
   - EXAKT innehål för VARJE SLIDE (①-⑭)
   
2. **[design/VISUAL_DESIGN_MANDATORY.md](design/VISUAL_DESIGN_MANDATORY.md)** ⭐ DESIGN
   - Symbol + Färg + Text (NPF/dyslexia-vänlig)
   
3. **[structure/PRESENTATION_STRUCTURE.md](monday_meeting/structure/PRESENTATION_STRUCTURE.md)**
   - 14 mötespunkter (①-⑭) definitioner

**Om två filer motsäger varandra:** SLIDE_DETAIL_SPEC.md VINNER.

---

### STEG 4: VERIFIERA PRESENTATION FÖRE RENDERING

Läs: **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)**
- KAN presentationen renderas?
- 13 checkpoints MÅSTE passeras

### ❌ VISA INTE (detta är AI-instruktioner, inte möte-innehål):

- ❌ "Verifieringslåge innan status"
- ❌ "Team roster: 7 medlemmar verifierade"
- ❌ "GitHub PRs inte läsbart via API"
- ❌ "Render gate checklist"
- ❌ "Verification report"
- ❌ "Identity verification status"
- ❌ "Data collection status"
- ❌ "AI process information"

### ✅ ANVÄND DENNA DATA (men VISA INTE verifikations-info):

- Commits denna vecka → från data (VISA det faktiska arbetet)
- Merged PRs → från data (VISA vad som blev klart)
- Team roster (för att VERIFIERA namn) → VISA bara namn + arbete, inte "verifierat"
- Fallback-strategier → använd om primär källa failas, men VISA inte att fallback användes
- Data sources (GitHub) → ANVÄND dem för presentationen, VISA inte käll-status

### 🎯 MÖTE-PRESENTATIONEN ska visa:

✅ Vad som arbetades med denna vecka  
✅ Vem som var ansvarig för vad  
✅ Vad som blev klart  
✅ Vad som är pågår  
✅ Vad som blockerar oss  
✅ Nästa prioriteringar  

❌ INTE: AI-verifikations-process, data-samlings-status, eller verifikations-rapporter

---

**MANDATORY_READING_ORDER.md — Denna fil är den ENDA körordningen.**

**Status:** 2026-09-14 — ORCHESTRATION FIXED (human verification removed, single workflow)

