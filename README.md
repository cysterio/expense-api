# 💸 Expense Tracker (Full-Stack Flask Web Application)

A full-stack expense tracking web application built using Flask, SQLAlchemy, Chart.js, and Docker.

This project demonstrates secure authentication, backend analytics processing, data visualization, and containerized deployment.

---

## 🚀 Features

- 🔐 Secure User Authentication (hashed passwords)
- 🧾 Add & Manage Expenses
- 📊 Dynamic Dashboard with Category-wise Spending Visualization
- 💰 Budget Tracking Logic
- 🗂 Session-based UI Authentication
- 🔑 JWT-based API Support
- 🐳 Dockerized Deployment
- 🌍 Cloud Hosted

---

## 🛠 Tech Stack

### Backend
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- SQLite
- Gunicorn

### Frontend
- Jinja2 Templates
- Bootstrap 5
- Chart.js

### DevOps
- Docker
- Git & GitHub

---

## 📊 How It Works

1. Users register and their passwords are securely hashed using Werkzeug.
2. Login verifies hashed passwords and stores user ID in session.
3. Expenses are stored in a SQLite database using SQLAlchemy ORM.
4. Backend aggregates total spending and category-wise totals.
5. Aggregated data is passed into Jinja templates.
6. Chart.js dynamically renders a pie chart on the dashboard.
7. The application is containerized using Docker for consistent deployment.

---

## 🧠 Key Engineering Decisions

- **Password Security**  
  Used `generate_password_hash()` and `check_password_hash()` to avoid storing plain text passwords.

- **Session vs JWT Separation**  
  Session-based authentication is used for UI rendering.  
  JWT-based authentication is implemented for API endpoints.

- **Consistent Response Schema**  
  Ensured backend always returns a consistent dictionary structure to prevent frontend runtime failures.

- **Type Safety**  
  Converted form date strings into Python `datetime.date` objects before saving to SQLite to ensure ORM compatibility.

- **Containerization**  
  Dockerized the application to ensure environment consistency across development and deployment.

---

## 📂 Project Structure
expense-api/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── services.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── register.html
│ │ └── dashboard.html
│
├── run.py
├── requirements.txt
├── Dockerfile
└── README.md

---

## ⚙️ Setup Instructions (Local Development)

### 1️⃣ Clone Repository
git clone <your-repo-url>
cd expense-api

### 2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate # Mac/Linux
.venv\Scripts\activate # Windows

### 3️⃣ Install Dependencies
pip install -r requirements.txt

### 4️⃣ Run Application
Visit: http://localhost:5000

---

## 🐳 Run Using Docker

Build image:
docker build -t expense-api .

Run container: 
docker run -p 8000:5000 expense-api

Visit: http://localhost:8000
---

## 📈 Dashboard Analytics

The dashboard calculates:

- Total Spending
- Remaining Budget
- Highest Spending Category
- Average Spending Per Entry
- Category-wise Spending Breakdown (Pie Chart)

Data aggregation is performed in the backend and visualized using Chart.js.

---

## 🔐 Authentication Flow

1. User registers → password hashed before saving.
2. User logs in → hash verified.
3. Session stores user ID.
4. Protected routes validate session.
5. JWT tokens available for API routes.

---

## 🧪 Example API Endpoint (JWT Protected)

Add expense via API:
POST /add-expense

Requires: 
Authorization: Bearer <JWT_TOKEN>

---

## 📌 Future Improvements

- Monthly trend line chart
- Category filter dropdown
- Expense history table with pagination
- Flash success/error notifications
- PostgreSQL production database
- Flask-Migrate for schema migrations
- Automated testing

---

## 🎯 Learning Outcomes

Through this project, I developed hands-on experience with:

- Full-stack application architecture
- Authentication systems
- ORM-based database management
- Data aggregation and visualization
- Template rendering with Jinja2
- Debugging production-style backend errors
- Docker-based deployment workflows

---

## 👨‍💻 Author

Built as a full-stack backend engineering project to move beyond beginner-level Python development.
