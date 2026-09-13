# Employee Management System 

employees = []

def add_employee():
    print("\n--- Add New Employee ---")
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    
    emp = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }
    employees.append(emp)
    print("Employee added successfully!")

def view_employees():
    print("\n--- Employee List ---")
    if not employees:
        print("No employees found.")
        return
        
    for emp in employees:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']} | Salary: {emp['salary']}")

def update_employee():
    print("\n--- Update Employee ---")
    emp_id = input("Enter Employee ID to update: ")
    
    for emp in employees:
        if emp['id'] == emp_id:
            print("Enter new details (leave blank to keep current):")
            name = input(f"New Name ({emp['name']}): ")
            dept = input(f"New Department ({emp['department']}): ")
            sal = input(f"New Salary ({emp['salary']}): ")
            
            if name != "":
                emp['name'] = name
            if dept != "":
                emp['department'] = dept
            if sal != "":
                emp['salary'] = float(sal)
                
            print("Employee updated successfully!")
            return
            
    print("Employee not found.")

def search_employee():
    print("\n--- Search Employee ---")
    emp_id = input("Enter Employee ID to search: ")
    
    for emp in employees:
        if emp['id'] == emp_id:
            print(f"Found! Name: {emp['name']}, Dept: {emp['department']}, Salary: {emp['salary']}")
            return
            
    print("Employee not found.")

def delete_employee():
    print("\n--- Delete Employee ---")
    emp_id = input("Enter Employee ID to delete: ")
    
    global employees
    new_list = []
    deleted = False
    
    for emp in employees:
        if emp['id'] != emp_id:
            new_list.append(emp)
        else:
            deleted = True
            
    employees = new_list
    if deleted:
        print("Employee deleted successfully!")
    else:
        print("Employee not found.")

def highest_salary():
    print("\n--- Highest Salary Employee ---")
    if not employees:
        print("No employees found.")
        return
        
    max_sal = employees[0]['salary']
    for emp in employees:
        if emp['salary'] > max_sal:
            max_sal = emp['salary']
            
    print(f"Highest Salary: {max_sal}")
    print("Employee(s) with highest salary:")
    for emp in employees:
        if emp['salary'] == max_sal:
            print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['department']}")

def average_salary():
    print("\n--- Average Salary ---")
    if not employees:
        print("No employees found.")
        return
        
    total = 0
    for emp in employees:
        total = total + emp['salary']
        
    avg = total / len(employees)
    print(f"Average Salary of all employees: {avg:.2f}")

def department_filter():
    print("\n--- Department Filter ---")
    dept = input("Enter department name to filter: ").strip().lower()
    
    found = False
    for emp in employees:
        if emp['department'].strip().lower() == dept:
            print(f"ID: {emp['id']} | Name: {emp['name']} | Salary: {emp['salary']}")
            found = True
            
    if not found:
        print("No employees found in this department.")

# Main CLI Menu Loop
while True:
    print("\n=== Employee Management System ===")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Delete Employee")
    print("6. Highest Salary")
    print("7. Average Salary")
    print("8. Department Filter")
    print("9. Exit")
    
    choice = input("Enter your choice (1-9): ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        view_employees()
    elif choice == '3':
        update_employee()
    elif choice == '4':
        search_employee()
    elif choice == '5':
        delete_employee()
    elif choice == '6':
        highest_salary()
    elif choice == '7':
        average_salary()
    elif choice == '8':
        department_filter()
    elif choice == '9':
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 9.")