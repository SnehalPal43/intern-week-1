// Processes HTTP requests, invokes service methods, and sends back JSON responses.

const employeeService = require('../services/employeeService');

class EmployeeController {
    // GET: Retrieve all employees
    async getEmployees(req, res, next) {
        try {
            const employees = await employeeService.fetchAllEmployees();
            res.status(200).json({ success: true, data: employees });
        } catch (error) {
            next(error);
        }
    }

    // GET: Retrieve a single employee by ID
    async getEmployeeById(req, res, next) {
        try {
            const employee = await employeeService.fetchEmployeeById(req.params.id);
            res.status(200).json({ success: true, data: employee });
        } catch (error) {
            next(error);
        }
    }

    // POST: Create a new employee
    async createEmployee(req, res, next) {
        try {
            const newEmployee = await employeeService.registerEmployee(req.body);
            res.status(201).json({ success: true, message: 'Employee created successfully', data: newEmployee });
        } catch (error) {
            next(error);
        }
    }

    // PUT: Update an existing employee
    async updateEmployee(req, res, next) {
        try {
            const updatedEmployee = await employeeService.modifyEmployee(req.params.id, req.body);
            res.status(200).json({ success: true, message: 'Employee updated successfully', data: updatedEmployee });
        } catch (error) {
            next(error);
        }
    }

    // DELETE: Remove an employee
    async deleteEmployee(req, res, next) {
        try {
            const result = await employeeService.removeEmployee(req.params.id);
            res.status(200).json({ success: true, ...result });
        } catch (error) {
            next(error);
        }
    }
}

module.exports = new EmployeeController();