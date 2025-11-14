# 📊 DataWhiz - AI-Powered Data Analysis Tool

**Created by Jericho Sonon**

DataWhiz is a powerful Streamlit application that combines data analysis, visualization, and AI-powered insights to help you understand your datasets better.

## 🚀 Features

### 📤 Upload & Preview
- Support for CSV and Excel files
- Instant dataset overview with key metrics
- Column information and data types
- Missing value detection
- Duplicate row identification
- Data preview with scrollable table
- Download processed data

### 💬 Chat & Analyze
- AI-powered natural language queries
- Ask questions about your data in plain English
- Get statistical summaries and insights
- Chat history tracking
- Quick statistics display
- Suggested question prompts

### 📈 Visualizations
- **Bar Charts** - Compare categories
- **Scatter Plots** - Find correlations
- **Line Charts** - Track trends
- **Histograms** - View distributions
- **Box Plots** - Identify outliers
- **Correlation Heatmaps** - Understand relationships
- Interactive Plotly charts
- Customizable axes and colors

### 📄 Reports
- AI-generated comprehensive summaries
- Editable report content
- Export to PDF
- Export to Markdown
- Professional formatting

## 🛠️ Installation

1. **Clone or download this repository**

2. **Install required packages:**
```bash
pip install -r requirements.txt
```

3. **Set up your API key:**
   - Create a `.env` file in the project root
   - Add your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## 🎯 Usage

1. **Start the application:**
```bash
streamlit run app.py
```
or
```bash
python -m streamlit run app.py
```

2. **Open your browser:**
   - The app will automatically open at `http://localhost:8501`

3. **Upload your data:**
   - Navigate to "📤 Upload & Preview"
   - Upload a CSV or Excel file
   - Review the data overview

4. **Analyze with AI:**
   - Go to "💬 Chat & Analyze"
   - Ask questions about your data
   - Get AI-powered insights

5. **Create visualizations:**
   - Visit "📈 Visualizations"
   - Choose chart type
   - Select columns
   - Generate interactive charts

6. **Generate reports:**
   - Navigate to "📄 Reports"
   - Use AI to auto-generate summaries
   - Edit and customize
   - Export to PDF or Markdown

## 📦 Requirements

- Python 3.8+
- streamlit==1.25.0
- pandas==2.2.1
- plotly==5.16.1
- groq>=0.30.0
- python-dotenv==1.0.0
- reportlab==4.0.0
- openpyxl==3.1.2

## 🔑 Getting a Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new API key
5. Copy and add to your `.env` file

## 💡 Tips

- **Data Quality:** Clean your data before uploading for best results
- **File Size:** Keep files under 200MB for optimal performance
- **Questions:** Be specific with your AI queries for better insights
- **Visualizations:** Choose appropriate chart types for your data
- **Reports:** Use AI summaries as a starting point, then customize

## 🐛 Troubleshooting

**Import errors:**
- Make sure all packages are installed: `pip install -r requirements.txt`

**Streamlit not found:**
- Use: `python -m streamlit run app.py`

**API errors:**
- Check your `.env` file has the correct API key
- Verify your Groq API key is active

**Large files:**
- Try sampling your data first
- Use CSV instead of Excel for better performance

## 📝 Project Structure

```
day 15/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                   # API keys (not in repo)
├── README.md              # This file
├── assets/
│   ├── sample.csv        # Sample dataset
│   └── styles.css        # Custom styles
└── modules/
    ├── __init__.py       # Package init
    ├── ai_engine.py      # Groq AI integration
    ├── data_analysis.py  # Data analysis functions
    ├── visualization.py  # Chart generation
    └── report_generator.py # PDF/MD export
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements!

## 📧 Contact

Created by **Jericho Sonon**

---

**Enjoy analyzing your data with DataWhiz! 📊✨**
# day14-datawhizai
