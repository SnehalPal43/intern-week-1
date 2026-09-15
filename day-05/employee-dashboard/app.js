// 1.Employee Data 
let employees = [
    { id: 1, name: "Amit Sharma", department: "Engineering", salary: 75000 },
    { id: 2, name: "Priya Verma", department: "HR", salary: 52000 },
    { id: 3, name: "Rahul Singh", department: "Marketing", salary: 48000 },
    { id: 4, name: "Sneha Patel", department: "Engineering", salary: 82000 },
    { id: 5, name: "Vikram Malhotra", department: "Finance", salary: 95000 },
    { id: 6, name: "Ananya Deshmukh", department: "Sales", salary: 60000 },
    { id: 7, name: "Rohan Gupta", department: "Engineering", salary: 67000 },
    { id: 8, name: "Neha Joshi", department: "HR", salary: 49000 },
    { id: 9, name: "Karan Mehta", department: "Marketing", salary: 54000 },
    { id: 10, name: "Pooja Kulkarni", department: "Finance", salary: 72000 },
    { id: 11, name: "Aditya Kulkarni", department: "Operations", salary: 45000 },
    { id: 12, name: "Meera Nair", department: "Engineering", salary: 88000 },
    { id: 13, name: "Siddharth Rao", department: "Sales", salary: 62000 },
    { id: 14, name: "Divya Iyer", department: "HR", salary: 58000 },
    { id: 15, name: "Manish Tiwari", department: "Marketing", salary: 51000 },
    { id: 16, name: "Tanvi Kothari", department: "Finance", salary: 81000 },
    { id: 17, name: "Akash Deshmukh", department: "Operations", salary: 47000 },
    { id: 18, name: "Kritika Sen", department: "Engineering", salary: 79000 },
    { id: 19, name: "Varun Nambiar", department: "Sales", salary: 65000 },
    { id: 20, name: "Nisha Pillai", department: "HR", salary: 53000 }
];

// Selecting DOM Elements from index.html
const tableBody = document.getElementById("employeeTableBody");
const employeeForm = document.getElementById("employeeForm");
const searchInput = document.getElementById("searchInput");
const departmentFilter = document.getElementById("departmentFilter");
const sortSelect = document.getElementById("sortSelect");
const saveBtn = document.getElementById("saveBtn");

// 2. LISTING OPERATION: Render Data in Table
function renderTable(dataToRender) {
    tableBody.innerHTML = ""; // Clear existing table rows
    
    // If no employees match, show a friendly message
    if (dataToRender.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="5" style="text-align:center;">No employees found</td></tr>`;
        return;
    }

    // Loop through each employee and create table rows dynamically
    dataToRender.forEach(emp => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${emp.id}</td>
            <td>${emp.name}</td>
            <td>${emp.department}</td>
            <td>₹${emp.salary}</td>
            <td>
                <button class="details" onclick="viewDetails(${emp.id})" style="background-color: #17a2b8; color: white; border: none; padding: 5px 8px; border-radius: 3px; cursor: pointer; margin-right: 3px;">Details</button>
                <button class="edit" onclick="editEmployee(${emp.id})" style="background-color: #ffc107; border: none; padding: 5px 8px; border-radius: 3px; cursor: pointer; margin-right: 3px;">Edit</button>
                <button class="delete" onclick="deleteEmployee(${emp.id})" style="background-color: #dc3545; color: white; border: none; padding: 5px 8px; border-radius: 3px; cursor: pointer;">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// 3. ADD & EDIT OPERATION: Form Submission
employeeForm.addEventListener("submit", function(e) {
    e.preventDefault(); 

    const idField = document.getElementById("empId").value;
    const name = document.getElementById("name").value;
    const department = document.getElementById("department").value;
    const salary = Number(document.getElementById("salary").value);

    if (idField) {
        // EDIT: Update existing employee using map()
        employees = employees.map(emp => 
            emp.id == idField ? { ...emp, name, department, salary } : emp
        );
        saveBtn.textContent = "Add Employee";
        document.getElementById("empId").value = "";
    } else {
        // ADD: Create a new employee object and push to array
        const newEmp = {
            id: employees.length > 0 ? employees[employees.length - 1].id + 1 : 1,
            name,
            department,
            salary
        };
        employees.push(newEmp);
    }

    employeeForm.reset(); 
    renderTable(employees); 
});

// 4. DELETE OPERATION: Remove Employee by ID
window.deleteEmployee = function(id) {
    // Keep only those employees whose ID does not match the deleted ID using filter()
    employees = employees.filter(emp => emp.id !== id);
    renderTable(employees);
};

// 5. EDIT OPERATION: Load Data into Form
window.editEmployee = function(id) {
    // Find the specific employee using find()
    const emp = employees.find(e => e.id === id);
    if (emp) {
        document.getElementById("empId").value = emp.id;
        document.getElementById("name").value = emp.name;
        document.getElementById("department").value = emp.department;
        document.getElementById("salary").value = emp.salary;
        saveBtn.textContent = "Update Employee";
    }
};

// 6. DETAILS OPERATION: View Individual Info
window.viewDetails = function(id) {
    const emp = employees.find(e => e.id === id);
    if (emp) {
        alert(`--- Employee Details ---\n\nID: ${emp.id}\nName: ${emp.name}\nDepartment: ${emp.department}\nSalary: ₹${emp.salary}`);
    }
};

// 7. SEARCH OPERATION: Filter by Name
searchInput.addEventListener("input", function(e) {
    const searchText = e.target.value.toLowerCase();
    const filtered = employees.filter(emp => emp.name.toLowerCase().includes(searchText));
    renderTable(filtered);
});

// 8. FILTER OPERATION: Filter by Department
departmentFilter.addEventListener("change", function(e) {
    const selectedDept = e.target.value;
    if (selectedDept === "") {
        renderTable(employees); // Show all if no filter selected
    } else {
        const filtered = employees.filter(emp => emp.department === selectedDept);
        renderTable(filtered);
    }
});


// 9. SORT OPERATION: Sort by Salary
sortSelect.addEventListener("change", function(e) {
    const sortOrder = e.target.value;
    let sorted = [...employees]; 
    if (sortOrder === "low-high") {
        sorted.sort((a, b) => a.salary - b.salary);
    } else if (sortOrder === "high-low") {
        sorted.sort((a, b) => b.salary - a.salary);
    }

    renderTable(sorted);
});


// Initial render when page loads
renderTable(employees);