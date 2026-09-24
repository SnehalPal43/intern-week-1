// Form to register a new employee and send data to the backend API.

'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';

export default function CreateEmployeePage() {
    const router = useRouter();
    const [formData, setFormData] = useState({
        name: '',
        department: '',
        salary: ''
    });
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await fetch('http://localhost:5000/api/employees', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });

            const data = await response.json();
            if (data.success) {
                router.push('/employees'); // Redirect to employee list after success
            } else {
                setError(data.error || 'Failed to create employee.');
            }
        } catch (err) {
            setError('Error connecting to backend server.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ maxWidth: '500px', margin: '0 auto', background: 'white', padding: '30px', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
                <h2 style={{ margin: 0, color: '#2c3e50' }}>Add New Employee</h2>
                <Link href="/employees" style={{ color: '#3498db', textDecoration: 'none', fontSize: '14px' }}>← Back to List</Link>
            </div>

            {error && <p style={{ color: 'red', backgroundColor: '#fde8e8', padding: '10px', borderRadius: '4px' }}>{error}</p>}

            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '15px' }}>
                    <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold', color: '#333' }}>Full Name:</label>
                    <input type="text" name="name" value={formData.name} onChange={handleChange} required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc', boxSizing: 'border-box' }} placeholder="Enter employee name" />
                </div>

                <div style={{ marginBottom: '15px' }}>
                    <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold', color: '#333' }}>Department:</label>
                    <input type="text" name="department" value={formData.department} onChange={handleChange} required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc', boxSizing: 'border-box' }} placeholder="e.g. Engineering, HR" />
                </div>

                <div style={{ marginBottom: '20px' }}>
                    <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold', color: '#333' }}>Salary (₹):</label>
                    <input type="number" name="salary" value={formData.salary} onChange={handleChange} required style={{ width: '100%', padding: '10px', borderRadius: '4px', border: '1px solid #ccc', boxSizing: 'border-box' }} placeholder="e.g. 75000" />
                </div>

                <button type="submit" disabled={loading} style={{ width: '100%', backgroundColor: '#27ae60', color: 'white', border: 'none', padding: '12px', borderRadius: '4px', fontSize: '16px', fontWeight: 'bold', cursor: 'pointer' }}>
                    {loading ? 'Saving...' : 'Save Employee'}
                </button>
            </form>
        </div>
    );
}