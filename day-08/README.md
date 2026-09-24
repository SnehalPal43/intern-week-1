# Day-08 Practical Assignment: Laravel CRUD API & SQL Database Architecture

## 📋 Project Overview
This project is a comprehensive backend implementation for Day-08, combining a robust relational database schema, advanced analytical SQL queries, and a fully functional RESTful CRUD API built using Laravel. The system manages organizational departments, employees, facilities, regulatory inspections, and user complaints.

## 🛑 Problem Statement
Modern organizations struggle to track maintenance records, monitor facility conditions, handle user complaints, and analyze operational data efficiently. This project solves this by establishing a centralized, structured database paired with an API-driven backend to automate tracking, streamline data retrieval, and ensure seamless interaction between facilities and inspection logs.

## ✨ Features
- **Relational Database Design**: Complete schemas for Users, Departments, Employees, Facilities, Inspections, and Complaints with active foreign key constraints and cascade rules.
- **Advanced SQL Analytics**: Pre-written analytical queries utilizing `JOIN`, `GROUP BY`, `AVG`, `LIMIT`, and `WHERE` clauses for reporting.
- **RESTful CRUD API**: Fully operational API endpoints for `Facilities`, `Inspections`, and `Complaints`.
- **Data Validation & Integrity**: Form request validation on all store and update operations.
- **Eloquent Relationships**: Implemented `hasMany` and `belongsTo` relationships across models for seamless relational querying.

## 🛠 Technology Stack
- **Backend Framework**: Laravel (PHP 8.0.30)
- **Database Management System**: SQLite (database/database.sqlite)
- **Server Environment**: Apache / PHP Development Server (`php artisan serve`)
- **API Testing Tools**: Postman / Thunder Client / Browser

## 🏛 Architecture
The application follows the standard **MVC (Model-View-Controller)** and request-response lifecycle pattern for Laravel APIs:
Request → Route (api.php) → Controller → Eloquent Model → Database (SQLite) → JSON Response


## 🗄 Database Design
The database consists of 6 core tables with relational integrity:
1. **departments**: Stores department details (`id`, `name`).
2. **users**: Stores user/inspector details (`id`, `name`, `email`, `password`, `role`).
3. **employees**: Linked to departments (`id`, `name`, `department_id`, `salary`).
4. **facilities**: Core entity tracking locations (`id`, `name`, `location`, `status`).
5. **inspections**: Linked to facilities and users (`id`, `facility_id`, `inspector_id`, `inspection_date`, `notes`).
6. **complaints**: Linked to facilities and users (`id`, `facility_id`, `user_id`, `description`, `status`).

## 🔌 API Documentation
| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/api/facilities` | GET | Retrieve all facilities |
| `/api/facilities` | POST | Create a new facility |
| `/api/facilities/{id}` | GET | Show a single facility |
| `/api/facilities/{id}` | PUT/PATCH | Update a facility |
| `/api/facilities/{id}` | DELETE | Delete a facility |
*(Similar resource routes exist for `/api/inspections` and `/api/complaints`)*

## 📦 Installation
1. Clone or copy the project directory to your local machine.
2. Open terminal inside the `laravel-api/` directory.
3. Install dependencies:
   ```
   composer install
   ```
## ⚙️ Environment Variables
Configure your .env file in the laravel-api/ directory with correct database credentials:

DB_CONNECTION=sqlite
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel
DB_USERNAME=root
DB_PASSWORD=

## 🚀 How to Run

1. Ensure the SQLite database file is set up (Laravel will automatically use or create `database/database.sqlite`).
2. Run database migrations:
   ```
   php artisan migrate
   ```
Start the Laravel development server:

php artisan serve
Access the API endpoints via browser or Thunder Client at http://127.0.0.1:8000/api/facilities.

API testing verified successfully returning JSON arrays and resource objects with populated mock data.

## ⚠️ Challenges Faced

Database Configuration Issues: Initially faced environment/connection setup errors while attempting to configure MySQL/XAMPP on the local machine.

Mass Assignment Restrictions: Encountered MassAssignmentException when inserting mock facility records via Tinker.

## 💡 Solutions
Switched to SQLite: Migrated the database environment to SQLite (database/database.sqlite) to bypass complex local server configuration hurdles.

Manual Model Instantiation: Bypassed mass assignment protection during mock data seeding by manually instantiating the Facility model, assigning properties, and calling $save().

## 📈 Future Improvements
Implement Laravel Sanctum for secure token-based API authentication.

Add comprehensive unit and feature testing using PHPUnit.

Integrate an Angular frontend dashboard to consume the REST API