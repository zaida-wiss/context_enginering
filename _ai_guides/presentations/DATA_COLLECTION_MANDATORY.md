---
name: data-collection-mandatory
description: MANDATORY — Complete data collection before any presentation rendering
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY DATA COLLECTION — INNAN PRESENTATION RENDERAS

🔗 **NOTE:** Alla externa URLs (Google Sheets, Google Docs, GitHub) är centraliserade i [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md). Se den filen för aktuella IDs och fallback-URLs.

⛔ **EXEMPEL-DATA I DENNA FIL:**
Alla exempelpersoner (<EXAMPLE_MEMBER_A>, <EXAMPLE_MEMBER_B>, etc) och issue-nummer i denna fil är INTE verklig projektdata.
Du får ALDRIG kopiera exempel-namn eller issue-nummer till en presentation.
Använd ENDAST GitHub-verifierad data från TEAM_ROSTER.md.

---

**DENNA CHECKLIST MÅSTE FÖLJA FÖRE NÅGON PRESENTATION GENERERAS.**

Om denna checklist inte är slutförd kommer presentationen att dölja arbete (som login-sidor, designsystem, andra stängda arbeten).

---

## ⏰ KURS-KONTEXT: DEADLINES & TIDSPLAN

**Presentationen måste också förstå kurs-tidskontext:**

📌 Se [`_memory/COURSE_DEADLINES.md`](../../_memory/COURSE_DEADLINES.md) för:
- Vilka kurs-deadlines påverkar denna vecka?
- Vad ska teamet fokusera på framåt? (kursuniquely)
- CTO-feedback? (sept 24 @ 4 PM)

**Använd denna kontext för att:**
- Förstå varför vissa arbeten prioriteras
- Se om denna vecka är pre-deadline-push (sprint, crunch)
- Markera om arbete kopplas till kursdeadlines

---

## 🚨 MANDATORY FALLBACK RULE

**OM GITHUB FAILAR — DU MÅSTE ANVÄNDA FALLBACKS**

Innan du säger "datainsamlingen är ofullständig":

```
1. FÖRSÖK: GitHub Issues/PRs/Commits (webben eller API)
   Failar? → Gå till fallback 1

2. FALLBACK 1: Google Sheets denna vecka (COMMITS + ALL DATA)
   🔗 https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/edit?usp=sharing
   
   Denna sheet innehåller:
     ✅ Commits denna vecka (primär fallback)
     ✅ Merged PRs (för punkt ①)
     ✅ Issues (öppna, stängda)
     ✅ Project Board status
   
   Kan du läsa denna? JA → använd denna för alla data
   NEJ → Gå till fallback 2

3. FALLBACK 2: Project Board denna vecka
   https://github.com/orgs/chas-challenge-2026/projects/31/views/1
   Kan du läsa denna? JA → använd status härifrån
   
4. FALLBACK 3: Meeting protocol denna vecka
   (länk i README.md)

5. ALLA FAILADE: Markera TYDLIGT "ej verifierat denna vecka"
   Exempel: "Data kunde inte samlas denna vecka (GitHub web + Sheets + Board alla begränsade)"
```

**REGEL: Presentationen får ALDRIG säga "ofullständig" utan att ha försökt alla fallbacks först.**

---

## ❌ PROBLEM VI LÖSER

**Tidigare problem:** Presentationen visade bara öppna issues och PR:er.

**Resultat:** All stängd arbete försvann ur bilden.

