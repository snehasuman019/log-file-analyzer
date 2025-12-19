import re
from datetime import datetime

LOG_PATTERN = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"

def parse_logs(file_path):
    logs = []

    with open(file_path, "r") as file:
        for line in file:
            match = re.match(LOG_PATTERN, line)
            if match:
                timestamp, level, message = match.groups()
                logs.append({
                    "timestamp": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                    "level": level,
                    "message": message.strip()
                })

    return logs
print("parser.py loaded successfully")
