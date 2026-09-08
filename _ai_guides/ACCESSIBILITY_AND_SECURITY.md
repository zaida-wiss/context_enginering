# ♿ Accessibility & 🔒 Security & 📘 TypeScript Guidelines

**VIKTIGT:** Accessibility, Security OCH TypeScript är integrated i ALLT arbete - inte separat.

---

## 📘 TypeScript First

**Varje kodexempel MÅSTE vara TypeScript, aldrig JavaScript:**

### ✅ RÄTT - TypeScript
```typescript
interface User {
  id: string;
  email: string;
  password?: string; // Never exposed
}

function getUser(id: string): Promise<User> {
  return fetch(`/api/users/${id}`).then(r => r.json());
}
```

### ❌ FEL - JavaScript (inte acceptabelt)
```javascript
function getUser(id) {
  return fetch(`/api/users/${id}`).then(r => r.json());
}
```

### TypeScript Checklist (varje kodexempel)
- [ ] Alla funktioner har explicit returntyp (`: ReturnType`)
- [ ] Alla parametrar har typer (`: Type`)
- [ ] Interfaces för all data
- [ ] Enums för constants
- [ ] `as const` för literal types
- [ ] Generics där relevant
- [ ] `readonly` för immutable data
- [ ] `type` vs `interface` korrekt valt
- [ ] Inga `any` typer (om möjligt)
- [ ] `null` vs `undefined` explicit

---

## 🎯 Rule #1: Integrera i Kodexempel

**Varje gång AI presenterar kodexempel - MÅSTE den tänka på:**

### ♿ Accessibility
- WCAG 2.1 Level AA compliance
- Keyboard navigation (tab, enter, arrow keys)
- ARIA labels och semantic HTML
- Färgkontrast: 4.5:1 för text, 3:1 för UI-komponenter
- Alt-text för bilder
- Responsiv design från start

### 🔒 Security
- Ingen hårdkodad data (keys, passwords, tokens)
- Input validering + sanitering
- CSRF-skydd om relevant
- SQL injection prevention (use parameterized queries)
- XSS prevention (escape output)
- Authentication/Authorization correct
- Sensitive data encrypted
- Error messages som inte leaker info

### ⚡ Performance
- Inte re-rendrera onödigt (useMemo, useCallback)
- Lazy loading för komponenter
- Optimera loops (inte O(n²))
- Caching där relevant
- Minimera network requests
- Bundle size consciousness
- Debounce/throttle för events
- Inga N+1 queries

---

## 📝 Exempel: Frontend-Komponenten

### ❌ DÅLIGT (glömde accessibility + security)
```typescript
function LoginForm() {
  const [password, setPassword] = useState("");
  return (
    <form>
      <input type="text" onChange={(e) => setPassword(e.target.value)} />
      <button onClick={() => sendPassword(password)}>Login</button>
    </form>
  );
}
```

### ✅ RÄTT (accessibility + security integrerat)
```typescript
interface LoginFormProps {
  onSubmit: (credentials: LoginCredentials) => Promise<void>;
}

export function LoginForm({ onSubmit }: LoginFormProps): JSX.Element {
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const passwordInputRef = useRef<HTMLInputElement>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    
    // Validering
    if (!password || password.length < 8) {
      setError("Password must be at least 8 characters");
      return;
    }
    
    try {
      await onSubmit({ password }); // Secure: password never logged
    } catch {
      setError("Invalid credentials"); // Security: generic message
      passwordInputRef.current?.focus(); // Accessibility: focus back
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Accessibility: proper labels + ARIA */}
      <label htmlFor="password">
        Password <span aria-label="required">*</span>
      </label>
      <input
        id="password"
        ref={passwordInputRef}
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        minLength={8}
        required
        aria-describedby={error ? "error" : undefined}
      />
      
      {/* Security: error doesn't reveal if account exists */}
      {error && (
        <div id="error" role="alert" className={styles.error}>
          {error}
        </div>
      )}
      
      <button type="submit">Login</button>
    </form>
  );
}
```

