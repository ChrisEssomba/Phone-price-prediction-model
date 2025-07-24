# 📱 Predicting Used Mobile Phone Prices with XGBoost

## 🚀 Project Value Proposition

In the growing second-hand mobile phone market, determining a **fair and accurate price** can be challenging. This project aims to solve that problem by using **machine learning (XGBoost)** to estimate the price of a used phone based on its **technical specifications**. The trained model is integrated into a **Flask web application**, allowing users to get real-time price predictions with ease.

This project provides **practical value** for individuals looking to sell their phones, as well as for resellers seeking to price items competitively and confidently.

---

## 🎯 Project Objectives

- Train an XGBoost regression model to predict the resale price of used smartphones based on key features.
- Build a user-friendly **web app using Flask** for live interaction with the model.
- Strengthen technical skills in **data preprocessing, model tuning, evaluation**, and **web deployment**.

---

## 🗂️ Project Structure

├── data/

│ └── dataset.csv # Raw dataset from Kaggle with phone specs and prices


├── models/

│ ├── model.pkl # Trained XGBoost model

│ ├── scaler.pkl # Feature scaler for numerical variables

│ └── label_encoder.pkl # Label encoder for categorical features


├── notebooks/

│ └── notebook.ipynb # Jupyter notebook for EDA, model training, and evaluation


├── app/

│ └── app.py # Flask web application for deployment



---

## 🛠️ Technologies Used

- **Python**
- **XGBoost** (for regression)
- **Pandas, Scikit-learn, Matplotlib, Seaborn** (data analysis & preprocessing)
- **Flask** (web app development)
- **Kaggle** (dataset source)

---

## 📈 Model & Analysis Summary

The notebook includes:

- 📊 **Exploratory Data Analysis (EDA)**: Understand feature distributions, correlations, and outliers.
- 🧹 **Preprocessing**: Encoding categorical variables, scaling numeric features.
- 🧠 **Model Training**: Fine-tuned XGBoost model with hyperparameter optimization (e.g., GridSearchCV).
- 📏 **Evaluation**: Model assessed using metrics like RMSE and R².
- 💾 **Model Serialization**: Export of trained model, scaler, and encoder for app use.

---

## 🌐 Web Application

The **Flask app** provides an intuitive UI for users to:

- Enter phone specifications (brand, RAM, storage, camera, battery, etc.)
- Receive an **instant price prediction**
- Access the model without technical knowledge

---

## 📦 Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/phone-price-predictor.git
cd phone-price-predictor
```
Create a virtual environment and install dependencies:
```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  pip install -r requirements.txt
```

Run the Flask application:
```bash
cd app
python app.py
```
Visit http://localhost:5000 in your browser to try the app.

📚 Resources

    📊 Dataset: Used Mobile Phone Prices – Kaggle
  
    📘 XGBoost Documentation: https://xgboost.readthedocs.io/
  
    🌐 Flask Documentation: https://flask.palletsprojects.com/
