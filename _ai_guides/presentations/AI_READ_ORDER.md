---
name: ai_read_order
description: EXAKT ordning för AI — vilka filer, i vilken ordning, för att bygga presentation
metadata:
  type: process
  critical: true
---

# 🤖 AI READ ORDER — Exakt läsordning före presentation

**DENNA FIL SÄGER DEN ENDA ORDNINGEN AI SKA FÖLJA.**

**Ingen annan ordning. Ingen hoppa över. Denna ordning.**

---

## STAGE 1: FÖRSTÅ SYSTEMET (10 min)

### Läs FÖRST (obligatorisk):
1. **[root README.md](../../README.md)** — 2 min
   - Tre steg för allt arbete
   - Länk till PROJEKTKONTEXT_AVANZA

2. **[MANDATORY_READING_ORDER.md](MANDATORY_READING_ORDER.md)** — 5 min
   - Systemöversikt (alla filer hänger ihop)
   - AI EXECUTION WORKFLOW (denna fil!)
   - STEG 1-3 (läsa instruktioner → identity → data)

3. **[presentations/README.md](README.md)** — 3 min
   - Tre filer som förbättrar presentation konkret
   - Quick Reference (vilken fil för vad)

---

## STAGE 2: SAMLA DATA (30 min)

### Läs OCH HÄM DATA:

1. **[TEAM_ROSTER.md](../../_memory/TEAM_ROSTER.md)** — 2 min
   - Vilka är de 7 team-medlemmarna?
   - Verifiera från git commits (INTE gissat)

2. **[data/DATA_SOURCES.md](data/DATA_SOURCES.md)** — 3 min
   - Vilka sources ska vi läsa från?
   - Fallback-hierarki
   - Canonical URLs för allt

3. **[DATA_COLLECTION_MANDATORY.md](DATA_COLLECTION_MANDATORY.md)** — 5 min
   - Checklista för komplett datainsamling
   - MÅSTE slutföras innan nästa steg
   - Render-gate (slides får INTE genereras utan denna)

4. **Hämta faktisk data från GitHub** — 15 min
   - Branches, commits, PRs, issues, project board
   - Verifiera från faktiska sources (ej gissningar)
   - Notera vilka kilder som ÄR nåbara + vilka som INTE är

5. **[data/DATA_COLLECTION_CHECKLIST.md](data/DATA_COLLECTION_CHECKLIST.md)** — 3 min
   - Dubbelt-checka att allt är samlat
   - Ingenting ska missas

---

## STAGE 3: PLANERA ARBETET (10 min)

### Läs OCH ANALYSERA:

1. **[models/REPO_FIRST_RECONSTRUCTION.md](models/REPO_FIRST_RECONSTRUCTION.md)** — 3 min
   - Varför använder vi commits/PRs som primär källa?
   - Inte issue-status, utan faktiskt arbete

2. **[models/DEPENDENCY_CHAIN_PLANNING.md](models/DEPENDENCY_CHAIN_PLANNING.md)** — 5 min
   - KRITISK för punkt ⑦⑧!
   - Vilka är Foundation-issues (låter upp mycket)?
   - Vilka är Dependenter (blockeras av andra)?
   - Vilka risker finns (mergekonflikter, omarbete)?
   - Fas-baserad ordning (Fas 1 → 2 → 3)

3. **[models/WEEKLY_PROGRESS_MODEL.md](models/WEEKLY_PROGRESS_MODEL.md)** — 2 min
   - Hur klassificerar vi arbete?
   - ✓ KLART / → PÅGÅR / ! BEHÖVER UPPMÄRKSAMHET

---

## STAGE 4: DESIGN SLIDORNA (20 min)

### Läs DESIGN-FILER (INTE valfritt):

1. **[design/ACCESSIBILITY_NEURODIVERSITY.md](design/ACCESSIBILITY_NEURODIVERSITY.md)** — 5 min
   - VARFÖR färg+symbol+text?
   - Dyslexi/ADHD-vänlighet är KÄRNAN
   - Färger = budskap, symboler = signaler
   - Whitespace = fokus

2. **[design/DESIGN_MODERN.md](design/DESIGN_MODERN.md)** — 8 min
   - MÅSTE LÄSAS FÖRE RENDERING
   - Vacker design (inte tråkiga tabeller)
   - Rundade hörn, modern stil
   - Semantiska färger (grön=färdig, orange=pågår, röd=blockerad)
   - Läsbara textstorlekar (32pt titel → 16pt innehål)
   - Whitespace-fokus (ADHD-vänligt)
   - Cards istället för tabeller
   - Konkreta CSS-regler

3. **[design/PRESENTATION_FORMAT_GUIDE.md](design/PRESENTATION_FORMAT_GUIDE.md)** — 5 min
   - Konkreta slide-exempel för alla 7 slide-typer
   - Hur varje format ska se ut
   - Borders, colors, layout, whitespace

### SEDAN Läs STRUKTUR:

4. **[structure/PRESENTATION_STRUCTURE.md](structure/PRESENTATION_STRUCTURE.md)** — 8 min
   - 14 mötespunkter (①-⑭)
   - EXAKTA krav för varje
   - Punkt ⑦ = blockerträd i map-format
   - Punkt ⑧ = fas-baserad ordning
   - Pedagogiska förklaringar (📚 märkade ord)
   - Käll-status i footer

### VALFRITT (djupare design):

5. **[design/PRESENTATION_STYLE.md](design/PRESENTATION_STYLE.md)** — 3 min
   - Färger, typografi, layout, NPF-regler
   - QA-checklista

