---
name: data-collection-mandatory
description: MANDATORY — Complete data collection before any presentation rendering
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY DATA COLLECTION — INNAN PRESENTATION RENDERAS

**DENNA CHECKLIST MÅSTE FÖLJA FÖRE NÅGON PRESENTATION GENERERAS.**

Om denna checklist inte är slutförd kommer presentationen att dölja arbete (som login-sidor, designsystem, andra stängda arbeten).

---

## 🚨 MANDATORY FALLBACK RULE

**OM GITHUB FAILAR — DU MÅSTE ANVÄNDA FALLBACKS**

Innan du säger "datainsamlingen är ofullständig":

```
1. FÖRSÖK: GitHub Issues/PRs/Commits (webben eller API)
   Failar? → Gå till fallback 1

2. FALLBACK 1: Google Sheets denna vecka
   https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/
   Kan du läsa denna? JA → använd denna
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

## ✅ MANDATORY CHECKLIST — Du måste göra ALLT detta

**Innan du renderar någon slide, verifiera att du har:**

### 1. ARBETE SOM LEVERERADES DENNA VECKA (merged PRs + closed issues)
- [ ] Läst GitHub: **Vilka PRs mergades denna vecka?** (primär källa för arbete)
- [ ] Läst GitHub: **Vilka issues stängdes denna vecka?** (sekundär verifiering)
- [ ] Data innehåller: author, PR-nummer, merge-datum, linked issue, commits
- [ ] **Exempel:** PR #90 Login (Zaida, merged 2026-09-10, links to #40, 4 commits)
- [ ] **Exempel:** PR #95 Design System (Björn, merged 2026-09-10, 15 commits)
- [ ] **VIKTIGT:** Fokus är ARBETE (commits + PRs), INTE issue-status
- [ ] Om issue är stängt men PRn är mergad → visa arbetet
- [ ] Om issue är öppet men PR är mergad → visa arbetet (den fortsätter)

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
- [ ] **Exempel:** Tomac: #43 API-klient PR (3 commits denna vecka, under review)
- [ ] **Exempel:** Marco: feature/#45-risk PR (5 commits denna vecka, ongoing)
- [ ] **Exempel:** Anna: feature/#52-tests (2 commits denna vecka, not yet in PR)
- [ ] **VIKTIGT:** Visa arbete från:
  * Open PRs (under review)
  * Feature branches med commits (even without PR)
  * NOT comments — activation = commits, PR-updates, branch pushes

### 4. OPEN ISSUES MED AKTIVITET DENNA VECKA
- [ ] Läst GitHub Issues API/Web för issues **öppna med aktivitet denna vecka**
- [ ] Aktivitet = commits eller PR-updates, INTE bara kommentarer
- [ ] **Exempel:** #43 API Client (Tomac, 3 commits denna vecka)

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

**DENNA CHECKLIST ÄR OBLIGATORISK.**

Om du hoppar över den kommer du att dölja arbete som login, designsystem och annat stängd arbete.

---

**Senast uppdaterad:** 2026-09-13
