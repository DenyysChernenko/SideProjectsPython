import os


class LogParser:

    def __init__(self, key_strings, log_directory_path, timestamp_format):
        self.key_strings = key_strings
        self.log_directory_path = log_directory_path
        self.timestamp_format = timestamp_format

    def parse_log_files(self):
        report_data = []

        list_with_all_files = os.listdir(self.log_directory_path)
        list_with_log_files = [
            file for file in list_with_all_files if file.endswith(".log")
        ]
        for log_file in list_with_log_files:
            with open(
                os.path.join(self.log_directory_path, log_file)
            ) as log_file_content:
                data = log_file_content.read()
                for key_string in self.key_strings:
                    keyword_count = data.count(key_string)

                    if keyword_count != 0:
                        report_data.append((log_file, key_string, keyword_count))

        return report_data

    def print_parser_configuration(self):
        print(f"Find these strings: {self.key_strings}")
        print(f"In this log directory: {self.log_directory_path}")
        print(f"With this timestamp format: {self.timestamp_format}")

    @staticmethod
    def validate_attribtues(key_strings, log_directory_path):
        if not os.path.isdir(log_directory_path):
            print(log_directory_path)
            raise ValueError("log_directory_path must be a directory")

        if not isinstance(key_strings, list) or not all(
            isinstance(word, str) for word in key_strings
        ):
            raise ValueError("key_strings must be a list with all strings")

        return True

    @classmethod
    def from_config(cls, key_strings, log_directory_path, timestamp_format):
        cls.validate_attribtues(key_strings, log_directory_path)
        return cls(key_strings, log_directory_path, timestamp_format)
