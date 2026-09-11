# 🎬 INSTRUKTIONER FÖR AI — Skapa Sprint Meeting Presentation

**DETTA ÄR EN REGEL FÖR AI** — Läs denna FÖRST innan du skapar presentationen.

**Vilken AI som helst (Claude, ChatGPT, Gemini) ska kunna följa denna guide och skapa SAMMA presentation varje gång.**

**Användaren kommer säga:** "Skapa en presentation till måndagsmötet" + länk till detta repo  
**Du läser denna fil FÖRST** → Du skapar presentationen enligt denna struktur  
**Resultat:** Samma struktur, samma innehål, varje vecka

---

## 📋 KORT INSTRUKTION FÖR AI

1. ✅ Läs denna fil (SPRINT_PRESENTATION_STRUCTURE.md)
2. ✅ Läs møtesprotokollet (SPRINT_PROTOCOL_NUMBERED.md) för denna vecka
3. ✅ Läs mötesprotokollet från Google Docs (raw-export länk i README.md)
4. ✅ Skapa presentation enligt denna struktur (samma ordning, samma format)
5. ✅ Varje slide får rätt symbol (📝①②③ etc)
6. ✅ Output: PowerPoint, Google Slides, eller Markdown (berätta vilket du använder)

---

## ✅ FÖRE DU BÖRJAR — CHECKLIST

- [ ] Jag har läst SPRINT_PRESENTATION_STRUCTURE.md (denna fil)
- [ ] Jag vet vilken mötesprotokolls-data som gäller denna vecka
- [ ] Jag vet att samma STRUKTUR ska användas varje vecka
- [ ] Jag förstår att varje slide ska ha symbol 📝①②③ etc
- [ ] Jag vet vilka färger som är 🟢🟠🔴

---

**Sekreteraren ser symbolen 📝①②③ på varje slide och vet vilket protokoll-punkt att fylla in.**

---

## 🎬 SLIDE 0 — AGENDA (ALLTID FÖRSTA SLIDEN)

**Slide 0.1 — AGENDA**
- Titel: "MÖTESPUNKTER DENNA VECKA"
- Innehål: Lista alla 11 punkter

```
📝① STATUS SEDAN FÖRRA MÖTE
📝② ÖVERGRIPANDE MÅL & STATUS
📝③ FRONTEND TEAM
📝④ BACKEND TEAM
📝⑤ NATIVE TEAM
📝⑥ PRIORITERING & SCOPE
📝⑦ ESTIMERING & RISK
📝⑧ TEKNISKA BESLUT
📝⑨ BEROENDEN & BLOCKERS
📝⑩ ARBETSUPPGIFTER
📝⑪ NÄSTA STEG & SAMMANFATTNING
```

---

## 📋 PRESENTATION FLOW (90 minuter)

```
09:00-09:15 (15 min) — SLIDES 📝①②
09:15-09:20 (5 min)  — SLIDES 🎙️ BREAKOUT INFO
09:20-09:25 (5 min)  — TEAM BREAKOUTS (ingen slide, team diskuterar)
09:25-09:30 (5 min)  — PAUS / SLIDES 🎙️ PAUS INFO
09:30-10:00 (30 min) — SLIDES 📝③④⑤⑥
10:00-10:25 (25 min) — SLIDES 📝⑦⑧
10:25-10:30 (5 min)  — SLIDES 📝⑨⑩⑪
```

---

## 🎬 SLIDES MED NUMRERING

### SEKTION 📝① — STATUS SEDAN FÖREGÅENDE MÖTE (5 min)

**Slide 1.1 — 📝①**
- Titel: "Status Sedan Föregående Möte"
- Innehål: 
  - Git log denna vecka (vad blev done)
  - GitHub Project Board (in progress / blocked)
  - 2-3 bullets max

---

### SEKTION 📝② — ÖVERGRIPANDE MÅL & STATUS (10 min)

**Slide 2.1 — 📝② (SYMBOL TILL VÄNSTER, TEXT TILL HÖGER)**
```
📝② DENNA VECKAS MÅL

Risk Metrics (#42 - Marco): [%]
FX Converter (#45 - Jana): [%]
Tests (#48 - Anna): [%]
Kärnflödet (#51 - Kiran): [status]
```
*Secretary copy-pastar allt till höger om 📝② direkt in i punkt ② i protokollet*

**Slide 2.2 — 📝② (FORTSÄTTNING — SAMMA PUNKT)**
```
📝② ÖVERGRIPANDE STATUS

Status: 🟢 GRÖN / 🟠 ORANGE / 🔴 RÖD

Deadlines:
- Torsdag 15:00 (Sprint end)
- 24 sep 16:00 (CTO-demo)
- 15 oktober (Kvaldemo)

Åtgärdsförslag (om orange/red):
[Åtgärder...]
```
*Secretary fortsätter copy-pasta till samma punkt ②*

---

