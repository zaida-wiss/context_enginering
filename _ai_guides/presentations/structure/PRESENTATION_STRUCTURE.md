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
- **①A: Levererat denna vecka** — **MERGED PRs in develop** (primary focus)
- **①B: Byggde vidare denna vecka** — pågående arbete med verifierad framdrift (commits)

**Obligatoriska element:**
- ✅ **HUVUDFOKUS: Vilka PRs blev MERGED in i develop denna vecka?**
- ✅ För varje PR: **Vem ÄGde den issuen?** (issue assignee eller PR-author)
- ✅ Visa länk mellan PR + issue-owner (dubbelt namn om samma person)
- ✅ Alla teammedlemmar måste synas (med namn + verifierat bidrag)
- ✅ Arbetsområden, inte bara issue-nummer (Frontend & Auth, Backend & Risk, etc)
- ✅ Differentiera mellan "jobbar på" och "faktiskt klar" (DoD-verifierat)
- ✅ Effektbeskrivning: varför detta arbete spelar roll

**Data från:** **Merged PRs in develop** (denna vecka) — repo-first reconstruction
**INTE:** Bara "closed issues" eller "issues utan merge"

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
- **③A: Var är vi? — Issue- och DoD-status**
- **③B: Vad behöver vi göra? — Handlingsplan, in/utgående beroenden och teamrisker**
- (Eventuellt) **③C: Visuell verifiering** — skärmdump från dev-environment

### ③A: Issue Status Table (OBLIGATORISKT FORMAT)

MÅSTE visas som en tabell, aldrig som lista eller generell text.

**Varje relevant aktiv issue ska visa:**
- issue-nummer + faktisk titel från GitHub
- kort beskrivning av vad issuen innebär
- faktisk assignee (flera om flera ansvariga)
- Board-status + GitHub Issue state (skildt)
- DoD-checkpoints som separata kolumner:
  **AC | Tests | Review | Docs**
- relevant PR/Git-aktivitet denna vecka

**Ingen generell lista såsom "Öppna: #89, #88, #87..." är tillåten.**
**Ingen generell DoD-förklaring får ersätta DoD-status för enskilda issues.**

Om tabellen inte ryms läsbart:
→ dela ③A på flera slides: ③A.1, ③A.2, etc
→ Ta ALDRIG bort kolumner eller assignees för att få plats

**Se PRESENTATION_SPEC.md för exakt tabell-format.**

### ③B: Handlingsplan + Beroenden + Risker (OBLIGATORISKT)

Efter denna slide ska teammedlemmen förstå:
- Vad är nästa prioriterade arbete per person?
- Vem väntar vi på?
- Vem väntar på oss?
- Vilka risker påverkar teamets plan?

**Fyra obligatoriska sektioner:**
1. **Nästa arbete** — prioriterad ordning per issue + assignee
2. **Vi väntar på** — inkommande beroenden (dependency vs blocker)
3. **Andra väntar på oss** — utgående beroenden (vem väntade vi på?)
4. **Risker att diskutera** — teamspecifika risker som kräver beslut/uppmärksamhet

**Allt måste kopplas till verkliga issues, personer, beroenden och risker.**

**Ingen generell lista är tillåten** (t.ex. "Fortsätt med tester", "Stäng DoD").

**See PRESENTATION_SPEC.md for exact table formats.**

**Obligatoriska element:**
- ✅ Prioriterat nästa arbete per issue och assignee
- ✅ Konkret nästa steg och verifierbart färdigkriterium
- ✅ INKOMMANDE beroenden: vem/vad blockerar eller fördröjer oss?
- ✅ UTGÅENDE beroenden: vilka team/personer väntar på oss?
- ✅ Fallback-arbete för varje kritiskt dependency
- ✅ Risker som specifikt påverkar teamets plan
- ✅ Ägare och nästa åtgärd för varje blocker/risk
- ✅ Beslut som måste fattas på mötet tydligt markerade

**Data från:** GitHub commits, open issues, PRs, DoD status per issue, team roster

---

## 📝④ BACKEND TEAM

**Samma struktur och visuell utrymme som Frontend (③)**

**Slides (kan vara 2-3):**
- **④A: Var är vi? — Issue- och DoD-status** (issue-tabell format)
- **④B: Vad behöver vi göra? — Handlingsplan, in/utgående beroenden och teamrisker**
- (Eventuellt) **④C: Visuell verifiering**

**Exakt samma regler som ③A och ③B.**
**Se PRESENTATION_SPEC.md för tabell-format och obligatoriska sektioner.**

---

## 📝⑤ NATIVE / SYSTEM TEAM

