import json
import os
from .parser import parse_yara_file


def cli_rule_add(file_path: str) -> bool:
    if not os.path.isfile(file_path):
        return False
    rules_list = parse_yara_file(file_path)
    with open("rules.jsonl", "a") as json_file:
        for rule in rules_list:
            json.dump(rule, json_file)
            json_file.write("\n")
    return True


def cli_rules_list() -> None:
    try:
        with open("rules.jsonl", "r") as rule_file:
            for line in rule_file:
                rule = json.loads(line)
                print(rule)
    except FileNotFoundError:
        print("File was not found!")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSONL: {e}")
