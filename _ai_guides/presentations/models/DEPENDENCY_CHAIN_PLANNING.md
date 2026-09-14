---
name: dependency_chain_planning
description: Fas-baserad planering med blockerträd, risk-register och teamregler — bättre än "3 issues per person"
metadata:
  type: reference
  for_presentations: true
  applies_to: "Punkt ⑦ Beroenden & Blockers, Punkt ⑧ Prioritering & Scope"
---

# 🔗 DEPENDENCY CHAIN PLANNING — Fas-baserad Ordning

**Denna mall visar optimal arbetsordning baserad på blockers, inte på "fair distribution".**

**Huvudprincip:** Varje merge låser upp nästa steg. Målet är maximalt genomflöde för teamet, inte maximalt antal parallella issues.

---

## 🎯 STRUCTURE (ALLTID DENNA ORDNING)

### 1. VERIFIED DEPENDENCY CHAINS

```
Här dokumenteras de verkliga kedjorna i koden:

Data/Integration chain:
[Foundation issue] → [Dependent 1] → [Dependent 2]

Test chain:
[Test framework] → [Core tests] → [E2E tests]

UI/Responsive chain:
[Foundation] → [Secondary features]
```

**REGLER för denna sektion:**
- Baseras ENDAST på faktisk kodberoende (grep, git log, code review)
- Om två issues rör samma funktion/fil → de är beroende
- Om Issue B använder output från Issue A → A måste mergera först

### 2. RISK MATRIX

```
Risk                          | Nivå  | Vad kan hända?        | Åtgärd
------------------------------|-------|----------------------|--------
[Specific risk]               | 🔴    | [Konkret scenario]    | [Konkret åtgärd]
```

**Risk-nivåer:**
- 🔴 HÖG — Stoppar demo eller tvingar stor omarbete
- 🟠 MEDEL — Fördröjning eller extra timmar
- 🟡 LÅGNIVÅ — Möjlig, men mindre påverkan

### 3. PHASED ROLLOUT (Fas 1-6)

**Format: Tabell med Fas, Person A, Person B, Person C, Varför**

```
Fas     | Person A      | Person B      | Person C      | Varför denna ordning?
--------|---------------|---------------|---------------|-------------------------------------------
1. Nu   | [Issue 1]     | [Issue 2]     | [Issue 3]     | Tre separata områden. #2 låser upp mycket.
2. Merge| [Issue 4]     | [Issue 5]     | [Issue 6]     | #5 kräver #2 merged. #6 oberoende.
3. Stab | [Issue 7]     | [Issue 8]     | [Issue 9]     | Fokus på stabilisering före nästa.
```

**KRITISKT:**
- Endast EN issue per person per fas (max 1 active + 1 queued)
- Nästa fas startar INTE innan fas N är merged och develop är uppdaterad
- Om blocker uppstår → parallel work på oberoende issues, aldrig på beroende

### 4. TEAMREGEL (ALLTID DENNA)

```
🚨 TEAMREGEL:

Ingen börjar nästa issue innan dependency är merged i develop.

Exempel ordning för Person A:
  1. [Issue 1] → merge → pull develop
  2. [Issue 2] (depender på Issue 1) → merge → pull develop
  3. [Issue 3] (depender på Issue 2) → merge

Innan varje ny issue:
  ☐ Pull/rebase mot aktuell develop
  ☐ Kontrollera öppna PRs (vem rör samma komponenter?)
  ☐ Bekräfta att dependency är faktiskt merged (inte bara "nästan klar")
```

---

## 📋 PRESENTATION FORMAT (för slide)

### Slide Format för Punkt ⑦ (Beroenden & Blockers)

```
📝⑦ BEROENDEN & BLOCKERS — Fas-baserad Ordning

🔗 VERIFIERADE KEDJOR:

Data/Integration:
  [Foundation issue] → [Dependent 1] → [Dependent 2]

Test:
  [Test framework] → [Core tests] → [E2E tests]

⚠️ RISK-REGISTER:

| Risk | Nivå | Åtgärd |
|------|------|--------|
| [Risk] | 🔴 | [Action] |

📅 PLANERAD ORDNING:

Fas 1 (Nu)     | Person A: [Issue] | Person B: [Issue] | Person C: [Issue]
Fas 2 (Merge)  | Person A: [Issue] | Person B: [Issue] | Person C: [Issue]
Fas 3+ (Stab)  | ...               |                   |

🚨 TEAMREGEL: Max 1 active issue per person. Nästa fas startar när fas N är merged.
```

