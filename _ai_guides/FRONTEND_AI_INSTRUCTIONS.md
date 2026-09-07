# 🎨 Frontend AI Instructions

**Denna fil instruerar ALLA AI-assistenter hur de ska hjälpa med frontend-utveckling.**

Läs denna **varje gång** användaren frågar om frontend-kod.

---

## ⚙️ Din Instruktion (VARJE FRONTEND-FRÅGA)

**REGEL: Du MÅSTE läsa design-specen innan du svarar**

1. **Läs denna fil** (`FRONTEND_AI_INSTRUCTIONS.md`) ← Du är här
2. **Läs sedan:** `_memory/UI_DESIGN_REFERENCE.md`
3. **Kolla bilderna:** `_docs/`-mappen för mockups
4. **Basera svaret på:** Design-specifikationen från mockuperna
5. **Referera i svaret:** "Enligt mockup XX..."

---

## 🎯 Frontend-Komponenter & Mockups

| Komponent | Mockup-Fil | Vad Den Visar |
|-----------|-----------|---------------|
| LoginForm | `01_login.webp` | Email + lösenord inloggning |
| PortfolioOverview | `02_overview.webp` | Huvudvy med varning när drift > 5% |
| WarningBox | `02_overview.webp` | Orange varningsbox för drift |
| TargetAllocationForm | `03_target_allocation.webp` | Sätta 60/40 målallokering |
| HoldingsTable | `04_holdings_table.webp` | Tabell med alla innehav i SEK |

---

## 📝 Svar-Format - Så Ska Du Struktura Det

**Använd denna struktur VARJE GÅNG du svarar på frontend-frågor:**

```markdown
## [Komponentnamn]

Enligt mockup [XX_namn.webp] (_docs/XX_namn.webp) behöver komponenten:
- Requirement 1 från designen
- Requirement 2 från designen
- Requirement 3 från designen

### Kod (TypeScript + React)
[Din implementering här]

### Design-Checklist
- [ ] Matchar mockup-layout
- [ ] Använder rätt färger (från mockup)
- [ ] Validering enligt spec
- [ ] CSS modules (en per komponent)

### Se även
- [UI_DESIGN_REFERENCE.md](../  UI_DESIGN_REFERENCE.md) - Full spec för denna komponent
- [DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md) - Acceptance criteria
- [TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md) - Code standards
```

---

## ❌ Vad Du INTE Ska Göra

❌ Svara på frontend-frågor utan att läsa UI_DESIGN_REFERENCE.md först  
❌ Förutsätta design utan att kolla mockup-bilderna  
❌ Bygga komponenter som inte matchar mockup-specen  
❌ Ge layout-förslag som strider mot designen  
❌ Ignorera varnings-logiken (drift > 5%)  

**Istället:** Alltid säg "Enligt mockup..." och referera till bildfilen

---

## 🎨 Design-Detaljer Du MÅSTE Följa

### Färger
- **Grön knapp:** Avanza-brand (#00A86B eller liknande)
- **Orange varning:** Risk-indikator (risk-box)
- **Grå bakgrund:** Neutral, clean design
- **Vit panel:** Fokus på innehål

### Komponenter (Mandatory)
- LoginForm - Email + Password inputs
- PortfolioOverview - Total värde + varning
- WarningBox - Orange alert när drift > 5%
- TargetAllocationForm - Input validering (sum = 100%)
- HoldingsTable - 7 kolumner med FX-justerad värde

### Varning-Logic (KRITISK!)
```
Om (currentAllocation - targetAllocation) > 5% → Visa WarningBox

Exempel från mockup:
- Mål: 60% aktier
- Faktisk: 75% aktier
- Drift: 15% (> 5%) → VISA VARNING
- Text: "Du driftat från 60% till 75% aktier (gräns 5%)"
```

---

## 🔗 Länka Till Mockups i Svaret

**Så refererar du i ditt svar:**

```markdown
Enligt mockup [02_overview.webp](_docs/02_overview.webp):
- Varningsbox ska vara orange
- Text ska vara dynamisk: "Du driftat från {target}% till {current}%"
- Kolla UI_DESIGN_REFERENCE.md för detaljer
```

---

## 📚 Standard References

**För varje frontend-fråga, referera även till:**

1. **[UI_DESIGN_REFERENCE.md](_memory/UI_DESIGN_REFERENCE.md)** - Full mockup-spec
2. **[DEFINITION_OF_DONE.md](_memory/DEFINITION_OF_DONE.md)** - Acceptance criteria
3. **[TEAMSTANDARDS.md](_memory/TEAMSTANDARDS.md)** - Code standards (TypeScript, CSS modules, etc.)

---

## ✅ Checklist - Innan Du Svarar

Innan du skickar frontend-hjälpen, kontrollera:

- [ ] Jag läste `UI_DESIGN_REFERENCE.md`
- [ ] Jag kollade mockup-bilden(es) i `_docs/`
- [ ] Min kod matchar mockup-specen
- [ ] Jag refererade till mockup-bilden(es) i mitt svar
- [ ] Jag länkade till `UI_DESIGN_REFERENCE.md`
- [ ] Kod följer `TEAMSTANDARDS.md` (TypeScript, CSS modules, etc.)
- [ ] Jag nämner acceptance criteria från `DEFINITION_OF_DONE.md`

---

## 🚨 Om Användaren Säger

**"Hjälp mig bygga [komponent]"**  
→ Läs mockup-specen, ge kod + design-checklist + links

**"Varför denna design?"**  
→ Referera till mockup-bilden och säg "Enligt mockup XX..."

**"Kan jag göra det annorlunda?"**  
→ Säg: "Mockup visar detta. Om det behöver ändras, uppdatera mockup-bilden först, sen revidera jag koden."

**"Det fungerar inte som mockup visar"**  
→ Debug utifrån mockup-specen, ge korrigerad kod

---

## 📞 Vid Frågor

Om du är osäker på design-detaljer:
1. Kolla mockup-bilden igen
2. Läs UI_DESIGN_REFERENCE.md igen
3. Om fortfarande osäker, säg: "Enligt mockup visar designen X, men det behöver förtydligas. Kan du bekräfta?"

---

**Version:** 1.0  
**Senast uppdaterad:** 2026-09-07  
**Ansvarig:** Frontend-teamet + AI-assistenter

**Denna fil läses automatiskt varje gång frontend-hjälp behövs.**
