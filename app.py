import streamlit as st
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# App title
st.title("🏠 House Price Predictor (INR)")

# User input
sqft = st.number_input("Enter the living area (in sqft):", min_value=100)

# Prediction
if sqft:
    predicted_price = model.predict([[sqft]])[0]
    st.success(f"Estimated House Price: ₹{predicted_price:,.2f}")
