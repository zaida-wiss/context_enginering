# 🎨 PRESENTATION FORMAT GUIDE — Exakt Layout för Varje Slide

## 📍 DOKUMENTVÄGEN

**Du är här:** PRESENTATION_FORMAT_GUIDE.md (Visuell formatering)

```
START — README.md
        ↓
SPRINT_PRESENTATION_STRUCTURE.md
        ↓
🟢 DU ÄR HÄR: PRESENTATION_FORMAT_GUIDE.md (denna fil)
        ↓
ANVÄND MED:
  • SPRINT_PROTOCOL_NUMBERED.md (vilka punkter?)
  • Dessa EXEMPEL-SLIDES (kopiera layout exakt)
        ↓
RESULTAT: NPF-vänlig presentation med rätt design
```

---

## 🚨 KRITISKT FÖR AI — TRE VIKTIGA REGLER

### REGEL 0: INGENTING FABRICERAS — ALLT FRÅN KÄLLOR

**Du får ALDRIG hitta på något.**

Varje siffra, datum, mål, och statistik i presentationen MÅSTE komma från dessa och ENDAST dessa kilder:

```
🔴 TVINGANDE KÄLLKRAV:

KURSMÅL denna vecka:
  → Läs från: _memory/KURSMAL_OCH_BETYG.md
  → ELLER: Mötesprotokollet (vad diskuterades förra veckan)
  → Verifiera: Vilka kursmål är "denna veckas fokus"?

PROJEKTMÅL denna vecka:
  → Läs från: GitHub Project Board (denna vecka)
  → Läs från: Mötesprotokollet (vad är målsättningen)
  → Verifiera: Vilka features ska vara klara THU 15:00?

VECKANS TIDSPLAN:
  → Läs från: Mötesprotokollet (vilka möten är bokade?)
  → Läs från: GitHub Project Board (deadlines)
  → Verifiera: Vem sa vilken tid? Är det i mötesprotokollet?

TEAM STATUS (grön/orange/röd):
  → Läs från: Mötesprotokollet (vad sa teamet förra veckan?)
  → Läs från: Git log denna vecka (faktiska commits)
  → Läs från: GitHub Project Board (faktiska issues done/in progress)
  → Verifiera: Matchar status det som faktiskt gjordes?

BLOCKERS:
  → Läs från: Mötesprotokollet (vilka blockers nämndes?)
  → Läs från: GitHub issues (marked as blocked)
  → Verifiera: Är denna blockade verklig eller löst redan?

ÅTGÄRDSFÖRSLAG:
  → Läs från: Mötesprotokollet (vad kom vi överens om?)
  → ALDRIG: Din egen gissning eller "normalt skulle man..."

🚫 ALDRIG HITTA PÅ:
❌ "Kursmål X är fokus denna vecka" (verifierat från KURSMAL_OCH_BETYG.md?)
❌ "Teamet är grön" (verifierat från actual git commits?)
❌ "Möte på TUE 10:00" (finns det i mötesprotokollet?)
❌ "En åtgärd skulle vara..." (kom teamet överens om detta?)
❌ Exempel-mål eller hypotes-mål

🔴 REGEL: Om du inte kan cita källan = DU HAR FABRICERAT = MISSLYCKAD
```

**Innan du sätter en siffra, ett mål, eller ett datum i presentationen — fråga dig själv:**
- Var står detta exakt? (fil + rad)
- Är det från en VERIFICERAD källa?
- Eller är det min gissning?

---

### REGEL 1: DATA FÖRE DESIGN
**Du MÅSTE följa denna format exakt.** Inte ungefär. EXAKT.

