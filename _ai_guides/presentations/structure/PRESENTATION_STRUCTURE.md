---
name: presentation_structure
description: Sprint meeting structure — 14 mötespunkter i pedagogisk ordning (Fakta → Analys → Beslut)
metadata:
  type: reference
  critical: true
---

# 📋 PRESENTATION STRUCTURE — 14 Mötespunkter

**Denna struktur följer en tydlig logik: FAKTA → ANALYS → BESLUT**

Mötet samlar först information, analyserar därefter situationen, och bestämmer först sedan planen.

---

## 🎯 MÖTESPRUNKTERNA — Ordning & Syfte

Varje punkt kan ha **en eller flera slides** (markerade 📝①A, 📝①B, etc).

---

## 📝① SEDAN FÖRRA MÖTET — Erkännande-retrospektiv

**Syfte:** Visa vad som faktiskt blev klart denna vecka

**Slides:**
- **①A: Levererat denna vecka** — merged PRs, closed issues, faktiska releases
- **①B: Byggde vidare denna vecka** — pågående arbete med verifierad framdrift (commits)

**Obligatoriska element:**
- ✅ Alla teammedlemmar måste synas (med namn + verifierat bidrag)
- ✅ Arbetsområden, inte bara issue-nummer (Frontend & Auth, Backend & Risk, etc)
- ✅ Differentiera mellan "jobbar på" och "faktiskt klar" (DoD-verifierat)
- ✅ Effektbeskrivning: varför detta arbete spelar roll

**Data från:** Commits, merged PRs, closed issues (denna vecka) — repo-first reconstruction

---

## 📝② PROJEKTETS NULÄGE & NÄSTA DEADLINE

**Syfte:** Etablera referenspunkt för all kommande analys

**Slides:**
- **②A: Övergripande status** — var står vi mot slutleverans?
- **②B: Nästa externa checkpoint** — nästa deadline/demo/milstolpe och hur långt ifrån vi är

**Obligatoriska element:**
- ✅ Slutleverans-deadline synlig och framräknad
- ✅ Nästa delpunkt/checkpoint (demo, review, integration-test)
- ✅ Status mot deadline: 🟢 ON TRACK / 🟠 SLIGHT RISK / 🔴 CRITICAL
- ✅ Projektets kundvärde/affärsbehov som bakgrund (varför gör vi det här?)

**Data från:** Project Board, meeting protocol, course requirements

---

## 📝③ FRONTEND TEAM

**Slides (kan vara 2-3):**
- **③A: Var är vi?** — status per person, open issues med aktivitet, pågående PRs
- **③B: Vad behöver vi göra?** — prioriterade issues, estimat, blockers
- (Eventuellt) **③C: Visuell verifiering** — skärmdump från dev-environment

**Obligatoriska element:**
- ✅ Alla Frontend-medlemmar måste synas (namn + aktivitet denna vecka)
- ✅ Tydlig separation mellan "pågår" och "blockerad"
- ✅ DoD-status för varje issue som ligger på "nästan klart"
- ✅ Ansvar + kapacitet per person

**Data från:** GitHub commits, open issues, PRs, team roster

---

## 📝④ BACKEND TEAM

**Samma struktur och visuell utrymme som Frontend (③)**

**Slides (kan vara 2-3):**
- **④A: Var är vi?**
- **④B: Vad behöver vi göra?**
- (Eventuellt) **④C: Visuell verifiering**

---

## 📝⑤ NATIVE / SYSTEM TEAM

**Samma struktur och visuell utrymme som Frontend (③) och Backend (④)**

**Slides (kan vara 2-3):**
- **⑤A: Var är vi?**
- **⑤B: Vad behöver vi göra?**
- (Eventuellt) **⑤C: Visuell verifiering**

---

## 📝⑥ BEROENDEN & BLOCKERS

**Syfte:** Identifiera vad som hindrar framsteg och vad vi kan göra åt det

**Slides:**
- **⑥A: Blocker-flödesdiagram** — vem väntar på vem? (visuell)
- **⑥B: Åtgärd denna vecka** — vad gör vi medan vi väntar?

**Obligatoriska element:**
- ✅ Varje blocker visar: VAD väntar, PÅ VAD, VEM påverkas
- ✅ Sannolikhet att lösas denna vecka
- ✅ Alternativ väg framåt (går något annat att göra?)
- ✅ Ägarskap för att lösa blockern

**Data från:** GitHub issues, PRs, meeting protocol

---

## 📝⑦ RISKER

