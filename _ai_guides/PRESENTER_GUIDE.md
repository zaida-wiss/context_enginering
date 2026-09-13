---
name: presenter-guide
description: Guide for humans presenting — what you need to know before the meeting
metadata:
  type: reference
  audience: presenters (not AI)
---

# 🎤 PRESENTER GUIDE — Before You Present

**Du ska presentera denna vecka? Läs detta innan mötet.**

---

## Quick Start (5 min)

**Innan mötet startar, förstå denna ordning:**

1. **Punkt ① (SEDAN FÖRRA MÖTET)** — Vad blev gjort?
   - Visar merged PRs denna vecka per team
   - Frontend, Backend, Native/System var för sig
   - Varje person som hade arbete ska synas

2. **Punkt ②-⑤ (NULÄGE & TEAM STATUS)** — Var är vi?
   - Övergripande status
   - Varje teams issue-status
   - Handlingsplan per team

3. **Punkt ⑥-⑦ (BLOCKERS & RISKER)** — Vad hindrar oss?
   - Beroenden mellan team
   - Identifierade risker

4. **Punkt ⑧-⑨ (KAPACITET & PRIORITERING)** — Kan vi klara det?
   - Tillgängliga timmar vs behövda
   - Prioriteringsordning (Must/Next/Later)

5. **Punkt ⑩-⑪ (BESLUT & SPRINTMÅL)** — Vad ska fungera?
   - Tekniska avtal mellan team
   - Sprintmålet denna vecka

6. **Punkt ⑫-⑬ (PLAN & ACTIONS)** — Vad gör vi?
   - Är planen realistisk?
   - Vem gör vad?

7. **Punkt ⑭ (FRÅGOR)** — Vad behövs från ledningen?

---

## För Varje Punkt — Vad Du Presenterar

### ① SEDAN FÖRRA MÖTET (3-5 min)
**Vad visar denna slide?**
- Vilka PRs mergades in i develop denna vecka
- Vem ägde varje issue
- Alla teammedlemmar som hade arbete

**Din roll:**
- Läs namnen högt
- Nämn kort vad arbetet var
- Effektbeskrivning: "Det här möjliggör nästa steg"

**Viktigt:**
- Om någon saknas: "X hade ingen verifierad GitHub-aktivitet denna vecka"
- Inte att bedöma arbetet, bara att rapportera det

---

### ② NULÄGE & DEADLINE (2-3 min)
**Vad visar denna slide?**
- Var står vi mot slutleverans
- Nästa checkpoint/deadline
- Status: 🟢 on track / 🟡 slight risk / 🔴 critical

**Din roll:**
- Säg hur långt vi är från deadline
- Säg om vi är on track eller risk

---

### ③-⑤ TEAM STATUS (5-7 min per team)

#### Slide A: Var är vi? (Issue-tabell)
**Vad visar denna slide?**
- Varje issue som är aktiv
- Vem som äger den
- DoD-status (AC, Tests, Review, Docs)

**Din roll:**
- Läs genom tabellen för ditt team
- Förklara vad varje issue gör
- Punkt ut vilka som är nästan klara ("bara review kvar")

**Viktigt:**
- Inte att bedöma, bara att rapportera
- Om något är rött: "Det här behöver uppmärksamhet"

#### Slide B: Handlingsplan (Fyra tabeller)
**Vad visar denna slide?**
1. **Nästa arbete** — prioriterad ordning
2. **Vi väntar på** — inkommande beroenden
3. **Andra väntar på oss** — utgående beroenden
4. **Risker** — specifika för teamet

**Din roll:**
- Läs igenom nästa arbete
- Säg vilka beroenden som påverkar er
- Nämn risker som behöver åtgärd

**Frågor att kunna svara på:**
- "Vad gör du härnäst?" (från Nästa arbete-tabellen)
- "Vem blockerar dig?" (från Vi väntar på)
- "Vem väntar på dig?" (från Andra väntar på oss)

---

### ⑥ BEROENDEN & BLOCKERS (2-3 min)
**Vad visar denna slide?**
- Vem väntar på vem i projektet
- Vilka blockers som existerar
- Fallback-arbete

**Din roll:**
- Peka på blockern i diagrammet
- Säg vad som blockeras
- Nämn fallback-arbetet

---

