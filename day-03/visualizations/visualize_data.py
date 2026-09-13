# Visualization 
import pandas as pd
import matplotlib.pyplot as plt

def generate_visualizations(file_path):
    # Load cleaned dataset
    df = pd.read_csv(file_path)
    
    # Set up the plotting window layout
    plt.figure(figsize=(14, 12))
    
    # 1. Bar Chart 1: Average Cleanliness by Location
    plt.subplot(3, 2, 1)
    location_cleanliness = df.groupby('location')['cleanliness_score'].mean()
    location_cleanliness.plot(kind='bar', color='skyblue')
    plt.title('Average Cleanliness Score by Location')
    plt.ylabel('Score')
    
    # 2. Bar Chart 2: Total Complaints by Location
    plt.subplot(3, 2, 2)
    location_complaints = df.groupby('location')['complaints'].sum()
    location_complaints.plot(kind='bar', color='salmon')
    plt.title('Total Complaints by Location')
    plt.ylabel('Complaints')
    
    # 3. Histogram: Distribution of Cleanliness Scores
    plt.subplot(3, 2, 3)
    plt.hist(df['cleanliness_score'], bins=5, color='lightgreen', edgecolor='black')
    plt.title('Distribution of Cleanliness Scores')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    
    # 4. Scatter Plot: Footfall vs Complaints
    plt.subplot(3, 2, 4)
    plt.scatter(df['footfall'], df['complaints'], color='purple')
    plt.title('Footfall vs Complaints')
    plt.xlabel('Footfall')
    plt.ylabel('Complaints')
    
    # 5. Additional Visualization: Footfall Trend Across Inspection Dates
    plt.subplot(3, 2, 5)
    plt.plot(df['inspection_date'], df['footfall'], marker='o', color='orange')
    plt.title('Footfall Across Inspection Dates')
    plt.xlabel('Inspection Date')
    plt.ylabel('Footfall')
    plt.xticks(rotation=45)
   
    plt.tight_layout(pad=3.0)
    # Save the chart image
    plt.savefig('facility_analysis_plots.png', bbox_inches='tight')
    print("All charts successfully generated and saved as 'facility_analysis_plots.png'!")
    plt.show()

if __name__ == "__main__":
    file_name = r"C:\Users\ASUS\OneDrive\Desktop\intern-week-1\day-03\dataset\cleaned_facility_data.csv"
    generate_visualizations(file_name)