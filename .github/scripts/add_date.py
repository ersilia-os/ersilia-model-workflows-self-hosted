import sys
import json
import collections
from ruamel.yaml import YAML

file_name = sys.argv[1]
date_str = sys.argv[2]

new_order = [
    'Identifier',
    'Slug',
    'Status',
    'Title',
    'Description',
    'Deployment',
    'Source',
    'Source Type',
    'Task',
    'Subtask',
    'Input',
    'Input Dimension',
    'Input Shape',
    'Output',
    'Output Dimension',
    'Output Consistency',
    'Interpretation',
    'Tag',
    'Biomedical Area',
    'Target Organism',
    'GitHub',
    'Publication Type',
    'Publication Year',
    'Publication',
    'Source Code',
    'License',
    'Host URL',
    'Contributor',
    'Contributor Profile',
    'Incorporation Date',
    'Incorporation Quarter',
    'Incorporation Year',
    'S3',
    'DockerHub',
    'Docker Architecture',
    'Docker Pack Method',
    'DO Deployment',
    'Biomodel Annotation',
    'Runtime',
    'Secrets',
    'Model Size',
    'Environment Size',
    'Image Size',
    'Computational Performance 1',
    'Computational Performance 10',
    'Computational Performance 100'
]

def sort_dictionary(data):
    data_ = collections.OrderedDict()
    for k in new_order:
        if k in data:
            data_[k] = data[k]
    for k,v in data.items():
        if k not in new_order:
            data_[k] = v
    return data_

if file_name.endswith(".json"):
    with open(file_name, 'r') as f:
        data = json.load(f)
    data['Incorporation Date'] = date_str
    data = sort_dictionary(data)       
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
elif file_name.endswith(".yaml") or file_name.endswith(".yml"):
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    with open(file_name, 'r') as f:
        data = yaml.load(f)
    data['Incorporation Date'] = date_str
    data = sort_dictionary(data)
    with open(file_name, 'w') as f:
        yaml.dump(data, f)
else:
    raise ValueError("Unsupported file format. Please provide a .json or .yaml file.")