---

## 🎯 Rule #2: Integrera i Projektdiskussioner

**Varje gång AI diskuterar projektet - MÅSTE den tänka på:**

### Frågor AI Ska Ställa
- "Vilka accessibility-krav gäller här?"
- "Vilka security-risker finns?"
- "Hur testar vi tillgänglighet?"
- "Hur skyddar vi känslig data?"

### Att Föra Upp
- Färgkontrast-krav från start
- Keyboard navigation design
- Data-handling policy
- Error-message handling
- Authentication flow
- HTTPS + TLS everywhere
- Secrets management (no hardcoded keys)

---

## ♿ Accessibility Checklist (för all kod)

- [ ] Semantisk HTML (nav, main, article, section)
- [ ] ARIA labels när behövs (aria-label, aria-describedby)
- [ ] Keyboard navigation: Tab, Enter, Arrow keys
- [ ] Focus visible (`:focus-visible` styling)
- [ ] Alt-text på alla bilder (meningsfull, inte "image123")
- [ ] Färgkontrast 4.5:1 för text (använd https://webaim.org/resources/contrastchecker/)
- [ ] Responsiv design (mobile-first)
- [ ] Testad med screen reader (NVDA, JAWS, VoiceOver)
- [ ] Testbar utan mus

---

## 🔒 Security Checklist (för all kod)

- [ ] Ingen API keys/tokens i kod (använd env vars)
- [ ] Input validering (type + length + whitelist)
- [ ] Output escaping (prevent XSS)
- [ ] Parameterized queries (prevent SQL injection)
- [ ] CSRF tokens om relevant
- [ ] Authentication kontrollerad
- [ ] Authorization kontrollerad (vem får göra vad?)
- [ ] Sensitive data encrypted (passwords, tokens, PII)
- [ ] Error messages generic (reveal ingen info)
- [ ] Dependencies uppdaterade (npm audit)
- [ ] HTTPS / TLS för all communication
- [ ] Rate limiting på API-endpoints
- [ ] Secrets managed properly (not in git)

---

## 🚨 Red Flags (AI Måste Säga Till)

**Accessibility Red Flags:**
- ❌ "Bara funktionsgränssnitt för desktop"
- ❌ "Färgen visar status" (utan alt-indikator)
- ❌ "Bara för musklik"
- ❌ "Ingen testning med skärmläsare"

**Security Red Flags:**
- ❌ Hardkodad API-nyckel
- ❌ Plain-text password i kod
- ❌ Ingen input-validering
- ❌ Error meddelande visar database-struktur
- ❌ Authentication skippat "för snabbhet"
- ❌ Sensitive data loggad
- ❌ Dependencies ej uppdaterade

---

## 📋 AI Workflow

**Varje gång AI ger kod eller diskuterar projektet:**

1. ✅ **Presentera lösningen**
2. ♿ **Säg vad som är gjort för accessibility**
3. 🔒 **Säg vad som är gjort för security**
4. ⚡ **Säg vad som är gjort för performance**
5. ⚠️ **Flagga om något missas** (accessibility, security ELLER performance)
6. 📚 **Länka till relevanta standarder**

### Performance Red Flags (AI måste flagga)
- ❌ Loop inuti loop (O(n²))
- ❌ Fetcha samma data flera gånger
- ❌ Re-render utan memoization
- ❌ Stora bundles utan code-splitting
- ❌ Blocking operations på main thread
- ❌ Memory leaks (event listeners inte removed)
- ❌ Inline functions i render
- ❌ Inline objects som props

---

**Version:** 1.0  
**Senast uppdaterad:** 2026-09-08  
**För:** Alla AI-assistenter på projektet

ACCESSIBILITY OCH SECURITY ÄR INTE OPTIONAL - DE ÄR FEATURES!
