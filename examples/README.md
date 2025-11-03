# Example Section Data

This folder contains example JSON files showing the format of saved section data.

## Usage

To see how the system works with real data:

1. Copy any example file to the `../saved_sections/` folder
2. Open `report_template.html` in your browser
3. Click "📂 Load Saved Data"
4. Select the example file

## Files

- `executive-summary_example.json` - Example executive summary section
- More examples coming soon!

## JSON Structure

Each section file contains:
- `sectionId`: Identifier for the section
- `timestamp`: ISO 8601 timestamp of when it was saved
- `author`: Name of the person who edited the section
- `fields`: Object containing all field IDs and their content

You can use these examples as templates for creating your own sections.
