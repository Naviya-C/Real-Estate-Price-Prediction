# 🏡 Real Estate House Price Prediction using Linear Regression

A Machine Learning project that predicts **house prices** based on various property features using **Linear Regression**.  
This project includes complete data preprocessing, feature engineering, and model training steps.

---

## 📘 Project Overview

This project aims to **predict house prices** using **Linear Regression** after performing extensive **data preprocessing and cleaning**.  
The dataset contains property-related features such as area type, location, size, availability, and more.

---

## 🧩 Project Workflow

### 🧠 1. Understanding the Data
- Loaded the dataset and explored key attributes.
- Identified data types, value ranges, and distributions.

### 🧹 2. Data Preprocessing Steps

| Step | Description |
|------|--------------|
| **Handle Missing Values** | Dropped rows/columns with missing data to maintain dataset integrity. |
| **Handle Duplicates** | Removed duplicate records to avoid redundancy. |
| **Handle Incorrect Data** | Fixed or removed invalid entries (e.g., negative area or price). |
| **Handle Inconsistent Data** | Standardized inconsistent text (e.g., `2 BHK` vs `2BHK`). |
| **Handle Outliers** | Removed extreme price or size outliers that affected model accuracy. |
| **Handle Categorical Data** | Encoded non-numeric columns like location and area type. |
| **One-Hot Encoding** | Applied one-hot encoding for categorical features. |
| **Save Clean Data** | Exported final preprocessed data to a clean `.csv` file. |

---

## 🧮 3. Model Building

- **Model Used:** Linear Regression  
- **Library:** `scikit-learn`  
- **Training Split:** 80% training, 20% testing  
- **Evaluation Metrics:** R² Score, Mean Absolute Error (MAE), Mean Squared Error (MSE)

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
predictions = model.predict(X_test)
print("R2 Score:", r2_score(y_test, predictions))
