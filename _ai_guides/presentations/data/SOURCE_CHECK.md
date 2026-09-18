---
name: source_check
description: Mandatory source verification checklist — must be completed before presentation delivery
metadata:
  type: process
  updated: 2026-09-13
---

# ✅ SOURCE CHECK — Obligatorisk Källverifiering

**DENNA CHECKLIST MÅSTE FYLLASPORRE PRESENTATION KAN ANSES FÄRDIG**

---

## 📋 Presentation Delivery Gate

**Presentation får INTE levereras förrän:**

- [ ] Denna SOURCE_CHECK har skapats
- [ ] Alla obligatoriska källor har försökts läsas
- [ ] Varje källa har status: ✅ LÄST / ⚠️ FALLBACK / ❌ MISSLYCKAD
- [ ] `checked_at` innehåller datum + tidspunkt + tidszon
- [ ] Samma käll-status visas på presentationens första slide
- [ ] Samma käll-status redovisas i chattsvaret när presentationen levereras

---

## 📊 Obligatoriska Källor

### CONTEXT-REPO SOURCES

- [ ] **Context README.md**
  - URL: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/README.md
  - Status: ✅ / ⚠️ / ❌
  - Fallback: N/A (lokalt känd)

- [ ] **PRESENTATION_SPEC.md**
  - URL: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/content/PRESENTATION_SPEC.md
  - Status: ✅ / ⚠️ / ❌
  - Fallback: N/A (lokalt känd)

- [ ] **DESIGN_AUTHORITY.md**
  - URL: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/design/DESIGN_AUTHORITY.md
  - Status: ✅ / ⚠️ / ❌
  - Fallback: N/A (lokalt känd)

- [ ] **PRESENTATION_STYLE.md**
  - URL: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/design/PRESENTATION_STYLE.md
  - Status: ✅ / ⚠️ / ❌
  - Fallback: N/A (lokalt känd)

- [ ] **PRESENTATION_STRUCTURE.md**
  - URL: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/monday_meeting/structure/PRESENTATION_STRUCTURE.md
  - Status: ✅ / ⚠️ / ❌
  - Fallback: N/A (lokalt känt)

- [ ] **WEEKLY_PROGRESS_MODEL.md**
  - URL: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/models/WEEKLY_PROGRESS_MODEL.md
  - Status: ✅ / ⚠️ / ❌
  - Fallback: N/A (lokalt känd)

- [ ] **DATA_SOURCES.md**
  - URL: https://raw.githubusercontent.com/zaida-wiss/context_enginering/main/_ai_guides/presentations/data/DATA_SOURCES.md
  - Status: ✅ / ⚠️ / ❌
  - Fallback: N/A (lokalt känd)

### PROJECT GITHUB SOURCES

- [ ] **GitHub Merged PRs (develop branch)**
  - Source: GITHUB_MERGED_PRS per EXTERNAL_SOURCES.yaml
  - Status: ✅ / ⚠️ / ❌
  - Primary: GitHub REST API
  - Fallback chain: Google Sheets (if fresh) → GitHub web
  - Reporting period: Last 7 calendar days

- [ ] **GitHub Open Issues**
  - Source: GITHUB_OPEN_ISSUES per EXTERNAL_SOURCES.yaml
  - Status: ✅ / ⚠️ / ❌
  - Primary: GitHub REST API
  - Fallback chain: Google Sheets (if fresh) → GitHub web
  - Reporting period: Last 7 calendar days with activity

- [ ] **GitHub Issues (open)**
  - URL: https://github.com/chas-challenge-2026/avanza-team1/issues
  - Status: ✅ / ⚠️ / ❌
  - Access method: GitHub Connector / Web
  - Fallback: GITHUB_SNAPSHOT.md

- [ ] **GitHub Pull Requests (open)**
  - URL: https://github.com/chas-challenge-2026/avanza-team1/pulls
  - Status: ✅ / ⚠️ / ❌
  - Access method: GitHub Connector / Web
  - Fallback: GITHUB_SNAPSHOT.md

- [ ] **GitHub Project Board**
  - URL: [EXACT PROJECT URL — FILL IN]
  - Status: ✅ / ⚠️ / ❌
  - Access method: GitHub Connector / Web
  - Fallback: CURRENT_PROJECT_STATUS.md

