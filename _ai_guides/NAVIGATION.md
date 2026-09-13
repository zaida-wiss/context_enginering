---
name: navigation
description: Quick index — all guidance starts in README.md
metadata:
  type: reference
  updated: 2026-09-13
---

# 🧭 NAVIGATION — Index Only

**All task routing and read order is defined in README.md**

This file is an index only. It does not define read order or rules.

---

## 📍 Quick Links

**Presentation:**  
→ README.md#presentation

**Risk & Decisions:**  
→ README.md#project-context


**Terminology:**  
→ _ai_guides/ORDBOK.md

**Project Context:**  
→ _project_context/

---

## 📚 All Guides

### AI Execution Guides — Presentations

**🚨 START HÄR:** presentations/MANDATORY_READING_ORDER.md — Exact sequence before rendering

**Main Navigation:**
→ presentations/README.md — What do you want to change?

**Mandatory Files (MUST READ before rendering):**
1. presentations/MANDATORY_READING_ORDER.md (this week's sequence)
2. presentations/DATA_COLLECTION_MANDATORY.md (data collection checklist)
3. presentations/structure/PRESENTATION_STRUCTURE.md (14 meeting points)
4. presentations/content/PRESENTATION_SPEC.md (content rules)
5. presentations/data/DATA_SOURCES.md (data sources)
6. presentations/data/TEAM_ROSTER.md (team members)
7. presentations/design/PRESENTATION_CONSISTENCY_FRAMEWORK.md (consistency rules)

**Content (vad sliderna ska innehålla):**
- presentations/content/PRESENTATION_SPEC.md

**Structure (slide-ordning & 14 mötespunkter):**
- presentations/structure/PRESENTATION_STRUCTURE.md
- presentations/structure/SPRINT_PROTOCOL_NUMBERED.md
- presentations/structure/SPRINT_MEETING_PROTOCOL_TEMPLATE.md

**Design (visuell utseende, färger, konsistens):**
- presentations/design/PRESENTATION_STYLE.md
- presentations/design/PRESENTATION_CONSISTENCY_FRAMEWORK.md
- presentations/design/DESIGN_AUTHORITY.md

**Data (sources & insamling):**
- presentations/DATA_COLLECTION_MANDATORY.md (MUST READ)
- presentations/data/DATA_SOURCES.md (fallback hierarchy)
- presentations/data/DATA_COLLECTION_CHECKLIST.md
- presentations/data/SOURCE_CHECK.md
- presentations/data/TEAM_ROSTER.md

**Verification (verifiering):**
- presentations/verification/VERIFICATION_SYSTEM.md
- presentations/verification/VERIFICATION_THIS_WEEK.md
- presentations/verification/VISUAL_VERIFICATION.md
- presentations/verification/VERIFICATION_BOARD_VS_GIT.md

**Models (datamodeller):**
- presentations/models/REPO_FIRST_RECONSTRUCTION.md
- presentations/models/WEEKLY_PROGRESS_MODEL.md

### Project Context
- _project_context/DEFINITION_OF_DONE.md
- _project_context/COURSE_REQUIREMENTS.md
- _project_context/DECISIONS.md
- _project_context/PROJECT.md


---

## 🚫 Old Task Router Below — IGNORE

(The sections below duplicate README.md. Use README instead.)

### TASK 1: "Skapa En Presentation Till Måndagsmötet"

**LÄSA (I denna ordning):**

1. ✅ **README.md** (denna repo)
   - Sektion: "Du ska skapa en presentation? START HÄR"
   - Sektion: "DATA FÖR SLIDE ① ("VAD GJORDES FÖRRA VECKAN")"
   - Sektion: "PEDAGOGI — PRESENTATIONEN SOM LÄRTILLFÄLLE"
   - Sektion: "FÄRGREGLER"
   
2. ✅ **_ai_guides/PRESENTATION_SPEC.md** (start + color rules)
   - Sektion: "MEGA-REGEL" (överordnad regel)
   - Sektion: "COLOR SEMANTICS" (färg = status, aldrig dekoration)
   
3. ✅ **_ai_guides/SPRINT_PRESENTATION_STRUCTURE.md**
   - Sektion: "HUVUDMÅL" (8 frågor varje person ska kunna svara på)
   - Sektion: "📝⑥ VAD GJORDES FÖRRA VECKAN" (ny regel om tempo + visuell känsla)
   
4. ✅ **_ai_guides/PRESENTATION_DESIGN.md**
   - Sektion: "MEGA-REGEL 0: Visual-First"
   - Sektion: "MEGA-REGEL 0B: Färg, Form & Symboler Bär Känslan"
   
5. ✅ **_ai_guides/PRESENTATION_FORMAT_GUIDE.md**
   - Sektion: "MEGA-REGEL 0A: INDIVIDPERSPEKTIV"
   - Sektion: "MEGA-REGEL 0B PLUS: VISUELL KÄNSLA"
   
6. ✅ **_ai_guides/DATA_SOURCES.md** (fallback-strategi)
   - Sektion: "INFORMATION NEEDED" (vilken info behövs)
   - Sektion: "FALLBACK HANDLING" (vad gör man om en källa failar)
   
7. ✅ **_ai_guides/PRESENTATION_STRUCTURE.md** (14 mötespunkter & struktur)
   - Sektion: "14 mötepunkter" (vilka slides behövs)

**SLIPP (Läs INTE dessa för presentation):**

- ❌ CROSS_TEAM_INTEGRATION.md (bara om en blocker mellan team behöver förklaras)
- ❌ SOURCE_CHECK.md (redan dokumenterat i PRESENTATION_SPEC)
- ❌ Hela ORDBOK.md (läs bara ord som dyker upp på sliderna)
- ❌ avanza-team1 README (läs bara kod vid verifiering av beroenden)

**TIDEN: ~45 minuter att läsa allt**

---

### TASK 2: "Jag Förstår Inte Färgerna — Varför Är Presentationen Orange?"

**LÄSA (snabbt):**

1. ✅ **README.md** → Sektion "FÄRGREGLER"
2. ✅ **_ai_guides/PRESENTATION_DESIGN.md** → "MEGA-REGEL 0B: Färg, Form & Symboler Bär Känslan"
3. ✅ **_ai_guides/PRESENTATION_FORMAT_GUIDE.md** → "MEGA-REGEL 0B PLUS"

**TIDEN: ~5 minuter**

---

### TASK 3: "Jag Vill Förstå Ett Ord (T.ex. 'Volatilitet')"

**LÄSA:**

1. ✅ **_ai_guides/ORDBOK.md** → Sök ordet (Ctrl+F)
2. ✅ Se "DEFINITION → EXEMPEL → VARFÖR DET SPELAR ROLL"

**TIDEN: ~1 minut per ord**

---

### TASK 4: "Vad Är Regeln För [X]?"

**Använd denna lookup-tabell:**

| Fråga | Läs Denna Fil | Sektion |
|-------|---------------|---------|
| Färg-regler | PRESENTATION_DESIGN.md | MEGA-REGEL 0B |
| Hur man hämtar GitHub-data | README.md | GITHUB DATA ACCESS |
| Format på slides | PRESENTATION_FORMAT_GUIDE.md | Alla mega-regler |
| Vilka slides behövs | PRESENTATION_STRUCTURE.md | 14 mötepunkter |
| Vilka frågor ska varje person kunna svara på | SPRINT_PRESENTATION_STRUCTURE.md | HUVUDMÅL |
| Om-commit-status-visar-vad | PRESENTATION_DESIGN.md | MEGA-REGEL 2 |
| Branschtermer | ORDBOK.md | Sök ordet |
| Data för slide ① | README.md | DATA FÖR SLIDE ① |
| Fallback när GitHub failar | DATA_SOURCES.md | FAILURE HANDLING |

---

## 📋 FILÖVERSIKT — VAD GÖR VARJE FIL

### Context-Repo Instruktioner

| Fil | Syfte | Läs Om Du... |
|-----|-------|------------|
| **README.md** | Datahämtning + översikt | Ska skapa presentation eller förstår inte struktur |
| **PRESENTATION_SPEC.md** | Officiell presentation-standard | Ska bygga slides eller förstår inte regler |
| **PRESENTATION_DESIGN.md** | Design + färg + NPF-regler | Färgval eller tillgänglighet |
| **PRESENTATION_FORMAT_GUIDE.md** | Layout + visuell känsla | Hur slides ska se ut |
| **SPRINT_PRESENTATION_STRUCTURE.md** | Slide-innehål per mötespunkt | Vilka slides behövs |
| **DATA_SOURCES.md** | Vilken data presentationen behöver | Fallback-strategi eller vilken källa att använda |
| **CROSS_TEAM_INTEGRATION.md** | Beroenden mellan team | Blockers mellan Frontend/Backend/Native |
| **SOURCE_CHECK.md** | Källverifiering | Vad ska presentationen rapportera? |
| **ORDBOK.md** | Branschterminologi | Ett ord verkar konstigt |

### Memory & Data Files

| Fil | Syfte | Läs Om Du... |
|-----|-------|------------|
| **PRESENTATION_STRUCTURE.md** | Övergripande krav (14 mötepunkter) | Vill förstå struktur övergripande |
| **PRESENTATION_DATA.md** | Snapshot för denna veckans presentation | Presentationen behöver färdig data |
| **GITHUB_SNAPSHOT.md** | Fallback för GitHub när API failar | GitHub är otillgänglig |
| **CURRENT_PROJECT_STATUS.md** | Fallback för Project Board | Project Board är otillgänglig |
| **PROTOCOL_SNAPSHOT.md** | Fallback för mötesprotokollet | Mötet kunde inte läsas |

---

## ⚡ SNABBVÄGAR

### "Jag Behöver Bara Färg-Info Nu"

```
1. README.md → FÄRGREGLER
2. PRESENTATION_DESIGN.md → MEGA-REGEL 0B
```

### "Jag Skapar Min Första Presentation"

```
1. README.md (hela)
2. PRESENTATION_SPEC.md (bara mega-regler)
3. SPRINT_PRESENTATION_STRUCTURE.md (HUVUDMÅL + Slide ①)
4. PRESENTATION_DESIGN.md (MEGA-REGEL 0, 0B, 1)
5. Börja bygga
```

### "Jag Behöver Veta Vilka Slides"

```
PRESENTATION_STRUCTURE.md → "14 mötepunkter struktur"
```

### "Jag Vill Bara Förstå Status-Färgerna"

```
1. README.md → FÄRGREGLER
2. Done.
```

---

## 🚫 ÖVERFULL LÄSNING — SLIPP DESSA

**Du behöver INTE läsa detta för presentation:**

- ❌ Hela CROSS_TEAM_INTEGRATION.md (läs bara om blocker behövs)
- ❌ Alla examples i PRESENTATION_FORMAT_GUIDE.md (scan bara headings)
- ❌ VERIFICATION_BOARD_VS_GIT.md (läs bara om en issue ser felaktig ut)
- ❌ avanza-team1 README.md (läs bara specifik kod vid behov)
- ❌ Alla branches i avanza-team1 (läs bara aktiva branches denna vecka)

**Dessa filer är REFERENS — läs bara relevant del.**

---

## 📍 KRITISK LÄSORDNING (ALDRIG ÄNDRA)

För presentation MÅSTE denna ordning följas:

```
1. README.md (datahämtning först)
2. PRESENTATION_SPEC.md (mega-regler)
3. SPRINT_PRESENTATION_STRUCTURE.md (innehål)
4. PRESENTATION_DESIGN.md (design)
5. PRESENTATION_FORMAT_GUIDE.md (layout)
6. Först DÅ börjar presentation-byggel
```

Om ordningen bryts kan presentationen missa kritiska regler.

---

## 🎯 RÉSUMÉ

**Du skapar presentation? Läs detta:**

→ README.md  
→ PRESENTATION_SPEC.md (mega-regler)  
→ SPRINT_PRESENTATION_STRUCTURE.md (slide ①)  
→ PRESENTATION_DESIGN.md (färger + visuell känsla)  
→ Börja bygga

**Allt annat är REFERENS. Läs bara när du behöver.**

Totaltid: ~45 minuter första gången, 10 minuter senare.

---

**Senast uppdaterad:** 2026-09-13