**Syfte:** Identifiera vad som kan hindra leveransen

**Slides:**
- **⑦A: Riskmatris** — Sannolikhet × Konsekvens
- **⑦B: Åtgärder** — vad gör vi proaktivt?

**Obligatoriska element:**
- ✅ Varje risk visar: TYP (teknisk, kapacitet, extern), SANNOLIKHET, KONSEKVENS
- ✅ Åtgärd (förebyggande eller beredskapplan)
- ✅ Ansvar för att monitorera
- ✅ Tidshorizon

**Data från:** Team input, meeting protocol, technical decisions

---

## 📝⑧ KAPACITET & ESTIMERING

**Syfte:** Verifiera att planen är realistisk

**Slides:**
- **⑧A: Timmar tillgänglig vs behövd** per team
- **⑧B: Överbelastning eller buffert** — kan vi klara det här?

**Obligatoriska element:**
- ✅ Tillgänglig kapacitet denna vecka (personer × timmar)
- ✅ Estimerad behov (alla issues + viss buffer)
- ✅ Skillnad: buffer eller överbelastning?
- ✅ Om överbelastning: vad skjuts upp?

**Data från:** Team estimates, issue estimates, available hours

---

## 📝⑨ PRIORITERING & SCOPE

**Syfte:** Besluta vad som FAKTISKT ska göras baserat på kapacitet & risker

**Slides:**
- **⑨A: Must / Next / Later-matris** — kategorisera issues
- **⑨B: Denna vecka Definitivt + Denna vecka Gärna** — vad är finalists?

**Obligatoriska element:**
- ✅ MUST-HA (blockar annars andra team eller slut-deadline)
- ✅ NEXT (viktigt men kan skjutas upp en vecka)
- ✅ LATER (nice-to-have, kan vänta)
- ✅ Avgöring: vilka MUST går in i sprintplanen?

**Data från:** Previous analysis (kapacitet, blockers, risker, kundvärde)

---

## 📝⑩ TEKNISKA BESLUT

**Syfte:** Fastställa kontrakt mellan team

**Slides:**
- **⑩A: API-kontrakt mellan Frontend-Backend** (om relevant)
- **⑩B: Native-integration & JNA (om relevant)**
- **⑩C: Andra kritiska avtal** (database schema, deployment procedure, etc)

**Obligatoriska element:**
- ✅ BESLUT (vad är fastslaget?)
- ✅ IMPLEMENTERAD I (vem bygger vad?)
- ✅ VERIFIERING (hur vet vi det fungerar tillsammans?)
- ✅ Deadline för implementering

**Data från:** Technical discussions, active branches, architecture decisions

---

## 📝⑪ SPRINTMÅL

**Syfte:** Formulera målet EFTER vi förstår läget, kapaciteten och prioriteringarna

**Denna punkt avgör:** Vad ska funktionera när sprinten är slut?

**Slides:**
- **⑪A: Sprintmål (text)** — kort formulering av veckans fokus
- **⑪B: Success criteria** — hur verifierar vi att målet är uppnått?

**Obligatoriska element:**
- ✅ Mål formulerat utifrån faktisk kapacitet (inte idealt)
- ✅ Success criteria som kan verifieras (demobara funktioner, tester klara, etc)
- ✅ Referens till slutleverans-deadline (hur bidrar detta till målet?)
- ✅ Kundbehov / affärslogik tydlig

**Format:** "Vid slutet av veckan ska [X] fungera så att [Y] kan [Z]"

**Exempel:** "Vid slutet av veckan ska login med två-faktor fungera så att säkerhetstesten kan passa."

---

## 📝⑫ SPRINTPLAN

**Syfte:** Konkret kodning av sprintmålet

**Slides:**
- **⑫A: Frontend sprintplan** — issues, ordning, assignees, pairing
- **⑫B: Backend sprintplan** — (samma)
- **⑫C: Native sprintplan** — (samma)

**Obligatoriska element:**
- ✅ Issue-nummer + titel + assignee + estimat
- ✅ Ordning (vad börjar vi med?)
- ✅ Beroenden markerade
- ✅ Pairing-sessioner inbokade
- ✅ Clear DoD for each issue

**Data från:** GitHub issues, team input, previous decisions

---

## 📝⑬ NÄSTA STEG / ACTIONS

**Syfte:** Konkreta åtgärder direkt efter mötet

**Slides:**
- **⑬A: Denna dag före nästa möte**
- **⑬B: Denna vecka före nästa sprint**

