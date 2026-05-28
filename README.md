# Smart ML Decision Support System

## Project Overview

An end-to-end machine learning project to predict customer churn
and support business decision-making using customer behavior data.

---

## Problem Statement

Predict whether a customer is likely to churn based on historical customer data and identify patterns affecting customer retention.

---

## Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Git & GitHub

---

## Project Structure

```bash
smart-ml-decision-support-system/
│
├── data/
│   ├── customer_churn.csv
│   └── customer_churn_cleaned.csv
│
├── src/
│   ├── data_understanding.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── test_libs.py
│   └── test_setup.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Week-wise Progress

## Week 1 — Environment Setup & Repository Initialization

### Completed Tasks

* Created project structure
* Initialized Git repository
* Connected local project to GitHub
* Created virtual environment (`venv`)
* Installed required ML libraries
* Configured `.gitignore`
* Added dependency management using `requirements.txt`

### Key Learning

* Python virtual environments
* Git & GitHub workflow
* Dependency management

---

## Week 2 — Data Understanding & Exploratory Data Analysis (EDA)

### Completed Tasks

* Loaded customer churn dataset using Pandas
* Explored dataset structure and feature types
* Checked missing values and duplicates
* Performed statistical summary analysis
* Visualized:

  * Churn distribution
  * Monthly charges distribution
  * Contract type vs churn
  * Internet service vs churn
  * Monthly charges vs churn

### Libraries Used

* Pandas
* Seaborn
* Matplotlib

### Key Learning

* Exploratory Data Analysis (EDA)
* Data visualization
* Identifying business patterns from data

---

## Week 3 — Data Preprocessing & Feature Engineering

### Completed Tasks

* Handled missing values
* Converted `TotalCharges` to numeric datatype
* Removed duplicate rows
* Performed feature-target split
* Applied one-hot encoding using `pd.get_dummies()`
* Performed 80-20 train-test split

### Key Learning

* Data cleaning
* Feature engineering
* Preparing datasets for machine learning models

---

## Week 4 — Machine Learning Model Training & Evaluation

### Completed Tasks

* Implemented Logistic Regression model
* Trained model using Scikit-learn
* Performed prediction on unseen test data
* Evaluated model using:

  * Accuracy Score
  * Classification Report
  * Confusion Matrix

### Final Result

* Model Accuracy: **~82%**

### Key Learning

* Supervised machine learning
* Binary classification
* Model evaluation techniques

---

# Machine Learning Workflow

1. Data Collection
2. Data Understanding
3. Exploratory Data Analysis
4. Data Cleaning & Preprocessing
5. Feature Engineering
6. Train-Test Split
7. Model Training
8. Prediction & Evaluation

---

# Key Features

* Customer churn prediction
* Automated preprocessing pipeline
* Binary classification using Logistic Regression
* Data visualization and EDA
* Feature encoding and train-test split
* Model evaluation using Scikit-learn metrics

---

# Evaluation Metrics

* Accuracy Score
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

# Final Model Results

| Metric         | Value                 |
| -------------- | --------------------- |
| Accuracy       | ~82%                  |
| Problem Type   | Binary Classification |
| Algorithm Used | Logistic Regression   |

---

# Future Improvements

* Hyperparameter tuning
* Model comparison with Random Forest/XGBoost
* Deployment using Flask or Streamlit
* Real-time prediction dashboard
* Explainable AI integration (SHAP/LIME)

---

# Learning Outcomes

Through this project, I learned:

* Data preprocessing techniques
* Exploratory Data Analysis (EDA)
* Feature engineering
* Binary classification
* Logistic Regression implementation
* Model evaluation techniques
* GitHub project management
* Dependency and environment management
