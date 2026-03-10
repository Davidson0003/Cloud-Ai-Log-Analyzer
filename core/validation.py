# core/validation.py

def validate_logs(parsed_logs: list) -> list:
    """
    Filters out malformed or incomplete log records.
    """

    valid_logs = []

    for log in parsed_logs:
        if (
            log.get("timestamp") and
            log.get("level") and
            log.get("message")
        ):
            valid_logs.append(log)

    return valid_logs
