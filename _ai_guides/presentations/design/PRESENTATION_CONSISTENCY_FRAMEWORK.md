---
name: presentation_consistency_framework
description: DEPRECATED — innehål flyttat till SLIDE_DETAIL_SPEC.md och PRESENTATION_RED_THREADS.md
metadata:
  type: reference
  deprecated: true
---

# 🚨 DEPRECATED — LÄSNING REKOMMENDERAS EJ

**DENNA FIL INNEHÖLL REGLER SOM NU ÄR GAMLA OCH STRIDER MOT NYA SPECIFIKATIONER.**

**🔴 VIKTIGT:** Denna fil definierade gamla KOLUMNER för slide-tabeller:
```
GAMMAL (föråldrad):      | Issue | Vad | Ägare | Status | AC | Tests | Review | Docs | PR |
NY (authoritative):      | Issue # | Titel | Assignad | Status | Merged/Branch |
```

**Nya, authoritative källor:**
- **Slide-level format** → [SLIDE_DETAIL_SPEC.md](./SLIDE_DETAIL_SPEC.md) ✅ ANVÄND DENNA
- **Röda trådar** → [PRESENTATION_RED_THREADS.md](./PRESENTATION_RED_THREADS.md) ✅ ANVÄND DENNA
- **Gamla tabellregler** → RADERA (strider mot SLIDE_DETAIL_SPEC.md)

**Denna fil sparas för historisk referens men ska INTE användas för nya presentationer.**

---

# PRESENTATION CONSISTENCY FRAMEWORK (DEPRECATED)

**Mål:** Varje presentation ser likadan ut, följer samma logik, och har en tydlig röd tråd.

⚠️ **OBSERVERA:** Se PRESENTATION_RED_THREADS.md för uppdaterade röda-trådar.

---

## DEEL 1: VISUELL KONSISTENS (DESIGN)

### Header på varje slide

**Obligatorisk struktur per slide:**

```
📝[NUMMER] [PUNKT-NAMN]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[SLIDE TITLE / RUBRIK]

[INNEHÅL]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Källa: GitHub | Verifiera: [link]
```

### Struktur per mötespunkt

**Alla punkter 1-14 följer samma mall:**

| Del | Syfte | Visuellt |
|-----|--------|----------|
| A-delen | "Var är läget?" | Tabell eller diagram |
| B-delen | "Vad gör vi?" | Konkret lista med åtgärder |
| (C-delen) | (Extra detalj) | (Visuell demo eller djup-info) |

### Färgkod — SEMANTISK BARA

**Färger används bara för FAKTISK STATUS, aldrig för estetik:**

- 🟢 **Grönt** = Klart / Verifierat / Ready to go
- 🟡 **Orange** = Pågår / Behöver uppmärksamhet / Tight
- 🔴 **Rött** = Blockerat / Kritiskt / EJ OK
- ⚪ **Vit/grå** = Neutral / Ingen aktivitet / Ej tilldelat
- 🟦 **Blå** = Endast för info-sektioner, aldrig status

**ALDRIG:** Dekorativ färg. Aldrig gradient. Aldrig för att "se snygg ut".

### Tabeller — SAMMA FORMAT VARJE GÅNG

**Alla issue-tabeller har denna struktur:**

```
| Issue | Vad | Ägare | Status | AC | Tests | Review | Docs | PR |
|-------|-----|-------|--------|----|----|--------|------|-----|
```

**Inte nödvändigt att visa alla kolumner — men ordningen är ALLTID densamma.**

Om en kolumn inte behövs denna vecka → dölj den, men behåll ordningen för nästa vecka.

### Mötesspunkt-märken — KONSISTENT

Varje slide börjar med:
```
📝① SEDAN FÖRRA MÖTET
📝②A Övergripande status
📝②B Nästa checkpoint
📝③A Var är vi? — Issues
📝③B Handlingsplan
...osv
```

**Märken är KONSTANTA varje vecka.** Mötet vet: "Punkt ③A är alltid issue-tabellen".

---

