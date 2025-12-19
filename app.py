import os

def analyze_logs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(base_dir, "logs", "app.log")

    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    if not os.path.exists(log_file):
        print("❌ Log file not found!")
        return

    with open(log_file, "r") as file:
        for line in file:
            for level in log_counts:
                if level in line:
                    log_counts[level] += 1

    print("\n===== LOG ANALYSIS v2.0 =====")
    print(f"INFO logs    : {log_counts['INFO']}")
    print(f"WARNING logs : {log_counts['WARNING']}")
    print(f"ERROR logs   : {log_counts['ERROR']}")
    print("============================")


if __name__ == "__main__":
    analyze_logs()
