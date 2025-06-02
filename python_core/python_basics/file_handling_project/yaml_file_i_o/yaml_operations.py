import yaml


filename = "malware_scan_config.yml"

with open(filename, "r") as f:
    data = yaml.safe_load(f)
    # print(data)
    # print(yaml.dump(data, indent=4))

malware_scan = {
    "file_name": "ransomware_sample.exe",
    "file_hash": "d41d8cd98f00b204e9800998ecf8427e",
    "detection_result": True,
    "scan_date": "2025-06-02",
    "threat_name": "Ransom.Locky",
    "severity": "Critical",
    "engine_version": "7.5.1",
    "scan_info": {
        "scanned_by": "MalwareScannerPro",
        "scan_duration_seconds": 45,
        "definitions_version": "2025-06-01",
    },
}


print(yaml.safe_dump(malware_scan, indent=4))


with open(filename, "w") as f:
    yaml.safe_dump(malware_scan, f, indent=4)

with open(filename, "r") as f:
    data = yaml.safe_load(f)
    data["scan_info"]["scan_duration_seconds"] = 50

with open(filename, "w") as f:
    yaml.safe_dump(data, f, indent=4)

try:
    with open("error.yml", "r") as f:
        data = yaml.safe_load(f)
except yaml.YAMLError as e:
    print(f"Failed to parse YAML data {e}")
