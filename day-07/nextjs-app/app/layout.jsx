// Defines the HTML structure, shared navigation, and global layout for all pages.

import Link from 'next/link';

export const metadata = {
    title: 'Employee Management Dashboard',
    description: 'Next.js App Router interface connected to Node.js backend API',
};

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body style={{ fontFamily: 'Arial, sans-serif', margin: '0', padding: '0', backgroundColor: '#f4f7f6' }}>
                {/* Navigation Header */}
                <header style={{ backgroundColor: '#2c3e50', color: 'white', padding: '1rem 2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h2 style={{ margin: 0 }}>🏢 Company Dashboard</h2>
                    <nav>
                        <Link href="/employees" style={{ color: 'white', textDecoration: 'none', marginRight: '20px', fontWeight: 'bold' }}>All Employees</Link>
                        <Link href="/employees/create" style={{ backgroundColor: '#3498db', color: 'white', padding: '8px 15px', borderRadius: '4px', textDecoration: 'none' }}>+ Add Employee</Link>
                    </nav>
                </header>

                {/* Main Content Area */}
                <main style={{ padding: '2rem', maxWidth: '1000px', margin: '0 auto' }}>
                    {children}
                </main>
            </body>
        </html>
    );
}