---
name: definition-of-done
description: Definition of Done (DoD) = when a GitHub issue is complete. NOT about course goals.
metadata:
  type: reference
---

## 📍 DOKUMENTVÄGEN

**Du är här:** DEFINITION_OF_DONE.md (Vad är en KLAR issue?)

```
START — README.md (denna repo)
        ↓
        VILL DU VERIFIERA EN ISSUE?
        ↓
🟢 DU ÄR HÄR: DEFINITION_OF_DONE.md (denna fil)
        ↓
ANVÄND MED:
  • DEFINITION_OF_READY.md (innan issue börjas)
  • VERIFICATION_SYSTEM.md ← Hur verifierar vi?
  • Faktisk GitHub issue ← Vilka kriterier är checkade?
        ↓
RESULTAT: Du vet om en issue är VERKLIGEN KLAR
```

**GÅ TILLBAKA TILL:** README.md för övergripande guide

---

# Definition of Ready & Definition of Done

**VIKTIGT:** DoD är en UTVECKLINGSTERMIN för när en issue är slutförd. Inte samma som kursmål!

Se [[course-goals-grading]] för information om betyg och kursmål.

---

## 🚀 Definition of Ready (DoR) - INNAN Vi Börjar

En issue är **READY** att börja arbeta på när:

### Tydlighet
- [ ] **Titel är klar** - "Add portfolio overview dashboard" (inte "dashboard")
- [ ] **Problem är definierat** - Vad är användarens behov?
- [ ] **Lösning är beskriven** - Vad ska vi bygga?

### Acceptance Criteria
- [ ] **3-5 mätbara kriterier** - Testa om det är klart
- [ ] **Inte vaga** - Inte "make it work", utan specifikt
- [ ] **Definition av klart** - Vad betyder "klart"?

### Teknik & Beroenden
- [ ] **Scope definierad** - Frontend/Backend/Native?
- [ ] **Ingen blockers** - Eller är det tydligt vad som blockerar?
- [ ] **Beroenden identifierade** - Väntar denna på något annat?
- [ ] **Estimat givet** - 4h/8h/16h/20h?

### Exempel på READY Issue:
```
Title: feat(frontend): Add portfolio overview dashboard (#26)

Problem: User cannot see total portfolio value across all savings

Solution: Dashboard showing total, allocation, risk metrics

Acceptance Criteria:
- [ ] Dashboard displays ISK + KF + depå value
- [ ] Values converted to SEK
- [ ] Allocation chart shows aktier/fonder %
- [ ] Components TypeScript-typed
- [ ] E2E test covers happy path

Blockers: None
Estimate: 16h
```

---

## 🎯 AC vs DoD - VIKTIGT SKILLJA!

**AC och DoD är INTE samma sak:**

```
AC (Acceptance Criteria)     = VAD ska fungera?
                               ☐ Login works
                               ☐ Error shows
                               ☐ Redirects
                               = ~20% av DoD

DoD (Definition of Done)     = HUR säkerställer vi det är klart?
                               ☐ AC uppfyllda (JA, men...)
                               ☐ Testade
                               ☐ Reviewade
                               ☐ Dokumenterat
                               ☐ Format korrekt
                               = 100% krav för att stänga
```

**AC är en DELMÄNGD av DoD!**

---

## ✅ Definition of Done - INNAN Vi Stänger Issue

En feature/fix är **DONE** när den uppfyller ALLT här (inklusive AC):

### Kod
- [ ] **AC är uppfyllda** - Allt som AC säger ska fungera gör det
- [ ] **Ingen console.log** - Debug-kod är borttagen
- [ ] **Ingen TODO/FIXME** - Eller tydligt dokumenterat varför det finns
- [ ] **Formatterad kod** - Linting passerar (ESLint, Prettier)
- [ ] **Ingen dead code** - Oanvänd kod är borttagen

### Tester
- [ ] **Unit tests** - För kritiska funktioner
- [ ] **Integration tests** - För databas/API-interaktion
- [ ] **E2E tests** - För kärnflödet
- [ ] **Alla tests passerar** - Lokalt OCH i CI
- [ ] **Testade edge cases** - Inte bara happy path

### Code Review
- [ ] **Granskad av annan** - Minst en annan person
- [ ] **Feedback adresserad** - Alla kommentarer lösta
- [ ] **Godkänd pull request** - Minst en godkännande review
- [ ] **Ingen self-approval** - Du kan INTE godkänna din egen PR

### Dokumentation
- [ ] **README uppdaterad** - Om issue påverkar installation/arkitektur
- [ ] **Komponenter dokumenterade** - Nya funktioner förklarade
- [ ] **API dokumenterad** - Nya endpoints/datamodeller
- [ ] **Beslutslogg uppdaterad** - Om arkitektur-val gjordes
- [ ] **Kända brister dokumenterade** - Vad fungerar INTE än