## DEL 2: INNEHÅLLS-KONSISTENS

### Varje punkt MÅSTE svara på samma fråga varje vecka

| Punkt | Frågan som besvaras | Data från | Visar |
|-------|-------------------|-----------|-------|
| ① | Vad blev gjort denna vecka? | GitHub PRs, commits | MERGED PRs + assignees |
| ② | Var står vi mot deadline? | Project Board, kurs | Status + nästa checkpoint |
| ③-⑤ | Var är varje team? | GitHub issues, DoD | Issue-tabell per team |
| ⑥ | Vem väntar på vem? | GitHub dependencies | Blocker-flöde |
| ⑦ | Vad kan brista? | Risk register | Risk-matris |
| ⑧ | Kan vi klara det? | Estimat + timmar | Kapacitet-graf |
| ⑨ | Vad är viktigast? | Prioriteringar | Must/Next/Later |
| ⑩ | Vilka kontrakt är låsta? | Tekniska beslut | API/integration-avtal |
| ⑪ | Vad ska fungera slut-veckan? | Prioritering + kapacitet | Sprint goal |
| ⑫ | Är planen rimlig? | Alla föregående | Plan-bedömning + Board-review |
| ⑬ | Vem gör vad efter mötet? | Mötes-beslut | GitHub-actions + pairing |
| ⑭ | Vad behöver ledningen? | Teamet | Öppna frågor |

**Varje punkt svarar på SAMMA fråga varje vecka. Innehållet kan ändras, men frågan är konstant.**

### Röd tråd: Fakta → Analys → Beslut

**Presentationen följer denna logik:**

```
FAKTA (①②):
  Vad hände? Var står vi?
  
ANALYS (③-⑨):
  Hur ser det ut per team?
  Vad blockerar oss?
  Vilka risker finns?
  Hur mycket kan vi göra?
  Vad är viktigast?
  
BESLUT (⑩-⑭):
  Vilka tekniska kontrakt?
  Vad är sprintmålet?
  Är planen rimlig?
  Vem gör vad?
  Vad frågade ledningen?
```

**Denna flöde är ALLTID densamma.**

---

## DEL 3: REPETERBARA STRUKTURER PER PUNKT

### Struktur för TEAM-SLIDES (③④⑤)

**Varje teamslide är uppbyggd identiskt:**

#### A-sliden: "Var är vi? — Issue-status"

1. **Header:** `📝③A VAR ÄR VI? — ISSUE- OCH DOD-STATUS`
2. **Beskrivning:** `Frontend team status denna vecka`
3. **Innehål:** Issue-tabell (samma format varje vecka)
4. **Footer:** `Källa: GitHub issues | Verifiera: [link till board]`

#### B-sliden: "Vad behöver vi göra? — Handlingsplan"

1. **Header:** `📝③B VAD BEHÖVER VI GÖRA? — HANDLINGSPLAN, BEROENDEN & RISKER`
2. **Fyra sektioner** (ALLTID i denna ordning):
   - A. Nästa arbete (tabell)
   - B. Vi väntar på (tabell)
   - C. Andra väntar på oss (tabell)
   - D. Risker att diskutera (tabell)
3. **Footer:** `Källa: GitHub issues + DoD status`

**Samma struktur för Backend (④) och Native (⑤).**

### Struktur för ANALYS-SLIDES (⑥⑦⑧⑨)

**Varje analys-slide följer denna mall:**

1. **Problem-statement:** Vad fråga besvarar vi?
2. **Data-källa:** Varifrån kommer informationen?
3. **Visuell representation:** Diagram, matris eller tabell
4. **Tolkning:** Vad betyder det?
5. **Nästa steg:** Vad gör vi med denna info?

### Struktur för BESLUT-SLIDES (⑩⑪⑫⑬)

**Varje beslut-slide följer denna mall:**

1. **Beslut som är fattad:** Vad är konklutt?
2. **Från vilken analys:** Vilka slides ledde hit?
3. **Vem äger det:** Vem ansvarar?
4. **Deadline:** När är det gjort?
5. **Verifiering:** Hur vet vi det fungerar?

