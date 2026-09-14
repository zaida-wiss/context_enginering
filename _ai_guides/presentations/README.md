---
name: presentations_navigation
description: Navigation guide for presentation development — find what you need to change
metadata:
  type: reference
  updated: 2026-09-13
---

# 📊 PRESENTATIONS — Navigation Guide

🔗 **Alla externa datakällor:** Se [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md) för centraliserad register över Google Sheets, Google Docs, GitHub och alla fallback-URLs.

⛔ **EXEMPEL-DATA I DESSA FILER:**
Alla exempelpersoner (<EXAMPLE_MEMBER_A>, etc), issue-nummer och branches i instruktionerna är ALDRIG verklig projektdata.
Du får ALDRIG kopiera exempel till en presentation. Använd ENDAST verifierad data från TEAM_ROSTER.md och GitHub.
Om ett namn inte finns i TEAM_ROSTER → det är inte en verklig teammedlem.

---

🚨 **DU ÄR HÄR FÖR ATT BYGGA EN PRESENTATION**

## 🤖 **START HÄR FÖR AI:**

👉 **[MANDATORY_READING_ORDER.md](MANDATORY_READING_ORDER.md)** ← ENDA ORDNINGEN FÖR AI

Denna fil säger:
- STEG 1: Läs system-filer (README, DATA_COLLECTION, DATA_SOURCES)
- STEG 2: Verifiera (AI_VERIFICATION_WORKFLOW, RENDER_GATE_CHECKLIST)
- STEG 3: Design & spec (SLIDE_DETAIL_SPEC, VISUAL_DESIGN_MANDATORY, PRESENTATION_STRUCTURE)
- STEG 4: Final render-gate innan presentation byggs

**En ordning. Ingen variation. Denna ordning.**

---

## TRE FILER SOM FÖRBÄTTRAR PRESENTATIONEN KONKRET:

1. **[DEPENDENCY_CHAIN_PLANNING.md](models/DEPENDENCY_CHAIN_PLANNING.md)** — FAS-BASERAD ORDNING
   - Ersätter "3 issues per person" med intelligent blockerträd
   - Visar vilka issues som låser upp nästa steg
   - Minskar mergekonflikter + omarbete
   - Presentationen visar nu: Fas 1 → 2 → 3 istället för MUST/NEXT/LATER

2. **[ACCESSIBILITY_NEURODIVERSITY.md](design/ACCESSIBILITY_NEURODIVERSITY.md)** — VARFÖR DESIGNEN ÄR SÅ
   - Förklarar hur färger/symboler/whitespace gör presentationen lättare att läsa
   - Hjälper ADHD/dyslektiker att förstå på 1 sekund
   - Gör presentationen vackrare OCH mer tillgänglig
   - Inte "extra", det är KÄRNAN i designen

3. **[AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)** — VILKA AI GÖR
   - Explicit ordning: hämta → verifiera → analysera → leverera
   - Visar vilka källor som är nåbar/inte nåbar i presentationen
   - Transparens utan distraction

---

**START HÄR → [MANDATORY_READING_ORDER.md](MANDATORY_READING_ORDER.md)** ← ALLT DU BEHÖVER

Denna fil innehåller:
- ✅ Systemöversikt (hur allt hänger ihop)
- ✅ Data-hämtning från GitHub (exakta URLs)
- ✅ Designregler (Symbol + Färg + Text från VISUAL_DESIGN_MANDATORY.md)
- ✅ Render-gate checklist (när presentation är klart)
- ✅ Länk till **[monday_meeting/design/SLIDE_DETAIL_SPEC.md](monday_meeting/design/SLIDE_DETAIL_SPEC.md)** — exakt innehål & format per slide
- ✅ Länk till **[monday_meeting/structure/PRESENTATION_STRUCTURE.md](monday_meeting/structure/PRESENTATION_STRUCTURE.md)** 
  - 14 mötespunkter (①-⑭) med EXAKTA krav för varje:
  - Fas-baserad ordning (punkt ⑧)
  - Blockerträd i map-format (punkt ⑦)
  - Övergripande regler (TEAMTÄNK, BRANSCHPEDAGOGIK)
  - Konkreta krav per slide
  - Visuella element
  - Struktur-summary

