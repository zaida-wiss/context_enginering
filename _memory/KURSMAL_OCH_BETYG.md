---
name: course-goals-grading
description: Course grading criteria, learning outcomes, deadlines — separate from DoD
metadata:
  type: project
---

# Kursmål & Betygsättning

**VIKTIGT:** Detta är PEDAGOGISK målsättning från skolan. Inte samma som DoD!

---

## ⚠️ TÄVLINGEN ≠ BETYGET

- **Tävlingsresultatet påverkar INTE ditt betyg**
- Finaldagen är INTE examinerande
- Du får betyg G eller VG baserat på slutleverans + kursmål
- Du får samma betyg oavsett om du går till final eller vinner

### Din Prioritering

1. **FÖRST:** Uppfylla alla 17 kursmål ← **Din betyg**
2. **SEDAN:** Lösa Annas problem + imponera på kund ← Kan ge finalplats
3. **BONUS:** Vinna tävlingen mot andra lag ← Coolt men inte avgörande

**Fokusera på kursmål, inte på att vinna tävlingen.**

---

## 📅 Tidsplan & Milestones

**Kursen löper 12 veckor: 17 aug – 6 nov 2026**

### Kritiska Deadlines

| Vecka | Datum | Mileston | Din Deadline |
|-------|-------|----------|--------------|
| V1 | 17-21 aug | Kursstart + första dialogfredag | Miljö installerad |
| V2 | 24 aug | Sprintstart: planering | Backlog + MVP klara |
| V3-V5 | 31 aug-18 sep | Produktion med veckovisa checkpoints | README-struktur, tester, beslutslogg |
| **V6** | **24 sep, 16:00** | **CTO-underlag deadline** | **Kod, arkitektur, beslut klara** |
| V7 | 28 sep & 1 okt | CTO-feedforward + inspelad demo | Bearbeta feedback, demo-plan |
| V8 | 5 okt | UX & DM-feedforward | Omsätta feedback till prioritering |
| **V9** | **15 okt, 17:00** | **Kvaldemo-plan deadline** | **Stabilisering + presentation klara** |
| V10 | 22 okt | **KVALDEMO** - livedemo för kund | Live-demo, finalistval |
| **V11** | **26 okt, 16:00** | **Omtagsplan deadline** | **Bearbeta kundfeedback** |
| **V12** | **4 nov, 15:00** | **SLUTLEVERANS deadline** | **Allt inlämnat** |
| V12 | 5 nov, 09:00 | **FINALDAG** - livedemo för juryn | De 4 finalistteamen presenterar |
| - | 6 nov | Betyg sätts | **Individuell bedömning** |

### Fredagar = Dialogdag (Obligatoriskt)

- Inget projektarbete på fredagar
- Professionella dialoger med branschen
- Career workshops
- Skyddad tid för att bygga nätverk

**Fredagarna är också betygsgrundande** – detta är Färdighet 8: "Initiera och driva professionella dialoger inom IT"

---

## Vad Som Måste Vara Klart NÄR

**Före V6 (24 sep):**
- ✅ Kärnflödet fungerar
- ✅ README-struktur på plats
- ✅ Veckovisa checkpoints genomförda
- ✅ Teststatus dokumenterad
- ✅ Beslutslogg igång
- ✅ Git-historia är tydlig
- ⚠️ Inte perfekt – men visar riktning

**Före V9 (15 okt):**
- ✅ Kundfeedback från V7-V8 implementerad
- ✅ Demo-plan + fallback klar
- ✅ Stabilisering påbörjad
- ✅ Presentation-material förberett

**Före V12 (4 nov):**
- ✅ ALLT är godkänt enligt Definition of Done
- ✅ Kundfeedback från V10 implementerad
- ✅ Slutleverans är körbar
- ✅ README är komplett
- ✅ Teststatus dokumenterad
- ✅ Fallback på plats

---

## Vad Examinatorn Tittar På

**Slutleverans bedöms på:**
- Funktionalitet (kursmål 1-4)
- Dokumentation (Git, README, beslut)
- Kodkvalitet (tester, granskning)
- Din individuella insats (Git-historia)
- Kursmål-uppfyllelse (alla 17)

**Finalplats bedöms INTE enligt kursmål** – betyget bygger på slutleveransen, inte på tävlingsresultatet.

---

## Godkänd = Allt Ovan + Ett Fungerande System

**En godkänd v2 är INTE:**
- En perfekt UI/UX (bra är nog)
- Alla möjliga features (MVP räcker)
- 100% kodtäckning (70%+ är tillräckligt)
- Helt utan buggar (men kritiska flödet fungerar)

**En godkänd v2 ÄR:**
- Kärnflödet fungerar från start till slut
- Användaren kan back-testa strategier
- Allt är dokumenterat
- Git-historia är tydlig
- Kan köras lokalt och demoas
- Svarar på Annas behov: "Förklara min portfölj utan att göra det för komplicerat"

---

## ✅ Kärnflödet Fungerar

Användaren kan gå igenom hela MVP-flödet från start till slut:

- [ ] Användare kan logga in
- [ ] Portföljöversikt visas med alla sparformer
- [ ] Värden är konverterade till SEK (FX-justering)
- [ ] Riskmått visas (allokering, volatilitet, Sharpe-ratio)
- [ ] Användare kan sätta målallokering
- [ ] Avvikelse-indikator visas tydligt
- [ ] Back-testing-motor kan köras
- [ ] Rebalanseringsförslag presenteras

**Acceptance Criteria:** Du kan köra genom hela flödet på ~5 minuter utan att något kraschar.
