---
name: protocol_snapshot
description: Snapshot of meeting protocol — FALLBACK ONLY (AI reads live Google Docs by default)
metadata:
  type: data
  snapshot_date: 2026-09-13
  snapshot_time: "08:42"
  snapshot_tz: "CEST"
  source: "Google Docs export (fallback only)"
  status: "OPTIONAL — not needed if live link works"
  instructions: "Only update if live Google Docs link fails. Otherwise leave empty."
---

# 📝 PROTOCOL SNAPSHOT — Mötesprotokoll [DATUM]

**STATUS: FALLBACK ONLY — Behövs bara om live-länken failar**

**LIVE-LÄNKEN (primär):**
https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit

AI läser denna direkt. Denna snapshot behövs INTE om länken fungerar.

---

## Om länken failar — använd denna fallback

(Uppdatera bara om Google Docs länken inte går att läsa)

Använd denna process:
1. Öppna: https://docs.google.com/document/d/1WD9XJBVrE49Csqz-XYiLgejlKlCA4t5sWiwoTkNiTD8/edit
2. Fil → Ladda ned → Vanlig text (.txt)
3. Kopiera innehållet
4. Klistra in under "MÖTESPROTOKOLLET BÖRJAR HÄR"
5. Spara denna fil
6. Commit & push

---

## 📋 MÖTESPROTOKOLLET BÖRJAR HÄR

[PLACEHOLDER — Klistra in Google Docs innehål här]

Exempel på innehål:
- Datum & tid för mötet
- Närvarande
- Agenda
- Beslut
- Åtgärder
- Nästa möte

---

## 🔧 TEKNISK INFO

**Denna fil uppdateras:**
- Före varje möte (innehål från Google Docs exporteras här)
- Manuellt (ingen automatisk synk)

**AI läser denna fil när:**
- Google Docs URL inte är åtkomlig
- Google Connector inte fungerar
- GitHub Connector inte kan läsa Google Docs

**Tidsstämpel:** `[Datum] [Tid] [Tidszon]` — visar när snapshot är från

---

**Senast uppdaterad:** 2026-09-13
