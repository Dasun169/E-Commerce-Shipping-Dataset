import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("Shipment Delay Prediction")

# Inputs
block = st.selectbox("Warehouse Block", ['A', 'B', 'C', 'D', 'F'])
mode = st.selectbox("Mode of Shipment", ['Flight', 'Ship', 'Road'])
calls = st.slider("Customer Care Calls", 0, 10, 3)
rating = st.slider("Customer Rating", 1, 5, 3)
cost = st.number_input("Cost of Product ($)")
prior_purchases = st.slider("Prior Purchases", 0, 10, 2)
importance = st.selectbox("Product Importance", ['low', 'medium', 'high'])
gender = st.selectbox("Customer Gender", ['M', 'F'])
discount = st.slider("Discount Offered (%)", 0, 100, 10)
weight = st.number_input("Weight (grams)")

# Encode input
block_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
mode_map = {'Flight': 0, 'Road': 1, 'Ship': 2}
importance_map = {'high': 0, 'low': 1, 'medium': 2}
gender_map = {'M': 1, 'F': 0}

input_data = [[
    block_map[block],
    mode_map[mode],
    calls,
    rating,
    cost,
    prior_purchases,
    importance_map[importance],
    gender_map[gender],
    discount,
    weight
]]

if st.button("Predict"):
    result = model.predict(input_data)
    if result[0] == 1:
        st.error("⚠️ Product is likely to be **delayed**.")
    else:
        st.success("✅ Product is likely to be **on time**.")
