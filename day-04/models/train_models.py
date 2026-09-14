# Model Training and Evaluation 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_and_evaluate():
    # 1. Load dataset
    df = pd.read_csv("dataset/facility_ml_data.csv")
    df = df.dropna()
    
    # 2. Preprocessing
    label_encoder = LabelEncoder()
    df['location'] = label_encoder.fit_transform(df['location'])
    df['waste_level'] = label_encoder.fit_transform(df['waste_level'])
    
    # Features and Target
    X = df[['location', 'cleanliness_score', 'odor_score', 'waste_level', 'complaints', 'footfall', 'hours_since_cleaning']]
    y = df['hygiene_risk']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Model 1: Logistic Regression
    lr_model = LogisticRegression(random_state=42)
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)
    
    print("--- Logistic Regression Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_test, lr_pred):.2f}")
    print(f"Precision: {precision_score(y_test, lr_pred, zero_division=0):.2f}")
    print(f"Recall: {recall_score(y_test, lr_pred, zero_division=0):.2f}")
    print(f"F1 Score: {f1_score(y_test, lr_pred, zero_division=0):.2f}")
    
    # 4. Model 2: Random Forest Classifier
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    
    print("\n--- Random Forest Classifier Evaluation ---")
    print(f"Accuracy: {accuracy_score(y_test, rf_pred):.2f}")
    print(f"Precision: {precision_score(y_test, rf_pred, zero_division=0):.2f}")
    print(f"Recall: {recall_score(y_test, rf_pred, zero_division=0):.2f}")
    print(f"F1 Score: {f1_score(y_test, rf_pred, zero_division=0):.2f}")
    
    # Save Random Forest predictions inside the predictions folder
    pred_df = pd.DataFrame({'Actual': y_test, 'Predicted': rf_pred})
    pred_df.to_csv("predictions/facility_predictions.csv", index=False)
    print("\nPredictions saved successfully to predictions/facility_predictions.csv")
    
    print("\nTraining and evaluation completed for both models successfully!")

if __name__ == "__main__":
    train_and_evaluate()