// SERVER ENTRY POINT (server.js)

// This file initializes the Express application, loads global 
// middleware, sets up routes, and starts the server.

const express = require('express');
const cors = require('cors');
const employeeRoutes = require('./routes/employeeRoutes');
const errorHandler = require('./middleware/errorHandler');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware for parsing incoming JSON requests
app.use(express.json());

// Enable Cross-Origin Resource Sharing for frontend communication
app.use(cors());

// Mount the employee REST API routes under the '/api' prefix
app.use('/api/employees', employeeRoutes);

// Global Error Handling Middleware
app.use(errorHandler);

// Start the server and listen on the specified port
app.listen(PORT, () => {
    console.log(`Server is running successfully on http://localhost:${PORT}`);
});