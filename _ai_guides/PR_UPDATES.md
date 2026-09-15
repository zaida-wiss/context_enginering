# 📋 PR Updates & Reviews (Fallback)

**VIKTIGT för AI:** Läs denna fil innan du ger svar om projektstatus!

Denna fil är fallback när GitHub PR-kommentarer inte kan läsas direkt via API.

🔗 **Alla externa datakällor:** Se [`_memory/EXTERNAL_SOURCES.md`](../_memory/EXTERNAL_SOURCES.md) för centraliserad register över Google Sheets, Google Docs, GitHub och alla fallback-URLs.

---

## ⚠️ AI-INSTRUKTION

**När användaren frågar: "Vad är projektets status?" eller "Vad är det för PRs öppna?"**

1. ✅ Försök läsa från GitHub: `https://github.com/chas-challenge-2026/avanza-team1/pulls`
2. ✅ Fallback: Läs denna fil (`PR_UPDATES.md`)
3. ✅ Fallback 2: Kolla Google Sheets: `See EXTERNAL_SOURCES.yaml: GOOGLE_PROJECT_DATA_SHEET`
4. ✅ **BERÄTTA vilken källa du använt:** "Läst från: [GitHub / denna fil / Google Sheets]"

---

## Format för PR-Updates

Lägg till nya PRs här med detta format:

```markdown
## PR #XX - [Branch Name]

**Status:** In Review / Approved / Changes Requested  
**Från:** [Developer Name]  
**Reviewers:** [Names]  

**Vad gör denna PR:**
- Kort beskrivning

**Key Changes:**
- Change 1
- Change 2

**Reviewer Comments (Sammanfattat):**
- Comment 1
- Comment 2

**Checklista:**
- [ ] Code review done
- [ ] Tests passing
- [ ] Documentation updated
- [ ] Ready to merge
```

---

## Senaste PRs

*(Uppdatera denna lista med nya PRs)*

---

**Tips för uppdatering:**
- Lägg bara in PRs som är "In Review" eller nya
- Når en PR är mergad, ta bort från denna lista
- Uppdatera när du skapat nya PRs

**Senast uppdaterad:** [Datum]
