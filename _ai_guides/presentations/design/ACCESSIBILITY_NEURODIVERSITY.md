---
name: accessibility_neurodiversity
description: Dyslexi- och ADHD-vänlig design — Färger, Former och Symboler levererar budskap FÖRE text
metadata:
  type: process
  critical: true
  for_ai: true
---

# 🧠 DYSLEXI & ADHD-VÄNLIG DESIGN — Färger, Former & Symboler

**DENNA FIL FÖRKLARAR varför presentationen är utformad som den är.**

En presentation som är vänlig för dyslekti och ADHD är **inte bara tillgänglig** — det är **bättre för ALLA läsare**. Färger och former bär meningar. Text bekräftar bara det som redan är tydligt.

---

## 🎯 VAD BETYDER "DYSLEXI/ADHD-VÄNLIGT"?

### För dyslektiker:
- **Text är ansträngande att läsa** — kan ta 2-3x längre tid än för andra
- **Ordningsföljd försvinner lätt** — "15" kan läsas som "51"
- **Fokus glider mellan rader** — behöver visuell struktur för att hålla reda
- **Färg + Symbol hjälper** — hjärnan kan fånga budskapet utan att stava ordet

### För ADHD:
- **Text kräver fokus som är hårt att hålla** — särskilt stora textstycken
- **Visuell stimulans behövs** — men INTE kaos (det distraherar)
- **Snabb visuell sammanfattning är kritisk** — "vad är det här slide-om?" på 1 sekund
- **Strukturerad layout** — tydliga separationer mellan element gör det lättare att inte hoppa omkring

### För ALLA:
- **Mänsklig hjärn läser bilder före text** — på ~1 sekund
- **Färg & form bär information** — snabbare än att läsa ord
- **Organiserad layout** — bättre retention och förståelse

---

## 🎨 FÄRGER = BUDSKAP (INTE DEKORATION)

### Färgsystemet i presentationen:

```
🟢 GRÖN       = Klart, levererat, READY
              RGB 76, 175, 80
              Betydelse: "Det här fungerar"

🟡 ORANGE     = Pågår, work-in-progress, delayed
              RGB 255, 152, 0
              Betydelse: "Det här är på vägen"

🔴 RÖD        = Blockerat, risk, kritisk
              RGB 244, 67, 54
              Betydelse: "Det här behöver uppmärksamhet"

⚪ GRÅ        = Okänd status, no activity, information
              RGB 224, 224, 224
              Betydelse: "Vi vet inte, eller det är neutral info"

🔵 MARINBLÅ   = Struktur, kontainer, neutral information
              RGB 33, 150, 243
              Betydelse: "Det här är en grupp/kategori"
```

### KRITISK REGEL:
**Ingen färg får användas för dekoration.** Varje färg MÅSTE signalera status eller gruppering.

Exempel på RÄTT:
```
🟢 Backend API — KLART     (grön = levererat)
🟡 Frontend UI — PÅG      (orange = arbete pågår)
🔴 Native test — BLOCKERAD (röd = väntar på Backend)
```

Exempel på FELAKTIGT:
```
Backend API (blå för att vi gillar blå)
Frontend UI (rosa för att det är vackert)
Native test (purple för variation)
← DESSA FÄRGER GER INGET BUDSKAP
```

---

## 📏 FORMER = HÄCKEN

### Symbol-system:
```
✅ = Checkmark i cirkel     → "Det här är KLART"
◐  = Halvcirkel/pac-man     → "Det här är HALVVÄGS"
✕  = Kryss                  → "Det här är BLOCKERAT"
?  = Frågetecken            → "Okänt/OKLAR STATUS"
→  = Pil                    → "BEROENDE → följer detta"
│  = Vertikal linje         → "Sekvens/ordning"
┌─ = Låda/kant              → "GRUPP/KATEGORI"
```

### VAD DESSA SIGNALERAR:
En dyslektiker kan läsa en slide **utan att läsa orden** genom att:
1. **Skanna färgerna** — snabbt se vad som är grön/orange/röd
2. **Matcha symboler** — ✅ betyder alltid "klart", aldrig något annat
3. **Läsa text sist** — för att bekräfta vad färg + symbol redan sa

---

## 📐 WHITESPACE & SEPARATION = FOKUS

### Regel: Minsta avstånd mellan element:

```
Mellan issue-rader:     6-8px    (lätt att särskilja)
Mellan färgbar + text:  12px     (fokuslinjer inte täta)
Mellan slides:          24px+    (mental paus)
Mellan par (Frontend):  16px     (visuell gruppering)
Mellan team-sektioner:  32px+    (tydlig NY SEKTION)
```

**VARFÖR?**
- ADHD-hjärnor kan bli överväldiga av täthet
- Dyslektiker behöver "andrum" mellan rader (annars kan ögonen hoppa rad)
- Alla människor fokuserar bättre på välseparerad information

### Exempel på RÄTT spacing:
```
Frontend
─────────────────────────────────
┌─ ✅ #95 Security review + merge (Zaida)
│  Merged 2026-09-13
│
┌─ ◐ #88 Critical interactions (Björn)     [6px avstånd mellan issues]
│  In progress — API väntas idag
│
[16px avstånd mellan teams]
Backend
─────────────────────────────────
┌─ ✓ #87 Test foundation (Rasha)
│  In progress — design-review imorgon
```

### Exempel på FELAKTIG spacing:
```
Frontend
┌─✅#95 Security review(Zaida)Merged 2026-09-13
┌─◐#88 Critical(Björn)PÅG API-väntar
Backend
┌─✓#87Test foundation(Rasha)PÅG
← FÖR TÄTT — Ögonen kan inte vila, dyslektiker stressar, ADHD-fokus försvinner
```

