import streamlit as st


st.title('Hello world samad streamlit app ' )

user_input = st.text_input("Enter text: ")

if st.button("show text"):
    st.write(f"You entered:, {user_input}")
    