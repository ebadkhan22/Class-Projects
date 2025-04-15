import streamlit as st
from pint import UnitRegistry
import google.generativeai as genai
import re


import streamlit as st





st.markdown(
    """
    <style>
    /* Apply checkered background to the whole page */
    .main {
        background: repeating-linear-gradient(
            45deg,
            #2c3e50 0px,
            #2c3e50 25px,
            #ecf0f1 25px,
            #ecf0f1 50px
        );
    }
    </style>
    """,
    unsafe_allow_html=True
)










# Initialize unit registry
ureg = UnitRegistry()

# Configure Google Gemini API key
genai.configure(api_key="your gemini key")

# Function to convert units
def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude, str(result.units)
    except Exception as e:
        return None, str(e)

# Function to call Gemini API with the correct model
def call_gemini_api(user_query):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Use latest available model
        response = model.generate_content(user_query)
        return response.text if response else None
    except Exception as e:
        print("API Error:", e)
        return None

# Function to extract numerical values and units from AI response
import re

import re

def extract_units(response):
    """
    Extracts numerical value, from-unit, and to-unit from an AI response.
    Example input: "4 kg is equal to approximately 8.82 pounds."
    Expected output: (4, "kg", "pounds")
    """

    # Use regex to find numbers and words (units)
    match = re.search(r"(\d+(\.\d+)?)\s*([a-zA-Z]+).*?(\d+(\.\d+)?)\s*([a-zA-Z]+)", response)

    if match:
        value = float(match.group(1))  # First number (4)
        from_unit = match.group(3)  # First unit (kg)
        to_unit = match.group(6)  # Second unit (pounds)
        return value, from_unit, to_unit
    else:
        return None  # If extraction fails




# Function to process LLM input
def process_llm_input(user_query):
    response = call_gemini_api(user_query)
    print("API Response:", response)  # Debugging print
    if response is None:
        return None, None, None
    return extract_units(response)

# Streamlit UI
st.title("📏 AI-Powered Unit Converter")

# User input method
input_method = st.radio("Choose input method:", ["Manual", "AI-powered (Natural Language)"])

# List of common units
units = [
    "meter", "centimeter", "millimeter", "kilometer",
    "gram", "kilogram", "milligram",
    "second", "minute", "hour",
    "liter", "milliliter",
    "inch", "foot", "yard", "mile",
    "pound", "ounce"
]

if input_method == "Manual":
    value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

    # Dropdown for unit selection
    from_unit = st.selectbox("Convert from:", units)
    to_unit = st.selectbox("Convert to:", units)

    if st.button("Convert"):
        if from_unit and to_unit:
            result, unit = convert_units(value, from_unit, to_unit)
            if result is not None:
                st.success(f"{value} {from_unit} = {result:.4f} {unit}")
            else:
                st.error("Invalid conversion units!")
        else:
            st.error("Please select both units!")

else:
    user_query = st.text_input("Enter conversion request (e.g., Convert 5 kg to pounds)")

    if st.button("Ask AI"):
        value, from_unit, to_unit = process_llm_input(user_query)
        if value is not None and from_unit and to_unit:
            result, unit = convert_units(value, from_unit, to_unit)
            if result is not None:
                st.success(f"{value} {from_unit} = {result:.4f} {unit}")
            else:
                st.error("Invalid conversion units!")
        else:
            st.error("Could not understand your request. Try again!")
