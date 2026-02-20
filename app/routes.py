from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .services import get_dashboard_data, add_expense

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({"message": "Expense API Running"})


# ---------------------------
# Protected Dashboard
# ---------------------------
@main.route("/dashboard")
@jwt_required()
def dashboard():
    user_id = get_jwt_identity()

    category = request.args.get("category")
    start = request.args.get("start")
    end = request.args.get("end")

    response, status = get_dashboard_data(user_id, category, start, end)
    return jsonify(response), status


# ---------------------------
# Protected Add Expense
# ---------------------------
@main.route("/add-expense", methods=["POST"])
@jwt_required()
def add_expense_route():
    user_id = int(get_jwt_identity())
    data = request.json

    response, status = add_expense(data, user_id)