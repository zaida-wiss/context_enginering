---
name: mandatory_reading_order
description: Exact order AI must read files before rendering presentation — NO EXCEPTIONS
metadata:
  type: process
  critical: true
---

# 🚨 MANDATORY READING ORDER — INNAN PRESENTATION RENDERAS

## 📋 SYSTEM CONTRACT (Read first)

Se [`SYSTEM_CONTRACT.yaml`](SYSTEM_CONTRACT.yaml) — **maskinläsbar definition av hela systemet**.

YAML-filen är källan till sanning. Den innehåller:
- ✅ Auktoritativa källor
- ✅ Execution sequence (8 steg)
- ✅ Hard rules (aldrig brytas)
- ✅ GitHub status definitions (mekaniska)
- ✅ Deprecated files (ta bort alla references)
- ✅ Success criteria

**Läs denna FÖRST, innan du läser något annat.**

---

🤖 **FÖR AI: Kopiera denna prompt direkt till vilken AI som helst:**
```
Läs: https://github.com/zaida-wiss/context_enginering/blob/main/_ai_guides/presentations/AI_PROMPT_GENERATE_PRESENTATION.md
Följ den exakt. Fetcha LIVE GitHub-data. Rapportera om något failar.
```

---

🚫 **KRITISK REGEL ÖVERST — AI MÅSTE VERIFIERA INNAN RENDERING:**
```
DO NOT CREATE PPTX UNTIL AI HAS:

✅ IDENTITY VERIFICATION: Alla 7 team-medlemmar verifierade från GitHub
✅ DATA COLLECTION: Hämtat alla källor (GitHub PRs, branches, commits, 
   Project Board, Google Sheets fallback, mötesprotokollet)
✅ DATA VERIFICATION REPORT: Visat användaren vilka källor som var nåbara/ej nåbara
✅ SLIDE_DETAIL_SPEC: Varje slide matchar specifikationen exakt
✅ VISUAL_DESIGN_MANDATORY: Alla 13 render-gate checkpoints passerade
✅ RENDER_GATE_CHECKLIST: Godkänt innan rendering

AI:s ansvar: Verifiera ALLT och rapportera status till användaren.
Användaren behöver INTE bekräfta — AI ansvarar för verifieringen.

If ANY verification fails → AI STOPS, presents report, gör INTE PPTX.
```

---

**DENNA FIL MÅSTE LÄSAS FÖRE PRESENTATION.**

🔗 **NOTE:** Alla externa URLs (Google Sheets, Google Docs, GitHub) är centraliserade i [`_memory/EXTERNAL_SOURCES.md`](../../_memory/EXTERNAL_SOURCES.md). Se den filen för aktuella IDs och fallback-URLs.

**Om denna ordning inte följs → presentation blir inkomplett eller bryter mot regler.**

---

## 🚨 KRITISK REGEL #0 — LÄSA INSTRUKTIONER ≠ VISA INSTRUKTIONER

**INNAN du läser NÅGOT annat:**

```
⭐ DENNA REGEL ÄR TVINGANDE ⭐

Du ska LÄSA dessa instruktioner för att FÖRSTÅ vad presentationen behöver.
Du ska ANVÄNDA dessa instruktioner för att BYGGA presentationen.
Du ska ALDRIG VISA dessa instruktioner ON SLIDES.

EXEMPEL:

🔴 FEL:
  Slide visar: "Repo-first: visa bara det som går att koppla till PR, commit..."
  Slide visar: "Måste räknas mot develop"
  Slide visar: "Ej live-låst här"
  → Dessa är instruktioner för DIG, inte innehål för mötet

✅ RÄTT:
  Slide visar: "#95 Security review · Zaida · ✓ DONE · merged 2026-09-13"
  Slide visar: "🔴 API-kontrakt inte låst — Frontend blockerad"
  Slide visar: "Backend måste leverera API-spec idag"
  → Dessa är RESULTAT av att följa instruktionerna

MECKANISK KONTROLL (efter rendering):
  För varje slide:
    Q: "Skulle en projektledare säga detta till teamet?"
    Ja → texten får vara på sliden
    Nej → ta bort texten

RENDER-GATE CHECK:
  ☐ Presentationen innehåller INGEN instruktioner?
  ☐ Presentationen innehåller INGEN checklista?
  ☐ Presentationen innehåller INGEN AI-process?
  
  Om något är NEJ → STOPP, ta bort det innan rendering
```

