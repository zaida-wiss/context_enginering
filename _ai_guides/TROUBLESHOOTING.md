---
name: troubleshooting
description: Common presentation problems and how to fix them
metadata:
  type: reference
  audience: anyone using presentations
---

# 🔧 TROUBLESHOOTING — When Presentations Go Wrong

**Något ser fel ut i presentationen? Hitta ditt problem här.**

🔗 **Alla externa datakällor:** Se [`_memory/EXTERNAL_SOURCES.md`](../_memory/EXTERNAL_SOURCES.md) för centraliserad register över Google Sheets, Google Docs, GitHub och alla fallback-URLs.

---

## PROBLEM 1: Vissa Team-Medlemmar Saknas

### Symptom
"En teammedlem är inte med på sliden, men han hade arbete denna vecka"

### Checklista

- [ ] **Läs TEAM_ROSTER.md** — Är Jan i rätt team?
  - Frontend: Tomac, Björn, Zaida
  - Backend: Erik, Rasha
  - Native: Pär, Henrik

- [ ] **Kollade GitHub denna vecka?** — Hade denna medlem faktisk aktivitet (commits/PR)?
  - Bara issue-kommentarer räknas INTE som aktivitet
  - PR updates räknas
  - Commits räknas

- [ ] **Är det en ny person?** — Uppdatera TEAM_ROSTER.md
  - Lägg till person + GitHub username
  - Uppdatera team-tillhörighet
  - Commit + push

- [ ] **Är personen på verifierings-sliden?** ("Alla i teamet")
  - Om "Ingen aktivitet" syns → det är OK att personen saknas från övriga slides
  - Om personen helt saknas → kontrollera TEAM_ROSTER

### Lösning

1. Verifiera i GitHub: `https://github.com/chas-challenge-2026/avanza-team1`
2. Om personen HAD aktivitet: kontrollera DATA_COLLECTION_MANDATORY.md — fullföldes steg 1-3?
3. Om person är NY: uppdatera TEAM_ROSTER.md
4. Generera presentationen igen

---

## PROBLEM 2: PR-Antal Stämmer Inte

### Symptom
"Sliderna visar 5 PRs men GitHub visar 8"

### Checklista

- [ ] **Kollade rätt tidsperiod?** — Denna vecka (senaste 7 dagar)?
  - Inte förra veckan
  - Inte hela månaden

- [ ] **Filtrerades fel PRs?** — Är detta MERGED PRs?
  - Draft PRs räknas INTE
  - Closed but not merged räknas INTE
  - Endast status "merged" räknas

- [ ] **Kollade alla branches?** — Är du på develop?
  - PRs kan mergea till main eller develop
  - Kontrollera BÅDA branches

- [ ] **Data-insamling komplett?** — Läs DATA_COLLECTION_MANDATORY.md avsnitt 1
  - Gick genom GitHub API eller web?
  - Fallback-hierarki försökt?

### Lösning

1. Manuell count på GitHub
2. Jämför med presentation
3. Om skillnad > 1: kontrollera DATA_COLLECTION_MANDATORY.md igen
4. Om fortfarande fel: uppdatera presentation

---

## PROBLEM 3: DoD-Status Verkar Fel

### Symptom
"Issue visar ✓ för Tests men det finns ingen test PR"

### Checklista

- [ ] **Läst issue-meddelandet?** — DoD-status måste vara i issue-description
  - Inte från Project Board status
  - Inte från assignee
  - Läs issue-body direkt på GitHub

- [ ] **Är det rätt issue?** — Kontrollera issue-nummer
  - Copy-paste från GitHub för att undvika fel

- [ ] **Är DoD uppdaterad denna vecka?** — Kan ha ändrats sedan presentation skapades
  - Uppdaterad issue = uppdaterad DoD
  - Presentation läste bara vid datainsamlingstillfället

### Lösning

1. Öppna GitHub issue direkt
2. Läs DoD-sektionen i issue-body
3. Om det är fel: uppdatera issue + regenerera presentation
4. Om det är rätt: DoD-status på sliden är korrekt

---

## PROBLEM 4: Blockers/Risker Saknas

### Symptom
"Vi vet om en blocker som inte står på sliden"

### Checklista

