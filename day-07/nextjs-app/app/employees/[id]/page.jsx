// ==========================================
// EMPLOYEE DETAILS & EDIT PAGE (app/employees/[id]/page.jsx)
// ==========================================
// Fetches a single employee's data, displays details, and provides an update form.

'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';

export default function EmployeeDetailPage({ params }) {
    // Directly extract id from params for Next.js 14 compatibility
    const id = params.id;

    const router = useRouter();
    const [formData, setFormData] = useState({ name: '', department: '', salary: '' });
    const [loading, setLoading] = useState(true);
    const [updating, setUpdating] = useState(false);
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);

    // Fetch single employee data on load
    useEffect(() => {
        const fetchEmployee = async () => {
            try {
                const response = await fetch(`http://localhost:5000/api/employees/${id}`);
                const data = await response.json();
                if (data.success) {
                    setFormData({
                        name: data.data.name,
                        department: data.data.department,
                        salary: data.data.salary
                    });
                } else {
                    setError('Employee not found.');
                }
            } catch (err) {
                setError('Error connecting to backend server.');
            } finally {
                setLoading(false);
            }
        };

        if (id) {
            fetchEmployee();
        }
    }, [id]);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleUpdate = async (e) => {
        e.preventDefault();
        setUpdating(true);
        setError(null);
        setSuccessMessage(null);

        try {
            const response = await fetch(`http://localhost:5000/api/employees/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            if (data.success) {
                setSuccessMessage('Employee updated successfully!');
                setTimeout(() => {
                    router.push('/employees');
                }, 1500);
            } else {
                setError(data.error || 'Failed to update employee.');
            }
        } catch (err) {
            setError('Error connecting to backend server.');
        } finally {
            setUpdating(false);
        }
    };

    if (loading) return <p style={{ textAlign: 'center' }}>Loading employee details...</p>;
    if (error && !formData.name) return <p style={{ color: 'red', textAlign: 'center' }}>{error}</p>;

    return (
        <div style={{ maxWidth: '500px', margin: '0 auto', background: 'white', padding: '30px', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
                <h2 style={{ margin: 0, color: '#2c3e50' }}>Edit Employee (ID: {id})</h2>
                <Link href="/employees" style={{ color: '#3498db', textDecoration: 'none', fontSize: '14px' }}>← Back to List</Link>
            </div>

            {error && <p style={{ color: 'red', backgroundColor: '#fde8e8', padding: '10px', borderRadius: '4px' }}>{error}</p>}
            {successMessage && <p style={{ color: 'green', backgroundColor: '#e8fde8', padding: '10px', borderRadius: '4px' }}>{successMessage}</p>}

            <form onSubmit={handleUpdate}>
                <div style={{ marginBottom: '15px' }}>
                    <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold', color: '#333' }}>Full Name:</label>
                    <input type="text" name="name" value={formData.name} onChange={handleChange} required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc', boxSizing: 'border-box' }} />
                </div>

                <div style={{ marginBottom: '15px' }}>
                    <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold', color: '#333' }}>Department:</label>
                    <input type="text" name="department" value={formData.department} onChange={handleChange} required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc', boxSizing: 'border-box' }} />
                </div>

                <div style={{ marginBottom: '20px' }}>
                    <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold', color: '#333' }}>Salary (₹):</label>
                    <input type="number" name="salary" value={formData.salary} onChange={handleChange} required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc', boxSizing: 'border-box' }} />
                </div>

                <button type="submit" disabled={updating} style={{ width: '100%', backgroundColor: '#3498db', color: 'white', border: 'none', padding: '12px', borderRadius: '4px', fontSize: '16px', fontWeight: 'bold', cursor: 'pointer' }}>
                    {updating ? 'Updating...' : 'Update Employee'}
                </button>
            </form>
        </div>
    );
}