**Se även:**
- [PRESENTATION_SPEC.md — NO META-INSTRUCTIONS ON SLIDES](content/PRESENTATION_SPEC.md#L219)
- [RENDER_GATE_CHECKLIST.md — KRITISK: INGEN AI-INSTRUKTIONER PÅ SLIDES](verification/RENDER_GATE_CHECKLIST.md)

---

---

## 🚨 KRITISK REGEL: DATA ACCESS

**INNAN något annat — DESSA REGLER FÅR ALDRIG BRYTAS:**

```
✅ DATA SOURCES (endast dessa):
  • GitHub API (raw.githubusercontent.com)
  • GitHub webben direkt (WebFetch)
  • Google Sheets (fallback)
  • Google Docs (fallback)

❌ ALDRIG DETTA:
  ✗ Web search (Google, Bing, etc) — SECURITY VIOLATION
  ✗ External APIs
  ✗ git clone, git ls-remote
  ✗ Söka projektdata på publika webbsidor

📋 OM GitHub failar:
  → Använd fallbacks från DATA_SOURCES.md
  → ALDRIG externa websökningar
  → Visa status i presentation (transparent)
```

**Om du börjar söka på webben → DU GJORDE NÅGOT FEL.**

---

## 🚀 AI EXECUTION WORKFLOW — DENNA ORDNING MÅSTE FÖLJAS

**DENNA FIL SÄGER DEN EXAKTA ORDNINGEN för AI:**

👉 **LÄS FÖRST:** [AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)

Den filen säger:
- FASE 1: Datainsamling & Identity verification (GitHub API endast!)
- FASE 2: Render gate check
- FASE 3: Bygga presentation & final verification
- **AI gör ALLT — levererar presentation KLAR (ingen human-loop)**

**UTAN denna ordning → presentation blir felaktig eller ej verifierad.**

---

---

### STEG 0: PROJEKTKONTEXT — LÄS FÖRST (innan GitHub-data)

**INNAN du börjar samla GitHub-data — läs dessa för att förstå projektkontexten:**

1. **[../../_memory/PROJEKTKONTEXT_AVANZA.md](../../_memory/PROJEKTKONTEXT_AVANZA.md)** 
   - Projekt-overview & styrning
   - Fallback-hierarki om något failar
   
2. **[../../_memory/TEAM_ROSTER.md](../../_memory/TEAM_ROSTER.md)**
   - Auktoritativ team-lista (för identity verification)
   
3. **[../../_memory/SCHEDULE.md](../../_memory/SCHEDULE.md)**
   - Vecko-fokus & kurschema
   - Relevanta för att förstå sprint-tema
   
4. **[../../_memory/COURSE_DEADLINES.md](../../_memory/COURSE_DEADLINES.md)** (om relevant för slide ⑫⑬)
   - Kurs-deadlines & specifikationer
   - Kan behövas för "realism check" på plan

**SEDAN gå till STEG 1 nedan.**

---

### STEG 1: LÄS DESSA FILER (i ordning)

**Läs INTE något mer — dessa filer säger allt:**

1. **[README.md](README.md)** — Vad är presentations-systemet?
2. **[monday_meeting/README.md](monday_meeting/README.md)** — 14 mötespunkter overview
3. **[monday_meeting/data/DATA_COLLECTION_MANDATORY.md](monday_meeting/data/DATA_COLLECTION_MANDATORY.md)** — Datainsamling & identity-verifikation
4. **[data/DATA_SOURCES.md](data/DATA_SOURCES.md)** — Vilka GitHub-URLs, fallback-ordning

**Sedan gå till STEG 2 (nedan).**

---

### STEG 2: VERIFIERA

**Läs dessa filer för verifikations-processen:**

1. **[verification/AI_VERIFICATION_WORKFLOW.md](verification/AI_VERIFICATION_WORKFLOW.md)** 
   - AI gör ALLT: hämta → verifiera → leverera
   
2. **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)** 
   - KAN presentationen renderas? 13 checkpoints MÅSTE passeras

