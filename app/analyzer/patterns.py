def analyze_patterns(parsed_logs):
    summary = {
        "ERROR": 0,
        "WARNING": 0,
        "INFO": 0
    }

    for log in parsed_logs:
        level = log["level"]
        if level in summary:
            summary[level] += 1

    return summary
