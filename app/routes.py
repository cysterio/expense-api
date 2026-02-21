from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from .models import User, Expense
from . import db
from .services import get_dashboard_data
from werkzeug.security import generate_password_hash, check_password_hash

main = Blueprint("main", __name__)

# Home
@main.route("/")
def home():
    return "Expense Tracker Running"

# Register
@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            return "Username and password required"

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "User already exists"

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password_hash=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("main.login"))

    return render_template("register.html")


# Login
@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password_hash, password):
            return "Invalid credentials"

        access_token = create_access_token(identity=str(user.id))
        session["token"] = access_token
        session["user_id"] = user.id

        return redirect(url_for("main.dashboard"))

    return render_template("login.html")


# Dashboard
@main.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("main.login"))

    user_id = session["user_id"]

    data, status = get_dashboard_data(user_id)

    if status != 200:
        return data, status

    print("DASHBOARD DATA:", data)
    return render_template("dashboard.html", data=data)

# Add expense from form
@main.route("/add-expense-form", methods=["POST"])
def add_expense_form():
    if "user_id" not in session:
        return redirect(url_for("main.login"))

    from datetime import datetime

    date_str = request.form.get("date")
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d").date()

    new_expense = Expense(
        date=parsed_date,
        category=request.form.get("category"),
        amount=float(request.form.get("amount")),
        payment_mode=request.form.get("payment_mode"),
        user_id=session["user_id"]
    )

    db.session.add(new_expense)
    db.session.commit()

    return redirect(url_for("main.dashboard"))


# Logout
@main.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.login"))