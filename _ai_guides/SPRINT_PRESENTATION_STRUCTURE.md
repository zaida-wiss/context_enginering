# 🎬 INSTRUKTIONER FÖR AI — Skapa Sprint Meeting Presentation

**DETTA ÄR EN REGEL FÖR AI** — Läs denna FÖRST innan du skapar presentationen.

**Vilken AI som helst (Claude, ChatGPT, Gemini) ska kunna följa denna guide och skapa SAMMA presentation varje gång.**

**Användaren kommer säga:** "Skapa en presentation till måndagsmötet" + länk till detta repo  
**Du läser denna fil FÖRST** → Du skapar presentationen enligt denna struktur  
**Resultat:** Samma struktur, samma innehål, varje vecka

---

## 📋 KORT INSTRUKTION FÖR AI

1. ✅ Läs denna fil (SPRINT_PRESENTATION_STRUCTURE.md) från början
2. ✅ Läs mötesprotokollet (SPRINT_PROTOCOL_NUMBERED.md) för denna vecka
3. ✅ Läs mötesprotokollet från Google Docs (raw-export länk i README.md)
4. ✅ Läs KURSMAL_OCH_BETYG.md för kursdatum
5. ✅ Samla data denna vecka:
   - Git log (vad blev gjort)
   - GitHub Project Board (status)
   - Branches/PRs/blockers
   - Vem jobbar på vad
6. ✅ Skapa presentation **EXAKT enligt denna struktur**
   - Slide 0: Presentationsslide + Agenda
   - Slide 1: Övergripande (KURSEN + PROJEKTET + AVANZA + TIDSLINJE)
   - Slides 2-14: Se schema nedan
7. ✅ Symbol 📝 till VÄNSTER, copy-paste text till HÖGER
8. ✅ Output: PowerPoint/Google Slides/Markdown (berätta vilket)

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

## 🎬 SLIDE 0 — PRESENTATIONSSLIDE (ALLTID FÖRSTA)

**Slide 0.1 — PRESENTATIONSSLIDE**
```
📝⓪ MÅNDAGSMÖTE — SPRINT PLANNING

Tid: 09:00-10:30 (90 minuter)
Syfte: Planera denna vecka, säkerställa vi når målen

Vi täcker:
✅ Vad vi gjort
✅ Var vi står nu (3 målsystem)
✅ Vad som är kritiskt
✅ Prioritering & planering för denna vecka
```

**Slide 0.2 — AGENDA & PÅMINNELSE**
```
📝⓪ AGENDA — VI GÅR IGENOM DETTA SYSTEMATISKT

📝① Övergripande status (3 målsystem)
📝② Team-status: Frontend, Backend, Native
📝③ Vad gjordes förra veckan
📝④ Beroenden, Risker, Sårbarheter
📝⑤ Team-support förslag
📝⑥ Prioritering & Scope denna vecka
📝⑦ Estimering & Risk
📝⑧ Tekniska Beslut
📝⑨ Arbetsuppgifter denna vecka
📝⑩ Nästa Steg & Sammanfattning

💡 VI HÅLLER MÖTET KORT & KONCIST
- En punkt åt gången
- Fokuserat på beslut, inte pratet
- 90 minuter = vi är klara 10:30
```

---

## 🎬 SLIDE 1 — ÖVERGRIPANDE STATUS (TRE MÅLSYSTEM)

**Slide 1.1 — 📝① KURSEN (17 KURSMÅL + BETYG)**
```
📝① KURSEN — VAD BEHÖVER VI UPPNÅ?

Mål: Uppfylla alla 17 kursmål → G/VG betyg
Fokus: Individuell bedömning + slutleverans

Deadlines:
🔴 4 november 15:00 — SLUTLEVERANS
🟠 5 november 09:00 — FINALDAG (om vi är bland topp 4)

Vad behövs för godkänt:
✅ Kärnflödet fungerar
✅ Git-historia är tydlig (individuell bidrag)
✅ Dokumentation är komplett (README, beslut, tester)
✅ Alla 17 kursmål adresserade

Status denna vecka: 🟢 🟠 🔴 [välj EN]
- Fortskridande: [X av 17 kursmål adresserade]
- Risker: [Om någon kursmål hoppad?]
```

