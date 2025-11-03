# Quick Start Guide

## 🎯 Get Started in 5 Minutes

### Step 1: Download
Download or clone this repository to your computer.

### Step 2: Open the Report
Double-click `report_template.html` - it opens in your browser. No installation needed!

### Step 3: Edit a Section
1. Click **"🔓 Enable Edit Mode"** button
2. Scroll to any section (e.g., "Executive Summary")
3. Type your content into the text fields
4. Click **"💾 Save Section"** at the bottom of that section
5. Enter your name when prompted

### Step 4: Handle the Downloaded File
A JSON file downloads automatically (e.g., `executive-summary_1705328400.json`). 

Move it to the `saved_sections/` folder in this project.

**Quick way:** Run this command:
```bash
python file_manager.py move
```

### Step 5: Continue Later
When you or someone else opens the report again:
1. Click **"📂 Load Saved Data"**
2. Select the JSON file(s) from `saved_sections/`
3. Everything loads automatically!

### Step 6: Generate PDF (When Done)
```bash
python report_generator.py generate
```

Then press **Ctrl+P** and choose "Save as PDF" in your browser.

---

## 💡 Pro Tips

- **Multiple People:** Each person can work on different sections at different times
- **Version Control:** JSON files track who edited what and when
- **No Server Needed:** Everything works offline on your computer
- **Auto-Save:** Your data is also saved in browser LocalStorage
- **Watch Mode:** Run `python file_manager.py watch` to auto-move JSON files

## 🧹 Clear LocalStorage (Reset Data)

If you want to start fresh and clear all locally saved data:

### Method 1: From the Browser Console
1. Open report in browser
2. Press **F12** to open Developer Tools
3. Go to **Console** tab
4. Type: `localStorage.clear()`
5. Press **Enter**
6. Refresh the page (**F5**)

### Method 2: From Browser Settings
**Chrome/Edge:**
1. Press **F12** → **Application** tab
2. Left sidebar → **Storage** → **Local Storage**
3. Right-click on your site → **Clear**

**Firefox:**
1. Press **F12** → **Storage** tab
2. Left sidebar → **Local Storage**
3. Right-click → **Delete All**

### Method 3: Clear Specific Section
Open console (F12) and type:
```javascript
localStorage.removeItem('report_data_executive-summary');
localStorage.removeItem('report_data_technical-analysis');
localStorage.removeItem('report_data_financial-analysis');
localStorage.removeItem('report_data_summary');
```

**Note:** Clearing LocalStorage only removes auto-saved browser data. Your JSON files in `saved_sections/` folder are safe!

## 🎬 Video Tutorial

Coming soon! For now, follow the steps above - it's really that simple.

## 📞 Need Help?

Check the main [README.md](README.md) or open an issue on GitHub.
