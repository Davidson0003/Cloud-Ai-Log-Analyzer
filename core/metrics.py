# core/metrics.py

def aggregate_metrics(features: dict, anomaly_result: dict, risk_result: dict) -> dict:
    """
    Aggregates overall system metrics for dashboard display.
    """

    return {
        "total_logs": features.get("total_logs", 0),
        "errors": features.get("error_count", 0),
        "warnings": features.get("warning_count", 0),
        "info": features.get("info_count", 0),
        "is_anomaly": anomaly_result.get("is_anomaly", False),
        "risk_score": risk_result.get("risk_score", 0),
        "risk_level": risk_result.get("risk_level", "Low")
    }