**Samma struktur och visuell utrymme som Frontend (③) och Backend (④)**

**Slides (kan vara 2-3):**
- **⑤A: Var är vi? — Issue- och DoD-status** (issue-tabell format)
- **⑤B: Vad behöver vi göra? — Handlingsplan, in/utgående beroenden och teamrisker**
- (Eventuellt) **⑤C: Visuell verifiering**

**Exakt samma regler som ③A/④A och ③B/④B.**
**Se PRESENTATION_SPEC.md för tabell-format och obligatoriska sektioner.**

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

## 📝⑫ SPRINTPLAN & PLANERINGSKONTROLL

**Syfte:** Översätta sprintmålet till en realistisk arbetsplan + kvalitetsgranska GitHub Project Board/backlog

**DENNA PUNKT GANSKA INTE BARA BESKRIVA PLANEN.**

AI ska analysera om planen är genomförbar utifrån verifierad projektdata från tidigare mötespunkter (①–⑪).
AI agerar som en erfaren projektledare och synliggör luckor, risker och förbättringar.

### ⑫A — PLANERINGSKONTROLL

**MÅSTE svara på:**
1. Är sprintmålet realistiskt med aktuell kapacitet?
2. Vilka issues ligger på kritisk väg?
3. Vilka beroenden styr ordningen?
4. Vilka team blockerar andra team?
5. Finns tillräckligt oberoende fallback-arbete?
6. Finns DoD-arbete som ännu inte är planerat?
7. Finns arbete i sprinten som inte bidrar till sprintmålet?
8. Finns för mycket arbete jämfört med verifierad kapacitet?

**Visa en sammanfattande bedömning:**

| Kontroll | Bedömning | Varför |
|----------|-----------|--------|
| Sprintmål mot kapacitet | 🟢/🟡/🔴 | [2-4 verifierade orsaker] |
| Kritisk väg | [status] | [vem → vem → vem] |
| Fallback-arbete | ✓/⚠️ | [antal oberoende issues] |
| Board-kvalitet | [status] | [antal issues med divergens] |
| Backlog | [status] | [luckor eller gamla items] |

**Färgkod (statussemantik):**
- 🟢 RIMLIG — planen håller
- 🟡 TIGHT / BEHÖVER BESLUT — resursöverkant eller beroenden krävs diskussion
- 🔴 EJ REALISTISK — sprintmålet eller planen måste justeras

### ⑫B–D — TEAMETS PRIORITERAD ARBETSKÖ

**Varje team visas som en prioriterad kö:**

| Ordning | Issue | Ägare | Estimat | Varför nu? | Beroende | Klart när |
|---------|-------|-------|---------|-----------|----------|-----------|
| 1 | #92 – Riskmotor | Anna | 13h | Sprintmål | Backend API | Tests + verifierad |
| 2 | #93 – … | … | … | Frigör Frontend | Inte blockerad | DoD ✓ |

**KRAV:**
- Issue-nummer + titel + faktisk assignee
- Verifierat estimat (om saknas: "Ej estimerad — behöver estimeras idag")
- Prioriteringsordning
- Varför arbetet ligger här (använd EN av: Sprintmål, Kritisk väg, Frigör annat team, Riskreduktion, DoD-stängning, Oberoende fallback, Kundvärde)
- Dependency/blocker
- Konkret DoD/färdigkriterium

### ⑫E — PROJECT BOARD & BACKLOG REVIEW

**AI jämför verifierat projektläge mot Project Board.**

**Visa fyra kategorier:**

#### 1. BOARD BÖR UPPDATERAS

Issues där faktisk status och Board-status verkar skilja sig:

```
#XX – Titel · Assignee
Nu: Board [kolumn] / Issue [state] / DoD [status]
Förslag: flytta till [status]
Orsak: [kort verifierad orsak]
```

#### 2. BÖR PRIORITERAS UPP

Befintliga issues som bör göras tidigare därför att de:
- ligger på kritisk väg
- blockerar annat team
- krävs för sprintmålet
- reducerar konkret hög risk
- behövs för demo/integration/DoD

#### 3. BÖR PRIORITERAS NED

Befintliga issues som:
- inte bidrar till sprintmålet denna vecka
- inte ligger på kritisk väg
- kan vänta utan att blockera leverans

*(Detta är ett FÖRSLAG, inte automatiskt beslut)*

#### 4. FÖRESLAGNA NYA ISSUES

AI får föreslå ett nytt issue ENDAST när verifierad projektdata visar ett konkret arbete som saknar motsvarande issue.

**VARJE FÖRSLAG MARKERAS TYDLIGT: "FÖRSLAG — finns ännu inte i GitHub"**

