# 🌐 Using HTML Report System in Google Colab

This guide explains how to use the report system in Google Colab for cloud-based collaborative editing.

## ✨ Why Google Colab?

- ☁️ **No installation** - works in your browser
- 🌍 **Accessible anywhere** - just need internet
- 👥 **Easy sharing** - share URL with your team
- 💾 **Cloud storage** - data saved in Colab
- 🆓 **Free** - no costs

## 🚀 Getting Started

### Step 1: Open the Colab Notebook

Click the badge in the main README or visit:
```
https://colab.research.google.com/github/M4rceli/report/blob/main/HTML_Report_System_Colab.ipynb
```

### Step 2: Run the Setup

1. Click **Runtime** → **Run all** (or press Ctrl+F9)
2. Wait for installation (~30 seconds)
3. Look for the public URL in the output

### Step 3: Open Your Report

You'll see output like:
```
🎉 Your report is ready!

📊 Open this URL in your browser:
   https://abc123.ngrok.io

💡 This URL is accessible from anywhere!
```

Click or copy that URL - this is your live report!

### Step 4: Edit and Save

1. Open the URL in a new tab
2. Click **"🔓 Enable Edit Mode"**
3. Fill in your sections
4. Click **"💾 Save Section"**
5. Data saves directly to Colab!

## 📋 Common Tasks

### Share with Your Team

Simply send them the ngrok URL from Step 3. They can:
- View the report (read-only by default)
- Edit sections (after enabling edit mode)
- Save their changes

**Note:** Everyone needs the same Colab session to be running!

### Save Your Progress

Run this cell in Colab:
```python
# Download backup of all sections
from google.colab import files
import shutil

shutil.make_archive('saved_sections_backup', 'zip', 'saved_sections')
files.download('saved_sections_backup.zip')
```

### Continue Later

1. Open the Colab notebook again
2. Run all cells
3. Upload your backup zip file when prompted
4. All your data is restored!

### Generate PDF

Run the "Generate PDF" cell in Colab:
```python
# Generate PDF from saved sections
generator = ReportGenerator(report_folder='.')
pdf_path = generator.generate_pdf()
```

Then download it:
```python
# Download the PDF
from google.colab import files
files.download(str(pdf_path))
```

## ⚠️ Important Notes

### Session Lifetime
- Colab sessions expire after ~12 hours of inactivity
- **Always download backups** before closing
- Your data is lost when session ends

### Public URL
- The ngrok URL is temporary
- It expires when you stop the notebook
- Get a new URL each time you run the notebook

### Collaboration
- Multiple people can access the same URL
- All edits save to the same Colab session
- Coordinate who edits which section

## 🎯 Best Practices

### For Solo Use
1. Run notebook when ready to work
2. Edit sections
3. Download backup frequently
4. Generate PDF when done
5. Stop notebook to free resources

### For Team Use
1. Designate one person as "host"
2. Host runs the notebook and shares URL
3. Team members access URL to edit
4. Host downloads backups periodically
5. Host generates final PDF

### Data Management
- Download backup after each editing session
- Keep backups organized by date
- Upload backup at start of new session
- Export PDF for final version

## 🔧 Troubleshooting

### URL not working?
- Check if Colab notebook is still running
- Re-run all cells to get new URL
- Try different browser

### Can't save sections?
- Check browser console (F12) for errors
- Verify Colab session is active
- Try refreshing the page

### Lost data?
- Check if you downloaded backup
- Look in Colab's file browser (📁 icon on left)
- Check `saved_sections/` folder

### Slow performance?
- Colab free tier has limits
- Close other tabs
- Restart runtime if needed

## 💡 Tips & Tricks

### Keep Session Alive
Run this cell to prevent timeout:
```python
# Keep session alive
import time
from IPython.display import clear_output

while True:
    clear_output(wait=True)
    print("⏰ Session active:", time.strftime("%H:%M:%S"))
    time.sleep(300)  # Ping every 5 minutes
```

### Auto-Backup
Set up automatic backups:
```python
# Auto-backup every 30 minutes
import time
import shutil
from datetime import datetime

while True:
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    backup_name = f'auto_backup_{timestamp}'
    shutil.make_archive(backup_name, 'zip', 'saved_sections')
    print(f"✅ Backup created: {backup_name}.zip")
    time.sleep(1800)  # 30 minutes
```

### Custom Domain (Advanced)
Instead of ngrok random URLs, you can:
1. Sign up for ngrok account (free)
2. Get your auth token
3. Set custom subdomain in Colab

## 🆚 Colab vs Local

| Feature | Google Colab | Local Installation |
|---------|-------------|-------------------|
| Setup | None | Minimal |
| Access | Anywhere | Local machine |
| Sharing | Easy (URL) | Manual file sharing |
| Data | Temporary | Persistent |
| PDF | Cloud | Local |
| Cost | Free | Free |
| Speed | Internet-dependent | Fast |

## 📚 Additional Resources

- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)
- [Ngrok Documentation](https://ngrok.com/docs)
- [Main Project README](../README.md)

## 🎓 Video Tutorial

Coming soon: Step-by-step video guide for using Colab version!

---

**Questions?** Open an issue on GitHub or check the main documentation.
