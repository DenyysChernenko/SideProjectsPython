import argparse
from log_scanner.parser import LogParser  # type: ignore
from log_scanner.report import Report  # type: ignore
import yaml
import os


config_dict = {"log_directory_path": "", "key_strings": [], "timestamp_format": ""}


def parse_arguments():
    parser = argparse.ArgumentParser(description="Parser for arguments")
    parser.add_argument("-p", "--path", help="Path to directory with logs")
    args = parser.parse_args()
    return args.path


def configure_attributes():

    with open("config/log_config.yml", "r", encoding="utf-8") as yaml_config:
        config = yaml.safe_load(yaml_config)
        config_dict["log_directory_path"] = config["log_directory_path"]
        config_dict["key_strings"] = config["key_strings"]
        config_dict["timestamp_format"] = config["timestamp_format"]


def main():

    log_dir_path = parse_arguments()
    configure_attributes()

    if log_dir_path:
        if not os.path.isdir(log_dir_path):
            print("Log_dir_path must be a directory")
        config_dict["log_directory_path"] = log_dir_path

    try:
        parser = LogParser.from_config(
            config_dict["key_strings"],
            config_dict["log_directory_path"],
            config_dict["timestamp_format"],
        )
    except ValueError as e:
        print(f"Configuration error: {e}")

    report_list = parser.parse_log_files()
    report_constructor = Report(report_list, config_dict["timestamp_format"])
    # report_constructor.write_csv_report()
    report_constructor.print_summary()


if __name__ == "__main__":
    main()
