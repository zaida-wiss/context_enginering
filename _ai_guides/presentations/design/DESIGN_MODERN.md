---
name: design_modern
description: Modern design — vackert, rundade hörn, semantiska färger, läsbar text, ADHD-vänligt
metadata:
  type: process
  critical: true
  replaces: VISUAL_DESIGN_MANDATORY
---

# 🎨 MODERN DESIGN — Vacker Presentation

**DENNA DESIGN ERSÄTTER gamla tråkiga tabeller och grå layout.**

---

## 🎯 DESIGN PRINCIPER

### 1. FÄRGER = BETYDELSE (Semantisk)

```
🟢 GRÖN (#4CAF50)      = FÄRDIG, KLART, LEVERERAT
🟡 ORANGE (#FF9800)    = PÅGÅR, WORK IN PROGRESS, VÄNTAR
🔴 RÖD (#F44336)       = BLOCKERAD, PROBLEM, KRITISK
⚪ GRÅ (#E0E0E0)       = OKÄND, INGEN AKTIVITET, INFORMATION
🔵 BLÅ (#2196F3)       = STRUKTUR, KATEGORI, GRUPPERING
🟣 LILA (#9C27B0)      = FOKUS, VIKTIG INFO, HIGHLIGHT

Regel: Färger är ALDRIG dekoration. Varje färg = ett budskap.
```

### 2. TEXTSTORLEKAR (Läsbara)

```
32pt BOLD       = Slide-titel (mötespunkt ①, ②, etc)
                  Standar: Arial/Helvetica Bold
                  Färg: Mörkgrå (#212121) eller mörkblå (#1565C0)

20pt BOLD       = Sektion-header (Frontend, Backend, Risk-register, etc)
                  Färg: Mörkgrå (#424242)
                  Margin-bottom: 16px (luftig)

16pt REGULAR    = Huvudinnehål (issue-titel, risk-beskrivning)
                  Färg: Mörkgrå (#424242)
                  Line-height: 1.6 (luftigt)

14pt REGULAR    = Sekundär info (assignee, datum, status)
                  Färg: Mörkgrå (#616161)

12pt SMALL      = Footer-info, källreferens
                  Färg: Ljusgrå (#9E9E9E)
                  Italic
```

### 3. SPACING & WHITESPACE (ADHD-vänligt)

```
Mellan slide-element:     24px (luftigt)
Mellan section-headers:   32px (tydlig paus)
Mellan cards/blocks:      16px (lätt att särskilja)
Mellan text-rader:        1.6x (mycket luftigt)
Side margins:             32px (inte för tätt)
Card padding:             16px-24px (inre luft)

Regel: Mer whitespace än text. Ögonen behöver vila.
```

### 4. RUNDADE HÖRN & MODERN STYLE

```
Card border-radius:       12px (modern, mjuk)
Button border-radius:     8px (liten, snäv)
Divider line:             1px #E0E0E0, ingen skugga

Skugga (subtil):          0 2px 4px rgba(0,0,0,0.1)
                          (inte dramatisk, bara djup)

Font-familie:             System font stack:
                          -apple-system, BlinkMacSystemFont,
                          "Segoe UI", Roboto, sans-serif
                          (modernt, clean)
```

---

## 📊 SLIDE LAYOUTS (Inte tabeller!)

### Layout 1: Issue/Task CARD (Ersätter tabell-rad)

```
┌─────────────────────────────────────────────────┐
│ 🟢 #95 Security review + merge                 │  ← färg = status
├─────────────────────────────────────────────────┤
│ Team: Backend      Assignad: Erik Berglund      │  ← info, mindre text
│ Status: ✓ DONE    Merged: 2026-09-13           │
│                                                  │
│ Vad: Verifikation av JWT-implementation        │  ← beskrivning
│ Risk: Låg          Review: 2 godkännanden       │
└─────────────────────────────────────────────────┘

CSS:
  border-left: 4px solid [färg];
  border-radius: 12px;
  padding: 16px;
  background: #F5F5F5;
  margin-bottom: 12px;
```

### Layout 2: Risk-BLOCK (Ersätter tabell)

