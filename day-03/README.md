# Day 3: Data Analysis & Python for AI/ML

## Overview
Cleaned, analyzed, and visualized a real-world facility dataset using NumPy, Pandas, and Matplotlib.

## Project Structure
- `dataset/`: Contains raw (`facility_data.csv`) and cleaned data.
- `data-cleaning/`: Handles missing values, duplicates, and data formatting.
- `analysis/`: Computes statistical summaries and location groups.
- `visualizations/`: Generates bar charts, histograms, scatter plots, and trend lines.

## Problems Encountered & Solutions
- **Problem:** Encountered `FileNotFoundError` while executing scripts from nested subdirectories (`data-cleaning`, `analysis`, `visualizations`) because relative paths could not locate the `dataset` folder.
- **Solution:** Implemented **absolute file paths** (`r"C:\Users\ASUS\OneDrive\Desktop\intern-week-1\day-03\dataset\..."`) across all Python scripts to ensure reliable and independent file reading and saving.