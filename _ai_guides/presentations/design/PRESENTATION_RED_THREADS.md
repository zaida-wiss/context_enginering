---
name: presentation_red_threads
description: Röda trådar genom presentationen — arbete, blockers, risker, kapacitet — kontinuerliga trådar som binder slidorna ihop
metadata:
  type: reference
  critical: true
  version: 1.0
---

# 🧵 PRESENTATION RED THREADS — Röda Trådar som Binder Slidorna Ihop

**Denna fil visar de fyra huvudsakliga röda trådar som löper genom HELA presentationen från ① till ⑭.**

**En röd tråd bruten = presentationen är INKOMPLETT.**

---

## DEL 1: RÖDA TRÅDAR (De fyra huvudsakliga)

### 🔗 TRÅD 1: ARBETET ("ARBETE-TRÅDEN")

```
① Vad blev gjort förra veckan?
  ↓
③-⑤ Vad pågår denna vecka?
  ↓
⑧ Kan vi klara det? (kapacitet)
  ↓
⑪ Sprintmål (baserat på arbets-kapacitet)
  ↓
⑫ Är planen realistisk för detta arbete?
  ↓
⑬ Vem jobbar på vad härnäst?
```

**Röd tråd:** Från förra veckas resultat → denna veckas plan → nästa veckas arbete

**Varför:** Mötet måste förstå: "Vi gjorde X förra veckan, vi gör Y denna vecka, nästa vecka gör vi Z"

---

### 🚧 TRÅD 2: BLOCKERS ("HINDER-TRÅDEN")

```
③-⑤ Varje team rapporterar: "Vi väntar på..."
  (Väntar på review, väntar på backend, väntar på API-kontrakt)
  ↓
⑥ Övergripande bild: Vem blockerar vem? (Dependency chain)
  ↓
⑨ Prioritering: Gör vi något åt blockers?
  ↓
⑫ Plan-kontroll: Har vi fallback-arbete?
  ↓
⑬ Vem löser blockers innan nästa möte?
```

**Röd tråd:** Från lokal blocker → projektöversikt → handlingsplan → åtgärd

**Varför:** Mötet måste se: "Frontend är blockerad på backend, det påverkar allt, här gör vi åt det"

---

### ⚠️ TRÅD 3: RISKER ("RISK-TRÅDEN")

```
⑦ Identifierade risker från RISK-registret
  (🔴 Critical, 🟠 High, 🟡 Medium)
  ↓
⑧ Hur påverkar risk vår kapacitet?
  (Behöver vi buffert? Kan vi ställa om?)
  ↓
⑨ Ändrar risken vår prioritering?
  (Måste vi göra något FÖRST för att minska risk?)
  ↓
⑪ Sprintmål måste hantera denna risk
  ("Vid veckan slut ska vi ha mitigerat denna risk")
  ↓
⑫ Plan-kontroll: Är åtgärden planerad?
```

**Röd tråd:** Från risk-identifiering → plan-justering → verifiering

**Varför:** Mötet måste se: "Vi identifierade denna risk, det påverkar vad vi kan göra, här minskar vi risken"

---

### 💪 TRÅD 4: KAPACITET ("REALISM-TRÅDEN")

```
③-⑤ Varje team rapporterar estimat
  ("Frontend behöver 40 timmar denna vecka")
  ↓
⑧ Totalt: Kan vi klara allt?
  (Totalt 60h behövs, 55h tillgängliga → överbelastad)
  ↓
⑨ Prioritering: Vad MÅSTE vi välja?
  (Must/Next/Later kategorisering)
  ↓
⑪ Sprintmål baserat på faktisk kapacitet
  ("Vi kan göra Must + Next, Later skjuts till nästa vecka")
  ↓
⑫ Plan-kontroll: Är planen realistisk?
  (Checkar vi faktisk kapacitet? Finns buffert?)
```

**Röd tråd:** Från estimat → kapacitet → möjligt sprintmål → verifierad plan

**Varför:** Mötet måste se: "Vi är överbelastade, här prioriterar vi, här är en realistisk plan"

---

## DEL 2: VARNING-SIGNALER — Vad Saknas = Presentationen är INKOMPLETT

**Om dessa saknas, presentationen är FELAKTIG:**

### ❌ ARBETE-TRÅDEN bruten?

- ❌ Punkt ① är tom → vi vet inte vad som gjordes förra veckan
- ❌ Punkt ③-⑤ är tom → vi vet inte vad som pågår denna vecka
- ❌ Punkt ⑧ visar inte "Kan vi klara allt?" → vi vet inte om det är realistiskt
- ❌ Punkt ⑪ (sprintmål) är från förra mötet, inte HÄRLEDD från ①-⑩ → målet är inte verklighetsbaserat
- ❌ Punkt ⑬ är lösa idéer, inte konkreta GitHub-actions → mötet blir inte till arbete

### ❌ HINDER-TRÅDEN bruten?

- ❌ Punkt ③-⑤ visar inte "Vi väntar på..." för varje team → vi ser inte vilka som är blockerade
- ❌ Punkt ⑥ (blockers) saknas → vi ser inte helhetsbilden av beroenden
- ❌ Punkt ⑫ visar inte fallback-arbete för varje blocker → planen kan kollapsa om vi blir blockerade
- ❌ Punkt ⑬ nämner inte vem som löser blockers → ansvaret är oklart

### ❌ RISK-TRÅDEN bruten?

- ❌ Punkt ⑦ är tom → vi identifierar inte risker
- ❌ Punkt ⑧ visar inte hur risk påverkar kapacitet → vi tar inte hänsyn till risk vid planering
- ❌ Punkt ⑨ visar inte om risk ändrar prioritering → vi behandlar risk som bakgrundsinfo
- ❌ Punkt ⑪ (sprintmål) nämner inte risk → målet ignorerar grootste hot
- ❌ Punkt ⑫ visar inte om risk-åtgärd är planerad → vi vet inte vem som gör vad

