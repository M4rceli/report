#!/usr/bin/env python3
"""
Pomocnik zarządzania plikami JSON - System raportowania
Automatycznie przenosi pliki JSON z Downloads do saved_sections
"""

import os
import shutil
from pathlib import Path
from datetime import datetime


class FileManager:
    def __init__(self, report_folder="c:/repos/report"):
        self.report_folder = Path(report_folder)
        self.saved_sections = self.report_folder / "saved_sections"
        self.downloads_folder = Path.home() / "Downloads"
        
        # Utwórz folder jeśli nie istnieje
        self.saved_sections.mkdir(exist_ok=True)
    
    def find_report_json_files(self, source_folder=None):
        """Znajdź pliki JSON raportu w folderze"""
        if source_folder is None:
            source_folder = self.downloads_folder
        
        # Wzorce nazw sekcji
        section_patterns = [
            'executive-summary_*.json',
            'technical-analysis_*.json',
            'financial-analysis_*.json',
            'summary_*.json',
            'report_complete_*.json'
        ]
        
        found_files = []
        for pattern in section_patterns:
            found_files.extend(source_folder.glob(pattern))
        
        return found_files
    
    def move_files_to_saved_sections(self):
        """Przenieś pliki JSON z Downloads do saved_sections"""
        print("\n🔍 Szukam plików JSON raportu w Downloads...")
        print("=" * 60)
        
        json_files = self.find_report_json_files()
        
        if not json_files:
            print("⚠️  Nie znaleziono plików JSON raportu w Downloads")
            print(f"📁 Szukano w: {self.downloads_folder}")
            return 0
        
        print(f"✅ Znaleziono {len(json_files)} plik(ów):\n")
        
        moved_count = 0
        for json_file in json_files:
            try:
                destination = self.saved_sections / json_file.name
                
                # Sprawdź czy plik już istnieje
                if destination.exists():
                    print(f"⚠️  Plik już istnieje: {json_file.name}")
                    overwrite = input("   Nadpisać? (t/n): ").lower().strip()
                    if overwrite != 't':
                        print("   Pominięto.\n")
                        continue
                
                # Przenieś plik
                shutil.move(str(json_file), str(destination))
                print(f"✅ Przeniesiono: {json_file.name}")
                print(f"   Do: {destination}\n")
                moved_count += 1
                
            except Exception as e:
                print(f"❌ Błąd przenoszenia {json_file.name}: {e}\n")
        
        if moved_count > 0:
            print("=" * 60)
            print(f"🎉 Przeniesiono {moved_count} plik(ów) pomyślnie!")
            print(f"📁 Lokalizacja: {self.saved_sections}")
        
        return moved_count
    
    def list_saved_sections(self):
        """Wyświetl listę zapisanych sekcji"""
        print("\n📋 Pliki w folderze saved_sections:")
        print("=" * 60)
        
        json_files = list(self.saved_sections.glob("*.json"))
        
        if not json_files:
            print("⚠️  Folder pusty")
            print(f"📁 Lokalizacja: {self.saved_sections}")
            return
        
        json_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        
        for i, json_file in enumerate(json_files, 1):
            modified = datetime.fromtimestamp(json_file.stat().st_mtime)
            size = json_file.stat().st_size
            
            print(f"{i}. {json_file.name}")
            print(f"   Data: {modified.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Rozmiar: {size} bajtów\n")
        
        print("=" * 60)
        print(f"Razem: {len(json_files)} plik(ów)")
    
    def open_folders(self):
        """Otwórz foldery w eksploratorze"""
        print("\n📂 Otwieranie folderów...")
        
        try:
            # Otwórz saved_sections
            os.startfile(str(self.saved_sections))
            print(f"✅ Otwarto: {self.saved_sections}")
            
            # Otwórz Downloads
            os.startfile(str(self.downloads_folder))
            print(f"✅ Otwarto: {self.downloads_folder}")
            
        except Exception as e:
            print(f"❌ Błąd: {e}")
    
    def auto_move_on_watch(self):
        """Automatycznie przenoś nowe pliki (tryb obserwacji)"""
        print("\n👁️  Tryb obserwacji - monitoruję folder Downloads...")
        print("Naciśnij Ctrl+C aby zatrzymać\n")
        
        import time
        processed_files = set()
        
        try:
            while True:
                json_files = self.find_report_json_files()
                
                for json_file in json_files:
                    if json_file not in processed_files:
                        print(f"\n🆕 Wykryto nowy plik: {json_file.name}")
                        
                        destination = self.saved_sections / json_file.name
                        try:
                            shutil.move(str(json_file), str(destination))
                            print(f"✅ Automatycznie przeniesiono do: saved_sections/")
                            processed_files.add(json_file)
                        except Exception as e:
                            print(f"❌ Błąd: {e}")
                
                time.sleep(2)  # Sprawdzaj co 2 sekundy
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Zatrzymano tryb obserwacji")


def main():
    """Główna funkcja programu"""
    print("=" * 60)
    print("   Pomocnik Zarządzania Plikami JSON")
    print("=" * 60)
    
    manager = FileManager()
    
    if len(os.sys.argv) > 1:
        command = os.sys.argv[1]
        
        if command == "move":
            manager.move_files_to_saved_sections()
        elif command == "list":
            manager.list_saved_sections()
        elif command == "open":
            manager.open_folders()
        elif command == "watch":
            manager.auto_move_on_watch()
        else:
            print(f"❌ Nieznana komenda: {command}")
            print("\nDostępne komendy:")
            print("  python file_manager.py move    - Przenieś pliki z Downloads")
            print("  python file_manager.py list    - Wyświetl zapisane pliki")
            print("  python file_manager.py open    - Otwórz foldery")
            print("  python file_manager.py watch   - Auto-przenoszenie (tryb obserwacji)")
    else:
        # Interaktywny tryb
        print("\n1. 📥 Przenieś pliki JSON z Downloads")
        print("2. 📋 Wyświetl zapisane pliki")
        print("3. 📂 Otwórz foldery w eksploratorze")
        print("4. 👁️  Tryb obserwacji (auto-przenoszenie)")
        print("0. Wyjście")
        
        choice = input("\nWybierz opcję: ").strip()
        
        if choice == "1":
            manager.move_files_to_saved_sections()
            input("\nNaciśnij Enter aby zakończyć...")
        elif choice == "2":
            manager.list_saved_sections()
            input("\nNaciśnij Enter aby zakończyć...")
        elif choice == "3":
            manager.open_folders()
            input("\nNaciśnij Enter aby zakończyć...")
        elif choice == "4":
            manager.auto_move_on_watch()
        elif choice == "0":
            print("Zamykanie...")
        else:
            print("❌ Nieprawidłowa opcja")


if __name__ == "__main__":
    import sys
    os.sys = sys
    main()
