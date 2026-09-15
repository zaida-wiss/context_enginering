---
name: data_sources
description: Canonical information needs and fallback access strategies for presentations
metadata:
  type: reference
  updated: 2026-09-14
---

# 📊 DATA SOURCES — Where to Find Information

**Authority:**
- **[`SYSTEM_CONTRACT.yaml`](../SYSTEM_CONTRACT.yaml)**: Definierar vilken information som KRÄVS och NÄR det ska stoppa
- **DATA_SOURCES.md** (denna fil): Definierar VAR informationen kan hämtas och fallback-ordningen

**This file does NOT decide whether information is required or whether rendering stops.**

🔗 **NOTE:** Alla externa URLs (Google Sheets, Google Docs, GitHub) är centraliserade i [`_memory/EXTERNAL_SOURCES.md`](../../../_memory/EXTERNAL_SOURCES.md). Se den filen för aktuella IDs och fallback-URLs.

---

## PRINCIPLE: Source Priority > Specific Technology

Målet är att hitta **verifierad information**, inte att en **specifik URL/API** fungerar.

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
1. **GitHub Issues API** — alla closed issues (REPORTING_PERIOD_START → REPORTING_PERIOD_END)
   - Filter: Exkludera labels "test", "duplicate", "wontfix", "archived"
   - Include: issues + linked PRs

2. **GitHub web: Issues tab**
   - URL: `https://github.com/chas-challenge-2026/avanza-team1/issues?q=is:closed`
   - Then filter results by REPORTING_PERIOD manually if date-filter fails

3. **GitHub web: Pulls tab (merged)**
   - URL: `https://github.com/chas-challenge-2026/avanza-team1/pulls?q=is:merged`
   - Use @today-1w syntax: `https://github.com/chas-challenge-2026/avanza-team1/pulls?q=merged%3A%3E%40today-1w`

4. **GitHub API (JSON)**
   - URL: `https://api.github.com/repos/chas-challenge-2026/avanza-team1/pulls?state=closed&per_page=100`
   - Filter results: merged_at ≠ null AND merged_at within REPORTING_PERIOD

5. **Raw GitHub URLs (if web fails)**
   - Commits: `https://raw.githubusercontent.com/chas-challenge-2026/avanza-team1/develop/...`
   - Individual PRs: Parse from GitHub web directly

6. **Individual PR detail pages**
   - URL: `https://github.com/chas-challenge-2026/avanza-team1/pull/[PR_NUMBER]`
   - Returns: Title, author, approver, merge-date, linked issues, commits

7. **Google Sheets fallback**
   - URL: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/
   - Use if: All GitHub methods fail
   - Filter: Exclude test-issues (same as GitHub rules)

8. **Project Board (reconstruction only)**
   - Use ONLY if issues/PRs data unavailable
   - May be incomplete; Issues list is more authoritative

9. **Meeting Protocol (context only)**
   - Use for verification context, never as primary source

**REPORTING_PERIOD standard:** Previous Monday 00:00 → Current Monday 00:00 (exclusive), Europe/Stockholm timezone

**If GitHub completely unavailable:** Use Sheets + Protocol; mark sources in presentation footer with ⚠️

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

### OPTIONAL ENRICHMENT: COMMIT HISTORY

**Status:** Optional (SYSTEM_CONTRACT.yaml lists as optional_enrichment)

**If available:** Provides timeline detail for already-verified delivery (from merged PRs)

**If unavailable:** Rendering continues; commit detail omitted from presentation

**Sources (for reference):**
1. GitHub Connector/API — commits to develop within REPORTING_PERIOD
2. GitHub /commits tab — filter by date
3. Google Sheets: https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/
4. Merged PRs metadata (already in required data)

**Note:** Commits are derived from merged PR data; endpoint failure is never a STOP condition.

---

### OPTIONAL ENRICHMENT: PROJECT BOARD STATUS

**Status:** Optional (SYSTEM_CONTRACT.yaml lists as optional_enrichment)

**If available:** Provides column-view for cross-verification of issue workflow

**If unavailable:** Rendering continues; reconstruct from issue-status + PR-status

**Sources (for reference):**
1. GitHub Project: https://github.com/orgs/chas-challenge-2026/projects/31/views/1
2. GitHub REST API /repos/issues med project-filter
3. Reconstruct from GitHub Issues view (labels as column mapping)

**Note:** Board is verification-only; can always be reconstructed from required data sources.

---

### OPTIONAL ENRICHMENT: MEETING PROTOCOL / DECISIONS

**Status:** Optional (SYSTEM_CONTRACT.yaml lists as optional_enrichment)

**If available:** Provides context for decisions and action items

**If unavailable:** Rendering continues; presentation uses GitHub data as primary source

**Sources (for reference):**
1. Google Docs: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/
2. TXT-export (?format=txt)
3. HTML-export (?format=html)
4. PDF-export (?format=pdf)

**Note:** Context only; never required for rendering. GitHub data sufficient if unavailable.

---

## ⚠️ FORBIDDEN SOURCES — NEVER USE THESE

**AI skal ALDRIG sök på dessa sources för Avanza-data:**

- ❌ Google/Bing/DuckDuckGo (web search)
- ❌ GitHub Search API (`api.github.com/search`)
- ❌ Stack Overflow, Reddit, eller community-forums
- ❌ Blockchain explorers (blockstream.info, etherscan.io, tronscan.org)
- ❌ Cryptocurrency exchanges (banxa.com, 1inch.com, bitref.com)
- ❌ Stock exchanges (live.deutsche-boerse.de, etc.)
- ❌ Finance/trading data sites
- ❌ AI "knowledge cutoff" eller modellens eget kunnande för faktiska Avanza-data
- ❌ Generella API-aggregatorer eller scrape-services

**WHY:** Dessa sources kan innehålla FELAKTIG eller VILSELEDANDE data om Avanza-projektet. Enda källan för Avanza-faktum är GitHub + Google Docs/Sheets.

**IF YOU SEARCH THESE SOURCES:** Presentationen MISSLYCKADES. Du sökte utanför tillåtna sources.

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

**OM GitHub web/API failar → använd denna sheet för ALL data:**

```
🔗 FALLBACK URL (primary):
   https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/

✅ Denna sheet innehåller fallback-data för:
   - Commits denna vecka (primär fallback för commit-historik)
   - Issues (öppna, stängda, assignees)
   - PRs (öppna, mergade, linked issues)
   - Project Board status
   - Mötesprotokollet (om tillgängligt)
   - Merged PRs in develop (för punkt ①)

📊 Status: Accessible, multiple sheets for different data types
🤖 AI can read: Yes, via direct link or CSV export
```

**USAGE:**
1. GitHub live-sources ALWAYS tried first (web, API, Connector)
2. If GitHub fails → use this Sheets URL as fallback
3. If this sheet fails → use meeting protocol or manual entry
4. Denna sheet är sista fallback innan presentationen säger "ej verifierat"

**EXPORT FOR AI READING:**
If direct access fails, download as:
- CSV: `https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/export?format=csv`
- Excel: `https://docs.google.com/spreadsheets/d/1TECz-PkbJhK6Jux6tpjcXDNvUNUZGI_nnIDE5rKr5UI/export?format=xlsx`

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

