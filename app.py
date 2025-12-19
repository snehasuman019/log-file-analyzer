import os

def analyze_logs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(base_dir, "logs", "app.log")

    print("DEBUG: Trying to read log file from:")
    print(log_file)

    if not os.path.exists(log_file):
        print("❌ ERROR: Log file not found!")
        return

    total_lines = 0
    error_count = 0

    with open(log_file, "r") as file:
        for line in file:
            total_lines += 1
            if "ERROR" in line:
                error_count += 1

    print("\n===== LOG ANALYSIS v1.0 =====")
    print(f"Total log entries: {total_lines}")
    print(f"Total ERROR logs: {error_count}")


if __name__ == "__main__":
    analyze_logs()
