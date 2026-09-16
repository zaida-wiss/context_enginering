---
name: team_decisions_log
description: Verified decisions made by Team 1 (Avanza Team 1, Chas Challenge 2026)
metadata:
  format: "YAML frontmatter per decision"
  updated: 2026-09-16
  note: "Used by presentation system to show decisions 'since last meeting'. Must have decision_date or updated_date within reporting period."
---

# BESLUT — Team 1

Denna fil dokumenterar verkliga beslut som teamet har fattat under utvecklingen.
Varje beslut ska ha ett tydligt beslutsdatum och påverkan på framtida arbete.

**Format:** Varje beslut är en Markdown-fil med YAML-frontmatter.

---

## Teststrategi — Vitest + RTL

```yaml
---
id: frontend-test-strategy
decision_date: 2026-09-15
updated_date: 2026-09-15
status: confirmed
---
```

**Beslut:**
Frontend använder Vitest + React Testing Library som gemensam testgrund.

**Påverkan:**
- Alla nya frontendtester följer samma teststrategi
- Bidrar till konsistens i testqualitet
- Främjar möjligheten att dela test utilities mellan team

---

## Review som arbetsstatus

```yaml
---
id: review-is-work
decision_date: 2026-09-15
updated_date: 2026-09-15
status: confirmed
---
```

**Beslut:**
Aktivt review-arbete räknas som pågående arbete i teamets kapacitetsmodell.
Reviewers visas inte som "tillgängliga" utan som "Reviewing #XXX".

**Påverkan:**
- Presentationen visar review som aktivt teamarbete
- Korrigerar tidigare skev uppfattning om "tillgänglighet"
- Möjliggör bättre kapacitetsplanering

---

## REDIGERING INSTRUKTIONER

**Lägg till nytt beslut:**

1. Kopiera denna mall:
```yaml
---
id: [slug-name]
decision_date: YYYY-MM-DD
updated_date: YYYY-MM-DD
status: confirmed
---

# [Beslutets namn]

**Beslut:**
[En kort beskrivning av vad som beslutades]

**Påverkan:**
[Varför detta beslut spelar roll för framtida arbete]
```

2. Fylla i:
   - `id`: slug-format (t.ex. `backend-jwt-first`, `native-ci-pipeline`)
   - `decision_date`: dag då beslut fattades
   - `updated_date`: dag då beslut senast uppdaterades/bekräftades
   - `status`: `confirmed` (eller `proposed` om under diskussion)

3. Spara som ny sektion i denna fil

**Viktigt för presentation:**
- AI filtrerar på `decision_date` och `updated_date` för att hitta "beslut sedan förra mötet"
- Datum **måste** finnas för att beslut ska visas i presentation
- Format **måste** vara YYYY-MM-DD (ISO 8601)

---

## EXEMPEL PÅ MER KOMPLEXA BESLUT

### Backend-integration: Java-Development-Environment först

```yaml
---
id: backend-java-dev-first
decision_date: 2026-09-10
updated_date: 2026-09-15
status: confirmed
---
```

**Beslut:**
Backend-arbete integreras alltid till Java-Development-Environment **före** merge till develop.

**Påverkan:**
- Säkerställer säker integration av säkerhetskritisk kod
- Möjliggör teamgranskning innan visibility på develop
- Etablerar branch-workflow som alla Backend-PRs följer

---

## FORMAT KRAV FÖR PRESENTATION SYSTEM

**Dessa fält är OBLIGATORISKA:**

| Fält | Format | Exempel | Används av |
|------|--------|---------|-----------|
| `id` | slug (a-z, -, _) | `frontend-test-strategy` | Deduplication |
| `decision_date` | YYYY-MM-DD | `2026-09-15` | Period filtering |
| `updated_date` | YYYY-MM-DD | `2026-09-15` | Period filtering |
| `status` | `confirmed` eller `proposed` | `confirmed` | Decision inclusion |

**Om dessa saknas:**
- Beslutet visas INTE i presentation ("can't verify date")
- AI loggar varning i DATA_AUDIT

---

**Status:** ACTIVE  
**Last synced with DATA_ACQUISITION_CONTRACT.yaml:** 2026-09-16