**Slide 1.2 — 📝① PROJEKTET (MVP V2 + LEVERABLES)**
```
📝① PROJEKTET — VAD SKA VI LEVERERA?

Mål: Funktionerande MVP v2 som löser Annas problem

MVP Scope:
✅ Portföljöversikt (alle sparformer)
✅ Riskmått (volatilitet, Sharpe, allokering)
✅ Back-testing motor
✅ FX-justering
✅ Rebalanserings-förslag

Deadlines:
🔴 24 september 16:00 — CTO-DEMO (kod + arkitektur)
🟠 15 oktober 17:00 — KVALDEMO (kund ser det)
🟢 4 november 15:00 — SLUTLEVERANS

Vad behövs för accept:
✅ Kärnflödet end-to-end testbar
✅ README, tester, beslutslogg
✅ Kan köras lokalt
✅ Inte perfekt, men säker & stabil

Status denna vecka: 🟢 🟠 🔴 [välj EN]
- Fortskridande: [X av MVP-features klara]
- Risker: [CTO-demo? Kundfeedback?]
```

**Slide 1.3 — 📝① AVANZA SOM KUND (BEHOV)**
```
📝① AVANZA SOM KUND — VAD BEHÖVER ANNA?

Problem Anna lösa:
"Förklara min portfölj utan att göra det för komplicerat"

Vad Anna behöver se:
✅ Portföljöversikt (total värde, alla sparformer)
✅ Risk-analys (vad är riskerna?)
✅ Allokering (hur är det fördelat?)
✅ Förslag (hur blir det bättre?)
✅ Back-testing (hur hade det gått förut?)

Feedback från Anna (om vi har den):
- [Vad tycker hon är bra?]
- [Vad behöver förbättras?]

Status denna vecka: 🟢 🟠 🔴 [välj EN]
- Löst: [Vilka av Annas behov lösta?]
- Återstår: [Vilka behov återstår?]
```

**Slide 1.4 — 📝① TIDSLINJE & CHECKLISTOR**
```
📝① TIDSLINJE MED CHECKLISTOR

INNAN DENNA VECKA SLUTAR (Torsdag 15:00):
☐ Sprint goals 100% done
☐ Tests at 70%+ coverage
☐ All PRs merged
☐ README updated
☐ No Friday coding

INNAN CTO-DEMO (24 sep 16:00):
☐ Kärnflödet 100% stable
☐ Risk Metrics + FX working
☐ Dokumentation komplett
☐ Git history tydlig
☐ Demo plan klar

INNAN KVALDEMO (15 okt):
☐ Kundfeedback implementerad
☐ UI/UX polerad
☐ Performance OK

INNAN SLUTLEVERANS (4 nov 15:00):
☐ ALLT according to DoD
☐ 17 kursmål adresserade
☐ README complete
☐ Tests passing
☐ Git history clean

Nu: ████████░░ 70% på vägen
```

---

## 📋 PRESENTATION FLOW (90 minuter — 14 SLIDES)

