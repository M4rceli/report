# Data Quality Report System with Multi-User Section Editing

A flexible HTML-based Data Quality reporting system that allows multiple users to edit different sections at different times, with automatic data persistence and PDF generation.

## Demo

👉 **[https://M4rceli.github.io/report/report_template.html](https://M4rceli.github.io/report/report_template.html)**

Open the link, click "Enable Edit Mode", and start editing!

## ✨ Features

-  **Edit/View Mode Toggle** - Safe editing with mode switching
-  **Section-by-Section Saving** - Each section saves independently as JSON
-  **Multi-User Support** - Different people can fill different sections
-  **Metadata Tracking** - Tracks who edited each section and when
-  **Auto-Save & Load** - LocalStorage + JSON file backup
-  **PDF Generation** - Multiple methods (browser, WeasyPrint, Playwright)
-  **Customizable** - Easy to add new sections and modify styling
-  **No Server Required** - Works completely offline

##  Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/M4rceli/report.git
cd report
```

### 2. Open the Report

Simply open `report_template.html` in your browser. No installation needed!

### 3. Edit and Save

1. Click **" Enable Edit Mode"**
2. Fill in your section
3. Click **" Save Section"**
4. Move the downloaded JSON file to `saved_sections/` folder

### 4. Generate PDF (Optional)


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
