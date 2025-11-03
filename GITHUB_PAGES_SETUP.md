# 🌐 Jak uruchomić GitHub Pages

## 📋 Szybka instrukcja (5 minut)

### Krok 1: Push kodu na GitHub

```bash
cd c:\repos\report

# Sprawdź status
git status

# Jeśli są zmiany, commit
git add .
git commit -m "Prepare for GitHub Pages deployment"

# Push
git push origin main
```

### Krok 2: Włącz GitHub Pages

1. **Otwórz repozytorium na GitHub:**
   ```
   https://github.com/M4rceli/report
   ```

2. **Przejdź do ustawień:**
   - Kliknij zakładkę **"Settings"** (na górze, po prawej)

3. **Znajdź sekcję Pages:**
   - Na lewym menu kliknij **"Pages"**
   - Lub przejdź bezpośrednio: `https://github.com/M4rceli/report/settings/pages`

4. **Skonfiguruj source:**
   - **Source:** `Deploy from a branch`
   - **Branch:** `main` (lub `master`)
   - **Folder:** `/ (root)`
   - Kliknij **"Save"**

5. **Poczekaj ~2 minuty:**
   - GitHub buduje stronę
   - Odśwież stronę po 2 minutach
   - Zobaczysz: "Your site is live at..."

### Krok 3: Otwórz swój raport!

Twój raport będzie dostępny pod adresem:
```
https://M4rceli.github.io/report/report_template.html
```

Lub sama strona główna (jeśli masz index.html):
```
https://M4rceli.github.io/report/
```

## 🎯 Szybki test

Otwórz w przeglądarce:
```
https://M4rceli.github.io/report/report_template.html
```

Jeśli wszystko działa, zobaczysz swój raport i będziesz mógł:
- ✅ Włączyć tryb edycji
- ✅ Wypełnić sekcje
- ✅ Zapisać dane
- ✅ Wczytać JSON
- ✅ Wygenerować PDF

## 📸 Wizualna instrukcja

### Krok po kroku ze screenshotami:

1. **GitHub → Settings**
   ```
   [Repository] → [Settings] (ikona koła zębatego)
   ```

2. **Settings → Pages**
   ```
   Lewa strona → "Pages" (w sekcji "Code and automation")
   ```

3. **Konfiguracja:**
   ```
   Build and deployment
   ├─ Source: [Deploy from a branch ▼]
   ├─ Branch: [main ▼] [/ (root) ▼] [Save]
   └─ Status: ✅ Your site is published at...
   ```

## 🔧 Zaawansowane opcje

### Opcja 1: Dodaj index.html (strona główna)

Jeśli chcesz aby główny adres `https://M4rceli.github.io/report/` od razu pokazywał raport:

```bash
# Skopiuj report_template.html jako index.html
cp report_template.html index.html
git add index.html
git commit -m "Add index.html for GitHub Pages"
git push
```

### Opcja 2: Niestandardowa domena (opcjonalnie)

1. Kup domenę (np. `mojraport.pl`)
2. W Settings → Pages → Custom domain
3. Wprowadź domenę
4. Skonfiguruj DNS u dostawcy domeny

### Opcja 3: GitHub Actions (automatyczne wdrażanie)

Stwórz `.github/workflows/deploy.yml`:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

## 🐛 Troubleshooting

### Problem: "404 - File not found"

**Rozwiązanie:**
1. Sprawdź czy plik `report_template.html` jest w głównym folderze (root)
2. Sprawdź czy jest commitowany: `git ls-files | grep report_template`
3. Sprawdź URL: musi być dokładnie `https://M4rceli.github.io/report/report_template.html`

### Problem: "Your site is having problems building"

**Rozwiązanie:**
1. Sprawdź czy branch `main` istnieje: `git branch`
2. Sprawdź czy kod jest pushowany: `git log`
3. Zobacz błędy w: Settings → Pages (na dole strony)

### Problem: Zmiany nie są widoczne

**Rozwiązanie:**
1. Poczekaj 2-5 minut (GitHub cache)
2. Hard refresh: `Ctrl + Shift + R` (lub `Cmd + Shift + R`)
3. Sprawdź w trybie incognito
4. Wyczyść cache przeglądarki

### Problem: Pliki JSON nie działają

**To jest normalne!** GitHub Pages to statyczna strona - nie ma serwera.

**Jak używać:**
1. Zapisywanie działa - pobiera JSON
2. LocalStorage działa - auto-save w przeglądarce
3. Wczytywanie działa - wybierz JSON z dysku
4. PDF działa - Ctrl+P

Wszystko działa tak samo jak lokalnie! 🎉

## ✅ Checklist

Po włączeniu GitHub Pages sprawdź:

- [ ] Strona otwiera się: `https://M4rceli.github.io/report/report_template.html`
- [ ] Raport wyświetla się poprawnie
- [ ] Przyciski działają
- [ ] Tryb edycji działa
- [ ] Zapisywanie pobiera JSON
- [ ] Wczytywanie działa
- [ ] PDF (Ctrl+P) działa
- [ ] CSS jest załadowany (strona wygląda ładnie)
- [ ] JavaScript działa (brak błędów w konsoli F12)

## 🎉 Gotowe!

Teraz możesz:

1. **Udostępnić link:** Wyślij `https://M4rceli.github.io/report/report_template.html` kolegom
2. **Użyć w prezentacji:** Pokaż live demo
3. **Dodać do CV/portfolio:** Działający projekt online
4. **Testować z dowolnego urządzenia:** Telefon, tablet, laptop

## 📝 Dodaj do README

Zaktualizuj README.md:

```markdown
## 🌐 Live Demo

**Try it now:** [https://M4rceli.github.io/report/report_template.html](https://M4rceli.github.io/report/report_template.html)

No installation needed - just open and use!
```

## 🔄 Aktualizacje

Każda zmiana na branch `main` automatycznie aktualizuje stronę:

```bash
# Zmień coś w kodzie
# Np. edytuj report_template.html

git add .
git commit -m "Update report design"
git push

# Poczekaj 2 minuty
# Strona zaktualizowana!
```

---

**Powodzenia! 🚀**

Twój raport będzie dostępny online 24/7!