### ⑦ RISKER (2-3 min)
**Vad visar denna slide?**
- Risk-matris (Sannolikhet × Konsekvens)
- Vilka åtgärder är planerade
- Vem äger varje risk

**Din roll:**
- Läs de högsta riskerna
- Förklara vad som kan gå fel
- Säg vad vi gör åt det

---

### ⑧-⑨ KAPACITET & PRIORITERING (3-4 min)
**Vad visar dessa slides?**
- Tillgängliga timmar vs behövda
- Must / Next / Later kategorisering
- Vad är realistiskt denna vecka

**Din roll:**
- Säg om vi är overloaded eller har buffer
- Förklara prioriteringen
- Säg vad som inte går att hinna

---

### ⑩-⑪ TEKNISKA BESLUT & SPRINTMÅL (2-3 min)
**Vad visar dessa slides?**
- API-kontrakt mellan team
- Sprintmålet denna vecka

**Din rolle:**
- Läs sprintmålet högt
- Förklara vad som ska fungera vid veckoends
- Säg hur det kopplas till deadline

---

### ⑫-⑬ SPRINTPLAN & ACTIONS (3-4 min)
**Vad visar dessa slides?**
- Är planen realistisk? (🟢/🟡/🔴)
- Vem gör vad denna vecka
- Konkreta GitHub-åtgärder efter mötet

**Din roll:**
- Förklara plan-bedömningen
- Läs actionlistan
- Bekräfta: "X är ansvarig för Y"

---

## Viktiga Regler När Du Presenterar

### ✅ DO

- ✅ Läs från sliderna direkt
- ✅ Nämn namn på människor (Zaida, Erik, etc)
- ✅ Förklara varför arbetet spelar roll
- ✅ Säg om något är blockerat eller delayed
- ✅ Ställ frågor om något är oklart
- ✅ Peka ut risker och beroenden
- ✅ Bekräfta att folk förstår handlingsplanen

### ❌ DON'T

- ❌ Ändra data på sliderna (om något är fel, notera det och uppdatera efteråt)
- ❌ Skumma över människor som saknas ("X hade inte tid")
- ❌ Gissa på vad som är gjort (läs bara vad som är verifierat på sliden)
- ❌ Säga "vi behöver prioritera upp det här" (det är redan prioriterat på sliden)
- ❌ Presentera något som inte är på sliden ("vi borde kanske...")

---

## Om Något Ser Fel Ut

**Fråga innan mötet:** Kontakta AI-förbindelsepersonen
- "Den här personen visas inte men de hade arbete denna vecka"
- "Det här numret verkar fel"
- "Vi saknar ett team"

**Anteckna under mötet:**
- Feedback skrivs ned för nästa vecka
- Säg det högt: "Det här behöver kontrolleras"

**Aldrig redigera sliderna själv** — det är AI:s jobb att fixa

---

## Vad Folk Förväntar Sig Från Dig

**Som presentatör förväntas du:**
1. Läst denna guide innan mötet ✅
2. Kunna förklara varje punkt på sliden ✅
3. Kunna svara på "Vad gör JAG härnäst?" ✅
4. Kunna svara på "Vem blockerar oss?" ✅
5. Kunna svara på "Varför är detta prioriterat?" ✅

**Du förväntas INTE:**
- Memorera alla siffror
- Veta detaljer om alla issues
- Göra ändringar på sliderna
- Bedöma om arbetet är bra eller dåligt

---

## Checklista Innan Mötet

```
[ ] Läst denna guide
[ ] Läst mötespunkterna ① till ⑦
[ ] Förstår sprintmålet denna vecka
[ ] Vet vilka mina team-medlemmar är
[ ] Vet vad jag ska göra denna vecka (från slide)
[ ] Kan förklara: "Vad gör vi denna vecka?"
[ ] Kan förklara: "Vem blockerar oss?"
[ ] Kan förklara: "Vad är nästa steg?"
```

---

## Om Du Är Osäker Under Mötet

**Säg en av dessa:**
- "Det här ser ut att behöva kontrolleras"
- "Jag är inte säker på varför det är röd"
- "Det här går inte ihop"
- "Kan vi ta detta efter mötet?"

**Aldrig:** "Jag vet inte vad det här betyder"

---

**Senast uppdaterad:** 2026-09-13
