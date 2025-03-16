import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n  \n\n {joke_data['punchline']}"
        else:
            return "⚠️ Failed to fetch a joke. Please try again later."
    except:
        return "😂 Why did the programmer quit his job? \n Because he didn't get array!"

def main():
    """Main function to run the Streamlit app"""
    st.set_page_config(page_title="😂 Joke Generator", page_icon="🎭", layout="centered")
    
    # Custom Styling
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(to right, #434343, #000000);
        }
        .stApp {
            background-color: #1E1E1E;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 0px 15px rgba(255,255,255,0.1);
        }
        .joke-box {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            color: #FFF;
            background: #FF0000;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 5px 15px rgba(255, 255, 255, 0.2);
        }
        .generate-btn {
            background-color: #FF5733 !important;
            color: white !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border-radius: 25px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.image("https://cdn-icons-png.flaticon.com/512/866/866764.png", width=100)
    st.title("😂 Random Joke Generator")
    st.write("Click the button below to generate a random joke!")
    
    if st.button("🎭 Generate Joke", key="joke_button", help="Click to generate a joke"):
        joke = get_random_joke()
        st.markdown(f'<div class="joke-box">{joke}</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Footer
    st.markdown(
        """
        <div style='text-align:center; font-size:14px; color:white;'>
            <p>🔗 Joke from <a href='https://github.com/samade747/' target='_blank' style='color:#FF5733;'>Official Joke API</a></p>
            <p>💻 Built with ❤️ by <a href='https://github.com/samade747/' target='_blank' style='color:#FF5733;'>samad</a> using Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
