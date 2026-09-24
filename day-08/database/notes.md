# Database Design & Architecture Notes (Day 8)

## 🏗️ Overview
This document outlines the relational database architecture designed for the municipal/facility management system. It establishes structured relationships using Primary and Foreign keys to maintain data integrity.

## 🔗 Table Relationships & Schema Mapping

1. **Departments & Employees (1-to-Many Relationship)**
   - A department can have multiple employees.
   - An employee belongs to only one department.
   - **Foreign Key:** `employees.department_id` references `departments(id)`.

2. **Users & Inspections / Complaints (1-to-Many Relationship)**
   - A user (staff/inspector) can conduct multiple inspections or raise multiple complaints.
   - **Foreign Keys:** 
     - `inspections.inspector_id` references `users(id)`.
     - `complaints.user_id` references `users(id)`.

3. **Facilities & Inspections / Complaints (1-to-Many Relationship)**
   - A facility can undergo multiple inspections and have multiple complaints registered against it.
   - **Foreign Keys:**
     - `inspections.facility_id` references `facilities(id)`.
     - `complaints.facility_id` references `facilities(id)`.

## ⚙️ Key Database Concepts Used
- **Primary Keys (`PRIMARY KEY`):** Ensures every row in a table is uniquely identified (e.g., `id`).
- **Foreign Keys (`FOREIGN KEY`):** Enforces referential integrity between related tables, preventing orphan records using `ON DELETE CASCADE` or `ON DELETE SET NULL`.
- **Aggregation & Joins:** Used SQL functions like `AVG()`, `COUNT()`, `GROUP BY`, and `JOIN` to query complex relational data efficiently.