### SEKTION 📝③ — FRONTEND TEAM STATUS (Per team 5-10 min)

**Slide 3.1 — 📝③**
- Titel: "🟢 Frontend Team — ON TRACK"
- Innehål:
  - Progress: 80% (████████░░)
  - Issues: 4 / 5 done
  - Vad är klart: [Issues]
  - Vad pågår: [Issues]
  - Blockers: None / [Beskrivning]

---

### SEKTION 📝④ — BACKEND TEAM STATUS

**Slide 4.1 — 📝④**
- Titel: "🟠 Backend Team — SLIGHT DELAY"
- Innehål:
  - Progress: 60% (██████░░░░)
  - Issues: 2 / 4 done
  - Vad är klart: [Issues]
  - Vad är bakom: [Issues]
  - Blockers: [Beskrivning]
  - Åtgärd: [Vad gör vi?]

---

### SEKTION 📝⑤ — NATIVE TEAM STATUS

**Slide 5.1 — 📝⑤**
- Titel: "🔴 Native Team — CRITICAL"
- Innehål:
  - Progress: 40% (████░░░░░░)
  - Issues: 1 / 3 done
  - Vad är klart: [Issues]
  - Vad är blockat: [Issues]
  - KRITISK BLOCKER: [Beskrivning]

**Slide 5.2 — 📝⑤**
- Titel: "🚨 Omedelbar Åtgärd Behövs"
- Innehål:
  - Backend + Native pair prog IDAG 14:00
  - Sharpe spec writing (1 hour)
  - Implementation (3 hours)
  - Deadline: SAME DAY

---

### BREAKOUT SEKTION 🎙️

**Slide 6.1 — 🎙️ BREAKOUTS**
- Titel: "Team Breakouts — 5 minuter"
- Innehål:
  - "Frontend rum: Vad behöver ni denna vecka?"
  - "Backend rum: Vad blockerar er?"
  - "Native rum: Vad behöver ni för att börja?"
  - "Vi ses om 5 minuter!"

**Slide 6.2 — 🎙️ PAUS**
- Titel: "Kaffepaus — 5 minuter"
- Innehål:
  - (Optional musik eller bara tom slide)
  - "Vi återsamlas om 5 minuter"

---

### SEKTION 📝⑥ — PRIORITERING & SCOPE (30 min)

**Slide 7.1 — 📝⑥**
- Titel: "Prioritering & Scope"
- Innehål:
  - MÅSTE-HA denna vecka: [Issues]
  - NICE-TO-HAVE: [Issues]
  - "Kan vi göra allt? Eller scope cut?"

**Slide 7.2 — 📝⑥** (om behövs)
- Titel: "Scope Cut Beslut"
- Innehål:
  - Skipped: [Issue - Why?]
  - Shifted: [Issue - To when?]

---

### SEKTION 📝⑦ — ESTIMERING & RISK (25 min)

**Slide 8.1 — 📝⑦**
- Titel: "Estimering & Kapacitet"
- Innehål:
  - Frontend: X hours available / Y hours needed
  - Backend: X hours available / Y hours needed
  - Native: X hours available / Y hours needed
  - "Passar det?"

**Slide 8.2 — 📝⑦**
- Titel: "Risker & Mitigation"
- Innehål:
  - Risk 1: [Beskrivning] → Mitigation: [Åtgärd]
  - Risk 2: [Beskrivning] → Mitigation: [Åtgärd]
  - Framgångskriterier: [Kriterium 1, 2, 3]

---

### SEKTION 📝⑧ — TEKNISKA BESLUT (Vid behov)

**Slide 9.1 — 📝⑧** (om det finns tekniska beslut denna vecka)
- Titel: "Tekniska Beslut"
- Innehål:
  - Beslut: [Vad?]
  - Varför: [Reasoning]
  - Impact: [Vad ändrar?]

---

### SEKTION 📝⑨ — BEROENDEN & BLOCKERS (Vid behov)

**Slide 10.1 — 📝⑨** (om det finns kritiska beroenden)
- Titel: "Beroenden Mellan Teams"
- Innehål:
  - Frontend väntar på: [Vad från vem] → Status
  - Backend väntar på: [Vad från vem] → Status
  - Native väntar på: [Vad från vem] → Status

---

### SEKTION 📝⑩ — ARBETSUPPGIFTER (Vid behov)

**Slide 11.1 — 📝⑩** (om detta behöver visas)
- Titel: "Issues Denna Vecka"
- Innehål:
  - Frontend: #XX, #YY (med assignee + timmar)
  - Backend: #XX, #YY
  - Native: #XX

---

### SEKTION 📝⑪ — NÄSTA STEG & SAMMANFATTNING

**Slide 12.1 — 📝⑪**
- Titel: "Nästa Steg"
- Innehål:
  - GitHub Project Board updated
  - Pair sessions booked
  - Deadlines clear