Format för varje förslag:

```
FÖRESLAGET ISSUE:

Titel:
Problem / behov:
Varför behövs det:
Acceptance criteria:
Föreslagen assignee:
Estimering: [eller "Behöver estimeras"]
Prioritet:
Blockerar / blockeras av:
Koppling till sprintmål:
```

**OBLIGATORISKA ELEMENT:**
- ✅ Prioriterad arbetskö per team (inte kalender)
- ✅ Verifierade estimat (eller märkt "behöver estimeras")
- ✅ Varför-kolumn länkad till sprintmål/kritisk väg/beroenden
- ✅ Planeringskontroll med bedömning (🟢/🟡/🔴)
- ✅ Board & Backlog Review med konkreta förbättringsförslag
- ✅ Nya issue-förslag tydligt märkta som "FÖRSLAG"
- ✅ Klart dödt för varje issue (DoD eller demo-kriterium)

**Data från:** GitHub issues, estimat, DoD-status, verifierad kapacitet från ⑧, prioritering från ⑨, tekniska beslut från ⑩, sprintmål från ⑪

---

## 📝⑬ NÄSTA STEG / ACTIONS — MÖTETS "COMMIT"

**Syfte:** Omvandla punkt ⑫ besluten till konkreta GitHub-actions

**DENNA PUNKT ÄR KRITISK:** Det här är där mötet blir verklig arbetsplan, inte bara diskussion.

### KOPPLING FRÅN ⑫ → ⑬

**Punkt ⑫:** AI analyserar, teamet beslutar
**Punkt ⑬:** Besluten omvandlas till konkreta GitHub-ändringar + ansvar

### Exempel på koppling:

⑫ Förslag: "#91 bör prioriteras före #87 därför att Native väntar på API-kontraktet"

Efter diskussion i mötet:

⑬ **BESLUT:** Flytta #91 till Position 1. Björn äger. Klart senast onsdag.
   → Åtgärd: Uppdatera Board efter mötet (vem?)
   → Åtgärd: Tilldela #91 till Björn + sätt förfallodatum (onsdag)

### Slides

- **⑬A: BESLUT DENNA MÖTE** — vad bestämde vi?
- **⑬B: ÄNDRINGAR I GITHUB** — vad uppdaterar vi efter mötet?
- **⑬C: PAIRING & BLOCKERS** — vem jobbar med vem? Vad löser vi idag?

### ⑬A — BESLUT DENNA MÖTE

Visa endast beslut som är nödvändiga för sprintplanen:

| Beslut | Från punkt | Ansvar | Åtgärd |
|--------|-----------|--------|--------|
| Björn äger #91, prioriterat position 1 | ⑫ | Björn | Tilldela + deadline: onsdag |
| Nytt issue för integrationstest behövs | ⑫E | PL | Skapa issue före nästa möte |
| Frontend/Backend låser API-kontrakt i ⑩ | ⑩ | Tomac/Anna | Dokumentera kontrakt i issue |
| Omprioritera #45 til senare sprint | ⑨ | PL | Flytta till backlog-sprinten |

### ⑬B — ÄNDRINGAR I GITHUB

**Vad uppdateras efter mötet och av vem?**

| Åtgärd | Issue | Förslag från | Ansvar | Status |
|--------|-------|------------|--------|--------|
| Flytta status | #XX · Namn | ⑫E | PL | ☐ |
| Prioritera upp | #YY · Namn | ⑫ | PL | ☐ |
| Tilldela | #ZZ | ⑫ | Assignee | ☐ |
| Skapa issue | Nytt · Integrationstest | ⑫E | PL | ☐ |
| Dela issue | #AA · Namn | ⑫E | PL | ☐ |

**Varje rad är en konkret GitHub-operation.**

### ⑬C — PAIRING & BLOCKERS ATT LÖSA IDAG

**Vad bokras in och vad behöver lösa innan nästa arbete kan börja?**

**Pairing-sessioner:**
- Datum, tid, vilka två personer, vad fokus är

**Blockers att lösa:**
- Vilken blocker
- Vem äger att lösa den
- Deadline för lösning
- Fallback om det inte löses

**Obligatoriska element:**
- ✅ Konkreta beslut från mötet (inte åsikter)
- ✅ Vem äger varje åtgärd?
- ✅ Deadlines för ändringar i GitHub
- ✅ Pairing-sessioner inbokade (datum + tid + syfte)
- ✅ Blockers med ansvar och fallback
- ✅ Koppling till punkt ⑫ (varifrån kom beslutet?)

**Data från:** Diskussionerna under ①–⑫, besluten som fattades

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
