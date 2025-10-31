# Django Rest API Project
This is a simple REST API Project that provides simple GET and POST endpoints 

# Setup
1.1. Clone the repository to local folder:
 ```bash
  git clone https://github.com/sweesram/Sample-Project.git
  cd Sample-Project

2. Create and activate a virtual environment:
"python -m venv .venv"   ->create the environment
".venv\Scripts\activate " -> Activate the environment.

3. Install dependencies:
"pip install django djangorestframework"

if any changes use this command
4. Apply database migrations:
"python manage.py migrate"

5. Run the development server:
"python manage.py runserver
"

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

### GET /api/get/
Returns a sample person data.

Response Example:
```json
{
    "name": "swees",
    "age": 13
}
```

### POST /api/post/
Accepts data and returns a welcome message with the posted data.

Request Body:
- Any JSON data

Response Example:
{
    "message": "Welcome to our team",
    "print-data": {
        // Your posted data will appear here
    }
}


**Status Codes:**
- 201: Successfully created
- 400: Bad request
- 405: Method not allowed

## Project Structure

├── api/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── products/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (default database)