**Exempel på döldt arbete:**
- ❌ Login page (#40 / PR #90) — Zaida stängde den, visades inte
- ❌ Design system (#44) — Björn stängde den, visades inte  
- ❌ Top bar (#45) — Björn stängde den, visades inte

**Anledning:** Presentationen läste inte `closed issues denna vecka`.

---

## 🚨 DEFINITION: "DENNA VECKA" = SENASTE 7 DAGAR

**Denna vecka = exakt 7 dagar bakåt från IDAG**

Exempel (om idag är 2026-09-13):
- Denna vecka = 2026-09-06 till 2026-09-13
- INTE förra veckan
- INTE denna kalendervecka (mon-sun)
- INTE "sedan förra mötet" (som kan vara olika långt)

**REGEL: Datumfiltret är ALLTID [idag - 7 dagar] till [idag]**

---

## ✅ MANDATORY CHECKLIST — Du måste göra ALLT detta

**Innan du renderar någon slide, verifiera att du har:**

### 1. ARBETE SOM LEVERERADES DENNA VECKA (merged PRs in develop — PRIMARY)
- [ ] Läst GitHub /pulls: **Vilka PRs är MERGADE in i develop denna vecka?** (DET ÄR HUVUDFOKUS)
- [ ] **RÄKNA:** Totalt antal PRs denna vecka
- [ ] För varje PR: **Vem ÄGde den issuen?** (issue assignee, INTE reviewer eller merger!)
  - 🚨 KRITISK DISTINKTION:
    - ASSIGNEE (visas) = Vem som ÄGde/GJORDE arbetet
    - REVIEWER (döljs) = Vem som checkade koden
    - MERGER (döljs) = Vem som mergade (ofta samma som reviewer)
  - Exempel: ✅ "PR #90 Login · Zaida" (Zaida ÄGde det, även om Erik reviewade)
  - Exempel: ❌ "PR #90 Login · Erik" (FELAKTIG — Erik reviewade men Zaida ägde det)
- [ ] För varje PR: Vilket issue var länkat? (if any)
- [ ] Data innehåller: PR-nummer, merge-datum, **issue-assignee**, linked issue, issue-owner
- [ ] **Exempel:** PR #90 Login (assignee: Zaida, #40 var ägd av Zaida) — visar Zaida
- [ ] **Exempel:** PR #95 Design System (assignee: Björn, reviewer: Erik) — visar Björn INTE Erik
- [ ] **VIKTIGT:** Vi visar MERGED PRs in develop, INTE bara "stängda issues"
- [ ] **Regel:** Visa ASSIGNEE (ägare), INTE reviewer eller merger
- [ ] **Regel:** Fokus = merged code in develop, och VEMS JOBB det var
- [ ] **KRITISK REGEL:** Inget arbete får utelämnas för att det inte får plats på sliden
- [ ] **Om många PRs denna vecka (>5):** Dela på flera slides (①A.1, ①A.2, etc)
- [ ] **CHECKLIST:** Räkna GitHub PRs. Matcha antal på slide mot GitHub. Noll får försvinna.

### 2. COMMITS DENNA VECKA (grupperade per arbetsområde)
- [ ] Läst GitHub Commits: **Vilka commits pushades denna vecka?** (primär bevis på arbete)
- [ ] Commit-listan innehåller: hash, author, message, date, branch
- [ ] Commits är grupperade per arbetsområde ELLER per person (inte enskilda commits på slide)
- [ ] **Exempel:** Zaida: 4 commits on login-arbete denna vecka
- [ ] **Exempel:** Björn: 15 commits on designsystem denna vecka
- [ ] **VIKTIGT:** Commits = direkta bevis på arbete gjort, oavsett om issue är stängt

### 3. ARBETE I PROGRESS DENNA VECKA (open PRs + open branches med nya commits)
- [ ] Läst GitHub PRs: **Vilka PRs är öppna med uppdateringar denna vecka?** (under review/testing)
- [ ] Läst GitHub Branches: **Vilka branches har nya commits denna vecka?** (även utan PR ännu)
- [ ] Data innehåller: 
  * För öppna PRs: person, PR-nummer, commits sedan förra, status
  * För feature-branches: person, branch-namn, senaste commit, komit-antal denna vecka
- [ ] **Exempel:** <EXAMPLE_MEMBER_A>: #43 API-klient PR (3 commits denna vecka, under review)
- [ ] **Exempel:** <EXAMPLE_MEMBER_B>: feature/#45-risk PR (5 commits denna vecka, ongoing)
- [ ] **Exempel:** <EXAMPLE_MEMBER_C>: feature/#52-tests (2 commits denna vecka, not yet in PR)
- [ ] **VIKTIGT:** Visa arbete från:
  * Open PRs (under review)
  * Feature branches med commits (even without PR)
  * NOT comments — activation = commits, PR-updates, branch pushes

### 4. OPEN ISSUES MED AKTIVITET + DoD STATUS
- [ ] Läst GitHub Issues API/Web för issues **öppna med aktivitet denna vecka**
- [ ] Aktivitet = commits eller PR-updates, INTE bara kommentarer
- [ ] **För varje issue: läst issue-description för DoD-status**
- [ ] DoD-kolumner (AC, Tests, Review, Docs) fylld från issue-meddelandet
- [ ] Om DoD saknas i issue: markerat med `?` (inte antagande)
- [ ] **Exempel:** #43 API Client (Tomac, 3 commits denna vecka, DoD: AC✓ Tests◐ Review? Docs✕)

### 5. GITHUB PROJECT BOARD STATUS
- [ ] Läst Project Board för denna vecka
- [ ] Status per issue: DONE, IN PROGRESS, BACKLOG
- [ ] **Notering:** Board status ≠ Issue state ≠ DoD

### 6. MÖTESPROTOKOLLET
- [ ] Läst aktuellt mötesprotokollet från denna vecka
- [ ] Finns det tidigare beslut om fokus eller blockade?

---

## VERIFIKATION FÖRE RENDERING

**Innan du startar slide-renderingen, svara på dessa:**

```
Q1: Hur många issues stängdes denna vecka?
    Svar: [ ]
    (Exempel: 4 issues)

Q2: Vilka är assignees för dessa stängda issues?
    Svar: [ ]
    (Exempel: Zaida, Björn)

Q3: Hur många PRs mergades denna vecka?
    Svar: [ ]
    (Exempel: 3 PRs)

Q4: Vilka arbetsområden kan du identifiera?
    Svar: [ ]
    (Exempel: Frontend & Auth, Backend & Session, Native & Risk)

Q5: Skulle login-arbetet, designsystemet och topbar visas i presentationen?
    Svar: [ ]
    (Rätt svar: JA — alla tre stängdes denna vecka och ska visas)
```

**Om du INTE kan svara på dessa frågor → datainsamlingen är INTE komplett.**

Gör inte presentation förrän du kan svara på alla fem.

---

## 🚨 RULE: Presentationen uppfinner ALDRIG nya issues

**OM DU TÄNKER:** "Vi borde ha en issue för X"

**GÖR DU:** ALDRIG lägg det på presentations-slides

**ISTÄLLET:**
- Gör ett GitHub issue själv FÖRST (om det är verkligt behov)
- ELLER märk det som FÖRSLAG på en separat, explicit märkt sida
- ELLER ta upp det i nästa möte + dokumentera i mötesprotokoll

**REGEL:** Alla issues på presentation-slides MÅSTE redan finnas på GitHub denna vecka.
Inga "skulle kunna vara", "kanske behöves", "föreslår att vi..."

**UNDANTAG:** Om du har separat FÖRSLAG-sida (märkt som 📝 FÖRSLAG eller likande):
- MÅSTE vara helt separerad från GitHub-data
- MÅSTE ha "FÖRSLAG:" prefix på varje item
- MÅSTE komma EFTER all verifierad GitHub-data

---

---

## PRESENTATION DATA STRUCTURE

**Efter datainsamlingen bygger du MEETING_STATE med:**

- `closed_issues_this_week`: Lista av stängda issues (med assignee, DoD-status)
- `merged_prs_this_week`: Lista av mergade PRs (med linked issues)
- `commits_this_week`: Commits grupperade per arbetsområde
- `open_issues_with_activity`: Öppna issues med faktisk arbetsaktivitet denna vecka
- `work_areas`: Grupperingar av arbete per område (Frontend & Auth, etc)

**Först SEDAN du har MEETING_STATE → du renderar slides.**

---

## RESULTAT

**Med denna checklist kommer presentationen att visa:**

✅ Login page + auth (Zaida)  
✅ Design system + topbar (Björn)  
✅ Alla andra stängda arbeten denna vecka  
✅ Pågående arbete med faktisk framdrift  
✅ Arbetsområden, inte bara issues  

**Istället för:** "Presentationen ser tom ut, vi gjorde nästan ingenting" → **Sant:** "Vi gjorde mycket arbete denna vecka"

---

---

## 🚨 NAMING RULE AFTER VERIFICATION

**Efter att verifierings-sliden "Alla i teamet" körs:**

Presentationen får BARA nämna namn som finns på verifierings-sliden.

**Exempel:**

Verifierings-slide visar:
- Zaida: PR #68
- Tomac: PR #80
- Björn: Review PR #90
- Pär: (Ingen verifierad GitHub-aktivitet denna vecka)
- Henrik: (Ingen verifierad GitHub-aktivitet denna vecka)

→ Senare i presentationen:
- ✅ Kan nämna Zaida, Tomac, Björn
- ❌ Får INTE nämna Pär eller Henrik (hade ingen aktivitet denna vecka)
- ❌ Får ALDRIG använda exempel-namn från instruktioner — de är platshållare, inte riktiga personer

**KRITISK:** Presentationen kan INTE växla mellan "verifierad data" och "exempel".

Om Pär eller Henrik saknar aktivitet denna vecka → de syns på verifierings-sliden som "(Ingen aktivitet)" och nämns inte senare SÅVIDA de inte får ny GitHub-data.

⛔ **EXEMPEL-NAMN I INSTRUKTIONER:**
Denna fil innehåller ofta exempel som `<EXAMPLE_MEMBER_A>`, `<EXAMPLE_MEMBER_B>`, etc.
**DESSA ÄR ALDRIG VERKLIGA PERSONERNA.**
Du får ALDRIG kopiera exempel-namn till en presentation.

**DENNA CHECKLIST ÄR OBLIGATORISK.**

Om du hoppar över den kommer du att:
- Dölja arbete (login, designsystem, osv)
- ELLER blanda exempel-namn med faktiska namn
- ELLER nämna personer som inte hade arbete denna vecka

---

**Senast uppdaterad:** 2026-09-13
