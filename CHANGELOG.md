# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-15

### Added
- Initial release of HTML Report System
- Multi-section editable HTML report template
- Edit/View mode toggle functionality
- Section-by-section saving to JSON files
- LocalStorage auto-save backup
- Metadata tracking (author, timestamp)
- PDF generation with multiple methods:
  - Browser-based (no dependencies)
  - WeasyPrint support
  - Playwright support
  - pdfkit support
- File management utility (`file_manager.py`)
  - Auto-move files from Downloads
  - List saved sections
  - Watch mode for automatic file handling
- Report generator utility (`report_generator.py`)
  - List saved sections
  - Generate PDF from saved data
  - Interactive and command-line modes
- Four pre-configured sections:
  - Executive Summary
  - Technical Analysis
  - Financial Analysis
  - Summary and Next Steps
- Comprehensive documentation
- MIT License
- Example JSON files

### Features
- No server required - works completely offline
- Multi-user collaboration support
- Responsive design
- Print-friendly styling
- Cross-browser compatible
- Easy customization and extensibility

## [Unreleased]

### Planned
- Real-time collaboration features
- Cloud storage integration options
- More section templates
- Import/export to other formats (Word, Markdown)
- Dark mode support
- Mobile-optimized editing interface
- Version comparison tool
- Comment/feedback system
