import streamlit as st  # Import Streamlit for creating the web-based UI

import random  # Import the random module to randomly select characters for the password

import string  # Import string to use predefined character sets (letters, digits, special characters)


# Function to generate a random password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Start with uppercase and lowercase letters (A-Z, a-z)

    if use_digits:
        characters += string.digits  # Add numbers (0-9) if the user selects this option

    if use_special:
        characters += string.punctuation  # Add special characters (!@#$%^&* etc.) if the user selects this option

    # Generate a password by randomly selecting characters from the chosen set
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI setup
st.title("Simple Password Generator by smaad")  # Display the app title on the web page

# User input: password length (slider to select length between 6 and 32 characters, default set to 12)
length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9), default is unchecked
use_special = st.checkbox("Include special characters")  # Checkbox for special characters (!@#$%^&*), default is unchecked

# Button to generate password
if st.button("Generate Password"):  # When the user clicks this button, generate a password
    password = generate_password(length, use_digits, use_special)  # Call the function to generate the password
    st.write(f"Generated Password: `{password}`")  # Display the generated password in a code-style format
