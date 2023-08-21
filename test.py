import json
with open("./output.json", 'r') as f:
    json_data = json.load(f)
    print(json_data[14]['price'][3:])
