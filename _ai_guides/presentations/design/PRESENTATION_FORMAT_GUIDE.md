---
name: presentation_format_guide
description: Exakt layout för varje slide — visuell formatering, design-regler, konkreta exempel
metadata:
  type: reference
  critical: true
  version: 1.0
---

# 🎨 PRESENTATION FORMAT GUIDE — Layout & Design för Varje Slide

**⚠️ DENNA FIL KOMPLETTERAR PRESENTATION_STRUCTURE.md**  

Se PRESENTATION_STRUCTURE.md för:
- 14 mötespunkter (①-⑧ eller ①-⑭)
- Vilka data-källor som används
- Vad varje mötespunkt MÅSTE innehålla

**Denna fil visar BARA:**
- Visuella layouts & designexempel
- Border-regler (färgade vs neutrala)
- Format-specifikation (PowerPoint/Slides/Markdown)
- Checklist FÖR AI innan leverans

---

## 🎯 MEGA-REGEL 0A: INDIVIDPERSPEKTIV — KRITISK REGEL

**En teammedlem ska aldrig behöva tolka projektstatus för att förstå vad den själv ska göra.**

När en slide visar ett problem MÅSTE den, när relevant, också visa konsekvensen för arbetets och nästa handling:

```
🔴 DÅLIGT EXEMPEL:
"Frontend är orange. Auth är blockerad."

🟢 BRA EXEMPEL:
"Frontend är orange eftersom #40 Auth väntar på backend.
Lisa fortsätter #40 med mockad integration.
Ali fortsätter #52 Responsive Design eftersom den inte är blockerad.
= I morgon kan Lisa börja integration när backend är klar."
```

**INFORMATIONSKEDJAN SOM MÅSTE FINNAS:**
```
Projektets status → Teamets läge → Min personliga situation → Min nästa handling
```

Om någon länk saknas är presentationen ofullständig.

---

## 🚨 MEGA-REGEL 0B: SANNINGEN FÖRE KÄNSLAN

**Blanda ALDRIG ihop design-känslan med faktisk data!**

```
🔴 ALDRIG:
- "Vi löser detta!" (känsla) när data visar KRITISK
- Snygga design för att dölja att vi ligger efter
- Optimistisk ton när projektet riskerar att INTE gå i mål
- Färger som inte matchar faktisk status

✅ ALLTID:
- Ärlig data: om vi är KRITISK → säg "🔴 KRITISK"
- Konkreta åtgärder: vad gör vi IDAG för att lösa det?
- Transparent bedömning: visa både problem OCH lösning
- Färger som matchar verkligheten
```

---

## 🎨 BORDER-REGLER — KRITISK REGEL

### Färgade borders = STATUS-BEDÖMNING ENDAST

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
Border-radius: 4px
Background: Ljus nyans av status-färg (10% opacity)
```

### Svart/Vit border = BARA INFORMATION (ingen bedömning)

```
⬛ SVART eller VIT border (2px solid):
   Betyder: Neutral information, INGEN status-bedömning
   Använd på:
     - Rubriker & innehål
     - Listor av issues (som inte är om framsteg)
     - Deadlines (information, inte status)
     - Åtgärdsförslag (innehål, inte bedömning)
     - Prioritering-tabeller
     - Arbetsuppgifter-listor

Kontrast: HIGH (4.5:1 minimum vs background)
Padding inuti: 16px
Border-radius: 4px

REGEL: Blanda ALDRIG färgade borders med neutral information
```

---

## 📐 NPF-DESIGN REGLER (TVINGANDE)

### Whitespace
```
Toppadding:        20px minimum
Sidpadding:        16px minimum vänster/höger
Mellan sektioner:  24px minimum
Mellan bullets:    8px minimum
Målsättning:       60-70% tom yta per slide
```

### Typografi
```
Rubrik (slides titel):     24-28pt, bold
Underrubrik (mötespunkt):  18-20pt, bold
Body text (bullets):       14-16pt, regular
Meta-text (footer):        10-12pt, diskret
Färger:                    Mörk text på ljus bakgrund (4.5:1 kontrast)
Font:                      Sans-serif (Arial, Helvetica, eller system-default)
```

### Färger & Status
```
🟢 GRÖN (ON TRACK):        #2ecc71
🟠 ORANGE (SLIGHT DELAY):  #e67e22
🔴 RÖD (CRITICAL):         #e74c3c
⬛ SVART/VIT (neutral):    #333333 / #ffffff
```

### Visuell Balans
```
LAYOUT SOM GÖR DIG GLAD:
- Färg/status överst på slide
- Framsteg visas först (positiv start)
- Problem + LÖSNING tillsammans (inte bara problem)
- Whitespace mellan sektioner (andrum)
- Motiverande avslut på sammanfattnings-slide

