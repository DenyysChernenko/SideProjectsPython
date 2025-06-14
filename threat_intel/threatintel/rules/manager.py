import json
import os
from .parser import parse_yara_file


def cli_rule_add(file_path: str) -> bool:
    
    if not os.path.isfile(file_path):
        print(f"Provided file does not exist: {file_path}")
        return False
    rules_list = parse_yara_file(file_path)
    loaded_rules_list = []    
    
    try:
        with open("rules.jsonl", "r", encoding="utf-8") as read_json_file:
            for line in read_json_file:
                try:
                    rule = json.loads(line)
                    loaded_rules_list.append(rule)
                except json.JSONDecodeError as e:
                    print(f"Skipping invalid JSONL line: {e}")
                    continue
    except Exception as e:
        print(f"Error reading existing rules: {e}")
        return False
           
                
    try:
        with open("rules.jsonl", "a", encoding="utf-8") as json_file:
            for rule in rules_list:
                if rule in loaded_rules_list:
                    continue
                json.dump(rule, json_file)
                json_file.write("\n")
    except Exception as e:
        print(f"Error writing to rules file: {e}")
        return False
    
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


def cli_rule_remove(rule_name: str) -> bool:
    try:
        is_deleted = False
        with open("rules.jsonl", "r", encoding="utf-8") as rule_file, \
             open("file.tmp", "w", encoding="utf-8") as temp_file:
                 
            for line in rule_file:
                try:
                    rule = json.loads(line)
                    if rule['rule_name'] != rule_name:
                        json.dump(rule, temp_file)
                        temp_file.write("\n")
                    else:
                        is_deleted = True
                except json.JSONDecodeError as e:
                    print(f"Failed to parse JSONL line {e}")
                    continue
            
        if is_deleted:
            os.replace("file.tmp", "rules.jsonl")
            return True
        else:
            os.remove("file.tmp")
            return False

    except json.JSONDecodeError as e:
        print(f"Error decoding JSONL: {e}")
        return False
    