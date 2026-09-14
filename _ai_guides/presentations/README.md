---
name: presentations_navigation
description: Navigation guide for presentation development — find what you need to change
metadata:
  type: reference
  updated: 2026-09-13
---

# 📊 PRESENTATIONS — Navigation Guide

⛔ **EXEMPEL-DATA I DESSA FILER:**
Alla exempelpersoner (<EXAMPLE_MEMBER_A>, etc), issue-nummer och branches i instruktionerna är ALDRIG verklig projektdata.
Du får ALDRIG kopiera exempel till en presentation. Använd ENDAST verifierad data från TEAM_ROSTER.md och GitHub.
Om ett namn inte finns i TEAM_ROSTER → det är inte en verklig teammedlem.

---

🚨 **DU ÄR HÄR FÖR ATT BYGGA EN PRESENTATION**

**START HÄR** → **[MANDATORY_READING_ORDER.md](MANDATORY_READING_ORDER.md)** ← ALLT DU BEHÖVER

Denna fil innehåller:
- ✅ Systemöversikt (hur allt hänger ihop)
- ✅ Data-hämtning från GitHub (exakta URLs)
- ✅ Designregler (Symbol + Färg + Text)
- ✅ Render-gate checklist (när presentation är klart)
- ✅ Länk till PRESENTATION_FORMAT_GUIDE.md (konkreta slide-exempel)

**ALLT är länkat därifrån. Ingenting mer att söka efter.**

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

## 🎨 **design/** — Visuell design & layout

**OBLIGATORISKA FILER (måste läsas före rendering):**
- `VISUAL_DESIGN_MANDATORY.md` — 🚨 **MÅSTE LÄSAS** — Symbol + Färg + Text (denna ordning), NPF/dyslexia-vänligt, WCAG-kontrast
  - Konkret PowerPoint-implementering
  - DoD-status rendering
  - Progress bars, dependency diagrams
  - Före rendering: VISUELL CHECKLIST
  
**REFERENSFILER:**
- `PRESENTATION_STYLE.md` — Färger, typografi, layout, NPF-regler, QA-checklista
- `PRESENTATION_CONSISTENCY_FRAMEWORK.md` — Röda trådar, repeterbara strukturer, content consistency
- `DESIGN_AUTHORITY.md` — Design-källa autoritet

**Använd VISUAL_DESIGN_MANDATORY om:** Du renderar en presentation (det är tvingande före rendering)
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
- `VISUAL_VERIFICATION.md` — Skärmdumpar från dev
- `VERIFICATION_BOARD_VS_GIT.md` — Verifiera Board-status vs Git-faktisk-status
- `VERIFICATION_SYSTEM.md` — Verifieringssystem

**Använd denna om:** Du vill ändra HUR vi verifierar att data är korrekt

---

## 🧮 **models/** — Datamodeller

**Filer:**
- `REPO_FIRST_RECONSTRUCTION.md` — **MANDATORY:** Varför vi samlar ALL repo-aktivitet först, inte issue-first
- `WEEKLY_PROGRESS_MODEL.md` — Hur vi kategoriserar arbete (✓ KLART / → PÅGÅR / ! BEHÖVER UPPMÄRKSAMHET)

**Använd denna om:** Du vill ändra HUR vi klassificerar och presenterar arbete

---

## 🎯 Quick Reference

| Jag vill ändra... | Gå till | Fil |
|-------------------|---------|-----|
| Vad sliderna ska innehålla | `content/` | PRESENTATION_SPEC.md |
| Ordningen på slides | `structure/` | PRESENTATION_STRUCTURE.md |
| Hur sliderna ser ut | `design/` | PRESENTATION_STYLE.md |
| Vilka sources vi läser från | `data/` | DATA_SOURCES.md |
| Hur vi verifierar data | `verification/` | VERIFICATION_BOARD_VS_GIT.md |
| Hur vi klassificerar arbete | `models/` | WEEKLY_PROGRESS_MODEL.md |

---

**Senast uppdaterad:** 2026-09-13
