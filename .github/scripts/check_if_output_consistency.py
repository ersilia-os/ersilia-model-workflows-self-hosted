import sys
import json
import yaml

file_name = sys.argv[1]

if file_name.endswith(".json"):
    with open(file_name, 'r') as f:
        data = json.load(f)
    sys.stdout.write(data.get("Output Consistency", ""))
elif file_name.endswith(".yaml") or file_name.endswith(".yml"):
    with open(file_name, 'r') as f:
        data = yaml.safe_load(f)
    sys.stdout.write(data.get("Output Consistency", ""))
