---
name: definition-of-done
description: Definition of Done (DoD) = checklist för när en GitHub issue är faktiskt slutförd
metadata:
  type: project_authority
  status: active
  updated: 2026-09-13
---

# ✅ Definition of Done (DoD)

**Definition of Done är en UTVECKLINGSTERMIN för när en issue är slutförd.**

Det är INTE samma som kursmål eller "Done på Project Board" — det är den faktiska tekniska checklistan för "denna feature är FÄRDIG att leverera".

---

## 🎯 AC vs DoD — KRITISK SKILLNAD

**AC (Acceptance Criteria) ≠ DoD (Definition of Done)**

```
AC = VAD ska fungera?
     ☐ Login works
     ☐ Error shows
     ☐ Redirects
     = ~20% av DoD (bara funktionalitet)

DoD = HUR säkerställer vi det är FAKTISKT klart?
      ☐ AC uppfyllda (JA, men...)
      ☐ Testade (unit, integration, E2E)
      ☐ Granskade av annan
      ☐ Dokumenterat
      ☐ Formaterad
      ☐ Git-historia ren
      ☐ Accessibility verifierad
      = 100% krav för att stänga issue
```

**AC är en DELMÄNGD av DoD** — DoD är större och omfattar hela livscykeln.

---

## ✅ DEFINITION OF DONE — Full Checklist

En issue är **DONE** när den uppfyller ALLT här:

### KÄLLKOD

- [ ] **AC är uppfyllda** — Allt som AC säger ska fungera fungerar
- [ ] **Ingen console.log** — Debug-kod är borttagen
- [ ] **Ingen TODO/FIXME** — Eller tydligt dokumenterat varför det finns
- [ ] **Linting passerar** — ESLint, Prettier, format OK
- [ ] **Ingen dead code** — Oanvänd kod är borttagen
- [ ] **Formatterad konsekvent** — Med teamets standard

### TESTER

- [ ] **Unit tests** — Kritiska funktioner täckta
- [ ] **Integration tests** — Databas/API-interaktion testad
- [ ] **E2E tests** — Kärnflödet testat end-to-end
- [ ] **Alla tests passerar** — Lokalt OCH i CI
- [ ] **Edge cases testade** — Inte bara happy path
- [ ] **Minst 70% kodtäckning** — Backend täckta väl

### CODE REVIEW

- [ ] **Granskad av annan** — Minst en annan teammedlem
- [ ] **Feedback löst** — Alla granskningskommentarer adresserade
- [ ] **Godkänd review** — Minst ett ✅-godkännande
- [ ] **Ingen self-approval** — Du kan INTE godkänna din egen PR

### DOKUMENTATION

- [ ] **README uppdaterad** — Installation, how-to, arkitektur
- [ ] **Komponenter dokumenterade** — API, inputs, outputs
- [ ] **Nya endpoints dokumenterade** — REST spec, parameters
- [ ] **Arkitektur-beslut dokumenterade** — Varför denna väg?
- [ ] **Kända brister dokumenterade** — Vad fungerar INTE än?

### GIT & COMMITS

- [ ] **Commits är logiska** — Inte "fixed stuff", utan meningsfulla
- [ ] **Commit messages tydliga** — `type(scope): message (#issue)`
- [ ] **Branch är deskriptiv** — `feature/#42-portfolio`
- [ ] **Branch är mergad** — Ej stray branches kvar
- [ ] **Git-historia ren** — Inga merge-artefakter, force-push-tecken

### ACCESSIBILITY (WCAG 2.1 AA)

- [ ] **Keyboard navigation** — Tab/Enter/Escape fungerar
- [ ] **Contrast ratios** — Text/bakgrund minst 4.5:1
- [ ] **ARIA labels** — Form inputs märkta för skärmläsare
- [ ] **Semantic HTML** — `<button>`, `<nav>`, `<main>` inte `<div>`
- [ ] **Inte bara färg** — Information måste även kunna förstås utan färg

### DEPLOYMENT & INTEGRATION

- [ ] **Kod passar in** — Ingen breaking changes
- [ ] **Beroenden uppdaterade** — package.json, pom.xml etc
- [ ] **Kan köras lokalt** — Setup-instruktioner klara
- [ ] **Environment-variables** — Inte hardkodade
- [ ] **Database-migrationer** — Dokumenterade och testade

### PRESTANDA & SÄKERHET

- [ ] **Performance OK** — Inte långsammare än tidigare
- [ ] **Database-queries optimerade** — Inga N+1-problem
- [ ] **Build passerar** — `npm run build`, `mvn clean build`
- [ ] **Linting passerar** — Inga format-fel
- [ ] **Ingen säkerhetsbuggar** — Granskat för OWASP Top 10

---

## 📋 FINAL CHECKLISTA INNAN STÄNGA ISSUE

```
FÖRE DU STÄNGER ISSUE, VERIFIERA:

☐ AC är uppfyllda
☐ Alla tests passerar (lokalt + CI)
☐ Code review är godkänd av annan
☐ Dokumentation uppdaterad
☐ Git-historia är ren (inga merge-artefakter)
☐ Ingen console.log eller debug-kod
☐ README är uppdaterad
☐ Accessibility verifierad (WCAG AA)
☐ Branch är mergad
☐ Issue kan stängas med god samvete
```

---

## 🚀 Definition of Ready (DoR) — INNAN VI BÖRJAR

En issue är **READY** att börja arbeta på när:

### Tydlighet
- [ ] **Titel är klar** — "Add portfolio dashboard" (specifikt)
- [ ] **Problem är definierat** — Vad är användarens behov?
- [ ] **Lösning är beskriven** — Vad ska vi bygga?

### Acceptance Criteria
- [ ] **3-5 mätbara AC** — Testa om det är klart
- [ ] **Inte vaga** — Inte "make it work", utan specifikt vad
- [ ] **Definition av klart** — Vad är success?

### Teknik & Beroenden
- [ ] **Scope definierad** — Frontend/Backend/Native?
- [ ] **Blockers identifierade** — Eller tydligt vad som blockerar?
- [ ] **Beroenden tydliga** — Väntar denna på något annat?
- [ ] **Estimat givet** — 4h/8h/16h/20h?

---

**En issue är DONE när du kan stänga den och aldrig tänka på den igen.**

**Senast uppdaterad:** 2026-09-13
