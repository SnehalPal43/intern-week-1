// 1. Enums & Interfaces
enum Department {
    IT = "IT",
    HR = "HR",
    Engineering = "Engineering",
    Marketing = "Marketing"
}

interface Employee {
    id: number;
    name: string;
    department: Department;
    salary: number;
    email?: string; 
}

// 2. Objects & Arrays using TypeScript Types
const emp1: Employee = {
    id: 1,
    name: "Amit Sharma",
    department: Department.Engineering,
    salary: 60000,
    email: "amit@company.com"
};

const employees: Employee[] = [
    emp1,
    { id: 2, name: "Priya Verma", department: Department.HR, salary: 50000 }
];

// 3. Typed Function with Return Type
const calculateTotalSalary = (empList: Employee[]): number => {
    return empList.reduce((total, emp) => total + emp.salary, 0);
};

console.log("Total Salary Expense:", calculateTotalSalary(employees));