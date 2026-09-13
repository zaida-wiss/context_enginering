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

### ✅ MEGA-REGEL 1: Assignee på VARJE Issue (TVINGANDE FORMAT)

**Format:** (#XX - Namn) eller (#XX - ??) om okänd

```
EXEMPEL RÄTT:
  ✅ #42 Portfolio overview (Zaida)
  ✅ #51 Risk metrics (Erik föreslaget)
  ✅ #48 Authentication (Marco)
  ✅ #52 API schema (??)  ← okänd assignee — visar att det behöver beslutas

EXEMPEL FEL — PRESENTATIONEN MISSLYCKADES OM:
  ❌ #42 Portfolio overview (utan parentes)
  ❌ #51 Risk metrics — nummer utan format
  ❌ #48 Tom assignee-cell
```

**Vägen när du föreslår assignee:**
1. Läs Project Board — vem är redan assignee?
2. Git log — vem jobbar redan på motsvarande branch?
3. Kapacitet — vem har mindre att göra denna vecka?
4. Balans — alla hjälps åt, inte max-flöde
5. Om ingen → markera med (??) och flagga för mötet

**(??) betyder:**
- Assignee ännu ej beslutad
- Flagga på mötet för snabb tilldelning
- Visar accountability-lucket visuellt

### ✅ MEGA-REGEL 2: Verifiera Git-Status & Jämför Med Project Board

**AI MÅSTE:** 
1. Köra git-commands för FAKTISK data (inte gissa)
2. Jämföra mot Project Board
3. Märka diskrepanser (Board kan stale)

```
🔴 TVINGANDE VERIFICERING:

FÖRE du säger något om "status" eller "framsteg":

1. git log develop --since="7 days ago" --oneline
   → Vilka commits är FAKTISKT mergade till develop?

2. git branch -a
   → Vilka branches existerar?

3. git log --all --since="7 days ago" --oneline
   → Vilka commits är gjorda denna vecka (i alla branches)?

4. För varje branch: git log -1 --format="%ai" [branch-name]
   → När var senaste commit? (Stale eller aktiv?)

5. git diff develop..feature/[branch-name] --stat
   → Vilka filer ändrades? Hur mycket arbete?

6. Jämför med GitHub Project Board denna vecka
   → Stämmer Board status överens med Git?
   → Vilka issues visar "In Progress" men är redan mergade?

RESULTAT du MÅSTE visa i presentationen:
✅ Konkreta commits (hash + message) från Git
✅ Vilka branches är aktiva denna vecka
✅ Vilka branches är stale (>3 dagar utan commit)
✅ Vem jobbar på vad (commit author)
✅ Total "delta" mellan develop och feature-branches
✅ Märka där Board-status motsäger Git-bevis

❌ ALDRIG säga: "Teamet jobbar på kärnflödet"
✅ ALLTID säga: "Git visar X commits denna vecka:
            • #42 (Jan - portfolio), #45 (Marco - risk-calc)
            • Branches active: feature/#42, feature/#45
            • Stale: feature/#40 (5 dagar, ingen commit)
            • Board-uppdatering: #40 visar 'In Progress' men ej aktiv"

SE ÄVEN: VERIFICATION_BOARD_VS_GIT.md för status-koder
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

### ✅ MEGA-REGEL 4: Presentationen Lär Branschterminologi

**Presentationen är både statusrapport OCH lärtillfälle för branschbegrepp.**

Regel: **Förklara aldrig ett ord som INTE står på sliden.**

Mängden: Aldrig använd term utan att förklara vad den betyder.
Men: Förklaringen ska INTE introducera nya termer — endast förtydliga dem som redan förekommer.

Presentationen ska graduellt bygga upp teamets ordförråd inom domänen, men utan att orsaka förvirring genom att nämna termer som inte är synliga.

```
❌ DÅLIGT: "Vi säkrar kärnflödet denna vecka"
          (vad är kärnflödet? vilka commits visar det?)

✅ BÄTTRE: "Vi fokuserar på kärnflödet: portföljöversikten 
          end-to-end (hela flödet från inmatning till visning).
          Git visar 5 commits denna vecka 
          (#42 portfolio, #45 risk-calc, etc).
          Status: 80% klar. API inte integrerad ännu."

❌ DÅLIGT: "Risk dashboard är i progress"
          (vad är risk dashboard? vem jobbar?)

✅ BÄTTRE: "Risk dashboard (visar risk-mått: volatilitet = 
          prissvängningar, Sharpe-ratio = risk-justerad avkastning).
          Jobbar på av: Marco (#45).
          Status: 60% klar. Väntar på: API-spec från backend."
```

**ANVÄND DENNA STRUKTUR:**
```
📚 Branschterm: [ordet]
   Definition: [vad betyder det enkelt förklarat]
   Kontext: [varför är det relevant för detta projekt]
   Status: [konkret progress på detta område]
```

**EXEMPEL PÅ TERMER SOM BÖR FÖRKLARAS:**
```
Portfolio (samling av investeringar)
Risk-ratio (mätning av osäkerhet)
Volatilitet (prissvängningar över tid)
Sharpe-ratio (risk-justerad avkastning)
API-kontrakt (överenskommelse mellan system)
Integration (två system arbetar tillsammans)
Branch (parallell utvecklingsväg i Git)
Blocker (något som stoppar framsteg)
Definition of Done (checklist för färdigt arbete)
```

**VARFÖR DET ÄR VIKTIGT:**
- Teammedlemmar lär sig domänvokabulär samtidigt som de jobbar
- Nykomlingar fångar upp termer organiskt
- Möten blir lärtillfällen, inte bara rapporter
- Vanlig ordbok byggas upp över tid

### ✅ MEGA-REGEL 5: Färg Är Semantik, Inte Dekoratör

**Varje färg måste betyda något konkret. Ingen dekorativ färgning.**

```
FÄRGPALETT MED BETYDELSE:

NEUTRALA (STRUKTURFÄRGER):
  🔵 Marinblå — huvudrubriker, viktig struktur, navigering
  🔵 Ljusblå — neutral information, processer, tekniska samband
  ⚫ Blågrå / Ljusgrå — vanliga informationskort, team-kortens baskort
  ⚪ Vit — luft, huvudytor, negativt utrymme

ACCENTFÄRGER (ICKE-STATUS):
  💜 Lila — sprintplanering, beslut, prioriteringar, "nästa steg"
  🌸 Dämpad rosa — människor, ägarskap, assignee, samarbete, variation mellan kort

STATUSFÄRGER (ENDAST NÄR STATUS FINNS):
  🟢 Grön — klart, på plan, låg risk
  🟠 Orange — behöver uppmärksamhet, osäkerhet, kapacitets-/beroenderisk
  🔴 Röd — blockerad, kritisk risk, måste agera omedelbar

EXEMPEL PÅ KORREKT ANVÄNDNING:
  ❌ DÅLIGT: Backend-kort är helt orange för att det är "riskigt"
  ✅ RÄTT: Backend-kort är blågrå (neutral). Inne i kortet markeras 
           just kapacitetsrisken med en liten orange indikator.

  ❌ DÅLIGT: NEXT-kategori är orange för att det är inte MUST
  ✅ RÄTT: NEXT-kategori använder marinblå eller lila. Status-färgning 
           reserveras för faktiska statusar (risk, blockering, etc).

  ❌ DÅLIGT: Assignee-namn i varierande färger för visuell variation
  ✅ RÄTT: Assignee-namn i dämpad rosa för att visa ägarskap. 
           Status-färgning reserveras för risk/blockering på själva uppgiften.
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

**VISUELLA ELEMENT:**
- [ ] Varje slide med DATA har minst ETT visuellt element
- [ ] Progress bars visar ████░░ (inte bara tal)
- [ ] Tidslinjer visar 📍 MON, 📍 TUE, etc (konkret tid)
- [ ] Blockers visar visuellt HUR de blockerar (pilar)
- [ ] Inga slides som är BARA text
- [ ] Progress visuell: från X → Y (inte bara "vi gör det")
- [ ] Ikoner överallt för snabb läsning (📚💪🎯📊)

**FÄRGKODNING (SEMANTISK, INTE DEKORATIV):**
- [ ] Marinblå/ljusblå/gråtoner för struktur & neutral info (majoriteten)
- [ ] 🟢 Grön ENDAST för faktisk god status (på plan, klart)
- [ ] 🟠 Orange ENDAST för faktisk risk/osäkerhet (kapacitet, beroende, blocker)
- [ ] 🔴 Röd ENDAST för faktisk blockering/kritisk status
- [ ] Lila för sprintplanering & prioritering (inget status-värde)
- [ ] Rosa för ägarskap/assignee (inget status-värde)
- [ ] Ingen dekorativ färgning av NEXT, team-namn, etc

**LAYOUT & LESBARHET:**
- [ ] Ingen text går utanför sin ruta (hellre fler slides)
- [ ] Min. 4.5:1 kontrast (WCAG AA)
- [ ] **TVINGANDE: Alla issues har format (#XX - NAMN) eller (#XX - ??)**
- [ ] 60-70% whitespace (NPF-vänligt)

**MISSLYCKAD PRESENTATION OM:**
- [ ] ❌ Issue saknar parentes helt (bara "#42 Portfolio")
- [ ] ❌ Assignee-parentes är tom eller otydlig
- [ ] ❌ Förslagen är inte förtydligade med "(föreslaget)"
- [ ] ✅ Okänd assignee markeras med (??) — det är OK

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
