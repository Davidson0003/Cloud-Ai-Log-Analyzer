from flask import Blueprint, render_template, request
import os
from app.analyzer.parser import read_log_file, parse_log_lines

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def dashboard():
    return render_template("dashboard.html")

@main_bp.route("/upload-page")
def upload_page():
    return render_template("upload.html")

@main_bp.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("logfile")
    if not file:
        return "No file uploaded", 400

    upload_folder = "data/sample_logs"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    raw_lines = read_log_file(file_path)
    parsed_logs = parse_log_lines(raw_lines)

    summary = {
        "total_logs": len(parsed_logs),
        "error_count": sum(1 for l in parsed_logs if l["level"] == "ERROR"),
        "warning_count": sum(1 for l in parsed_logs if l["level"] == "WARNING"),
        "info_count": sum(1 for l in parsed_logs if l["level"] == "INFO")
    }

    return render_template("results.html", results=parsed_logs, summary=summary)
app_routes = main_bp