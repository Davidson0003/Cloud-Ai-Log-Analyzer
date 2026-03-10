# core/parser.py

import re
from typing import List, Dict


LOG_PATTERN = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2}[\sT]\d{2}:\d{2}:\d{2})\s+'
    r'(?P<level>INFO|ERROR|WARNING|DEBUG)\s+'
    r'(?P<message>.*)'
)


def parse_logs(log_lines: List[str]) -> List[Dict[str, str]]:
    """
    Parses raw log lines into structured log records.
    """
    parsed_logs = []

    for line in log_lines:
        match = LOG_PATTERN.match(line)
        if match:
            parsed_logs.append(match.groupdict())

    return parsed_logs