---

### STEG 3: DESIGN & SPECIFIKATION — OBLIGATORISK LÄSNING

🚨 **DETTA STEG ÄR INTE VALFRITT — PRESENTATION ÄR FELAKTIG UTAN DET**

**Läs DESSA filer i denna ordning (de innehåller ALLT):**

1. **[design/ACCESSIBILITY_NEURODIVERSITY.md](design/ACCESSIBILITY_NEURODIVERSITY.md)** 🧠 LÄS FÖRST
   - VARFÖR Symbol + Färg + Text? (för dyslektiker, ADHD, autism — och alla andra)
   - Påtvingad läsning för att förstå designfilosofin
   - **KRITIK:** Utan denna förståelse kommer designen bli felaktig
   
2. **[design/VISUAL_DESIGN_MANDATORY.md](design/VISUAL_DESIGN_MANDATORY.md)** 🚨 OBLIGATORISK FÖRE RENDERING
   - **DEN HÄR FILEN ÄR LAGLIG REQUIREMENT — PRESENTATION RENDERAS ALDRIG UTAN DET**
   - Symbol + Färg + Text (mekanisk implementering)
   - RGB-värden, px-storlekar, font-specs, whitespace — ALLT konkret
   - **RENDERING-CHECKLIST:** 13 punkter som MÅSTE passeras innan presentation kan visas
   - **FÖRBJUDNA PATTERNS:** Textlistor, bara färg (utan symbol), ingen whitespace, liten text
   - **HIERARKI:** NPF-regler > Design-regler (se denna fil för prioritering om de krockar)
   
3. **[monday_meeting/design/SLIDE_DETAIL_SPEC.md](monday_meeting/design/SLIDE_DETAIL_SPEC.md)** ⭐ AUKTORITATIV
   - EXAKT innehål för VARJE SLIDE (①-⑭)
   - **VISUELL REFERENS:** Se [`TEMPLATE_REFERENCE.html`](monday_meeting/design/TEMPLATE_REFERENCE.html) för konkret visuell exempel (färger, fonts, spacing, rundade hörn)
   - **KRITISK FORMAT-REGEL:** Slide ①A-C är TABELLER med tre sektioner (Merged | Pågår | Review), INTE sammanfattning-tabeller
   - Se exempel längre ned under "SLIDE ①A-C FORMAT"
   
4. **[monday_meeting/structure/PRESENTATION_STRUCTURE.md](monday_meeting/structure/PRESENTATION_STRUCTURE.md)**
   - 14 mötespunkter (①-⑭) definitioner

**HIERARKI när regler krockar:**

```
🚨 NPF-REGLER (ACCESSIBILITY_NEURODIVERSITY.md) — HÖGSTA PRIORITET
   ↓
VISUAL_DESIGN_MANDATORY.md — Designregler
   ↓
SLIDE_DETAIL_SPEC.md — Innehållsformat
   ↓
PRESENTATION_STRUCTURE.md — Ordning

OM NPF och DESIGN krockar → NPF VINNER ALLTID
OM DESIGN och CONTENT krockar → DESIGN VINNER
OM CONTENT och STRUCTURE krockar → CONTENT VINNER
```

**VIKTIG REGEL:** Om NPF-reglerna säger "detta behövs för dyslektiker" men designen säger "det ser inte bra ut" → **NPF VINNER. Alltid.**

Exempel:
- ❌ FALSKT: "Design säger ingen färg här, men NPF säger 🟢🟡🔴 behövs"
- ✅ RÄTT: Lägg på färgerna. NPF vinner.

Samma med:
- ✅ RÄTT: 24px radhöjd (NPF) > 20px (Design)
- ✅ RÄTT: Symbol → Färg → Text (NPF) > bara Text (Design)
- ✅ RÄTT: Orange bakgrund för Review-sektion (NPF) > ingen bakgrund (Design)

