Day 2: Python Development & Management System
Welcome to my Day 2 practical assignment for the 10-Day Intern Technical Training Program. This project focuses on strengthening core Python programming, building an interactive employee management system with persistent storage, and analyzing CSV data.

📁 Project Structure
The day-02 directory is organized as follows:

day-02/
├── python-exercises/        # Foundational Python syntax and practice scripts
├── management-system/       # Employee management tool with CRUD and JSON persistence
├── csv-analysis/            # CSV dataset profiling and analysis script
└── README.md                # Project documentation

🚀 Modules Overview

1. Python Exercises (python-exercises/)
Covers core Python concepts including data types, lists, dictionaries, loops, functions, and exception handling.

Acts as a practice ground for core programming constructs.

2. Employee Management System (management-system/)
An interactive command-line application to manage employee records efficiently.

Features:

Add new employee details.

Update or delete existing records by ID.

Search records quickly by ID or name.

Filter employees by department and sort them by ID or salary.

Compute key statistics like total count, average, minimum, and maximum salary.

Automatic data persistence using a JSON file (employees.json).

Robust exception handling for invalid inputs.

3. CSV Data Analysis (csv-analysis/)
A data profiling tool that reads a CSV file and generates a clean diagnostic summary report.

Metrics Report:

Total record count.

Detection of missing/blank values.

Identification of duplicate rows.

Numerical salary statistics (average, min, max).

Category-wise department distribution counts.

🛠️ How to Run
Navigate to the specific module folder inside day-02/ to run the scripts:

To run the Management System:
PowerShell
cd management-system
python main.py
To run the CSV Analysis Tool:
PowerShell
cd csv-analysis
python analysis.py