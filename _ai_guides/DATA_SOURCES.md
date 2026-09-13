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
1. GitHub Connector/API — issues & PRs med closed-date denna vecka
2. GitHub /issues tab → filter "closed:2026-09-08..2026-09-14"
3. GitHub /pulls tab → filter "merged:2026-09-08..2026-09-14"
4. Projekt-board status (se PROJECT BOARD)
5. Mötesprotokoll från denna vecka — vad sade vi var klart?

**Om all misslyckas:** Presentationen kan säga "saknad verifiering av denna veckas avslutade arbete" men INTE "Git log kunde inte läsas"

---

### 2. WORK IN PROGRESS

**Behövs för:** Visa vad som pågår och vem som jobbar

**Fakta:** Vilka issues är öppna? Vilka PRs är under review? Vem är assignad?

**Primär källa:**
- GitHub Issues med status "open" + assignee

**Fallback ordning:**
1. GitHub Connector/API — open issues + PR list
2. GitHub /issues tab
3. GitHub /pulls tab
4. Projekt-board "In Progress"-kolumn
5. Mötesprotokoll från denna vecka

**Viktigt:** Vi behöver name + issue-number för varje person

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
3. Merged PRs (se WORK COMPLETED) — de visar commits utan att behöva log
4. Mötesprotokoll — vad sade vi implementerade?

**VIKTIGT:** Git-kloning är ALDRIG ett krav för commit-historik. Det behövs inte för statusrapportering.

---

### 5. PROJECT BOARD STATUS

**Behövs för:** Kolumn-vy av arbete (backlog, ready, in progress, review, done)

**Fakta:** Vilka issues är i vilken kolumn?

**Primär källa:**
- GitHub Projects/Board via Connector/API eller webben

**Fallback ordning:**
1. GitHub Connector/API — Project status om tillgänglig
2. GitHub Project-webben (https://github.com/chas-challenge-2026/avanza-team1/projects/XX)
3. GitHub Issues-vyn — filtrera på labels som motsvarar kolumner
4. Dra slutsatser från issue-status + PR-status
5. Mötesprotokoll från denna vecka

**Om board misslyckas:** Presentationen kan säga "Project Board kunde inte läsas direkt; status är baserad på issues + PRs"

---

### 6. MEETING PROTOCOL / DECISIONS

**Behövs för:** Vad sade vi att vi skulle göra?

**Fakta:** Tidigare beslut, frågor till ledning, anteckningar

**Primär källa:**
- Google Docs-protokoll (veckan-X.txt eller motsvarande länk)

**Fallback ordning:**
1. Google Drive Connector — om autentiserad
2. Public shared Google Docs → TXT-export
3. Cached snapshot i context_enginering (_memory/PROTOCOL_SNAPSHOT.md)
4. Lösen från presentation-begäran — använd det som angavs

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

```
URL: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
PROJECT ID: 31
Status: Öppen för alla att läsa (ingen auth behövs)
AI kan läsa: Ja, direkt från länken
```

AI läser denna länk direkt för presentationen. Ingen snapshot-process behövs.

### Meeting Protocol

```
URL: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit
Status: Öppen för alla att läsa (ingen auth behövs)
AI kan läsa: Ja, direkt från länken
```

AI läser denna länk direkt för presentationen. Ingen snapshot-process behövs.

### Fallback Snapshot Files (when live sources fail)
```
Commits/Branches/Issues/PRs: _memory/GITHUB_SNAPSHOT.md
Project Board: _memory/PROJECT_BOARD_SNAPSHOT.md
Meeting Protocol: _memory/PROTOCOL_SNAPSHOT.md
```

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

