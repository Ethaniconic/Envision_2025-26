# 🕵️ Grey Market Detection Model

## Overview

This module contains machine learning models trained to detect counterfeit and grey market products from e-commerce platforms (specifically Snapdeal) using pricing patterns and product title analysis. The project includes model training, evaluation, and a web-based interactive Streamlit application for real-time predictions.

## 📁 Project Structure

```
Model/
├── 3-ML.ipynb                              # Jupyter notebook with model training
├── app.py                                  # Streamlit web application
├── Final-snapdeal-dataset.csv              # Training dataset
├── requirements.txt                        # Python dependencies
├── logistic_grey_market_model.pkl          # Trained Logistic Regression model (generated)
└── grey_market_xgboost_model.pkl           # Trained XGBoost model (generated)
```

## 🎯 Objective

Develop and deploy machine learning models to identify suspicious products that are likely to be:
- **Grey Market Products**: Legitimate products sold through unauthorized channels
- **Counterfeit Items**: Fake or unauthorized copies of products
- **Suspicious Listings**: Products with abnormal pricing patterns

## 📊 Dataset

**File**: `Final-snapdeal-dataset.csv`

### Features Used for Training:
| Feature | Type | Description |
|---------|------|-------------|
| `Product_Title` | Text | Product name/title (TF-IDF vectorized) |
| `Selling_Price` | Numeric | Current selling price on Snapdeal |
| `MRP` | Numeric | Maximum Retail Price |
| `Discount_Pct` | Numeric | Discount percentage |
| `Review_Count` | Numeric | Number of customer reviews |

### Target Variable:
- `Is_Grey_Market`: Binary label (0 = Legitimate, 1 = Grey Market)

## 🤖 Models Implemented

### 1. **Logistic Regression Model**
- **File**: `logistic_grey_market_model.pkl`
- **Algorithm**: Logistic Regression with balanced class weights
- **Key Parameters**:
  - Max iterations: 2000
  - Solver: liblinear
  - Class weight: balanced
  - Random state: 42

**Architecture**:
```
Text Features (TF-IDF) ─────┐
                             ├──> Logistic Regression Classifier
Numeric Features (Scaled) ──┘
```

**TF-IDF Configuration**:
- Max features: 4000
- N-gram range: (1, 2) (unigrams and bigrams)
- Min document frequency: 2
- Stop words: English

### 2. **XGBoost Classifier Model**
- **File**: `grey_market_xgboost_model.pkl`
- **Algorithm**: Gradient Boosting with XGBoost
- **Key Parameters**:
  - Estimators: 400
  - Max depth: 6
  - Learning rate: 0.05
  - Subsample: 0.8
  - Colsample bytree: 0.8
  - Scale pos weight: Auto-calculated (class imbalance correction)
  - Evaluation metric: Logloss
  - Random state: 42
  - Jobs: -1 (all cores)

**Architecture**:
```
Text Features (TF-IDF) ─────┐
                             ├──> Gradient Boosting
Numeric Features (Scaled) ──┘     (400 trees, depth=6)
```

## 📈 Model Training Pipeline

### Preprocessing Steps:
1. **Text Processing**:
   - TF-IDF vectorization of product titles
   - Bigram inclusion for context
   - Removal of English stop words
   - Maximum 4000 features

2. **Numeric Processing**:
   - StandardScaler normalization for:
     - Selling Price
     - MRP
     - Discount Percentage
     - Review Count

3. **Train-Test Split**:
   - Test size: 20%
   - Stratified split (maintains class distribution)
   - Random state: 42

### Training Process:
```python
Pipeline(
    steps=[
        ("preprocessor", ColumnTransformer),  # Text + Numeric features
        ("classifier", LogisticRegression/XGBClassifier)  # Model
    ]
)
```

## 📊 Model Evaluation Metrics

Both models are evaluated on:
- **Confusion Matrix**: True/False positives and negatives
- **Classification Report**: Precision, Recall, F1-Score per class
- **ROC-AUC Score**: Area Under the Receiver Operating Characteristic Curve
- **Visualizations**: Heatmaps of confusion matrices

## 🌐 Streamlit Web Application

### Features

**File**: `app.py`

A user-friendly web interface for real-time product classification.

#### **UI Components**:

1. **Sidebar Settings**:
   - Model Selection: Choose between Logistic Regression or XGBoost
   - Detection Threshold: Adjustable probability threshold (0.3 - 0.9)

2. **Input Section** (Two columns):
   - **Product Information**:
     - Product Title (text area)
     - Review Count (number input)
   - **Pricing Details**:
     - Selling Price
     - MRP (Maximum Retail Price)
     - Discount % (slider)

3. **Analysis Output**:
   - Prediction result (Grey Market / Legitimate)
   - Confidence score (0-100%)
   - Progress bar visualization
   - Model used indicator