- ✅ Symbol **📝①** överst på VARJE slide (vänster kant)
- ✅ Färger **🟢🟠🔴** för status (MÅSTE finnas)
- ✅ Borders runt team-status (visar om de är i fas)
- ✅ Tabeller, inte bara bullets
- ✅ Whitespace (60-70% tom yta)
- ✅ Kontrast WCAG AA (4.5:1 minimum)
- ✅ MAX 3-5 bullets per sektion
- ✅ **VARJE issue nummer MÅSTE ha assignee:** (#XX - Namn) eller (#XX - Namn föreslaget)

### REGEL 2: SANNINGEN FÖRE KÄNSLAN ⚠️
**Blanda ALDRIG ihop design-känslan med faktisk data!**

```
🔴 ALDRIG:
- "Vi löser detta!" (känsla) när data visar KRITISK
- Snygga design för att dölja att vi ligger efter
- Optimistisk ton när projektet riskerar att INTE gå i mål
- Färger som inte matchar faktisk status

✅ ALLTID:
- Ärlig data: om vi är kritisk → säg "KRITISK" (🔴)
- Konkreta åtgärder: vad gör vi IDAG för att lösa det?
- Transparent bedömning: visa både problem OCH lösning
- Färger som matchar verkligheten: 🟢 = faktisk ON TRACK
```

**Användaren säger: "Om vårat projekt riskerar att inte gå i mål, 
ska AI inte lura oss att tro att vi är på banan i texten som står."**

Du har förvaret att vara helt ÄRLIG med data.

---

## 💫 TONALITET vs DATA — TVÅ HELT OLIKA SAKER

**🚨 VARNING: Blanda ALDRIG ihop DESIGN-känslan med faktiska DATA!**

```
TONALITET (Design, färger, layout):
✅ KAN vara: Organiserad, lättläst, tydlig visuell hierarki
✅ SYFTE: Göra presentationen lätt att förstå, inte stressande
✅ EXEMPEL: Bra whitespace, tydlig struktur, ikoner

DATA & TEXT (Faktisk status, siffror, bedömning):
✅ MÅSTE vara: 100% ÄRLIG, INGEN giltig
✅ REGEL: Om vi är KRITISK → text säger "🔴 KRITISK"
✅ REGEL: Om vi är GRÖN → text säger "🟢 ON TRACK"
✅ REGEL: Om vi ligger EFTER → säg det tydligt, göm det INTE

🚨 ALDRIG GÖRA:
❌ "Vi är on track" (text) när data visar bakom plan
❌ Snygga design för att dölja faktiska problem
❌ Positivitet i ord när data visar kritisk status
❌ "Allt är bra" design-känsla när projektet riskerar att inte gå i mål
```

### EXEMPEL på RÄTT SEPARATION:

**❌ FELAKTIGT (blandning av design-känsla & faktisk data):**
```
Slide ser snyggt ut: "Vi löser detta! 💪"
Men text säger: "Bakom plan 60%, två kritiska blockers"
Resultat: Användare blir vilseförd av design-känslan
```

**✅ KORREKT (ärlig data, organiserad design):**
```
Slide är tydlig & organiserad:

🔴 NATIVE TEAM — CRITICAL
Progress: ████░░░░░░ 40%
Issues: 1/3 done

Blocker: API spec väntas WED 14:00

ÅTGÄRD: Backend + Native pair prog MON 14:00
         • Spec writing (1h)
         • Implementation (3h)
         • Deadline: SAMMA DAG 17:00

Känsla: "Vi är i en utmaning men vi HANDLAR på det"
Sanningen: Vi är kritisk OCH vi gör något konkret
```

### RÄTT TONALITET BETYDER:
✅ Organiserad layout (du FÖRSTÅR situationen)
✅ Tydliga färger (du VET vad som är kritisk)
✅ Konkreta åtgärder (du VET vad vi gör)
✅ Ärlig data (du kan lita på informationen)

### FELAKTIG TONALITET BETYDER:
❌ Vilseledande design (dölja problem med snyggt layout)
❌ Falskt positiv text ("allt är bra" när det inte är det)
❌ Tomt positivitet utan åtgärder (bara ord, ingen handling)
❌ Data som motsäger design (förvirring)

### Hur vi skapar denna känsla:

**Färger & Emojis**
- 🟢 Grön visar framsteg och ON TRACK — se det överallt!
- 🟠 Orange visar utmaningar men LÖSBAR — vi har åtgärder
- 🔴 Röd visar KRITISKT men ADRESSERAD — vi gör något IDAG
- ✅ Checkmarks visar vad som är klart (framsteg!)
- 💪 Motiverande ord på slutslide ("Lycka till denna vecka!")

**Layout & Whitespace**
- 60-70% tom yta = andrum, inte känslan av kaos
- Tydlig hierarki = "jag förstår vad som är viktigt"
- Borders & cards = struktur, "vi har kontroll"
- Tabeller & bars = visuell förståelse, inte massa text

**Text & Ord**
- "Framsteg", "ON TRACK", "klart" visas överst
- "Blocker", "Risk", "åtgärd" visas MED LÖSNING
- Deadlines = konkreta (inte vaga)
- Actions = konkreta steg (vi gör något!)

**Exempel på GOD tonalitet:**
```
❌ "Native är bakom och det är ett problem"
✅ "Native ligger bakom (40%) — Backend + Native pair prog 
    IDAG 14:00 för spec-writing. Resultat: Vi kommer i fas."
```

**Exempel på GLAD layout:**
```
Framsteg denna vecka:
✅ Portfolio overview klar
✅ Risk calc klar  
✅ Tests 80% klara
⏳ Rebalance i progress

Resultat: Vi ligger ON TRACK 🟢

🚨 En blocker: Sharpe spec väntas WED 14:00
ÅTGÄRD: Pair prog MON 14:00 för att köra parallelt
```

---

## 📐 NPF-DESIGN REGLER (TVINGANDE)

### Whitespace
```
Toppadding:    20px minimum
Sidpadding:    16px minimum vänster/höger
Mellan sektioner: 24px minimum
Mellan bullets: 8px minimum
```

### Typografi
```
Rubrik (slides titel):     24-28pt, bold
Undernubrik (mötespunkt):  18-20pt, bold
Body text (bullets):       14-16pt, regular
Färger:                    Mörk text på ljus bakgrund (4.5:1 kontrast)
```

### Färger & Status
```
🟢 GRÖN (ON TRACK):        #2ecc71 (framsteg!)
🟠 ORANGE (SLIGHT DELAY):  #e67e22 (vi åtgärdar)
🔴 RÖD (CRITICAL):         #e74c3c (vi gör något)

Ikoner för att göra det lekfullt:
✅ Klart (framsteg!)
⏳ Pågår (vi jobbar)
⚠️ Blocker (men vi löser det)
🔴 Kritisk (vi gör något IDAG)
💪 Motiverande avslut
🎯 Fokus denna vecka
```

### Visuell Balans (för känslan av kontroll)
```
LAYOUT SOM GÖR DIG GLAD:
- Färg överst på slide (status-färg)
- Framsteg visas först (positiv start)
- Problem + LÖSNING tillsammans (inte bara problem)
- Whitespace mellan sektioner (andrum)
- Motiverande avslut ("Lycka till!")

LAYOUT SOM STRESSAR:
❌ All text buntat ihop
❌ Endast negativa saker utan lösning
❌ Dålig kontrast (svårt att läsa)
❌ För många färger (förvirrande)
❌ Ingen struktur (kaotisk)
```

### Borders & Frames — KRITISK REGEL

**FÄRGADE BORDERS = STATUS-BEDÖMNING ENDAST**

```
🟢 GRÖN border (3px solid #2ecc71):
   Betyder: ON TRACK / Vi når målet / Klart
   Använd på: Team-status cards, progress bars
   
🟠 ORANGE border (3px solid #e67e22):
   Betyder: SLIGHT DELAY / Försenat / Inte på målvägen än
   Använd på: Team-status cards med problem
   
🔴 RÖD border (3px solid #e74c3c):
   Betyder: CRITICAL / Behöver stärkas upp / Omedelbar åtgärd
   Använd på: Team-status cards med kritisk status
   
Padding inuti färgade borders: 16px
Border-radius: 4px (skarpa hörn)
Background: Ljus nyans av status-färg (10% opacity)
```

**SVART/VIT BORDER = BARA INFORMATION (ingen bedömning)**

```
⬛ SVART eller VIT border (2px solid):
   Betyder: Neutral information, ingen status-bedömning
   Använd på: 
     - Rubriker & innehål
     - Listor av issues (som inte är om framsteg)
     - Deadlines (information, inte status)
     - Åtgärdsförslag (innehål, inte bedömning)
   
Kontrast: HIGH (4.5:1 minimum vs background)
Padding inuti: 16px
Border-radius: 4px

EXEMPEL:
- MÅSTE HA svart border: Arbetsuppgifter lista (#42, #45, etc)
- MÅSTE HA svart border: Prioritering tabell (MÅSTE-HA | NICE-TO-HAVE)
- MÅSTE HA svart border: Deadlines lista
- MÅSTE HA färgad border: Team-status card (visar grön/orange/röd)
```

**REGEL: Blanda ALDRIG färgade borders med neutral information**

```
❌ FELAKTIGT (förvirrande):
Röd border runt "Prioritering & Scope" → ser ut som det är kritiskt
Grön border runt arbetslista → ser ut som allt är klart

✅ KORREKT (klart):
Svart border runt "Prioritering & Scope" (neutral info)
Svart border runt arbetslista (neutral info)
Röd border endast runt Native-teamstatus (visar faktisk kritisk status)
```

---

## 🎨 SYMBOLER & STATISTIK — ANVÄND ÖVERALLT

### Symboler för snabb överblick:

```
STATUS-SYMBOLER:
✅ Klart / Done / Delivered
⏳ Pågår / In Progress
🔜 Planerat / Upcoming / Inte startad
⚠️ Blocker / Problem / Risk
🔴 Kritisk / Critical / Omedelbar åtgärd
🟢🟠🔴 Status-färger (grön/orange/röd)

KONTEXT-SYMBOLER:
💪 Motiverande / Vi löser detta!
🎯 Fokus denna vecka
📊 Statistik / Data visar
📈 Trend / Utveckling
🔗 Beroende / Väntar på
👥 Assignee / Person
⏰ Deadline / Tid
🚀 Launch / Ready to go
🛠️ Under konstruktion / Building
📋 Checklist / Plan
🤝 Samarbete / Together
🚨 Urgent / Immediate
```

### Statistik (alltid visa konkret data):

```
PROGRESS:
████░░ Progress bar (visuell framsteg)
80%, 60%, 40% (procenttal)
4/5 issues done (ratio — vad/totalt)
Fortskridande: 14/17 (framsteg mot mål)

KAPACITET:
18h needed / 20h available (timmar)
Pass vi? Ja/Nej
Buffer: 2h kvar

DEADLINES:
MON 14:00 (konkret tid, inte "snart")
THU 15:00 (när måste det vara klart)
I dag / Denna vecka / Nästa vecka

TEAM:
2/3 assignees working (vem jobbar)
3 blockers identified (antal problem)
1 critical issue (prioritet)
```

---

## 🎬 SLIDE-FORMAT EXEMPEL

### **SLIDE 0.1 — 📝⓪ PRESENTATIONSSLIDE (ENKEL & KORT)**

```
╔════════════════════════════════════════════════╗
║ 📝⓪ MÅNDAGSMÖTE                                ║
║                                                ║
║                                                ║
║ Typ: SPRINT PLANNING                           ║
║ Tid: 09:00-10:30 (90 minuter)                  ║
║                                                ║
║ Syfte denna vecka:                             ║
║ Planera, prioritera & se vad som blockerar    ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- ENKEL — bara möte-typ, tid, syfte
- Symbol 📝⓪ ÖVERST VÄNSTER
- Max 3 rader innehål
- MYCKET whitespace (70% tom yta)
- Ingen tema, ingen agenda, ingen long list
- Detta är bara "här är mötet", sen kommer resten
```

---

### **🆕 SLIDE 0.1.5 — 📅 VECKANS SCHEMA & MÅL (NYTT!)**

```
╔════════════════════════════════════════════════╗
║ 📅 VECKANS SCHEMA & MÅLSÄTTNING                ║
║                                                ║
║ ┌──────────────────────────────────────────┐  ║
║ │ 🎯 DENNA VECKA SKA VI UPPNÅ:             │  ║
║ └──────────────────────────────────────────┘  ║
║                                                ║
║ 📚 KURSMÅL DENNA VECKA:                        ║
║ ✅ Adressera kursmål #5-7 (Git historik)      ║
║ ✅ Slutföra individuell dokumentation          ║
║ ✅ Framsteg: 14/17 → 16/17 kursmål            ║
║                                                ║
║ 🚀 PROJEKTMÅL DENNA VECKA:                     ║
║ ✅ Portfolio dashboard fungerar end-to-end    ║
║ ✅ Risk metrics calculation live               ║
║ ✅ Backend API testad med Frontend             ║
║ ✅ Framsteg: 75% → 85% MVP                    ║
║                                                ║
║ ┌──────────────────────────────────────────┐  ║
║ │ ⏰ VECKANS TIDSPLAN:                     │  ║
║ └──────────────────────────────────────────┘  ║
║                                                ║
║ 📍 MON 09:00  Sprint Planning möte (90 min)   ║
║ 📍 MON 14:00  Backend + Native pair prog      ║
║ 📍 TUE 10:00  Frontend möte                   ║
║ 📍 TUE 13:00  Halvtids-checkup möte          ║
║ 📍 WED 14:00  Sharpe spec ready (väntat)     ║
║ 📍 THU 15:00  SPRINT END (allt klart!)       ║
║ 📍 THU 17:00  CTO demo (feedback)            ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Svart border (neutral info, ingen status-bedömning)
- Två spalter visuell: KURSMÅL | PROJEKTMÅL
- Tydliga deadlines med konkret tid (inte bara "denna vecka")
- Symbols: 📚 🚀 📍 ⏰ ✅
- Visuell progress: "från 75% → 85%"
- Konkreta handlingar (vad ska hända DENNA VECKA)
```

---

### **SLIDE 1 — 📝① ÖVERGRIPANDE MÅL (DEL 1: KURSEN)**

```
╔════════════════════════════════════════════════╗
║ 📝① KURSEN — VAD BEHÖVER VI UPPNÅ?             ║
║                                                ║
║                                                ║
║ Mål: Uppfylla alla 17 kursmål → G/VG betyg    ║
║                                                ║
║ Deadlines:                                     ║
║ 🔴 4 november 15:00 — SLUTLEVERANS             ║
║ 🟠 5 november 09:00 — FINALDAG (om topp 4)    ║
║                                                ║
║ Status denna vecka: 🟢 ON TRACK                ║
║                                                ║
║ Fortskridande: 14/17 kursmål adresserade      ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Symbol 📝① överst
- Deadlines med färgkodning (🔴🟠🟢)
- Status-färg ÖVERST HÖGER på slide
- Copy-paste-friendly format
- Bullets alignerade vänster
```

---

### **SLIDE 2 — 📝① ÖVERGRIPANDE STATUS (DEL 2: PROJEKTET)**

```
╔════════════════════════════════════════════════╗
║ 📝① PROJEKTET — MVP v2 LEVERABLES             ║
║                                                ║
║                                                ║
║ Mål: Funktionerande MVP som löser Annas       ║
║       problem                                  ║
║                                                ║
║ MVP Scope:                                     ║
║ ✅ Portföljöversikt (alla sparformer)         ║
║ ✅ Riskmått (volatilitet, Sharpe)             ║
║ ✅ Back-testing motor                          ║
║ ✅ FX-justering                                ║
║ ✅ Rebalanserings-förslag                      ║
║                                                ║
║ Status denna vecka: 🟢 ON TRACK                ║
║ Fortskridande: 4/5 features klara             ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Samma layout som förra slide
- ✅-markörer för färdig funktion
- Status-färg tydlig
```

---

### **SLIDE 3 — 📝① PROGRESS BOARD (DEL 3: BIG PICTURE)**

```
╔════════════════════════════════════════════════╗
║ 📝① PROGRESS BOARD — MÅLSYSTEM + TEAM         ║
║                                                ║
║                                                ║
║ ┌──────────────────────────────────────────┐  ║
║ │ 🟢 BIG TEAM — VÄG TILL SLUTLEVERANS     │  ║
║ │                                          │  ║
║ │ Deadline: 4 november 15:00               │  ║
║ │                                          │  ║
║ │ Kursmål:  ████████░░ 80% (14/17)        │  ║
║ │ Projekt:  ████████░░ 75% (4/5 features) │  ║
║ │ Kund:     ███████░░░ 70% (Annas behov)  │  ║
║ │                                          │  ║
║ │ Status: 🟢 ON TRACK                      │  ║
║ └──────────────────────────────────────────┘  ║
║                                                ║
║ ┌──────────────────┐ ┌──────────────────┐     ║
║ │ 🟢 FRONTEND      │ │ 🟠 BACKEND       │     ║
║ │ ████████░░ 80%  │ │ ██████░░░░ 60%   │     ║
║ │ 4/5 done        │ │ 2/4 done (1 wait)│     ║
║ │ ON TRACK        │ │ SLIGHT DELAY     │     ║
║ └──────────────────┘ └──────────────────┘     ║
║                                                ║
║ ┌──────────────────┐                          ║
║ │ 🔴 NATIVE        │                          ║
║ │ ████░░░░░░ 40%  │                          ║
║ │ 1/3 done        │                          ║
║ │ CRITICAL 🚨     │                          ║
║ └──────────────────┘                          ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Borders RUNT team-status (3px solid färg)
- 🟢🟠🔴 färger MÅSTE finnas
- Progress bars (████░░)
- Separated cards för big team + small teams
- Status-ord (ON TRACK / SLIGHT DELAY / CRITICAL) tydligt
```

---

### **SLIDE 4 — 📝② FRONTEND TEAM STATUS**

```
╔════════════════════════════════════════════════╗
║ 📝② FRONTEND TEAM — 🟢 ON TRACK                ║
║                                                ║
║ ┌──────────────────────────────────────────┐  ║
║ │ 🟢 FRONTEND TEAM                         │  ║
║ │ Progress: ████████░░ 80%                 │  ║
║ │ Issues: 4/5 done                         │  ║
║ │ Assignees: Jan, Marco                    │  ║
║ └──────────────────────────────────────────┘  ║
║                                                ║
║ Klart denna vecka:                            ║
║ ✅ #42 Portfolio overview (Jan)               ║
║ ✅ #45 Risk dashboard (Marco)                 ║
║                                                ║
║ Pågår:                                        ║
║ ⏳ #51 Rebalance suggestions (Jan)            ║
║                                                ║
║ Blockers: ❌ Ingen                             ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Border RUNT team-card (3px solid 🟢)
- Progress bar (████░░)
- ✅ för klara items
- ⏳ för pågår
- ❌ för blockers
- Assignee namn obligatoriskt
```

---

### **SLIDE 5 — 📝③ BACKEND TEAM STATUS (MED ÅTGÄRD)**

```
╔════════════════════════════════════════════════╗
║ 📝③ BACKEND TEAM — 🟠 SLIGHT DELAY             ║
║                                                ║
║ ┌──────────────────────────────────────────┐  ║
║ │ 🟠 BACKEND TEAM                          │  ║
║ │ Progress: ██████░░░░ 60%                 │  ║
║ │ Issues: 2/4 done                         │  ║
║ │ Assignees: Anna, Kiran                   │  ║
║ └──────────────────────────────────────────┘  ║
║                                                ║
║ Klart denna vecka:                            ║
║ ✅ #48 Risk metrics (Anna)                    ║
║                                                ║
║ Bakom plan:                                   ║
║ ⏳ #51 FX conversion (Kiran) — väntar data  ║
║                                                ║
║ BLOCKER: ⚠️ Swagger spec från API team        ║
║ Förväntat: ONSDAG 14:00                       ║
║                                                ║
║ ÅTGÄRD:                                       ║
║ → Kiran startar Core calc (oberoende)        ║
║ → Möte TIS 10:00 för spec-draft               ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Orange border (🟠) för SLIGHT DELAY
- ⚠️ för kritisk blocker
- ÅTGÄRD-sektion tydlig (vad gör vi?)
- Deadlines för åtgärder (datum + tid)
- Action items som konkreta steg (inte vaga)
```

---

### **SLIDE 6 — 📝④ NATIVE TEAM STATUS (KRITISK)**

```
╔════════════════════════════════════════════════╗
║ 📝④ NATIVE TEAM — 🔴 CRITICAL 🚨              ║
║                                                ║
║ ┌──────────────────────────────────────────┐  ║
║ │ 🔴 NATIVE TEAM                           │  ║
║ │ Progress: ████░░░░░░ 40%                 │  ║
║ │ Issues: 1/3 done                         │  ║
║ │ Assignee: Sam                            │  ║
║ └──────────────────────────────────────────┘  ║
║                                                ║
║ Klart denna vecka:                            ║
║ ✅ #40 App setup (Sam)                       ║
║                                                ║
║ KRITISK BLOCKER 🔴:                           ║
║ ❌ Sharpe formula spec SAKNAS                 ║
║ ❌ API endpoint inte redo                     ║
║ Påverkan: Native kan inte testa               ║
║                                                ║
║ OMEDELBAR ÅTGÄRD:                             ║
║ 🔴 Backend + Native pair prog IDAG 14:00     ║
║    • Spec writing (1 hour)                    ║
║    • Implementation (3 hours)                 ║
║    • Deadline: SAMMA DAG 17:00               ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- RÖD border (🔴) för CRITICAL
- 🚨 OMEDELBAR ÅTGÄRD section måste finnas
- Konkreta tidsestimat (1h, 3h)
- Deadline SAMMA DAG om kritisk
- Bold eller highlighting för "OMEDELBAR"
```

---

### **SLIDE 7 — 📝⑤ PRIORITERING & SCOPE**

```
╔════════════════════════════════════════════════╗
║ 📝⑤ PRIORITERING & SCOPE — KAN VI GÖRA ALLT?  ║
║                                                ║
║ ┌─────────────────────┬─────────────────────┐ ║
║ │ 🟢 MÅSTE-HA DENNA   │ 🟠 NICE-TO-HAVE     │ ║
║ │    VECKA            │                     │ ║
║ │                     │                     │ ║
║ │ #42 Portfolio (3h)  │ #99 Dark mode (2h)  │ ║
║ │ #45 Risk calc (5h)  │ #100 Export (1h)   │ ║
║ │ #48 Tests (4h)      │                     │ ║
║ │ #51 Core flow (6h)  │                     │ ║
║ │                     │                     │ ║
║ │ TOTAL: 18h          │ TOTAL: 3h           │ ║
║ └─────────────────────┴─────────────────────┘ ║
║                                                ║
║ Kapacitet denna vecka: 20h                    ║
║                                                ║
║ ✅ JAM VI GÖR ALLT? Ja, 18h passar inom 20h  ║
║                                                ║
║ 🟠 NICE-TO-HAVE: Kan vänta till nästa vecka  ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Tabell-layout (två spalter: MÅSTE-HA | NICE-TO-HAVE)
- Timestimat på VARJE issue
- Summa totalt
- Kapacitet tydlig
- RESULTAT: "Passar vi?" med 🟢 eller 🟠 eller 🔴
```

---

### **SLIDE 8 — 📝⑥ ESTIMERING & RISK**

```
╔════════════════════════════════════════════════╗
║ 📝⑥ ESTIMERING & RISK                          ║
║                                                ║
║ ┌──────────────────────────────────────────┐  ║
║ │ KAPACITET DENNA VECKA                    │  ║
║ │                                          │  ║
║ │ Frontend:  20h available / 15h needed   │  ║
║ │ Backend:   18h available / 18h needed   │  ║
║ │ Native:    15h available / 25h needed   │  ║
║ │                                          │  ║
║ │ ✅ Frontend: OK (5h buffer)              │  ║
║ │ 🟡 Backend:  TIGHT (0h buffer)           │  ║
║ │ 🔴 Native:   OVER 10h saknas!            │  ║
║ └──────────────────────────────────────────┘  ║
║                                                ║
║ 🔴 KRITISK RISK:                              ║
║ Native kan inte allt denna vecka              ║
║                                                ║
║ MITIGATION:                                   ║
║ • Delay #100 (2h) till nästa vecka            ║
║ • Backend stödjar Native (pair prog)          ║
║ • Resultat: Native 15h, passar inom 15h ✅   ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Tabell med AVAILABLE | NEEDED
- ✅🟡🔴 status för varje team
- Risk highlighted (🔴 KRITISK RISK)
- Mitigation konkret (vad gör vi?)
- Resultat: "Passar vi?" efter åtgärd
```

---

### **SLIDE 9 — 📝⑦ ARBETSUPPGIFTER (ISSUES DENNA VECKA)**

```
╔════════════════════════════════════════════════╗
║ 📝⑦ ARBETSUPPGIFTER — ISSUES DENNA VECKA      ║
║                                                ║
║ ┌─────────────────────────────────────────┐   ║
║ │ FRONTEND                                │   ║
║ │ [ ] #42 Portfolio overview (Jan) - 3h  │   ║
║ │ [ ] #45 Risk dashboard (Marco) - 5h    │   ║
║ │ [ ] #51 Rebalance (Jan) - 7h            │   ║
║ │ [ ] #52 Export CSV (Jan föreslaget) - 4h│   ║
║ └─────────────────────────────────────────┘   ║
║                                                ║
║ ┌─────────────────────────────────────────┐   ║
║ │ BACKEND                                 │   ║
║ │ [ ] #48 Risk metrics (Anna) - 4h        │   ║
║ │ [ ] #51 FX conversion (Kiran) - 5h      │   ║
║ │ [ ] #52 Tests (Anna) - 9h               │   ║
║ │ [ ] #53 Performance (Marco föreslaget) -2h│   ║
║ └─────────────────────────────────────────┘   ║
║                                                ║
║ ┌─────────────────────────────────────────┐   ║
║ │ NATIVE                                  │   ║
║ │ [ ] #40 App setup (Sam) - 5h            │   ║
║ │ [ ] #53 Integration (Sam) - 10h         │   ║
║ └─────────────────────────────────────────┘   ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Per-team boxes (borders)
- Checkboxes [ ] för copy-paste
- #issue-nummer
- **ASSIGNEE namn TVINGANDE:**
  - Om GitHub visar: (#XX - Namn)
  - Om ingen assignee: (#XX - Namn föreslaget) baserat på git log
  - SYFTE: Sammanlänka issues (samma person fortsätter sitt arbete)
- Timestimat (h) — faktiska estimat
- Kan copy-pastas direkt till protokollet
```

---

### **SLIDE 8.5 — 🆕 BLOCKERS — VISUELL FLOWCHART (SEPARAT SLIDE)**

```
╔════════════════════════════════════════════════╗
║ 🚨 BLOCKERS — HUR BLOCKAR DE OSS?              ║
║                                                ║
║ BLOCKER 1: Sharpe formula spec                 ║
║ ┌────────────────────────────────────────┐    ║
║ │ VÄNTAR PÅ: Backend API team            │    ║
║ │ BLOCKERAR:                              │    ║
║ │   → Native implementation (#40)         │    ║
║ │   → Frontend testing (#51)              │    ║
║ │                                         │    ║
║ │ STATUS: 🔴 CRITICAL                    │    ║
║ │ FÖRVÄNTAS: WED 14:00                    │    ║
║ │ ÅTGÄRD: Backend + Native pair prog     │    ║
║ │          MON 14:00-17:00               │    ║
║ └────────────────────────────────────────┘    ║
║                                                ║
║ BLOCKER 2: Test data fixtures                 ║
║ ┌────────────────────────────────────────┐    ║
║ │ VÄNTAR PÅ: QA team (externa)           │    ║
║ │ BLOCKERAR:                              │    ║
║ │   → All integration testing             │    ║
║ │   → Performance validation              │    ║
║ │                                         │    ║
║ │ STATUS: 🟠 SLIGHT DELAY                │    ║
║ │ FÖRVÄNTAS: THU 09:00                    │    ║
║ │ ÅTGÄRD: Mock fixtures denna dag        │    ║
║ │          tills externa data kommer     │    ║
║ └────────────────────────────────────────┘    ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Visuell blockeringskedja (vad blockeras av vad)
- 🚨 VISUELL — pilar visar block-relationer
- Vem blockerar vem / vilken team / vilken extern
- Förväntat datum för lösning (konkret)
- Åtgärd nu (vad gör vi medan vi väntar)
- ⬛ Svart border (neutral information, inte status-bedömning)
- Status-färger INOM blockers (🔴🟠 visar allvarlighetsgrad)
```

---

### **SLIDE 10 — 📝⑧ NÄSTA STEG & SUMMARY**

```
╔════════════════════════════════════════════════╗
║ 📝⑧ NÄSTA STEG & SUMMARY                       ║
║                                                ║
║ NÄSTA STEG (IDAG):                            ║
║                                                ║
║ ☐ GitHub Project Board uppdaterad             ║
║ ☐ Pair programming sessions bokade:           ║
║   • Backend + Native: IDAG 14:00 (3h)         ║
║   • Frontend + Backend: TIS 10:00 (1h)        ║
║ ☐ Alla vet sitt jobb & timestimat            ║
║ ☐ Blockers documented i GitHub                ║
║                                                ║
║ DENNA VECKAS DEADLINES:                       ║
║                                                ║
║ MON 17:00  — Native spec done (KRITISK)       ║
║ TUE 14:00  — #42 #45 klara (Frontend)         ║
║ WED 09:00  — #48 #51 klara (Backend)          ║
║ THU 15:00  — SPRINT END (allt klart)          ║
║                                                ║
║ DENNA VECKAS FOKUS:                           ║
║ "Risk prioritization & team capacity"         ║
║                                                ║
║ ÖVERGRIPANDE STATUS: 🟢 ON TRACK (med        ║
║ Native support från Backend)                  ║
║                                                ║
║ Lycka till denna vecka! 💪                    ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Checkboxes [ ] för actionitems
- Deadlines tydliga (DAY HH:MM)
- Färger för kritiska deadlines (🔴)
- Sammanfattning: FOKUS + STATUS
- Motiverande avslut
```

---

## 🚨 CHECKLIST FÖR AI — INNAN DU LEVERERAR

✅ **OBLIGATORISK CHECKLIST:**

```
🔴 KÄLLKRAV & SANNINGSCHECK (VIKTIGAST!):
  [ ] 🚫 INGENTING är fabricerat — ALLT från verifierade källor
  [ ] Kursmål denna vecka: från KURSMAL_OCH_BETYG.md
  [ ] Projektmål denna vecka: från GitHub Project Board + Mötesprotokollet
  [ ] Tidsplan: från mötesprotokollet (vilka möten är bokade?)
  [ ] Team status (grön/orange/röd): från git log + actual commits
  [ ] Blockers: från mötesprotokollet + GitHub issues
  [ ] Åtgärdsförslag: från mötesprotokollet (INTE AI gissningar)
  [ ] DATA matchar MÖTESPROTOKOLLET (ingen feltolkningar)
  [ ] Om vi är KRITISK (🔴) → texten säger KRITISK (inte dolt)
  [ ] Om vi ligger EFTER → texten säger det klart (inte dolt)
  [ ] Inga LÖJ-positiva tal ("vi löser detta") om data visar motsatsen
  [ ] Alla blockers är namngivna + timeline från mötet
  [ ] Åtgärder är KONKRETA (datum, tid, person från mötesprotokollet)

Symbol & Numrering:
  [ ] VARJE slide har symbol 📝① eller 📝⓪ överst VÄNSTER
  [ ] Symbol matchar SPRINT_PROTOCOL_NUMBERED.md (ingen blandning)
  [ ] Symbolen är TYDLIG (inte dold eller liten)

Färger & Status:
  [ ] 🟢🟠🔴 färger matchar FAKTISK status (inte design-känsla)
  [ ] Green = ON TRACK med data som visar ON TRACK
  [ ] Orange = DELAY med konkret data om vad som ligger efter
  [ ] Red = CRITICAL med omedelbar åtgärd specificerad
  [ ] Färgerna ANVÄND konsistent överallt

Design & Layout:
  [ ] 🟢🟠🔴 Färgade borders (3px) ENDAST på team-status cards
  [ ] ⬛ Svart/vit borders (2px) på neutral information (prioritering, deadlines, listor)
  [ ] Progress bars (████░░) på team-status slides
  [ ] Tabeller (MÅSTE-HA | NICE-TO-HAVE) på prioritering — svart border
  [ ] Checkboxes [ ] på arbetsuppgifter för copy-paste — svart border
  [ ] ALDRIG färgad border på non-status information
  [ ] Hög kontrast (4.5:1) på alla borders

Whitespace & Typografi:
  [ ] 60-70% tom yta på varje slide
  [ ] Toppadding 20px, sidpadding 16px
  [ ] Ingen text-overlap
  [ ] Kontrast 4.5:1 minimum (WCAG AA)

Innehål:
  [ ] Max 3-5 bullets per sektion
  [ ] Deadlines med tid (HH:MM) — faktiska deadlines
  [ ] **ASSIGNEE på VARJE issue:** (#XX - Namn)
  [ ] Timestimat på varje issue — faktiska estimat
  [ ] ÅTGÄRD-sektion på röda slides (CRITICAL) + konkreta steg

📌 ASSIGNEE-REGEL (KRITISK):
  [ ] **VARJE issue nummer MÅSTE ha assignee i parentes**
  [ ] Format: (#42 - Jan) eller (#42 - Jan föreslaget)
  [ ] Om GitHub visar assignee → använd det: (#42 - Jan)
  [ ] Om ingen assignee → FÖRESLÅ baserat på git log:
      • Vem har arbetat på liknande issues tidigare?
      • Vem skrev commits för samma feature-område?
      • Format då: (#42 - Jan föreslaget, baserat på portfolio-arbete)
  [ ] SYFTE: Få sammanlänkade issues (samma person fortsätter sitt arbete)

Format:
  [ ] PowerPoint eller Google Slides eller Markdown
  [ ] Allt kan copy-pastas direkt till mötesprotokollet
  [ ] Samma struktur som dessa EXEMPEL-SLIDES

TOTALT:
  [ ] ~16-20 slides (beroende på innehål)
      (mer innehål OK nu: schema, blockers, statistik)
  [ ] Alla 📝⓪-⑫ punkter representerade
  [ ] SEPARAT slide för blockers visualisering
  [ ] SEPARAT slide för veckans schema & mål
  [ ] NPF-vänlig (förutsägbar, visuell, lättläst)
  [ ] ÄRLIG DATA utan vilseledning
```

---

## 💡 TIPS FÖR CONSISTENCY

**Samma design varje vecka = Teamet känner igen den**

- Punkt ① är ALLTID övergripande (med 3 målsystem)
- Punkt ②③④ är ALLTID team-status (med borders & färger)
- Punkt ⑤ är ALLTID prioritering (tabell-layout)
- Punkt ⑥ är ALLTID estimering (kapacitet-tabell)
- Punkt ⑦ är ALLTID issues (per-team boxes)
- Punkt ⑧ är ALLTID nästa steg (deadlines + summary)

**Resultat:** Mötet flyter snabbt, desigben är tydlig, protokollet blir korrekt.

---

## 🤖 FÖR EXTERNA AIs

**Om du är AI och ska skapa presentation:**

1. ✅ Läs denna fil från början
2. ✅ Kopiera LAYOUT från EXEMPEL-SLIDES ovan
3. ✅ Ersätt data med denna veckas information
4. ✅ Verifiera CHECKLIST innan leverans
5. ✅ Leverera i PowerPoint, Google Slides, eller Markdown

**ALDRIG:**
- ❌ Skapa egen design (använd DESSA exempel)
- ❌ Skippa borders runt team-status
- ❌ Glömma färger (🟢🟠🔴)
- ❌ Mindre än 10 slides
- ❌ Skippa checkboxes på arbetsuppgifter
- ❌ Dålig kontrast eller text-overlap

**Du har MISSLYCKATS om något av checklist-items inte är gjort.**