6. **[design/PRESENTATION_CONSISTENCY_FRAMEWORK.md](design/PRESENTATION_CONSISTENCY_FRAMEWORK.md)** — 2 min
   - Röda trådar vecka-till-vecka
   - Repeterbara strukturer

7. **[design/DESIGN_AUTHORITY.md](design/DESIGN_AUTHORITY.md)** — 1 min
   - Vem beslutar om design?

---

## STAGE 5: VERIFIERA & RENDERA (15 min)

### Läs VERIFICATION-FILER:

1. **[verification/AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)** — 5 min
   - Exakt ordning: hämta → verifiera → analysera → leverera
   - Vilka käll-status ska visas i presentationen
   - Om källa inte nåbar → visa detta (ej gömt)

2. **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)** — 5 min
   - KAN/INTE KAN presentationen renderas?
   - Per-slide-verifikation
   - 13 checkpoints MÅSTE passeras
   - INGEN UNDANTAG

3. **[verification/VERIFICATION_SYSTEM.md](verification/VERIFICATION_SYSTEM.md)** — 2 min
   - Hur verifierar vi data?
   - Vilket är sanningen (GitHub, Project Board, etc)?

### VALFRITT (djupare verifikation):

4. **[verification/VERIFICATION_BOARD_VS_GIT.md](verification/VERIFICATION_BOARD_VS_GIT.md)** — 2 min
   - Är Project Board i sync med Git?

5. **[verification/VERIFICATION_THIS_WEEK.md](verification/VERIFICATION_THIS_WEEK.md)** — 1 min
   - Denna veckas specifika verifikation

---

## STAGE 6: BUILD & DELIVER (30+ min)

### Bygga presentationen:

1. Följ PRESENTATION_STRUCTURE.md (14 mötespunkter)
2. Använd DEPENDENCY_CHAIN_PLANNING för punkt ⑦⑧
3. Använd VISUAL_DESIGN_MANDATORY för fonts, colors, spacing
4. Använd ACCESSIBILITY_NEURODIVERSITY för varför design är som den är
5. Visa käll-status i footer
6. Verifiera RENDER_GATE_CHECKLIST innan delivering
7. Leverera KLAR presentation

---

## 🚨 FILER INTE I DENNA ORDNING (legacy eller optional):

❌ **SPRINT_PRESENTATION_STRUCTURE.md** — Legacy (använd PRESENTATION_STRUCTURE istället)
❌ **SPRINT_PROTOCOL_NUMBERED.md** — Legacy mötesprotokolls-struktur
❌ **SPRINT_MEETING_PROTOCOL_TEMPLATE.md** — Template (ej för denna presentation)
❌ **TEAM_WORK_OVERVIEW.md** — Ej använd (valfritt)
❌ **VISUAL_TEMPLATES_MANDATORY.md** — Utgått (använd PRESENTATION_FORMAT_GUIDE istället)
❌ **SOURCE_CHECK.md** — Backup (DATA_COLLECTION_MANDATORY räcker)
❌ **PRESENTATION_SPEC.md** — Utgått (använd PRESENTATION_STRUCTURE istället)
❌ **VISUAL_VERIFICATION.md** — Optional (endast för QA)

---

## 📝 TOTAL TIME

- Stage 1 (Förstå): 10 min
- Stage 2 (Data): 30 min
- Stage 3 (Plan): 10 min
- Stage 4 (Design): 20 min
- Stage 5 (Verify): 15 min
- Stage 6 (Build): 30+ min

**TOTALT: ~115 min (2 timmar) före rendering**

---

## ✅ CHECKLIST

Innan AI börjar bygga presentation:

```
STAGE 1:
  [ ] Root README läst
  [ ] MANDATORY_READING_ORDER läst
  [ ] presentations/README läst

STAGE 2:
  [ ] TEAM_ROSTER läst (7 medlemmar verifierade från git)
  [ ] DATA_SOURCES läst (vilka sources)
  [ ] DATA_COLLECTION_MANDATORY läst (checklist)
  [ ] Data samlat från GitHub (branches, commits, PRs, issues)
  [ ] DATA_COLLECTION_CHECKLIST låst (ingenting missats)

STAGE 3:
  [ ] REPO_FIRST_RECONSTRUCTION läst
  [ ] DEPENDENCY_CHAIN_PLANNING läst (blockerträd, Fas 1-3)
  [ ] WEEKLY_PROGRESS_MODEL läst

STAGE 4:
  [ ] ACCESSIBILITY_NEURODIVERSITY läst (VARFÖR design)
  [ ] VISUAL_DESIGN_MANDATORY läst (RGB, fonts, spacing)
  [ ] PRESENTATION_FORMAT_GUIDE läst (slide-exempel)
  [ ] PRESENTATION_STRUCTURE läst (14 mötespunkter)

STAGE 5:
  [ ] AI_VERIFICATION_WORKFLOW läst (ordning: hämta → verifiera → leverera)
  [ ] RENDER_GATE_CHECKLIST läst (13 checkpoints)
  [ ] VERIFICATION_SYSTEM läst

STAGE 6:
  [ ] Presentation byggd enligt PRESENTATION_STRUCTURE
  [ ] Punkt ⑦⑧ använder DEPENDENCY_CHAIN_PLANNING
  [ ] Fonts/colors från VISUAL_DESIGN_MANDATORY
  [ ] Käll-status visad i footer
  [ ] RENDER_GATE_CHECKLIST passar (ALLT ✅)
  [ ] Presentation levererad KLAR
```

---

**Version:** 1.0  
**Status:** MANDATORY  
**Senast uppdaterad:** 2026-09-14