- [ ] **Är det dokumenterat?** — Blockers måste vara:
  - Gitissues med label "blocked" eller "waiting", ELLER
  - PR-kommentarer som nämner beroendet, ELLER
  - Mötesprotokollet från denna veckan

- [ ] **Kontrollerades vid datainsamling?** — Se punkt ⑥ i DATA_COLLECTION_MANDATORY.md
  - GitHub issues granskade?
  - PRs granskade?
  - Mötesprotokollet läst?

- [ ] **Är det en NEW blocker denna vecka?** — Eller från förra veckan?
  - Presentationen läser bara denna vecka's data

### Lösning

1. Dokumentera på GitHub (issue eller PR-kommentar)
2. Återkör datainsamling (DATA_COLLECTION_MANDATORY.md)
3. Regenerera presentation

---

## PROBLEM 5: Presentation Är Tom eller Saknar Slides

### Symptom
"Slide ① visar nästan ingenting" eller "Punkt ③ saknas helt"

### Checklista

- [ ] **Kördes DATA_COLLECTION_MANDATORY.md?** — All data måste samlas in FÖRE rendering
  - Se avsnitt "PHASE 1 — DATA COLLECTION"
  - Alla steg måste checkades OFF

- [ ] **Fallback-hierarkin försökt?** — Om GitHub failade:
  - Google Sheets: See EXTERNAL_SOURCES.yaml: GOOGLE_PROJECT_DATA_SHEET
  - Project Board: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
  - Meeting protocol (länk i README.md)

- [ ] **Team-medlemmar verifierade?** — Se TEAM_ROSTER.md
  - Är alla 7 medlemmar i listan?
  - Kontrollerades alla för aktivitet?

- [ ] **Denna vecka eller förra veckan?** — Data-filtret måste vara rätt
  - Senaste 7 dagar (Monday-Sunday)
  - INTE förra veckan

### Lösning

1. Läs DATA_COLLECTION_MANDATORY.md igen
2. Gå genom checklist punkt för punkt
3. Försök alla fallback-källor
4. Regenerera presentation

---

## PROBLEM 6: Färger Verkar Fel

### Symptom
"Status är 🟢 grön men det är inte klart" eller "Allt är 🔴 rött"

### Checklista

- [ ] **Förstod färg-semantiken?** — Läs PRESENTATION_STYLE.md
  - 🟢 = faktiskt KLART (merged + DoD verifierat)
  - 🟡 = PÅGÅR (commits denna vecka, men inte merged)
  - 🔴 = BLOCKERAT eller KRITISKT
  - ⚪ = INGEN AKTIVITET

- [ ] **Är det issue-state eller DoD?** — Två olika saker
  - Issue kan vara "Closed" men DoD inte slutförord
  - Presentation visar DoD-status från issue-meddelandet

- [ ] **Uppdaterad issue-DoD?** — Presentationen läser DoD vid datainsamlingstillfället
  - Om DoD ändrades senare: uppdatering syns i nästa presentation

### Lösning

1. Läs issue-meddelandet direkt på GitHub
2. Kontrollera DoD-sektionen
3. Färgen på sliden ska matcha faktisk DoD-status
4. Om presentation är fel: DATA_COLLECTION_MANDATORY.md igen

---

## PROBLEM 7: Slide Visar Fel Namn eller Data

### Symptom
"Zaida är inte assignee på det här men sliden säger hon är"

### Checklista

- [ ] **Är det GitHub-data eller presentation-data?** — Verifiera på GitHub direkt
  - GitHub är sanningen
  - Presentationen läste vid datainsamlingstillfället

- [ ] **Ändrades issue EFTER presentation skapades?** — Om assignee ändrades:
  - Presentation visar gammal data
  - Regenerera för att få ny data

- [ ] **Är data-källan rätt?** — Se DATA_SOURCES.md
  - GitHub Web eller API (primär)
  - Google Sheets fallback
  - Inte mänskliga tankar eller minnen

### Lösning

1. Verifiera på GitHub
2. Om GitHub och presentation skiljer: uppdatera GitHub först
3. Regenerera presentation från GitHub-data

---

## PROBLEM 8: Punkt ① Visar Inte Alla PRs

