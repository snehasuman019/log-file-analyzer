from collections import Counter, defaultdict

def log_level_count(logs):
    return Counter(log["level"] for log in logs)

def error_frequency(logs):
    errors = [log["message"] for log in logs if log["level"] == "ERROR"]
    return Counter(errors)

def logs_per_hour(logs):
    hourly_logs = defaultdict(int)

    for log in logs:
        hour = log["timestamp"].strftime("%Y-%m-%d %H:00")
        hourly_logs[hour] += 1

    return dict(hourly_logs)

print("stats.py loaded successfully")
