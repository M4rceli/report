#!/usr/bin/env python3
"""
Generator PDF z plików HTML - System raportowania
Skrypt do generowania finalnego PDF z wypełnionego raportu HTML
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Sprawdź dostępne biblioteki PDF
PDF_LIBRARY = None
PDF_METHOD = None

try:
    from weasyprint import HTML, CSS
    PDF_LIBRARY = 'weasyprint'
    PDF_METHOD = 'weasyprint'
except ImportError:
    pass

if PDF_LIBRARY is None:
    try:
        import pdfkit
        PDF_LIBRARY = 'pdfkit'
        PDF_METHOD = 'pdfkit'
    except ImportError:
        pass

if PDF_LIBRARY is None:
    try:
        from playwright.sync_api import sync_playwright
        PDF_LIBRARY = 'playwright'
        PDF_METHOD = 'playwright'
    except ImportError:
        pass

# Jeśli brak bibliotek, użyj przeglądarki
if PDF_LIBRARY is None:
    PDF_METHOD = 'browser'
    print("ℹ️  Brak bibliotek PDF. Użyj metody przeglądarki (Ctrl+P -> Save as PDF)")


class ReportGenerator:
    def __init__(self, report_folder="c:/repos/report"):
        self.report_folder = Path(report_folder)
        self.data_folder = self.report_folder / "saved_sections"
        self.output_folder = self.report_folder / "generated_pdfs"
        
        # Utwórz foldery jeśli nie istnieją
        self.data_folder.mkdir(exist_ok=True)
        self.output_folder.mkdir(exist_ok=True)
    
    def load_section_data(self, section_id):
        """Wczytaj dane sekcji z pliku JSON"""
        json_files = list(self.data_folder.glob(f"{section_id}_*.json"))
        
        if not json_files:
            print(f"⚠️  Brak danych dla sekcji: {section_id}")
            return None
        
        # Weź najnowszy plik
        latest_file = max(json_files, key=lambda p: p.stat().st_mtime)
        
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ Wczytano dane sekcji: {section_id} z {latest_file.name}")
        return data
    
    def inject_data_into_html(self, html_path):
        """Wczytaj HTML i wstrzyknij dane z JSON"""
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Sekcje do wczytania
        sections = [
            'executive-summary',
            'technical-analysis',
            'financial-analysis',
            'summary'
        ]
        
        # Wczytaj wszystkie sekcje
        all_data = {}
        for section_id in sections:
            data = self.load_section_data(section_id)
            if data:
                all_data[section_id] = data
        
        # Wstrzyknij dane do HTML (zamień placeholder na rzeczywiste wartości)
        for section_id, data in all_data.items():
            for field_id, field_value in data.get('fields', {}).items():
                # Zamień zawartość w widoku
                placeholder = f'id="{field_id}-view">[Wprowadź'
                if placeholder in html_content:
                    # Znajdź i zamień
                    import re
                    pattern = f'(<div[^>]*id="{field_id}-view"[^>]*>).*?(</div>)'
                    replacement = f'\\1{field_value}\\2'
                    html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
            
            # Zaktualizuj metadane autora i daty
            if 'author' in data and 'timestamp' in data:
                author = data['author']
                date = datetime.fromisoformat(data['timestamp']).strftime('%Y-%m-%d %H:%M')
                
                prefix = self.get_section_prefix(section_id)
                html_content = html_content.replace(
                    f'<span id="{prefix}-author">Nie zapisano</span>',
                    f'<span id="{prefix}-author">{author}</span>'
                )
                html_content = html_content.replace(
                    f'<span id="{prefix}-date">-</span>',
                    f'<span id="{prefix}-date">{date}</span>'
                )
        
        return html_content
    
    def get_section_prefix(self, section_id):
        """Pobierz prefix sekcji"""
        prefixes = {
            'executive-summary': 'exec',
            'technical-analysis': 'tech',
            'financial-analysis': 'fin',
            'summary': 'sum'
        }
        return prefixes.get(section_id, section_id)
    
    def generate_pdf_weasyprint(self, html_content, output_path, pdf_css):
        """Generuj PDF używając WeasyPrint"""
        from weasyprint import HTML as WeasyprintHTML, CSS as WeasyprintCSS
        WeasyprintHTML(string=html_content, base_url=str(self.report_folder)).write_pdf(
            output_path,
            stylesheets=[WeasyprintCSS(string=pdf_css)]
        )
    
    def generate_pdf_pdfkit(self, html_content, output_path):
        """Generuj PDF używając pdfkit (wymaga wkhtmltopdf)"""
        import pdfkit
        pdfkit.from_string(html_content, str(output_path))
    
    def generate_pdf_playwright(self, html_content, output_path):
        """Generuj PDF używając Playwright"""
        from playwright.sync_api import sync_playwright
        
        # Zapisz tymczasowy plik HTML
        temp_html = self.report_folder / "temp_report.html"
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file:///{temp_html}")
            page.pdf(path=str(output_path), format='A4')
            browser.close()
        
        # Usuń tymczasowy plik
        temp_html.unlink()
    
    def generate_pdf_browser(self, html_content, output_path):
        """Przygotuj HTML do ręcznego drukowania przez przeglądarkę"""
        # Zapisz wypełniony HTML
        filled_html = self.report_folder / "report_filled.html"
        with open(filled_html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\n📄 Wypełniony raport zapisany: {filled_html}")
        print("\n📋 Instrukcje generowania PDF:")
        print("1. Otwórz plik w przeglądarce:")
        print(f"   {filled_html}")
        print("2. Naciśnij Ctrl+P (lub Cmd+P na Mac)")
        print("3. Wybierz 'Zapisz jako PDF'")
        print(f"4. Zapisz jako: {output_path.name}")
        
        # Spróbuj otworzyć w przeglądarce
        try:
            import webbrowser
            webbrowser.open(str(filled_html))
            print("\n✅ Przeglądarka powinna się otworzyć automatycznie")
        except:
            pass
        
        return filled_html
    
    def generate_pdf(self, html_path=None, output_name=None):
        """Wygeneruj PDF z HTML"""
        if html_path is None:
            html_path = self.report_folder / "report_template.html"
        
        if not os.path.exists(html_path):
            print(f"❌ Plik HTML nie istnieje: {html_path}")
            return None
        
        print(f"\n📄 Generowanie PDF z: {html_path}")
        print(f"🔧 Metoda: {PDF_METHOD}")
        print("=" * 60)
        
        # Wczytaj i wstrzyknij dane
        html_content = self.inject_data_into_html(html_path)
        
        # Dodaj style dla PDF
        pdf_css = """
        @media print {
            .controls, .section-actions, .btn {
                display: none !important;
            }
            body {
                background-color: white;
                padding: 0;
            }
            .container {
                box-shadow: none;
                max-width: 100%;
            }
            .field-input {
                display: none !important;
            }
            .field-value {
                display: block !important;
            }
        }
        """
        
        # Generuj PDF
        if output_name is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_name = f"raport_finalny_{timestamp}.pdf"
        
        output_path = self.output_folder / output_name
        
        try:
            if PDF_METHOD == 'weasyprint':
                self.generate_pdf_weasyprint(html_content, output_path, pdf_css)
                print(f"\n✅ PDF wygenerowany pomyślnie (WeasyPrint)!")
            elif PDF_METHOD == 'pdfkit':
                self.generate_pdf_pdfkit(html_content, output_path)
                print(f"\n✅ PDF wygenerowany pomyślnie (pdfkit)!")
            elif PDF_METHOD == 'playwright':
                self.generate_pdf_playwright(html_content, output_path)
                print(f"\n✅ PDF wygenerowany pomyślnie (Playwright)!")
            else:  # browser
                return self.generate_pdf_browser(html_content, output_path)
            
            print(f"📁 Lokalizacja: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"\n❌ Błąd generowania PDF: {e}")
            print("\n💡 Alternatywa - użyj metody przeglądarki:")
            return self.generate_pdf_browser(html_content, output_path)
    
    def list_saved_sections(self):
        """Wyświetl listę zapisanych sekcji"""
        print("\n📋 Zapisane sekcje:")
        print("=" * 60)
        
        json_files = list(self.data_folder.glob("*.json"))
        
        if not json_files:
            print("⚠️  Brak zapisanych sekcji")
            return
        
        # Grupuj po section_id
        sections_data = {}
        for json_file in json_files:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                section_id = data.get('sectionId', 'unknown')
                
                if section_id not in sections_data:
                    sections_data[section_id] = []
                
                sections_data[section_id].append({
                    'file': json_file.name,
                    'author': data.get('author', 'Nieznany'),
                    'timestamp': data.get('timestamp', ''),
                    'modified': datetime.fromtimestamp(json_file.stat().st_mtime)
                })
        
        # Wyświetl
        for section_id, files in sections_data.items():
            print(f"\n📌 {section_id}:")
            # Sortuj po dacie modyfikacji
            files.sort(key=lambda x: x['modified'], reverse=True)
            
            for i, file_data in enumerate(files):
                prefix = "  └─" if i == len(files) - 1 else "  ├─"
                newest = " [NAJNOWSZY]" if i == 0 else ""
                print(f"{prefix} {file_data['file']}{newest}")
                print(f"     Autor: {file_data['author']}")
                print(f"     Data: {file_data['modified'].strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Główna funkcja programu"""
    print("=" * 60)
    print("   System Generowania Raportów PDF")
    print("=" * 60)
    
    generator = ReportGenerator()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "list":
            generator.list_saved_sections()
        elif command == "generate":
            output_name = sys.argv[2] if len(sys.argv) > 2 else None
            generator.generate_pdf(output_name=output_name)
        else:
            print(f"❌ Nieznana komenda: {command}")
            print("\nDostępne komendy:")
            print("  python report_generator.py list        - Wyświetl zapisane sekcje")
            print("  python report_generator.py generate    - Generuj PDF")
    else:
        # Interaktywny tryb
        print("\n1. Wyświetl zapisane sekcje")
        print("2. Generuj PDF")
        print("0. Wyjście")
        
        choice = input("\nWybierz opcję: ").strip()
        
        if choice == "1":
            generator.list_saved_sections()
        elif choice == "2":
            generator.generate_pdf()
        elif choice == "0":
            print("Zamykanie...")
        else:
            print("❌ Nieprawidłowa opcja")


if __name__ == "__main__":
    main()
