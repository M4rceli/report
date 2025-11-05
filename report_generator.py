#!/usr/bin/env python3
"""
PDF Generator from HTML files - Reporting System
Script for generating final PDF from filled HTML report
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Check available PDF libraries
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

# If no libraries available, use browser
if PDF_LIBRARY is None:
    PDF_METHOD = 'browser'
    print("ℹ️  No PDF libraries found. Use browser method (Ctrl+P -> Save as PDF)")


class ReportGenerator:
    def __init__(self, report_folder="c:/repos/report"):
        self.report_folder = Path(report_folder)
        self.data_folder = self.report_folder / "saved_sections"
        self.output_folder = self.report_folder / "generated_pdfs"
        
        # Create folders if they don't exist
        self.data_folder.mkdir(exist_ok=True)
        self.output_folder.mkdir(exist_ok=True)
    
    def load_section_data(self, section_id):
        """Load section data from JSON file"""
        json_files = list(self.data_folder.glob(f"{section_id}_*.json"))
        
        if not json_files:
            print(f"⚠️  No data found for section: {section_id}")
            return None
        
        # Get the newest file
        latest_file = max(json_files, key=lambda p: p.stat().st_mtime)
        
        with open(latest_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ Loaded section data: {section_id} from {latest_file.name}")
        return data
    
    def inject_data_into_html(self, html_path):
        """Load HTML and inject data from JSON"""
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Sections to load
        sections = [
            'overall-assessment',
            'completeness-analysis',
            'accuracy-consistency',
            'action-plan'
        ]
        
        # Load all sections
        all_data = {}
        for section_id in sections:
            data = self.load_section_data(section_id)
            if data:
                all_data[section_id] = data
        
        # Inject data into HTML (replace placeholders with actual values)
        for section_id, data in all_data.items():
            for field_id, field_value in data.get('fields', {}).items():
                # Replace content in view
                placeholder = f'id="{field_id}-view">[Enter'
                if placeholder in html_content:
                    # Find and replace
                    import re
                    pattern = f'(<div[^>]*id="{field_id}-view"[^>]*>).*?(</div>)'
                    replacement = f'\\1{field_value}\\2'
                    html_content = re.sub(pattern, replacement, html_content, flags=re.DOTALL)
            
            # Update author and date metadata
            if 'author' in data and 'timestamp' in data:
                author = data['author']
                date = datetime.fromisoformat(data['timestamp']).strftime('%Y-%m-%d %H:%M')
                
                prefix = self.get_section_prefix(section_id)
                html_content = html_content.replace(
                    f'<span id="{prefix}-author">Not saved</span>',
                    f'<span id="{prefix}-author">{author}</span>'
                )
                html_content = html_content.replace(
                    f'<span id="{prefix}-date">-</span>',
                    f'<span id="{prefix}-date">{date}</span>'
                )
        
        return html_content
    
    def get_section_prefix(self, section_id):
        """Get section prefix"""
        prefixes = {
            'overall-assessment': 'overall',
            'completeness-analysis': 'compl',
            'accuracy-consistency': 'acc',
            'action-plan': 'action'
        }
        return prefixes.get(section_id, section_id)
    
    def generate_pdf_weasyprint(self, html_content, output_path, pdf_css):
        """Generate PDF using WeasyPrint"""
        from weasyprint import HTML as WeasyprintHTML, CSS as WeasyprintCSS
        WeasyprintHTML(string=html_content, base_url=str(self.report_folder)).write_pdf(
            output_path,
            stylesheets=[WeasyprintCSS(string=pdf_css)]
        )
    
    def generate_pdf_pdfkit(self, html_content, output_path):
        """Generate PDF using pdfkit (requires wkhtmltopdf)"""
        import pdfkit
        pdfkit.from_string(html_content, str(output_path))
    
    def generate_pdf_playwright(self, html_content, output_path):
        """Generate PDF using Playwright"""
        from playwright.sync_api import sync_playwright
        
        # Save temporary HTML file
        temp_html = self.report_folder / "temp_report.html"
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"file:///{temp_html}")
            page.pdf(path=str(output_path), format='A4')
            browser.close()
        
        # Remove temporary file
        temp_html.unlink()
    
    def generate_pdf_browser(self, html_content, output_path):
        """Prepare HTML for manual printing through browser"""
        # Save filled HTML
        filled_html = self.report_folder / "report_filled.html"
        with open(filled_html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\n📄 Filled report saved: {filled_html}")
        print("\n📋 PDF Generation Instructions:")
        print("1. Open file in browser:")
        print(f"   {filled_html}")
        print("2. Press Ctrl+P (or Cmd+P on Mac)")
        print("3. Select 'Save as PDF'")
        print(f"4. Save as: {output_path.name}")
        
        # Try to open in browser
        try:
            import webbrowser
            webbrowser.open(str(filled_html))
            print("\n✅ Browser should open automatically")
        except:
            pass
        
        return filled_html
    
    def generate_pdf(self, html_path=None, output_name=None):
        """Generate PDF from HTML"""
        if html_path is None:
            html_path = self.report_folder / "report_template.html"
        
        if not os.path.exists(html_path):
            print(f"❌ HTML file does not exist: {html_path}")
            return None
        
        print(f"\n📄 Generating PDF from: {html_path}")
        print(f"🔧 Method: {PDF_METHOD}")
        print("=" * 60)
        
        # Load and inject data
        html_content = self.inject_data_into_html(html_path)
        
        # Add styles for PDF
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
        
        # Generate PDF
        if output_name is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_name = f"data_quality_report_{timestamp}.pdf"
        
        output_path = self.output_folder / output_name
        
        try:
            if PDF_METHOD == 'weasyprint':
                self.generate_pdf_weasyprint(html_content, output_path, pdf_css)
                print(f"\n✅ PDF generated successfully (WeasyPrint)!")
            elif PDF_METHOD == 'pdfkit':
                self.generate_pdf_pdfkit(html_content, output_path)
                print(f"\n✅ PDF generated successfully (pdfkit)!")
            elif PDF_METHOD == 'playwright':
                self.generate_pdf_playwright(html_content, output_path)
                print(f"\n✅ PDF generated successfully (Playwright)!")
            else:  # browser
                return self.generate_pdf_browser(html_content, output_path)
            
            print(f"📁 Location: {output_path}")
            return output_path
            
        except Exception as e:
            print(f"\n❌ Error generating PDF: {e}")
            print("\n💡 Alternative - use browser method:")
            return self.generate_pdf_browser(html_content, output_path)
    
    def list_saved_sections(self):
        """Display list of saved sections"""
        print("\n📋 Saved Sections:")
        print("=" * 60)
        
        json_files = list(self.data_folder.glob("*.json"))
        
        if not json_files:
            print("⚠️  No saved sections found")
            return
        
        # Group by section_id
        sections_data = {}
        for json_file in json_files:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                section_id = data.get('sectionId', 'unknown')
                
                if section_id not in sections_data:
                    sections_data[section_id] = []
                
                sections_data[section_id].append({
                    'file': json_file.name,
                    'author': data.get('author', 'Unknown'),
                    'timestamp': data.get('timestamp', ''),
                    'modified': datetime.fromtimestamp(json_file.stat().st_mtime)
                })
        
        # Display
        for section_id, files in sections_data.items():
            print(f"\n📌 {section_id}:")
            # Sort by modification date
            files.sort(key=lambda x: x['modified'], reverse=True)
            
            for i, file_data in enumerate(files):
                prefix = "  └─" if i == len(files) - 1 else "  ├─"
                newest = " [LATEST]" if i == 0 else ""
                print(f"{prefix} {file_data['file']}{newest}")
                print(f"     Author: {file_data['author']}")
                print(f"     Date: {file_data['modified'].strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Main program function"""
    print("=" * 60)
    print("   PDF Report Generation System")
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
            print(f"❌ Unknown command: {command}")
            print("\nAvailable commands:")
            print("  python report_generator.py list        - Display saved sections")
            print("  python report_generator.py generate    - Generate PDF")
    else:
        # Interactive mode
        print("\n1. Display saved sections")
        print("2. Generate PDF")
        print("0. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            generator.list_saved_sections()
        elif choice == "2":
            generator.generate_pdf()
        elif choice == "0":
            print("Closing...")
        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()
