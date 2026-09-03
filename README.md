# Expense Tracker

A full-stack expense tracking web application built with Flask, SQLAlchemy, and Chart.js. The application provides user authentication, expense management, budget tracking, and category-based spending analytics.

## Features

- User registration and login
- Password hashing using Werkzeug
- Session-based authentication for the web interface
- JWT-based authentication for API endpoints
- Add and manage expenses
- Budget tracking
- Dashboard with spending summaries
- Category-wise spending visualization
- Docker-based deployment

## Technology Stack

### Backend

- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite
- Gunicorn

### Frontend

- Jinja2
- Bootstrap 5
- Chart.js

### Development and Deployment

- Python
- Git
- GitHub
- Docker

## Project Structure

```text
expense-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       └── dashboard.html
├── run.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Application Flow

1. A user registers through the web interface.
2. The password is hashed before being stored in the database.
3. During login, the submitted password is verified against the stored hash.
4. The user's ID is stored in the session after successful authentication.
5. Protected routes verify the session before allowing access.
6. Expenses are stored in the database using SQLAlchemy.
7. The backend calculates spending summaries and category-wise totals.
8. The aggregated data is passed to the dashboard template.
9. Chart.js renders the category-wise spending visualization.

## Authentication

The application uses separate authentication mechanisms for its web interface and API endpoints.

### Session Authentication

Session-based authentication is used for the server-rendered web interface. After a successful login, the user's ID is stored in the session. Protected routes verify the session before processing requests.

### JWT Authentication

JWT-based authentication is implemented for API endpoints. Clients authenticate using a JWT token and include it in the request's `Authorization` header.

```http
Authorization: Bearer <JWT_TOKEN>
```

## Database

The application currently uses SQLite for storing users and expenses. SQLAlchemy is used as the ORM for database operations.

## Dashboard Analytics

The dashboard displays the following information:

- Total spending
- Remaining budget
- Highest spending category
- Average spending per expense
- Category-wise spending breakdown

The backend performs the aggregation, while Chart.js is responsible for rendering the visualization.

## API

### Add Expense

```http
POST /add-expense
```

**Authentication:** JWT required

**Request header:**

```http
Authorization: Bearer <JWT_TOKEN>
```

The endpoint accepts expense data and stores the expense in the database.

> Add the actual request body and response examples here once the endpoint schema is finalized.

## Local Development

### Clone the Repository

```bash
git clone <your-repo-url>
cd expense-api
```

### Create a Virtual Environment

**Mac/Linux**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python run.py
```

The application will be available at:

```text
http://localhost:5000
```

## Docker

### Build the Image

```bash
docker build -t expense-api .
```

### Run the Container

```bash
docker run -p 8000:5000 expense-api
```

The application will be available at:

```text
http://localhost:8000
```

## Project Structure

The application follows a modular Flask structure:

- `__init__.py` — Application initialization and configuration
- `models.py` — Database models
- `routes.py` — Application and API routes
- `services.py` — Business logic and data processing
- `templates/` — Jinja2 templates
- `run.py` — Application entry point

## Future Improvements

- Monthly spending trend visualization
- Category filtering
- Paginated expense history
- Flash notifications
- PostgreSQL support
- Flask-Migrate integration
- Automated testing

