import streamlit as st
import joblib
import pandas as pd

model = joblib.load("grey_market_model.pkl")

st.set_page_config(page_title="Grey Market Detector", layout="centered")

st.title("🕵️ Grey Market Product Detection")
st.write("Predict whether a product listing is Grey Market or Legitimate")

product_title = st.text_input("Product Title")
selling_price = st.number_input("Selling Price", min_value=0.0)
mrp = st.number_input("MRP", min_value=0.0)
discount_pct = st.number_input("Discount Percentage", min_value=0.0, max_value=100.0)
review_count = st.number_input("Review Count", min_value=0)

if st.button("Detect"):
    input_df = pd.DataFrame([{
        "Product_Title": product_title,
        "Selling_Price": selling_price,
        "MRP": mrp,
        "Discount_Pct": discount_pct,
        "Review_Count": review_count
    }])

    prob = model.predict_proba(input_df)[0][1]
    prediction = 1 if prob >= 0.75 else 0

    if prediction == 1:
        st.error(f"⚠️ Grey Market Detected (Confidence: {prob:.2f})")
    else:
        st.success(f"✅ Legit Product (Confidence: {1 - prob:.2f})")