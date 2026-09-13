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

### 1. CLOSED ISSUES DENNA VECKA
- [ ] Läst GitHub Issues API/Web för issues **stängda denna vecka**
- [ ] Issue-listan innehåller: assignee, titel, stäng-datum, möjlig PR
- [ ] **Exempel:** #40 Login Page (Zaida, stängd 2026-09-10)
- [ ] **Exempel:** #44 Design System (Björn, stängd 2026-09-10)

### 2. MERGED PRs DENNA VECKA
- [ ] Läst GitHub PRs API/Web för PRs **mergade denna vecka**
- [ ] PR-listan innehåller: nummer, titel, author, merge-datum, linked issue
- [ ] **Exempel:** PR #90 Login (Zaida, merged 2026-09-10, links to #40)
- [ ] **Exempel:** PR #91 Design System (Björn, merged 2026-09-10, links to #44)

### 3. COMMITS DENNA VECKA
- [ ] Läst GitHub Commits API/Web för **commits på develop denna vecka**
- [ ] Commit-listan innehåller: hash, author, message, date
- [ ] Commits är grupperade per issue/arbetsområde (ej enskilda commits på slide)
- [ ] **Exempel:** 4 commits från Zaida på login-arbete → "Frontend & Auth"

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
