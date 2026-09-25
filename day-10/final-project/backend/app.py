import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Simple API Simulation for Smart Hygiene Risk Prediction (Bonus Requirement)
def predict_hygiene_risk_api(cleanliness_score, odor_score, waste_level, complaints, footfall, hours_since_cleaning):
    # 1. Load data to train model on the fly for the API
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../ml/preprocessing/processed_data/cleaned_processed_facility.csv")
    
    if not os.path.exists(file_path):
        file_path = "ml/preprocessing/processed_data/cleaned_processed_facility.csv"
        
    df = pd.read_csv(file_path)
    
    X = df.drop(["facility_id", "inspection_date", "hygiene_risk"], axis=1, errors="ignore")
    y = df["hygiene_risk"]
    
    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    
    # 2. Create sample input dataframe matching training columns
    input_data = pd.DataFrame([{
        'location': 1,
        'facility_type': 2,
        'cleanliness_score': cleanliness_score,
        'odor_score': odor_score,
        'waste_level': waste_level,
        'water_availability': 1,
        'footfall': footfall,
        'complaints': complaints,
        'hours_since_cleaning': hours_since_cleaning
    }])
    
    # Ensure columns match training data order
    input_data = input_data[X.columns]
    
    # 3. Predict
    prediction = model.predict(input_data)[0]
    return prediction

if __name__ == "__main__":
    print("--- Smart Hygiene Risk Prediction API Simulation ---")
    # Test case: Low cleanliness, high odor, high complaints
    sample_risk = predict_hygiene_risk_api(
        cleanliness_score=3.5, 
        odor_score=8.5, 
        waste_level=85.0, 
        complaints=12, 
        footfall=500, 
        hours_since_cleaning=24.0
    )
    print(f"API Prediction Result for Test Facility -> Hygiene Risk: {sample_risk}")