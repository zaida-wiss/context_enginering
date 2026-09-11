# 🎨 Presentation Design Guide - Sprint Meetings

**Denna guide visar design-principerna för presentationer till sprintmöten.**

## Design-Principer (TVINGANDE)

### ✅ MEGA-REGEL 0: Visuell Pedagogik för Bildtänkare

Presentationen är INTE bara text. Den är FÖR DE SOM TÄNKER BILDLIGT.

```
🖼️ VISUELL DESIGN (OBLIGATORISK):

PROGRESS & STATISTIK:
  ✅ Progress bars (████░░ 80%)
  ✅ Grafer/tal (14/17, 75% → 85%)
  ✅ Färgkodade status (🟢🟠🔴)
  ✅ Ikoner för snabb scanning (📚 Kursmål, 🚀 Projekt, 📍 Deadline)
  ❌ INTE bara "vi ligger bakom"

FLÖDEN & PROCESSER:
  ✅ Visuell blockering (pillar: väntar på → blockerar)
  ✅ Tidslinjer med ikoner (📍 MON 09:00, 📍 THU 15:00)
  ✅ Steg-för-steg diagrammer (vad → hur → resultat)
  ✅ Flödeskartor för arkitektur
  ❌ INTE bara ord-listor

TEAM STATUS:
  ✅ Färgade kort (borders visar status 🟢🟠🔴)
  ✅ Progress-bars per team (████░░)
  ✅ Ikon-representationer av personer (👥 Jan, Marco, Anna)
  ✅ Antal issues/blockers visualiserat
  ❌ INTE bara namn i text

PRIORITERING:
  ✅ Visuell tabell med prioriterings-kolumner
  ✅ Storlek/färg visar viktighet
  ✅ Pilar mellan related/blocking items
  ✅ MÅ-HA vs NICE-TO-HAVE visuellt separerad
  ❌ INTE bara bullet-lista

ARKITEKTUR & BEROENDEN:
  ✅ Visuella flödesdiagram (boxar + pilar)
  ✅ Vilka blockar vilka (visuell blockering)
  ✅ System-komponenter som färgade boxar
  ✅ Beroende-kedjor visuella
  ❌ INTE bara text-beskrivningar
```

### ✅ MEGA-REGEL 1: Assignee på VARJE Issue

