# 📋 PRESENTATION SPECIFICATION — Source of Truth

**Denna fil är den ENDA auktoritativa specifikationen för presentationer.**  
Andra filer (DESIGN, FORMAT_GUIDE, STRUCTURE) fördjupar denna spec men motsäger aldrig den.

---

## 🎯 Presentationens Tre Syften

1. **TEAMTÄNK** — Hjälpa teamet att nå sprintmålet tillsammans, inte rapportera individuella insatser
2. **BRANSCHPEDAGOGIK** — Lära teamet domänvokabulär medan vi arbetar
3. **TEAMSTÖD** — Identifiera var hjälp behövs och omfördela kapacitet

---

## 📌 Issue Format — Enda Giltiga Format

**VARJE issue-referens MÅSTE följa detta format, överallt:**

```
#40 – Login page · Zaida
#43 – API client · Erik (förslag)
#48 – Risk dashboard · ??
```

**Tolkning:**
- `#40 –` = issue-nummer med bindestreck
- `Login page` = kortfattad titel
- `·` = mitternpunkt som separator
- `Zaida` = faktisk assignee
- `Erik (förslag)` = föreslaget namn (ännu ej bekräftat)
- `??` = okänd assignee (behöver beslut på mötet)

**Detta gäller överallt:**
- Issue-tabeller
- Risk-kort
- Dependency-diagram
- Footnotes
- Sprint goals
- Löptext

Ingen issue-referens får sakna assignee-information.

---

## 🎨 Färgsemantik — Förbjudna & Obligatoriska Regler

**PRINCIP: Färg är semantik, aldrig dekoration. Varje färg måste betyda något.**

### Status-Färger (Endast För Faktisk Status)

```
🟢 GRÖN = Verifierat bra / Klart / On track / Låg risk
🟡 GUL = Behöver uppmärksamhet / Beslut ausstående
🟠 ORANGE = Risk / Osäkerhet / Kapacitets-/beroenderisk
🔴 RÖD = Blockerad / Kritisk risk / Måste agera omedelbar
```

**STRIKT REGEL:**
Dessa färger får ENDAST användas när elementet faktiskt kommunicerar denna status.
Om du måste förklara "det betyder inte verkligen rött" → använd neutral färg istället.

### Neutral Färger (För All Övrig Information)

```
🔵 Marinblå = Huvudrubriker, viktig struktur
🔵 Ljusblå = Neutral information, processer, tekniska samband
⚫ Blågrå / Ljusgrå = Vanliga informationskort, team-kort
⚪ Vit = Luft, huvudytor, negativt utrymme
```

### Accent-Färger (Icke-Status Syften)

```
💜 Lila = Sprintplanering, beslut, prioriteringar, förslag, "nästa steg"
🌸 Dämpad rosa = Människor, ägarskap, assignees, samarbete
```

### BORDER-FÖRBUDSREGEL

```
🚨 STRIKT: Röda, orange, gröna eller gula borders är FÖRBJUDNA på neutral mark.

❌ FELAKTIGT:
  [Neutral teamkort med grön border]  ← ser ut som "bra status" men är bara struktur
  [Neutral risklista med orange border] ← förbisningen risker
  [Neutral issue-container med röd border] ← får oläslig prioritet

✅ KORREKT:
  [Neutral grå teamkort → liten 🟠 markering bredvid "API dependency"]
  [Neutral grå riskkort → 🔴 indikator på kritisk item, inte hela kortet]
```

**Om ett neutralt element innehåller status:** Visa status med liten lokaliserad indikator INNANFÖR kortet, aldrig genom att färga hela kortet eller ramen.

### Preflight-Kontroll

Presentationen **misslyckades** om:
- [ ] En neutral ruta har grön border
- [ ] En neutral ruta har orange border
- [ ] En neutral ruta har röd border
- [ ] En hel teamruta färgas efter en enskild risk
- [ ] En färg används utan att kunna förklara dess status-betydelse

---

## ⚡ Risk / Dependency / Blocker — Definitioner & Format

### Risk
```
Potentiell framtida problem som kan påverka sprint-leverans.

OBLIGATORISK STRUKTUR:
  Risk: [namn]
  Nuläge: [faktisk situation nu]
  Konsekvens: [vad händer om det inträffar]
  Sannolikhet: 🟢 / 🟡 / 🟠 / 🔴
  Åtgärd: [vad gör vi]
  Ägare: [vem ansvarar]
```

### Dependency
```
Arbetet är beroende av något annat, men produktivt arbete KAN fortsätta.

OBLIGATORISK STRUKTUR:
  Dependency: [namn]
  Väntar på: [vad/vem]
  Blockerar: [vilka uppgifter]
  Fallback-arbete: [vad kan vi göra istället denna vecka]
  Förväntat löst: [datum]
```

### Blocker
```
Aktuellt arbete KAN INTE fortsätta utan detta löst.

OBLIGATORISK STRUKTUR:
  Blocker: [namn]
  Blockerar: [vilka uppgifter / vilket team]
  Root cause: [varför kan arbetet inte fortsätta]
  Åtgärd: [vad gör vi NU]
  Ägare: [vem ansvarar]
  Förväntat löst: [tid/datum]
```

### Team Blockerad (Inte Bara Ett Beroende)
```
Teamet saknar produktivt oberoende arbete att göra.

KAN BARA HÄNDA OM:
- Alla kritiska beroenden är obeslutade/okända
- Fallback-arbete saknas eller är också blockerat
- Team-medlemmar kan inte rediriera till annan MVP-feature

ÅTGÄRD: Omfördela från annat team eller prioritera annan feature.
```

