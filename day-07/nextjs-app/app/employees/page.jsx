// Fetches and displays the list of employees from the backend API with delete functionality.

'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';

export default function EmployeesPage() {
    const [employees, setEmployees] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch employees from the Express backend API
    const fetchEmployees = async () => {
        try {
            const response = await fetch('http://localhost:5000/api/employees');
            const data = await response.json();
            if (data.success) {
                setEmployees(data.data);
            } else {
                setError('Failed to load employees.');
            }
        } catch (err) {
            setError('Error connecting to backend server.');
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchEmployees();
    }, []);

    // Handle employee deletion
    const handleDelete = async (id) => {
        if (!confirm('Are you sure you want to delete this employee?')) return;

        try {
            const response = await fetch(`http://localhost:5000/api/employees/${id}`, {
                method: 'DELETE',
            });
            const data = await response.json();
            if (data.success) {
                // Refresh list after deletion
                setEmployees(employees.filter(emp => emp.id !== id));
            } else {
                alert(data.error || 'Failed to delete employee.');
            }
        } catch (err) {
            alert('Error connecting to server.');
        }
    };

    if (loading) return <p style={{ textAlign: 'center' }}>Loading employees...</p>;
    if (error) return <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>;

    return (
        <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
                <h1 style={{ color: '#2c3e50', margin: 0 }}>Employee Directory</h1>
                <Link href="/employees/create" style={{ backgroundColor: '#27ae60', color: 'white', padding: '10px 15px', borderRadius: '5px', textDecoration: 'none', fontWeight: 'bold' }}>+ Add New Employee</Link>
            </div>

            {employees.length === 0 ? (
                <p>No employees found.</p>
            ) : (
                <div style={{ display: 'grid', gap: '15px' }}>
                    {employees.map((emp) => (
                        <div key={emp.id} style={{ background: 'white', padding: '15px 20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                            <div>
                                <h3 style={{ margin: '0 0 5px 0', color: '#333' }}>{emp.name}</h3>
                                <p style={{ margin: 0, color: '#666', fontSize: '14px' }}>Department: <b>{emp.department}</b> | Salary: <b>₹{emp.salary}</b></p>
                            </div>
                            <div style={{ display: 'flex', gap: '10px' }}>
                                <Link href={`/employees/${emp.id}`} style={{ backgroundColor: '#3498db', color: 'white', padding: '6px 12px', borderRadius: '4px', textDecoration: 'none', fontSize: '14px' }}>View / Edit</Link>
                                <button onClick={() => handleDelete(emp.id)} style={{ backgroundColor: '#e74c3c', color: 'white', border: 'none', padding: '6px 12px', borderRadius: '4px', cursor: 'pointer', fontSize: '14px' }}>Delete</button>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}