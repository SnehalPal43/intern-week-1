# Import libraries
import pandas as pd
import numpy as np

def clean_facility_data(file_path):
    # Load the raw dataset from the CSV file
    df = pd.read_csv(file_path)
    print(f"Original dataset shape: {df.shape}")
    
    # Remove duplicate rows from the dataset
    df = df.drop_duplicates()
    print(f"Shape after removing duplicates: {df.shape}")
    
    # Fill missing values in cleanliness score using the median
    df['cleanliness_score'] = df['cleanliness_score'].fillna(df['cleanliness_score'].median())
    
    # Fill missing complaint values with 0 assuming no complaints were logged
    df['complaints'] = df['complaints'].fillna(0)
    
    # Fill missing water availability with 'Unknown'
    df['water_availability'] = df['water_availability'].fillna('Unknown')
    
    # Save the cleaned dataset back into the dataset folder
    cleaned_path = r"C:\Users\ASUS\OneDrive\Desktop\intern-week-1\day-03\dataset\cleaned_facility_data.csv"
    df.to_csv(cleaned_path, index=False)
    print(f"Cleaned dataset successfully saved to: {cleaned_path}")
    return df

if __name__ == "__main__":
    # Path to the raw dataset file from the main day-03 directory
    file_name = r"C:\Users\ASUS\OneDrive\Desktop\intern-week-1\day-03\dataset\facility_data.csv"
    clean_facility_data(file_name)