---

### 🚨 KRITISKA FORMAT-REGLER — LÄS FÖRE RENDERING

**SLIDE ①A-C (Frontend/Backend/Native) MÅSTE VARA DENNA FORMAT:**

```
| Issue # | Titel (2-5 ord) | Assignad | Status | Merged/Branch |
|---------|-----------------|----------|--------|---------------|
| ✅ MERGED DENNA VECKA |
| #95 | Security review | Zaida Wiss | ✓ DONE | 2026-09-13 |
| #87 | Test foundation | Björn Boman | ✓ DONE | 2026-09-12 |
|
| ◐ PÅGÅR DENNA VECKA |
| #88 | Critical interactions | Björn Boman | ◐ PÅG | feature/#88 |
| #89 | E2E happy path | Tomac Barin | ◐ PÅG | feature/#89 |
|
| ⏳ VÄNTAR PÅ REVIEW (🟠 eller 🔴 bakgrund för att dra uppmärksamhet) |
| #90 | Auth flow refactor | Lisa Andersson | ⏳ REVIEW | PR #142 |
| #91 | Session storage | Erik Berglund | ⏳ REVIEW | PR #143 |
```

**REGLER:**
- ✅ **TRE SLIDES, EN PER TEAM:**
  - **①A = ENDAST Frontend-issues** (filtrera: Team = "Frontend" från GitHub)
  - **①B = ENDAST Backend-issues** (filtrera: Team = "Backend" från GitHub)
  - **①C = ENDAST Native-issues** (filtrera: Team = "Native" från GitHub)

- ✅ **TIDSPERIOD: SENASTE 7 DAGARNA** (sedan förra mötet)
  - Merged: PRs mergade senaste 7 dagarna
  - Pågår: Branches med commits senaste 7 dagarna
  - Väntar på review: PRs skapade/uppdaterade senaste 7 dagarna
  - Stale branches: >3 dagar utan push (risk-flagg)

- ✅ **TRE SEKTIONER per slide:** Merged (sortera datum, nyast först) | Pågår (senast pushad först) | Review (äldst först)
- ✅ **Assignad = ÄGARE av arbetet** (GitHub issue assignee), INTE reviewer eller merger
- ✅ **FAKTISK GitHub-data**, ALDRIG exempel eller placeholders
- ✅ **Väntar på review-sektion** måste ha tydlig visuell markering (orange/röd bakgrund)
- ✅ **ALLA 7 team-medlemmar** måste synas distribuerade över ①A-C (även om 0 arbete denna vecka)
- ✅ **Footer:** `Källa: GitHub PRs + branches (senaste 7d) + Project Board ✅ | ⏳ Reviews behövs på: [faktiska issues]`

