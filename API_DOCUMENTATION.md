# Logistics REST API Documentation

A Flask-based REST API for managing logistics operations including drivers, vehicles, routes, and packages.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Base URL](#base-url)
- [Database Schema](#database-schema)
- [Endpoints](#endpoints)
  - [Health Check](#health-check)
  - [Drivers](#drivers)
  - [Vehicles](#vehicles)
  - [Routes](#routes)
  - [Packages](#packages)
- [Response Format](#response-format)
- [Error Handling](#error-handling)

---

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL database

### Installation

1. Clone the repository and navigate to the project folder.

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```env
   DB_HOST=your_db_host
   DB_PORT=5432
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_SSLMODE=require
   ```

5. Run the server:
   ```bash
   python app.py
   ```

The server starts on `http://127.0.0.1:5000` by default. On startup, it automatically creates the required database tables if they don't exist.

---

## Base URL

```
http://127.0.0.1:5000
```

---

## Database Schema

The API uses a PostgreSQL database with the following tables under the `logistics` schema:

| Table     | Primary Key    | Fields                                                                 |
|-----------|----------------|------------------------------------------------------------------------|
| `driver`  | `driver_id`    | `name` (varchar), `license_type` (varchar)                             |
| `vehicle` | `vehicle_id`   | `license_plate` (varchar), `model` (varchar), `driver_id` (FK)        |
| `route`   | `route_id`     | `service_zone` (varchar), `order_date` (timestamp), `driver_id` (FK)  |
| `package` | `package_id`   | `description` (varchar), `weight` (numeric), `route_id` (FK), `driver_id` (FK) |

---

## Endpoints

### Health Check

#### `GET /`

Confirms the server is running.

**Response**
```json
{
  "message": "Server Online"
}
```

---

### Drivers

Base path: `/driver`

#### `GET /driver/`

Returns a list of all drivers.

**Response `200 OK`**
```json
[
  {
    "driver_id": 1,
    "name": "John Doe",
    "license_type": "Class A"
  }
]
```

---

#### `POST /driver/`

Creates a new driver.

**Request Body**
```json
{
  "name": "John Doe",
  "license_type": "Class A"
}
```

| Field          | Type   | Required | Description                        |
|----------------|--------|----------|------------------------------------|
| `name`         | string | Yes      | Full name of the driver            |
| `license_type` | string | Yes      | Driver's license classification    |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

#### `PUT /driver/<id>`

Updates an existing driver by ID.

**URL Parameter**

| Parameter | Type    | Description       |
|-----------|---------|-------------------|
| `id`      | integer | The driver's ID   |

**Request Body**
```json
{
  "name": "Jane Doe",
  "license_type": "Class B"
}
```

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

#### `DELETE /driver/<id>`

Deletes a driver by ID.

**URL Parameter**

| Parameter | Type    | Description       |
|-----------|---------|-------------------|
| `id`      | integer | The driver's ID   |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

### Vehicles

Base path: `/vehicle`

#### `GET /vehicle/`

Returns a list of all vehicles.

**Response `200 OK`**
```json
[
  {
    "vehicle_id": 1,
    "model": "Ford Transit",
    "license_plate": "ABC-1234",
    "driver_id": 2
  }
]
```

---

#### `POST /vehicle/`

Creates a new vehicle.

**Request Body**
```json
{
  "model": "Ford Transit",
  "license_plate": "ABC-1234"
}
```

| Field           | Type   | Required | Description                  |
|-----------------|--------|----------|------------------------------|
| `model`         | string | Yes      | Vehicle model name           |
| `license_plate` | string | Yes      | Vehicle license plate number |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

#### `PUT /vehicle/<id>`

Updates an existing vehicle by ID.

**URL Parameter**

| Parameter | Type    | Description        |
|-----------|---------|--------------------|
| `id`      | integer | The vehicle's ID   |

**Request Body**
```json
{
  "model": "Mercedes Sprinter",
  "license_plate": "XYZ-5678",
  "driver_id": 1
}
```

| Field           | Type    | Required | Description                        |
|-----------------|---------|----------|------------------------------------|
| `model`         | string  | Yes      | Vehicle model name                 |
| `license_plate` | string  | Yes      | Vehicle license plate number       |
| `driver_id`     | integer | Yes      | ID of the assigned driver          |

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

#### `DELETE /vehicle/<id>`

Deletes a vehicle by ID.

**URL Parameter**

| Parameter | Type    | Description        |
|-----------|---------|--------------------|
| `id`      | integer | The vehicle's ID   |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

### Routes

Base path: `/route`

#### `GET /route/`

Returns a list of all routes.

**Response `200 OK`**
```json
[
  {
    "route_id": 1,
    "service_zone": "Zone A",
    "order_date": "2026-05-12T08:00:00",
    "driver_id": 1
  }
]
```

---

#### `POST /route/`

Creates a new route.

**Request Body**
```json
{
  "service_zone": "Zone A",
  "order_date": "2026-05-12T08:00:00"
}
```

| Field          | Type      | Required | Description                              |
|----------------|-----------|----------|------------------------------------------|
| `service_zone` | string    | Yes      | The zone or area the route covers        |
| `order_date`   | timestamp | Yes      | Date and time the route was ordered (ISO 8601) |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

#### `PUT /route/<id>`

Updates an existing route by ID.

**URL Parameter**

| Parameter | Type    | Description      |
|-----------|---------|------------------|
| `id`      | integer | The route's ID   |

**Request Body**
```json
{
  "service_zone": "Zone B",
  "order_date": "2026-05-13T09:00:00",
  "driver_id": 1
}
```

| Field          | Type      | Required | Description                              |
|----------------|-----------|----------|------------------------------------------|
| `service_zone` | string    | Yes      | The zone or area the route covers        |
| `order_date`   | timestamp | Yes      | Date and time of the route (ISO 8601)    |
| `driver_id`    | integer   | Yes      | ID of the assigned driver                |

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

#### `DELETE /route/<id>`

Deletes a route by ID.

**URL Parameter**

| Parameter | Type    | Description      |
|-----------|---------|------------------|
| `id`      | integer | The route's ID   |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

### Packages

Base path: `/package`

#### `GET /package/`

Returns a list of all packages.

**Response `200 OK`**
```json
[
  {
    "package_id": 1,
    "description": "Fragile electronics",
    "weight": 2.5,
    "route_id": 1,
    "driver_id": 1
  }
]
```

---

#### `POST /package/`

Creates a new package.

**Request Body**
```json
{
  "description": "Fragile electronics",
  "weight": 2.5
}
```

| Field         | Type    | Required | Description                        |
|---------------|---------|----------|------------------------------------|
| `description` | string  | Yes      | Description of the package content |
| `weight`      | numeric | Yes      | Weight of the package (in kg)      |

**Response `201 Created`**
```json
{
  "message": "Object Created"
}
```

---

#### `PUT /package/<id>`

Updates an existing package by ID.

**URL Parameter**

| Parameter | Type    | Description        |
|-----------|---------|--------------------|
| `id`      | integer | The package's ID   |

**Request Body**
```json
{
  "description": "Heavy machinery parts",
  "weight": 15.0,
  "route_id": 2,
  "driver_id": 1
}
```

| Field         | Type    | Required | Description                        |
|---------------|---------|----------|------------------------------------|
| `description` | string  | Yes      | Description of the package content |
| `weight`      | numeric | Yes      | Weight of the package (in kg)      |
| `route_id`    | integer | Yes      | ID of the assigned route           |
| `driver_id`   | integer | Yes      | ID of the assigned driver          |

**Response `201`**
```json
{
  "message": "Object Updated"
}
```

---

#### `DELETE /package/<id>`

Deletes a package by ID.

**URL Parameter**

| Parameter | Type    | Description        |
|-----------|---------|--------------------|
| `id`      | integer | The package's ID   |

**Response `201`**
```json
{
  "message": "Object Deleted"
}
```

---

## Response Format

All responses are JSON. Successful list responses return an array of objects. Write operations return a message object.

```json
{ "message": "Object Created" }
{ "message": "Object Updated" }
{ "message": "Object Deleted" }
```

---

## Error Handling

All endpoints return a `500` status code with a descriptive message if an unexpected server or database error occurs.

```json
{
  "message": "An unexpected error occurred: <error details>"
}
```

Common causes:
- Missing required fields in the request body
- Invalid foreign key references (e.g., referencing a `driver_id` that doesn't exist)
- Database connectivity issues