**ALLT är länkat därifrån. Ingenting mer att söka efter.**

⚠️ **OM PRESENTATIONEN INTE BLEV BÄTTRE:**
- Kontrollera att AI_VERIFICATION_WORKFLOW.md är läst (punkt ⑦⑧)
- Kontrollera att DEPENDENCY_CHAIN_PLANNING.md används för punkt ⑧
- Kontrollera att ACCESSIBILITY_NEURODIVERSITY.md påverkar färgvalet (punkt ①-⑭)
- Kontrollera källstatus visas i footer (ej blockad, liten text)

---

**OM DU VIL ÄNDRA SYSTEMET** (inte bygga presentation):
1. Läs [DATA_COLLECTION_MANDATORY.md](DATA_COLLECTION_MANDATORY.md) för att förstå datahämtning
2. Läs [design/DESIGN_AUTHORITY.md](design/DESIGN_AUTHORITY.md) för design-principer
3. Navigera via "Vad vill du ändra?" sektion nedan

⚠️ **OM WEBBEN ÄR BEGRÄNSAD:**
   - GitHub-webben kan failas på grund av nätverksbegränsningar
   - Google Sheets fallback är alltid tillgänglig: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/
   - Se [data/DATA_SOURCES.md](data/DATA_SOURCES.md) för fullständig fallback-hierarki

---

**Vad vill du ändra?** Gå hit:

---

## 📝 **content/** — Vad presentationen ska innehålla

**Filer:**
- `PRESENTATION_SPEC.md` — Vad sliderna MÅSTE innehålla (issue-format, färger, regler)

**Använd denna om:** Du vill ändra VAD som ska synas på sliderna

---

## 🗂️ **structure/** — Slide-ordning & organisation

**Filer:**
- `PRESENTATION_STRUCTURE.md` — 14 mötespunkter & slidinformation (①-⑭)
- `SPRINT_PROTOCOL_NUMBERED.md` — Mötesprotokollet struktur
- `SPRINT_MEETING_PROTOCOL_TEMPLATE.md` — Template för mötet
- `SPRINT_PRESENTATION_STRUCTURE.md` — (Legacy/deprecated — bruk PRESENTATION_STRUCTURE istället)

**Använd denna om:** Du vill ändra ORDNINGEN på slides, lägga till/ta bort mötespunkter, eller ändra vad som ska hända i mötet

---

## 🎨 **design/** — Visuell design & layout & Tillgänglighet

**OBLIGATORISKA FILER (måste läsas före rendering):**
- `VISUAL_DESIGN_MANDATORY.md` — 🚨 **MÅSTE LÄSAS** — Symbol + Färg + Text (denna ordning), NPF/dyslexia-vänligt, WCAG-kontrast
  - Konkret PowerPoint-implementering
  - DoD-status rendering
  - Progress bars, dependency diagrams
  - Före rendering: VISUELL CHECKLIST
- `ACCESSIBILITY_NEURODIVERSITY.md` — **NYTT & KRITISK:** VARFÖR färg+symbol+text? Dyslexi/ADHD-vänlig design explained. Färger = budskap, symboler = signaler, whitespace = fokus
  
**REFERENSFILER:**
- `PRESENTATION_RED_THREADS.md` (i monday_meeting/design/) — Röda trådar, repeterbara strukturer, content consistency
- `DESIGN_AUTHORITY.md` — Design-källa autoritet

