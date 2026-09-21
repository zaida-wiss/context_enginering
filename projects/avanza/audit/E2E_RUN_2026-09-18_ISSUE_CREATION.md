# End-to-end run — Issue Creation

**Date:** 2026-09-18  
**Context ref:** `dev`  
**Test case:** `_audit/END_TO_END_TEST_CASES.md` → Test 2

## Goal

Verify that issue creation uses a **scope-specific Applicable Definition of Done**
instead of copying every project criterion into every issue.

---

## Case A — Small UI/CSS change

### Prompt

> Skapa en issue för att fixa spacing i mobilmenyn.

### Expected generated shape

```markdown
## Why
Mobilmenyn har spacing som behöver korrigeras för att layouten ska vara tydlig
på berörda små skärmstorlekar.

## Outcome
Mobilmenyn använder avsedd spacing utan att påverka övrig navigation.

## Acceptance Criteria
- [ ] Spacing stämmer i de berörda mobilvyerna.
- [ ] Navigationens funktion och klickytor fungerar som tidigare.
- [ ] Ingen oavsiktlig layoutförändring syns i närliggande viewport.

## Testing
**Verify**
- [ ] Kontrollera berörda mobilstorlekar.
- [ ] Kontrollera att navigation/interaktion fortfarande fungerar.

**Test level**
- Manual visual/responsive check
- Component/interaction test only if existing component behavior warrants it

## Applicable Definition of Done
- [ ] Acceptance Criteria verifierade.
- [ ] Relevanta visuella/interaktiva kontroller genomförda.
- [ ] Branchen är synkad med aktuell develop innan PR.
- [ ] PR är reviewad/accepterad och mergad.
- [ ] Issuen flyttas till Done efter merge.
```

### Correct omissions

The generated issue should **not** add these without evidence:

- README update
- API contract documentation
- architecture decision
- backend/native verification
- every test level
- invented risk entry

### Verdict

**PASS**

The current template and DoD authority support this scope correctly.

---

## Case B — API response contract change

### Prompt

> Skapa en issue för att ändra portfolio-endpointens response-format.

### Expected generated shape

```markdown
## Why
Response-formatet behöver ändras på ett kontrollerat sätt eftersom konsumenter
kan bero på fältnamn, typer, optional/null-semantik och felbeteende.

## Outcome
Det nya response-kontraktet är explicit, implementerat och verifierat mot
relevanta konsumenter.

## Acceptance Criteria
- [ ] Nya/ändrade fält och typer är explicit definierade.
- [ ] Berörda konsumenter använder samma kontrakt.
- [ ] Relevant fel/null/optional-beteende är definierat.
- [ ] Integrationsverifiering visar att producent och konsument fungerar ihop.

## Dependencies / contracts
- [relevant producer/consumer and existing contract source]

## Testing
**Risk this change introduces**
- Ett kontraktsbrott kan göra en konsument inkompatibel.

**Verify**
- [ ] Serialization/response shape.
- [ ] Consumer integration/contract behavior.
- [ ] Relevant failure/null/optional case.

**Test level**
- Integration / contract verification
- Additional unit/component checks only where the changed behavior requires them

## Applicable Definition of Done
- [ ] Acceptance Criteria verifierade.
- [ ] Relevant kontrakts-/integrationsverifiering passerar.
- [ ] API/kontraktsdokumentation som beskriver response-formatet är uppdaterad.
- [ ] Relevant beslut/risk uppdateras endast om ändringen faktiskt skapar ett sådant.
- [ ] Branchen är synkad med aktuell develop innan PR.
- [ ] PR är reviewad/accepterad och mergad.
- [ ] Issuen flyttas till Done efter merge.
```

### README rule

README is **not automatic**.

Include a README criterion only when the project's README actually documents the
changed endpoint usage, setup or response behavior. Otherwise the contract's
canonical documentation is the relevant documentation target.

### Verdict

**PASS**

The current authorities select materially different DoD criteria for the API
change than for the CSS change.

---

## Structural issue discovered and fixed during test

Before this run:

- `templates/ISSUE_BODY.md` owned the new Applicable DoD layout
- `TEAM_STANDARDS.md` still contained an older partial copy of the issue body

This was not a direct rule contradiction, but it created two competing-looking
body descriptions.

### Fix

`TEAM_STANDARDS.md` now owns workflow expectations and references
`templates/ISSUE_BODY.md` as the single issue-body layout owner.

## Test verdict

**PASS**

The issue-creation flow now demonstrates:

- adaptive DoD selection
- risk-based test selection
- conditional README/documentation requirements
- no automatic API/architecture criteria for unrelated issues
- no invented risk or decision merely to fill a section

---

**Status:** PASS
