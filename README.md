
Flight Search & Reservation System API

A robust, RESTful backend service built with Django REST Framework (DRF) for searching flights, and handling ticket reservations.

Features

• User Authentication: Token/JWT-based registration, login, logout, and profile management.
• Flight Search & Filtering: Search flights by origin (source), destination (destination), and departure date.
• Flight Management: CRUD operations for administrators to manage flights, aircraft, and schedules.
• Seat & Ticket Reservation: Book single or round-trip tickets with automatic seat validation.
• Booking Management: Users can view their booking history, check reservation status (Confirmed / Cancelled), and cancel active bookings.
• API Documentation: Built-in endpoints and browsable DRF API interface.

Tech Stack

• Language: Python 3.13+
• Framework: Django REST Framework (DRF)
• Database: MySQL / SQLite (default for development)
• Authentication: djangorestframework-simplejwt

Prerequisites

• Python 3.10 or higher
• pip and virtualenv

Installation & Setup

1. Clone the repository:bash
git clone https://github.com/JamesEdwards84/flight-reservation-backend.git
cd flight-reservation-backend
Use code with caution.
2. Create and activate a virtual environment:bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Use code with caution.
3. Install dependencies:bash
pip install -r requirements.txt
Use code with caution.
4. Apply database migrations:bash
python manage.py makemigrations
python manage.py migrate
Use code with caution.
5. Create a superuser (for admin access):bash
python manage.py createsuperuser
Use code with caution.
6. Run the development server:bash
python manage.py runserver
Use code with caution.
The API will be available at http://127.0.0.1:8000

API Endpoints

Authentication (/api/auth/)

• POST /api-auth-token/ — Obtain JWT access and login tokens

Flights (/flightServices/flights/)
• GET /flightServices/flights/ — List all flights
• GET /flightServices/flights/<int:pk>/ — Get details of a specific flight
• POST /flightServices/flights/ — Create a new flight (Admin only)
• DELETE /flightServices/flights/ — Delete a flight (Admin only)
• GET /flightServices/findFlights/ — Search flights by origin (source), destination (destination), and departure date.

Passengers (/flightServices/passengers/)
• GET /flightServices/passengers/ — List all passenger details
• GET /flightServices/reservations/<int:pk>/ — Get details of a specific passenger
• POST /flightServices/passengers/ — Create a new passenger
• DELETE /flightServices/passengers/ — Delete a passenger (Admin only)

Reservation (/flightServices/reservations/)
• GET /flightServices/reservations/ — List all reservation details
• GET /flightServices/reservations/<int:pk>/ — Get details of a specific reservation
• POST /flightServices/reservations/ — Create a new reservation
• DELETE /flightServices/reservations/ — Delete a reservation (Admin only)
• GET /flightServices/saveReservation/ — Save flight reservation details


Contributing

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
