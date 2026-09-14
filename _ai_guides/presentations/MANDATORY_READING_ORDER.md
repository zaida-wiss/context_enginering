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

1. **[design/ACCESSIBILITY_NEURODIVERSITY.md](design/ACCESSIBILITY_NEURODIVERSITY.md)** 🧠 LÄS FÖRST
   - VARFÖR Symbol + Färg + Text? (för dyslektiker, ADHD, autism — och alla andra)
   - Påtvingad läsning för att förstå designfilosofin
   
2. **[design/VISUAL_DESIGN_MANDATORY.md](design/VISUAL_DESIGN_MANDATORY.md)** ⭐ DESIGN
   - Symbol + Färg + Text (mekanisk implementering)
   - RGB-värden, px-storlekar, font-specs, whitespace — ALLT konkret
   
3. **[monday_meeting/design/SLIDE_DETAIL_SPEC.md](monday_meeting/design/SLIDE_DETAIL_SPEC.md)** ⭐ AUKTORITATIV
   - EXAKT innehål för VARJE SLIDE (①-⑭)
   
4. **[monday_meeting/structure/PRESENTATION_STRUCTURE.md](monday_meeting/structure/PRESENTATION_STRUCTURE.md)**
   - 14 mötespunkter (①-⑭) definitioner

**Om två filer motsäger varandra:** SLIDE_DETAIL_SPEC.md VINNER.

---

### STEG 4: FINAL RENDER GATE

Läs: **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)**
- 13 checkpoints MÅSTE passeras innan rendering
- Om någon checkpoint failas → presentation renderas INTE

---

**MANDATORY_READING_ORDER.md — Denna fil är den ENDA körordningen.**

**Status:** 2026-09-14 — ORCHESTRATION FIXED (human verification removed, single workflow)

