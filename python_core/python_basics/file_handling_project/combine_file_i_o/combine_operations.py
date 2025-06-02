from pathlib import Path
import json
import yaml

current_file = Path(__file__)
current_dir = current_file.parent

files_list = Path(current_dir).glob("*.txt")
log_filename = "log_file.log"
log_filename = current_dir / "log_file.log"


with open(log_filename, "a") as log_file:
    for file in files_list:
        log_file.write(f"\n--- {file.name} ---\n")
        with open(file, "r") as text_file:
            content = text_file.read()
            log_file.write(content + "\n")


# =========================================================

json_filename = "json_example.json"
yaml_filename = "yaml_example.yaml"

with open(json_filename, "r") as json_file:
    content_from_json = json.load(json_file)

with open(yaml_filename, "w") as yaml_file:
    yaml.safe_dump(content_from_json, yaml_file, default_flow_style=False)
