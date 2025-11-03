# HTML Report System with Multi-User Section Editing

A flexible HTML-based reporting system that allows multiple users to edit different sections at different times, with automatic data persistence and PDF generation.

## ✨ Features

- 🔓 **Edit/View Mode Toggle** - Safe editing with mode switching
- 💾 **Section-by-Section Saving** - Each section saves independently as JSON
- 👥 **Multi-User Support** - Different people can fill different sections
- 📅 **Metadata Tracking** - Tracks who edited each section and when
- 🔄 **Auto-Save & Load** - LocalStorage + JSON file backup
- 📄 **PDF Generation** - Multiple methods (browser, WeasyPrint, Playwright)
- 🎨 **Customizable** - Easy to add new sections and modify styling
- 🌐 **No Server Required** - Works completely offline

## 🚀 Quick Start

### Option A: Google Colab (Cloud-Based) ☁️

**Perfect for teams - no installation needed!**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/M4rceli/report/blob/main/HTML_Report_System_Colab.ipynb)

1. Click the badge above
2. Run all cells (Runtime → Run all)
3. Get a public URL to share with your team
4. Edit, save, and generate PDFs - all in the cloud!

### Option B: Local Installation 💻

### 1. Clone the Repository

```bash
git clone https://github.com/M4rceli/report.git
cd report
```

### 2. Open the Report

Simply open `report_template.html` in your browser. No installation needed!

### 3. Edit and Save

1. Click **"🔓 Enable Edit Mode"**
2. Fill in your section
3. Click **"💾 Save Section"**
4. Move the downloaded JSON file to `saved_sections/` folder

### 4. Generate PDF (Optional)

**Method A - Browser (No installation):**
```bash
python report_generator.py generate
```
Then press Ctrl+P → "Save as PDF"

**Method B - Automated (Requires WeasyPrint):**
```bash
pip install weasyprint
python report_generator.py generate
```

## 📁 Project Structure

```
html-report-system/
├── report_template.html      # Main editable HTML report
├── report_generator.py        # PDF generation script
├── file_manager.py            # JSON file management helper
├── saved_sections/            # Saved section data (JSON files)
├── generated_pdfs/            # Output PDF files
├── requirements.txt           # Python dependencies (optional)
├── README.md                  # This file
├── LICENSE                    # MIT License
└── .gitignore                 # Git ignore rules
```

## 📖 Usage Guide

### Scenario: Multi-Person Report Workflow

#### Person 1 - Project Manager (Day 1)
1. Open `report_template.html`
2. Enable edit mode
3. Fill "Executive Summary" section
4. Save section → downloads `executive-summary_*.json`
5. Move JSON to `saved_sections/` folder

#### Person 2 - Technical Lead (Day 3)
1. Open `report_template.html`
2. Click **"📂 Load Saved Data"**
3. Select all JSON files from `saved_sections/`
4. Enable edit mode
5. Fill "Technical Analysis" section
6. Save section

#### Person 3 - Finance Director (Day 5)
Same as Person 2, fill "Financial Analysis" section

#### Person 4 - Manager (Day 7) - Finalization
1. Load all saved data
2. Review all sections
3. Click **"✅ Mark as Complete"**
4. Generate final PDF

### File Management Helper

```bash
# Automatically move JSON files from Downloads
python file_manager.py move

# List saved sections
python file_manager.py list

# Open folders in file explorer
python file_manager.py open

# Watch mode (auto-move new files)
python file_manager.py watch
```

### PDF Generation Methods

```bash
# Method 1: Browser (always works, no installation)
python report_generator.py generate

# Method 2: List saved sections first
python report_generator.py list

# Method 3: Custom filename
python report_generator.py generate my_report.pdf

# Method 4: Interactive mode
python report_generator.py
```

## 🔧 Installation (Optional)

Python dependencies are **optional**. The system works without them using browser-based PDF generation.

```bash
# Optional: For automated PDF generation
pip install weasyprint

# Alternative: Playwright
pip install playwright
playwright install chromium

# Alternative: pdfkit (requires wkhtmltopdf)
pip install pdfkit
# Also install: https://wkhtmltopdf.org/downloads.html
```

## 🎨 Customization

### Adding a New Section

Edit `report_template.html` and add:

```html
<div class="section" data-section-id="new-section">
    <div class="section-header">
        <h2>5. New Section Title</h2>
        <div class="section-meta">
            <span id="new-author">Not saved</span> | 
            <span id="new-date">-</span>
        </div>
    </div>
    <div class="section-content">
        <div class="field-group">
            <label class="field-label">Description:</label>
            <div class="field-value view-mode" id="new-desc-view">
                [Enter description]
            </div>
            <textarea class="field-input edit-mode" id="new-desc" 
                style="display: none;"></textarea>
        </div>
    </div>
    <div class="section-actions">
        <button class="btn btn-success" onclick="saveSection('new-section')">
            💾 Save Section
        </button>
    </div>
</div>
```
Then update `report_generator.py` sections list:

```python
sections = [
    'executive-summary',
    'technical-analysis',
    'financial-analysis',
    'summary',
    'new-section'  # Add your new section
]
```

### Styling

Edit the `<style>` section in `report_template.html` to customize colors, fonts, and layout.

## 📋 JSON Data Format

Each saved section creates a JSON file:

```json
{
  "sectionId": "executive-summary",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "author": "John Doe",
  "fields": {
    "exec-goals": "Content here...",
    "exec-achievements": "Content here...",
    "exec-conclusions": "Content here..."
  }
}
```

## 🐛 Troubleshooting

### Data not loading?
- Check if JSON files are in `saved_sections/` folder
- Use "📂 Load Saved Data" button to manually load
- Check browser console (F12) for errors

### PDF not generating?
- Use browser method (Ctrl+P → Save as PDF)
- Check if Python script has access to folders
- Try installing WeasyPrint: `pip install weasyprint`

### Files not auto-moving?
- Run `python file_manager.py move` manually
- Check Downloads folder permissions
- Use `python file_manager.py watch` for auto-monitoring

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with vanilla JavaScript - no frameworks required
- Uses WeasyPrint, Playwright, or pdfkit for optional PDF generation
- Designed for ease of use and flexibility

## 📧 Support

If you have questions or issues:
1. Check the Troubleshooting section
2. Open an issue on GitHub
3. Review existing issues for solutions

---

**Made with ❤️ for collaborative reporting**

## 🎯 Use Cases

- Project status reports with multiple stakeholders
- Quarterly business reviews with cross-functional teams
- Research reports with different domain experts
- Audit reports with section-by-section completion
- Any collaborative document requiring structured input

## 🔒 Privacy & Security

- All data stored locally (no cloud/server)
- JSON files can be encrypted if needed
- No external dependencies for core functionality
- Works completely offline

## 📊 Version History

- **v1.0.0** - Initial release
  - Multi-section editing
  - JSON persistence
  - Multiple PDF generation methods
  - File management utilities