---

## 📊 Sprint-Planering: Kapacitet & Avlastning

### Obligatorisk Struktur

```
KAPACITET → KRITISK VÄG → KAN AVLASTA → HUR

Exempel:

FRONTEND
  Tillgänglig: 60 timmar denna vecka
  Kritisk väg: #40 Portfolio (20h) + #43 Risk calc (25h) = 45h
  Margin: 15h
  
  Kan avlasta: Ja
    · API-kontrakt & mock-data prep (5h)
    · Integrations-tests setup (5h)
    · Target-allocation responsivitet (5h)

RESULTAT: Frontend kan ta #52 Target allocation denna vecka
```

### Fallback-Arbete (Obligatoriskt För Varje Beroende)

**För varje kritiskt beroende: identifiera nästa högst prioriterade OBEROENDE arbete.**

```
FRONTEND PRIMÄRT: #40 Integration med Backend
  ↓ Backend API ej redo → DEPENDENCY

FALLBACK A: #52 Frontend-testgrund (oberoende)
  ↓ (om färdigt snabbare)

FALLBACK B: #55 Target-allocation (oberoende)
  ↓ (om ännu tidigare färdigt)

FALLBACK C: #58 Responsivitet-UX polish (oberoende)
```

Fallback-arbete **måste** hämtas från GitHub Project Board denna vecka — aldrig uppfunna.

---

## ✅ Preflight-Validator (Obligatorisk Innan Leverans)

Presentationen accepteras **INTE** förrän alla dessa kontroller passerar:

```
ISSUE-FORMAT:
  ☐ Varje #XX har assignee eller ?? (ingen exception)
  ☐ Format konsekvent (#XX – Title · Name) överallt
  ☐ Förslag märkta (förslag), inte osäkra

FÄRGKODNING:
  ☐ Grön används ENDAST för faktisk god status
  ☐ Orange används ENDAST för faktisk risk/osäkerhet
  ☐ Röd används ENDAST för faktisk blockering/kritisk
  ☐ Gul används ENDAST för "behöver beslut"
  ☐ Inga statusfärger på neutral mark
  ☐ Inga statusfärgade borders på neutral info
  ☐ Neutral information använder marinblå/grå/vit

RISK/BLOCKER/DEPENDENCY:
  ☐ Varje risk har: Nuläge + Konsekvens + Nivå + Åtgärd + Ägare
  ☐ Varje dependency har: Fallback-arbete identifierat
  ☐ Varje blocker har: Root cause + Åtgärd + Förväntat löst
  ☐ Om team är blockerat: Omfördelning eller ny feature föreslagen

KAPACITET & AVLASTNING:
  ☐ Kapacitet visar: Tillgängligt + Kritisk väg + Margin
  ☐ Avlastning analyserad: Kan andra team ta arbete?
  ☐ Fallback-arbete listades för alla dependencies

LESBARHET:
  ☐ Ingen text går utanför sin box
  ☐ Min. 4.5:1 kontrast (WCAG AA)
  ☐ 60-70% whitespace (NPF-vänligt)
  ☐ Varje branschterm på sliden förklaras (inte nya termer i förklaring)

OM NÅGON KONTROLL MISSLYCKAS:
  Presentationen är INTE färdig.
  Åtgärda problemen och genomför validator igen.
```

---

## 📝 14 Mötespunkter (Struktur)

**En mötespunkt ≠ en slide. Presentationen blir 20–30 slides.**

Mötespunkterna är:
1. **Sedan förra mötet** — Commits från alla team
2. **Sprintmål** — Big picture
3. **Nuläge** — Övergripande status
4. **Frontend status** — Issues, progress, risk
5. **Backend status** — Issues, progress, risk
6. **Native status** — Issues, progress, risk
7. **Beroenden & Blockers** — Vad väntar på vad + fallback-arbete
8. **Prioritering & Scope** — Must/Next/Later
9. **Kapacitet & Estimering** — Tillgängligt vs Behövt
10. **Risker** — Risk-matrix med åtgärder
11. **Tekniska Beslut** — Arkitektur-beslut denna vecka
12. **Sprintplan** — Konkret vem gör vad denna vecka (visar support/pairing)
13. **Nästa Steg** — Action plan + Teamstöd & Hållbarhet
14. **Frågor till PL** — Discussion board

---

## 🔍 Git-Board Verifiering (Obligatorisk Innan Presentation)

Se **VERIFICATION_BOARD_VS_GIT.md** för detaljer.

**TL;DR:**
- Git är sanningen när Board är stale
- Status-koder: 🟢 Verifierad | 🟣 Git-verified-Board-stale | ⚪ Unverified | 🔴 Konflikt
- Märk alla Board-diskrepanser i presentationen

---

## 📚 Branschpedagogik

**Regel: Förklara bara ord som står på sliden. Aldrig introducera nya termer.**

Varje term ska förklaras simpelt när den förekommer första gången:
```
Risk Dashboard (visar risk-mått: volatilitet = prissvängningar, 
Sharpe-ratio = risk-justerad avkastning)
```

Termer markeras med 📚 för att visa att detta är lärmål.

---

**Senast uppdaterad:** 2026-09-13  
**Syfte:** Canonical specification för alla presentationer  
**Status:** Source of Truth — alla andra filer fördjupar, motsäger aldrig denna
