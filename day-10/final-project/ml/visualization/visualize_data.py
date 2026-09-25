import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_visualizations():
  # 1. Load the preprocessed dataset
  current_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(
      current_dir, "../preprocessing/processed_data/cleaned_processed_facility.csv"
  )

  if not os.path.exists(file_path):
    file_path = "ml/preprocessing/processed_data/cleaned_processed_facility.csv"

  df = pd.read_csv(file_path)
  print("--- Generating Visualizations ---")

  os.makedirs(current_dir, exist_ok=True)

  # 2. Visualization 1: Cleanliness Score vs Odor Score Scatter Plot
  plt.figure(figsize=(8, 6))
  plt.scatter(
      df["cleanliness_score"],
      df["odor_score"],
      c=df["cleanliness_score"],
      cmap="viridis",
      alpha=0.7,
  )
  plt.title("Cleanliness Score vs Odor Score Analysis")
  plt.xlabel("Cleanliness Score")
  plt.ylabel("Odor Score")
  plt.colorbar(label="Cleanliness Level")
  plt.tight_layout()

  plot_path_1 = os.path.join(current_dir, "hygiene_risk_scatter.png")
  plt.savefig(plot_path_1)
  plt.close()
  print(f"Saved plot 1 to: {plot_path_1}")

  # 3. Visualization 2: Hygiene Risk Count Bar Chart
  plt.figure(figsize=(6, 4))
  risk_counts = df["hygiene_risk"].value_counts()
  risk_counts.plot(kind="bar", color=["skyblue", "orange", "salmon"])
  plt.title("Distribution of Hygiene Risk Levels")
  plt.xlabel("Hygiene Risk")
  plt.ylabel("Count")
  plt.xticks(rotation=0)
  plt.tight_layout()

  plot_path_2 = os.path.join(current_dir, "hygiene_risk_distribution.png")
  plt.savefig(plot_path_2)
  plt.close()
  print(f"Saved plot 2 to: {plot_path_2}")

  print("\nAll visualizations generated successfully!")


if __name__ == "__main__":
  generate_visualizations()