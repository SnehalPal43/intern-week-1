# API Integration - Facility Inspection Dashboard

This folder documents the REST API integration between the Angular frontend and the Laravel backend for Day 9.

## Backend Base URL
- **Local API Endpoint:** `http://127.0.0.1:8000/api`

## API Endpoints & Routes

### 1. Get All Facilities
- **URL:** `/facilities`
- **Method:** `GET`
- **Description:** Fetches the list of all facilities including their status and location for the dashboard list, search, and filtering.

### 2. Get Single Facility Details
- **URL:** `/facilities/{id}`
- **Method:** `GET`
- **Description:** Retrieves specific details of a selected facility for the inspection form view.

### 3. Store Facility Inspection
- **URL:** `/inspections` (or facility-specific inspection route)
- **Method:** `POST`
- **Description:** Submits new inspection notes and history data from the Angular inspection form to the database.

## Frontend Consumption
- The Angular application utilizes **`HttpClient`** inside **`FacilityService`** to communicate with these Laravel endpoints asynchronously, using TypeScript interfaces for type safety.