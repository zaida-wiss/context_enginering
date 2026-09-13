---
name: data_sources
description: Canonical information needs and fallback access strategies for presentations
metadata:
  type: reference
  updated: 2026-09-13
---

# 📊 DATA SOURCES — Information Needs & Fallback Strategy

**Denna fil definierar vilken information som behövs, inte vilka tekniska metoder som MÅSTE användas.**

---

## PRINCIPLE: Information > Technology

Målet är att presentationen innehåller **verifierade fakta**, inte att en **specifik URL-metod** fungerar.

Exempel:

❌ **Dåligt tänk:**
"Git log behövs → GitHub API måste fungera → om API failar är presentationen ofullständig"

✅ **Bra tänk:**
"Vi behöver verifierad commit-historik → försök GitHub API → försök GitHub-webben → försök PR-historik → använd bästa verifierbar källa"

---

## INFORMATION NEEDED FOR STATUS

Presentationen måste kunna verifiera dessa fakta:

### 1. WORK COMPLETED THIS WEEK

**Behövs för:** Visa vad som är klart

**Fakta:** Vilka issues/PRs är merged/closed denna vecka?

**Primär källa:**
- GitHub Issues/PRs med status "done" eller "closed" + merge-datum denna vecka

**Fallback ordning:**
1. **GitHub Issues API** — alla closed issues denna vecka
   - FILTER: Exkludera labels "test", "duplicate", "wontfix", "archived"
   - Inklud: både issues och linked PRs
   
2. **GitHub /issues tab** → filter "closed:2026-09-08..2026-09-14"
   - FILTER: Samma som ovan (exkludera test-issues)
   
3. **GitHub /pulls tab** → filter "merged:2026-09-08..2026-09-14"
   - Linked issues automatiskt inclusion
   
4. **Google Sheets fallback** — https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/
   - CSV export eller manual entry
   - FILTER: Samma som GitHub (exkludera test-issues)
   
5. **Projekt-board "Done"-kolumn** (se PROJECT BOARD)
   - Risk: kan missa issues som INTE är på board
   - Använd endast om alla andra failar
   
6. **Mötesprotokoll från denna vecka** — vad sade vi var klart?
   - Fältdata, kan missa issues från veckan

**Om all misslyckas:** Presentationen kan säga "saknad verifiering av denna veckas avslutade arbete" men INTE "Git log kunde inte läsas"

**VIKTIGT:** GitHub Issues är mer komplett än Project Board (inte alla issues synkas till board). Ignorera ALDRIG issues bara för att de saknas från board.

---

### 2. WORK IN PROGRESS

**Behövs för:** Visa vad som pågår och vem som jobbar

**Fakta:** Vilka issues är öppna? Vilka PRs är under review? Vem är assignad?

**Primär källa:**
- GitHub Issues med status "open" + activity denna vecka (commits, PR updates)

**Fallback ordning:**
1. **GitHub Issues API** — open issues + activity denna vecka
   - FILTER: Exkludera "test", "duplicate", "wontfix"
   - Kräv: commits eller PR-updates (NOT bara issue-comments)
   
2. **GitHub /issues tab** — filter "is:open"
   - FILTER: Samma som ovan
   
3. **GitHub /pulls tab** — open PRs
   - Linked issues automatiskt inclusion
   
4. **Google Sheets fallback** — samma URL som ovan
   - För open items med aktivitet
   
5. **Projekt-board "In Progress"-kolumn**
   - Risk: kan missa open issues som INTE är på board
   
6. **Mötesprotokoll från denna vecka**

**Viktigt:** Vi behöver name + issue-number för varje person

**RULE:** Om issue är öppen men SAKNAS från Project Board — det är FORTFARANDE aktuellt arbete och måste visas.

---

### 3. BLOCKERS / DEPENDENCIES

**Behövs för:** Visa vad som väntar på vad

**Fakta:** Vilka issues blockerar andra? Vilka väntar på externa input?

**Primär källa:**
- GitHub Issues med labels "blocked", "waiting", "dependency"
- PR-kommentarer som visar "waiting for #XX"

**Fallback ordning:**
1. GitHub Issues — labels eller description mentioning blocks
2. GitHub PRs — comments mentioning dependencies
3. Mötesprotokoll från denna vecka
4. Team-beskrivningar från mötet

---

### 4. COMMIT HISTORY

**Behövs för:** "Vi har gjort följande denna vecka"

**Fakta:** Vilka ändringar har gjorts i develop/main sedan förra möte?

**Primär källa:**
- GitHub Connector/API — commits to develop since last Tuesday

**Fallback ordning:**
1. GitHub Connector/API — commits to develop + date range
2. GitHub /commits tab — filter by date
3. Google Sheets (universal fallback): https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/
4. Merged PRs (se WORK COMPLETED) — de visar commits utan att behöva log
5. Mötesprotokoll — vad sade vi implementerade?

**VIKTIGT:** Git-kloning är ALDRIG ett krav för commit-historik. Det behövs inte för statusrapportering.

---

### 5. PROJECT BOARD STATUS

**Behövs för:** Kolumn-vy av arbete (backlog, ready, in progress, review, done)

**Fakta:** Vilka issues är i vilken kolumn?

**Primär källa:**
- GitHub Projects/Board via Connector/API eller webben

