#!/bin/bash

# DataWhiz - Run Script
# This script starts the Streamlit application

echo "🚀 Starting DataWhiz..."
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "💡 Creating .env.example as template..."
    if [ ! -f .env.example ]; then
        echo "GROQ_API_KEY=your_api_key_here" > .env.example
    fi
    echo "📝 Please create a .env file with your GROQ_API_KEY"
    echo "   Get your API key from: https://console.groq.com/"
    echo ""
fi

# Check if dependencies are installed
echo "🔍 Checking dependencies..."
python3 -c "import streamlit, pandas, plotly, groq" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing dependencies..."
    python3 -m pip install -r requirements.txt
fi

# Start the app
echo "✅ Starting Streamlit app..."
echo "🌐 The app will open in your browser at http://localhost:8501"
echo ""

python3 -m streamlit run app.py

