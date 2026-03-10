from flask import Blueprint, request, jsonify

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "Dashboard routes working"})