**Fallback ordning:**
1. GitHub Connector/API — Projects API v4
2. GitHub Project-webben (https://github.com/orgs/chas-challenge-2026/projects/31/views/1)
3. GitHub REST API /repos/issues med project-filter
4. GitHub Issues-vyn — filtrera på labels som motsvarar kolumner
5. Dra slutsatser från issue-status + PR-status
6. Mötesprotokoll från denna vecka

**Om board misslyckas:** Presentationen kan säga "Project Board kunde inte läsas direkt; status är baserad på issues + PRs"

---

### 6. MEETING PROTOCOL / DECISIONS

**Behövs för:** Vad sade vi att vi skulle göra?

**Fakta:** Tidigare beslut, frågor till ledning, anteckningar

**Primär källa:**
- Google Docs-protokoll (veckan-X.txt eller motsvarande länk)

**Fallback ordning:**
1. Google Drive Connector — om autentiserad
2. Google Docs länk — läs direkt från webben
3. TXT-export (?format=txt) — raw text
4. HTML-export (?format=html) — strukturerad text
5. PDF-export (?format=pdf) — om övriga misslyckas
6. GitHub-data om protocol misslyckas totalt

**Om all misslyckas:** Presentationen bygger på GitHub-data men noterar "mötesprotokoll kunde inte verifieras"

---

## FAILURE HANDLING

### ❌ TEKNISKA FEL HÖRS ALDRIG I PRESENTATIONEN

Dessa ord får ALDRIG stå på slides:

- "Google Docs fetch-error"
- "Git log kunde inte verifieras"
- "Project Board är inte åtkomlig"
- "GitHub API returnerade 403"
- "Connector failed"

### ✅ I STÄLLET: Använd nästa fallback

Om en källa misslyckas:
1. Prova nästa i fallback-ordningen
2. Om flera misslyckas, använd den bästa som fungerade
3. Om ingen fungerar, säg **vad informationen är** och **varför den behövs**, inte **tekniska orsaker**

### ✅ EXEMPEL PÅ RÄTT FELHANTERING

❌ Dåligt:
"Google Docs TXT-export kunde inte läsas denna gång"

✅ Bra:
"Status denna vecka baseras på GitHub issues och PRs; mötesprotokoll kunde inte verifieras"

✅ Bättre:
"Lisa är assignad #40 (verifiera från GitHub); hennes uppdaterade handlingar från mötet kunde inte verifieras från protokoll"

---

## UNIVERSAL FALLBACK — Google Sheets

**Om multiple live-sources failar, denna sheet innehåller fallback-data för:**
- Commits denna vecka
- Issues (öppna, stängda, assignees)
- PRs (öppna, mergade)
- Project Board status
- Mötesprotokollet

```
URL: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/
Status: Accessible, multiple sheets for different data types
AI can read: Yes, via direct link or export
```

**Denna sheet är sista fallback innan presentationen säger "ej verifierat".**

---

## CANONICAL URLS — DETERMINISTIC DATA SOURCES

### GitHub Repository
```
https://github.com/chas-challenge-2026/avanza-team1
```

### GitHub Branches (develop + active)
```
https://github.com/chas-challenge-2026/avanza-team1/branches
API: https://api.github.com/repos/chas-challenge-2026/avanza-team1/branches
```

### GitHub Commits (develop branch — THIS WEEK)
```
WEB: https://github.com/chas-challenge-2026/avanza-team1/commits/develop
API: https://api.github.com/repos/chas-challenge-2026/avanza-team1/commits?sha=develop&since=[MONDAY]&until=[NOW]
```

### GitHub Issues (open + closed this week)
```
WEB: https://github.com/chas-challenge-2026/avanza-team1/issues
API: https://api.github.com/repos/chas-challenge-2026/avanza-team1/issues?state=all&since=[MONDAY]
```

### GitHub Pull Requests (open + merged this week)
```
WEB: https://github.com/chas-challenge-2026/avanza-team1/pulls
API: https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?state=all&since=[MONDAY]
```

### GitHub Project Board

**Primär källa:**
```
URL: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
Status: Öppen för alla att läsa (ingen auth behövs)
```

**Fallback metoder:**
1. GitHub Connector/API — Projects API v4
2. Vanlig GitHub web-länk (ovan)
3. GitHub REST API — /repos/{owner}/{repo}/issues med project-filter
4. GitHub Issues view med kolumn-labels som mapping

### Meeting Protocol

**Primär källa:**
```
URL: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit
Status: Öppen för alla att läsa (ingen auth behövs)
```

**Fallback metoder:**
1. Google Drive Connector (om autentiserad)
2. Vanlig Google Docs länk (ovan)
3. Raw-export: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=txt
4. PDF-export: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=pdf
5. HTML-export: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/export?format=html

---

## SUMMARY: WHAT GOES WRONG & HOW TO FIX IT

| Problem | Root Cause | Solution |
|---------|-----------|----------|
| "Git log could not be verified" on slides | AI tried one method, it failed, gave up | Try multiple methods; GitHub Issues/PRs = backup for commit-history |
| "Project Board not accessible" | API failed; AI assumed Board was THE source | Board is source 3; issues/PRs are sources 1-2 |
| "Google Docs fetch failed" message appears in presentation | Technical error shown to team | Use fallback protocol or build from issues; NEVER show fetch errors |
| Presentation stops because one source failed | Single-source dependency | All information needs have 3+ fallback sources |

---

## FOR AI PRESENTATION BUILDERS

When README or PRESENTATION_SPEC mentions "Git log, Project Board, meeting protocol":

1. Map to THIS document first
2. Read the "INFORMATION NEEDED" section
3. Use the fallback order
4. If a method fails, try the next automatically
5. NEVER report technical fetch failures in the presentation
6. Combine information from multiple sources if needed

