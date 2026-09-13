---
name: visual_design_mandatory
description: MANDATORY — All presentations MUST use color, symbols, and form BEFORE text — NPF/Dyslexia-first design
metadata:
  type: process
  critical: true
  required_before: rendering
---

# 🎨 VISUAL DESIGN MANDATORY — INNAN PRESENTATION RENDERAS

**🚨 DENNA FIL MÅSTE LÄSAS OCH FÖLJAS FÖRE VARJE PRESENTATION.**

Om denna fil inte följs → presentationen blir utan färg, utan symboler, utan visuell hierarki.

---

## 🚨 SINGLE RULE: SYMBOL + FÄRG + TEXT

**Varje element på sliderna måste ha TRE lager i DENNA ordning:**

```
1️⃣ SYMBOL      (Läses först — 1 sekund)
2️⃣ FÄRG        (Säger status — 2-3 sekunder)
3️⃣ TEXT        (Bekräftar — 5-10 sekunder)
```

**UTAN detta är presentationen INKOMPLETT.**

---

## 📋 KONKRET IMPLEMENTERING PER ELEMENT

### A. DoD-Status (Definition of Done)

**Format som MÅSTE användas:**

```
✅ AC (Acceptance Criteria)     🟢 Complete
◐  Tests                        🟡 In progress  
✕  Review                       🔴 Blocked
?  Docs                         ⚪ Unknown
```

**RENDERING-REGLER (PowerPoint/Google Slides):**

1. **Symbol-kolumn** (vänster):
   - ✅ = grön cirkel med checkmark
   - ◐  = orange halvcirkel
   - ✕  = röd kryss
   - ? = grå frågetecken

2. **Färg-block** (bakom symbol):
   - 🟢 Grön bakgrund (RGB 76, 175, 80) — FÄRDIG
   - 🟡 Orange bakgrund (RGB 255, 152, 0) — PÅGÅR
   - 🔴 Röd bakgrund (RGB 244, 67, 54) — BLOCKERAD
   - ⚪ Grå bakgrund (RGB 224, 224, 224) — OKÄND

3. **Text** (höger):
   - Font: Arial, 14pt, bold för symbol, regular för text
   - Kontrast: Vit text på färgad bakgrund (WCAG AA)
   - Whitespace: Minst 4px padding runt symbolen

**EXEMPEL:**

```
┌─────────────────────────────────┐
│ ✅ AC               🟢 Complete │ (grön bakgrund)
│ ◐  Tests            🟡 In progress (orange bakgrund)
│ ✕  Review          🔴 Blocked    (röd bakgrund)
│ ?  Docs            ⚪ Unknown    (grå bakgrund)
└─────────────────────────────────┘
```

---

### B. Issue Status (Slide ① — Sedan förra mötet)

**Format som MÅSTE användas:**

```
[SYMBOL] [FÄRG-BOX] #XX – Titel (Assignee)
         Vad det innebär · Status · Commits · Datum
```

**Symbol-urval:**

```
✅ = Merged & DoD complete (grön)
🔄 = Merged but DoD incomplete (orange)
⏳ = Open with commits (pågår, orange)
⚠️ = Blocked dependency (röd)
□  = No activity (grå)
```

**RENDERING-REGLER:**

1. **Symbol** (vänster kant):
   - Storlek: 24x24px
   - Färg: Motsvar status (🟢/🟡/🔴/⚪)
   - Font: Helvetica/Arial, bold

2. **Färg-block** (bakgrund för hela raden):
   - Liten färgad bar (4px bredd, full höjd)
   - Placering: Vänster kant av textbox
   - Färg: Motsvar SYMBOL
   - **VIKTIGT:** Bar ska synas VID GLANCE, innan text läses

3. **Text-innehål**:
   ```
   #XX – Titel (Assignee)     [Huvud-rad, 14pt bold]
   Vad det innebär            [Effekt-rad, 12pt regular, grå text]
   · Status (merged/open)     [Meta-rad, 11pt italic, mörkgrå]
   · X commits denna vecka
   · Klar/ETA datum
   ```

**KONTRAST:**
- Symbol + färgbar måste synas tydligt mot bakgrund
- Text måste läsas enkelt (4.5:1 kontrast minimum)

**WHITESPACE:**
- Mellan rader: minimum 8px
- Mellan färgbar och text: minimum 12px
- Mellan issue-rader: minimum 6px

---

### C. Progress Bars (Kapacitet, Sprint Progress)

**Format som MÅSTE användas:**

