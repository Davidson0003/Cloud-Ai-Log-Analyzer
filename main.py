from flask import Flask, render_template, request
from app.analyzer.parser import read_log_file, parse_log_lines
import os

# ===== Flask App =====
app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

# ===== Routes =====
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/upload-page")
def upload_page():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    # Get uploaded file
    file = request.files.get("logfile")
    if not file:
        return "No file uploaded", 400

    # Ensure upload folder exists
    upload_folder = os.path.join("app", "data", "sample_logs")
    os.makedirs(upload_folder, exist_ok=True)

    # Save uploaded file
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    # Read and parse logs
    raw_lines = read_log_file(file_path)
    parsed_logs = parse_log_lines(raw_lines)

    # Detect errors
    anomalies = [l for l in parsed_logs if l.get("level") == "ERROR"]

    # Prepare summary
    summary = {
        "total_logs": len(parsed_logs),
        "error_count": sum(1 for l in parsed_logs if l.get("level") == "ERROR"),
        "warning_count": sum(1 for l in parsed_logs if l.get("level") == "WARNING"),
        "info_count": sum(1 for l in parsed_logs if l.get("level") == "INFO")
    }

    return render_template(
        "results.html",
        results=parsed_logs,
        summary=summary,
        filename=file.filename,
        issues=[a.get("message") for a in anomalies]
    )


@app.route("/error-report")
def error_report():
    # Dummy data for testing
    anomalies = [
        {"timestamp": "2025-01-01 10:22:01", "message": "Disk failure detected"},
        {"timestamp": "2025-01-01 10:24:10", "message": "Unauthorized access attempt"}
    ]
    return render_template("error_report.html", anomalies=anomalies)


# ===== Run App =====
if __name__ == "__main__":
    # Make sure to run from project root:
    # python -m app.routes
    app.run(debug=True)