### Symptom
"Vi hade 10 PRs denna vecka men sliden visar bara 5"

### Checklista

- [ ] **MÅSTE alla PRs synas?** — Se punkt ①-regel:
  - "ALLA PRs denna vecka, inget får utelämnas för plats"
  - Om många PRs: dela på fler slides (①A.1, ①A.2, ①A.3)

- [ ] **Var är övriga PRs?** — Kollade alla tre team-slides?
  - ①A Frontend PRs
  - ①B Backend PRs
  - ①C Native PRs

- [ ] **Är det merged PRs?** — Bara merged till develop räknas
  - Draft PRs räknas INTE
  - Open PRs räknas INTE
  - Endast merged

### Lösning

1. Gå igenom ALLA punkt ①-slides (A, B, C)
2. Räkna total — ska matcha GitHub count
3. Om några saknas: kontrollera DATA_COLLECTION_MANDATORY.md punkt 1

---

## PROBLEM 9: Mötesledaren Förstår Inte Sprintmålet

### Symptom
"Vad är sprintmålet denna vecka?" — och sliden är tom eller generell

### Checklista

- [ ] **Är punkt ⑪ komplett?** — Målet måste ha:
  - Kortfattad text: "Vid slutet av veckan ska [X] fungera"
  - Success criteria: konkreta, verifierbara resultat
  - Koppling till slutleverans-deadline

- [ ] **Är målet realistisk?** — Se punkt ⑫ (planeringskontroll)
  - 🟢 Rimlig, 🟡 Tight, eller 🔴 Ej realistisk
  - Om rött: målet måste justeras

- [ ] **Är det från förra veckan?** — Målet ska vara NYTT denna vecka
  - Baserat på kapacitet + prioritering
  - Inte samma som förra veckan

### Lösning

1. Läs punkt ⑫A (planeringskontroll)
2. Om målet är 🔴 rött: justera scope
3. Regenerera presentation med nytt mål

---

## PROBLEM 10: "Vem Gör Vad?" Är Inte Klart

### Symptom
"Jag vet inte vad jag ska göra denna vecka"

### Checklista

- [ ] **Läs punkt ③-⑤ slide B** — "Vad behöver vi göra?"
  - "Nästa arbete" visar vad du gör FÖRST
  - "Vi väntar på" visar vad som blockerar dig
  - "Kan göras utan beroendet" visar fallback-arbete

- [ ] **Läs punkt ⑫** — Sprint plan
  - Varje person bör ha ett nummer och issue

- [ ] **Läs punkt ⑬** — Actions
  - Konkreta GitHub-åtgärder efter mötet
  - Din namn → ditt ansvar

### Lösning

1. Slå upp ditt namn på slide
2. Läs rad för rad vad du ska göra
3. Om oklart: fråga mötesledaren UNDER mötet
4. Efter mötet: GitHub-actions ska uppdateras (punkt ⑬)

---

## "JAG HITTAR INTE NÅGOT"

**Om inget av ovan löser det:**

1. **Läs ROOT README.md** — Start-punkten
   - `_ai_guides/presentations/MANDATORY_READING_ORDER.md` är läsordningen

2. **Läs MANDATORY_READING_ORDER.md** — Exakt sekvens för denna vecka
   - Fase 1-5 måste följas

3. **Läs DATA_COLLECTION_MANDATORY.md** — Var kom data från?
   - Avsnitt 1-6 måste alla kompletterade

4. **Kontakta AI-förbindelseperson** — Om fortfarande oklart
   - "Jag följde alla steg men X är fortfarande fel"

---

## Snabb Referens — Vanligaste Problem

| Problem | Lösning |
|---------|---------|
| Person saknas | Kolla TEAM_ROSTER, kontrollera GitHub |
| PR-antal stämmer inte | Räkna PRs på GitHub denna vecka |
| DoD ser fel ut | Läs issue-description på GitHub |
| Tom presentation | Körde DATA_COLLECTION_MANDATORY? |
| Färger verkar fel | Läs DoD från GitHub, kontrollera PRESENTATION_STYLE |
| Vad gör jag? | Läs punkt ③-⑤ slide B, kolumn "Nästa arbete" |

---

**Senast uppdaterad:** 2026-09-13