**FÅR INTE SES:**
- ❌ **EN gemensam slide för alla team** (detta är fel!)
- ❌ Bara "Väntar på review"-sektion (måste visa Merged + Pågår också)
- ❌ Team-områdena som sammanfattning (Frontend/Backend/Native/Team)
- ❌ Commit-hashar
- ❌ Stale branches (>3 dagar utan push)
- ❌ Reviewer-namn som assignee
- ❌ Exempel-issue-nummer (#90, #91, etc) från denna spec — använd FAKTISK GitHub-data!

---

### 🚨 SLIDES ③④⑤ FORMAT-REGEL: PER TEAM, ALDRIG SAMMANFATTNING

**SLIDES ③④⑤ (Frontend/Backend/Native) MÅSTE VARA DENNA STRUKTUR:**

```
SLIDE ③A (Frontend — denna sprint):
┌──────┬───────────────────────┬──────────────┬────────┬──────────────┐
│ Issue│ Titel                 │ Assignad     │ Status │ Blocker      │
├──────┼───────────────────────┼──────────────┼────────┼──────────────┤
│ #88  │ Critical interactions │ Björn Boman  │ ◐ PÅG  │ API-kontrakt │
│ #89  │ E2E happy path        │ Tomac Barin  │ ◐ PÅG  │ API-kontrakt │
│ #85  │ Responsive header     │ Zaida Wiss   │ ✓ DONE │ —            │
└──────┴───────────────────────┴──────────────┴────────┴──────────────┘

SLIDE ④A (Backend — denna sprint):
┌──────┬──────────────────────┬──────────────┬────────┬────────────┐
│ Issue│ Titel                │ Assignad     │ Status │ Blocker    │
├──────┼──────────────────────┼──────────────┼────────┼────────────┤
│ #87  │ API-definition       │ Erik Bergl.  │ ◐ PÅG  │ —          │
│ #95  │ Security review      │ Rasha Knifdi │ ✓ DONE │ —          │
└──────┴──────────────────────┴──────────────┴────────┴────────────┘

SLIDE ⑤A (Native — denna sprint):
┌──────┬──────────────────────┬──────────────┬────────┬──────────────┐
│ Issue│ Titel                │ Assignad     │ Status │ Blocker      │
├──────┼──────────────────────┼──────────────┼────────┼──────────────┤
│ #86  │ Support capacity     │ Pär Lundh    │ ◐ PÅG  │ API-kontrakt │
│ #92  │ Performance testing  │ Henrik W.    │ ◐ PÅG  │ —            │
└──────┴──────────────────────┴──────────────┴────────┴──────────────┘
```

**REGLER:**
- ✅ EN SLIDE PER TEAM (③A, ④A, ⑤A)
- ✅ **Alla 7 team-medlemmar distribuerade enligt faktiskt arbete** — inte en gemensam sammanfattning
- ✅ Sortera på status (DONE sist)
- ✅ Blocker = vad väntar vi på (issue-nummer eller kort text, eller "—" om ingen)
- ✅ Status: ✓ DONE | ◐ PÅG | ⏳ VÄNTAR

**FÅR INTE SES:**
- ❌ En gemensam "Teamtäckning" slide med alla 7 medlemmar
- ❌ Sammanfattnings-tabell (Område | Fokus)
- ❌ Commit-hashar
- ❌ PR-nummer (vi visar issues, inte PRs)
- ❌ Estimat i timmar
- ❌ "Nästan klart" (antingen DONE eller PÅG)

---

### STEG 4: FINAL RENDER GATE

🚨 **INNAN DU RENDERAR — VERIFIERA ATT DU LÄST ALLT:**

**Checklista före rendering:**
- ☐ Läst STEG 0? (Läs _memory/)
- ☐ Läst STEG 1? (GitHub-data)
- ☐ Läst STEG 2? (Verifikation)
- ☐ **Läst STEG 3?** (Design — MANDATORY_READING_ORDER + ACCESSIBILITY_NEURODIVERSITY + **VISUAL_DESIGN_MANDATORY**)
  - Om NEJ → **STOPP, läs den nu**
  - Om JA → fortsätt

Läs: **[verification/RENDER_GATE_CHECKLIST.md](verification/RENDER_GATE_CHECKLIST.md)**
- 13 checkpoints MÅSTE passeras innan rendering
- Om någon checkpoint failas → presentation renderas INTE
- **RENDER_GATE checklist inkluderar VISUAL_DESIGN_MANDATORY verifyas**

---

### 🚨 SLUTREGEL — STRUCTURE vs CONTENT

**If the generated presentation output differs from SLIDE_DETAIL_SPEC.md:**
- Structurally (wrong columns, wrong order, wrong sections)
- Visually (wrong colors, wrong fonts, wrong spacing, wrong symbols)
- Even if the factual data (GitHub commits, PRs, etc.) is correct

→ **Presentation is INVALID. Do not deliver. Show report to user. Stop.**

Structure matters as much as content. A presentation with correct data but wrong structure is broken, not good enough.

This is not a design preference — it is a specification requirement.

---

**MANDATORY_READING_ORDER.md — Denna fil är den ENDA körordningen.**

**Status:** 2026-09-14 — ORCHESTRATION FIXED (human verification removed, single workflow)

