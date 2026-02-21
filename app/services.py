from datetime import datetime
from sqlalchemy import func
from .models import Expense
from . import db

MONTHLY_BUDGET = 5000

ALLOWED_CATEGORIES = {
    "Food",
    "Transport",
    "Shopping",
    "Entertainment",
    "Subscriptions"
}


# ---------------------------
# Dashboard (User Scoped)
# ---------------------------
def get_dashboard_data(user_id, category=None, start=None, end=None):
    query = Expense.query.filter(Expense.user_id == user_id)

    if category:
        query = query.filter(Expense.category == category)

    if start:
        try:
            start_date = datetime.strptime(start, "%Y-%m-%d").date()
            query = query.filter(Expense.date >= start_date)
        except ValueError:
            return {"error": "Invalid start date format (YYYY-MM-DD)"}, 400

    if end:
        try:
            end_date = datetime.strptime(end, "%Y-%m-%d").date()
            query = query.filter(Expense.date <= end_date)
        except ValueError:
            return {"error": "Invalid end date format (YYYY-MM-DD)"}, 400

    expenses = query.all()

    if not expenses:
        return {
        "total_spent": 0,
        "budget_remaining": MONTHLY_BUDGET,
        "highest_spend_category": "None",
        "highest_category_amount": 0,
        "average_spend_per_entry": 0,
        "category_totals": {}
    }, 200

    total_spent = sum(e.amount for e in expenses)

    category_totals = {}
    for e in expenses:
        category_totals[e.category] = category_totals.get(e.category, 0) + e.amount

    highest_category = max(category_totals, key=category_totals.get)

    avg_daily = total_spent / len(expenses)

    return {
    "total_spent": round(total_spent, 2),
    "budget_remaining": round(MONTHLY_BUDGET - total_spent, 2),
    "highest_spend_category": highest_category,
    "highest_category_amount": round(category_totals[highest_category], 2),
    "average_spend_per_entry": round(avg_daily, 2),
    "category_totals": category_totals,  
    "filters_applied": {
        "category": category,
        "start": start,
        "end": end
    }
}, 200

# ---------------------------
# Add Expense (User Scoped)
# ---------------------------
def add_expense(data, user_id):
    required_fields = {"date", "category", "amount", "payment_mode"}

    if not required_fields.issubset(data.keys()):
        return {"error": "Missing required fields"}, 400

    # Validate date
    try:
        date_obj = datetime.strptime(data["date"], "%Y-%m-%d").date()
    except ValueError:
        return {"error": "Invalid date format. Use YYYY-MM-DD"}, 400

    # Validate amount
    try:
        amount = float(data["amount"])
        if amount <= 0:
            return {"error": "Amount must be positive"}, 400
    except ValueError:
        return {"error": "Amount must be a number"}, 400

    # Validate category
    if data["category"] not in ALLOWED_CATEGORIES:
        return {"error": f"Category must be one of {ALLOWED_CATEGORIES}"}, 400

    expense = Expense(
        date=date_obj,
        category=data["category"],
        amount=amount,
        payment_mode=data["payment_mode"],
        user_id=user_id
    )

    db.session.add(expense)
    db.session.commit()

    return {"message": "Expense added successfully"}, 201