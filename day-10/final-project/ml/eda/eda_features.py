import os
import pandas as pd


def perform_eda_and_selection():
  # 1. Load the preprocessed dataset
  current_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(
      current_dir, "../preprocessing/processed_data/cleaned_processed_facility.csv"
  )

  if not os.path.exists(file_path):
    file_path = "ml/preprocessing/processed_data/cleaned_processed_facility.csv"

  df = pd.read_csv(file_path)
  print("--- Exploratory Data Analysis (EDA) Summary ---")

  # 2. Display basic statistical overview
  print(df.describe())

  # 3. Feature Selection: Correlation with the target variable (numeric encoding of hygiene_risk)
  # Encoding target 'hygiene_risk' temporarily for correlation check
  df_corr = df.copy()
  df_corr["hygiene_risk_encoded"] = df_corr["hygiene_risk"].astype("category").cat.codes
  
  print("\n--- Feature Correlation with Hygiene Risk ---")
  correlation = df_corr.corr(numeric_only=True)["hygiene_risk_encoded"].sort_values(ascending=False)
  print(correlation)

  # 4. Save EDA summary report to the evaluation folder
  eval_dir = os.path.join(current_dir, "../evaluation")
  os.makedirs(eval_dir, exist_ok=True)
  report_path = os.path.join(eval_dir, "eda_summary_report.txt")

  with open(report_path, "w") as f:
    f.write("=== EDA AND FEATURE SELECTION REPORT ===\n\n")
    f.write(str(df.describe()))
    f.write("\n\n=== CORRELATION WITH HYGIENE RISK ===\n\n")
    f.write(str(correlation))

  print(f"\nEDA summary report saved successfully to: {report_path}")


if __name__ == "__main__":
  perform_eda_and_selection()