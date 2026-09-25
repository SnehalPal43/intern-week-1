import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_and_evaluate_models():
    # 1. Load the preprocessed dataset
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../preprocessing/processed_data/cleaned_processed_facility.csv")
    
    if not os.path.exists(file_path):
        file_path = "ml/preprocessing/processed_data/cleaned_processed_facility.csv"
        
    df = pd.read_csv(file_path)
    print("--- Preprocessed Data Loaded Successfully ---")
    
    # 2. Define features (X) and target label (y)
    # Dropping non-numeric or ID columns like facility_id, inspection_date and target column
    X = df.drop(["facility_id", "inspection_date", "hygiene_risk"], axis=1, errors="ignore")
    y = df["hygiene_risk"]
    
    # 3. Split dataset into training set (80%) and testing set (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Train Model 1: Logistic Regression
    print("\n--- Training Logistic Regression ---")
    log_reg = LogisticRegression(max_iter=1000, random_state=42)
    log_reg.fit(X_train, y_train)
    y_pred_lr = log_reg.predict(X_test)
    lr_accuracy = accuracy_score(y_test, y_pred_lr)
    print("Logistic Regression Accuracy:", lr_accuracy)
    
    # 5. Train Model 2: Random Forest Classifier
    print("\n--- Training Random Forest Classifier ---")
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, y_pred_rf)
    print("Random Forest Accuracy:", rf_accuracy)
    
    rf_report = classification_report(y_test, y_pred_rf)
    print("\nRandom Forest Classification Report:")
    print(rf_report)
    
    # 6. Save performance evaluation report to the evaluation folder
    eval_dir = os.path.join(current_dir, "../evaluation")
    os.makedirs(eval_dir, exist_ok=True)
    report_path = os.path.join(eval_dir, "model_performance_report.txt")
    
    with open(report_path, "w") as f:
        f.write("=== SMART HYGIENE RISK MODEL PERFORMANCE REPORT ===\n\n")
        f.write(f"1. Logistic Regression Accuracy: {lr_accuracy}\n\n")
        f.write(f"2. Random Forest Accuracy: {rf_accuracy}\n\n")
        f.write("=== RANDOM FOREST CLASSIFICATION REPORT ===\n")
        f.write(rf_report)
        
    print(f"\nModel performance report saved successfully to: {report_path}")

if __name__ == "__main__":
    train_and_evaluate_models()