### ❌ KAPACITET-TRÅDEN bruten?

- ❌ Punkt ③-⑤ visar inte estimat per team → vi vet inte hur lång tid arbetet tar
- ❌ Punkt ⑧ visar inte "Totalt behövda timmar vs tillgängliga" → vi kan inte se överbelastning
- ❌ Punkt ⑨ visar inte Must/Next/Later kategorisering → vi prioriterar inte
- ❌ Punkt ⑪ (sprintmål) är för stort för tillgänglig kapacitet → planen är omöjlig
- ❌ Punkt ⑫ visar inte plan-bedömning (🟢/🟡/🔴) → vi vet inte om planen är realistisk

---

## DEL 3: CHECKLIST FÖR RÖDA TRÅDAR

**Innan presentation avslutas, kontrollera:**

### ✅ Arbete-tråden (LÄS DETTA)
- ✅ Punkt ① visar faktiska merged PRs denna vecka?
- ✅ Punkt ③-⑤ visar pågående arbete denna vecka?
- ✅ Punkt ⑧ frågar "Kan vi klara allt detta?"?
- ✅ Punkt ⑪ (sprintmål) är härledd från ①-⑩, inte förutbestämt?
- ✅ Punkt ⑬ visar konkreta GitHub-actions (PR reviews, branches) med ägare?

### ✅ Hinder-tråden (LÄS DETTA)
- ✅ Punkt ③-⑤ visar "Vi väntar på..." för varje team?
- ✅ Punkt ⑥ visar övergripande bild av beroenden (dependency chains)?
- ✅ Punkt ⑫ visar fallback-arbete för varje blocker?
- ✅ Punkt ⑬ visar vem som löser blockers denna vecka?

### ✅ Risk-tråden (LÄS DETTA)
- ✅ Punkt ⑦ identifierar 🔴/🟠/🟡 risker konkret?
- ✅ Punkt ⑧ visar om risk påverkar kapacitet?
- ✅ Punkt ⑨ visar om risk ändrar prioritering?
- ✅ Punkt ⑪ visar hur sprintmål hanterar risk?
- ✅ Punkt ⑫ visar om risk-åtgärd är planerad?

### ✅ Kapacitet-tråden (LÄS DETTA)
- ✅ Punkt ③-⑤ visar estimat per team?
- ✅ Punkt ⑧ visar "Totalt behövda timmar vs tillgängliga"?
- ✅ Punkt ⑨ visar Must/Next/Later kategorisering?
- ✅ Punkt ⑪ visar sprintmål baserat på denna kapacitet?
- ✅ Punkt ⑫ visar plan-bedömning (🟢 Green / 🟡 Yellow / 🔴 Red)?

---

**Om en rad inte är checkad → röda tråden är bruten.**

---

## DEL 4: EXEMPEL PÅ RÖDA TRÅDAR I ACTION

### Exempel 1: ARBETE-TRÅDEN denna vecka

```
① SEDAN FÖRRA MÖTET
  ✅ PR #90 Login (Zaida) — merged 2026-09-13
  ✅ PR #95 Design system (Björn) — merged 2026-09-12

③ FRONTEND TEAM — Var är vi?
  | #87 Tests | Zaida | ◐ PÅG | feature/#87 | PR open awaiting review
  | #89 Risk Calculation | Erik | ◐ PÅG | feature/#89 | 5 commits denna vecka

⑧ KAPACITET
  Frontend: 40h tillgängliga denna vecka
  Pågår: #87 + #89 = 30h (tight men går)

⑪ SPRINTMÅL
  "Slutveckan ska #87 och #89 vara mergead och testade"
  (= möjligt baserat på kapacitet från ⑧)

⑬ ACTIONS
  ☐ Zaida: Begär review på PR #87 (onsdag 2026-09-15)
  ☐ Erik: Avsluta tester på #89 (tisdag 2026-09-14)
```

**Röd tråd är tydlig:** Förra veckan → denna vecka → nästa steg

---

### Exempel 2: RISK-TRÅDEN denna vecka

```
⑦ RISKER
  🟠 API-kontrakt är inte låst → Frontend kan inte starta integration
     Sannolikhet: Medel
     Påverkan: Backend startar sent, triggar frontend-omarbete
     Åtgärd: Lås kontrakt i möte (punkt ⑩)

⑧ KAPACITET
  Frontend: 40h
  Behöver: 48h (inklusive integrations-buffert för risk)
  Slutsats: Överbelastad OM risk håller

⑨ PRIORITERING
  MUST: Lås API-kontrakt (löser risk, frigör Frontend)
  MUST: Tester för #87 (blockerar merge)
  NEXT: Dashboard-UI (#89)

⑪ SPRINTMÅL
  "Vid slutet av veckan ska API-kontrakt vara låst
   och Frontend kunna börja integration-tester"
  (= hanterar risk, möjliggör nästa vecka)

⑫ PLAN-KONTROLL
  Bedömning: 🟡 Yellow (tight men går IF API-kontrakt löses)
  Åtgärd: Prioritera API-kontrakt före dashboard
  Fallback: Om kontrakt inte löses — switch till #81 (oberoende arbete)
```

**Röd tråd är tydlig:** Risk → kapacitet-påverkan → prioritering-justering → sprintmål → plan-justering

---

**Version:** 1.0  
**Status:** SOURCE OF TRUTH FÖR RÖDA TRÅDAR  
**Senast uppdaterad:** 2026-09-14
