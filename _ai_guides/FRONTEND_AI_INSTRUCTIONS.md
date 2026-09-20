# 🎨 Frontend AI Instructions

**Denna fil instruerar ALLA AI-assistenter hur de ska hjälpa med frontend-utveckling.**

Läs denna **varje gång** användaren frågar om frontend-kod.

---

## ⚙️ Din Instruktion (VARJE FRONTEND-FRÅGA)

**REGEL: Du MÅSTE läsa design-specen innan du svarar**

1. **Läs denna fil** (`FRONTEND_AI_INSTRUCTIONS.md`) ← Du är här
2. **Resolve selected project:** `PROJECTS.yaml → selected project → PROJECT.yaml`
3. **Läs projektets registrerade designkontext**, för Avanza: `projects/avanza/design/DESIGN_MOCKUPS_README.md`
4. **Kontrollera endast bild-assets som faktiskt finns i Git.** Saknas en refererad asset får AI:n inte påstå att bilden har inspekterats.
5. **Basera svaret på verifierad designkontext** och skilj dokumenterade designkrav från visuellt verifierade detaljer.

---

## 📘 TypeScript är Mandatory

**REGEL: Alla kodexempel MÅSTE vara TypeScript**

- ✅ Explicit types på all kod
- ✅ Interfaces för all data
- ✅ Enums för constants
- ✅ Generics där relevant
- ✅ Strict mode enabled
- ❌ ALDRIG `any` types
- ❌ ALDRIG JavaScript-only
- ❌ ALDRIG lösa typer

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

Enligt den verifierade projektdesignen behöver komponenten:
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
- Projektets registrerade designkontext via `PROJECT.yaml → context.design.*`
- [DEFINITION_OF_DONE.md](project/DEFINITION_OF_DONE.md) - Acceptance criteria
- [TEAM_STANDARDS.md](project/TEAM_STANDARDS.md) - Code standards
```

---

## ❌ Vad Du INTE Ska Göra

❌ Svara på frontend-frågor utan att läsa projektets registrerade designkontext först  
❌ Påstå att en mockup-bild har kontrollerats när asseten saknas  
❌ Bygga komponenter som strider mot verifierad designkontext  
❌ Ge layout-förslag som strider mot designen  
❌ Ignorera dokumenterad varnings-logik (drift > 5%)  

**Istället:** Ange om uppgiften kommer från dokumenterad designkontext eller från en faktiskt verifierad bild-asset.

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

## 🔗 Källstatus för mockups

För Avanza beskriver projektdokumentationen fyra historiska mockups, men dessa assets är för närvarande markerade som saknade i Git. Referera därför till designkravet i dokumentationen, inte till en bild som om den hade inspekterats. Om assets senare återfinns och verifieras kan visuella detaljer åter användas som bildbelagd källa.

---

## 📚 Standard References

**För varje frontend-fråga, referera även till:**

1. **Projektets registrerade designkontext** via `PROJECT.yaml → context.design.*`
2. **[DEFINITION_OF_DONE.md](project/DEFINITION_OF_DONE.md)** - Acceptance criteria
3. **[TEAM_STANDARDS.md](project/TEAM_STANDARDS.md)** - Code standards (TypeScript, CSS modules, etc.)

---

## ✅ Checklist - Innan Du Svarar

Innan du skickar frontend-hjälpen, kontrollera:

- [ ] Jag läste projektets registrerade designkontext
- [ ] Jag verifierade om refererade bild-assets faktiskt finns
- [ ] Jag skiljer dokumenterad design från visuellt verifierad design
- [ ] Min kod matchar den verifierade designkontexten
- [ ] Jag påstår inte att en saknad bild har inspekterats
- [ ] Kod följer `TEAM_STANDARDS.md` (TypeScript, CSS modules, etc.)
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
1. Läs projektets registrerade designkontext igen
2. Kontrollera om relevant asset faktiskt finns
3. Om en visuell detalj inte kan verifieras, säg tydligt att dokumentationen beskriver kravet men att bilden saknas; gissa inte.

---

**Version:** 1.1  
**Senast uppdaterad:** 2026-09-20  
**Ansvarig:** Frontend-teamet + AI-assistenter

**Denna fil läses automatiskt varje gång frontend-hjälp behövs.**
