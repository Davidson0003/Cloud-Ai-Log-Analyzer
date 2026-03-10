# core/timeseries.py

def analyze_time_series(hourly_activity: dict) -> dict:
    """
    Analyzes log activity over time to detect spikes or inactivity.
    """

    if not hourly_activity:
        return {
            "activity_pattern": "No data",
            "spike_detected": False
        }

    values = list(hourly_activity.values())
    average = sum(values) / len(values)

    spike_detected = False

    for count in values:
        if count > average * 2:
            spike_detected = True
            break

    return {
        "average_activity": round(average, 2),
        "spike_detected": spike_detected,
        "activity_pattern": "Spike detected" if spike_detected else "Normal activity"
    }
