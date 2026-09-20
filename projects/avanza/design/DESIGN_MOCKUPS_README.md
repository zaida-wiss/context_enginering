# 🎨 UI Design Mockups - Portföljhälsa

**Dessa mockups visar måldesignen för Avanza Portföljhälsa-appen.**

## Assetstatus

> ⚠️ **Refererade assets saknas i Git.** De fyra mockupfilerna nedan beskrivs av den historiska projektdokumentationen, men har inte kunnat återfinnas på `dev` eller beläggas som versionshanterade filer i den granskade Git-historiken. Dokumentationen bevaras som projektkontext; filerna får inte behandlas som tillgängliga förrän de faktiskt återfinns eller återskapas från en verifierad källa.

## Refererade mockups

| Mockup | Sida | Syfte | Format | Storlek |
|--------|------|-------|--------|---------|
| `01_login.webp` *(saknas)* | Login | Inloggnings-sida för användare | WebP | 7.2 KB |
| `02_overview.webp` *(saknas)* | Portföljöversikt | Huvudvyn - total portföljvärde + varning om drift | WebP | 27 KB |
| `03_target_allocation.webp` *(saknas)* | Målallokering | Ange målallokering (60% aktier / 40% fonder) | WebP | 20 KB |
| `04_holdings_table.webp` *(saknas)* | Innehav-tabell | Lista över alla innehav med värde i SEK | WebP | 21 KB |

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
Här är designmockups från _docs/:
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
Follow TEAM_STANDARDS.md för TypeScript + CSS modules."
```

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
**Status:** Design mockups från Avanza - redo för implementation
