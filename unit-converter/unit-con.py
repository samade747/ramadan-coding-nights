import streamlit as st


def convert_unit(value, unit_from, unit_to):


    conversions = {
        "meters_kiliometers" : 0.001, # 1 meter = 0.001 kilometer
        "kilometers_meters" : 1, # 1 kilometer = 1000 meter
        "grams_kilograms" : 0.001, # 1 gram = 0.001 kilogram
        "kilograms_grams" : 1000, # 1 kilogram = 1000 gram

    }

    key = f"{unit_from}_{unit_to}" # Generate a unqiue key  based on the input and output unit

    if key in conversions:
        conversions = conversions[key]
        result = value * conversions
    else:
        result = "Not Supported"

st.title("Unit Converter by samad")

value = st.number_input("Enter the value to convert", min_value=1.0, step=1.0)

unit_from = st.selectbox(" convert from", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox(" convert to", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")



