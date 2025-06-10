import streamlit as st
import joblib
import numpy as np

# Load the scaler and model
scaler = joblib.load('Scaler.pkl')
model = joblib.load('usa_real_estate.pkl')

st.title('House Price Predictor USA')
st.divider()

bed = st.number_input("Enter the number of bedrooms", value=2, step=1)
bath = st.number_input("Enter the number of bathrooms", value=1, step=1)
size = st.number_input("Enter the size", value=1000, step=50)

X = [bed, bath, size]

st.divider()

predictbutton = st.button("Predict!")
st.divider()

if predictbutton:
    st.balloons()
    X1 = np.array(X).reshape(1, -1)  # Ensure correct shape for scaler
    X_scaled = scaler.transform(X1)
    prediction = model.predict(X_scaled)[0]  # Get the first prediction
    
    # Convert to float and format
    prediction_float = float(prediction)
    st.write(f"The predicted price is **${prediction_float:,.2f}**")  # Format as currency
else:
    st.write("Please click the 'Predict!' button")