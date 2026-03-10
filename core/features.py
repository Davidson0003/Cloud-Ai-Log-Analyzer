# core/features.py

from typing import List, Dict
from collections import Counter
from datetime import datetime


def extract_features(parsed_logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Extracts numerical features from structured log data.
    """

    levels = []
    hourly_activity = Counter()

    for log in parsed_logs:
        level = log.get("level")
        timestamp = log.get("timestamp")

        if level:
            levels.append(level)

        if timestamp:
            try:
                hour = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").hour
                hourly_activity[hour] += 1
            except ValueError:
                pass

    level_counts = Counter(levels)

    features = {
        "total_logs": len(parsed_logs),
        "error_count": level_counts.get("ERROR", 0),
        "warning_count": level_counts.get("WARNING", 0),
        "info_count": level_counts.get("INFO", 0),
        "unique_hours_active": len(hourly_activity),
        "peak_activity_hour": hourly_activity.most_common(1)[0][0] if hourly_activity else None
    }

    return features