---

## 🔤 TYPOGRAFI = HIERARKI

### Font-storlekar i presentationen:

```
28pt BOLD       = SLIDE-TITEL (mötespunkt ①, ②, etc)
                  (Dyslektiker: STOR är viktigt, lättare att läsa)

14pt BOLD       = Sektion-header (Frontend, Backend, etc)
                  (Gruppering — detta är en KATEGORI)

14pt REGULAR    = Issue-titel (#95 Security review)
                  (Huvudinformation — läs detta)

13pt REGULAR    = Metainfo (Assignad, Status, Datum)
                  (Bekräftelse av vad färg/symbol sa)

11pt ITALIC     = Extra info (commits, test-status)
                  (Sekundär läsning)

10-12pt SMALL   = Footer-info
                  (Tertiär — läs bara om du vill djupdyka)
```

**RADAVSTÅND: 24px mellan rader** (1.5x linjeavstånd)
- Standard är ofta 20px — för tätt för dyslektiker
- 24px ger "andrum" — ögonen kan vila mellan rader

**TECKENFÖRDELNING:**
- Max 60-70 tecken per rad (inte full slidbredd)
- Gör det lättare för dyslektiker att följa rad-för-rad
- Hjälper ADHD-fokus att inte hoppa omkring

---

## 🎯 PRAKTISKA REGLER FÖR AI

### Före rendering — Kontrollista:

```
FÄRGER:
  [ ] Varje färg i presentationen signalerar STATUS, aldrig dekoration
  [ ] Grön = KLART, Orange = PÅG, Röd = BLOCKERAT, Grå = OKÄND
  [ ] Färger matchar mellan slides (samma regel överallt)

FORMER & SYMBOLER:
  [ ] ✅ = alltid "klart"
  [ ] ◐ = alltid "pågår/hälften klart"
  [ ] ✕ = aldrig något positivt
  [ ] ? = osäker status
  [ ] → = beroende/flöde
  [ ] (samma symbol = samma betydelse ÖVERALLT)

WHITESPACE:
  [ ] Minst 6-8px mellan issue-rader
  [ ] Minst 12px mellan färgbar och text
  [ ] Minst 16px mellan team-sektioner
  [ ] Minst 32px mellan mötespunkter
  [ ] 70% tom yta på framsidan (mental paus)

TYPOGRAFI:
  [ ] 28pt bold för slide-titel
  [ ] 14pt bold för sektion-headers
  [ ] 14pt regular för huvud-innehål
  [ ] 24px radavstånd (minst)
  [ ] Max 60-70 tecken per rad

KONTRAST:
  [ ] WCAG AA minst (4.5:1 ratio)
  [ ] Vit text på färgad bakgrund (eller omvänt)
  [ ] Ingen grå text på grå bakgrund

FOKUS:
  [ ] Läsaren kan förstå slide på 1 sekund utan text
  [ ] Läsaren kan bekräfta förståelse genom att läsa text
  [ ] Ögonen har "vilpunkter" (whitespace) att fokusera mellan objekt
```

---

## 💡 VAD HANDLAR PRESENTATIONEN EGENTLIGEN OM?

**En väl designad presentation säger:**
- 🟢 "Vi levererar. Det här fungerar."
- 🟡 "Vi är på vägen. Det tar tid men vi är fokuserade."
- 🔴 "Det här behöver uppmärksamhet. Vi vet om det och gör något."
- ⚪ "Vi vet inte än, eller det är neutral info."

**UTAN denna visuella kodning**, måste läsaren:
1. Läsa varje ord (ansträngande för dyslektiker)
2. Hålla fokus under 10+ sekunder (svårt för ADHD)
3. Minnas tidigare information (slitsamt)

**MED denna kodning**, läser läsaren:
1. **Färg först** (1 sekund) — "OK, vi är på vägen"
2. **Symbol andra** (1 sekund) — "◐ betyder pågår"
3. **Text sist** (5 sekunder) — bekräftar detaljer
4. **Total tid: ~7 sekunder** — möjlighet att hänga med

---

## 🔗 LÄNKNINGAR

**Se även:**
- [VISUAL_DESIGN_MANDATORY.md](VISUAL_DESIGN_MANDATORY.md) — Konkret implementering (PowerPoint-inställningar, RGB-värden)
- [PRESENTATION_FORMAT_GUIDE.md](PRESENTATION_FORMAT_GUIDE.md) — Slide-exempel som visar detta i praktiken
- [MANDATORY_READING_ORDER.md](../MANDATORY_READING_ORDER.md) — Var denna fil passar in i läsordningen

---

## 📝 FÖRFATTARENS INTENTIONER

**Denna presentationsdesign är gjord för att:**

✅ **Möjliggöra för ALLA att förstå projektstatus snabbt**
- Dyslektiker kan läsa utan att stava
- ADHD-fokus kan fångas och hållas
- Alla kan se trends på 1 sekund

✅ **Göra presentationen inte bara tillgänglig utan BÄTTRE för alla**
- Färg + symbol + text = triple redundancy = säker kommunikation
- Mindre läsning = mer fokus på innehål
- Visuell struktur = vackrare design

✅ **Bygga teamtänk genom visuell klarhet**
- När status är tydlig från färg, kan mötet fokusera på lösningar
- Ingen tid går till att "läsa på" vad som är gjort/pågår/blockerat
- Presentation blir möte-verktyg, inte läsuppgift

---

**Status:** PRODUCTION  
**Version:** 1.0  
**Senast uppdaterad:** 2026-09-14
