def read_log_file(file_path):
    """
    Reads a log file and returns all lines as a list
    """

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        lines = file.readlines()

    return lines
def parse_log_lines(lines):
    """
    Converts raw log lines into structured data
    """

    parsed_logs = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        parts = line.split(" ", 3)

        if len(parts) < 4:
            continue

        log_entry = {
            "timestamp": parts[0] + " " + parts[1],
            "level": parts[2],
            "message": parts[3]
        }

        parsed_logs.append(log_entry)

    return parsed_logs
def parse_logs(log_lines):
    parsed = []

    for line in log_lines:
        # Example log format:
        # [TIME] LEVEL Message
        parts = line.split(" ", 2)

        if len(parts) == 3:
            parsed.append({
                "timestamp": parts[0],
                "level": parts[1],
                "message": parts[2]
            })

    return parsed
