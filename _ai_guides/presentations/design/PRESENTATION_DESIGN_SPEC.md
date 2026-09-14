---
name: presentation_design_spec
description: DEPRECATED — innehål flyttat till VISUAL_DESIGN_MANDATORY.md och DESIGN_AUTHORITY.md
metadata:
  type: design_specification
  deprecated: true
  version: 1.0
---

# 🚨 DEPRECATED — LÄSNING REKOMMENDERAS EJ

**DENNA FIL INNEHÖLL DESIGN-REGLER SOM NU ÄR GAMLA OCH ÖVERFLÖDIGA.**

**Nya, authoritative källor:**
- **Design-regler** → [VISUAL_DESIGN_MANDATORY.md](./VISUAL_DESIGN_MANDATORY.md)
- **Färg-semantik** → [DESIGN_AUTHORITY.md](./DESIGN_AUTHORITY.md)

**Denna fil sparas för historisk referens men ska INTE användas för nya presentationer.**

---

# 🎨 PRESENTATION DESIGN SPECIFICATION (DEPRECATED)

**Denna fil definierar ENBART design-regler för presentationen — MEN ÄR NU FÖRÅLDRAD.**

**Se `VISUAL_DESIGN_MANDATORY.md` för konkreta design-regler.**

---

## 🎨 BORDER-REGLER

### Färgade borders = STATUS-BEDÖMNING ENDAST

```
🟢 GRÖN border (3px solid #2ecc71):
   Betyder: ON TRACK / Vi når målet / Klart
   Använd på: Team-status cards, progress bars
   Padding inuti: 16px
   Border-radius: 4px
   Background: Ljus grön (10% opacity)

🟠 ORANGE border (3px solid #e67e22):
   Betyder: SLIGHT DELAY / Försenat / Inte på målvägen än
   Använd på: Team-status cards med problem
   Padding inuti: 16px
   Border-radius: 4px
   Background: Ljus orange (10% opacity)

🔴 RÖD border (3px solid #e74c3c):
   Betyder: CRITICAL / Behöver stärkas upp / Omedelbar åtgärd
   Använd på: Team-status cards med kritisk status
   Padding inuti: 16px
   Border-radius: 4px
   Background: Ljus röd (10% opacity)
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

## 📐 NPF-DESIGN REGLER

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
Slide-titel:              28-32pt BOLD
Mötespunkt-rubrik:        18-20pt BOLD
Sektion-header:           14pt BOLD
Body text (huvudinnehål): 14-16pt REGULAR
Metainfo (assignee, etc): 13pt REGULAR
Footer-info:              10-12pt DISKRET

Font: Sans-serif (Arial, Helvetica, system-default)
Radavstånd (line-height): 24px MINIMUM
Teckenfördelning: Max 60-70 tecken per rad
```

### Färg-semantik
```
STÖD-FÄRGER (För status):
  🟢 GRÖN (ON TRACK)        — #2ecc71
  🟠 ORANGE (SLIGHT DELAY)  — #e67e22
  🔴 RÖD (CRITICAL)         — #e74c3c
  ⚪ GRÅ (UNKNOWN/NEUTRAL)  — #e0e0e0

STRUKTUR-FÄRGER (Icke-status):
  🔵 Marinblå (Huvudrubrik) — #2196F3
  ⬛ Blågrå (Neutral info)   — #607D8B
  ⚫ Svart (Text)            — #212121

NEUTRAL:
  ⚪ Vit (Luft, negativt utrymme) — #ffffff

ACCENT (Icke-status):
  💜 Lila (Prioritering, förslag) — #9C27B0
  🌸 Dämpad rosa (Människor, ägare) — #EF5350
```

**STRIKT REGEL:**
Ingen färg får användas utan att kunna förklara dess betydelse.
Om du måste förklara "det betyder inte verkligen detta" → använd neutral färg istället.

---

## 💫 SYMBOLER & STATISTIK

### Status-symboler (samma betydelse överallt):

```
✅ Klart / Done / Delivered
◐ Pågår / In Progress / Hälften klart
✕ Blockerat / Kan inte göras
? Okänd status / Ej verifierad
→ Beroende / Väntar på / Flöde
│ Vertikal linje / Sekvens / Ordning
```

### Kontext-symboler:

