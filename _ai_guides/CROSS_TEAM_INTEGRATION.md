# 🔗 Cross-Team Integration Analysis — Senior Tech Lead Guide

**Presentationen är RESULTAT av denna analys, inte en separat aktivitet.**

Innan varje sprintmöte: Läs verklig kod i pågående brancher för att décourage integrationsproblem innan teamet springer in i dem.

---

## 🎯 Fyra Slags Hjälp AI Ska Ge Varje Vecka

### 1️⃣ "Här behöver ni prata"
**Cross-team-kontrakt som saknas, är oklara eller missmatchar.**

Exempel:
```
🟡 BEHÖVER SYNKAS
Frontend (Zaida) skickar login request
↓ Kontraktuell fråga:
  Frontend: vilka fält skickas? (username + password? email + password?)
  Backend: vad förväntar du? Vilken format?
  Decision needed på mötet innan Frontend byts från mock
```

### 2️⃣ "Här riskerar ni att bygga åt olika håll"
**Branch/code mismatches som redan existerar.**

Exempel:
```
🔴 BRANCH DIVERGENCE
Backend Add/security-filter och Add/flyway-migration:
  - 75 commits efter develop (långt borta)
  - Båda modifierar AuthController, SessionSecurityFilter, pom.xml
  - Flyway lägger till databaskändringar
Problem: Vilken av de två är integrationskandidaten? Motsäger de varandra?
Beslut behövs på mötet.
```

### 3️⃣ "Här sitter någon fast, men behöver inte göra det"
**Fallback-arbete och möjlig kapacitetsomfördelning.**

Exempel:
```
Frontend väntar på Backend API
  Fallback A: Frontend testning (unabhängigt)
  Fallback B: Target-allocation responsivitet (unabhängigt)
  Fallback C: Offline-mode (unabhängigt men kan kopplas senare)
Åtgärd: Omfördela kapacitet eller switch to fallback.
```

### 4️⃣ "Här håller ni på att skapa nästa veckas problem"
**Tech debt, organisatoriska fel, otydliga ägarkskäp.**

Exempel:
```
⚠️ RISK - TEKNIK-SKULD
- Gamla brancher som inte mergats sedan 2 veckor
- #42 Login har ingen Backend-motpart ännu
- Risk-endpoint API:t är inte dokumenterat
- Två personer bör prata om samma code-område
```

---

## 📊 Integration-Kedjor: Hur Du Läser Dem

### Struktur

```
PERSON · ISSUE
↓ [teknisk handling]
LAYER/SYSTEM (Frontend/Backend/Native)
↓ [kontrakt: vad skickas/tas emot]
NÄSTA LAYER
```

### Konkret Exempel: Login-Flödet

```
Zaida · #40 Login
↓ skickar credentials
FRONTEND AUTH (drift.ts, Portfolio.tsx)
↓ HTTP POST /auth/login
  Request: { email, password }
  Response: { token, user }
API-KONTRAKT
↓ Implementeras av Backend
BACKEND AUTHCONTROLLER (Java)
↓ validerar, skapar token
SESSIONFILTER (SecurityFilter)
↓ token → session → user context
NATIVE (C++)
↓ SDK uppdaterar lokal session
MOBILAPP AUTH
```

### Hur Du Verifierar Denna Kedja

1. **Frontend-sida:** Läs Zaidas branch `frontend/#40-login`
   - Vilka filer ändras? (drift.ts, Portfolio.tsx)
   - Vilken endpoint anropas? (POST /auth/login)
   - Vilka fält skickas? (email, password, eller något annat?)

2. **API-kontrakt:** Finns det en dokumenterad spec?
   - GitHub Wiki? Figma? BESLUT.md? Shared doc?
   - Eller endast i Frontend-koden (=risk)?

3. **Backend-sida:** Vilken branch implementerar det?
   - `backend/Add/security-filter`? `backend/Add/auth`?
   - Vilka filer ändras? (AuthController, SecurityFilter, entities)
   - Motsäger det Frontend-förväntningarna?

4. **Native-sida:** Hur tas detta emot?
   - SDK-uppdateringar på `native/#XX-auth-sdk`?
   - Motsäger den Backend-implementationen?

5. **Jämför Brancher:**
   - Är alla tre brancher up-to-date med develop?
   - Ligger någon långt efter?
   - Modifierar två brancher samma filer?

---

