# Royal Car Rental

A group project built with Django and MySQL.  
The goal is to create a platform for managing and renting cars with role-based access (store owners and renters).

---

## Requirements
- Python 3.10+
- Django 4.x
- MySQL
- Bootstrap
- mysqlclient
- Stripe (Handling Payments).

---

## Setup (Quick Start)
1. Create a virtual environment
2. Install requirements
3. Configure the database
4. Run the server

---

## Main Roles
- Renter: Browse and book cars.
- Owner: Add and manage cars, track bookings.
- Admin: Full control over users, cars, and system settings.
  
---

## Key Features
- Clean, responsive design (works on all devices).
- Role‑based dashboards (each role sees its own tools).
- Secure role‑based access and permissions.
- Booking and payment tracking.
- Notifications and alerts for quick feedback.

---

## Getting Started
```bash
# Clone the repository
git clone https://github.com/MohDDH/Royal-Car-Rental.git

# Go to the project folder
cd Royal-Car-Rental

# Create and activate a virtual environment
python -m venv venv

# On Linux/Mac
source venv/bin/activate

# On Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Run the server
python manage.py runserver

```

