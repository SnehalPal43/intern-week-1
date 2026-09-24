// Handles data storage operations and mimics database interactions.

let employees = [
    { id: '1', name: 'Rahul Sharma', department: 'Engineering', salary: 75000 },
    { id: '2', name: 'Priya Verma', department: 'Human Resources', salary: 60000 },
    { id: '3', name: 'Amit Patel', department: 'Marketing', salary: 55000 },
    { id: '4', name: 'Sneha Joshi', department: 'Engineering', salary: 80000 },
    { id: '5', name: 'Rohit Kumar', department: 'Sales', salary: 50000 },
    { id: '6', name: 'Neha Gupta', department: 'Finance', salary: 70000 },
    { id: '7', name: 'Vikas Singh', department: 'Engineering', salary: 85000 },
    { id: '8', name: 'Pooja Deshmukh', department: 'Marketing', salary: 52000 },
    { id: '9', name: 'Aniket Kulkarni', department: 'HR', salary: 48000 },
    { id: '10', name: 'Karan Malhotra', department: 'Finance', salary: 90000 },
    { id: '11', name: 'Divya Rao', department: 'Engineering', salary: 78000 },
    { id: '12', name: 'Manish Tiwari', department: 'Sales', salary: 53000 },
    { id: '13', name: 'Swati Patil', department: 'Marketing', salary: 56000 },
    { id: '14', name: 'Akash Mehra', department: 'Finance', salary: 72000 },
    { id: '15', name: 'Ritu Sen', department: 'Engineering', salary: 82000 },
    { id: '16', name: 'Sandeep Nair', department: 'HR', salary: 49000 },
    { id: '17', name: 'Megha Kadam', department: 'Sales', salary: 51000 },
    { id: '18', name: 'Kunal Shinde', department: 'Engineering', salary: 88000 },
    { id: '19', name: 'Tanvi More', department: 'Marketing', salary: 59000 },
    { id: '20', name: 'Alok Varma', department: 'Finance', salary: 76000 }
];

class EmployeeModel {
    static async getAll() {
        return employees;
    }

    static async getById(id) {
        return employees.find(emp => emp.id === id);
    }

    static async create(employeeData) {
        const newEmployee = {
            id: Date.now().toString(),
            ...employeeData
        };
        employees.push(newEmployee);
        return newEmployee;
    }

    static async update(id, updatedData) {
        const index = employees.findIndex(emp => emp.id === id);
        if (index === -1) return null;

        employees[index] = { ...employees[index], ...updatedData };
        return employees[index];
    }

    static async delete(id) {
        const index = employees.findIndex(emp => emp.id === id);
        if (index === -1) return false;

        employees.splice(index, 1);
        return true;
    }
}

module.exports = EmployeeModel;