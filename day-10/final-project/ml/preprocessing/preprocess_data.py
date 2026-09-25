import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data():
  # 1. Locate the CSV dataset file dynamically
  current_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(
      current_dir, "../dataset/facility_hygiene_ml_dataset.csv"
  )

  if not os.path.exists(file_path):
    file_path = "ml/dataset/facility_hygiene_ml_dataset.csv"

  # Read the CSV file
  df = pd.read_csv(file_path)
  print("--- Original Data Shape ---")
  print(df.shape)

  # 2. Handle missing values by dropping rows with nulls in important columns
  df = df.dropna(subset=["cleanliness_score", "waste_level", "hygiene_risk"])

  # 3. Encode categorical text columns into numbers using LabelEncoder
  label_encoder_loc = LabelEncoder()
  df["location"] = label_encoder_loc.fit_transform(df["location"])

  label_encoder_type = LabelEncoder()
  df["facility_type"] = label_encoder_type.fit_transform(df["facility_type"])

  label_encoder_water = LabelEncoder()
  df["water_availability"] = label_encoder_water.fit_transform(
      df["water_availability"].astype(str)
  )

  # 4. Save the cleaned and processed data into the processed_data folder
  processed_dir = os.path.join(current_dir, "processed_data")
  os.makedirs(processed_dir, exist_ok=True)
  processed_file_path = os.path.join(
      processed_dir, "cleaned_processed_facility.csv"
  )
  df.to_csv(processed_file_path, index=False)

  print("\nData preprocessing completed successfully!")
  print(f"Processed file saved to: {processed_file_path}")
  print(df.head())


if __name__ == "__main__":
  preprocess_data()