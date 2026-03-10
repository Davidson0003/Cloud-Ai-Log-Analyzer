# core/explain.py

def generate_explanation(features: dict, anomaly_result: dict, risk_result: dict) -> str:
    """
    Generates human-readable explanation for detected anomalies and risks.
    """

    if not anomaly_result.get("is_anomaly"):
        return "System behavior is normal. No significant anomalies detected."

    explanations = []

    total_logs = features.get("total_logs", 0)
    error_count = features.get("error_count", 0)
    warning_count = features.get("warning_count", 0)

    if total_logs > 0:
        error_rate = (error_count / total_logs) * 100
        if error_rate > 20:
            explanations.append(
                f"High error rate observed ({error_rate:.2f}% of total logs)."
            )

    if warning_count > 50:
        explanations.append(
            "Unusually high number of warning messages detected."
        )

    explanations.append(
        f"Overall system risk classified as {risk_result.get('risk_level')}."
    )

    return " ".join(explanations)
