# 🚚 Shipment Delay Prediction

This project uses a machine learning model to predict whether a shipment will be delivered on time or delayed, based on various customer and product-related features. The project includes data preprocessing, model training (Random Forest), performance evaluation, and a Streamlit web interface for prediction.

---

## 📦 Dataset Overview

**Source**: Provided as part of a customer analytics dataset.

**Total Records**: 10,999 rows  
**Features**: 11 input features + 1 target variable  
**Target Variable**: `Reached.on.Time_Y.N`  
- `0` = Delivered on time  
- `1` = Not delivered on time (Delayed)

### 📊 Dataset Columns:

| Column Name              | Description |
|--------------------------|-------------|
| `ID`                     | Unique identifier for each customer/order |
| `Warehouse_block`        | Warehouse section where the product is stored (A–F) |
| `Mode_of_Shipment`       | Shipment method: Flight, Ship, or Road |
| `Customer_care_calls`    | Number of customer service calls made |
| `Customer_rating`        | Customer satisfaction rating (1 = Worst, 5 = Best) |
| `Cost_of_the_Product`    | Price of the product in USD |
| `Prior_purchases`        | Number of previous purchases by the customer |
| `Product_importance`     | Importance level of the product: Low, Medium, High |
| `Gender`                 | Gender of the customer (M or F) |
| `Discount_offered`       | Discount applied on the product (%) |
| `Weight_in_gms`          | Product weight in grams |
| `Reached.on.Time_Y.N`    | **Target**: 1 = Delayed, 0 = On time |

---

## ⚙️ Project Workflow

1. **Data Preprocessing**
   - Handling categorical features using Label Encoding
   - Dropping unnecessary columns like `ID`
   - Splitting the data into training and test sets

2. **Model Training**
   - RandomForestClassifier used for training
   - Model saved as `model.pkl` using `pickle`

3. **Performance Evaluation**
   - Confusion Matrix
   - Classification Report
   - Accuracy, Precision, Recall, F1-Score
   - Feature Importance

4. **Visualization**
   - Scatter plots: e.g., `Customer_care_calls` vs `Reached.on.Time_Y.N`
   - Feature importance bar chart
   - Prediction vs Actual scatter plot
   - ROC and Precision-Recall curves

5. **Web Interface**
   - Built using **Streamlit**
   - User inputs shipment details and gets prediction instantly
   - Run using:  
     ```
     streamlit run app.py
     ```

---

## 📈 Example Visualizations

- ✅ **Scatter Plot**: Customer Care Calls vs Delivery Delay  
- ✅ **Strip Plot**: Actual vs Predicted Delivery Status  
- ✅ **Feature Importance**: Top factors affecting delivery outcome  
- ✅ **Confusion Matrix**: Overall model accuracy  
- ✅ **ROC & PR Curves**: Model performance evaluation

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/shipment-delay-prediction.git
   cd shipment-delay-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:
   Open Shipment_Model_Training.ipynb to explore the data and train the model.
4. Launch the web app:
   ```bash
   streamlit run app.py
   ```

---

## 📁 Folder Structure
```bash
├── dataset/
│   ├── shipment_data.csv
│   ├── model.pkl
│   ├── app.py
│   └── visuals/
├── Shipment_Model_Training.ipynb
├── requirements.txt
└── README.md
```
