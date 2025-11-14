import streamlit as st
import pandas as pd
import plotly.express as px
from modules.ai_engine import AIEngine
from modules.data_analysis import DataAnalysis
from modules.visualization import Visualizations
from modules.report_generator import ReportGenerator
from modules.data_calculator import DataCalculator

st.set_page_config(
    page_title="DataWhiz by Jericho Sonon", 
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Enhanced Custom CSS with modern design
st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary-color: #1f77b4;
        --secondary-color: #ff7f0e;
        --success-color: #2ecc71;
        --danger-color: #e74c3c;
        --background-light: #f8f9fa;
        --text-dark: #2c3e50;
    }
    
    /* Main header styling */
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeInDown 0.8s ease-in-out;
        letter-spacing: -0.5px;
    }
    
    /* Animated gradient background for header */
    .animated-gradient-header {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Stat boxes with hover effects */
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.2);
    }
    
    /* Metric cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateX(5px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Chat message styling */
    .chat-message {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        animation: slideInLeft 0.5s ease-out;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: 2rem;
    }
    
    .ai-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        margin-right: 2rem;
    }
    
    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.5;
        }
    }
    
    /* File uploader styling */
    .uploadedFile {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .uploadedFile:hover {
        border-color: #764ba2;
        background-color: rgba(102, 126, 234, 0.05);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(240, 147, 251, 0.3);
    }
    
    /* Success message */
    .success-message {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        animation: slideInLeft 0.5s ease-out;
    }
    
    /* Loading spinner */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Dataframe styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 10px 20px;
        background-color: #f0f2f6;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Tooltip styling */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    
    /* Card container */
    .card {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        margin: 1rem 0;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: 0.25rem;
    }
    
    /* Floating action button */
    .fab {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .fab:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation with modern design
st.sidebar.markdown("""
    <div style='text-align: center; padding: 1rem 0; background: white; border-radius: 10px; margin-bottom: 1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1);'>
        <h1 style='color: #667eea; font-size: 2.5rem; margin: 0;'>📊</h1>
        <h2 style='color: black; margin: 0.5rem 0; font-weight: 700;'>DataWhiz</h2>
        <p style='color: #666; font-size: 0.875rem; margin: 0;'>AI-Powered Analytics</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# Navigation with icons
page = st.sidebar.radio(
    "Navigation", 
    ["📤 Upload & Preview", "💬 Chat & Analyze", "📈 Visualizations", "📄 Reports"],
    label_visibility="collapsed"
)

# Add progress indicator with improved styling
st.sidebar.markdown("---")
if 'df' in st.session_state:
    st.sidebar.markdown("""
        <div style='background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <p style='color: white; margin: 0; font-weight: 600; text-align: center;'>✅ Dataset Loaded</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.metric("📝 Rows", f"{st.session_state['df'].shape[0]:,}")
    with col2:
        st.metric("📋 Columns", st.session_state['df'].shape[1])
else:
    st.sidebar.markdown("""
        <div style='background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
            <p style='color: white; margin: 0; font-weight: 600; text-align: center;'>📁 No Dataset Loaded</p>
        </div>
    """, unsafe_allow_html=True)

st.sidebar.markdown("---")

# Quick actions in sidebar with better styling
st.sidebar.markdown("""
    <div style='background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 1rem;'>
        <h4 style='color: #667eea; margin-bottom: 0.75rem; font-weight: 600; font-size: 0.95rem;'>⚡ Quick Actions</h4>
    </div>
""", unsafe_allow_html=True)

if st.sidebar.button("🔄 Refresh App", use_container_width=True):
    st.rerun()

if st.sidebar.button("🗑️ Clear All Data", use_container_width=True):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Initialize AI engine
if 'ai' not in st.session_state:
    st.session_state['ai'] = AIEngine()

ai = st.session_state['ai']

if page == "📤 Upload & Preview":
    st.markdown('<div class="main-header">📤 Upload Your Dataset</div>', unsafe_allow_html=True)
    
    # Welcome message with animation
    st.markdown("""
        <div class="card" style="text-align: center;">
            <h3>👋 Welcome to DataWhiz!</h3>
            <p>Upload your CSV or Excel file to start analyzing your data with AI-powered insights</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Enhanced file uploader with drag-and-drop
        st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); 
                        padding: 2rem; border-radius: 15px; border: 2px dashed #667eea; text-align: center; margin-bottom: 1rem;'>
                <h4 style='color: #667eea; margin-bottom: 1rem;'>📁 Drag & Drop Your File Here</h4>
                <p style='color: #666;'>or click to browse</p>
            </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Upload CSV or Excel file", 
            type=["csv", "xlsx"],
            label_visibility="collapsed"
        )
        
        if uploaded_file:
            # Show loading animation
            with st.spinner("🔄 Loading your data..."):
                try:
                    if uploaded_file.name.endswith("csv"):
                        df = pd.read_csv(uploaded_file)
                    else:
                        df = pd.read_excel(uploaded_file)
                    
                    st.session_state['df'] = df
                    
                    # Animated success message
                    st.markdown(f"""
                        <div class="success-message">
                            ✅ <strong>Successfully loaded:</strong> {uploaded_file.name}
                            <br>
                            <small>{df.shape[0]:,} rows × {df.shape[1]} columns</small>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Show progress bar animation
                    progress_bar = st.progress(0)
                    for i in range(100):
                        progress_bar.progress(i + 1)
                    progress_bar.empty()
                    
                    # Dataset overview with animated cards
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.subheader("📊 Dataset Overview")
                    
                    # Create 4 metric cards
                    col_a, col_b, col_c, col_d = st.columns(4)
                    
                    metrics = [
                        ("📝 Rows", f"{df.shape[0]:,}", "Total records"),
                        ("📋 Columns", df.shape[1], "Total fields"),
                        ("💾 Memory", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB", "Data size"),
                        ("🔄 Duplicates", df.duplicated().sum(), "Duplicate rows")
                    ]
                    
                    for col, (icon_label, value, delta) in zip([col_a, col_b, col_c, col_d], metrics):
                        with col:
                            st.metric(icon_label, value, delta)
                    
                    # Tabbed interface for different views
                    tab1, tab2, tab3, tab4 = st.tabs(["🔍 Data Preview", "📋 Column Info", "📊 Statistics", "🔎 Data Quality"])
                    
                    with tab1:
                        st.markdown("### 🔍 Data Preview")
                        
                        # Row selection slider
                        num_rows = st.slider("Number of rows to display", 5, min(100, len(df)), 10)
                        
                        # Search functionality
                        search_term = st.text_input("🔎 Search in data", "")
                        if search_term:
                            mask = df.astype(str).apply(lambda x: x.str.contains(search_term, case=False, na=False)).any(axis=1)
                            filtered_df = df[mask]
                            st.dataframe(filtered_df.head(num_rows), use_container_width=True, height=400)
                            st.info(f"Found {len(filtered_df)} rows containing '{search_term}'")
                        else:
                            st.dataframe(df.head(num_rows), use_container_width=True, height=400)
                    
                    with tab2:
                        st.markdown("### 📋 Column Information")
                        col_info = pd.DataFrame({
                            'Column': df.columns,
                            'Type': df.dtypes.values,
                            'Non-Null': df.count().values,
                            'Null': df.isnull().sum().values,
                            'Null %': (df.isnull().sum() / len(df) * 100).round(2).values,
                            'Unique': df.nunique().values
                        })
                        st.dataframe(col_info, use_container_width=True, height=400)
                        
                        # Column type distribution
                        st.markdown("#### 📊 Data Types Distribution")
                        type_counts = df.dtypes.value_counts()
                        fig_types = px.pie(
                            values=type_counts.values, 
                            names=type_counts.index.astype(str),
                            title="Distribution of Data Types",
                            hole=0.4
                        )
                        st.plotly_chart(fig_types, use_container_width=True)
                    
                    with tab3:
                        st.markdown("### 📊 Statistical Summary")
                        st.dataframe(df.describe(), use_container_width=True, height=400)
                        
                        # Interactive statistics
                        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
                        if numeric_cols:
                            selected_col = st.selectbox("Select column for detailed stats", numeric_cols)
                            if selected_col:
                                col_stats = df[selected_col].describe()
                                
                                stat_col1, stat_col2, stat_col3 = st.columns(3)
                                stat_col1.metric("Mean", f"{col_stats['mean']:.2f}")
                                stat_col2.metric("Median", f"{df[selected_col].median():.2f}")
                                stat_col3.metric("Std Dev", f"{col_stats['std']:.2f}")
                                
                                # Distribution plot
                                fig_dist = px.histogram(df, x=selected_col, title=f"Distribution of {selected_col}")
                                st.plotly_chart(fig_dist, use_container_width=True)
                    
                    with tab4:
                        st.markdown("### 🔎 Data Quality Check")
                        
                        # Missing values visualization
                        missing_data = df.isnull().sum()
                        missing_data = missing_data[missing_data > 0].sort_values(ascending=False)
                        
                        if len(missing_data) > 0:
                            st.warning(f"⚠️ Found {len(missing_data)} columns with missing values")
                            
                            fig_missing = px.bar(
                                x=missing_data.index, 
                                y=missing_data.values,
                                labels={'x': 'Column', 'y': 'Missing Values'},
                                title="Missing Values by Column"
                            )
                            st.plotly_chart(fig_missing, use_container_width=True)
                        else:
                            st.success("✅ No missing values found!")
                        
                        # Duplicate check
                        duplicates = df.duplicated().sum()
                        if duplicates > 0:
                            st.warning(f"⚠️ Found {duplicates} duplicate rows")
                            if st.button("🗑️ Remove Duplicates"):
                                df = df.drop_duplicates()
                                st.session_state['df'] = df
                                st.success(f"✅ Removed {duplicates} duplicate rows")
                                st.rerun()
                        else:
                            st.success("✅ No duplicate rows found!")
                    
                except Exception as e:
                    st.error(f"❌ Error loading file: {str(e)}")
                    st.info("💡 Make sure your file is a valid CSV or Excel file")
    
    with col2:
        # Tips card with animated gradient
        st.markdown("""
            <div class="info-box">
                <h3 style='margin-top: 0;'>💡 Pro Tips</h3>
                <ul style='margin-bottom: 0;'>
                    <li>📄 Supported: CSV, Excel (XLSX)</li>
                    <li>📦 Max size: 200MB</li>
                    <li>✨ Clean data = Better insights</li>
                    <li>🚀 Try sample data first!</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        # Sample data option
        st.markdown("### 📊 Try Sample Data")
        if st.button("📥 Load Sample Dataset", use_container_width=True):
            try:
                sample_df = pd.read_csv("assets/sample.csv")
                st.session_state['df'] = sample_df
                st.success("✅ Sample data loaded!")
                st.rerun()
            except Exception as e:
                st.warning(f"Sample file not found: {str(e)}. Upload your own data!")
        
        if 'df' in st.session_state:
            st.markdown("---")
            st.markdown("### 📥 Export Options")
            
            # Download CSV
            csv = st.session_state['df'].to_csv(index=False)
            st.download_button(
                "⬇️ Download as CSV",
                csv,
                "datawhiz_export.csv",
                "text/csv",
                use_container_width=True
            )
            
            # Download Excel
            from io import BytesIO
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                st.session_state['df'].to_excel(writer, index=False)
            st.download_button(
                "⬇️ Download as Excel",
                buffer.getvalue(),
                "datawhiz_export.xlsx",
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

elif page == "💬 Chat & Analyze":
    st.markdown('<div class="main-header">💬 Chat with Your Data</div>', unsafe_allow_html=True)
    
    df = st.session_state.get('df', None)
    if df is None:
        # Empty state with call to action
        st.markdown("""
            <div class="card" style="text-align: center; padding: 3rem;">
                <h2>📊 No Data Loaded Yet</h2>
                <p style="font-size: 1.2rem; color: #666; margin: 2rem 0;">
                    Upload a dataset to start chatting with your data using AI
                </p>
                <p>👈 Go to the <strong>Upload & Preview</strong> page to get started</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        data_analysis = DataAnalysis(df)
        calculator = DataCalculator(df)  # Initialize calculator
        
        # Collapsible Quick stats section
        with st.expander("📊 View Statistical Summary", expanded=False):
            st.dataframe(data_analysis.summary(), use_container_width=True, height=300)
        
        # Suggested questions as clickable chips
        st.markdown("### 💡 Quick Questions")
        suggested_questions = [
            "What are the main trends in this data?",
            "Which columns have missing values?",
            "What's the average of numeric columns?",
            "Can you summarize the key insights?",
            "Show me the data distribution"
        ]
        
        cols = st.columns(len(suggested_questions))
        for col, question in zip(cols, suggested_questions):
            with col:
                if st.button(f"💬 {question[:20]}...", use_container_width=True, key=f"quick_{question}"):
                    st.session_state['quick_question'] = question
        
        st.markdown("---")
        
        # Chat interface with modern design
        st.markdown("### 💬 Chat History")
        
        # Initialize chat history
        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []
        
        # Chat container with scrollable area
        chat_container = st.container()
        with chat_container:
            if len(st.session_state['chat_history']) == 0:
                st.info("👋 Start by asking a question about your data!")
            else:
                for i, chat in enumerate(st.session_state['chat_history']):
                    # User message
                    st.markdown(f"""
                        <div class="chat-message user-message">
                            <strong>👤 You:</strong><br>{chat['question']}
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # AI message
                    st.markdown(f"""
                        <div class="chat-message ai-message">
                            <strong>🤖 AI:</strong><br>{chat['answer']}
                        </div>
                    """, unsafe_allow_html=True)
        
        # Input area with modern design
        st.markdown("---")
        st.markdown("### ✍️ Ask Your Question")
        
        # Check for quick question
        default_question = st.session_state.get('quick_question', '')
        if default_question:
            del st.session_state['quick_question']
        
        chat_input = st.text_area(
            "Type your question here...",
            value=default_question,
            height=100,
            placeholder="e.g., What is the average value across all years?"
        )
        
        col1, col2, col3 = st.columns([2, 2, 6])
        with col1:
            send_button = st.button("🚀 Send Question", use_container_width=True, type="primary")
        with col2:
            if st.button("🗑️ Clear History", use_container_width=True):
                st.session_state['chat_history'] = []
                st.success("Chat history cleared!")
                st.rerun()
        
        if send_button and chat_input:
            with st.spinner("🤔 Analyzing your data..."):
                # First, try to provide calculated values directly
                calculated_answer = None
                try:
                    # Attempt to provide direct calculated answers for common questions
                    if any(word in chat_input.lower() for word in ['average', 'mean', 'sum', 'total', 'count', 'max', 'min', 'calculate', 'value']):
                        calculated_answer = calculator.generate_answer_with_values(chat_input)
                except Exception as e:
                    pass
                
                # Enhanced prompt with actual calculations
                prompt = f"""You are a data analyst assistant. Answer the user's question with SPECIFIC VALUES and COMPLETE ANALYSIS.

Dataset Information:
- Columns: {df.columns.tolist()}
- Shape: {df.shape[0]} rows, {df.shape[1]} columns
- Data Types: {df.dtypes.to_dict()}

Sample Data (first 5 rows):
{df.head().to_string()}

Statistical Summary:
{df.describe().to_string()}

User Question: {chat_input}

CRITICAL INSTRUCTIONS:
1. DO NOT provide Python code as an answer
2. Provide ACTUAL CALCULATED VALUES - not code snippets
3. Use the statistical summary above to derive specific numbers
4. If asking for averages, provide the actual average numbers
5. If asking for totals, provide the actual sum values
6. Format numbers clearly (e.g., $1,234.56 million or 45.2%)
7. Be specific and complete - show all requested values
8. Answer in plain English with real numbers from the data

Example of GOOD answer: "The average value is $976.17 million across all years."
Example of BAD answer: "You can calculate this using: df['Value'].mean()"

Provide a complete answer with actual values now."""
                
                answer = ai.ask(prompt)
                
                # Prepend calculated values if available
                if calculated_answer:
                    answer = f"## 📊 Calculated Values:\n\n{calculated_answer}\n\n---\n\n## 🤖 AI Analysis:\n\n{answer}"
                
                # Add additional calculated insights for numeric questions
                try:
                    if any(word in chat_input.lower() for word in ['average', 'mean', 'sum', 'total', 'count', 'max', 'min']):
                        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
                        if numeric_cols and len(numeric_cols) > 0:
                            insights = "\n\n---\n\n## 📊 Quick Data Summary:\n"
                            for col in numeric_cols[:3]:  # Limit to first 3 numeric columns
                                try:
                                    mean_val = df[col].mean()
                                    sum_val = df[col].sum()
                                    min_val = df[col].min()
                                    max_val = df[col].max()
                                    insights += f"\n**{col}:**\n"
                                    insights += f"- Average: {calculator.format_number(mean_val)}\n"
                                    insights += f"- Total: {calculator.format_number(sum_val, decimals=0)}\n"
                                    insights += f"- Range: {calculator.format_number(min_val)} to {calculator.format_number(max_val)}\n"
                                except:
                                    pass
                            answer += insights
                except Exception as e:
                    pass
                
                # Add to chat history
                st.session_state['chat_history'].append({
                    'question': chat_input,
                    'answer': answer
                })
                
                st.rerun()

elif page == "📈 Visualizations":
    st.markdown('<div class="main-header">📈 Data Visualizations</div>', unsafe_allow_html=True)
    
    df = st.session_state.get('df', None)
    if df is None:
        st.warning("⚠️ Please upload a dataset first!")
    else:
        vis = Visualizations()
        
        st.subheader("🎨 Create Visualizations")
        
        # Get numeric and categorical columns
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        all_cols = df.columns.tolist()
        
        viz_type = st.selectbox("Select Visualization Type", 
                                ["Bar Chart", "Scatter Plot", "Line Chart", "Histogram", "Box Plot", "Correlation Heatmap"])
        
        if viz_type == "Bar Chart":
            col1, col2 = st.columns(2)
            with col1:
                x = st.selectbox("X-axis", all_cols)
            with col2:
                y = st.selectbox("Y-axis", numeric_cols if numeric_cols else all_cols)
            
            if st.button("Generate Chart"):
                fig = px.bar(df, x=x, y=y, title=f"{y} by {x}")
                st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Scatter Plot":
            col1, col2, col3 = st.columns(3)
            with col1:
                x = st.selectbox("X-axis", numeric_cols if numeric_cols else all_cols)
            with col2:
                y = st.selectbox("Y-axis", numeric_cols if numeric_cols else all_cols)
            with col3:
                color = st.selectbox("Color by (optional)", ["None"] + all_cols)
            
            if st.button("Generate Chart"):
                color_col = None if color == "None" else color
                fig = px.scatter(df, x=x, y=y, color=color_col, title=f"{y} vs {x}")
                st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Line Chart":
            col1, col2 = st.columns(2)
            with col1:
                x = st.selectbox("X-axis", all_cols)
            with col2:
                y = st.selectbox("Y-axis", numeric_cols if numeric_cols else all_cols)
            
            if st.button("Generate Chart"):
                fig = px.line(df, x=x, y=y, title=f"{y} over {x}")
                st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Histogram":
            col = st.selectbox("Select Column", numeric_cols if numeric_cols else all_cols)
            bins = st.slider("Number of bins", 5, 100, 20)
            
            if st.button("Generate Chart"):
                fig = px.histogram(df, x=col, nbins=bins, title=f"Distribution of {col}")
                st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Box Plot":
            col1, col2 = st.columns(2)
            with col1:
                y = st.selectbox("Y-axis (numeric)", numeric_cols if numeric_cols else all_cols)
            with col2:
                x = st.selectbox("X-axis (category, optional)", ["None"] + all_cols)
            
            if st.button("Generate Chart"):
                x_col = None if x == "None" else x
                fig = px.box(df, x=x_col, y=y, title=f"Box Plot of {y}")
                st.plotly_chart(fig, use_container_width=True)
        
        elif viz_type == "Correlation Heatmap":
            if numeric_cols:
                if st.button("Generate Heatmap"):
                    corr = df[numeric_cols].corr()
                    fig = px.imshow(corr, text_auto=True, aspect="auto", 
                                  title="Correlation Heatmap",
                                  color_continuous_scale="RdBu_r")
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("No numeric columns available for correlation analysis")

elif page == "📄 Reports":
    st.markdown('<div class="main-header">📄 Generate Reports</div>', unsafe_allow_html=True)
    
    df = st.session_state.get('df', None)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("✍️ Report Content")
        
        if df is not None:
            if st.button("🤖 Generate AI Summary"):
                with st.spinner("Generating summary..."):
                    # Get numeric columns for correlation analysis
                    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
                    correlation_info = ""
                    if len(numeric_cols) > 1:
                        corr_matrix = df[numeric_cols].corr()
                        # Get top correlations
                        correlations = []
                        for i in range(len(corr_matrix.columns)):
                            for j in range(i+1, len(corr_matrix.columns)):
                                col1 = corr_matrix.columns[i]
                                col2 = corr_matrix.columns[j]
                                corr_val = corr_matrix.iloc[i, j]
                                if abs(corr_val) > 0.3:  # Only significant correlations
                                    correlations.append(f"{col1} vs {col2}: {corr_val:.2f}")
                        if correlations:
                            correlation_info = "\n\nTop Correlations:\n" + "\n".join(correlations[:10])
                    
                    prompt = f"""Create a comprehensive data analysis report for this dataset. Use the EXACT formatting style shown below.

Dataset Overview:
- Rows: {df.shape[0]}
- Columns: {df.shape[1]}
- Column Names: {df.columns.tolist()}

Statistical Summary:
{df.describe().to_string()}
{correlation_info}

Missing Values:
{df.isnull().sum().to_string()}

Data Types:
{df.dtypes.to_string()}

IMPORTANT: Format your response EXACTLY like this example structure:

**Comprehensive Data Analysis Report**

=====================================

**Executive Summary**

--------------------

[Provide a brief overview of the dataset and analysis objectives]

**Key Findings**

----------------

### Descriptive Statistics

*   [List key statistics with specific values, ranges, and standard deviations for each numeric column]

### Correlation Analysis

*   **[Column1] vs. [Column2]:** [Describe correlation with coefficient value]

**Data Quality Assessment**

-------------------------

### Missing Values

*   [Report on missing values]

### Data Types

*   [Report on data types]

### Data Distribution

*   [Report on distribution, outliers, etc.]

**Recommendations**

------------------

1.  **[Recommendation 1]:** [Detailed explanation]

2.  **[Recommendation 2]:** [Detailed explanation]

[Add more recommendations as needed]

**Limitations and Future Work**

------------------------------

1.  **[Limitation 1]:** [Explanation]

2.  **[Limitation 2]:** [Explanation]

**Conclusion**

--------------

[Summary of key insights and takeaways]

CRITICAL: 
- Use **bold** for section headers
- Use === and --- for separators
- Use bullet points with * for lists
- Include ACTUAL NUMERIC VALUES from the statistical summary
- Use proper markdown formatting throughout
- Be specific and detailed with numbers and statistics"""
                    
                    report_content = ai.ask(prompt)
                    st.session_state['report_content'] = report_content
                    st.success("✅ AI Summary generated! View it in the Formatted Preview tab.")
        
        # Create tabs for formatted preview and editing
        if st.session_state.get('report_content', ''):
            tab1, tab2 = st.tabs(["📄 Formatted Preview", "✏️ Edit Markdown"])
            
            with tab1:
                st.markdown("### 📄 Formatted Report Preview")
                st.markdown(st.session_state.get('report_content', ''))
            
            with tab2:
                st.markdown("### ✏️ Edit Report Content")
                edited_content = st.text_area(
                    "Report Content (Markdown)", 
                    value=st.session_state.get('report_content', ''),
                    height=400,
                    help="Edit the markdown content here. Click 'Update Preview' to see changes in the Formatted Preview tab.",
                    key="report_editor"
                )
                col_save, _ = st.columns([1, 3])
                with col_save:
                    if st.button("💾 Update Preview", use_container_width=True):
                        st.session_state['report_content'] = edited_content
                        st.success("✅ Content updated! Switch to the Formatted Preview tab to see changes.")
                        st.rerun()
        else:
            content = st.text_area(
                "Report Content", 
                value=st.session_state.get('report_content', ''),
                height=400,
                help="Write or edit your report content here. Generate an AI summary to see formatted preview."
            )
            if content:
                st.session_state['report_content'] = content
        
        st.subheader("💾 Export Options")
        col_a, col_b = st.columns(2)
        
        export_content = st.session_state.get('report_content', '')
        
        with col_a:
            if st.button("📄 Export as PDF", use_container_width=True):
                if export_content:
                    try:
                        ReportGenerator.generate_pdf("report.pdf", export_content)
                        st.success("✅ PDF generated as report.pdf")
                        with open("report.pdf", "rb") as f:
                            st.download_button("Download PDF", f, "report.pdf", "application/pdf")
                    except Exception as e:
                        st.error(f"Error generating PDF: {str(e)}")
                else:
                    st.warning("Please add content to the report first")
        
        with col_b:
            if st.button("📝 Export as Text", use_container_width=True):
                if export_content:
                    try:
                        ReportGenerator.generate_markdown("report.txt", export_content)
                        st.success("✅ Formatted text generated as report.txt")
                        # Get the formatted text content for download
                        formatted_text = ReportGenerator._parse_markdown_to_plain_text(export_content)
                        st.download_button("Download Text", formatted_text, "report.txt", "text/plain")
                    except Exception as e:
                        st.error(f"Error generating text file: {str(e)}")
                else:
                    st.warning("Please add content to the report first")
    
    with col2:
        st.info("""
        ### 📝 Report Tips
        
        - Use the AI summary button for quick insights
        - Edit the generated content as needed
        - Export to PDF or formatted Text
        - All exports show formatted content (no markdown syntax)
        - Include key findings and visualizations
        """)
        
        if df is not None:
            st.markdown("### 📊 Dataset Info")
            st.metric("Rows", df.shape[0])
            st.metric("Columns", df.shape[1])

# Enhanced Footer with modern design
st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style='text-align: center; padding: 1rem; background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);'>
        <h4 style='color: #667eea; margin-bottom: 0.5rem; font-weight: 600;'>About DataWhiz</h4>
        <p style='color: #333; font-size: 0.875rem; margin-bottom: 1rem; line-height: 1.6;'>
            Created by <strong style='color: #667eea;'>Jericho Sonon</strong><br>
            <span style='color: #666;'>AI-Powered Data Analytics Platform</span>
        </p>
        <div style='display: flex; justify-content: center; gap: 1.5rem; margin: 1rem 0;'>
            <a href='https://github.com/jlsonon' style='color: #667eea; text-decoration: none; font-weight: 500; transition: all 0.3s;'> GitHub</a>
            <a href='https://medium.com/@jlsonon12' style='color: #667eea; text-decoration: none; font-weight: 500; transition: all 0.3s;'> Medium</a>
            <a href='https://www.linkedin.com/in/jlsonon' style='color: #667eea; text-decoration: none; font-weight: 500; transition: all 0.3s;'> Linkedin</a>
        </div>
        <p style='color: #999; font-size: 0.75rem; margin-top: 1rem;'>
            Version 2.0 | © 2025
        </p>
    </div>
""", unsafe_allow_html=True)

# Main page footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%); border-radius: 15px; margin-top: 3rem;'>
        <h3 style='color: #667eea; margin-bottom: 1rem;'>🚀 Ready to Analyze More Data?</h3>
        <p style='color: #666; margin-bottom: 1.5rem;'>Upload different datasets and discover insights with AI-powered analytics</p>
        <p style='font-size: 0.875rem; color: #888;'>
            Made with Streamlit, Plotly, and Groq AI
        </p>
    </div>
""", unsafe_allow_html=True)