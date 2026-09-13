# Python Exercises - JSON Data Reader & Analysis System
import json

# Function to read data from JSON file with Exception Handling
def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print(f"Successfully loaded {len(data)} records from '{file_path}'\n")
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON data. Please check file format.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Function to analyze data (Missing values, Duplicates, Statistics, Category-wise breakdown)
def analyze_employee_data(emp_list):
    if not emp_list:
        print("No data available to analyze.")
        return

    total_records = len(emp_list)
    missing_count = 0
    seen_records = set()
    duplicate_count = 0
    dept_stats = {}
    valid_salaries = []

    for emp in emp_list:
        # Check for missing values 
        if emp.get("salary") is None or not emp.get("name") or not emp.get("department"):
            missing_count += 1
        else:
            valid_salaries.append(emp["salary"])

        # Check for duplicates using a tuple identifier
        identifier = (emp.get("id"), emp.get("name"), emp.get("department"), emp.get("salary"))
        if identifier in seen_records:
            duplicate_count += 1
        else:
            seen_records.add(identifier)

        # Category-wise statistics 
        dept = emp.get("department", "Unknown")
        salary = emp.get("salary")
        if salary is not None:
            if dept not in dept_stats:
                dept_stats[dept] = []
            dept_stats[dept].append(salary)

    # Calculating basic statistics from valid salaries
    if valid_salaries:
        avg_salary = sum(valid_salaries) / len(valid_salaries)
        min_salary = min(valid_salaries)
        max_salary = max(valid_salaries)
    else:
        avg_salary = min_salary = max_salary = 0

    # Printing Reports
    print("--- Data Analysis Report ---")
    print(f"Total Records: {total_records}")
    print(f"Missing Values Count: {missing_count}")
    print(f"Duplicate Records Count: {duplicate_count}")
    print(f"Average Salary: {avg_salary:.2f}")
    print(f"Minimum Salary: {min_salary}")
    print(f"Maximum Salary: {max_salary}")

    print("\n--- Category-wise Statistics ---")
    for dept, salaries in dept_stats.items():
        dept_avg = sum(salaries) / len(salaries)
        print(f"Department: {dept} | Employee Count: {len(salaries)} | Avg Salary: {dept_avg:.2f}")

# Main execution flow

if __name__ == "__main__":
    # Path to our JSON file 
    file_name = "data.json"

    # Load records from file
    employees = load_data_from_json(file_name)

    # Run analysis on loaded records
    analyze_employee_data(employees)