### Accessibility (WCAG 2.1 AA)
- [ ] **Keyboard navigation** - Tab/Enter/Escape funkar
- [ ] **Contrast ratios** - Text/bakgrund minst 4.5:1
- [ ] **ARIA labels** - Form inputs har aria-label
- [ ] **Semantic HTML** - `<button>`, `<nav>`, `<main>` används
- [ ] **Color blindness** - Inte bara färg för info

### Git & Commit
- [ ] **Commits är logiska** - Inte "fixed stuff"
- [ ] **Commit messages är tydliga** - `type(scope): message (#issue)`
- [ ] **Branch är deskriptiv** - `feature/#42-portfolio-dashboard`
- [ ] **Branch är mergad** - Ej stray branch kvar
- [ ] **Git-historia är ren** - Inga force-push artefakter

### Deploy & Integration
- [ ] **Kod passar in i systemet** - Ingen breaking changes
- [ ] **Beroenden är uppdaterade** - package.json, pom.xml etc
- [ ] **Migration klara** - Databas-schema-ändringar dokumenterade
- [ ] **Environment-variables** - Inte hardkodade
- [ ] **Kan köras lokalt** - Inga externa tjänster som krävas (om möjligt)

### Kvalitets-gates
- [ ] **70%+ kodtäckning** - Coverage acceptabel
- [ ] **Ingen kritiska säkerhetsproblem** - Inga OWASP-bärbara buggar
- [ ] **Performance OK** - Inte långsammare än tidigare
- [ ] **Build passerar** - `npm run build`, `mvn clean build` etc
- [ ] **Linting passerar** - Ingen format-brus

---

## 📖 Dokumentation (Specifikt för DoD)

### README.md
Måste innehålla:

- [ ] **Projektbeskrivning** - Vad är detta?
- [ ] **Installationsinstruktioner** - Steg-för-steg setup
- [ ] **Hur man kör projektet** - Start backend, frontend, native
- [ ] **Hur man kör tester** - Testkommando för alla tre lager
- [ ] **Arkitektur-översikt** - Hur fungerar systemet?
- [ ] **Kända brister** - Vad fungerar inte än?
- [ ] **Avgränsningar** - Vad gjorde vi INTE?

### Beslutslogg (DECISIONS.md eller i README)
Måste dokumentera:

- [ ] Varför denna teknikstack (not Vue, Svelte, etc.)
- [ ] Varför denna arkitektur (choices made)
- [ ] Varför dessa prioriteringar (vad gjorde vi först, vad skippade vi)

### Teststatus
Måste dokumentera:

- [ ] Unit tests täckning (% för varje lager)
- [ ] Integration tests status
- [ ] E2E tests (minst kärnflödet)
- [ ] Testresultat (vilka passar, vilka är TODO)

---

## 🔀 Git & Process (Specifikt för DoD)

### Commits & Branches
- [ ] Alla commits följer format: `type(scope): message (#issue)`
- [ ] Alla branches följer namngivning: `type/#issue-description`
- [ ] Brancher länkas till GitHub issues
- [ ] Commits är små och logiska (inte "fixed stuff")

### Pull Requests
- [ ] Alla features/fixes är via PR
- [ ] PR:er är granskade av annan teammedlem
- [ ] Granskare kan INTE merga sitt eget godkännande
- [ ] PR-beskrivning refererar till issue

### Historia & Traceability
- [ ] `git log --graph --all --oneline` visar tydlig historia
- [ ] Individuella bidrag går att härleda (vem gjorde vad)
- [ ] Branches behålls för historik (tas INTE bort)

---

## 🧪 Testing (Specifikt för DoD)

Måste ha tester för:

### Frontend
- [ ] Unit tests för komponenter (Vitest/Jest)
- [ ] Test för varje kritisk user-interaction
- [ ] E2E test för kärnflödet (Cypress/Playwright)

### Backend
- [ ] Unit tests för service-lager (JUnit)
- [ ] Integration tests för repository (använder testdatabase)
- [ ] API tests för endpoints (REST endpoints testad)

### Native
- [ ] Unit tests för kritiska funktioner
- [ ] Benchmark tests (prestanda)
- [ ] Edge case testing

### Täckning
- [ ] Minst 70% kodtäckning på backend
- [ ] Minst 60% på frontend
- [ ] Kritiska paths täckta 100%

---

## 🚀 Prestanda & Skalning

- [ ] Inte långsammare än tidigare
- [ ] Database-queries är optimerade (inga N+1 problem)
- [ ] Build-tid rimlig (inte exponentiell ökning)

---

## ✅ Final Checklista Innan Stänga Issue

- [ ] Alla AC är uppfyllda
- [ ] Alla tests passerar
- [ ] Code review är godkänd
- [ ] Dokumentation är uppdaterad
- [ ] Git-historia är ren
- [ ] Ingen `console.log` eller debug-kod
- [ ] README är uppdaterad
- [ ] Accessibility klar (WCAG AA)
- [ ] Branch är mergad

---

**En issue är DONE när du kan stänga den och inte tänka på den igen.**