### Slide Format för Punkt ⑧ (Prioritering & Scope) — Baserat på Chains

```
📝⑧ PRIORITERING & SCOPE — Chain-baserat

🔴 KRITISKA VÄGEN (måste lösa först denna vecka):
  [Foundation issue #XX] (Person A)
  [Foundation issue #YY] (Person B)
  [Foundation issue #ZZ] (Person C)

🟠 SEKUNDÄR (startar när kritiska är mergade):
  [Dependent issue #AA] (Person A)
  [Dependent issue #BB] (Person B)
  [Dependent issue #CC] (Person C)

🟡 OPTIONAL (om extra tid):
  [Lower-priority issue]
  [Polish/optimization]
```

---

## 🔄 HUR AI ANVÄNDER DENNA MALL

**Innan presentation:**

1. **Greppa beroendestruktur** från GitHub + kod:
   ```
   Vilka issues refererar till varandra?
   Vilka issues rör samma filer/komponenter?
   Vilka är issue-blockers i GitHub?
   ```

2. **Identifiera kedjor:**
   ```
   Chain 1: #A → #B → #C
   Chain 2: #D → #E → #F
   Chain 3: #G (independent)
   ```

3. **Analysera risker:**
   ```
   För varje chain: Vad kan gå fel?
   - Mergekonflikter? (parallell development samma fil)
   - API-mismatch? (frontend väntar på backend)
   - Test-failure? (tester skrivs innan stabilisering)
   - WIP-explosion? (för många öppna PRs)
   ```

4. **Skapa fas-plan:**
   ```
   Fas 1: Foundation issues (låga konfliktrisker, låser upp mycket)
   Fas 2: Dependents (startar när Fas 1 merged)
   Fas 3+: Secondary/Polish
   ```

5. **Presentera med teamregel:**
   ```
   "Max 1 active + 1 queued per person.
    Nästa issue startar när dependency är merged och develop uppdaterad."
   ```

---

## 🚨 KRITISKA REGLER FÖR DENNA MALL

**ABSOLUT:**
- ❌ Aldrig "vi lägger 3 issues per person och de löser det parallellt"
- ✅ Alltid "kedjor med verified beroenden → fas-baserad ordning"

**TRANSPARENS:**
- Varje risk MÅSTE ha konkret åtgärd (inte vag)
- Varje fas MÅSTE ha tydlig "vad triggar nästa fas?" (merged, tested, stabilized)
- Varje person MÅSTE veta: vilken issue > vilken nästa?

**TEAMREGEL:**
- Denna regel är INTE optional — det är vad som förebygger mergekonflikter + omarbete
- Presenteras alltid explicit i punkt ⑦ eller ⑧

---

## 📝 EXEMPEL (Men aldrig i presentations-mallen!)

**Frontend kedjor denna vecka:**

```
Fas 1 (Nu):
  Zaida: #87 Test foundation (låga risker, låser upp #88/#89)
  Tomac: #43 API client + mock (låg konflikt, låser upp #82/#83)
  Björn: #81 Linked allocation inputs (egen komponent, låg risk)

Fas 2 (Merge + develop update):
  Zaida: #88 Critical interaction tests (testar stabila delar först)
  Tomac: #82 usePortfolio (kräver #43 merged)
  Björn: #85 Responsive header (oberoende, kan parallelleras)

Fas 3 (Efter #81 + #43 merged):
  Zaida: Fortsätt #88 (anpassa efter nytt dataflöde)
  Tomac: #83 saveAllocation (NOW kan starta utan #81 konflikt)
  Björn: #86 Responsive dashboard (baseras på #85)

Risk: #43 + JWT från backend inte helt klart
  → Åtgärd: Mock-adapter PRIORITERAS för att inte blockera #82/#83
```

---

**Version:** 1.0  
**Status:** MALL FÖR PRESENTATIONER  
**Senast uppdaterad:** 2026-09-14
