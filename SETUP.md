# 🚀 Quick Setup Guide

## Installation (One-time)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   python3 -m pip install -r requirements.txt
   ```

2. **Set up your API key:**
   - Get your Groq API key from: https://console.groq.com/
   - Create a `.env` file in the project root:
     ```bash
     echo "GROQ_API_KEY=your_actual_api_key_here" > .env
     ```
   - Or copy `.env.example` to `.env` and edit it

## Running the App

### Option 1: Using the run script (easiest)
```bash
./run.sh
```

### Option 2: Direct Streamlit command
```bash
streamlit run app.py
```

### Option 3: Using Python module
```bash
python3 -m streamlit run app.py
```

## What's Been Fixed/Improved

✅ **Fixed deprecated `st.experimental_rerun()` → `st.rerun()`**
- Updated all 6 instances to use the current API

✅ **Improved error handling**
- Better error messages in AI engine
- Clear instructions when API key is missing
- Better exception handling throughout

✅ **Fixed character encoding issue**
- Fixed corrupted emoji character in Quick Data Summary section

✅ **Updated dependencies**
- Updated to compatible versions with flexible versioning (>= instead of ==)
- Added numpy to requirements

✅ **Created helper files**
- `run.sh` - Easy run script
- `.env.example` - Template for API key
- `SETUP.md` - This file

## Verification

To verify everything is set up correctly:
```bash
python3 -c "import streamlit, pandas, plotly, groq; print('✓ All dependencies OK')"
```

## Troubleshooting

**Issue: Module not found**
- Solution: Run `pip install -r requirements.txt`

**Issue: API errors**
- Solution: Check your `.env` file has the correct `GROQ_API_KEY`

**Issue: Port already in use**
- Solution: Use `streamlit run app.py --server.port 8502` to use a different port

**Issue: App won't start**
- Solution: Check Python version (needs 3.8+): `python3 --version`

## Next Steps

1. Run the app: `./run.sh` or `streamlit run app.py`
2. Upload a CSV or Excel file
3. Try the AI chat features
4. Create visualizations
5. Generate reports

Enjoy analyzing your data! 📊✨