```
┌──────────────────────────────────────────────────┐
│ 🔴 RISK — API-kontrakt inte klart              │  ← röd = kritisk
├──────────────────────────────────────────────────┤
│ Sannolikhet: HÖG    Påverkan: Frontend blockerad │
│                                                   │
│ Konsekvens:                                      │
│ Frontend kan inte integrera, pushes försenas     │
│                                                   │
│ Mitigation:                                      │
│ Erik + Björn möte idag 14:00 för att fastslå     │
│ kontrakt. Mockad API redan tillgänglig.          │
└──────────────────────────────────────────────────┘

CSS:
  border-left: 4px solid #F44336 (röd);
  border-radius: 12px;
  background: #FFEBEE (ljusröd bakgrund);
  padding: 16px;
```

### Layout 3: Progress BAR (Ersätter text)

```
Frontend Status denna vecka:

████████░░ 80% — 4/5 issues done
           ↑
        Grön färg (pågår bra)

Förklaring under:
• #95 Security review ✓
• #87 Test foundation ◐  
• #88 Critical interactions ◐
• #85 Responsive header ✓
• #89 E2E happy path (nästa vecka)

CSS:
  background: #E0E0E0 (ljusgrå, tom del);
  fill: [färg enligt status] (grön/orange/röd);
  height: 8px;
  border-radius: 4px;
  width: 200px (or 100% of container);
```

### Layout 4: Info-BOX (Enkelt & luftigt)

```
┌─────────────────────────────────┐
│ 🔵 TEAM: Frontend               │  ← blå = struktur
├─────────────────────────────────┤
│ Medlemmar: 3                    │
│ • Zaida Wiss                    │
│ • Björn Boman                   │
│ • Tomac Barin Jansson           │
│                                 │
│ Work denna vecka: 5 PRs merged  │
│ Status: 🟢 I tid                │
└─────────────────────────────────┘

CSS:
  border-left: 4px solid #2196F3 (blå);
  border-radius: 12px;
  background: #F3F5FF (ljusblå);
  padding: 16px;
  max-width: 300px;
```

### Layout 5: TIMELINE (För Fas-baserad ordning)

```
Fas 1 — Nu
├─ Zaida: #87 Test foundation          🟢 Ready
├─ Tomac: #43 API client + mock        🟢 Ready
└─ Björn: #81 Linked allocation        🟢 Ready

↓ (Efter merge + develop update)

Fas 2 — Nästa
├─ Zaida: #88 Critical interaction     🟡 Pågår
├─ Tomac: #82 usePortfolio            🟡 Planerad
└─ Björn: #85 Responsive header        🟡 Planerad

↓ (Efter #81 + #43 mergad)

Fas 3 — Stabilisering
├─ Zaida: Stabilisering #88            ⚪ Queue
├─ Tomac: #83 saveAllocation            ⚪ Queue
└─ Björn: #86 Responsive dashboard     ⚪ Queue

CSS:
  Vertical line: 1px #E0E0E0;
  Circles: 24px, färgade enligt status;
  Font: 14pt regular;
  Line-height: 2.0 (mycket luftigt);
```

---

## 🎯 KONKRETA EXEMPEL PER MÖTESPUNKT

### Punkt ① — Sedan förra mötet

```
FRONTEND — Levererat denna vecka

[Card] ✓ #95 Security review + merge (Erik)
       Merged 2026-09-13

[Card] ✓ #87 Test foundation (Rasha)
       Merged 2026-09-12

BACKEND — Levererat denna vecka

[Card] ✓ #80 Drift banner (Erik)
       Merged 2026-09-11

NATIVE — Levererat denna vecka

[INFO-BOX]
🔵 Pär Lundh: Tilldelads ingen ny issue denna vecka
   (möjlig support på andra team)

[INFO-BOX]
🔵 Henrik Westerlund: Väntar på API-kontrakt
   (starts nästa fas)
```

### Punkt ⑦ — Beroenden & Blockers

```
BLOCKERTRÄD:

🔴 #43 API Foundation
   ├──→ 🟡 #82 Portfolio reads (väntar)
   └──→ 🟡 #83 Allocation saves (väntar)
             ↑
        🟡 #81 måste mergas först

🟢 #87 Test Foundation
   └──→ 🟡 #88 Critical interactions (väntar)
             └──→ ⚪ #89 E2E (planerad)

RISKER:

[RISK-BLOCK — röd]
🔴 RISK — API-kontrakt inte klart
   Sannolikhet: MEDEL
   Mitigation: Erik möte idag 14:00

[RISK-BLOCK — orange]
🟠 RISK — #81 och #83 kan krocka
   Sannolikhet: LÅGT (om #81 mergas först)
   Mitigation: Strikta merge-regler
```

### Punkt ⑧ — Prioritering & Scope

