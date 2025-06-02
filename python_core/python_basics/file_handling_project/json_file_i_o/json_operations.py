import json


# Serialization
# json.dumps() -> convert python object to a JSON | python -> JSON
# json.dump() -> convert and write to a JSON File | convert+write -> JSON

# Deserialization
# json.loads() -> convert JSON String to a Python Object | JSON -> python
# json.load() -> read JSON from a file and convert to Python | read from JSON -> Python

 
# json.JSONDecodeError Raised

with open("example.json", "r") as f:
    data = json.load(f)
    # print(data)


malware_data = {
    'file_name': "malicious.exe",
    'file_hash': "abc123def456",
    'detection_result': True,
    'scan_date': "2025-06-01",
    'threat_name': "Trojan.Generic",
    'severity': "High",
    'engine_version': "5.2.4",
    "scan_info": {
        "date": "2025-06-01",
        "engine_version": "5.2.4"
    }
}

json_string = json.dumps(malware_data, indent=4) 
# print(json_string)   


with open('example.json', 'w') as f:
    json.dump(malware_data, f, indent=4)


with open('example.json', 'r') as f:
    data = json.load(f)
    # print(data) # -> python dict
    # print(type(data))
    # print(json.dumps(data, indent=4))
    # print(type(json.dumps(data, indent=4))) # -> formatted json string
    

with open('example.json', 'r') as f:
    data_json = json.load(f)
    data_json.update({'detection_result': False})
    data_json['file_name'] = 'dota.exe'

with open('example.json', 'w') as f:
    json.dump(data_json, f, indent=4)
    
     
try:
    with open('error.json', 'r') as f:
        data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Erorr to open JSON as this error: {e}")



json_string = '{"age": 15, "is_old_enough": false}'
python_dict = json.loads(json_string)
print(type(python_dict))
print(python_dict)
