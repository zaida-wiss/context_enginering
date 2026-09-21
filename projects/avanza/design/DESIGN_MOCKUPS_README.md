# 🎨 UI Design Mockups - Portföljhälsa

**Dessa mockups visar måldesignen för Avanza Portföljhälsa-appen.**

## Assetstatus

De versionshanterade mockup-assetsen ligger under:

`projects/avanza/design/mockups/`

Projektassets ska stanna under projektroten och får inte placeras i globala
`_docs/`, `data/` eller AI-instruktionsmappar.

## Refererade mockups

| Mockup | Sida | Syfte | Format | Storlek |
|--------|------|-------|--------|---------|
| `mockups/01_login.webp` | Login | Inloggnings-sida för användare | WebP | 7.2 KB |
| `mockups/02_overview.webp` | Portföljöversikt | Huvudvyn - total portföljvärde + varning om drift | WebP | 27 KB |
| `mockups/03_target_allocation.webp` | Målallokering | Ange målallokering (60% aktier / 40% fonder) | WebP | 20 KB |
| `mockups/04_holdings_table.webp` | Innehav-tabell | Lista över alla innehav med värde i SEK | WebP | 21 KB |

## Design-Principer (från Mockups)

### ✅ Vad vi MÅSTE ha

1. **Varningsmeddelande när portfölj driftar**
   - "Portföljen har glidit från målet — aktier 75% mot mål 60% (gräns 5%)"
   - Orange varning-box på Portföljöversikt

2. **Målallokering UI**
   - Input-fält för procentsatser (Aktier, Fonder)
   - Validering: summan måste vara 100%
   - "Spara mål"-knapp

3. **Holdings-tabell**
   - Kolumner: Ticker | Namn | Konto | Antal | Valuta | Värde SEK | Förändring %
   - Klickbar för detaljer

4. **Multi-tab Navigation**
   - Portföljöversikt | Målallokering | Innehav | Inloggning
   - Grön accent-färg (Avanza-branding)st

## Använd denna kontext när du frågar Frontend-AI

```
"Jag bygger Frontend för Avanza Portföljhälsa.
Här är designmockups från projects/avanza/design/mockups/:
- Login-sida
- Portföljöversikt med varning
- Målallokering-sida
- Holdings-tabell

Komponenter som krävs:
1. LoginForm
2. PortfolioOverview (med varning när drift > 5%)
3. TargetAllocationForm
4. HoldingsTable

Använd design-mockups för CSS/layout-inspiration.
Resolve TEAM_STANDARDS.md for workflow standards, and verify TypeScript/CSS-module requirements against current project configuration or a documented project requirement."
```

## Frontend implementation context

The following checklist and architecture are preserved from the historical Avanza frontend documentation. They are **project-specific context**, not generic framework rules.

Technology/style requirements such as TypeScript, CSS Modules or exact implementation conventions are mandatory only when verified by the active project repository/configuration, a registered external requirement, or a documented team decision. Do not promote a historical example to a binding rule without that evidence.

## Frontend-Checklist

- ✅ LoginForm komponent med email/password
- ✅ PortfolioOverview visar total värde + varning
- ✅ TargetAllocationForm med validering
- ✅ HoldingsTable med alla kolumner
- ✅ Navigation mellan tabs
- ✅ Responsive design (mobil + desktop)
- ✅ Avanza grön branding (#00A86B eller liknande)

## Diagram över UI-arkitektur

```
App.tsx
├── Navigation (tabs)
├── LoginForm (konditionell rendering)
├── PortfolioOverview
│   ├── WarningBox (när drift > 5%)
│   ├── AccountsSummary
│   └── AllocationCards
├── TargetAllocationForm
└── HoldingsTable
```

---

**Senast uppdaterad:** 2026-09-07
**Status:** Historical project design context preserved; image assets are stored under the project root and implementation requirements must be re-verified against active project sources