```
FAS 1 — Nu (Starta nu)

[CARD — grön border]
🟢 #87 Test foundation (Backend, Zaida)
   Status: Ready. Låser upp #88/#89.

[CARD — grön border]
🟢 #43 API client (Frontend, Tomac)
   Status: Ready. Låser upp #82/#83.

[CARD — grön border]
🟢 #81 Linked allocation (Frontend, Björn)
   Status: Ready. Låg konflikt-risk.

FAS 2 — Efter Fas 1 mergad

[CARD — orange border]
🟡 #88 Critical interactions (Frontend, Zaida)
   Status: Starts when #87 merged.
   Väntar på: #87

[CARD — orange border]
🟡 #82 usePortfolio (Frontend, Tomac)
   Status: Starts when #43 merged.
   Väntar på: #43

[CARD — orange border]
🟡 #85 Responsive header (Frontend, Björn)
   Status: Independent. Start parallel.
   Väntar på: Inget
```

---

## 🎨 FÄRGPALLETT (Verklig användning)

```
Primary Colors (Semantiska):
  🟢 #4CAF50 (Grön) — färdig, success
  🟡 #FF9800 (Orange) — pågår, warning
  🔴 #F44336 (Röd) — blockerad, error
  ⚪ #E0E0E0 (Grå) — unknown, info

Neutral:
  Mörkgrå text: #212121 (títlar), #424242 (body)
  Ljusgrå text: #616161 (secondary), #9E9E9E (footer)
  Vit background: #FFFFFF
  Ljusgrå background: #F5F5F5

Accent:
  🔵 #2196F3 (Blå) — struktur, kategori
  🟣 #9C27B0 (Lila) — focus, highlight
  
WCAG AA Contrast (minimum 4.5:1):
  ✓ Mörkgrå (#212121) på vit = 12:1 OK
  ✓ Mörkgrå (#424242) på ljusgrå = 7:1 OK
  ✓ Ljusgrå (#616161) på vit = 5:1 OK
```

---

## ✅ CHECKLISTA FÖR VARJE SLIDE

```
Innan slide presenteras:

FÄRG:
  [ ] Innehåller färg endast för BETYDELSE (inte dekoration)?
  [ ] Grön för färdig? Orange för pågår? Röd för blockerad?
  [ ] Maximalt 2-3 färger per slide?

TEXT:
  [ ] Titlar är 32pt, headers är 20pt?
  [ ] Brödtext är 16pt (läsbar)?
  [ ] Line-height är 1.6 eller mer (luftigt)?

LAYOUT:
  [ ] Rundade hörn på alla textrutor (border-radius: 12px)?
  [ ] Whitespace är 70% av slide?
  [ ] Ingen tabeller (bara cards/blocks)?
  [ ] Spacing mellan element: 16-24px?

ADHD-VÄNLIG:
  [ ] Kan läsaren scanна denna slide på 3 sekunder?
  [ ] Finns visuell hierarki (stor → små)?
  [ ] Ögonen har vilpunkter (whitespace)?
  [ ] Maximalt 3-4 textblock per slide?

PROFESSIONELL:
  [ ] Ingen AI-instruktioner synliga?
  [ ] Endast innehål från PRESENTATION_STRUCTURE?
  [ ] Källstatus i liten footer-text?
  [ ] Konsistent font och spacing?
```

---

## 📐 TEKNISK IMPLEMENTERING (PowerPoint/Google Slides)

```
1. Välj rätt FONT:
   - Helvetica eller Segoe UI
   - INTE serif-fonts (gammalt)

2. Sätt upp COLOR PALETTE:
   - Definiera 6 färger (se paletten ovan)
   - Använd ENDAST dessa

3. Använd SHAPES för cards:
   - Rounded rectangle (12px radius)
   - Border-left: 4px [färg]
   - Shadow: 0 2px 4px rgba(0,0,0,0.1)

4. Spacing-regler:
   - Slide margins: 32px
   - Section gap: 32px
   - Element gap: 16px
   - Line-height: 1.6

5. Ingen tabeller:
   - Ersätt alla tabeller med CARDS
   - Börja från Layout 1 ovan

6. Testa ADHD:
   - Kan du förstå slide på 3 sekunder?
   - Är det luftigt nog?
   - Är texten läsbar från 2 meters avstånd?
```

---

**Version:** 1.0 — Modern, ADHD-vänlig design  
**Status:** MANDATORY för alla nya presentationer  
**Senast uppdaterad:** 2026-09-14
