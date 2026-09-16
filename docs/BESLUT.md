---
name: decisions_index
description: Index of team decisions (actual decisions in docs/decisions/*.md)
metadata:
  format: "One decision per file with YAML frontmatter"
  canonical_path: "docs/decisions/"
  updated: 2026-09-16
---

# BESLUT — Team 1

Denna fil är ett **INDEX** för teamets officiella beslut.

**Alla verkliga beslut lagras i separata filer under [`docs/decisions/`](decisions/).**

## Varför denna struktur?

- **En fil per beslut** = enkel uppdatering, versionshantering, och merge-konflikthantering
- **Maskinläsbar format** = alla AI-agenter tolkar YAML-frontmatter på samma sätt
- **Typ-säker** = DATA_ACQUISITION läser direkt från `docs/decisions/` utan att behöva tolka många frontmatter-block i samma fil

## Aktuella beslut

| Beslut-ID | Titel | Decision Date | Status |
|-----------|-------|---------------|--------|
| `frontend-test-strategy` | [Teststrategi — Vitest + RTL](decisions/frontend-test-strategy.md) | 2026-09-15 | ✓ confirmed |
| `review-is-work` | [Review som arbetsstatus](decisions/review-is-work.md) | 2026-09-15 | ✓ confirmed |

## Lägg till nytt beslut

Skapa ny fil i `docs/decisions/` med namn `<decision-id>.md`:

**Exempel-template:**

```markdown
---
id: <decision-id>
decision_date: YYYY-MM-DD
updated_date: YYYY-MM-DD
status: confirmed
---

# [Beslutets namn]

## Beslut
[Vad beslutades - en eller två meningar]

## Påverkan
[Varför detta spelar roll för framtida arbete]
```

**Regler:**
- `id`: slug-format (lowercase, hyphens) — måste matcha filnamnet
- `decision_date`: när beslut fattades
- `updated_date`: när beslut senast uppdaterades
- `status`: `confirmed` (eller `proposed` om under diskussion)

## Integration med presentation

DATA_ACQUISITION_CONTRACT läser alla `docs/decisions/*.md` filer och:
- Filtrerar på `decision_date` / `updated_date` för rapportperiod
- Exkluderar filer med `status: proposed` (inte bekräftade än)
- Visar upp till 4 beslut i presentation Slide ①E

Se [`CONTEXT_ROUTING.yaml`](../_ai_guides/context/CONTEXT_ROUTING.yaml) för hur man klassificerar nytt innehål.

---

**Status:** ACTIVE  
**Last synced with DATA_ACQUISITION_CONTRACT.yaml:** 2026-09-16
