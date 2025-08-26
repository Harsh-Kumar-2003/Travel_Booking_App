# Travel Booking Application

A Django-based web application for booking travel options (flights, trains, buses) with user authentication and booking management.

## 🌟 Features

- **User Authentication**: Registration, login, logout with Django's built-in auth system
- **Travel Options**: Browse available flights, trains, and buses
- **Advanced Filtering**: Filter by type, source, destination, and date
- **Booking System**: Book travel options with seat selection and price calculation
- **Booking Management**: View all bookings and cancel confirmed ones
- **Responsive Design**: Mobile-friendly interface using Bootstrap 5
- **MySQL Database**: Production-ready database setup
- **Admin Panel**: Full CRUD operations for administrators

## 🛠️ Tech Stack

- **Backend**: Django 5.0+ (Python)
- **Frontend**: Django Templates, Bootstrap 5
- **Database**: MySQL
- **Authentication**: Django Auth System
- **Deployment**: PythonAnywhere ready

## 📦 Installation & Local Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Step-by-Step Setup


1. **Clone the repository**
    ```bash
    git clone <your-repository-url>
    cd travel-booking-app


2. **Create and activate virtual environment**

    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python -m venv venv
    source venv/bin/activate


3. **Install dependencies**

    ```bash
    pip install django mysqlclient


4. **Set up MySQL database**

    ```sql
    mysql -u root -p
    CREATE DATABASE travel_booking_db;
    EXIT;


5. **Configure database settings**
    Edit travel_booking/settings.py:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'travel_booking_db',
            'USER': 'root',
            'PASSWORD': 'your_mysql_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }


6. **Run migrations**

    ```bash
    python manage.py migrate


7. **Create superuser (for admin access)**

    ```bash
    python manage.py createsuperuser


8. **Start development server**

    ```bash
    python manage.py runserver


9. **Access the application**

    Main application: http://localhost:8000

    Admin panel: http://localhost:8000/admin


## 📋 Usage Guide

    For Users


    Register/Login: Create an account or login with existing credentials

    Browse Travel: View all available travel options on the Travel page

    Filter Options: Use filters to find specific travel options

    Book Travel: Click "Book Now" on any option, select seats, and confirm

    Manage Bookings: View all bookings in "My Bookings" section

    Cancel Bookings: Cancel confirmed bookings if needed



    For Administrators


    Access Admin Panel: Login at /admin with superuser credentials

    Manage Travel Options: Add, edit, or delete travel options

    Manage Bookings: View and manage all user bookings

    User Management: Manage user accounts and permissions



## 🗂️ Project Structure

    travel-booking-app/
    ├── bookings/                 # Main application
    │   ├── migrations/          # Database migrations
    │   ├── templates/           # HTML templates
    │   │   ├── bookings/        # App-specific templates
    │   │   └── registration/    # Auth templates
    │   ├── __init__.py
    │   ├── admin.py            # Admin panel configuration
    │   ├── apps.py
    │   ├── forms.py            # Booking form
    │   ├── models.py           # Database models
    │   ├── tests.py            # Unit tests
    │   ├── urls.py             # App URL routes
    │   └── views.py            # Application logic
    ├── travel_booking/          # Project settings
    │   ├── __init__.py
    │   ├── settings.py         # Project configuration
    │   ├── urls.py             # Main URL routes
    │   └── wsgi.py
    ├── venv/                   # Virtual environment (ignored in git)
    ├── .gitignore             # Git ignore rules
    ├── manage.py              # Django management script
    ├── requirements.txt       # Python dependencies
    └── README.md              # This file



## 🚀 Deployment

    PythonAnywhere Deployment
    Create account on PythonAnywhere

    Upload code via GitHub integration or manual upload

    Create virtual environment:

    bash
    mkvirtualenv --python=/usr/bin/python3.8 venv
    Install dependencies:

    bash
    pip install django mysqlclient
    Set up MySQL in PythonAnywhere dashboard

    Update settings.py with production database credentials

    Run migrations:

    bash
    python manage.py migrate
    Collect static files:

    bash
    python manage.py collectstatic
    Reload web app from PythonAnywhere dashboard

    Environment Variables (Production)
    For production, set these in your deployment environment:

    DEBUG=False

    SECRET_KEY=your-production-secret-key

    Database credentials

    ALLOWED_HOSTS=your-domain.com



## 🧪 Testing
    Run the test suite:

    bash
    python manage.py test



    📝 API Endpoints
    Endpoint	Method	Description
    /	GET	Home page
    /accounts/login/	GET/POST	User login
    /accounts/signup/	GET/POST	User registration
    /accounts/logout/	POST	User logout
    /travel/	GET	Browse travel options
    /book/<travel_id>/	GET/POST	Book travel option
    /my-bookings/	GET	View user bookings
    /cancel-booking/<booking_id>/	POST	Cancel booking


## 🤝 Contributing
    Fork the repository

    Create a feature branch (git checkout -b feature/amazing-feature)

    Commit changes (git commit -m 'Add amazing feature')

    Push to branch (git push origin feature/amazing-feature)

    Open a Pull Request



## 📄 License
    This project is licensed under the MIT License.

## 👥 Author
    Harsh Kumar