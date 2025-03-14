import streamlit as st

def main():
    # Page configuration
    st.set_page_config(page_title="Advanced Calculator", page_icon="\U0001F522", layout="centered")
    
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .main {background-color: #f5f5f5;}
        div.stButton > button {width: 100%; padding: 10px; font-size: 18px; border-radius: 10px;}
        div.stSelectbox > label {font-size: 18px; font-weight: bold;}
        div.stNumberInput > label {font-size: 16px;}
        .result-box {padding: 20px; border-radius: 10px; background-color: #4CAF50; color: white; font-size: 20px; text-align: center;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Title and description
    st.markdown("""<h1 style='text-align: center; color: #333;'>Advanced Calculator</h1>""", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Perform basic arithmetic operations with a modern UI.</p>", unsafe_allow_html=True)

    # Input section
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            num1 = st.number_input("Enter first number", value=0.0, step=0.1, key="num1")
        with col2:
            num2 = st.number_input("Enter second number", value=0.0, step=0.1, key="num2")
    
    # Operation selection
    operation = st.selectbox("Choose operation", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])
    
    # Calculate button
    if st.button("Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (×)":
                result = num1 * num2
                symbol = "×"
            else:  # Division
                if num2 == 0:
                    st.error("Error: Division by zero!")
                    return
                result = num1 / num2
                symbol = "÷"
            
            # Display result with enhanced UI
            st.markdown(f"""<div class='result-box'>{num1} {symbol} {num2} = <b>{result}</b></div>""", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Run the app
if __name__ == "__main__":
    main()