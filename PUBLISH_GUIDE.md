# 🚀 Instrukcje publikacji na GitHub

## Kroki do opublikowania repozytorium M4rceli/report

### 1. Przygotowanie repozytorium lokalnego

```bash
cd c:\repos\report

# Inicjalizuj Git (jeśli jeszcze nie zrobione)
git init

# Dodaj wszystkie pliki
git add .

# Sprawdź co zostanie dodane
git status

# Commit
git commit -m "Initial release v1.0.0 - HTML Report System with Colab support"
```

### 2. Połączenie z GitHub

```bash
# Dodaj remote (jeśli repozytorium już istnieje na GitHub)
git remote add origin https://github.com/M4rceli/report.git

# Lub jeśli remote już istnieje, zaktualizuj:
git remote set-url origin https://github.com/M4rceli/report.git

# Sprawdź remote
git remote -v
```

### 3. Push do GitHub

```bash
# Push do main branch
git branch -M main
git push -u origin main
```

Jeśli wystąpi błąd (np. repozytorium już ma zawartość), użyj:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### 4. Weryfikacja

Po pushu sprawdź czy wszystko jest na GitHub:
- ✅ README.md wyświetla się poprawnie
- ✅ Wszystkie pliki są obecne
- ✅ Foldery (saved_sections, generated_pdfs, examples, docs) istnieją
- ✅ HTML raport działa lokalnie

### 5. Test lokalny

Otwórz raport lokalnie aby sprawdzić:
- ✅ HTML otwiera się w przeglądarce
- ✅ Tryb edycji działa
- ✅ Zapisywanie sekcji działa
- ✅ Wczytywanie danych działa
- ✅ File manager działa (jeśli używasz Pythona)

### 6. Stwórz Release (opcjonalnie)

Na GitHub:
1. Przejdź do **Releases**
2. Kliknij **"Create a new release"**
3. Tag: `v1.0.0`
4. Title: `Initial Release - HTML Report System`
5. Description:
   ```markdown
   # 🎉 Initial Release v1.0.0
   
   Multi-user HTML report system with Google Colab support!
   
   ## ✨ Features
   - Edit/View mode toggle
   - Section-by-section saving
   - Multi-user collaboration
   - Google Colab integration
   - PDF generation (multiple methods)
   - No server required
   
   ## 🚀 Quick Start
   - Local: Clone and open `report_template.html`
   - Cloud: Click the "Open in Colab" badge
   
   ## 📖 Documentation
   - [README.md](README.md) - Full documentation
   - [QUICKSTART.md](QUICKSTART.md) - 5-minute guide
   - [Colab Guide](docs/COLAB_GUIDE.md) - Cloud usage
   ```
6. Kliknij **"Publish release"**

### 7. Zaktualizuj opis repozytorium

Na stronie głównej repozytorium dodaj:

**Description:**
```
HTML-based reporting system with multi-user editing and Google Colab support
```

**Topics (tags):**
- `html`
- `reporting`
- `collaboration`
- `pdf-generation`
- `javascript`
- `python`
- `no-server`
- `offline-first`

**Website (optional):**
```
https://m4rceli.github.io/report/report_template.html
```
(if you enable GitHub Pages)

### 8. Opcjonalnie - GitHub Pages

Możesz włączyć GitHub Pages dla live demo:

1. Settings → Pages
2. Source: **Deploy from branch**
3. Branch: **main** → folder: **/ (root)**
4. Save

Twój raport będzie dostępny pod:
```
https://M4rceli.github.io/report/report_template.html
```

Możesz wtedy dodać link w README:
```markdown
🔗 [Live Demo](https://M4rceli.github.io/report/report_template.html)
```

### 9. Dodaj badges do README (opcjonalnie)

Możesz dodać więcej badges:

```markdown
![GitHub release](https://img.shields.io/github/v/release/M4rceli/report)
![GitHub stars](https://img.shields.io/github/stars/M4rceli/report)
![GitHub license](https://img.shields.io/github/license/M4rceli/report)
![GitHub last commit](https://img.shields.io/github/last-commit/M4rceli/report)
```

### 10. Share!

Podziel się swoim projektem:
- Twitter/LinkedIn
- Reddit (r/webdev, r/Python)
- Dev.to
- Hacker News

---

## 🔧 Komendy pomocnicze

### Aktualizacja po zmianach
```bash
git add .
git commit -m "Update: opis zmian"
git push
```

### Sprawdzenie statusu
```bash
git status
git log --oneline
```

### Cofnięcie zmian
```bash
# Cofnij ostatni commit (zachowaj zmiany)
git reset --soft HEAD~1

# Cofnij wszystko (UWAGA: usuwa zmiany!)
git reset --hard HEAD~1
```

### Branch do nowych funkcji
```bash
# Stwórz nowy branch
git checkout -b feature/nowa-funkcja

# Wróć do main
git checkout main

# Merge branch
git merge feature/nowa-funkcja
```

---

## ✅ Checklist przed publikacją

- [ ] Wszystkie pliki commitowane
- [ ] README.md zaktualizowany z prawidłowymi linkami
- [ ] Pliki Colab usunięte (jeśli nie są potrzebne)
- [ ] LICENSE file obecny
- [ ] .gitignore skonfigurowany
- [ ] HTML raport przetestowany lokalnie
- [ ] Przykładowe pliki JSON w examples/
- [ ] Dokumentacja kompletna
- [ ] GitHub remote dodany
- [ ] Push wykonany pomyślnie
- [ ] Repozytorium publiczne

---

**Powodzenia z publikacją! 🚀**
