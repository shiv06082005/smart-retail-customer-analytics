import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="Smart Retail Analytics", page_icon="📊")

st.title("📊 Smart Retail Customer Analytics Dashboard")

st.write("Predict whether a product belongs to High Value category.")

quantity = st.number_input("Quantity", value=1)

unit_price = st.number_input(
    "Unit Price",
    min_value=0.0,
    value=10.0
)

country = st.number_input(
    "Country Encoded Value",
    min_value=0,
    value=0
)

if st.button("Predict"):

    data = pd.DataFrame({
        "Quantity": [quantity],
        "UnitPrice": [unit_price],
        "Country": [country]
    })

    prediction = model.predict(data)[0]

    if prediction == 1:
        st.success("✅ High Value Product")
    else:
        st.error("❌ Low Value Product")