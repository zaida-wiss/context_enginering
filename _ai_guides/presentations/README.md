---
name: presentations_navigation
description: Navigation guide for presentation development — find what you need to change
metadata:
  type: reference
  updated: 2026-09-13
---

# 📊 PRESENTATIONS — Navigation Guide

🚨 **INNAN DU BÖRJAR:** Två obligatoriska filer måste läsas i denna ordning

1. **[DATA_COLLECTION_MANDATORY.md](DATA_COLLECTION_MANDATORY.md)** ← START HÄR
   - Checklist för datainsamling (stängda issues, mergade PRs, commits)
   - Om denna hoppar över → arbete blir dolt (login-arbete, designsystem, etc)

2. **[design/DESIGN_AUTHORITY.md](design/DESIGN_AUTHORITY.md)** ← SEDAN DESIGN-REGLER
   - Designkällor kommer ENDAST från context_enginering (aldrig från avanza-team1)
   - PRESENTATION_STYLE.md är auktoritativ över presentationsverktygets defaults
   - Presentationsverktygets defaults MÅSTE åsidosättas om de strider mot reglerna

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

**Filer:**
- `PRESENTATION_STYLE.md` — Färger, typografi, layout, NPF-regler, QA-checklista

**Använd denna om:** Du vill ändra hur sliderna ser ut (färger, typsnitt, spacing, visuella element)

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
