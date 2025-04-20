import streamlit as st
import pandas as pd
import joblib


# print("✅ Model trained and saved as model.pkl")
joblib.dump(model, 'D:\\JUPYTER PROJECT\\house_price_app\\model.pkl')
model = joblib.load('model.pkl')

st.title("🏠 House Price Predictor")

sqft = st.number_input("Enter living area (sqft):", min_value=100)

if sqft:
    price = model.predict([[sqft]])[0]
    st.success(f"Predicted Price: ₹{price:,.2f}")
    st.success(f"Price per sqft: ₹{price_per_sqft:,.2f}")
print("model trained and saved as model.pkl")
