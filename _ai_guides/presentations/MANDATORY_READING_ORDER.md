---
name: mandatory_reading_order
description: Exact order AI must read files before rendering presentation — NO EXCEPTIONS
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER — INNAN PRESENTATION RENDERAS

**DENNA FIL MÅSTE LÄSAS FÖRE PRESENTATION.**

**Om denna ordning inte följs → presentation blir inkomplett eller bryter mot regler.**

---

## FASE 1: FÖRSTÅ SYSTEMET (5-10 min)

Läs i denna ordning. Allt är obligatoriskt.

### 1. **START HÄR: README.md** (denna mapp)
   - Vad är presentations-systemet?
   - Var finns vad?
   - Länka direkt till nästa fil

### 2. **DATA_COLLECTION_MANDATORY.md** (denna mapp)
   - INNAN du renderar någon slide, samla denna data
   - Checklista för komplett datainsamling
   - Fallback-hierarki

### 3. **structure/PRESENTATION_STRUCTURE.md**
   - De 14 mötespunkterna
   - Vad varje punkt ska innehålla
   - Obligatoriska element per punkt
   - Varför ordningen fungerar

---

## FASE 2: DESIGN & FORM (5 min)

Dessa styr VISUELLa regler.

### 4. **design/PRESENTATION_STYLE.md**
   - Färger (semantisk BARA)
   - Typografi
   - Layout
   - NPF-regler

### 5. **design/PRESENTATION_CONSISTENCY_FRAMEWORK.md**
   - Visuell konsistens
   - Innehålls-konsistens
   - Röda trådar
   - Varning-signaler

### 6. **design/DESIGN_AUTHORITY.md**
   - Designkällor
   - Vad måste åsidosättas från verktyg-defaults

---

## FASE 3: INNEHÅL PER PUNKT (10-15 min)

Läs den relevanta för vilken punkt du bygger.

### 7. **content/PRESENTATION_SPEC.md**
   - ALLA regler för innehål
   - Issue-format
   - Färger och status
   - NO META-INSTRUCTIONS on slides
   - PROJECT LEAD REVIEW checklist

### 8. **models/WEEKLY_PROGRESS_MODEL.md**
   - Två slides för ① (Levererat + Byggde vidare)
   - Hur klassificera arbete

### 9. **models/REPO_FIRST_RECONSTRUCTION.md**
   - Varför repo-first (inte issue-first)
   - Mekaniska regler

---

## FASE 4: DATA & KÄLLOR (5 min)

Läs detta INNAN du försöker samla data.

### 10. **data/DATA_SOURCES.md**
   - Vilken information behövs
   - Fallback-ordning
   - Canonical URLs
   - Failure handling

### 11. **data/TEAM_ROSTER.md**
   - Vem tillhör vilka team
   - Coverage validation
   - Alla team-medlemmar måste kontrolleras

### 12. **data/SOURCE_CHECK.md**
   - Hur verifiera att data är från rätt källa
   - Timestamps
   - GitHub-länk struktur

---

## FASE 5: VERIFIERING (5 min)

Läs innan du renderar final version.

### 13. **verification/VERIFICATION_SYSTEM.md**
   - QA-process
   - Vad kontrollera

### 14. **verification/VERIFICATION_THIS_WEEK.md**
   - Denna veckas specifika verifiering
   - Vilka rules gäller nu

---

## SNABB REFERENCE

**Om du bara har 5 minuter:** Läs dessa i ordning:
1. README.md (denna mapp)
2. DATA_COLLECTION_MANDATORY.md
3. PRESENTATION_STRUCTURE.md
4. PRESENTATION_SPEC.md

**Dessa är MINIMUM för en presentation.**

---

## CRITICAL RULES SUMMARY

**Från denna läsning, dessa är NOT-negotiable:**

✅ **Data-insamling:** ALL data från GitHub denna vecka (repo-first)
✅ **Mötespunktsmarkörer:** Varje slide har 📝[NUM][TITLE] överst
✅ **Team-struktur:** Två slides per team (Var är vi? + Vad behöver vi göra?)
✅ **Färger:** Semantiska BARA (🟢 klart, 🟡 pågår, 🔴 blockerat)
✅ **Namn:** BARA verifierade namn från GitHub denna vecka
✅ **Issue-tabeller:** Issue | Vad | Ägare | Status | AC | Tests | Review | Docs | PR
✅ **Handlingsplan:** Fyra separata tabeller (arbete, väntar på, blockerar, risker)
✅ **Blockers:** Issue | Väntar på | Påverkar | Äger | Sannolikhet | Fallback
✅ **Risker:** Risk | Typ | Sannolikhet | Konsekvens | Åtgärd | Ansvar | Tid
✅ **DoD:** Läs från issue-description, ALDRIG gissat
✅ **Point ①:** ALLA PRs denna vecka, inget får utelämnas för plats
✅ **Point ⑪:** Sprintmål EFTER kapacitet och prioritering
✅ **Point ⑫:** Senior PL-granskning, plan-bedömning 🟢/🟡/🔴
✅ **Point ⑬:** Beslut → konkreta GitHub-åtgärder

---

## DEPRECATED FILER (läs INTE dessa)

❌ SPRINT_PRESENTATION_STRUCTURE.md (old version)
❌ SPRINT_PROTOCOL_NUMBERED.md (old version)
❌ Gamla examples från innan-context-restructure

---

## VAD OM JAG INTE HINNER LÄSA ALLT?

**Minimum (10 min, 3 slides):**
1. README.md
2. DATA_COLLECTION_MANDATORY.md
3. PRESENTATION_STRUCTURE.md

**Rekomenderad (20 min, full presentation):**
1-5 ovan + PRESENTATION_SPEC.md + DATA_SOURCES.md + TEAM_ROSTER.md

**Full (30 min, senior presentation):**
Alla 1-14 ovan

---

## KONTROLL: Är du redo?

Innan du börjar rendera, svara på dessa:

```
Läst DATA_COLLECTION_MANDATORY.md?          [ ] Ja [ ] Nej — STOP om nej
Läst PRESENTATION_STRUCTURE.md?             [ ] Ja [ ] Nej — STOP om nej
Läst PRESENTATION_SPEC.md?                  [ ] Ja [ ] Nej — STOP om nej
Läst DATA_SOURCES.md?                       [ ] Ja [ ] Nej — STOP om nej
Läst TEAM_ROSTER.md?                        [ ] Ja [ ] Nej — STOP om nej
Läst PRESENTATION_CONSISTENCY_FRAMEWORK.md? [ ] Ja [ ] Nej — STOP om nej

Vet du vilka 7 team-medlemmar som finns denna vecka?  [ ] Ja [ ] Nej — STOP om nej
Vet du vilka 14 mötespunkter som finns?              [ ] Ja [ ] Nej — STOP om nej
Vet du reglerna för mötespunktsmarkörer?             [ ] Ja [ ] Nej — STOP om nej
Vet du fallback-hierarkin för data?                  [ ] Ja [ ] Nej — STOP om nej
```

**Om alla är Ja → du kan börja.**
**Om något är Nej → läs det filen först.**

---

**Denna fil uppdaterades:** 2026-09-13
**Senast följd:** [Du måste fylla detta innan rendering]