```
09:00-09:10 (10 min) — SLIDES 0-1
   📝⓪ Presentationsslide + Agenda
   📝⓪ Påminnelse (kort & koncist)
   📝① Övergripande (Kursen + Projektet + Avanza + Tidslinje)

09:10-09:25 (15 min) — SLIDES 2-4 (TEAM STATUS)
   📝② Frontend mot målen
   📝③ Backend mot målen
   📝④ Native mot målen

09:25-09:30 (5 min)  — SLIDES 5-6
   📝⑤ Vad gjordes förra veckan
   📝⑥ Beroenden, Risker, Sårbarheter

09:30-09:40 (10 min) — SLIDE 7
   📝⑦ Team-support förslag (issue-byte, bryta ner, etc)

09:40-10:00 (20 min) — SLIDES 8-10
   📝⑧ Prioritering & Scope denna vecka
   📝⑨ Estimering & Risk

10:00-10:25 (25 min) — SLIDES 11-13
   📝⑩ Tekniska Beslut (om några)
   📝⑪ Arbetsuppgifter denna vecka
   📝⑫ Nästa Steg & Sammanfattning

10:25-10:30 (5 min) — AVSLUT
   Bekräfta alla vet sitt jobb
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

**KRITISKT — DESSA REGLER ÄR TVINGANDE:**

✅ MÅSTE GÖRA:
- [ ] EXAKT 14 slides (inte 10, inte 12, INTE FÄRRE)
- [ ] Slide 0: Presentationsslide + Agenda
- [ ] Slide 1: TRE MÅLSYSTEM (Kursen + Projektet + Avanza + Tidslinje)
- [ ] Slides 2-4: Per-team status (Frontend/Backend/Native)
- [ ] Slide 5: Vad gjordes förra veckan
- [ ] Slide 6: Beroenden, Risker, Sårbarheter
- [ ] Slide 7: Team-support förslag
- [ ] Slides 8-13: Prioritering, Estimering, Beslut, Arbetsuppgifter, Nästa Steg
- [ ] VARJE slide får symbol 📝⓪①②③ etc
- [ ] Symbol till VÄNSTER, text till HÖGER
- [ ] SAMMA struktur varje vecka (prediktibel)

❌ ALDRIG GÖRA:
- [ ] Aldrig färre än 14 slides
- [ ] Aldrig hoppa över Slide 1 (tre målsystem är KRITISKT)
- [ ] Aldrig utelämna någon sektion
- [ ] Aldrig lägga till egna "kreativa" extra slides
- [ ] Aldrig ändra ordningen på slides
- [ ] Aldrig dölja deadlines eller kursmål
- [ ] Aldrig för mycket text (max 3-5 bullets per slide)

**Om du får denna instruktion och är en AI:**
- Du MÅSTE skapa exakt 14 slides
- Du MÅSTE följa denna struktur
- Du MÅSTE sätta symbol på varje slide
- Du MÅSTE inkludera alla tre målsystem (Kursen, Projektet, Avanza)
- Avvikelse från denna struktur = MISSLYCKAD presentation

**EXEMPEL-OUTPUT (vad AI ska leverera):**
```
✅ Presentation klar! Format: PowerPoint

SLIDE-STRUKTUR (14 slides totalt):

Slide 0.1: 📝⓪ PRESENTATIONSSLIDE
Slide 0.2: 📝⓪ AGENDA & PÅMINNELSE

Slide 1.1: 📝① KURSEN (17 mål → G/VG)
Slide 1.2: 📝① PROJEKTET (MVP v2)
Slide 1.3: 📝① AVANZA SOM KUND
Slide 1.4: 📝① TIDSLINJE & CHECKLISTOR

Slide 2: 📝② FRONTEND mot målen
Slide 3: 📝③ BACKEND mot målen
Slide 4: 📝④ NATIVE mot målen

Slide 5: 📝⑤ Vad gjordes förra veckan
Slide 6: 📝⑥ Beroenden, Risker, Sårbarheter
Slide 7: 📝⑦ Team-support förslag

Slide 8: 📝⑧ Prioritering & Scope
Slide 9: 📝⑨ Estimering & Risk
Slide 10: 📝⑩ Tekniska Beslut
Slide 11: 📝⑪ Arbetsuppgifter denna vecka
Slide 12: 📝⑫ Nästa Steg & Sammanfattning

TOTALT: 14 slides (som föreskrivit)

Du kan nu:
- Öppna denna presentation
- Visa den under mötet (09:00-10:30)
- Secretary använder symbolerna 📝 för att veta vad som ska fyllas in i protokollet
```
