# Data Analysis 
import pandas as pd
import numpy as np

def analyze_facility_data(file_path):
    # Load the cleaned dataset
    df = pd.read_csv(file_path)
    
    print("--- KEY STATISTICAL SUMMARY ---")
    print(f"Average Cleanliness Score: {df['cleanliness_score'].mean():.2f}")
    print(f"Average Footfall: {df['footfall'].mean():.2f}")
    print(f"Total Complaints Registered: {df['complaints'].sum()}")
    
    print("\n--- LOCATION-WISE GROUPING ---")
    location_group = df.groupby('location').agg({
        'cleanliness_score': 'mean',
        'footfall': 'sum',
        'complaints': 'sum'
    }).reset_index()
    print(location_group)
    
    print("\n--- USEFUL INSIGHTS ---")
    print("1. Downtown facilities maintain higher average cleanliness and footfall.")
    print("2. Suburb locations record higher complaints due to increased waste levels.")
    print("3. Facilities with reliable water availability show lower complaint counts.")

if __name__ == "__main__":
    # Path to the cleaned dataset from root directory
    file_name = r"C:\Users\ASUS\OneDrive\Desktop\intern-week-1\day-03\dataset\cleaned_facility_data.csv"
    analyze_facility_data(file_name)