```
████████░░ 80% (Klar — grön)
██████░░░░ 60% (Pågår — orange)
████░░░░░░ 40% (Svag — orange)
██░░░░░░░░ 20% (Kritik — röd)
```

**RENDERING-REGLER:**

1. **Bar själv:**
   - Längd: 200px (responsiv på mindre skärmar)
   - Höjd: 16px
   - Fyllda delen: 🟢 grön (80%+), 🟡 orange (40-79%), 🔴 röd (<40%)
   - Tom delen: ljusgrå (RGB 200, 200, 200)
   - Border: Ingen (bar bör vara smooth)

2. **Text bredvid bar:**
   - Procent: 14pt bold
   - Label: 12pt regular
   - Status: 11pt italic (grön/orange/röd text matchande bar)

3. **Whitespace runt bar:**
   - Ovanför: 12px
   - Nedan: 12px
   - Sida: 12px

---

### D. Dependency Diagrams (Vem väntar på vem)

**Format som MÅSTE användas:**

```
┌─────────────┐     ┌─────────────┐
│  Frontend   │────▶│   Backend   │
│  (#42)      │     │  (BLOCKERAD)│
└─────────────┘     └─────────────┘
     🟡              🔴
   (väntar)        (blockerar)
```

**RENDERING-REGLER:**

1. **Boxar (team/issue):**
   - Storlek: 120x60px (responsiv)
   - Bakgrundsfärg: Marinblå (RGB 33, 150, 243) för struktur
   - Text: Vit, 12pt bold
   - Border: 2px färgad kant (🟢/🟡/🔴 för status)

2. **Pilar (beroenden):**
   - Stil: Hel linje, 2px tjock
   - Färg: 🟠 orange om blocking, 🟡 yellow om waiting
   - Pil-huvud: Fyllt triangel samma färg
   - Label över pil: "blocks", "waiting for", "depends on" (11pt)

3. **Status-symbol under box:**
   - 🟢 grön = OK
   - 🟡 orange = pågår/delayed
   - 🔴 röd = blockerat/kritiskt

---

### E. Team Status Cards (Punkt ③④⑤ Slide A)

**Format som MÅSTE användas:**

```
┌─────────────────────────────────┐
│ 📝③A Frontend Team               │  (header)
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                 │
│  Issue Status denna vecka       │
│  ┌─────────────────────────┐    │
│  │ #42 Login (Zaida)  🟢   │    │
│  │ #43 CSS (Björn)    🟡   │    │
│  │ #44 Nav (Tomac)    🔴   │    │
│  └─────────────────────────┘    │
│                                 │
│  Källa: GitHub                  │
└─────────────────────────────────┘
```

**RENDERING-REGLER:**

1. **Card-struktur:**
   - Bakgrund: Vit (RGB 255, 255, 255)
   - Border: 2px marinblå (RGB 33, 150, 243)
   - Corner radius: 4px
   - Padding: 16px
   - Margin under: 16px

2. **Header:**
   - Bakgrund: Marinblå (RGB 33, 150, 243)
   - Text: Vit, 14pt bold
   - Padding: 8px (inuti marinblå bak)
   - Avskiljning: 2px grå linje under header

3. **Tabell inuti card:**
   - Border mellan rader: 1px ljusgrå
   - Padding per cell: 8px
   - Issue-nummer: 12pt bold
   - Status-symbol: 24x24px, högerställd
   - Assignee: 11pt regular grå

---

### F. Risk Matrix (Punkt ⑦)

**Format som MÅSTE användas:**

```
         Låg          Medel        Hög Sannolikhet
      ┌─────────┬──────────┬──────────┐
Låg   │  🟢     │   🟡    │   🟡    │
      ├─────────┼──────────┼──────────┤
Medel │  🟡     │   🟡    │   🔴    │
      ├─────────┼──────────┼──────────┤
Hög   │  🟡     │   🔴    │   🔴    │
      └─────────┴──────────┴──────────┘
 Låg Konsekvens ────────▶ Hög
```

**RENDERING-REGLER:**

1. **Matrix-cells:**
   - Storlek: 80x80px per cell
   - Färg: Motsvar risk (🟢/🟡/🔴)
   - Linjerna: 1px grå mellan celler
   - Border: 2px mörkgrå runt hela matrisen

2. **Etiketter:**
   - Axlar: 12pt bold
   - Risk-nivåer inuti cells: 24pt bold, symbol + text
   - Exempel: "🟡 Medium" eller "🔴 Critical"