```
📋 Checklist / Plan
📊 Statistik / Data
📈 Trend / Utveckling
🔗 Beroende / Väntar på
👥 Assignee / Person
⏰ Deadline / Tid
🤝 Samarbete / Möte
🚨 Urgent / Kritisk
💪 Motiverande / Lycka till
🎯 Fokus denna vecka
```

### Statistik (alltid visa konkret data):

```
PROGRESS:
████░░ Progress bar (visuell framsteg)
80%, 60%, 40% (procenttal)
4/5 issues done (ratio)

KAPACITET:
18h needed / 20h available

DEADLINES:
MON 14:00 (konkret tid, inte "snart")

TEAM:
2/3 assignees working (vem jobbar)
3 blockers identified
1 critical issue
```

---

## 📐 VISUELL BALANS

### Layout som gör läsaren glad:
- Färg/status överst på slide
- Framsteg visas först (positiv start)
- Problem + LÖSNING tillsammans (inte bara problem)
- Whitespace mellan sektioner (andrum)
- Motiverande avslut på sammanfattnings-slide

### Layout som stressar (UNDVIK):
```
❌ All text buntat ihop
❌ Endast negativa saker utan lösning
❌ Dålig kontrast (svårt att läsa)
❌ För många färger (förvirrande)
❌ Ingen struktur (kaotisk)
```

---

## 🚨 FÖRBJUDS

### Färgade borders på neutral mark

```
❌ FÖRBJUDET:
  [Neutral teamkort med grön border]  ← ser ut som "bra status" men är bara struktur
  [Neutral risklista med orange border] ← förstärker risker onödigt
  [Neutral issue-container med röd border] ← ger falsk prioritet

✅ KORREKT:
  [Neutral grå teamkort → liten 🟠 markering bredvid "API dependency"]
  [Neutral grå riskkort → 🔴 indikator på kritisk item, inte hela kortet]
```

**Om ett neutralt element innehåller status:** 
Visa status med liten lokaliserad indikator INNANFÖR kortet, aldrig genom att färga hela kortet eller ramen.

---

## 🔍 PREFLIGHT-KONTROLL

Presentationen **misslyckades** om:
- [ ] En neutral ruta har grön border
- [ ] En neutral ruta har orange border
- [ ] En neutral ruta har röd border
- [ ] En hel teamruta färgas efter en enskild risk
- [ ] En färg används utan att kunna förklara dess status-betydelse
- [ ] Radavståndet är mindre än 20px (målet: 24px)
- [ ] Fontstorleken är mindre än 12pt (footer) eller mindre än 14pt (brödtext)
- [ ] Kontrast är mindre än 4.5:1 (WCAG AA-standard)

---

## 📋 CHECKLIST FÖR DESIGN-COMPLIANCE

```
FÄRGER & STATUS:
  [ ] Grön används ENDAST för faktisk god status
  [ ] Orange används ENDAST för faktisk risk/osäkerhet
  [ ] Röd används ENDAST för faktisk blockering/kritisk
  [ ] Gul används ENDAST för "behöver beslut"
  [ ] Inga statusfärger på neutral mark
  [ ] Inga statusfärgade borders på neutral info
  [ ] Neutral information använder marinblå/grå/vit

BORDER-REGLER:
  [ ] Färgade borders (3px) ENDAST på team-status cards
  [ ] Svart/vit borders (2px) på neutral information
  [ ] Padding 16px inuti borders
  [ ] Kontrast 4.5:1 minimum (WCAG AA)

WHITESPACE & TYPOGRAFI:
  [ ] 60-70% tom yta på varje slide
  [ ] Toppadding 20px, sidpadding 16px
  [ ] Ingen text-overlap
  [ ] Font-hierarki: 28pt → 14pt → 13pt
  [ ] Radavstånd minst 24px
  [ ] Max 60-70 tecken per rad

SYMBOLER & STATISTIK:
  [ ] Symboler konsistenta (✅ = alltid "klart")
  [ ] Statistik konkret (tal + procent, inte vague)
  [ ] Deadlines med tid (HH:MM), inte "snart"

TOTALT:
  [ ] Designen passar NPF/dyslexia/ADHD-vänlighet
  [ ] Ingen animation/blinking
  [ ] Visuell förutsägbarhet (samma layout varje vecka)
  [ ] Explicit information (inga gissningar)
  [ ] Sensory-friendly (minimal rörelse, begränsad stimuli)
```

---

**Version:** 1.0  
**Senast uppdaterad:** 2026-09-14  
**Status:** PRODUCTION — Design-specifikation för alla presentationer
