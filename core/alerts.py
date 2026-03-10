# core/alerts.py

def generate_alert(risk_result: dict) -> dict:
    """
    Generates alerts based on system risk level.
    """

    risk_level = risk_result.get("risk_level", "Low")

    if risk_level == "Critical":
        return {
            "alert": True,
            "severity": "Critical",
            "message": "Immediate attention required! System at high risk."
        }

    if risk_level == "High":
        return {
            "alert": True,
            "severity": "High",
            "message": "System instability detected. Investigation recommended."
        }

    return {
        "alert": False,
        "severity": "Normal",
        "message": "System operating within normal parameters."
    }
