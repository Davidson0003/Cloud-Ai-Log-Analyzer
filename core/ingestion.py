# core/ingestion.py

from typing import List


def read_log_file(file_path: str) -> List[str]:
    """
    Reads a log file from the given path and returns
    a list of raw log lines.
    """
    log_lines = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                cleaned_line = line.strip()
                if cleaned_line:
                    log_lines.append(cleaned_line)

    except FileNotFoundError:
        raise Exception("Log file not found.")

    except Exception as e:
        raise Exception(f"Error reading log file: {str(e)}")

    return log_lines
