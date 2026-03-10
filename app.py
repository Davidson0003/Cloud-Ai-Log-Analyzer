from flask import Flask, request, jsonify, render_template, send_from_directory
import os

from core.upload import allowed_file
from core.parser import parse_logs
from core.validation import validate_logs
from core.features import extract_features
from core.anomaly import detect_anomaly
from core.risk import calculate_risk
from core.explain import generate_explanation
from core.metrics import aggregate_metrics
from core.timeseries import analyze_time_series
from core.alerts import generate_alert
from core.dashboard import prepare_dashboard_response
from core.system_logger import log_event
from core.report import export_report
from core.ingestion import read_log_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")


@app.route("/charts")
def charts():
    return render_template("charts.html")


@app.route("/analyze", methods=["POST"])
def analyze_logs():

    file = request.files.get("logfile")

    if not file or not allowed_file(file.filename):
        return jsonify({"error": "Invalid file"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    raw_lines = read_log_file(filepath)

    parsed = parse_logs(raw_lines)
    valid = validate_logs(parsed)

    features = extract_features(valid)

    anomaly = detect_anomaly(features)
    risk = calculate_risk(anomaly)

    explanation = generate_explanation(features, anomaly, risk)

    metrics = aggregate_metrics(features, anomaly, risk)

    time_analysis = analyze_time_series(features.get("hourly_activity", {}))

    alert = generate_alert(risk)

    dashboard_data = prepare_dashboard_response(
        metrics,
        explanation,
        time_analysis,
        alert
    )

    report_path = export_report(dashboard_data)

    dashboard_data["report_path"] = report_path

    return jsonify(dashboard_data)


@app.route("/reports/<path:filename>")
def download_report(filename):
    return send_from_directory("reports", filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)