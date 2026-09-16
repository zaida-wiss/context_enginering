---
name: slide_detail_spec
description: Exakt innehål för varje slide i presentationen (①-⑭) — format, kolumner, regler
metadata:
  type: critical_specification
  version: 1.0
---

# 📊 SLIDE DETAIL SPECIFICATION — Exakt Innehål per Slide

**Denna fil säger EXAKT vad varje slide ska innehålla — ingen gissning.**

## 🎨 VISUAL IMPLEMENTATION — AUTHORITY

**Do NOT define colors, typography, borders, spacing or card geometry here.**

All visual implementation — colors, fonts, spacing, contrast, borders, background fills, corner radius — 
MUST come from [`VISUAL_DESIGN_MANDATORY.md`](../design/VISUAL_DESIGN_MANDATORY.md).

This file defines **content only** (what data goes where, how it's structured).

**Authority hierarchy:**
1. **VISUAL_DESIGN_MANDATORY.md** — ALL visual rules (colors, fonts, spacing, borders)
2. **ACCESSIBILITY_NEURODIVERSITY.md** — WCAG 2.2 AA boundaries (cannot be violated by visual choices)
3. **This file (SLIDE_DETAIL_SPEC.md)** — Content structure and data fields ONLY

---

🔗 **VISUAL REFERENCE:** Se [`TEMPLATE_REFERENCE.html`](TEMPLATE_REFERENCE.html) för exempel-layouts.

Se [PRESENTATION_STRUCTURE.md](../structure/PRESENTATION_STRUCTURE.md) för punkt-nivå-overview.

---

## 🚨 KRITISK REGEL — MÖTESPUNKTS-SYMBOLER

**VARJE slide-rubrik MÅSTE börja med mötespunkts-symbolen så det är OMEDELBAR VISUELL klar vilken mötespunkt sliden tillhör.**

```
❌ FEL:   "Avklarat sedan förra mötet — Frontend"
✅ RÄTT:  "① Avklarat sedan förra mötet — Frontend"

❌ FEL:   "Aktuell status"
✅ RÄTT:  "② Aktuell status"

❌ FEL:   "Frontend"
✅ RÄTT:  "③ Frontend"
```

**REGLER (Mechanical — no variation):**
- Symbolen måste vara FÖRST i rubriken (no exceptions)
- Exakt två mellanslag mellan symbol och rubrik-text
- Samma symbol för alla sub-slides (①A, ①B, ①C använder alla ①)
- Font: 28pt BOLD (per VISUAL_DESIGN_MANDATORY.md, never smaller, never different)

**NOTE:** These are rendering rules for AI, not content to display.

---

## 📝⓪ FRAMSIDA (1 slide, mandatory)

**REQUIRED CONTENT:**
- Meeting date: "Veckomöte · [DATE, e.g. "21 september 2026"]"
- Team identifier: "Avanza Team 1"
- Reporting period: "Rapportperiod: [START DATE] – [END DATE]"

**WEEKLY FOCUS (primary content):**
- Sprint goal or weekly focus (if defined)
- Key deliverable this week
- Any critical deadline or milestone

**RELEVANT PL CONVERSATION TOPICS (if applicable):**
- Topics to discuss with Project Lead
- Source: Extracted from schedule/timeline (NOT meeting notes)
- Example: "Release candidate criteria by Friday" / "CTO demo readiness"

**DATA INTEGRITY FOOTER:**
- Data source verification: "✅ [number] sources verified"
- List of verified sources:
  - ✅ GitHub (commits, PRs, issues per-person)
  - ✅ Team roster (7 members)
  - [Other sources if used]
- Status: Green checkmark if all sources OK, yellow warning if fallback used, red if incomplete

**VISUAL NOTES:**
- Large, centered meeting title
- Significant whitespace
- Weekly focus as main message
- Data provenance footer proves integrity
- Follows ACCESSIBILITY_NEURODIVERSITY.md + VISUAL_DESIGN_MANDATORY.md for layout

**CRITICAL: Do NOT include:**
- ❌ NPF/design explanations ("Färg + symbol + text...")
- ❌ Design methodology descriptions
- ❌ Process explanations
- Focus on: Sprint goal, deadline, and what PL wants to discuss

---

## 🎯 CONDITIONAL SLIDE RULE — When slides may be omitted

**A slide MAY be omitted only if its dataset is empty, with these requirements:**

1. **Dataset must be verified empty** (not just "no data found")
   - Explicit count: 0 verified items
   - Record omission reason
   
2. **Audit must explicitly record:**
   ```
   ①B omitted — 0 verified collection-branch deliveries (dataset empty)
   ①D omitted — 0 verified cross-team active items (dataset empty)
   ```
   
3. **Forbidden:** Omitting a slide because generator chose to skip it
   - Every slide must have explicit decision: SHOW or OMIT (with reason)
   - Default: SHOW (even if empty, show "no items this period")

---

## 📝① AVKLARAT SEDAN FÖRRA MÖTET

**Point ① shows ONLY completed work during reporting period.**

This mötespunkt is divided into phases (①A, then ①B-①E in team context later):

---

## 📊 ①A — MERGADE PR:ER SEDAN FÖRRA MÖTET (1+ slides, split as needed)

**PURPOSE:**
Global overview of ALL work merged to develop, displayed chronologically.
Shows what was actually delivered to develop, regardless of team.
Does NOT include work merged to team collection branches (that goes to ①B).

**CONTENT REQUIREMENTS:**
- All PRs merged TO DEVELOP during REPORTING_PERIOD (not to collection branches)
- Sort chronologically (oldest first)
- Chronological order CONTINUES across slides if >12 cards
- Include cross-team PRs in chronological order
- Show assignee + GitHub login for each

**CARD DATA FIELDS (showing ACTUAL WORK DONE, not just assignment):**
- PR number + title
- **Developed by:** [Name(s)] (@github_login) — verified from:
  1. Commit authors in PR (primary)
  2. Issue assignee if commits missing (fallback)
  3. PR author as last resort (weak signal)
- **Reviewed by:** [Name] (@github_login) — who actually approved (not requested_reviewers)
- **Merged by:** [Name] (@github_login) — who merged to develop
- Merged date

**PAGINATION (MANDATORY):**
- Slide ①A shows MAX 6 cards per physical slide (3 columns × 2 rows)
- If merged PR count > 6:
  - Create continuation slide ①A-2 (preserves ① symbol, continues chronologically)
  - Continue ①A-3, ①A-4 if needed
  - FORBIDDEN: shrink cards, reduce font below 12pt, place >6 on one slide
  - If merged PR count <= 6: single ①A slide
- Chronological order continues unbroken across ①A pages

**CRITICAL:**
- Show actual code contributors (commit authors > assignee > pr_author)
- PR author is fallback only, NOT the definition of "developer"
- Show actual reviewers (who approved), NOT just requested_reviewers
- All three fields must be filled (if missing, show "?" or note "no review yet")
- This demonstrates team collaboration (not just individual work)

**VISUAL IMPLEMENTATION:**
Do NOT define colors, grid, layout, or badge styling here.
All visual rules are in [`VISUAL_DESIGN_MANDATORY.md`](../design/VISUAL_DESIGN_MANDATORY.md):
- Grid dimensions: 3 × 2 (max 6 cards per slide)
- Team colors (borders, badges)
- Card layout and spacing
- Legend

This file defines WHAT goes on the slide. VISUAL_DESIGN_MANDATORY defines HOW it looks.

---

## 🟢 TEAM MEMBER CAPACITY — UNIVERSAL RULE

If a team member has NO verified active issue or PR:

**Show:**
"[Name] — Ny issue eller tillgänglig för hjälp i [teamet]"

**This means:**
- Can take next prioritized issue
- Can help a team colleague
- Can pair or review
- Can help unblock someone
- Is available for support/ramp-up

**This is capacity information, NOT performance assessment.**

**CRITICAL: Review is work, not "available":**
- If a person is actively reviewing PRs → show them as "Reviewing [PR#] for [person]"
- Do NOT show reviewers as "Ny issue eller tillgänglig för hjälp"
- Review work is actual work and should be visible
- Only show "available" if the person has NO active reviews or PRs

**DO NOT:**
- Write "Ingen aktivitet" (implies inactivity)
- Write "Inget arbete" (implies no work)
- Use red warning
- Use phrasing that implies low performance
- Hide reviewers as if they're "idle"

**Visual style:**
- Neutral gray or blue color
- Symbol: ○ or ↔
- Text: "Ny issue eller tillgänglig för hjälp"

Example on team slide later:
```
○ Erik — Ny issue eller tillgänglig för hjälp i Backend
○ Pär — Ny issue eller tillgänglig för hjälp i Native
```

---

## 📊 ①B — MERGAT TILL TEAM COLLECTION BRANCHES (om relevant, 0-1 slides)

**PURPOSE:**
Show work that has been merged to team collection branches (e.g., Java-Development-Environment for Backend)
but NOT yet merged to develop. This represents work-in-progress that's committed to a team branch.

**WHEN TO SHOW:**
- Only if there are PRs merged to collection branches during REPORTING_PERIOD
- If no such PRs, skip this slide

**CONTENT:**
- PRs merged to [Team Collection Branch] (e.g., Java-Development-Environment, C/C++-Native)
- Sort chronologically (oldest first)
- Show same fields as ①A: Developed by | Reviewed by | Merged to [Branch] | Date

**CRITICAL (no double-counting):**
- Do NOT show work that's already on ①A (merged to develop)
- This slide shows work that's on a team branch but not yet on develop
- It's progress, but not yet delivered to develop

---

## 📊 ①C — PÅGÅR DENNA VECKA: FRONTEND, BACKEND, NATIVE

**PURPOSE:**
Shows active work by team. Three separate columns, each team's pågår issues.
Does NOT include cross-team work (that goes to ①C).

**CONTENT REQUIREMENTS:**
- Active (open) issues assigned to team members
- One column per team (Frontend | Backend | Native)
- Max 4 rows per column = max 12 cards total
- Include issue number, branch, latest commit timestamp
- Exclude cross-team work (goes to ①D)

**CARD DATA FIELDS:**
- Issue number + title
- Branch name
- Latest commit timestamp + author name
- Assignee name (@github_login)
- Code inspection notes (if issues detected)

**DATA SOURCE:**
- Open issues + matching active branches
- Recent commits (last 7 days)
- Per team via TEAM_ROSTER.md
- Latest commit timestamp from DATA_ACQUISITION_CONTRACT.yaml

**VISUAL IMPLEMENTATION:**
Do NOT define colors, grid layout, or spacing here.
All visual rules are in [`VISUAL_DESIGN_MANDATORY.md`](../design/VISUAL_DESIGN_MANDATORY.md):
- Column structure (3 columns)
- Team border colors
- Card dimensions and spacing
- How to display commit timestamp

This file defines WHAT goes on the slide. VISUAL_DESIGN_MANDATORY defines HOW it looks.

---

## 📊 ①C — PÅGÅR DENNA VECKA: CROSS-TEAM

**PURPOSE:**
Shows active cross-team work (affects multiple teams).
Separate slide to keep team columns clean and highlight cross-team coordination.

**CONTENT REQUIREMENTS:**
- Active (open) issues affecting multiple teams
- Max 12 cards per slide
- Show which teams are involved in each issue
- Include branch names and latest commit timestamps
- Sort by activity (most recent first)

**CARD DATA FIELDS:**
- Issue number + title
- Teams involved
- Branch name
- Latest commit timestamp + author name
- Assignee name (@github_login)

**DATA SOURCE:**
- Open issues marked as cross-team or affecting multiple teams
- Latest commit timestamp from DATA_ACQUISITION_CONTRACT.yaml

**VISUAL IMPLEMENTATION:**
Do NOT define colors, grid layout, or border styling here.
All visual rules are in [`VISUAL_DESIGN_MANDATORY.md`](../design/VISUAL_DESIGN_MANDATORY.md):
- Grid dimensions: 3 × 2 (max 6 cards per slide)
- Cross-team border color and styling
- Card layout and spacing

This file defines WHAT goes on the slide. VISUAL_DESIGN_MANDATORY defines HOW it looks.

---

## 📝 ①D-①E — HINDER, RISKER, BLOCKERS (deferred to team context)

**Planerat, blockers/risker → shown during detailed team slides later.**

**Structure: ①A-①D contain completed/merged work, pågår work, and collection-branch progress.**

---

## 📝 ① AVSLUT — BESLUT (0-1 slides, conditional)

### SLIDE ① BESLUT SEDAN FÖRRA MÖTET

**PURPOSE:**
Help team see what decisions have been made (documented in docs/BESLUT.md)
and discover what decisions should perhaps be documented (candidates from GitHub).

**TWO SECTIONS:**

#### Section A: VERIFIERADE BESLUT

Show confirmed decisions from docs/BESLUT.md during reporting period.

**Format:** Vertically stacked compact cards, one decision per card

```
✓ Teststrategi
Vitest + RTL används för frontendtester.
Dokumenterat: 15 september

✓ API-kontrakt
JWT skickas via HttpOnly-cookie.
Dokumenterat: 12 september
```

**RULES:**
- Only show if 1+ decisions exist in docs/BESLUT.md
- Max 4 decisions per slide
- If no decisions: omit Section A

#### Section B: FÖRSLAG PÅ BESLUT ATT DOKUMENTERA (optional)

Show 2-3 decision candidates. These are things GitHub/code patterns suggest
the team has already adopted or decided, but isn't yet documented as formal decisions.

Format helps team learn: "What makes something a real decision?"

```
? Backend-integrationsflöde
Ska Backend alltid integrera i Java-Development-Environment
innan merge till develop?

Underlag: Flera säkerhets-PR:er följer detta mönster.
Varför dokumentera? Påverkar hur vi reviewar och planerar.
```

**RULES FOR CANDIDATES:**
- Show ONLY if evidence suggests team has adopted the practice
- NEVER claim a decision is made — use "Förslag på beslut" (suggestion)
- Evidence must be from: GitHub PRs, code patterns, or team workflow
- Max 2-3 suggestions per presentation
- If no candidates: omit Section B
- Include: question form, evidence, why it matters

**CANDIDATE CRITERIA (what AI should suggest):**

✅ Suggest as decision candidate if it:
- Affects future implementation
- Establishes reusable rule
- Selects between alternatives
- Defines interface or contract
- Changes team workflow
- Creates dependency/order between work
- Establishes quality/security/testing practice

❌ Do NOT suggest if it's only:
- A single commit
- Ordinary implementation detail
- Task completion or status
- Temporary debugging change
- One-off code review

**SLIDE OMISSION:**
- If no verified decisions AND no candidates: omit entire slide
- Record omission in audit: "Slide ① BESLUT omitted — 0 decisions + 0 candidates"

**VISUAL IMPLEMENTATION:**
- Verified decisions: green check + date
- Candidates: blue question mark + evidence link
- Both: soft cards, centered text, responsive height
- See VISUAL_DESIGN_MANDATORY.md for card styling

---

## 📝② NULÄGE & DEADLINE (1 slide)

### SLIDE ②A: Nuläge + Deadline Tracker & Risk

**FORMAT: Vertically stacked compact priority cards**

Use small vertically-stacked cards (NOT wide horizontal bands).
Each card shows one ranked priority item. Cards grow vertically to fit content.

**INNEHÅL - Vertically ranked cards:**

```
    1️⃣ KRITISK — [MILESTONE_A]
       Idag 14:00

    VAD: [TEAM_A] + [TEAM_B] fastslår [DECISION]
    VARFÖR: Låser upp [FEATURE_1], [FEATURE_2]
    STATUS: ⏳ Ingen aktivitet än
    RISK: [N] dagar försening om ej klart
    ACTION: [PERSON] möte 14:00


    2️⃣ HÖGT — [MILESTONE_B]
       Imorgon

    VAD: Dokumentation i issue #XX
    VARFÖR: [TEAM_C] behöver för [PHASE]
    STATUS: ⏳ Beror på möte idag
    RISK: Kan försena nästa fas
    ACTION: Vilka kan assistera [PERSON]?


    3️⃣ MEDEL — CTO-demo denna vecka

    VAD: Feature-complete eller fallback
    VARFÖR: Demo är schemalagd
    STATUS: 🟢 80% (Frontend), 60% (Backend)
    BUFFER: 1 dag kvar
    ACTION: Fokusera på blockers
```

**REGLER:**
- **Layout:** Vertically stacked compact cards, one per ranked item
- **Ranking:** 1️⃣ = highest urgency, 2️⃣ = next, 3️⃣ = next
- **Each card:** Rank | Priority level | Deadline | VAD | VARFÖR | STATUS | RISK | ACTION
- **Card behavior:** Grows vertically to fit all content (no clipping)
- **Text alignment:** All text centered inside each card
- **STATUS-märken:** ⏳ = waiting, 🟢 = on track, 🔴 = behind, 🟠 = risk
- **ACTION:** Konkret nästa steg med ÄGA och TIDRAM

**MÅSTE innehålla:**
- ✅ Progress % per team
- ✅ Vilka deadlines vi har (prioriterade)
- ✅ VAD varje deadline innebär (inte bara datum)
- ✅ VARFÖR deadline är viktig (påverkan)
- ✅ Nuläge mot deadline (STATUS)
- ✅ RISK om vi missar (KONKRET konsekvens)
- ✅ KONKRET nästa handling (ACTION)

**FÅR INTE innehålla:**
- ❌ Detaljerade issue-listor (se punkt ③-⑤)
- ❌ Historiska data ("förra veckan var vi...")
- ❌ Försäljnings-språk ("Vi är på vägen!")
- ❌ Vaga risks ("vi kan bli sen") — måste vara KONKRET
- ❌ Vaga actions ("vi ska jobba på det") — måste ha ÄGA och TIDRAM

**FOOTER:** `Källa: GitHub issues + Project Board + Sprint planning ✅`

---

## 🎯 TEAM DETAIL LAYOUT (③ Frontend, ④ Backend, ⑤ Native)

**All team detail slides use identical card layout:**

- Vertically stacked compact cards (NOT wide horizontal bands)
- One work item per card
- Text centered horizontally inside every card
- Card height adapts to content (no clipping allowed)
- Minimum height, let cards expand vertically
- Same spacing and typography hierarchy across all teams

**Card structure (centered):**
```
    ✅ #93 · PR #95
    SQL-injection fix

    Mergat till
    Java-Development-Environment

       Rasha
    Review: Erik
    Merge: Erik
```

**See VISUAL_DESIGN_MANDATORY.md for complete TEAM DETAIL CARDS rules.**

---

## 📝③ FRONTEND (2-3 slides per mötespunkt)

### MÖTESPUNKT ③ — FRONTEND: DENNA SPRINT & NULÄGE

🚨 **KRITISK: Denna mötespunkt visar ALLA issues denna sprint — både kommande backlog + pågående arbete + blockers + risker**

🚨 **NO POWERPOINT TABLES** — Use visual cards/rows instead (NPF requirement)

**FORMAT:** Visuella status-cards klassificerad på dependencies + status

**STRUKTUR:**

```
PÅGÅR DENNA VECKA (fortsätt från senaste mötet):
  #XX | [FEATURE_A] | [PERSON_A] | ◐ PÅG | Blocker: [FEATURE_B] (#YY)
  #YY | [FEATURE_C] | [PERSON_B] | ◐ PÅG | Blocker: Backend API (#ZZ)

KOMMANDE DENNA SPRINT (från backloggen):
  #AA | [FEATURE_D] | [PERSON_C] | ⏳ BACKLOG | Beror på: #XX
  #BB | [FEATURE_E] | ?? | ⏳ BACKLOG | Beror på: #XX (review)
  #CC | [FEATURE_F] | ?? | ⏳ BACKLOG | Beror på: External blocker

INTE TILLDELAT (Förslag baserat på tidigare arbete):
  [PERSON_X]: [FEATURE_G] — nära tidigare arbete denna område
  [PERSON_Y] + [PERSON_Z]: [FEATURE_H] — pairing för snabbare progress
  [PERSON_W]: Flexibel support — täcka blockers om de dyker upp
```

**KOLUMNER:** Issue # | Titel | Assignad | Status | Blocker/Beroenden

**STATUS-MÄRKEN:**
- ✓ DONE (redan mergad denna vecka)
- ◐ PÅG (aktivt arbete nu)
- ⏳ BACKLOG (väntar på detta sprint, ej startat ännu)
- ?? UNASSIGNED (vi föreslår assignee baserat på tidigare mönster)

**REGLER:**
- Sortera på DEPENDENCIES (vad måste göras först?)
- Visa ALLA issues denna sprint, klassificerat per status
- **Assignad = vem som ÄGer arbetet**
  - Om redan assignad i GitHub: visa namn
  - Om INTE assignad: visa "??" + förslag baserat på tidigare commits
- "Blocker" = vad väntar vi på (issue-nummer eller PR)
- **BEROENDEN MÅSTE VISAS** — använd "Beror på: #X" för clarity

**MÅSTE innehålla:**
- ✅ Issue-nummer (#XX)
- ✅ Titel (2-5 ord)
- ✅ Assignad (namn eller "??" + förslag)
- ✅ Status (✓/◐/⏳)
- ✅ Blocker/Beroenden (tydligt vilken issue som blockerar vilken)
- ✅ **ALLA 7 team-medlemmar — vem gör vad eller "pairing X+Y"**

**FÅR INTE innehålla:**
- ❌ Commit-hash
- ❌ PR-nummer (det är issues vi visar, inte PRs)
- ❌ Estimat i timmar
- ❌ Issues från förra veckan som redan är klara
- ❌ Vaga assignee-förslag ("kanske [PERSON_X]")

**DATA-SOURCES:**
- 📊 **Pågår:** GitHub issues with status "In Progress" + branches with commits senaste 7 dagar
- 📊 **Backlog denna sprint:** GitHub issues labeled "Sprint-X" eller Project Board "Sprint" column
- 📊 **Assignee-förslag:** Git blame + git log för varje issue-kategori (vem jobbade senast på liknande?)
- 📊 **Beroenden:** DEPENDENCY_CHAIN_PLANNING.md klassificering

**FOOTER:** `Källa: GitHub issues + Project Board + Git history ✅ | Assignee-förslag baserat på tidigare arbete`

---

### SLIDE ③B: Frontend — Operativ handlingsplan (om behövs)

**FORMAT:** Numrerad lista

**INNEHÅL:**
```
NÄSTA STEG:
1. [PERSON_A] ↔ Backend ([PERSON_B]): API-kontrakt möte idag 14:00
2. [PERSON_C] pairing med [PERSON_D]: Testa [FEATURE] mot mock-API
3. [PERSON_E]: Code review #XX innan merge
```

**REGLER:**
- Numrerad lista (1, 2, 3...)
- Högst 3-5 actions
- Format: `Namn: Vad, när` eller `Person A ↔ Person B: Möte vad`
- Inkludera tid om relevant ("idag 14:00", "imorgon")

**MÅSTE innehålla:**
- ✅ Vem gör vad
- ✅ Nästa 24-48 timmar
- ✅ Tidsram om kritiskt

**FÅR INTE innehålla:**
- ❌ Generell planering ("vi ska jobba på...")
- ❌ Redan gjorda saker

**FOOTER:** `Baserat på punkt ③A status`

---

### SLIDE ③C: Frontend — Beroenden & Risker (om behövs)

**FORMAT:** Text med färgade markeringar

**INNEHÅL:**
```
VÄNTAR PÅ:
  🔴 Backend API-definition för #XX, #YY (blockerar Frontend #AA)
  🟠 Möjlig: [EXTERNAL_RESOURCE] från [TEAM/PERSON]

RISK:
  🟠 Om [BLOCKER] inte klart [WHEN] → [DAYS] dagar försening på [FEATURES]
```

**REGLER:**
- 🔴 = kritisk, 🟠 = måttlig
- "Väntar på" = externa dependencies
- "Risk" = vad kan gå fel denna vecka

**FÅR INTE innehålla:**
- ❌ Gamla problem från förra veckan
- ❌ Spekulationer ("kanske blir det...")

---

## 📝④ BACKEND (1-3 slides)

### SLIDE ④A: Backend — Denna sprint

**FORMAT:** Visuella status-cards (identisk som ③A — NO POWERPOINT TABLES)

**KOLUMNER:** Issue # | Titel | Assignad | Status | Blocker

**REGLER:** (identiska som ③A)

---

### SLIDE ④B: Backend — API-kontrakt-status (om behövs)

**FORMAT:** Visuella status-cards med kolumner (NO POWERPOINT TABLES)

**KOLUMNER:**
| Endpoint | Status | Frontend blockar? | Nästa |
|----------|--------|-------------------|-------|
| [ENDPOINT_A] | ✅ Dokumenterad | Nej | Testning |
| [ENDPOINT_B] | 🟠 I review | JA (#XX-#YY) | [PERSON] review idag |

**REGLER:**
- Status: ✅ = klart, 🟠 = in progress, ❌ = ej påbörjad
- "Frontend blockar?" = JA/Nej (med issue-nummer om JA)
- "Nästa" = nästa steg (en mening)

---

### SLIDE ④C: Backend — Operativ handlingsplan (om behövs)

**FORMAT:** Numrerad lista (samma som ③B)

---

## 📝⑤ NATIVE (1-3 slides)

### SLIDE ⑤A: Native — Denna sprint

**FORMAT:** Visuella status-cards (identisk som ③A — NO POWERPOINT TABLES)

---

### SLIDE ⑤B: Native — JNA-kontrakt-status (om behövs)

**FORMAT:** Text

**INNEHÅL:**
```
VÄNTAR PÅ:
  🔴 Backend API-kontrakt för #XX

MÖJLIG SUPPORT:
  [PERSON_N] kan stödja [TEAM] denna vecka medan väntar
```

---

## 📝⑥ BLOCKERS & DEPENDENCIES (1-2 slides)

### SLIDE ⑥A: Blockerträd — Alla kritiska kedjor

**FORMAT:** Visuell dependency-diagram med noder och pilar

**SYFTE:**
Visa hur issues hänger ihop i kedjor, vilken issue som låser upp nästa steg, 
och var den aktuella blockeringen finns.

**VISUELLT FORMAT:**
- Varje issue visas som en separat nod / "mjukt kort"
- Noder binds ihop med pilar
- Varje kedja visas som en egen tydlig sektion
- Kedjor får visas vänster→höger eller uppifrån→ned beroende på utrymme
- Om en kedja har flera grenar ska förgrening visas visuellt

**VARJE NOD SKA VISA:**
- Issue-nummer
- Kort titel
- Team (via färg eller märkning)
- Status:
  - ✅ Klar
  - ◐ Pågår
  - ⏳ Väntar
  - 🔴 Blockerad

**REGLER:**
- Visa sambandet visuellt, inte bara som meningar
- Pilar ska visa riktning: vilken issue låser upp nästa
- Kritisk blocker ska markeras tydligt
- Om flera issues beror på samma foundation-issue ska detta förgrenas
- Max 3–4 kedjor per slide, annars delas innehållet upp på fler slides
- Noder måste vara rundade kort med padding (se VISUAL_DESIGN_MANDATORY.md)

**EXEMPEL LAYOUT:**
```
KEDJA 1
[ #43 API Foundation ] ─────→ [ #82 usePortfolio ]
      ✅                            ◐

KEDJA 2
[ #103 JWT-auth ] ─────────→ [ #104 Spring Security ]
      ◐                              ⏳

KEDJA 3
[ #6 JNA-bridge ] ─────────→ [ #16 back-testing ]
      ⏳
            └──────→ [ #98 historical FX ]
            └──────→ [ #99 multi-currency FX ]
```

**MÅSTE innehålla:**
- ✅ Foundation-issues (låser upp mycket)
- ✅ Dependenter (startar när foundation mergad)
- ✅ Vilka är redan lösta (✅ markerade)

**FÅR INTE innehålla:**
- ❌ Alla issues (bara kritiska kedjor)
- ❌ Timmar eller estimat
- ❌ Långa textstycken — kort titel per nod

---

### SLIDE ⑥B: Code Review Findings (om behövs)

**FORMAT:** Text med märkningar

**INNEHÅL:**
```
KRITISKA FYND:

🔴 Backend PR #XX — [SECURITY_ISSUE]
   STATUS: Åtgärdad + testning igång
   LÖST: Ja, ready för merge

🟠 Frontend PR #YY — [DESIGN_ISSUE]
   STATUS: Väntar på [PERSON/TEAM] [DEPENDENCY]
   NÄSTA: [PERSON] reviewar igen när [CONDITION] klart
```

**REGLER:**
- 🔴 = säkerhetsproblem, 🟠 = designproblem
- "STATUS" = vad gör vi åt det?
- "LÖST" = Ja/Nej/I progress

---

## 📝⑦ RISKER (1-2 slides)

### SLIDE ⑦A: Risk-register denna vecka

**FORMAT:** Tabell

**KOLUMNER:**
| Risk | Sannolikhet | Konsekvens | Mitigation | Status |
|------|-------------|-----------|-----------|--------|
| [RISK_A] ej klart | Låg | [TEAM] får [N]d försening | [PERSON_A] + [PERSON_B] möte idag 14:00 | Pågår |
| [RISK_B] | Medel | [IMPACT] | Pairing [PERSON_C]+[PERSON_D] | Planerat |

**REGLER:**
- Sannolikhet: Låg/Medel/Hög
- Konsekvens: En mening om vad som händer
- Mitigation: Konkret åtgärd (inte "vi hoppas...")
- Status: Identifierad/Pågår/Löst

**MÅSTE innehålla:**
- ✅ Vad kan gå fel
- ✅ Vad gör vi åt det (mitigation)
- ✅ Vem gör det

**FÅR INTE innehålla:**
- ❌ Spekulationer
- ❌ Gamla risker från förra veckan

**FOOTER:** `Källa: Code review + kapacitet-analys ✅`

---

## 📝⑧ KAPACITET & ESTIMERING (1 slide)

### SLIDE ⑧A: Kapacitet denna vecka — Passar detta?

**FORMAT:** Tabell + bedömning

**INNEHÅL:**
```
KAPACITET DENNA VECKA:

Frontend:
  Tillgängligt: 45 timmar (3 × 15h/vecka)
  Planerat: 48 timmar (#88, #89, #85, overhead)
  Status: 🟠 LITE STRAMT

Backend:
  Tillgängligt: 40 timmar (2 × 20h/vecka)
  Planerat: 35 timmar (#95, #87, API-def, möte-overhead)
  Status: 🟢 OK

Native:
  Tillgängligt: 30 timmar (2 × 15h/vecka)
  Planerat: 15 timmar (#86, blockerad på API)
  Status: 🟢 OK — extra kapacitet för support

REKOMMENDATION:
  Flytta #XX till nästa vecka för att ge [TEAM] andrum.
  [PERSON_N] kan stödja [TEAM] #YY under [BLOCKER]-väntan.
```

**REGLER:**
- Kolumner: Tillgängligt | Planerat | Status
- Status-färger: 🟢 OK / 🟠 STRAMT / 🔴 ÖVERBELASTAT
- Rekommendation = konkret (vilka issues flytta?)
- Timmar = estimates från team-medlemmar

**MÅSTE innehålla:**
- ✅ Kapacitet per team
- ✅ Jämförelse: kan vi klara allt?
- ✅ Rekommendation om justering

**FÅR INTE innehålla:**
- ❌ "Vi löser det" (optimism utan data)
- ❌ Micro-managing per person

**FOOTER:** `Källa: Team estimat (från punkt ③-⑤) ✅`

---

## 📝⑨ PRIORITERING & SCOPE (1-2 slides)

### SLIDE ⑨A: Planerad ordning — Fas 1 → 2 → 3

**FORMAT:** Tabell eller text

**INNEHÅL:**
```
🔴 FAS 1 — Foundation Issues (starta nu):
  ✅ [PERSON_A]: #XX [FEATURE_A] (låser upp #YY/#ZZ)
  ✅ [PERSON_B]: #AA [FEATURE_B] (låser upp #BB/#CC)
  ✅ [PERSON_C]: #DD [FEATURE_C] (låg konflikt, egen komponent)

  Varför: Tre kedjor, låg mergekonfliktrisk. #XX/#AA låser upp mycket.

🟠 FAS 2 — Efter Fas 1 mergad (pull develop först!):
  [PERSON_A]: #EE [FEATURE_D]
  [PERSON_B]: #FF [FEATURE_E] (kräver #XX merged)
  [PERSON_C]: #GG [FEATURE_F] (kan parallelleras)

  Varför: #FF kräver #XX. #GG oberoende av dataflödet.

🟡 FAS 3+ — Beroenden lösta:
  [PERSON_A]: Stabilisering #EE
  [PERSON_B]: #HH [FEATURE_G] (kan NOW startas)
  [PERSON_C]: #II [FEATURE_H]
```

**REGLER:**
- Fas 1 = vad gör vi DENNA VECKA
- Fas 2 = när Fas 1 är merged, pull develop först
- Format: Person: Issue + varför denna ordning
- Färger: 🔴 = nästa, 🟠 = sedan, 🟡 = senare

**MÅSTE innehålla:**
- ✅ Ordning (Fas 1 → 2 → 3)
- ✅ Vem gör vad
- ✅ Varför denna ordning (blockers, deps)
- ✅ "Max 1 active + 1 queued per person" regel

**FÅR INTE innehålla:**
- ❌ Slumpmässig ordning
- ❌ "Vi hoppas vi hinner"

**FOOTER:** `Källa: DEPENDENCY_CHAIN_PLANNING + kapacitet ✅`

---

### SLIDE ⑨B: Teamregel — Max 1 active + 1 queued per person

**FORMAT:** Text med exempel

**INNEHÅL:**
```
🚨 MAX 1 ACTIVE + 1 QUEUED PER PERSON

Ingen börjar nästa issue innan dependency är merged i develop.

Exempel ordning för [PERSON_A]:
  1. #XX → merge → pull develop
  2. #YY (depender på #XX) → merge → pull develop
  3. #ZZ (depender på #YY)

Före varje ny issue:
  ☐ Pull/rebase mot develop
  ☐ Kontrollera öppna PRs (vem rör samma komponenter?)
  ☐ Bekräfta dependency är mergad (inte bara "nästan klar")
```

---

## 📝⑩ TEKNISKA BESLUT (1 slide)

### SLIDE ⑩A: Arkitektur-beslut denna vecka

**FORMAT:** Visuella cards/rader (NO POWERPOINT TABLES)

**INNEHÅL:**
```
🟢 BESLUT ① — [DECISION_A]
   FORMAT: [CHOICE_1] (redan validerat)
   ÄGARE: [PERSON_X] (Backend-lead)
   DEADLINE: Idag 14:00
   DOKUMENTATION: #XX GitHub issue
   PÅVERKAN: [TEAM_A] (#YY-#ZZ), [TEAM_B] (#AA)

🟠 BESLUT ② — [DECISION_B]
   FORMAT: [CHOICE_2] + [CHOICE_3]
   ÄGARE: [PERSON_Y] (Backend-lead)
   DEADLINE: Denna dag
   DOKUMENTATION: #BB GitHub issue
   PÅVERKAN: Alla teams

🟡 DISKUSSION — [DECISION_C]
   FRÅGA: [QUESTION] direkt eller via [ALTERNATIVE]?
   ÄGARE: [PERSON_X] + PL
   DEADLINE: Innan #CC klar (idag)
   PÅVERKAN: [IMPACT]
```

**REGLER:**
- 🟢 = Beslut fattad, 🟠 = Under granskning, 🟡 = Diskussion behövs
- Format: BESLUT # — Rubrik
- Varje beslut: FORMAT | ÄGARE | DEADLINE | DOKUMENTATION | PÅVERKAN
- Max 3-4 beslut per vecka

**MÅSTE innehålla:**
- ✅ Vad beslutas
- ✅ Vem beslutar
- ✅ Deadline
- ✅ Vem påverkas

**FÅR INTE innehålla:**
- ❌ Tekniska detaljer (spara för GitHub issue)
- ❌ Gamla beslut

**FOOTER:** `Källa: Code review + arkitektur-diskussioner ✅`

---

## 📝⑪ SPRINTMÅL (1 slide)

### SLIDE ⑪A: Sprintmål denna vecka — Härledd från data

**FORMAT:** Text med bullet points

**INNEHÅL:**
```
SPRINTMÅL DENNA VECKA (baserat på prioritering + kapacitet):

✅ Bekräfta [DECISION_A] innan vecka-slut (KRITISK)
   Varför: Låser upp [TEAM_A] och [TEAM_B]
   Ägare: [PERSON_X] ([TEAM_X]) + [PERSON_Y] ([TEAM_Y])
   Deadline: Fredag EOD (eller denna dag för att ha buffer)

✅ Etablera [FOUNDATION_RESOURCE] (FOUNDATION)
   Varför: [TEAM_A] + [TEAM_B] behöver detta för [PHASE]
   Ägare: [PERSON_Z] ([TEAM_Z])
   Deadline: Denna dag eller imorgon

✅ Ge [TEAM_A] + [TEAM_B] möjlighet att börja [NEXT_PHASE]
   Varför: Två teams kan parallellisera när [BLOCKER] är klart
   Ägare: [PERSON_X] + [PERSON_Y] + [PERSON_W]
   Deadline: Vecka-slut

FEASIBILITY-CHECK:
  ✅ Frontend kapacitet stramt men möjligt (47/48 timmar)
  ✅ Backend har kapacitet (35/40 timmar)
  ✅ Native kan stödja Frontend medan väntar
  → MÅL ÄR REALISTISKT med rekommenderade justeringar
```

**REGLER:**
- Mål ska vara HÄRLEDD från data (punkt ①-⑧), inte önskefullhet
- Max 3-4 mål per vecka
- Varje mål: Vad | Varför | Ägare | Deadline
- Feasibility-check: Kan vi faktiskt göra detta?
- Om inte realistiskt: Säg det direkt (🟠 STRAMT, 🔴 OMÖJLIGT)

**MÅSTE innehålla:**
- ✅ Övergripande mål (1-2 meningar)
- ✅ Deadline
- ✅ Varför detta mål (inte bara "vi vill...")
- ✅ Feasibility-bedömning (kan vi göra det?)

**FÅR INTE innehålla:**
- ❌ Mål från förra veckan (vi bygger nytt från ny data)
- ❌ Optimism utan grund

**FOOTER:** `Härledd från punkt ③-⑧ (team-status, kapacitet, prioritering) ✅`

---

## 📝⑫ SPRINTPLAN (1-2 slides)

### SLIDE ⑫A: Daglig tidsplan denna vecka

**FORMAT:** Text med daglig breakdown

**INNEHÅL:**
```
MÅNDAG [DATE_1]:
  09:00-10:30  Sprint Planning-möte
  14:00-14:30  [PERSON_A] ↔ [TEAM_A] [DECISION]-möte
  Deadline: #XX [TASK] klar

TISDAG [DATE_2]:
  10:00-10:30  [PERSON_B] ↔ [TEAM_B] [TASK]-möte
  Deadline: [MILESTONE] formell dokumenterad i GitHub

ONSDAG [DATE_3]:
  08:00-09:00  Code review för #YY-#ZZ ([DESCRIPTION])
  14:00-14:30  Team-synk på progress
  Deadline: #YY ready för [NEXT_PHASE]

TORSDAG [DATE_4]:
  09:00-12:00  [ACTIVITY] av #ZZ flow
  14:00-15:00  [TASK]-session

FREDAG [DATE_5]:
  09:00-10:00  Final [QA]
  14:00-16:00  [DEMO/REVIEW] KÖRNING
  Deadline: Allt [STATE] eller känd fallback

VECKA-SLUT:
  18:00+  [RETROSPECTIVE] + nästa sprint planning förberedelse
```

**REGLER:**
- Dag för dag breakdown
- Format: Tid - Möte/deadline, Vad
- Deadline = när måste detta vara klart
- Möten = både interna och externa (API möte)

**MÅSTE innehålla:**
- ✅ Kritiska möten denna vecka
- ✅ Deadline per dag
- ✅ CTO-demo tid (om denna vecka)

**FÅR INTE innehålla:**
- ❌ "Slacka", "pausa"
- ❌ Personliga möten

**FOOTER:** `Källa: Kalender + punkt ⑬ (nästa steg) ✅`

---

### SLIDE ⑫B: Milestones (om behövs)

**FORMAT:** Numrerad lista

**INNEHÅL:**
```
MILESTONES:

✅ Idag (Måndag): [MILESTONE_A] avklarat
   Vad: [PERSON_A] + [PERSON_B] fastslår [DECISION]
   Ägare: [PERSON_A]
   Verifikation: #XX issue innehåller [PROOF]

⚠️ Imorgon (Tisdag): [MILESTONE_B] dokumenterad i GitHub
   Vad: Formell dokumentation (inte bara PR)
   Ägare: [PERSON_C]
   Verifikation: [TEAM] kan läsa specifikationen

🟢 Denna vecka (Onsdag): #YY-#ZZ ready för [PHASE]
   Vad: [STATE], inga större bugs
   Ägare: [PERSON_D] + [PERSON_E]
   Verifikation: [ACTIVITY] kan börja onsdag 08:00

🎯 Vecka-slut (Fredag): [DELIVERABLE] körbar
   Vad: [STATE] eller känd fallback
   Ägare: Alla
   Verifikation: [VERIFICATION_METHOD] lyckas
```

---

## 📝⑬ NÄSTA STEG (1-2 slides)

### SLIDE ⑬A: Handlingsplan direkt efter mötet

**FORMAT:** Numrerad lista med tid + verifikation

**INNEHÅL:**
```
HANDLINGSPLAN:

INOM 1 TIMMA EFTER MÖTET:
[ ] 1. [PERSON_A]: Uppdatera GitHub issue #XX med [DECISION]
    Verifikation: Issue-description innehåller [PROOF]

[ ] 2. [PERSON_B]: Uppdatera Project Board — flytta #YY till "[STATUS]"
    Verifikation: Project Board visar #YY i rätt kolumn

IDAG (före [TIDPUNKT] möte):
[ ] 3. [PERSON_C]: Review [RESOURCE] för #ZZ
    Verifikation: [PERSON_C] säger "ready" i GitHub-kommentarer

[ ] 4. [PERSON_D]: Genomför [TASK] på #AA
    Verifikation: [PERSON_D] mergear #AA eller sätter label "[STATUS]"

IMORGON:
[ ] 5. [PERSON_E]: Starta #BB [TASK]-implementation
    Verifikation: Branch #BB-branch skapad + första commit pushad

[ ] 6. [PERSON_F]: Börja pairing-session med [PERSON_G] på #CC
    Verifikation: Commit pushad från #CC-branch

DENNA VECKA:
[ ] 7. [PERSON_H]: Genomför [MEETING] med [TEAM] ([WHEN])
    Verifikation: Issue-comment i GitHub med mötes-summering

[ ] 8. [PERSON_I]: Code-review alla inkommande PRs från [TEAM]
    Verifikation: Alla PRs har review-kommentar

[ ] 9. PL: Verifiera Project Board stämmer med Git-branch-status
    Verifikation: Board-kolumner matchar faktisk arbete
```

**REGLER:**
- Numrerad lista (1, 2, 3...)
- Tidsgrupp: Inom 1h | Idag | Imorgon | Denna vecka
- Format: Nummer. Namn: Action
- MÅSTE ha verifikation (hur vet vi att det är klart?)
- Verifikation = GitHub-verifierbar (inte "vi tror")

**MÅSTE innehålla:**
- ✅ Konkreta GitHub-åtgärder (issue-update, branch-create, PR-create)
- ✅ Ägare för varje åtgärd
- ✅ Deadline (samma dag, imorgon, denna vecka)
- ✅ Verifikation-punkt (hur vet vi det är klart?)

**FÅR INTE innehålla:**
- ❌ Vague tasks ("vi ska jobba på...")
- ❌ Åtgärder utan ägare
- ❌ "Vi hoppas..." (bara konkreta saker)

**FOOTER:** `Baserat på punkt ③-⑫ (status, prioritering, plan) ✅`

---

## 📝⑭ FRÅGOR TILL PL (1 slide)

### SLIDE ⑭A: Öppna frågor för PL-svar

**FORMAT:** Numrerad lista med prioritering

**INNEHÅL:**
```
ÖPPNA FRÅGOR FÖR PL-SVAR:

IDAG-SVAR BEHÖVS (höga prioriteten):

1. SCOPE — Ska #XX ([FEATURE_A]) in i denna sprint?
   VARFÖR VIKTIG: Påverkar [TEAM]-kapacitet (+ [N] timmar)
   IMPAKT: Om JA → flytta #YY till nästa vecka

2. PRIORITERING — Om #ZZ mergea idag, kan vi skippa #AA?
   VARFÖR VIKTIG: Kan spara [N] timmar [TASK]
   IMPAKT: Säkerhets-testing vs testramverk-investering

3. SCOPE — Responsive dashboard (#86): krävs desktop-version också?
   VARFÖR VIKTIG: Påverkar Native-tidsuppskattning (+ 12 timmar)
   IMPAKT: Om JA → omöjligt denna vecka

IDAG-SVAR NICE-TO-HAVE (diskussions-frågor):

4. PROCESS — Ska mötet nästa vecka starta med Code Review eller Retrospekt?
   VARFÖR VIKTIG: Påverkar agenda (40min skillnad)

5. PROCESS — Ska vi döpa om branches enligt naming-convention?
   VARFÖR VIKTIG: CI/CD-fokus eller flexibilitet?
```

**REGLER:**
- MAX 5-6 frågor per möte
- Börja med "IDAG-SVAR BEHÖVS" (höga prioriteten)
- Avsluta med "IDAG-SVAR NICE-TO-HAVE" (diskussions-frågor för senare)
- Format: Nummer. KATEGORI — Fråga + VARFÖR VIKTIG + IMPAKT
- PL måste kunna svara direkt (inte "vi återkommer")

**MÅSTE innehålla:**
- ✅ Öppna frågor från teamet
- ✅ PL-beslut som saknas
- ✅ Scope-frågor ("ska vi inkludera X?")
- ✅ Prioritering (vad ska PL svara på IDAG)

**FÅR INTE innehålla:**
- ❌ Retoriska frågor
- ❌ "Vi undrar om..." (bara konkreta frågor)
- ❌ >6 frågor

**FOOTER:** `Källa: Team-feedback under mötet ✅`

---

## 🔗 HUVUD-REGEL: VARJE SLIDE HAR ETT SYFTE

**En slide = ETT av dessa:**
1. Status (vad är klart/pågår)
2. Problem (vad blockerar oss)
3. Plan (vad gör vi härnäst)
4. Åtgärd (vem gör vad, när)

**Om en slide blandar två syften → bryta upp den.**

Exempel:
- ❌ "Punkt ①A visar både merged + commits"
- ✅ "①A visar merged PRs, ①D visar commits"

---

## 🔗 MOTSÄTTA: VERIFIKATION-FOOTER

**Varje slide med data MÅSTE ha footer med källa:**

```
RÄTT:
  "Källa: GitHub PRs (merged denna vecka) ✅"
  "Källa: Code review + kapacitet-analys ✅"
  "Källa: GitHub issues + Project Board ✅"

FEL:
  "Källa: GitHub" (för vag)
  "Källa: Underlag" (från vad?)
  Ingen footer (var kom datan ifrån?)
```

**Format:** `Källa: [Vad] ([Tidsram]) [Status: ✅/⚠️]`

---

**Version:** 1.0
**Status:** KRITISK SPECIFIKATION
**Senast uppdaterad:** 2026-09-14