3. **Legenden:**
   - Under matrisen
   - 🟢 = Acceptabel risk
   - 🟡 = Kräver åtgärd
   - 🔴 = Måste hanteras nu

---

## ✅ BEFORE RENDERING — VISUELL CHECKLIST

**Innan presentationen renderas, verifiera ALLA dessa:**

```
Slides ① (Sedan förra mötet):
  ☐ Varje issue har symbol (✅/🔄/⏳/⚠️/□)
  ☐ Varje issue har färgbar (🟢/🟡/🔴/⚪)
  ☐ Varje issue visar effekt ("Vad det innebär")
  ☐ Text läsbar (minst 12pt)
  ☐ Kontrast OK (testa med contrast checker)

Slides ③④⑤ (Team Status):
  ☐ Issue-tabell har DoD-kolumn med ✅/◐/✕/?
  ☐ Varje DoD-symbol har motsvarande färg (🟢/🟡/🔴/⚪)
  ☐ Team-kort har marinblå border
  ☐ Whitespace omkring element (minst 8px)

Slide ⑥ (Beroenden):
  ☐ Dependency-diagram visat (ej bara text)
  ☐ Pilar visar riktning (väntar på, blockerar)
  ☐ Status-färger på boxar (🟢/🟡/🔴)

Slide ⑦ (Risker):
  ☐ Risk-matris visat (ej bara tabell)
  ☐ Färger motsvar risk (🟢/🟡/🔴)

Slide ⑧-⑨ (Kapacitet):
  ☐ Progress bars visat
  ☐ Procent i bars (80%, 60%, osv)
  ☐ Färger motsvar status (🟢/🟡/🔴)

ALLA SLIDES:
  ☐ Ingen ENDAST text-lista (alla slides har minst ett visuellt element)
  ☐ Mötesspunkt-markörer (📝① 📝③A osv) överst
  ☐ Mötets logik följd: Symbol → Färg → Text (VID VARJE ELEMENT)
  ☐ Whitespace är rimlighör (ej trångt, ej tomt)
  ☐ Font-storlek konsistent (header 14pt bold, body 12pt, meta 11pt)
  ☐ Färger är SEMANTISKA (ingen dekoration)

WCAG ACCESSIBILITY:
  ☐ Text-kontrast minimum 4.5:1 (test med webaim.org)
  ☐ Färg+symbol tillsammans (ej färg ensam för status)
  ☐ Font-size minimum 12pt (dyslexia-vänligt)
  ☐ Line-height minimum 1.5 (NPF-vänligt)
```

**Om NÅGON checkbox är UNCHECKED:**
```
❌ PRESENTATIONEN ÄR INTE KLAR
❌ Du måste fixa elementet enligt VISUAL_DESIGN_MANDATORY
❌ Rendrera INTE utan att alla är checkade
```

---

## 🎯 SUMMARY: TRE PRINCIPER

**1. SYMBOL FÖRE FÄRG FÖRE TEXT**
- Du ska förstå status på 1 sekund från symbol
- Färg bekräftar status på 2-3 sekunder
- Text ger detaljer på 5+ sekunder

**2. FÄRG ÄR ALDRIG DEKORATION**
- 🟢 = klart/verifierat
- 🟡 = pågår/avvikelse
- 🔴 = blockerat/kritisk
- ⚪ = okänd/neutral
- Lila/blå = struktur/kategorier (ALDRIG status)

**3. WHITESPACE & TILLGÄNGLIGHET**
- Minst 8px mellan element (NPF/ADHD-vänligt)
- Minst 12pt font (dyslexia-vänligt)
- Minst 1.5 line-height (läsbar)
- Minst 4.5:1 kontrast (WCAG AA)

---

## 🚨 RED FLAGS — OM DU SER DET HÄR, FIX DET

```
❌ "Sliden är bara text-listor" → Lägg till symbols, färger, diagrams
❌ "Status visar bara som färg" → Lägg till symbol + text också
❌ "Texten är liten och tätt packad" → Öka font, öka whitespace
❌ "Jag behöver läsa alla ord för att förstå status" → Du läste fel — symbol ska räcka
❌ "Färgen motsvarar inte semantiken" → Fixa enligt SYMBOL + FÄRG MANDATORY
```

---

**Version:** 1.0  
**Senast uppdaterad:** 2026-09-13  
**DENNA FIL ÄR MANDATORY FÖRE RENDERING**

INGEN PRESENTATION UTAN DENNA DESIGN. PERIOD.
