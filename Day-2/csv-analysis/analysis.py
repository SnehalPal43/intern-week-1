import csv
import os

# Path to the CSV file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data.csv")

def analyze_csv():
    if not os.path.exists(FILE_PATH):
        print(f"Error: {FILE_PATH} not found.")
        return

    rows = []
    missing_count = 0
    
    # 1. Read CSV file using standard loop
    try:
        with open(FILE_PATH, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check for missing values 
                is_missing = False
                for value in row.values():
                    if value == "":
                        is_missing = True
                        break
                if is_missing:
                    missing_count += 1
                
                rows.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    if not rows:
        print("No records found in CSV.")
        return

    # 2. Record Count
    total_records = len(rows)

    # 3. Check for Duplicates (Using a simple loop and set)
    seen_rows = set()
    duplicates_count = 0
    for r in rows:
        # Convert dictionary items to a tuple so it can be stored in a set
        row_tuple = tuple(r.items())
        if row_tuple in seen_rows:
            duplicates_count += 1
        else:
            seen_rows.add(row_tuple)

    # 4. Numeric Statistics (Salaries)
    salaries = []
    for r in rows:
        try:
            if r["salary"]:
                salaries.append(float(r["salary"]))
        except ValueError:
            pass

    if salaries:
        avg_salary = sum(salaries) / len(salaries)
        min_salary = min(salaries)
        max_salary = max(salaries)
    else:
        avg_salary = min_salary = max_salary = 0

    # 5. Category-wise Statistics
    dept_counts = {}
    for r in rows:
        dept = r.get("department", "").strip()
        if dept:
            if dept in dept_counts:
                dept_counts[dept] += 1
            else:
                dept_counts[dept] = 1

    # Print Analysis Report
    print("--- CSV Data Analysis Report ---")
    print(f"Total Records: {total_records}")
    print(f"Missing Values Rows: {missing_count}")
    print(f"Duplicate Rows: {duplicates_count}")
    print(f"Average Salary: {avg_salary:.2f}")
    print(f"Minimum Salary: {min_salary}")
    print(f"Maximum Salary: {max_salary}")
    print("\n--- Category-wise Statistics ---")
    for dept, count in dept_counts.items():
        print(f"Department '{dept}': {count} employees")

if __name__ == "__main__":
    analyze_csv()