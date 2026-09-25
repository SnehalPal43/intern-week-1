import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def generate_predictions():
    # 1. Load the preprocessed dataset
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../preprocessing/processed_data/cleaned_processed_facility.csv")
    
    if not os.path.exists(file_path):
        file_path = "ml/preprocessing/processed_data/cleaned_processed_facility.csv"
        
    df = pd.read_csv(file_path)
    print("--- Loaded Preprocessed Data for Predictions ---")
    
    # 2. Prepare features and target
    X = df.drop(["facility_id", "inspection_date", "hygiene_risk"], axis=1, errors="ignore")
    y = df["hygiene_risk"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Predict on the entire dataset 
    predictions = model.predict(X)
    
    # 5. Create results dataframe
    results_df = df[["facility_id"]].copy()
    results_df["actual_hygiene_risk"] = y
    results_df["predicted_hygiene_risk"] = predictions
    
    # 6. Save to predictions folder
    os.makedirs(current_dir, exist_ok=True)
    pred_file_path = os.path.join(current_dir, "facility_predictions.csv")
    results_df.to_csv(pred_file_path, index=False)
    
    print("\nPredictions generated successfully!")
    print(f"Predictions file saved to: {pred_file_path}")
    print(results_df.head(10))

if __name__ == "__main__":
    generate_predictions()