## 📌 Status-Koder (Inte Bara MATCH/MISMATCH)

### 🟢 VERIFIERAD MATCH
```
Båda sidorna av kontraktet läst och funkar tillsammans.

Exempel:
  Frontend skickar: { email, password }
  Backend förväntar: { email, password }
  ✅ VERIFIERAD MATCH
```

### 🟡 TROLIG MATCH
```
Verkar kompatibelt men inte helt verifierat.

Exempel:
  Frontend använder fortfarande mock, inte verklig backend
  Backend-implementationen finns men är inte testresultat
  ⚠️ TROLIG MATCH (behöver integration-test)
```

### 🟠 BEHÖVER SYNKAS
```
Oklarheter eller små missmatches som kan lösas snabbt.

Exempel:
  Frontend skickar { email, password, rememberMe }
  Backend tar emot { email, password }
  Backend ignorerar rememberMe (inget fel, men inte dokumenterat)
  🟠 BEHÖVER SYNKAS — dokumentera eller ta bort fältet
```

### 🔴 MISMATCH
```
Faktisk inkompatibilitet. Koden fungerar inte tillsammans.

Exempel:
  Frontend skickar { username, password }
  Backend förväntar { email, password }
  Response-format skiljer sig
  🔴 MISMATCH — måste fixas innan integration
```

### ⚪ KAN INTE VERIFIERAS
```
En eller båda sidor saknas ännu, eller kod kan inte läsas.

Exempel:
  Backend-branchen finns inte ännu
  Frontend-branchen har ingen API-anrop ännu (bara mock)
  ⚪ KAN INTE VERIFIERAS — väntar på implementation
```

---

## 🔍 Integration-Analys: Steg-för-Steg

### 1. Läs Aktiva Brancher

```bash
git branch -a | grep -E "(frontend|backend|native)" | grep -v develop
```

Resultat för varje branch:
- Branch-namn
- Hur många commits efter develop?
- Vilka filer ändras?
- Senaste commit: när? av vem?

### 2. Identifiera Integrations-Kedjor

**Frågor att ställa:**
- Vilka Frontend-brancher anropar Backend-API:er?
- Vilka Backend-brancher implementerar dessa API:er?
- Vilka Native-brancher använder Backend-funktionalitet?
- Vilka är de kritiska kopplingar denna sprint?

**Resultat:** Lista över kedjor
```
Frontend #40 Login
  ↔ Backend AuthController
  ↔ Native AuthSDK

Frontend #43 Risk Dashboard
  ↔ Backend RiskEndpoint
  ↔ Native RiskDisplay
```

### 3. Verifiera Varje Kedja

**För varje kedja:**

```
KEDJA: Frontend #40 Login → Backend Auth → Native SDK

Frontend-sida:
  ✅ Branch: frontend/#40-login (3 commits after develop)
  ✅ Filer: drift.ts, Portfolio.tsx
  ✅ Endpoint: POST /auth/login
  ✅ Request: { email, password }
  ✅ Response: { token, expiry }

Backend-sida:
  ✅ Branch: backend/Add/security-filter (75 commits after develop - WARNING)
  ✅ Filer: AuthController, SessionSecurityFilter
  ✅ Endpoint: POST /auth/login
  ✅ Request: { email, password }
  ✅ Response: { token, expiry, user } (extra "user" - CHECK)

Native-sida:
  ⚪ Branch: INTE STARTAD ännu
  ⚪ KAN INTE VERIFIERAS
```

### 4. Klassificera Status

```
🟡 TROLIG MATCH (med varningar)

Varningar:
  - Backend-branch ligger långt efter develop (75 commits)
  - Backend returnerar extra "user"-fält → Frontend behöver veta detta
  - Native ännu inte påbörjad

Beslut behövs på mötet:
  1. Är "user" i response avsiktlig? Ska Frontend hantera det?
  2. När startar Native-branchen?
  3. Bör Backend-branchen synkas med develop först?
```

### 5. Döck Kritiska Insikter

**För presentationen:**
- Vilka kedjor MÅSTE synkas innan sprint slutar?
- Vilka kedjor riskerar att divergera?
- Vilka kedjor är fullständiga och redo att integreras?

---

## 📋 Integration-Analys Checklist (Obligatorisk)

Innan AI presenterar något måste den svara ja på ALLA dessa:

