# Practical Assignment - Employee Management System 
import json
import os

DATA_FILE = "employees.json"

# Load data from JSON file with Exception Handling
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Corrupted JSON file. Starting with empty records.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# Save data to JSON file
def save_data(employees):
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(employees, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# 1. Add Employee
def add_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID: "))
        # Check if ID already exists
        if any(emp["id"] == emp_id for emp in employees):
            print("Error: Employee ID already exists!")
            return

        name = input("Enter Name: ").strip()
        if not name:
            print("Error: Name cannot be empty!")
            return
            
        department = input("Enter Department: ").strip()
        salary = float(input("Enter Salary: "))
        
        new_emp = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        }
        
        employees.append(new_emp)
        save_data(employees)
        print("Success: Employee added successfully!")
    except ValueError:
        print("Invalid input! Please enter correct numerical values for ID and Salary.")

# 2. View / Statistics Report
def show_statistics(employees):
    if not employees:
        print("No records found.")
        return
        
    salaries = [emp["salary"] for emp in employees]
    print(f"\n--- Statistics Report ---")
    print(f"Total Records: {len(employees)}")
    print(f"Average Salary: {sum(salaries)/len(salaries):.2f}")
    print(f"Minimum Salary: {min(salaries)}")
    print(f"Maximum Salary: {max(salaries)}")

# 3. Search Employee
def search_employee(employees):
    query = input("Enter employee name or ID to search: ").strip().lower()
    found = [emp for emp in employees if query in str(emp["id"]) or query in emp["name"].lower()]
    
    if found:
        print("\n--- Search Results ---")
        for emp in found:
            print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']} | Salary: {emp['salary']}")
    else:
        print("No matching records found.")

# 4. Update Employee
def update_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID to update: "))
    except ValueError:
        print("Error: Please enter a valid numeric ID.")
        return

    for emp in employees:
        if emp["id"] == emp_id:
            print(f"Current Details -> Name: {emp['name']}, Dept: {emp['department']}, Salary: {emp['salary']}")
            
            new_name = input("Enter new name (leave blank to keep same): ").strip()
            new_dept = input("Enter new department (leave blank to keep same): ").strip()
            new_salary_str = input("Enter new salary (leave blank to keep same): ").strip()

            if new_name:
                emp["name"] = new_name
            if new_dept:
                emp["department"] = new_dept
            if new_salary_str:
                try:
                    emp["salary"] = float(new_salary_str)
                except ValueError:
                    print("Invalid salary format. Salary not updated.")

            save_data(employees)
            print("Success: Employee updated successfully!")
            return

    print("Error: Employee ID not found.")

# 5. Delete Employee
def delete_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID to delete: "))
        initial_len = len(employees)
        employees[:] = [emp for emp in employees if emp["id"] != emp_id]
        
        if len(employees) < initial_len:
            save_data(employees)
            print("Success: Employee deleted successfully!")
        else:
            print("Error: Employee ID not found.")
    except ValueError:
        print("Invalid ID format.")

# 6. Filter Employees 
def filter_employees(employees):
    if not employees:
        print("No records found.")
        return

    dept = input("Enter department name to filter (e.g., IT, HR): ").strip().lower()
    filtered = [emp for emp in employees if emp["department"].lower() == dept]

    if not filtered:
        print(f"No employees found in department '{dept}'.")
        return

    print(f"\n--- Employees in Department: {dept.upper()} ---")
    for emp in filtered:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']} | Salary: {emp['salary']}")

# 7. Sort Employees
def sort_employees(employees):
    if not employees:
        print("No records found.")
        return

    print("\n1. Sort by Salary (Low to High)")
    print("2. Sort by Salary (High to Low)")
    print("3. Sort by ID")
    choice = input("Choose sorting option (1-3): ").strip()

    if choice == '1':
        sorted_emps = sorted(employees, key=lambda x: x['salary'])
        print("\n--- Sorted by Salary (Low to High) ---")
    elif choice == '2':
        sorted_emps = sorted(employees, key=lambda x: x['salary'], reverse=True)
        print("\n--- Sorted by Salary (High to Low) ---")
    elif choice == '3':
        sorted_emps = sorted(employees, key=lambda x: x['id'])
        print("\n--- Sorted by ID ---")
    else:
        print("Invalid choice.")
        return

    for emp in sorted_emps:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']} | Salary: {emp['salary']}")

# Main Menu Loop
def main():
    employees = load_data()
    
    while True:
        print("\n--- Employee Management System ---")
        print("1. View Statistics & Records")
        print("2. Add Employee")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Filter Employees")
        print("7. Sort Employees")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            show_statistics(employees)
            print("\nAll Records:")
            for emp in employees:
                print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']} | Salary: {emp['salary']}")
        elif choice == "2":
            add_employee(employees)
        elif choice == "3":
            search_employee(employees)
        elif choice == "4":
            update_employee(employees)
        elif choice == "5":
            delete_employee(employees)
        elif choice == "6":
            filter_employees(employees)
        elif choice == "7":
            sort_employees(employees)
        elif choice == "8":
            print("Exiting management system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 to 8.")

if __name__ == "__main__":
    main()