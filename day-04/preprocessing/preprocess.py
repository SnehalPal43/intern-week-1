# Preprocessing 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Drop missing values if any
    df = df.dropna()
    
    # Encode categorical text columns into numbers
    label_encoder = LabelEncoder()
    df['location'] = label_encoder.fit_transform(df['location'])
    df['waste_level'] = label_encoder.fit_transform(df['waste_level'])
    
    # Define features (X) and target label (y)
    X = df[['location', 'cleanliness_score', 'odor_score', 'waste_level', 'complaints', 'footfall', 'hours_since_cleaning']]
    y = df['hygiene_risk']
    
    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Preprocessing completed successfully!")
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    preprocess_data("dataset/facility_ml_data.csv")