### MEETING PROTOCOL

- [ ] **Veckan's Meeting Protocol**
  - URL: [GOOGLE DOCS / TXT EXPORT LINK — FILL IN]
  - Status: ✅ / ⚠️ / ❌
  - Access method: Google Drive Connector / TXT export
  - Fallback: PROTOCOL_SNAPSHOT.md

---

## 📝 Verifikationsresultat

**Checked at:** [DATUM] [TIDPUNKT] [TIDSZON]  
**Checked by:** [AI MODEL]  
**Presentation for:** [MÖTE/DATUM]

### Sammanfattning

```
SOURCES READ SUCCESSFULLY (✅):
- Context README
- Presentation specifications
- Cross-team integration
- GitHub branches
- Commits on develop
- GitHub issues
- GitHub PRs
- Project Board
- Meeting protocol

SOURCES WITH FALLBACK (⚠️):
- [Om något används fallback, lista här]

SOURCES THAT FAILED (❌):
- [Om någon källa inte kunde läsas, lista här]
```

### Details per source

- **Context README** → ✅ LÄST
- **PRESENTATION_SPEC** → ✅ LÄST
- **DESIGN_AUTHORITY** → ✅ LÄST
- **PRESENTATION_STYLE** → ✅ LÄST
- **PRESENTATION_STRUCTURE** → ✅ LÄST
- **WEEKLY_PROGRESS_MODEL** → ✅ LÄST
- **DATA_SOURCES** → ✅ LÄST
- **GitHub branches** → ✅ LÄST via Connector
- **GitHub commits** → ✅ LÄST via Connector
- **GitHub issues** → ✅ LÄST via Connector
- **GitHub PRs** → ✅ LÄST via Connector
- **GitHub Project Board** → ✅ LÄST via Connector
- **Meeting protocol** → ✅ LÄST via Google Docs

---

## 📋 Första Slide-Format

Denna SOURCE_CHECK ska visas exakt på **presentationens första slide** (före AGENDA):

```
📝⓪ KÄLLKONTROLL

Senast avstämd: 14 sep 2026 · 08:42 CEST

✅ Context-repo
✅ Presentationsspecs
✅ Cross-team integration
✅ GitHub branches
✅ Commits på develop
✅ Issues
✅ Pull requests
✅ Project Board
✅ Mötesprotokoll

Ej läsbara källor: Inga

[Eller om någon misslyckades:]

⚠️ Project Board — rekonstruerat från issues + PRs
❌ Mötesprotokollet — kunde inte läsas

Presentation bygger på X av Y källor.
```

---

## 💬 Chat-Redovisning

När presentationen levereras i chatten, rapportera FÖRST:

```
Källkontroll · 14 sep 2026 08:42 CEST
✅ Context-repo
✅ Presentationsspecs
✅ Cross-team integration
✅ GitHub branches + commits
✅ Issues
✅ PRs
✅ Project Board
✅ Mötesprotokoll

Ej läsbara källor: Inga
Presentation är klar med full källverifiering.
```

Eller om något misslyckades:

```
Källkontroll · 14 sep 2026 08:42 CEST
✅ Context-repo
✅ Presentationsspecs
⚠️ Project Board (fallback: issues + PRs)
❌ Mötesprotokoll (kunde inte läsas; baseras på mötes-anteckningar)
✅ Övriga källor

Presentation bygger på 7 av 9 huvudkällor.
Status är rekonstruerad från GitHub; mötesbeslut baseras på förra veckans anteckningar.
```

---

## 🎯 Syfte

Denna SOURCE_CHECK säkerställer att:

1. **Transparens** — Du vet exakt vilka källor som användes
2. **Reproducerbarhet** — Samma källor, samma format, varje gång
3. **Tillförlitlighet** — Presentationen är inte byggt på gissningar eller luckfyllningar
4. **Förtroende** — Om något misslyckades rapporteras det öppet
5. **Datakvalitet** — Du kan bedöma om data är aktuell eller fallback

En presentation UTAN SOURCE_CHECK är en presentation du inte kan lita på.
[RETIRED — DO NOT USE FOR PRODUCTION. Allowed sources and access methods are
owned by `_memory/EXTERNAL_SOURCES.yaml`.]