**Obligatoriska element:**
- ✅ Issues som ska tilldelas / skapas / uppdateras
- ✅ Pairing-sessioner att boka (datum + tid)
- ✅ Blockers att lösa omedelbar (med ansvar)
- ✅ GitHub Board uppdateras efter mötet

**Data från:** Mötes-decisions

---

## 📝⑭ FRÅGOR FRÅN PL / STAKEHOLDERS

**Syfte:** Bara sådant teamet INTE kan lösa självt

**Slides:**
- **⑭A: Öppna frågor** — vad behöver vi input på?
- **⑭B: Gällande beslut från ledningen** — vad är ändrat sedan förra mötet?

**Obligatoriska element:**
- ✅ Tydlig fråga (inte bara "vad tycker du?")
- ✅ Varför det spelar roll
- ✅ Tidsgräns för svar (om relevant)
- ✅ Vem från PL som kan svara

---

## 🎯 SEX KRITISKA ELEMENT SOM ALDRIG FÅR FÖRSVINNA

**Dessa måste finnas någonstans i presentationen, inte dölda:**

1. **NÄSTA DEADLINE tidigt** (punkt ②)
   - Projektets övergripande slutdatum
   - Nästa delpunkt/checkpoint
   - Status mot deadline redan på slide två

2. **PROJEKTETS KUNDVÄRDE som referenspunkt**
   - Varför gör vi det här? Vem behöver det?
   - Används för att bedöma prioritering

3. **DEFINITION OF DONE (DoD) som skillnad**
   - "Jobbar på" (commits, PR öppet) ≠ "faktiskt klart" (merged, tests pass, DoD)
   - Måste synas på slide ①

4. **ALLA TEAMMEDLEMMAR med namn och verifierat bidrag**
   - Eller explicit: "[Namn] — ingen verifierad GitHub-aktivitet denna vecka"
   - Ingen person får försvinna bara för att de inte är assignee

5. **BESLUT från DISKUSSIONER**
   - Klart märkat: "Vi bestämde att..." eller "BESLUT: ..."
   - Kan skiljas från "Vi diskuterade möjligheten att..."
   - Mötet ska veta vad som är faktisk beslut

6. **TYDLIG HANDLINGSPLAN för varje person**
   - "Vad gör JAG härnäst?"
   - "Vad ska mitt TEAM åstadkomma?"
   - "Vad försöker PROJEKTET nå?"

---

## 🧠 VARFÖR DENNA ORDNING FUNGERAR

```
GAMLA ORDNING (problem):
  1. Sprintmål first (innan teamläget är känt)
  2. Sen status (kan motsäga målet)
  3. Resultat: Målet är ofta orealistiskt
  
NYA ORDNING (logisk):
  ① Faktarapporten (vad hände?)
  ② Referenspunkt (slutdatum, nästa checkpoint)
  ③④⑤ Teamstatus (var står vi?)
  ⑥ Blockers (vad hindrar oss?)
  ⑦ Risker (vad kan brista?)
  ⑧ Kapacitet (realistiska timmar?)
  ⑨ Prioritering (vad är viktigast?)
  ⑩ Tekniska beslut (vilka kontrakt?)
  ⑪ SPRINTMÅL (nu kan vi sätta ett realistiskt mål)
  ⑫ Plan (hur genomför vi det?)
  ⑬ Actions (vem gör vad?)
  ⑭ PL-input (vad behöver vi från ledningen?)
  
RESULTAT: Målet är grundat i fakta, inte idealism
```

---

## 📐 VARJE MÖTESPUNKT KAN HA FLERA SLIDES

```
Exempel:
  📝③ FRONTEND
    ③A Var är vi?
    ③B Vad behöver vi göra?
    ③C Visuell verifiering (optional)
    
Alla tre slides märks 📝③ men A/B/C visar vilken av dem det är.
En mötespunkt kan ha 1-3 slides beroende på innehål.
```

---

## 🚨 DETTA ÄR EN FÖRÄNDRING FRÅN TIDIGARE STRUKTUR

**Om du körs gamla presentationer:**
- De kan ha sprintmålet på punkt ②
- De kan ha blockers / risker blandade i teamstatus
- De kan missa deadlines eller kundvärde

**Nya presentationer ska:**
- Följa denna ordning (① → ②→ ... → ⑭)
- Säkerställa de sex kritiska elementen
- Märka varje slide med rätt symbol (📝①, 📝②, etc)

---

**Senast uppdaterad:** 2026-09-13
