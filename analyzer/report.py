import json

def generate_json_report(data, output_path):
    with open(output_path, "w") as file:
        json.dump(data, file, indent=4, default=str)
