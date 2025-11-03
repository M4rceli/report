# ❓ Frequently Asked Questions (FAQ)

## 🔧 LocalStorage i Dane

### Czym jest LocalStorage?
LocalStorage to funkcja przeglądarki która automatycznie zapisuje dane lokalnie na Twoim komputerze. Dzięki temu gdy ponownie otworzysz raport, Twoje dane są wciąż tam!

### Gdzie są przechowywane moje dane?
System używa **dwóch** mechanizmów zapisu:
1. **LocalStorage** - w przeglądarce (automatyczny backup)
2. **Pliki JSON** - w folderze `saved_sections/` (główne miejsce)

### Kiedy powinienem wyczyścić LocalStorage?

Wyczyść LocalStorage gdy:
- ✅ Chcesz zacząć nowy raport od zera
- ✅ Dane w LocalStorage są nieaktualne
- ✅ Widzisz stare dane które nie chcesz
- ✅ Przeglądarka pokazuje błędy
- ✅ Chcesz przetestować czysty start

### Jak wyczyścić LocalStorage?

**Metoda 1: Przycisk w raporcie (najłatwiejsza)**
1. Otwórz `report_template.html`
2. Kliknij **"🗑️ Wyczyść LocalStorage"**
3. Potwierdź

**Metoda 2: Konsola przeglądarki**
1. Naciśnij **F12**
2. Zakładka **Console**
3. Wpisz: `localStorage.clear()`
4. Enter

**Metoda 3: DevTools**
- **Chrome/Edge:** F12 → Application → Local Storage → Usuń
- **Firefox:** F12 → Storage → Local Storage → Usuń

### Czy stracę moje dane po wyczyszczeniu LocalStorage?

**NIE!** Twoje główne dane są w plikach JSON w folderze `saved_sections/`.

LocalStorage to tylko **automatyczny backup**. Możesz go wyczyścić bez obaw.

### Jak odzyskać dane po wyczyszczeniu LocalStorage?

1. Kliknij **"📂 Wczytaj zapisane dane"**
2. Wybierz pliki JSON z folderu `saved_sections/`
3. Wszystko się wczyta!

### LocalStorage vs Pliki JSON - różnice?

| Feature | LocalStorage | Pliki JSON |
|---------|-------------|------------|
| Lokalizacja | Przeglądarka | Folder `saved_sections/` |
| Trwałość | Do wyczyszczenia cache | Permanentne |
| Udostępnianie | Nie | Tak (prześlij plik) |
| Backup | Automatyczny | Ręczny (pobierany) |
| Priorytet | Backup | Główne źródło |

## 📁 Zarządzanie Plikami

### Gdzie zapisują się pliki JSON?

Domyślnie pobierają się do folderu **Downloads**. Musisz przenieść je do `saved_sections/`.

**Szybszy sposób:**
```bash
python file_manager.py move
```

### Mogę usunąć stare wersje JSON?

Tak! System zawsze używa **najnowszego** pliku dla danej sekcji.

Możesz bezpiecznie usunąć starsze wersje, np.:
- `executive-summary_1234567890.json` ← stary
- `executive-summary_1234567999.json` ← nowy (zostaw ten)

### Jak udostępnić raport innym osobom?

**Metoda 1: Pliki JSON**
1. Wyślij pliki z `saved_sections/` mailem/dyskiem
2. Druga osoba wczytuje je w swoim raporcie

**Metoda 2: Cały folder**
1. Spakuj folder `saved_sections/` do ZIP
2. Wyślij
3. Druga osoba rozpakuje i wczyta

## 🖨️ PDF Generation

### Który sposób generowania PDF jest najlepszy?

**Rekomendacje:**

1. **Brak Pythona?** → Użyj przeglądarki (Ctrl+P)
2. **Masz Python?** → Nie instaluj nic, też użyj przeglądarki
3. **Potrzebujesz automatyzacji?** → Zainstaluj WeasyPrint

### PDF wygląda źle - co robić?

1. Upewnij się że jesteś w trybie **Podgląd** (nie Edycja)
2. Użyj Ctrl+P → "Zapisz jako PDF"
3. W ustawieniach druku:
   - Margines: Domyślne
   - Skala: 100%
   - Tło: Włączone

### Czy muszę instalować Python?

**NIE!** Python jest **opcjonalny**.

System działa w 100% bez Pythona:
- ✅ HTML otwiera się w przeglądarce
- ✅ Zapisywanie działa
- ✅ PDF przez przeglądarkę

Python jest tylko dla:
- Automatycznego przenoszenia plików
- Automatycznego generowania PDF

## 👥 Praca Zespołowa

### Jak pracować w zespole?

**Workflow:**
1. **Osoba 1:** Wypełnia sekcję → zapisuje → wysyła JSON
2. **Osoba 2:** Wczytuje JSON od 1 → dodaje swoją sekcję → zapisuje → wysyła
3. **Osoba 3:** Wczytuje JSONy → dodaje swoją część
4. **Finalizacja:** Ostatnia osoba generuje PDF

### Czy można edytować równocześnie?

Nie bezpośrednio. System jest przeznaczony do edycji **sekwencyjnej**.

Alternatywa:
- Każda osoba edytuje **różne sekcje**
- Potem łączycie pliki JSON

### Jak połączyć prace od wielu osób?

1. Zbierz wszystkie pliki JSON
2. Wrzuć do `saved_sections/`
3. Otwórz raport
4. Kliknij "Wczytaj zapisane dane"
5. Wybierz wszystkie pliki

System automatycznie użyje najnowszej wersji każdej sekcji!

## 🔒 Bezpieczeństwo

### Czy moje dane są bezpieczne?

✅ **TAK** - wszystko jest **lokalnie** na Twoim komputerze:
- Brak serwera
- Brak chmury
- Brak internetu potrzebnego
- Pełna kontrola nad danymi

### Czy mogę zaszyfrować pliki JSON?

Tak! To zwykłe pliki tekstowe. Możesz:
- Zaszyfrować folder `saved_sections/`
- Użyć zaszyfrowanego dysku
- Dodać hasło do ZIP

### Co jeśli stracę pliki JSON?

Jeśli masz **LocalStorage** w przeglądarce:
1. Otwórz raport
2. Kliknij "Zapisz sekcję" dla każdej sekcji
3. Pobierze się nowy JSON

Jeśli straciłeś też LocalStorage:
- 😢 Dane są utracone
- 💡 Dlatego ważne są **backupy**!

**Wskazówka:** Regularnie kopiuj folder `saved_sections/` do backup!

## 🐛 Problemy

### Przycisk "Zapisz" nie działa

1. Sprawdź konsolę (F12) → Console
2. Sprawdź czy jesteś w trybie **Edycji**
3. Spróbuj innej przeglądarki
4. Wyczyść cache (Ctrl+F5)

### Dane się nie wczytują

1. Sprawdź czy pliki JSON są w `saved_sections/`
2. Spróbuj ręcznie: "Wczytaj zapisane dane" → wybierz pliki
3. Sprawdź czy JSON jest poprawny (otwórz w notatniku)

### Raport nie otwiera się

1. Sprawdź czy przeglądarka obsługuje JavaScript
2. Sprawdź czy plik nie jest zablokowany
3. Spróbuj innej przeglądarki

## 📚 Więcej Pomocy

- [README.md](README.md) - Pełna dokumentacja
- [QUICKSTART.md](QUICKSTART.md) - Szybki start
- [GitHub Issues](https://github.com/M4rceli/report/issues) - Zgłoś problem

---

**Nie znalazłeś odpowiedzi?** Otwórz issue na GitHub!
