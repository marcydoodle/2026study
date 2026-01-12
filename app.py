import streamlit as st
import json
import os
from datetime import datetime

# Page Config
st.set_page_config(page_title="Cybersecurity PhD Roadmap", layout="wide")

# Load Roadmap Data
def load_data():
    with open('roadmap.json', 'r') as f:
        return json.load(f)

data = load_data()

# Sidebar - Progress & Navigation
st.sidebar.title("🛡️ Research Command Center")
current_week = st.sidebar.number_input("Current Week", min_value=1, max_value=52, value=1)
st.sidebar.progress(current_week / 52)

# Main Interface
st.title(f"🚀 Week {current_week} Study Portal")

# Find the current week's data
week_data = next((w for w in data['weeks'] if w['week'] == current_week), None)

if week_data:
    # Row 1: Core Subjects
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.header("🔢 Math & Logic")
        st.info(f"**Topic:** {week_data['math_topic']}")
        for day, task in week_data['math_daily'].items():
            st.checkbox(f"{day}: {task}", key=f"math_{day}")

    with col2:
        st.header("🛡️ Cyber & Python")
        st.warning(f"**Security:** {week_data['security']}")
        st.success(f"**Python:** {week_data['python']}")
        st.write("---")
        st.header("⛩️ Japanese")
        for jp_task in week_data.get('japanese_topics', []):
            st.write(f"- {jp_task}")

    # Row 2: Journaling System
    st.write("---")
    st.header("📝 Daily Research Journal")
    
    selected_day = st.selectbox("Select Day to Journal", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
    journal_path = f"journals/week_{current_week:02}_{selected_day.lower()}.md"
    
    if os.path.exists(journal_path):
        with open(journal_path, 'r') as f:
            current_content = f.read()
        
        user_entry = st.text_area("Write your 'Golden Rule' entry here:", height=300)
        
        if st.button("Save Journal Entry"):
            with open(journal_path, 'a') as f:
                f.write(f"\n\n### Entry Recorded on {datetime.now()}\n")
                f.write(user_entry)
            st.balloons()
            st.success(f"Saved to {journal_path}")
    else:
        st.error("Journal file not found. Please run Step 3 (gen_journals.py) first.")
else:
    st.error("Week data not found in roadmap.json")# Main Streamlit Dashboard Entry Point
