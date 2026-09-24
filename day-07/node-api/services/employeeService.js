// Contains core business logic, validation checks, and data manipulation rules.

const EmployeeModel = require('../models/employeeModel');

class EmployeeService {
    async fetchAllEmployees() {
        return await EmployeeModel.getAll();
    }

    async fetchEmployeeById(id) {
        const employee = await EmployeeModel.getById(id);
        if (!employee) {
            throw new Error('Employee not found in the database.');
        }
        return employee;
    }

    async registerEmployee(data) {
        // Business rule validation: Check if required fields exist
        if (!data.name || !data.department || !data.salary) {
            throw new Error('Missing required fields: name, department, and salary are mandatory.');
        }
        return await EmployeeModel.create(data);
    }

    async modifyEmployee(id, data) {
        const existingEmployee = await EmployeeModel.getById(id);
        if (!existingEmployee) {
            throw new Error('Cannot update: Employee does not exist.');
        }
        return await EmployeeModel.update(id, data);
    }

    async removeEmployee(id) {
        const success = await EmployeeModel.delete(id);
        if (!success) {
            throw new Error('Cannot delete: Employee not found.');
        }
        return { message: 'Employee deleted successfully.' };
    }
}

module.exports = new EmployeeService();