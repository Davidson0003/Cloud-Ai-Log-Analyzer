# core/risk.py

def calculate_risk(anomaly_result: dict) -> dict:
    """
    Calculates risk score based on anomaly severity.
    """

    risk_score = 0
    risk_level = "Low"

    reasons = anomaly_result.get("reasons", [])

    if not anomaly_result.get("is_anomaly"):
        risk_score = 10
        risk_level = "Low"

    else:
        risk_score = 40 + (len(reasons) * 20)

        if risk_score >= 80:
            risk_level = "Critical"
        elif risk_score >= 60:
            risk_level = "High"
        else:
            risk_level = "Medium"

    return {
        "risk_score": min(risk_score, 100),
        "risk_level": risk_level
    }