LAYOUT SOM STRESSAR:
❌ All text buntat ihop
❌ Endast negativa saker utan lösning
❌ Dålig kontrast (svårt att läsa)
❌ För många färger (förvirrande)
❌ Ingen struktur (kaotisk)
```

---

## 💫 SYMBOLER & STATISTIK — ANVÄND ÖVERALLT

### Symboler för snabb överblick:

```
STATUS-SYMBOLER:
✅ Klart / Done / Delivered
⏳ Pågår / In Progress
🔜 Planerat / Upcoming
⚠️ Blocker / Problem / Risk
🔴 Kritisk / Critical
🟢🟠🔴 Status-färger

KONTEXT-SYMBOLER:
💪 Motiverande
🎯 Fokus denna vecka
📊 Statistik / Data
📈 Trend / Utveckling
🔗 Beroende / Väntar på
👥 Assignee / Person
⏰ Deadline / Tid
📋 Checklist / Plan
🤝 Samarbete
🚨 Urgent
```

### Statistik (alltid visa konkret data):

```
PROGRESS:
████░░ Progress bar (visuell framsteg)
80%, 60%, 40% (procenttal)
4/5 issues done (ratio)

KAPACITET:
18h needed / 20h available
Pass vi? Ja/Nej

DEADLINES:
MON 14:00 (konkret tid, inte "snart")
THU 15:00 (när måste det vara klart)