**Slide 12.2 — 📝⑪**
- Titel: "Sammanfattning"
- Innehål:
  - Fokus denna vecka: [...]
  - Kritiska actions: [...]
  - Status: 🟢 / 🟠 / 🔴
  - "Lycka till denna vecka!"

---

## 🎨 DESIGN-REGLER FÖR ALLA SLIDES

- **Font:** Stor, läsbar (minst 24pt)
- **Kontrast:** WCAG AA (4.5:1 text/bakgrund)
- **Padding:** 12px horisontellt, 16px vertikalt (ingen text-overlap)
- **Färger:** 
  - 🟢 Grön = #2ecc71
  - 🟠 Orange = #e67e22
  - 🔴 Röd = #e74c3c
- **Varje slide:** Max 3-5 bullets, inte massa text
- **Symbol:** 📝① etc bör synas tydligt (övre högra hörnet?)

---

## ✅ CHECKLIST FÖR PRESENTATION

Innan mötet:
- [ ] Alla slides har rätt symbol (📝①②③ etc)
- [ ] Symbolerna matchar mötesprotokollet
- [ ] Slides är i rätt ordning
- [ ] Färger är WCAG AA contrast
- [ ] Padding är minst 12px/16px
- [ ] Breakout-slides är klara (🎙️)
- [ ] Paus-slide är klara (🎙️)

Under mötet:
- [ ] Secretary kan se både presentation + protokoll sida vid sida
- [ ] Secretary copy-pastar text från slides till rätt punkt
- [ ] Facilitator följer slide-order (springar inte omkring)

---

## 💡 TIPS FÖR CONSISTENCY

**Samma struktur varje vecka = Teamet känner igen den**
- Punkt ① är alltid Status
- Punkt ② är alltid Mål & Status
- Punkt ③④⑤ är alltid Teams
- Punkt ⑥⑦ är alltid Prioritering & Estimering
- Punkt ⑧⑨⑩⑪ är alltid Beslut/Nästa steg

Lag lär sig: "Jag vet att efter Breakout kommer Prioritering på slide 7"
Secretary vet: "Slide med 📝⑥ = Jag fyller in punkt 6 i protokollet"

**Resultat:** Mötet flyter snabbt, protokollet blir korrekt och komplett.

---

## 🤖 FÖR EXTERNA AIS — ANVÄNDA DENNA GUIDE

**Om någon säger:** "Skapa en presentation till måndagsmötet enligt context_enginering repo"

**Du gör:**
1. Läs denna fil (SPRINT_PRESENTATION_STRUCTURE.md) från början
2. Läs SPRINT_PROTOCOL_NUMBERED.md för att förstå strukturen
3. Fråga användaren: "Vilken vecka?" eller "Läs mötesprotokollet från Google Docs"
4. Samla data för denna vecka:
   - Git log denna vecka (vad blev done)
   - GitHub Project Board status
   - Mötesprotokollet från tidigare möten
   - Team-status från mötesprotokollet (🟢🟠🔴)
5. Skapa presentation **EXAKT enligt denna struktur**:
   - **SLIDE 0:** AGENDA med alla 11 punkter (📝①②③ etc) — ALLTID FÖRST
   - Slide 1.1 → 📝① med text till höger
   - Slide 2.1, 2.2 → 📝② med text till höger (båda samma punkt)
   - Slide 3.1 → 📝③ (Frontend)
   - Slide 4.1 → 📝④ (Backend)
   - Slide 5.1, 5.2 → 📝⑤ (Native)
   - osv enligt schema ovan

6. **KRITIGT:** VARJE SLIDE måste ha:
   - Symbol **📝① klistrad till VÄNSTER**
   - Text till HÖGER som kan copy-pastas direkt
   - Secretary kan se symbolen och veta exakt vilken punkt att fylla in

7. Output i format: **PowerPoint (.pptx), Google Slides, eller Markdown**
   - Berätta vilket format du använder
   - Sätt in all text direkt (inte "add text manually")

**WICHTIGT:**
- ✅ SAMMA struktur varje vecka
- ✅ VARJE slide får symbol 📝①②③ etc
- ✅ Designkrav: WCAG AA, padding 12px/16px
- ✅ Max 3-5 bullets per slide
- ❌ Aldrig ändra ordningen på slides
- ❌ Aldrig lägga till "kreativa" extra slides utan att fråga
- ❌ Aldrig utelämna breakout/paus-slides

**Output:**
```
Presentation klar! Format: [PowerPoint / Google Slides / Markdown]

📝① Status — [summary]
📝② Mål & Status — [summary]
📝③ Frontend — [summary]
📝④ Backend — [summary]
📝⑤ Native — [summary]
📝⑥ Prioritering — [summary]
📝⑦ Estimering & Risk — [summary]
📝⑧⑨⑩⑪ Tekniska beslut, nästa steg

Du kan nu:
- Kopiera denna presentation
- Visa den under mötet
- Secretary fyller in mötesprotokollet parallelt
```
