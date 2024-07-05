import streamlit as st
import requests 
st.title("Currency Converter")

# Input field for the amount
amount = st.number_input("Enter the amount to convert", value=1.0)

# Dropdown for selecting the source currency
source_currency = st.selectbox("Select source currency", ["USD", "EUR", "GBP", "INR"])

# Dropdown for selecting the target currency
target_currency = st.selectbox("Select target currency", ["USD", "EUR", "GBP", "INR"])

# Button to perform the conversion
if st.button("Convert"):
    # Perform the currency conversion (you can use a real-time exchange rate API)
    # For this example, let's assume a simple conversion rate
    conversion_rate = {
        "USD": {"USD": 1.0, "EUR": 0.85, "GBP": 0.74, "INR": 83.51},
        "EUR": {"USD": 1.18, "EUR": 1.0, "GBP": 0.87, "INR": 90.38},
        "GBP": {"USD": 1.35, "EUR": 1.16, "GBP": 1.0, "INR": 106.67},
        "INR": {"USD": 0.012, "EUR": 0.012, "GBP": 0.009, "INR": 1.0}
    }

    converted_amount = amount * conversion_rate[source_currency][target_currency]

    st.write(f"{amount} {source_currency} is equal to {converted_amount} {target_currency}")
