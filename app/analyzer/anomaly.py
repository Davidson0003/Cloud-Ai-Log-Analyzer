def find_anomalies(parsed_logs):
    anomalies = []

    for log in parsed_logs:
        if log["level"] in ["ERROR", "CRITICAL"]:
            anomalies.append(log)

    return anomalies
