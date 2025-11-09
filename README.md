# Django REST API Project

This is a Django REST API project that provides simple GET and POST endpoints for data handling.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sweesram/Sample-Project.git
cd Sample-Project
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install django djangorestframework
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

### GET /api/get/
Returns a sample person data.

**Response Example:**
```json
{
    "name": "swees",
    "age": 13
}
```

### POST /api/post/
Accepts data and returns a welcome message with the posted data.

**Request Body:**
- Any JSON data

**Response Example:**
```json
{
    "message": "Welcome to our team",
    "print-data": {
        // Your posted data will appear here
    }
}
```

**Status Codes:**
- 201: Successfully created
- 400: Bad request
- 405: Method not allowed

## Project Structure

```
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
```

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite (default database)

## Development

To contribute to this project:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a Pull Request