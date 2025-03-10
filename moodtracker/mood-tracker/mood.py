import streamlit as st
import pandas as pd
import datetime
import csv
import os

# Define the file name for storing mood data
MOOD_FILE = "mood_log.csv"

# Function to read mood data from the CSV file
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        return pd.DataFrame(columns=["Date", "Mood"])
    
    try:
        data = pd.read_csv(MOOD_FILE)
        if "Date" not in data.columns or "Mood" not in data.columns:
            return pd.DataFrame(columns=["Date", "Mood"])
        return data
    except Exception as e:
        st.error(f"Error loading mood data: {e}")
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to add new mood entry to CSV file
def save_mood_data(date, mood):
    file_exists = os.path.exists(MOOD_FILE)
    with open(MOOD_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Mood"])
        writer.writerow([date, mood])

# Streamlit app title with styled markdown
st.set_page_config(page_title="Mood Tracker", page_icon="😊", layout="wide")
st.markdown("# 🌈 Mood Tracker")
st.markdown("#### Track how you feel daily and analyze your mood trends!")

# Sidebar with info and styling
with st.sidebar:
    st.markdown("## About the App")
    st.info("This app helps you track your moods over time and visualize trends.")
    st.markdown("Built with ❤️ by [samad](https://github.com/samade747)")
    st.markdown("---")
    st.markdown("### Select a Date")
    selected_date = st.date_input("Pick a date", datetime.date.today())

# Mood selection options with emojis
mood_options = {
    "😃 Happy": "Happy",
    "😢 Sad": "Sad",
    "😡 Angry": "Angry",
    "😐 Neutral": "Neutral",
    "😌 Relaxed": "Relaxed",
    "😴 Tired": "Tired",
    "😕 Confused": "Confused",
    "🤩 Excited": "Excited",
    "🥰 Loved": "Loved",
    "🤯 Stressed": "Stressed",
}

st.subheader("How are you feeling today?")
mood = st.selectbox("Select your mood", list(mood_options.keys()))

# Button to log mood
if st.button("Log Mood"):
    save_mood_data(selected_date, mood_options[mood])
    st.success(f"Mood Logged Successfully for {selected_date}!")

# Load mood data and display if available
data = load_mood_data()
if not data.empty:
    st.subheader("📊 Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')
    data = data.dropna()
    
    # Show data in a table
    st.dataframe(data.sort_values(by="Date", ascending=False), height=250)
    
    # Mood count visualization
    mood_counts = data["Mood"].value_counts()
    st.bar_chart(mood_counts)
    
    # Line chart for trends
    mood_trends = data.groupby("Date")["Mood"].count()
    st.line_chart(mood_trends)
