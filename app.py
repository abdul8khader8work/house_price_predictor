# Step 1: Import libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 2: Load your dataset (already in INR)
data = pd.read_csv("D:\\JUPYTER PROJECT\\House Price India.csv")  # Replace with your file path
print("First 5 rows:\n", data.head(14000))  # Verify columns

# Step 3: Prepare features (X) and target (y)
X = data[["living area"]]  # House size in sqft
y = data["Price"]   # Price in INR (already converted)

# Step 4: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Predict for 1200 sqft
sqft_to_predict = 1200
predicted_price = model.predict([[sqft_to_predict]])[0]
print(f"\nPredicted price for {sqft_to_predict} sqft: ₹{predicted_price:,.2f}")

# Step 6: Check accuracy
accuracy = model.score(X, y)
print(f"Model accuracy (R-squared): {accuracy:.2f}")

# Bonus: Show price per sqft trend
price_per_sqft = model.coef_[0]
print(f"Price per sqft: ₹{price_per_sqft:,.2f}")
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