---

## DEL 4: RÖDA TRÅDAR

### Huvudsakliga röda trådar genom mötet

#### Tråd 1: ARBETET ("ARBETE-TRÅDEN")

```
① Vad blev gjort förra veckan?
  ↓
③-⑤ Vad pågår denna vecka?
  ↓
⑫ Är det tillräckligt för sprintmålet?
  ↓
⑬ Vem jobbar på vad härnäst?
```

Röd tråd: **Från förra veckas resultat → denna veckas plan → nästa veckas arbete**

#### Tråd 2: BLOCKERS ("HINDER-TRÅDEN")

```
③-⑤ Varje team rapporterar: "Vi väntar på..."
  ↓
⑥ Övergripande bild: Vem blockerar vem?
  ↓
⑫ Plan-kontroll: Har vi fallback-arbete?
  ↓
⑬ Vem löser blockers innan nästa möte?
```

Röd tråd: **Från lokal blocker → projektöversikt → handlingsplan**

#### Tråd 3: RISKER ("RISK-TRÅDEN")

```
⑦ Identifierade risker
  ↓
⑧ Hur påverkar risk vår kapacitet?
  ↓
⑨ Ändrar risken vår prioritering?
  ↓
⑪ Sprintmål måste hantera denna risk
  ↓
⑫ Plan-kontroll: Är åtgärden planerad?
```

Röd tråd: **Från risk-identifiering → plan-justering → verifiering**

#### Tråd 4: KAPACITET ("REALISM-TRÅDEN")

```
③-⑤ Varje team rapporterar estimat
  ↓
⑧ Totalt: Kan vi klara allt?
  ↓
⑨ Prioritering: Vad MÅSTE vi välja?
  ↓
⑪ Sprintmål baserat på faktisk kapacitet
  ↓
⑫ Plan-kontroll: Är planen realistisk?
```

Röd tråd: **Från estimat → kapacitet → möjligt sprintmål → verifierad plan**

---

## DEL 5: VARNING-SIGNALER (Så att röda tråden inte bryts)

**Om dessa saknas, presentationen är INKOMPLETT:**

### Röda trådar som kan gå förlorade

- ❌ Punkt ① (förra veckan) är tom eller saknar arbete → vi vet inte vad som gjordes
  - **OBS:** Punkt ① kan ha 1-2 slides (tabeller per team: Frontend, Backend, Native)
  - ALLA arbete som gjordes denna vecka MÅSTE synas
  - Inget får utelämnas för att det inte fick plats
- ❌ Punkt ② (nuläge & deadline) saknar tidsplan → mötet vet inte varför det bryr sig
- ❌ Punkt ③-⑤ (teams) saknar "väntar på..." → vi ser inte vilka är blockerade
- ❌ Punkt ⑥ (blockers) saknas → vi ser inte helhetsbilden av beroenden
- ❌ Punkt ⑧ (kapacitet) ej jämfört mot ⑨ → planen kan vara omöjlig
- ❌ Punkt ⑪ (sprintmål) är från förra mötet, inte HÄRLEDD från ①-⑩ → målet är inte realistisk-baserat
- ❌ Punkt ⑫ (sprintplan) saknas → vi vet inte om tidsplanen håller
- ❌ Punkt ⑬ (nästa steg) är lösa idéer, inte konkreta GitHub-åtgärder → mötet blir inte arbete

**Var och en av dessa är KRITISK för röda tråden.**

---

## DEL 6: CHECKLIST FÖR RÖDA TRÅDAR

**Innan presentation renderas, kontrollera:**

### Arbete-tråden
- ✅ Punkt ① visar faktiska merged PRs denna vecka?
- ✅ Punkt ③-⑤ visar pågående arbete denna vecka?
- ✅ Punkt ⑫ jämför detta mot sprintmål?
- ✅ Punkt ⑬ visar vem som jobbar på vad härnäst?

