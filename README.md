# Ticket Booking Automation System

A RESTful ticket booking API built with Python, Flask, and SQLite.

The application provides booking management functionality through API endpoints, allowing users to create bookings, retrieve booking information, and update booking statuses.

## Features

* Create new bookings
* Retrieve all bookings
* Retrieve booking details by ID
* Update booking status
* SQLite database integration
* JSON-based API responses

## Technology Stack

* Python
* Flask
* SQLite
* REST API
* Thunder Client

## API Endpoints

### Get All Bookings

```http
GET /bookings
```

### Get Booking By ID

```http
GET /bookings/<id>
```

### Create Booking

```http
POST /bookings
```

Example request:

```json
{
  "passenger_name": "John Doe",
  "departure_city": "Tbilisi",
  "destination_city": "Batumi",
  "travel_date": "2026-07-01",
  "seat_number": "B15",
  "ticket_price": 75
}
```

### Update Booking Status

```http
PUT /bookings/<id>
```

Example request:

```json
{
  "status": "cancelled"
}
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

The server runs locally at:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
ticket-booking-automation/
│
├── app.py
├── database.py
├── bookings.db
├── requirements.txt
└── README.md
```


