import React, { useState, useMemo } from 'react';
import type { Employee } from './types';
import './App.css';

function App() {
  // Initial Mock State
  const [employees, setEmployees] = useState<Employee[]>([
    { id: 1, name: "Amit Sharma", department: "Engineering", salary: 55000, email: "amit@company.com" },
    { id: 2, name: "Priya Verma", department: "HR", salary: 48000, email: "priya@company.com" },
    { id: 3, name: "Rahul Singh", department: "Marketing", salary: 42000, email: "rahul@company.com" }
  ]);

  // Form State
  const [name, setName] = useState('');
  const [department, setDepartment] = useState('Engineering');
  const [salary, setSalary] = useState('');
  const [email, setEmail] = useState('');
  const [editingId, setEditingId] = useState<number | null>(null);

  // Search, Filter & Sort State
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedDept, setSelectedDept] = useState('All');
  const [sortOrder, setSortOrder] = useState('');

  // 1. SUMMARY METRICS CALCULATION (using useMemo for optimization)
  const totalEmployees = employees.length;
  const averageSalary = totalEmployees > 0 
    ? Math.round(employees.reduce((acc, curr) => acc + curr.salary, 0) / totalEmployees) 
    : 0;
  const uniqueDepartments = new Set(employees.map(e => e.department)).size;

  // 2. FILTER & SORT LOGIC
  const filteredEmployees = useMemo(() => {
    return employees.filter(emp => {
      const matchesName = emp.name.toLowerCase().includes(searchTerm.toLowerCase());
      const matchesDept = selectedDept === 'All' || emp.department === selectedDept;
      return matchesName && matchesDept;
    }).sort((a, b) => {
      if (sortOrder === 'low-high') return a.salary - b.salary;
      if (sortOrder === 'high-low') return b.salary - a.salary;
      return 0;
    });
  }, [employees, searchTerm, selectedDept, sortOrder]);

  // 3. ADD / EDIT CRUD HANDLER
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name || !salary) {
      alert("Please fill in all mandatory fields!");
      return;
    }

    if (editingId !== null) {
      // Update existing
      setEmployees(employees.map(emp => 
        emp.id === editingId ? { ...emp, name, department, salary: Number(salary), email } : emp
      ));
      setEditingId(null);
    } else {
      // Add new
      const newEmp: Employee = {
        id: employees.length > 0 ? employees[employees.length - 1].id + 1 : 1,
        name,
        department,
        salary: Number(salary),
        email
      };
      setEmployees([...employees, newEmp]);
    }

    // Reset Form
    setName('');
    setDepartment('Engineering');
    setSalary('');
    setEmail('');
  };

  // 4. EDIT POPULATE
  const handleEdit = (emp: Employee) => {
    setEditingId(emp.id);
    setName(emp.name);
    setDepartment(emp.department);
    setSalary(emp.salary.toString());
    setEmail(emp.email || '');
  };

  // 5. DELETE HANDLER
  const handleDelete = (id: number) => {
    setEmployees(employees.filter(emp => emp.id !== id));
  };

  // 6. DETAILS HANDLER
  const handleDetails = (emp: Employee) => {
    alert(`Employee Details:\nID: ${emp.id}\nName: ${emp.name}\nDepartment: ${emp.department}\nSalary: ₹${emp.salary}\nEmail: ${emp.email || 'N/A'}`);
  };

  return (
    <div className="dashboard-container" style={{ padding: '20px', fontFamily: 'Arial, sans-serif', maxWidth: '1000px', margin: 'auto' }}>
      <h1>React Employee Dashboard (TypeScript)</h1>

      {/* Summary Metric Cards */}
      <div className="metrics-container" style={{ display: 'flex', gap: '20px', marginBottom: '20px' }}>
        <div style={{ background: '#e3f2fd', padding: '15px', borderRadius: '8px', flex: 1, textAlign: 'center' }}>
          <h3>Total Employees</h3>
          <p style={{ fontSize: '24px', fontWeight: 'bold' }}>{totalEmployees}</p>
        </div>
        <div style={{ background: '#e8f5e9', padding: '15px', borderRadius: '8px', flex: 1, textAlign: 'center' }}>
          <h3>Average Salary</h3>
          <p style={{ fontSize: '24px', fontWeight: 'bold' }}>₹{averageSalary}</p>
        </div>
        <div style={{ background: '#fff3e0', padding: '15px', borderRadius: '8px', flex: 1, textAlign: 'center' }}>
          <h3>Departments</h3>
          <p style={{ fontSize: '24px', fontWeight: 'bold' }}>{uniqueDepartments}</p>
        </div>
      </div>

      {/* Controls: Search, Filter, Sort */}
      <div className="controls" style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <input 
          type="text" 
          placeholder="Search by name..." 
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ padding: '8px', flex: 2 }}
        />
        <select value={selectedDept} onChange={(e) => setSelectedDept(e.target.value)} style={{ padding: '8px', flex: 1 }}>
          <option value="All">All Departments</option>
          <option value="Engineering">Engineering</option>
          <option value="HR">HR</option>
          <option value="Marketing">Marketing</option>
        </select>
        <select value={sortOrder} onChange={(e) => setSortOrder(e.target.value)} style={{ padding: '8px', flex: 1 }}>
          <option value="">Sort by Salary</option>
          <option value="low-high">Low to High</option>
          <option value="high-low">High to Low</option>
        </select>
      </div>

      {/* Add / Edit Form */}
      <form onSubmit={handleSubmit} style={{ background: '#f5f5f5', padding: '15px', borderRadius: '8px', marginBottom: '20px', display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
        <input type="text" placeholder="Full Name" value={name} onChange={(e) => setName(e.target.value)} style={{ padding: '8px', flex: 1 }} required />
        <select value={department} onChange={(e) => setDepartment(e.target.value)} style={{ padding: '8px', flex: 1 }}>
          <option value="Engineering">Engineering</option>
          <option value="HR">HR</option>
          <option value="Marketing">Marketing</option>
        </select>
        <input type="number" placeholder="Salary" value={salary} onChange={(e) => setSalary(e.target.value)} style={{ padding: '8px', flex: 1 }} required />
        <input type="email" placeholder="Email (Optional)" value={email} onChange={(e) => setEmail(e.target.value)} style={{ padding: '8px', flex: 1 }} />
        <button type="submit" style={{ background: '#28a745', color: 'white', border: 'none', padding: '8px 15px', cursor: 'pointer', borderRadius: '4px' }}>
          {editingId !== null ? "Update Employee" : "Add Employee"}
        </button>
      </form>

      {/* Employee Table */}
      <table border={1} cellPadding={10} style={{ width: '100%', borderCollapse: 'collapse', background: 'white' }}>
        <thead>
          <tr style={{ background: '#007bff', color: 'white' }}>
            <th>ID</th>
            <th>Name</th>
            <th>Department</th>
            <th>Salary</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {filteredEmployees.length > 0 ? (
            filteredEmployees.map(emp => (
              <tr key={emp.id}>
                <td>{emp.id}</td>
                <td>{emp.name}</td>
                <td>{emp.department}</td>
                <td>₹{emp.salary}</td>
                <td>{emp.email || 'N/A'}</td>
                <td>
                  <button onClick={() => handleDetails(emp)} style={{ background: '#17a2b8', color: 'white', border: 'none', padding: '5px', marginRight: '5px', cursor: 'pointer', borderRadius: '3px' }}>Details</button>
                  <button onClick={() => handleEdit(emp)} style={{ background: '#ffc107', border: 'none', padding: '5px', marginRight: '5px', cursor: 'pointer', borderRadius: '3px' }}>Edit</button>
                  <button onClick={() => handleDelete(emp.id)} style={{ background: '#dc3545', color: 'white', border: 'none', padding: '5px', cursor: 'pointer', borderRadius: '3px' }}>Delete</button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan={6} style={{ textAlign: 'center' }}>No employees found</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default App;
