//JavaScript Fundamentals & Array Methods Practice

// 1. Arrow Functions & Template Literals
const getEmployeeInfo = (name, department) => {
    return `Employee Name: ${name}, Department: ${department}`;
};
console.log(getEmployeeInfo("Rahul", "Engineering"));

// 2. Sample Data for Employees
const employees = [
    { id: 1, name: "Amit", department: "IT", salary: 50000 },
    { id: 2, name: "Priya", department: "HR", salary: 45000 },
    { id: 3, name: "Neha", department: "IT", salary: 60000 },
    { id: 4, name: "Rohan", department: "Sales", salary: 40000 }
];

// 3. Array Method: filter (Get only IT employees)
const itEmployees = employees.filter(emp => emp.department === "IT");
console.log("IT Employees:", itEmployees);

// 4. Array Method: map (Get names only)
const employeeNames = employees.map(emp => emp.name);
console.log("Employee Names:", employeeNames);

// 5. Array Method: reduce (Total Salary)
const totalSalary = employees.reduce((sum, emp) => sum + emp.salary, 0);
console.log("Total Salary Expense:", totalSalary);