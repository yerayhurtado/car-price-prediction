import os
import pandas as pd
import streamlit as st

# --- Load dataset ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "car_prediction_data.csv")

df = pd.read_csv(DATA_PATH)

st.title("🚗 Car Price Prediction")

with st.form("prediction_form"):
    year = st.number_input("Year", min_value=1970,max_value=2025,value=2015)
    present_price = st.number_input("Present Price (€)",min_value=0.0,max_value=100000.0,step=500.0)
    kms_driven = st.number_input("Kms Driven", min_value=0, value=10000)
    owner = st.number_input("Owners", min_value=0)
    fuel_type = st.selectbox("Fuel Type",["Petrol","Diesel","CNG"])
    seller_type = st.selectbox("Seller Type",["Dealer","Individual"])
    transmission = st.selectbox("Transmission",["Manual","Automatic"])
    submitted = st.form_submit_button("Predict Price")

if submitted:
    st.write(f"✅ Input received: {year}, {present_price}€, {kms_driven} km, {owner} owners, {fuel_type}, {seller_type}, {transmission}.")


