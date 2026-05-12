# Maintenance Dispatch System - Backend

A Django REST Framework backend for managing property maintenance requests with role-based access control.

## Tech Stack

- Python 3.13
- Django 6.0
- Django REST Framework
- SQLite (development)
- Session-based Authentication with CSRF protection

## Features

- **Role-based Access Control**: Manager, Staff, and Resident roles
- **Maintenance Requests**: Create, view, update, and delete maintenance requests
- **Staff Assignment**: Managers can assign requests to maintenance staff
- **Status Tracking**: Track request status (Pending → In Progress → Completed)

## Quick Start

### 1. Navigate to Backend Directory

```bash
cd Backend
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000`

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/auth/csrf/` | Get CSRF token |
| POST | `/api/auth/login/` | User login |
| POST | `/api/auth/logout/` | User logout |
| GET | `/api/auth/me/` | Get current user info |
| GET | `/api/auth/staff/` | Get list of staff users (Manager only) |

### Maintenance Requests

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/requests/` | List requests (filtered by role) |
| POST | `/api/requests/` | Create new request (Resident only) |
| GET | `/api/requests/{id}/` | Get request details |
| PATCH | `/api/requests/{id}/` | Update request |
| DELETE | `/api/requests/{id}/` | Delete request (Manager only) |

### Admin Panel

Access Django Admin at: `http://127.0.0.1:8000/admin/`

## Test Users

| Username | Password | Role | Permissions |
|----------|----------|------|-------------|
| `admin` | `admin1234` | Manager | Full access, assign tasks, delete requests |
| `manager1` | `Test1234!` | Manager | Full access, assign tasks, delete requests |
| `staff1` | `Test1234!` | Staff | View assigned tasks, update status |
| `staff2` | `Test1234!` | Staff | View assigned tasks, update status |
| `resident1` | `Test1234!` | Resident | Create requests, view own requests |
| `resident2` | `Test1234!` | Resident | Create requests, view own requests |

## Role Permissions

### Property Manager
- View all maintenance requests
- Assign requests to maintenance staff
- Update request status
- Delete requests

### Maintenance Staff
- View only requests assigned to them
- Update task status (Pending → In Progress → Completed)
- Cannot reassign tasks
- Cannot view other staff's assignments

### Resident
- Create new maintenance requests
- View only their own requests
- Track request status
- Cannot modify or delete requests

## Project Structure

```
Backend/
├── config/                 # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── maintenance/            # Maintenance requests app
│   ├── models.py          # MaintenanceRequest model
│   ├── views.py           # API viewsets
│   ├── serializers.py     # DRF serializers
│   ├── permissions.py     # Custom permission classes
│   └── urls.py
├── users/                  # User authentication app
│   ├── models.py          # Custom User model with roles
│   ├── views.py           # Login, Logout, Me views
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Environment Variables

For production, update these in `settings.py`:

- `SECRET_KEY`: Change to a secure random key
- `DEBUG`: Set to `False`
- `ALLOWED_HOSTS`: Add your domain
- `DATABASES`: Configure PostgreSQL

## License

MIT License
