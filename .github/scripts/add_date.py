import sys
import json
from ruamel.yaml import YAML

file_name = sys.argv[1]
date_str = sys.argv[2]

if file_name.endswith(".json"):
    with open(file_name, 'r') as f:
        data = json.load(f)
    data['Incorporation Date'] = date_str
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
elif file_name.endswith(".yaml") or file_name.endswith(".yml"):
    yaml = YAML()
    with open(file_name, 'r') as f:
        data = yaml.load(f)
    data['Incorporation Date'] = date_str
    with open(file_name, 'w') as f:
        yaml.dump(data, f)
else:
    raise ValueError("Unsupported file format. Please provide a .json or .yaml file.")