### Hinder-tråden
- ✅ Punkt ③-⑤ visar "vi väntar på..." för varje team?
- ✅ Punkt ⑥ visar övergripande bild av beroenden?
- ✅ Punkt ⑫ visar fallback-arbete för varje blocker?
- ✅ Punkt ⑬ visar vem som löser blockers?

### Risk-tråden
- ✅ Punkt ⑦ identifierar konkreta risker?
- ✅ Punkt ⑧ visar om risk påverkar kapacitet?
- ✅ Punkt ⑨ visar om risk ändrar prioritering?
- ✅ Punkt ⑪ visar hur sprintmål hanterar risk?
- ✅ Punkt ⑫ visar om risk-åtgärd är planerad?

### Realism-tråden
- ✅ Punkt ③-⑤ visar estimat per team?
- ✅ Punkt ⑧ visar totalt behövda timmar vs tillgängliga?
- ✅ Punkt ⑨ visar Must/Next/Later kategorisering?
- ✅ Punkt ⑪ visar sprintmål baserat på denna kapacitet?
- ✅ Punkt ⑫ visar plan-bedömning (🟢/🟡/🔴)?

**Om en rad inte är checkad → röda tråden är bruten.**

---

## DEL 7: EXEMPEL PÅ RÖDA TRÅDAR I ACTION

### Exempel 1: ARBETE-TRÅDEN denna vecka

```
① SEDAN FÖRRA MÖTET
  ✅ PR #90 Login (Zaida)
  ✅ PR #95 Design system (Björn)

③ FRONTEND TEAM — Var är vi?
  | #87 – Tests | Zaida | 🟡 PR open | ✓ | ◐ | ? | ✕ | PR #104
  | #89 – Risk Calculation | Erik | 🟡 Open | ✓ | ✓ | ◐ | ✕ | 5 commits

⑫ PLANERINGSKONTROLL
  🟡 Tight — två issues (#87, #89) behöver reviews denna vecka
  
  Nästa arbete:
  1. #87 – Tests (Zaida) — Review denna vecka innan merge
  2. #89 – Risk Calculation (Erik) — Tester denna vecka

⑬ ACTIONS
  ☐ Zaida: Begär review på PR #104 (onsdag)
  ☐ Erik: Kör tester på #89 (tisdag)
  ☐ Frontend lead: Uppdatera PR-status på Board efter mötet
```

**Röd tråd är tydlig: Förra veckan → pågår denna vecka → nästa steg**

### Exempel 2: RISK-TRÅDEN denna vecka

```
⑦ RISKER
  🟠 API-kontrakt är inte låst → Frontend kan inte starta
     Sannolikhet: Medel
     Åtgärd: Lås kontrakt på mötet (punkt ⑩)

⑧ KAPACITET
  Frontend: 40h tillgängliga
  Behöver: 48h (inklusive integrations-buffert)
  → Överbelastad om API-kontrakt inte löses snabbt

⑨ PRIORITERING
  MUST: API-kontrakt (löser risk, frigör Frontend)
  MUST: Tester för #87 (blockerar merge)
  NEXT: Dashboard-UI (#89)

⑪ SPRINTMÅL
  "Vid slutet av veckan ska API-kontrakt vara låst
  och Frontend kunna börja integration-tester"
  (= hanterar risk + möjliggör nästa vecka)

⑫ PLAN-KONTROLL
  Förslag: Prioritera API-kontrakt före dashboard-UI
  Anledning: Minskar risk från medel till låg
  
  Board-förslag: Flytta #87 och #89 upp i prioritet
```

**Röd tråd är tydlig: Risk → kapacitet-påverkan → prioritering-justering → sprintmål → plan-justering**

---

## RESULTAT

**Med denna struktur:**
- ✅ Mötet vet alltid vad som kommer nästa
- ✅ Samma struktur varje vecka = lätt att följa
- ✅ Röda trådar visar varför vi gör vad vi gör
- ✅ Inget viktigt information går förlorat
- ✅ Mötet kan fokusera på INNEHÅL, inte form

