---
name: visual_verification
description: Screenshots from dev — automatic inclusion in presentations
metadata:
  type: process
  updated: 2026-09-13
---

# 📸 VISUAL VERIFICATION — Skärmdumpar från Dev

**Skärmdumparna inkluderas AUTOMATISKT i presentationen. Ingen extra instruktion behövs.**

Du säger bara: "Ge mig en presentation till måndagsmötet"

Presentationen letar själv efter skärmdumparna och inkluderar dem.

---

## 📁 PLACERING — Där Skärmdumparna Lagras

```
_memory/screenshots/
├── 01-login.png              ← Inloggningsflödet (Frontend denna vecka)
├── 02-portfolio-dashboard.png ← Portfolio-översikt (Frontend denna vecka)
├── 03-risk-metrics.png        ← Riskmått (Backend denna vecka)
└── 04-mobile-view.png         ← Mobile-vyn (Native denna vecka)
```

---

## 🎬 PROCESS — Ta Skärmdumparna

**Före mötet (30 minuter före presentation-bygget):**

### Frontend — Login + Portfolio
```
1. Clone/pull developer-branch från avanza-team1
2. npm install
3. npm run dev (eller motsvarande)
4. Öppna http://localhost:3000
5. Login med test-konto
6. Skärmdump: Inloggningsformulär
   → Spara som: _memory/screenshots/01-login.png
7. Efter login: Skärmdump: Portfolio-dashboard
   → Spara som: _memory/screenshots/02-portfolio-dashboard.png
8. Commit & push
```

### Backend — API-data (om relevant)
```
1. Starta backend dev-server
2. Curl/Postman: GET /api/portfolio
3. Skärmdump: JSON-respons
   → Spara som: _memory/screenshots/03-api-response.png
8. Commit & push
```

### Native — Mobile View (om relevant)
```
1. Starta Native dev-server
2. Öppna i simulator eller browser
3. Skärmdump: Mobile-vyn
   → Spara som: _memory/screenshots/04-mobile-view.png
4. Commit & push
```

---

## 🤖 PRESENTATION INTEGRATION — Automatisk

**Du behöver inte säga något speciellt.**

Presentationen gör detta automatiskt:

### Slide ④ (Frontend — Vad gjordes?)
```
❌ INNAN (bara text):
✓ #40 Auth flow
  Merged PR #81 · 4 commits · klart 11 sep

✅ EFTER (text + visuell verifiering):
✓ #40 Auth flow
  Merged PR #81 · 4 commits · klart 11 sep

[SCREENSHOT: 01-login.png — Inloggningsformulär]
[SCREENSHOT: 02-portfolio-dashboard.png — Portfolio-översikt]
```

### Slide ⑤ (Backend — Vad gjordes?)
```
→ #45 FX-integration
  3 commits denna vecka · PR #82 öppen

[SCREENSHOT: 03-api-response.json — FX API-svar]
```

### Slide ⑥ (Native — Vad gjordes?)
```
→ #60 Mobile auth screen
  Design complete · Väntar på API

[SCREENSHOT: 04-mobile-view.png — Mobile-vy]
```

---

## ✅ CHECKLIST — Före Du Säger "Ge Mig En Presentation"

```
[ ] Developer-branch är uppdaterad
[ ] Dev-server startar utan fel
[ ] Du kan logga in och se portfolio
[ ] 01-login.png sparad i _memory/screenshots/
[ ] 02-portfolio-dashboard.png sparad
[ ] Committed och pushed
```

Om denna checklist är klar, säger du bara:

```
"Ge mig en presentation till måndagsmötet"
```

Presentationen hittar skärmdumparna automatiskt och inkluderar dem.

---

## 🔍 VISUELL VERIFIERING — Vad Det Visar

Skärmdumparna bevisar:

✅ **Funktionen fungerar verkligen** (inte bara på GitHub)
✅ **UX är genomtänkt** (designen är korrekt)
✅ **Integration fungerar** (data flödar korrekt)
✅ **Framstegen är verkliga** (inte bara commits)

Utan skärmdumpar:
- Presentationen säger "Auth flow är klart"
- Men ingen vet hur det ser ut

Med skärmdumpar:
- Presentationen visar hur det ser ut
- Alla förstår omedelbar vad som byggts

---

## 🤔 OM SKÄRMDUMPARNA SAKNAS

Presentationen bygger ändå — utan skärmdumparna.

```
✓ #40 Auth flow
  Merged PR #81 · 4 commits · klart 11 sep
  [Screenshot saknas]
```

Nästa gång:
- Ta skärmdumparna
- Spara i _memory/screenshots/
- Presentationen inkluderar dem automatiskt

---

**Senast uppdaterad:** 2026-09-13
