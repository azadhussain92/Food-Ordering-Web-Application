# Full Stack Food Ordering Web Application

A full-stack food ordering web application built using Python, Django, SQL, HTML, CSS, Bootstrap, and JavaScript. The application provides food ordering functionality with customer and vendor management features.

## Features

- User registration and login
- Vendor registration and admin approval
- Restaurant and food item management
- Food menu display and category management
- Shopping cart management
- Order placement and order management
- Vendor dashboard and profile management
- Customer profile management
- Session-based cart functionality

## Tech Stack

- **Backend:** Python, Django
- **Database:**  SQL
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Authentication:** Django Authentication
- **Forms:** Django Forms
- 
- ## Food Ordering System Workflow
### User Workflow
```text
REGISTER / LOGIN
       ↓
USER DASHBOARD
       ↓
VIEW RESTAURANTS
       ↓
SELECT FOOD → ADD TO CART
       ↓
PLACE ORDER
       ↓
ORDER CONFIRMATION
       ↓
TRACK ORDER STATUS
```

### Vendor Workflow
```text
VENDOR REGISTER / LOGIN
          ↓
   ADMIN APPROVAL
          ↓
    VENDOR DASHBOARD
          ↓
      MANAGE MENU
          ↓
     RECEIVE ORDERS
          ↓
    ACCEPT / REJECT
          ↓
   UPDATE ORDER STATUS
```

### Admin Workflow
```text
ADMIN LOGIN
     ↓
ADMIN DASHBOARD
     ↓
MANAGE USERS
     ↓
APPROVE VENDORS
     ↓
MONITOR ORDERS
```

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Configure database settings and environment variables if required.
5. Run migrations using `python manage.py migrate`.
6. Create a superuser using `python manage.py createsuperuser`.
7. Start the development server using `python manage.py runserver`.
8. Open `http://127.0.0.1:8000/` in your browser.

## Note

This project was developed for learning and demonstrating full-stack web development using Django. Features such as payment integration should be described as implemented only if they are available in the application.
