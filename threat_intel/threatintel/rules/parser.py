from plyara import Plyara


def parse_yara_file(file_path: str) -> list[dict]:
    parser = Plyara()
    with open(file_path, "r") as yara_file:
        yara_source = yara_file.read()

    if not yara_source.strip():
        raise ValueError(f"YARA file can't be empty, path is: {file_path}")

    try:
        parsed_rules = parser.parse_string(yara_source)
    except Exception as e:
        raise ValueError(f"Failed to parse YARA file: {file_path}: {e}")

    if not parsed_rules:
        raise ValueError(f"No YARA rules found in file: {file_path}")

    serialized_rules = serialize_yara_rules(parsed_rules)
    return serialized_rules


def serialize_yara_rules(parsed_rules: list[dict]) -> list[dict]:
    serialized_rules_list = []
    for rule in parsed_rules:
        if "rule_name" not in rule:
            raise KeyError(f"Parsed rule missing 'rule_name' field: {rule}")

        if "strings" not in rule:
            raise KeyError(f"Parsed rule missing 'strings' field: {rule}")

        rule_data = {
            "rule_name": rule["rule_name"],
            "string_names": extract_string_names(rule["strings"]),
        }
        serialized_rules_list.append(rule_data)
    return serialized_rules_list


def extract_string_names(strings: list[dict]) -> list[str]:
    names = []
    for s in strings:
        if "name" not in s:
            raise KeyError(f"String object missing 'name' field: {s}")
        names.append(s["name"])
    return names
