from flask import Flask, render_template, request
from app.analyzer.parser import read_log_file, parse_log_lines
import os

app = Flask(__name__, template_folder="app/templates", static_folder="static")

@app.route("/")
def home():
    return render_template("dashboard.html")

@app.route("/upload-page")
def upload_page():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["logfile"]

    upload_folder = "data/sample_logs"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)

    raw_lines = read_log_file(file_path)
    parsed_logs = parse_log_lines(raw_lines)

    # summary counts
    summary = {
        "total_logs": len(parsed_logs),
        "error_count": sum(1 for l in parsed_logs if l["level"] == "ERROR"),
        "warning_count": sum(1 for l in parsed_logs if l["level"] == "WARNING"),
        "info_count": sum(1 for l in parsed_logs if l["level"] == "INFO")
    }

    return render_template(
        "results.html",
        results=parsed_logs,
        summary=summary
    )
from app import create_app
app = create_app()
if __name__ == "__main__":
    app.run(debug=True)