TEAM:
2/3 assignees working (vem jobbar)
3 blockers identified
1 critical issue
```

---

## 🎬 SLIDE-FORMAT EXEMPEL

### **SLIDE 0 — PRESENTATIONSSLIDE (ENKEL)**

```
╔════════════════════════════════════════════════╗
║ 📝⓪ SPRINTMÖTE                                 ║
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
- Symbol 📝⓪ ÖVERST VÄNSTER
- Max 3 rader innehål
- MYCKET whitespace (70% tom yta)
- Ingen färg, ingen agenda, ingen lista
```

---

### **SLIDE 1 — TEAM STATUS (MED FÄRGAD BORDER)**

```
╔════════════════════════════════════════════════╗
║ 📝① FRONTEND TEAM — 🟢 ON TRACK                ║
║                                                ║
║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓    ║
║ ┃ 🟢 FRONTEND TEAM                       ┃    ║
║ ┃ Progress: ████████░░ 80%                ┃    ║
║ ┃ Issues: 4/5 done                       ┃    ║
║ ┃ Assignees: Jan, Marco                  ┃    ║
║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    ║
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
- GRÖN 3px border (solid) RUNT team-card (box = 🟢 ON TRACK)
- Padding 16px inuti
- Progress bar (████░░)
- ✅ för klara, ⏳ för pågår
- Assignee namn obligatoriskt (#XX - Namn)
```

---

### **SLIDE 2 — BACKEND TEAM (MED ÅTGÄRD)**

```
╔════════════════════════════════════════════════╗
║ 📝② BACKEND TEAM — 🟠 SLIGHT DELAY             ║
║                                                ║
║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓    ║
║ ┃ 🟠 BACKEND TEAM                        ┃    ║
║ ┃ Progress: ██████░░░░ 60%                ┃    ║
║ ┃ Issues: 2/4 done                       ┃    ║
║ ┃ Assignees: Anna, Kiran                 ┃    ║
║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    ║
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
- ORANGE 3px border (solid) RUNT team-card (box = 🟠 SLIGHT DELAY)
- Padding 16px
- ÅTGÄRD-sektion tydlig (vad gör vi?)
- Deadlines konkreta (dag + tid)
```

---

### **SLIDE 3 — NATIVE TEAM (KRITISK)**

```
╔════════════════════════════════════════════════╗
║ 📝③ NATIVE TEAM — 🔴 CRITICAL 🚨              ║
║                                                ║
║ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓    ║
║ ┃ 🔴 NATIVE TEAM                         ┃    ║
║ ┃ Progress: ████░░░░░░ 40%                ┃    ║
║ ┃ Issues: 1/3 done                       ┃    ║
║ ┃ Assignee: Sam                          ┃    ║
║ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    ║
║                                                ║
║ Klart denna vecka:                            ║
║ ✅ #40 App setup (Sam)                       ║
║                                                ║
║ 🔴 KRITISK BLOCKER:                           ║
║ ❌ Sharpe formula spec SAKNAS                 ║
║ ❌ API endpoint inte redo                     ║
║ Påverkan: Native kan inte testa               ║
║                                                ║
║ 🚨 OMEDELBAR ÅTGÄRD:                          ║
║ Backend + Native pair prog IDAG 14:00         ║
║   • Spec writing (1 hour)                     ║
║   • Implementation (3 hours)                  ║
║   • Deadline: SAMMA DAG 17:00                ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- RÖD 3px border (solid) RUNT team-card (box = 🔴 CRITICAL)
- 🚨 OMEDELBAR ÅTGÄRD section obligatorisk
- Konkreta tidsestimat + deadlines
- Bold eller highlighting för "OMEDELBAR"
```

---

### **SLIDE 4 — PRIORITERING & SCOPE (NEUTRAL BORDER)**

```
╔════════════════════════════════════════════════╗
║ 📝④ PRIORITERING & SCOPE                       ║
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
║ ✅ JAM VI? Ja, 18h passar inom 20h           ║
║                                                ║
║ 🟠 NICE-TO-HAVE: Kan vänta till nästa vecka  ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- SVART 2px border (neutral — ingen status-bedömning)
- Tabell-layout (två spalter)
- Timestimat på VARJE issue
- Summa totalt
- RESULTAT: "Passar vi?" med status-svar
- Padding 16px inuti
```

---

### **SLIDE 5 — ARBETSUPPGIFTER (CHECKBOXES)**

```
╔════════════════════════════════════════════════╗
║ 📝⑤ ARBETSUPPGIFTER — DENNA VECKA              ║
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
║ │ [ ] #53 Performance (Marco föreslaget) -2h │   ║
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
- SVART 2px border per team-box (neutral)
- Padding 16px
- [ ] Checkboxes för copy-paste till protokoll
- **ASSIGNEE namn TVINGANDE:**
  Format: #issue-nummer Titel (Namn) - Xh
  Exempel: #42 Portfolio overview (Jan) - 3h
  Om föreslaget: #52 Export CSV (Jan föreslaget) - 4h
- Timestimat konkret
```

---

### **SLIDE 6 — BLOCKERS (VISUELL FLOWCHART)**

```
╔════════════════════════════════════════════════╗
║ 🚨 BLOCKERS — VAD BLOCKERAR VAD?               ║
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
║ │                                         │    ║
║ │ STATUS: 🟠 SLIGHT DELAY                │    ║
║ │ FÖRVÄNTAS: THU 09:00                    │    ║
║ │ ÅTGÄRD: Mock fixtures medan vi väntar  │    ║
║ └────────────────────────────────────────┘    ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- SVART 2px border per blocker (neutral)
- Visuell blockering-kedja tydlig
- Förväntat datum konkret
- Åtgärd specifik (vad gör vi medan vi väntar?)
- Status-färg INOM text (🔴🟠 visar allvar)
```

---

### **SLIDE 7 — SAMMANFATTNING (MOTIVERANDE)**

```
╔════════════════════════════════════════════════╗
║ 📝⑥ SAMMANFATTNING — DENNA VECKA               ║
║                                                ║
║ 🎯 DENNA VECKAS FOKUS:                         ║
║ Risk prioritization & team capacity           ║
║                                                ║
║ 📊 STATUS ÖVERGRIPANDE:                        ║
║ 🟢 ON TRACK (med Native support från Backend) ║
║                                                ║
║ 📈 FRAMSTEG DENNA VECKA:                       ║
║ • Kursmål: 14/17 → 16/17 ✅                   ║
║ • Projekt: 75% → 85% MVP ✅                   ║
║ • Alla team vet sitt jobb ✅                  ║
║                                                ║
║ 🚨 KRITISKT ATT LÖSA:                          ║
║ Sharpe spec — Backend + Native pair prog idag ║
║                                                ║
║ 💪 LYCKA TILL DENNA VECKA!                     ║
║ Vi löser detta tillsammans.                   ║
║                                                ║
╚════════════════════════════════════════════════╝

REGLER:
- Fokus på denna veckan
- Status övergripande (🟢/🟠/🔴)
- Framsteg visuellt (tal + pil: från X → Y)
- Kritiska åtgärder högt upp
- MOTIVERANDE avslut
- Svart border (neutral sammanfattning)
```

---

## 🚨 CHECKLIST FÖR AI — INNAN DU LEVERERAR

✅ **OBLIGATORISK CHECKLIST:**

```
🔴 KÄLLKRAV & SANNINGSCHECK (VIKTIGAST!):
  [ ] INGENTING är fabricerat — ALLT från verifierade källor
  [ ] Data matchar MÖTESPROTOKOLLET (ingen feltolkningar)
  [ ] Om vi är 🔴 KRITISK → texten säger KRITISK (inte dolt)
  [ ] Om vi ligger EFTER → texten säger det klart (inte dolt)
  [ ] Inga löj-positiva tal ("vi löser detta") om data visar motsatsen
  [ ] Alla blockers är namngivna + timeline från mötet
  [ ] Åtgärder är KONKRETA (datum, tid, person)

Symbol & Numrering:
  [ ] VARJE slide har symbol 📝① eller 📝⓪ överst VÄNSTER
  [ ] Symbol är TYDLIG (inte dold eller liten)
  [ ] Symbolen matchar mötespunkter

Färger & Status:
  [ ] 🟢🟠🔴 färger matchar FAKTISK status (inte design-känsla)
  [ ] Green = ON TRACK
  [ ] Orange = DELAY med konkret data om vad som ligger efter
  [ ] Red = CRITICAL med omedelbar åtgärd
  [ ] Färgerna är KONSISTENTA överallt

Borders:
  [ ] 🟢🟠🔴 FÄRGADE borders (3px) ENDAST på team-status cards
  [ ] ⬛ SVART/VIT borders (2px) på neutral information
  [ ] ALDRIG färgad border på non-status information
  [ ] Padding 16px inuti borders
  [ ] Kontrast 4.5:1 minimum (WCAG AA)

Whitespace & Typografi:
  [ ] 60-70% tom yta på varje slide
  [ ] Toppadding 20px, sidpadding 16px
  [ ] Ingen text-overlap
  [ ] Kontrast 4.5:1 minimum (WCAG AA)

Innehål:
  [ ] Max 3-5 bullets per sektion
  [ ] Deadlines med tid (HH:MM) — faktiska deadlines
  [ ] **ASSIGNEE på VARJE issue:** (#XX - Namn)
  [ ] Timestimat på varje issue
  [ ] ÅTGÄRD-sektion på röda slides + konkreta steg

Checkboxes & Format:
  [ ] Checkboxes [ ] på arbetsuppgifter (copy-paste ready)
  [ ] Progress bars (████░░) på team-status slides
  [ ] Tabeller på prioritering-slides
  [ ] Kan copy-pastas direkt till mötesprotokollet

TOTALT:
  [ ] Minst 10-12 slides
  [ ] Alla kritiska mötespunkter representerade
  [ ] NPF-vänlig (förutsägbar, visuell, lättläst)
  [ ] ÄRLIG DATA utan vilseledning
  [ ] Motiverande avslut
```

---

**Version:** 1.0  
**Senast uppdaterad:** 2026-09-14  
**Status:** PRODUCTION — Format-standarder för alla presentationer
