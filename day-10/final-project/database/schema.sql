-- Smart Hygiene Risk Prediction System Database Schema
CREATE TABLE IF NOT EXISTS facilities (
    facility_id VARCHAR(50) PRIMARY KEY,
    location VARCHAR(100),
    facility_type VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS hygiene_inspections (
    inspection_id INT AUTO_INCREMENT PRIMARY KEY,
    facility_id VARCHAR(50),
    cleanliness_score FLOAT,
    odor_score FLOAT,
    waste_level FLOAT,
    water_availability VARCHAR(10),
    footfall INT,
    complaints INT,
    hours_since_cleaning FLOAT,
    hygiene_risk VARCHAR(20),
    inspection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (facility_id) REFERENCES facilities(facility_id)
);