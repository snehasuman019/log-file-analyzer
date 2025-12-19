import argparse
from analyzer.parser import parse_logs
from analyzer.stats import log_level_count, error_frequency, logs_per_hour
from analyzer.report import generate_json_report

def main():
    parser = argparse.ArgumentParser(description="Log Analyzer v3.0")
    parser.add_argument("--logfile", required=True, help="Path to log file")
    parser.add_argument(
        "--report",
        default="reports/analysis_report.json",
        help="Output JSON report path"
    )

    args = parser.parse_args()

    logs = parse_logs(args.logfile)

    report_data = {
        "total_logs": len(logs),
        "log_levels": log_level_count(logs),
        "top_errors": error_frequency(logs),
        "logs_per_hour": logs_per_hour(logs)
    }

    generate_json_report(report_data, args.report)

    print("===== LOG ANALYSIS v3.0 =====")
    print(f"Total Logs: {report_data['total_logs']}")
    print("Log Levels:", report_data["log_levels"])
    print("Top Errors:", report_data["top_errors"])
    print("Logs per Hour:", report_data["logs_per_hour"])
    print(f"Report saved at: {args.report}")

if __name__ == "__main__":
    main()
