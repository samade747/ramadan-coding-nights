# Import necessary tools/libraries
import streamlit as st  # Imports Streamlit for making web apps
import random  # Imports random number generator
import time  # Imports time-related functions (used for delay)
import requests  # Imports tool for making web requests (used to fetch data from API)

# Set the title of our web app
st.title("Money Making Machine")  # Displays the main title on the Streamlit app

# Function to create random amount of money
def generate_money():
    return random.randint(1, 1000)  # Returns a random integer between 1 and 1000

# Create a section for generating money
st.subheader("Instant Cash Generator")  # Adds a subheading to the app
if st.button("Generate Money"):  # Creates a button, and runs the following code when clicked
    st.write("Counting your money...")  # Displays a message indicating a process is running
    time.sleep(5)  # Pauses the execution for 5 seconds to simulate counting money
    amount = generate_money()  # Calls the function to generate a random money amount
    st.success(f"You made ${amount}!")  # Displays a success message showing the generated amount

# Function to get side hustle ideas from a server
def fetch_side_hustle():
    try:
        # Try to get data from local server
        response = requests.get("http://127.0.0.1:8000/side_hustles")  # Sends GET request to local API server
        if response.status_code == 200:  # Checks if the request was successful (status code 200)
            hustles = response.json()  # Converts response data to JSON format
            return hustles["side_hustle"]  # Extracts and returns the "side_hustle" field from the response
        else:
            return "Freelancing"  # Returns a default hustle idea if the server fails to respond properly
    except:
        return "Something went wrong!"  # Returns an error message if request fails

# Create a section for side hustle ideas
st.subheader("Side Hustle Ideas")  # Adds a subheading for side hustle ideas
if st.button("Generate Hustle"):  # Creates a button that runs the following code when clicked
    idea = fetch_side_hustle()  # Calls function to get a side hustle idea
    st.success(idea)  # Displays the generated hustle idea as a success message

# Function to get money-related quotes from server
def fetch_money_quote():
    try:
        # Try to get quote from local server
        response = requests.get("http://127.0.0.1:8000/money_quotes")  # Sends GET request to local API server
        if response.status_code == 200:  # Checks if the request was successful (status code 200)
            quotes = response.json()  # Converts response data to JSON format
            return quotes["money_quote"]  # Extracts and returns the "money_quote" field from the response
        else:
            return "Money is the root of all evil!"  # Returns a default quote if the server fails to respond properly
    except:
        return "Something went wrong!"  # Returns an error message if request fails

# Create a section for motivation quotes
st.subheader("Money-Making Motivation")  # Adds a subheading for motivation quotes
if st.button("Get Inspired"):  # Creates a button that runs the following code when clicked
    quote = fetch_money_quote()  # Calls function to fetch a money-related quote
    st.info(quote)  # Displays the fetched quote inside an info message