**Använd VISUAL_DESIGN_MANDATORY om:** Du renderar en presentation (det är tvingande före rendering)
**Använd ACCESSIBILITY_NEURODIVERSITY om:** Du vill förstå VARFÖR design är som den är (pedagogisk + neurotypisk tillgänglig)
**Använd PRESENTATION_STYLE om:** Du vill förstå djupare design-principerna
**Använd framework om:** Du vill förstå hur presentationen håller röd tråd från möte till möte

---

## 📊 **data/** — Datainsamling & källor

**Filer:**
- `TEAM_ROSTER.md` — **MANDATORY:** Auktoritativ lista över team-medlemmar (Frontend/Backend/System)
- `DATA_SOURCES.md` — Vilka sources att läsa från (GitHub, Project Board, Google Docs, Sheets fallback)
- `DATA_COLLECTION_CHECKLIST.md` — Checklist innan presentation börjas
- `DATA_COLLECTION_MANDATORY.md` — Obligatorisk checklista som förhindrar att arbete försvinner
- `SOURCE_CHECK.md` — Källverifiering & timestamp

**Använd denna om:** Du vill ändra VILKA SOURCES presentationen läser från, eller HUR data samlas in

---

## ✅ **verification/** — Verifiering & QA

**Filer:**
- `AI_VERIFICATION_WORKFLOW.md` — **NYTT & KRITISK:** Exakt ordning för AI — hämta → verifiera → analysera → leverera. Inkl. hur man visar käll-status om något inte är nåbar
- `RENDER_GATE_CHECKLIST.md` — Når presentationen kan/inte kan renderas (per-slide-verifikation)
- `VISUAL_VERIFICATION.md` — Skärmdumpar från dev
- `VERIFICATION_BOARD_VS_GIT.md` — Verifiera Board-status vs Git-faktisk-status
- `VERIFICATION_SYSTEM.md` — Verifieringssystem

**Använd denna om:** Du vill ändra HUR vi verifierar att data är korrekt, eller vilka steg AI måste följa

---

## 🧮 **models/** — Datamodeller & Planering

**Filer:**
- `REPO_FIRST_RECONSTRUCTION.md` — **MANDATORY:** Varför vi samlar ALL repo-aktivitet först, inte issue-first
- `WEEKLY_PROGRESS_MODEL.md` — Hur vi kategoriserar arbete (✓ KLART / → PÅGÅR / ! BEHÖVER UPPMÄRKSAMHET)
- `DEPENDENCY_CHAIN_PLANNING.md` — **NYTT:** Fas-baserad ordning, blockerträd, risk-register. Ersätter "3 issues per person" med intelligent chain-planning

**Använd denna om:** Du vill ändra HUR vi klassificerar och presenterar arbete, eller hur vi planerar för blockers/beroenden

---

## 🎯 Quick Reference

| Jag vill... | Gå till | Fil |
|---|---|---|
| Bygga presentation | `MANDATORY_READING_ORDER.md` | **START HERE** |
| Förstå AI-ordningen | `verification/` | AI_VERIFICATION_WORKFLOW.md |
| Se blockers & beroenden | `models/` | DEPENDENCY_CHAIN_PLANNING.md |
| Förstå VARFÖR designen | `design/` | ACCESSIBILITY_NEURODIVERSITY.md |
| Rendrera slides | `design/` | VISUAL_DESIGN_MANDATORY.md |
| Vad sliderna ska innehålla | `content/` | PRESENTATION_SPEC.md |
| Ordningen på slides | `structure/` | PRESENTATION_STRUCTURE.md |
| Hur sliderna ser ut | `design/` | PRESENTATION_STYLE.md |
| Vilka sources vi läser från | `data/` | DATA_SOURCES.md |
| Hur vi verifierar data | `verification/` | VERIFICATION_BOARD_VS_GIT.md |
| Hur vi klassificerar arbete | `models/` | WEEKLY_PROGRESS_MODEL.md |

---

**Senast uppdaterad:** 2026-09-14 — Fixed: removed deprecated file references, single reading order