#### **Key Features**:
- ✅ Input validation
- ✅ Error handling with user-friendly messages
- ✅ Real-time predictions
- ✅ Model caching for performance
- ✅ Threshold customization
- ✅ Interpretation guide

#### **Running the Application**:
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 🚀 Setup & Installation

### Prerequisites:
- Python 3.7 or higher
- pip package manager

### Installation Steps:

1. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

2. **Additional Packages** (if needed):
```bash
pip install xgboost
```

3. **Training Models** (Optional):
   - Run the Jupyter notebook `3-ML.ipynb` to retrain models
   - Models will be saved as `.pkl` files

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | Latest | Web application framework |
| scikit-learn | Latest | ML algorithms & preprocessing |
| pandas | Latest | Data manipulation & analysis |
| joblib | Latest | Model serialization/deserialization |
| numpy | Latest | Numerical computing |
| xgboost | Latest | Gradient boosting classifier |
| matplotlib | Latest | Visualization (in notebook) |
| seaborn | Latest | Statistical visualization (in notebook) |

## 📝 Usage Guide

### **For Training New Models**:

1. Open `3-ML.ipynb` in Jupyter Notebook
2. Ensure `Final-snapdeal-dataset.csv` is in the same directory
3. Run all cells sequentially
4. Two model files will be generated:
   - `logistic_grey_market_model.pkl`
   - `grey_market_xgboost_model.pkl`

### **For Making Predictions via Web App**:

1. Ensure trained model files are present
2. Run: `streamlit run app.py`
3. Enter product details in the web interface
4. Adjust threshold if needed
5. Click "Analyze Product" to get prediction

### **For Programmatic Usage**:

```python
import joblib
import pandas as pd

# Load model
model = joblib.load("grey_market_xgboost_model.pkl")

# Prepare input
input_data = pd.DataFrame([{
    "Product_Title": "Apple iPhone 15",
    "Selling_Price": 50000,
    "MRP": 79900,
    "Discount_Pct": 37,
    "Review_Count": 245
}])

# Make prediction
probability = model.predict_proba(input_data)[0][1]
prediction = model.predict(input_data)[0]

print(f"Grey Market Probability: {probability:.2%}")
print(f"Prediction: {'Grey Market' if prediction == 1 else 'Legitimate'}")
```

## 🎯 Model Comparison

### **Logistic Regression**
- ✅ Interpretable results
- ✅ Faster training & inference
- ✅ Lower memory footprint
- ❌ May underfit complex patterns

### **XGBoost**
- ✅ Better accuracy typically
- ✅ Captures non-linear patterns
- ✅ Handles feature interactions
- ❌ Slower inference
- ❌ Requires more computational resources

## 📊 Decision Threshold

The detection threshold determines the probability cutoff for classification:
- **Lower threshold** (0.3-0.5): More sensitive, catches more grey market products but more false positives
- **Higher threshold** (0.7-0.9): More conservative, fewer false positives but may miss some grey market items
- **Recommended**: 0.75 for balanced performance

## ⚠️ Limitations & Considerations

1. **Data Dependency**: Model performance depends on dataset quality and representativeness
2. **Class Imbalance**: Dataset may have imbalanced classes (handled via `scale_pos_weight`)
3. **Feature Limitations**: Relies only on title, pricing, and review count
4. **Domain Specificity**: Trained on Snapdeal data; may need retraining for other platforms
5. **Text Features**: Sensitive to product title variations and typos

## 🔧 Troubleshooting

### **Model File Not Found Error**:
- Ensure trained models are in the same directory as `app.py`
- Run the notebook to generate model files: `3-ML.ipynb`

### **Streamlit Application Won't Start**:
```bash
# Clear Streamlit cache
streamlit cache clear

# Run again
streamlit run app.py
```

### **Prediction Errors**:
- Verify all required features are provided
- Check that numeric values are valid (non-negative)
- Product title should not be empty

## 📈 Future Improvements

- [ ] Add ensemble model (voting classifier)
- [ ] Include additional features (seller rating, product category)
- [ ] Implement model monitoring and retraining pipeline
- [ ] Add confidence intervals to predictions
- [ ] Support for multiple e-commerce platforms
- [ ] Real-time API endpoint with FastAPI/Flask
- [ ] Model explainability (SHAP values)
- [ ] A/B testing framework for threshold optimization

## 📞 Support & Documentation

For questions or issues:
1. Check the Jupyter notebook for detailed model development
2. Review input validation in `app.py`
3. Examine confusion matrices and classification reports in notebook outputs

## 📄 License

This project is part of the Envision initiative for product authenticity detection.

---

**Last Updated**: December 2025  
**Model Version**: 1.0  
**Status**: Production Ready
