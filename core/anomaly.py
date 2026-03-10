# core/anomaly.py

def detect_anomaly(features: dict) -> dict:
    """
    Detects anomalies based on rule-based thresholds.
    """

    anomalies = []
    is_anomaly = False

    total_logs = features.get("total_logs", 0)
    error_count = features.get("error_count", 0)
    warning_count = features.get("warning_count", 0)

    # Rule 1: High error rate
    if total_logs > 0:
        error_rate = error_count / total_logs
        if error_rate > 0.2:  # 20% threshold
            is_anomaly = True
            anomalies.append("High error rate detected")

    # Rule 2: Excessive warnings
    if warning_count > 50:
        is_anomaly = True
        anomalies.append("Unusual number of warnings")

    return {
        "is_anomaly": is_anomaly,
        "reasons": anomalies
    }
