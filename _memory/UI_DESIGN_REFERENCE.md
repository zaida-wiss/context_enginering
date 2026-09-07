---
name: ui_design_reference
description: UI mockups för Avanza Portföljhälsa - design specs och guidelines för frontend-implementering
metadata:
  type: reference
---

# 🎨 UI Design Reference - Portföljhälsa

**Denna memory dokumenterar design-mockups och guidar frontend-teamet när de bygger.**

## Mockup-Mappen

**Sökväg:** `/context_enginering/_docs/`  
**Format:** WebP-bilder (4 mockups från Avanza, ~75 KB totalt)  
**Ansvarig:** Frontend-teamet

## De 4 Mockups

### 1️⃣ **Login-Sida** (`01_login.webp`)
- **Syfte:** Autentisering av användare
- **Komponenter:**
  - Titel: "Portföljhälsa"
  - Email-fält
  - Lösenord-fält
  - "Logga in"-knapp (grön)
- **Färg:** Vit bakgrund, grön knapp (Avanza-brand)

### 2️⃣ **Portföljöversikt** (`02_overview.webp`)
**VIKTIGAST - Huvudvyn**
- **Syfte:** Visa total portföljvärde + varning om drift
- **Key Elements:**
  - **Varningsbox** (orange) när drift > 5%
    - Text: "Portföljen har glidit från målet — aktier 75% mot mål 60% (gräns 5%)"
  - **Total värde:** "698 450 SEK"
  - **FX-kurs:** "Valuta: USD/SEK 10.45"
  - **Kontoöversikt:** ISK (412k), KF (186k), Depå (100k)
  - **Tillgångsslag:** Aktier 75% / Fonder 25%
- **Features:**
  - "Ändra målallokering"-länk
  - "Visa innehav"-länk

### 3️⃣ **Målallokering-Form** (`03_target_allocation.webp`)
**Sätta målportfölj**
- **Syfte:** Användaren definierar sin målallokering
- **Komponenter:**
  - Ikon + label: "Aktier (%)" → Input "60"
  - Ikon + label: "Fonder (%)" → Input "40"
  - **Summa:** "100 %" (måste vara 100%)
  - Info-box: "Ett vanligt exempel är 60 / 40. Det är inte ett råd."
  - "Spara mål"-knapp (grön)
- **Validering:** Måste summera till 100%

### 4️⃣ **Holdings-Tabell** (`04_holdings_table.webp`)
**Alla innehav i listan**
- **Syfte:** Detaljöversikt över varje innehav
- **Kolumner:**
  - Ticker (t.ex. "AAPL")
  - Namn (t.ex. "Apple Inc")
  - Konto (ISK, KF, Depå)
  - Antal
  - Valuta (USD, SEK, etc.)
  - **Värde SEK** (FX-justerad!)
  - Förändring % (grön/röd)
- **Data-exempel från mockup:**
  - AAPL: 10 st USD → 21 000 SEK (+12%)
  - VOLV-B: 40 st SEK → 112 000 SEK (+4%)
  - Avanza Global: 250 st SEK → 89 500 SEK (+7%)

## Använd denna Design När Du Frågar Frontend-AI

**Copy-pasta denna prompt till Claude/ChatGPT när du jobbar på Frontend:**

```markdown
Jag bygger Frontend för Avanza Portföljhälsa.

Här är design-mockups från context_enginering/_docs/:
1. Login-sida
2. Portföljöversikt (med varning när drift > 5%)
3. Målallokering-form (60/40 allocation)
4. Holdings-tabell (alla innehav)

Komponenter jag behöver bygga:
1. LoginForm (email + password)
2. PortfolioOverview 
   - Visa total värde i SEK
   - Varningsbox: "Du driftat från 60% till 75% aktier"
   - Account summary (ISK, KF, Depå)
3. TargetAllocationForm
   - Input för Aktier % + Fonder %
   - Validering: summa = 100%
4. HoldingsTable
   - Ticker | Namn | Konto | Antal | Valuta | Värde SEK | Förändring

Använd design-mockups för CSS/layout inspiration.

Följ dessa standards:
- TypeScript + React
- CSS modules (en fil per komponent)
- PascalCase komponenter
- camelCase variabler
- Se TEAMSTANDARDS.md för detaljer
```

## Design-Principer Från Mockups

### ✅ Färger
- **Grön knapp:** Avanza-brand (#00A86B eller liknande)
- **Orange varning:** Risk-indikator
- **Grå bakgrund:** Neutral, clean design
- **Vit kort/panel:** Fokus på innehål

### ✅ Komponenter Att Bygga

| Komponent | MockUp | Prioritet | Notes |
|-----------|--------|-----------|-------|
| LoginForm | #1 | Högt | Email + Password |
| PortfolioOverview | #2 | KRITISK | Varning när drift > 5% |
| WarningBox | #2 | KRITISK | Orange alert-box |
| TargetAllocationForm | #3 | Högt | Validering: sum = 100% |
| HoldingsTable | #4 | Högt | FX-justerad värde i SEK |
| Navigation/Tabs | Alla | Högt | Toggle mellan sidor |

### ✅ API-Integration (Backend)

Dessa komponenter behöver data från backend:

```typescript
// PortfolioOverview behöver:
interface Portfolio {
  totalValueSEK: number;
  fxRate: { currency: string; rate: number };
  accounts: Account[];
  allocation: { stocks: number; bonds: number };
  targetAllocation: { stocks: number; bonds: number };
  driftPercentage: number; // När > 5%, visa varning
}

// HoldingsTable behöver:
interface Holding {
  ticker: string;
  name: string;
  account: "ISK" | "KF" | "Depå";
  quantity: number;
  currency: "USD" | "EUR" | "SEK" | ...;
  valueSEK: number; // Redan FX-justerad!
  changePercent: number;
}
```

## Hantera Varningen (VIKTIGT!)

**Regel från design:**
- Om `(currentAllocation - targetAllocation) > 5%` → visa varning
- Från mockup: "aktier 75% mot mål 60% (gräns 5%)"
- **Text ska vara dynamisk:** "Du driftat från {target}% till {current}%"

```typescript
// Example logic
const driftPercentage = Math.abs(current - target);
const showWarning = driftPercentage > 5;

if (showWarning) {
  return <WarningBox 
    current={75} 
    target={60} 
    asset="aktier"
    drift={15}
  />;
}
```

## Länk Denna Memory från Dokumenten

**Från:** [_memory/DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md)  
**Från:** [_ai_guides/WHAT_CAN_I_HELP_WITH.md](_ai_guides/WHAT_CAN_I_HELP_WITH.md)  
**Från:** Frontend issue-beskrivningar i GitHub

## Frontend-Checklist Från Design

- [ ] LoginForm komponent (email + password)
- [ ] PortfolioOverview med total värde
- [ ] WarningBox när drift > 5%
- [ ] Account summary (ISK/KF/Depå breakdown)
- [ ] TargetAllocationForm med validering
- [ ] HoldingsTable med alla kolumner
- [ ] FX-justerad värde visas i SEK
- [ ] Förändring % visar grön/röd
- [ ] Navigation mellan tabs fungerar
- [ ] Responsive design (mobil + desktop)
- [ ] Avanza-branding (grön knapp, clean layout)
- [ ] Alla komponenter har TypeScript-interfaces
- [ ] CSS modules för styling
- [ ] Ingen inline styles

---

**Remember:** Dessa mockups är ditt designkontrakt. Om du är osäker på layout/komponenter → referera till mockups och meddela AI.
