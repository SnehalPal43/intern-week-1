-- 1. Get all employees with their respective department names (JOIN)
SELECT employees.id, employees.name AS employee_name, departments.name AS department_name, employees.salary
FROM employees
JOIN departments ON employees.department_id = departments.id;

-- 2. Find the average salary of employees per department (GROUP BY, AVG)
SELECT departments.name AS department_name, AVG(employees.salary) AS average_salary
FROM employees
JOIN departments ON employees.department_id = departments.id
GROUP BY departments.name;

-- 3. Find the highest-paid employee (ORDER BY, LIMIT)
SELECT employees.name, employees.salary, departments.name AS department_name
FROM employees
JOIN departments ON employees.department_id = departments.id
ORDER BY employees.salary DESC
LIMIT 1;

-- 4. Find facilities that are marked as 'Poor' or need attention (WHERE)
SELECT * FROM facilities
WHERE status = 'Poor' OR status = 'Inactive';

-- 5. Count the total number of complaints per facility (GROUP BY, COUNT, JOIN)
SELECT facilities.name AS facility_name, COUNT(complaints.id) AS total_complaints
FROM facilities
LEFT JOIN complaints ON facilities.id = complaints.facility_id
GROUP BY facilities.id, facilities.name;

-- 6. Get complete inspection history for facilities including inspector names (JOIN)
SELECT inspections.id, facilities.name AS facility_name, users.name AS inspector_name, inspections.inspection_date, inspections.notes
FROM inspections
JOIN facilities ON inspections.facility_id = facilities.id
JOIN users ON inspections.inspector_id = users.id
ORDER BY inspections.inspection_date DESC;