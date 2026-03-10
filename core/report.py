# core/report.py

import json
import datetime
import os

REPORT_DIR = "reports"

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

def export_report(data: dict, format: str = "json") -> str:
    """
    Exports analysis report.
    """

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    if format == "json":
        filename = f"report_{timestamp}.json"
        filepath = os.path.join(REPORT_DIR, filename)

        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)

        return filepath