**Format:** (#XX - Namn) eller (#XX - Namn föreslaget)

```
EXEMPEL RÄTT:
  #42 Portfolio overview (Jan)
  #51 Rebalance (Marco föreslaget)
  #48 Risk metrics (Anna)

EXEMPEL FEL:
  ❌ #42 Portfolio overview (utan namn)
  ❌ #51 Rebalance suggestions (ingen assignee)
```

**Väg vid förslag:**
1. Git log — vem jobbar redan på det?
2. Kapacitet — vem har mindre att göra?
3. Balans över effektivitet (alla hjälps åt, inte max-flöde)

### ✅ MEGA-REGEL 2: Verifiera Faktisk Git-Status

**AI MÅSTE köra dessa git-commands för att få FAKTISK data (inte gissa):**

```
🔴 TVINGANDE VERIFICERING:

FÖRE du säger något om "status" eller "framsteg":

1. git log develop --since="7 days ago" --oneline
   → Vilka commits är mergade till develop DENNA VECKA?

2. git branch -a
   → Vilka branches existerar?

3. git log --all --since="7 days ago" --oneline
   → Vilka commits är gjorda DENNA VECKA (i alla branches)?

4. För varje branch: git log -1 --format="%ai" [branch-name]
   → När var senaste commit? (Stale eller aktiv?)

5. git diff develop..feature/[branch-name] --stat
   → Vilka filer ändrades? Hur mycket arbete?

RESULTAT du MÅSTE visa i presentationen:
✅ Konkreta commits (hash + message)
✅ Vilka branches är aktiva denna vecka
✅ Vilka branches är stale (>3 dagar utan commit)
✅ Vem jobbar på vad (commit author)
✅ Total "delta" mellan develop och feature-branches

❌ ALDRIG säga: "Teamet jobbar på kärnflödet"
✅ ALLTID säga: "Git visar X commits denna vecka:
            • #42 (Jan - portfolio), #45 (Marco - risk-calc)
            • Branches active: feature/#42, feature/#45
            • Stale: feature/#40 (5 dagar, ingen commit)"
```

### ✅ MEGA-REGEL 3: Ingenting Fabriceras

Varje siffra, datum, mål måste komma från:
- KURSMAL_OCH_BETYG.md (kursmål)
- GitHub Project Board (projektmål)
- Mötesprotokollet (tidsplan, åtgärder)
- **Git log (VERIFIERA — kör git commands!)**
- **Git branches (vad pågår — vilka är aktiva?)**
- **Git diff (hur mycket arbete — konkreta ändringar)**

**ALDRIG:** Gissa, antag, eller "normalt skulle man..."

### ✅ MEGA-REGEL 4: Sanningen Före Känslan

Design ska vara organiserad och lätt att läsa.
Men DATA måste ALLTID vara ärlig.

```
❌ FALSKT: "Vi löser detta! 💪" (känsla) 
           + "Bakom plan 40%" (data mismatch)

✅ RÄTT: "🔴 CRITICAL: 40% på plan
         ÅTGÄRD: Backend + Native pair prog idag 14:00"
```

---

## Slides som MÅSTE vara Visuella

| Slide | Visuella Element | Exempel |
|-------|-----------------|---------|
| **Veckans Schema & Mål** | Timeline + ikoner | 📍 MON 09:00, 🎯 Fokus |
| **Övergripande Status** | Progress bars + färger | ████░░ 80%, 🟢🟠🔴 |
| **Team-Status** | Färgade kort + bars | 🟢 Frontend 80%, 🟠 Backend 60% |
| **Blockers** | Flödesdiagram | Pilar: väntar på → blockerar |
| **Prioritering** | Visuell tabell + storlek | MÅSTE-HA större än NICE-TO-HAVE |
| **Nästa Steg** | Timeline med checkboxes | ☐ Board updated, 📍 MON 17:00 |
| **Sammanfattning** | Statistik visuell | 14/17 → 16/17, 75% → 85% |

---

## Checklist Innan Leverans

- [ ] Varje slide med DATA har minst ETT visuellt element
- [ ] Progress bars visar ████░░ (inte bara tal)
- [ ] Färger matchar verklighet (🟢 ON TRACK, 🟠 DELAY, 🔴 CRITICAL)
- [ ] Tidslinjer visar 📍 MON, 📍 TUE, etc (konkret tid)
- [ ] Blockers visar visuellt HUR de blockerar (pilar)
- [ ] Alla issues har (#Namn) assignee
- [ ] Inga slides som är BARA text
- [ ] Progress visuell: från X → Y (inte bara "vi gör det")
- [ ] Ikoner överallt för snabb läsning (📚💪🎯📊)
- [ ] Färgade kort för team-status (border visar färg)

---

## För AI som Skapar Presentationen

När du får instruktionen "skapa presentation för måndagsmötet":

1. ✅ Rensa ditt minne (från tidigare diskussioner denna vecka)
2. ✅ Läs PRESENTATION_FORMAT_GUIDE.md
3. ✅ Läs denna fil (PRESENTATION_DESIGN.md)
4. ✅ Samla data från: mötesprotokollet, GitHub, git log
5. ✅ Skapa slides med VISUELLA element (inte bara text)
6. ✅ Verifiera: varje issue har (#Namn)
7. ✅ Verifiera: data är från källorna, inte fabricerat
8. ✅ Verifiera: 17-21 slides, separata "Nästa steg" och "Sammanfattning"

---

**Design-filosofi:**
- Visuell = lättläst för bildtänkare
- Ärlig = ingen vilseledning
- Balanserad = hela teamet hjälps åt
- Konkret = datum, namn, tal (inte vag)
- Organiserad = samma struktur varje vecka

**Senast uppdaterad:** 2026-09-11  
**Status:** Design guide för sprint-presentationer