```
GIT-LÄSNING:
  ☐ Läst pågående brancher (frontend, backend, native)
  ☐ Kontrollerat antal commits efter develop för varje branch
  ☐ Identifierat vilka filer som ändras
  ☐ Noterat senaste commit-datum

INTEGRATIONS-KEDJOR:
  ☐ Mappat vilka Frontend-funktioner som behöver Backend-API
  ☐ Mappat vilka Backend-API:er som behöver Native-SDKs
  ☐ Identifierat API-kontrakt (endpoint, request/response format)
  ☐ Läst de faktiska fälten (inte antaganden från issue-namn)

VERIFIERING:
  ☐ Kontrollerat varje kedjans båda ändor
  ☐ Klassificerat status (VERIFIERAD/TROLIG/BEHÖVER SYNKAS/MISMATCH/KAN INTE VERIFIERAS)
  ☐ Identifierat divergerande brancher (långt efter develop)
  ☐ Noterat vilka brancher modifierar samma filer

KRITISKA INSIKTER:
  ☐ Vilka kedjor MÅSTE synkas denna sprint?
  ☐ Vilka kedjor divergerar redan?
  ☐ Vilka kedjor är redo att integreras?
  ☐ Vilka personpar måste prata innan integration?
```

Om något är ☐, presentationen kan inte levereras.

---

## 🎬 Integration-Slide i Presentationen

Integration-analysen resulterar i minst EN slide i presentationen.

### Format

```
INTEGRATION MAP — Denna Vecka

Frontend #40 Login (Zaida)
  ↓ POST /auth/login
  BACKEND Auth (Erik) 
  ↓ SessionFilter
  NATIVE SDK (Pär)

🟡 TROLIG MATCH
  Varning: Backend-branch långt efter develop
  Beslut: Ska "user" i response med?
```

### Multipla Kedjor

Om flera kedjor existerar, visa alla (eller flera slides):

```
CHAIN 1: Login (🟡 TROLIG MATCH)
CHAIN 2: Risk Dashboard (🔴 MISMATCH)
CHAIN 3: Offline Mode (⚪ KAN INTE VERIFIERAS)
```

---

## 💡 Exempel: Verklig Branch-Analys

**Given:** Dessa brancher är aktiva denna vecka

```
frontend/#42-drift-indicator (3 commits after develop)
  → Ändrar: drift.ts, Portfolio.tsx, services/driftApi.ts
  
backend/Add/security-filter (75 commits after develop)
  → Ändrar: AuthController, SessionSecurityFilter, entities/User.java
  
backend/Add/flyway-migration (75 commits after develop)
  → Ändrar: pom.xml, db/migration/V*.sql, AuthController
```

**Analys:**

```
KEDJA 1: Frontend #40 Login
  Frontend-sida: skickar credentials till /auth/login
  Backend-sida: AuthController + SessionSecurityFilter
  Status: 🟠 BEHÖVER SYNKAS
    Varning: två Backend-brancher modifierar AuthController!
    Fråga: Vilken är integrations-kandidaten?

KEDJA 2: Frontend #42 Drift-Indicator
  Frontend-sida: anropar /api/drift
  Backend-sida: EJ PÅBÖRJAT ännu
  Status: ⚪ KAN INTE VERIFIERAS
  
BÅDA BRANCHER:
  Ligger långt efter develop (75 commits)
  Risk: Divergerande kod, konflikter vid merge
```

**Presentationens beslut-punkt:**

```
🟠 MÅSTE SYNKAS PÅ MÖTET
- Backend: Vilken bransch är integrations-kandidaten? 
  (security-filter, flyway-migration, eller väntar vi på något tredje?)
- Databaskändringar: Flyway först eller security-filter?
- Frontend #42 driftindikator: Startar backend denna vecka?
```

---

## 🚀 Implementering för AI-er

**Varje måndagsmöte:**

1. Rensa minne (som alltid)
2. Läs DENNA fil
3. Klon/läs projekt-repot lokalt
4. Kör integrations-analysen
5. Klassificera varje kedja
6. Skapa integration-slide(n)
7. Presentera resultat med konkreta personer + branch-namn

**Du presenterar inte abstraktion. Du presenterar konkret arbete från konkreta personer.**

---

**Senast uppdaterad:** 2026-09-13  
**Syfte:** Göra AI till Senior Tech Lead som läser verklig kod före mötet  
**Status:** Obligatorisk analys före varje sprintmöte
