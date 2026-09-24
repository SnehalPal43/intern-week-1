// Maps HTTP endpoints to corresponding controller functions and applies middleware.

const express = require('express');
const router = express.Router();
const employeeController = require('../controllers/employeeController');
const requestLogger = require('../middleware/requestLogger');

// Apply request logger middleware to all routes
router.use(requestLogger);

// REST API Endpoints
router.get('/', employeeController.getEmployees);           // GET all employees
router.get('/:id', employeeController.getEmployeeById);    // GET employee by ID
router.post('/', employeeController.createEmployee);       // POST create employee
router.put('/:id', employeeController.updateEmployee);     // PUT update employee
router.delete('/:id', employeeController.deleteEmployee);  // DELETE employee

module.exports = router;