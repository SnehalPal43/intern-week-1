# Day 4: Machine Learning Fundamentals & Practical Assessment

## Overview
This project builds and evaluates a binary classification machine learning model to predict **facility hygiene risk** based on operational metrics (cleanliness scores, waste levels, complaints, footfall, and cleaning history). 

The workflow strictly follows standard machine learning practices: Dataset preparation $\rightarrow$ Preprocessing $\rightarrow$ Train/Test Split $\rightarrow$ Model Training $\rightarrow$ Prediction $\rightarrow$ Evaluation.

---

## Project Deliverables & Structure
- `dataset/`: Contains the raw CSV dataset (`facility_ml_data.csv`).
- `preprocessing/`: Handles data cleaning and text-to-number encoding (`preprocess.py`).
- `models/`: Contains model training, comparison, and execution scripts (`train_models.py`).
- `evaluation/`: Stores performance metrics summary (`metrics.txt`).
- `predictions/`: Contains generated prediction outputs (`facility_predictions.csv`).

---

## Selected Model & Features
- **Selected Model:** Random Forest Classifier (achieved 100% accuracy on test split).
- **Target Label:** `hygiene_risk` (0 = Low Risk, 1 = High Risk).
- **Features Engineered & Utilized:** 
  - `location` (Categorical $\rightarrow$ Encoded)
  - `cleanliness_score` (Numerical)
  - `odor_score` (Numerical)
  - `waste_level` (Categorical $\rightarrow$ Encoded)
  - `complaints` (Numerical)
  - `footfall` (Numerical)
  - `hours_since_cleaning` (Numerical)

---

## Algorithm Performance Comparison
Two classification algorithms were trained and evaluated:

1. **Logistic Regression:**
   - **Accuracy:** 0.50
   - **Precision:** 1.00 | **Recall:** 0.50 | **F1 Score:** 0.67
   - *Observation:* Struggled with non-linear relationships in the multi-feature dataset.

2. **Random Forest Classifier (Selected):**
   - **Accuracy:** 1.00
   - **Precision:** 1.00 | **Recall:** 1.00 | **F1 Score:** 1.00
   - *Observation:* Handled complex decision boundaries effectively, resulting in optimal classification.

---

## Problems Encountered & Solutions
1. **Categorical Data Types:** 
   - *Problem:* Machine learning algorithms cannot ingest text features directly (`location`, `waste_level`).
   - *Solution:* Implemented Scikit-Learn's `LabelEncoder` within the preprocessing pipeline to safely convert text into numeric arrays.
2. **Path Resolution Errors:** 
   - *Problem:* Relative path mismatches threw `FileNotFoundError` when execution context shifted between directories.
   - *Solution:* Standardized paths relative to the project root directory.
3. **Variable Scope Restrictions:** 
   - *Problem:* A `NameError` occurred when attempting to write test evaluation metrics outside the local function scope.
   - *Solution:* Embedded data exporting logic directly inside the execution function where `y_test` and predictions were defined.

---

## Possible Improvements
- Scale the dataset to include hundreds of real-world rows for better model generalization.
- Implement hyperparameter tuning (e.g., `GridSearchCV`) to optimize tree depths and prevent potential overfitting.