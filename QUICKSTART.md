# 🚀 Quick Start Guide - DataWhiz

## Getting Started in 3 Minutes

### 1️⃣ First Time Setup (One-time only)

```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your Groq API key
echo GROQ_API_KEY=your_api_key_here > .env
```

### 2️⃣ Launch the App

```bash
python -m streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

### 3️⃣ Try It Out

**Option A: Use Sample Data**
- Located at: `assets/sample.csv`
- Contains employee data (20 records)
- Perfect for testing features

**Option B: Upload Your Own**
- Click "📤 Upload & Preview"
- Upload CSV or Excel file
- Start analyzing!

---

## 🎯 Quick Feature Tour

### 📤 Upload & Preview
1. Upload your CSV/Excel file
2. View dataset overview
3. Check column information
4. Download processed data

### 💬 Chat & Analyze
1. Ask questions like:
   - "What's the average salary by department?"
   - "Show me the correlation between experience and salary"
   - "What are the key insights from this data?"
2. Get AI-powered answers
3. View statistical summaries

### 📈 Visualizations
1. Select chart type (Bar, Scatter, Line, etc.)
2. Choose your columns
3. Generate interactive charts
4. Explore your data visually

### 📄 Reports
1. Click "🤖 Generate AI Summary"
2. Get comprehensive analysis
3. Edit as needed
4. Export to PDF or Markdown

---

## 💡 Pro Tips

✅ **Best Practices:**
- Clean data = better insights
- Be specific with AI questions
- Use appropriate chart types
- Save reports for later reference

⚡ **Keyboard Shortcuts:**
- `Ctrl + R` - Reload app
- `Ctrl + Shift + R` - Hard reload
- `Ctrl + S` - Save (in text areas)

🔧 **Troubleshooting:**
- If charts don't show → Check column selection
- If AI doesn't respond → Verify API key in .env
- If app won't start → Run: `pip install -r requirements.txt`

---

## 📚 Example Questions to Ask

**For Employee Data:**
- What's the average salary by department?
- Who are the top performers?
- What's the correlation between experience and performance?
- Show me salary distribution by city

**For Sales Data:**
- What are the monthly trends?
- Which products sell best?
- What's the growth rate?
- Identify seasonal patterns

**For General Analysis:**
- Summarize the key findings
- What anomalies exist in the data?
- Which columns have missing values?
- Suggest areas for improvement

---

## 🎓 Learning Path

1. **Day 1:** Upload sample data → Explore features
2. **Day 2:** Upload your own data → Ask questions
3. **Day 3:** Create visualizations → Generate reports
4. **Day 4:** Master advanced queries → Share insights

---

## 🆘 Need Help?

**Common Issues:**
- Import errors → Reinstall packages
- API errors → Check `.env` file
- Slow performance → Reduce file size
- Charts not displaying → Refresh page

**Still stuck?** Check the full README.md for detailed documentation.

---

**Ready to analyze? Let's go! 🚀**

```bash
python -m streamlit run app.py
```
