# core/dashboard.py

def prepare_dashboard_response(metrics, explanation, time_analysis, alert):
    """
    Prepares structured dashboard response.
    """

    return {
        "summary": {
            "risk_level": metrics.get("risk_level"),
            "risk_score": metrics.get("risk_score"),
            "is_anomaly": metrics.get("is_anomaly")
        },
        "stats": {
            "total_logs": metrics.get("total_logs"),
            "errors": metrics.get("errors"),
            "warnings": metrics.get("warnings"),
            "info": metrics.get("info")
        },
        "time_analysis": time_analysis,
        "alert": alert,
        "explanation": explanation
    }
