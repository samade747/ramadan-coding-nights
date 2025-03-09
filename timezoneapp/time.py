import streamlit as st
from datetime import datetime, date
from zoneinfo import ZoneInfo

# Set page config with title and wide layout
st.set_page_config(page_title="Time Zone App", layout="wide")

# CSS for styling the app title and subheaders
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subheader {
        font-size: 1.5em;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# App Title
st.markdown("<div class='title'>Time Zone App</div>", unsafe_allow_html=True)

# Sidebar instructions
st.sidebar.header("Instructions")
st.sidebar.info("""
Select one or more time zones to view the current time.
Use the conversion section to convert time between different time zones.
You can also choose a specific date for conversion.
""")

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Display current times for selected time zones
st.subheader("Current Time in Selected Timezones")
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Add a refresh button to update current times
if st.button("Refresh Current Times"):
    st.experimental_rerun()

for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

# Time conversion section
st.subheader("Convert Time Between Timezones")

# Date input for selecting the conversion date
selected_date = st.date_input("Select Date", value=datetime.today().date())

# Time input field (defaulting to the current time)
current_time_input = st.time_input("Select Time", value=datetime.now().time())

# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

# Dropdown to select target timezone
to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

# Convert time when button is clicked
if st.button("Convert Time"):
    try:
        # Combine the selected date and time with the source timezone
        dt = datetime.combine(selected_date, current_time_input, tzinfo=ZoneInfo(from_tz))
        # Convert to the target timezone
        converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
        st.success(f"Converted Time in {to_tz}: {converted_time}")
    except Exception as e:
        st.error(f"Error converting time: {e}")

st.info("Note: Time conversion takes into account Daylight Saving Time changes if applicable.")

# About section
st.markdown("---")
st.subheader("About This App")
st.write("""
This Enhanced Time Zone App allows you to view the current time in multiple time zones 
and convert times between them. Simply select your desired time zones, set a time and date, 
and the app will display the converted time.
""")
