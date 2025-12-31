def generate_summary(parsed_logs):
    summary = {
        "total_logs": len(parsed_logs),
        "error_count": 0,
        "warning_count": 0,
        "info_count": 0
    }

    for log in parsed_logs:
        level = log["level"].upper()
        if level == "ERROR":
            summary["error_count"] += 1
        elif level == "WARNING":
            summary["warning_count"] += 1
        elif level == "INFO":
            summary["info_count"] += 1

    return summary
