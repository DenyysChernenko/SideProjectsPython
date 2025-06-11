import csv
from datetime import datetime
import os


class Report:

    def __init__(self, report_data_list=None, timestamp_format=None):
        self.report_data_list = []
        if report_data_list is not None:
            self.report_data_list = report_data_list

        self.timestamp_format = "%Y-%m-%d_%H-%M-%S"
        if timestamp_format is not None:
            self.timestamp_format = timestamp_format

    def write_csv_report(self):
        os.makedirs("reports", exist_ok=True)

        timestamp = datetime.now().strftime(self.timestamp_format)
        file_name = f"reports/csv_report{timestamp}.csv"
        with open(file_name, "w", newline="") as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["file_name", "keyword", "count"])
            for report_info in self.report_data_list:
                writer.writerow(report_info)

    def print_summary(self):
        print("===SUMMARY INFROMATION IN TERMINAL===")
        for data in self.report_data_list:
            print(data)
        print("=====================================")
