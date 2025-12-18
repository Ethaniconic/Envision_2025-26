import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Grey Market Detector",
    layout="wide",
    page_icon="🕵️"
)

@st.cache_resource
def load_models():
    try:
        # Use correct model file names from your ML notebook
        rf = joblib.load("logistic_grey_market_model.pkl")
        xgb = joblib.load("grey_market_xgboost_model.pkl")
        return rf, xgb
    except FileNotFoundError as e:
        st.error(f"❌ Model file not found: {e}")
        st.stop()

rf_model, xgb_model = load_models()

st.sidebar.title("⚙️ Settings")
model_choice = st.sidebar.selectbox(
    "Select Model",
    ["Random Forest", "XGBoost"]
)

threshold = st.sidebar.slider(
    "Detection Threshold",
    min_value=0.3,
    max_value=0.9,
    value=0.75,
    step=0.05
)

model = rf_model if model_choice == "Random Forest" else xgb_model

st.title("🕵️ Grey Market Product Detection")
st.caption("ML-based detection using pricing patterns and product title analysis")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Product Information")
    product_title = st.text_area("Product Title", height=100)
    review_count = st.number_input("Review Count", min_value=0, value=0)

with col2:
    st.subheader("💰 Pricing Details")
    selling_price = st.number_input("Selling Price", min_value=0.0, value=0.0)
    mrp = st.number_input("MRP", min_value=0.0, value=0.0)
    discount_pct = st.slider("Discount %", 0, 100, 0)

st.markdown("---")

if st.button("🔍 Analyze Product", use_container_width=True):
    # Validate input
    if not product_title.strip():
        st.warning("⚠️ Please enter a product title")
    elif mrp <= 0:
        st.warning("⚠️ MRP must be greater than 0")
    elif selling_price < 0:
        st.warning("⚠️ Selling price cannot be negative")
    else:
        try:
            input_df = pd.DataFrame([{
                "Product_Title": product_title,
                "Selling_Price": selling_price,
                "MRP": mrp,
                "Discount_Pct": discount_pct,
                "Review_Count": review_count
            }])

            prob = model.predict_proba(input_df)[0][1]
            prediction = prob >= threshold

            st.subheader("📊 Result")
            st.progress(min(int(prob * 100), 100))

            if prediction:
                st.error(f"⚠️ Grey Market Detected\n\nConfidence Score: {prob:.2f}")
            else:
                st.success(f"✅ Legitimate Product\n\nConfidence Score: {(1 - prob):.2f}")

            st.caption(f"Model used: {model_choice}")
        except Exception as e:
            st.error(f"❌ Error during prediction: {str(e)}")

st.markdown("---")

st.subheader("ℹ️ Model Interpretation Guide")

st.markdown(f"""
**Detection Threshold:**  
The minimum probability required to classify a product as *Grey Market*.  
Current value: **{threshold}**

- Higher threshold → Fewer false positives, more conservative detection  
- Lower threshold → Higher recall, more aggressive detection  

**Confidence Score:**  
Represents how strongly the model believes in its prediction.

**Model Behavior:**  
- **Random Forest:** More conservative, higher precision  
- **XGBoost:** More sensitive, higher recall  

**Disclaimer:**  
This system is intended as a *decision-support tool* and should be used alongside manual review.
""")