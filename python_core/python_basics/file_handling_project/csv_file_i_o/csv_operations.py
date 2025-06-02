import csv

filename = "csv_example.csv"

with open(filename, "r", newline="") as f:
    content = csv.reader(f)
    next(content)
    for row in content:
        if row:
            print(row)

with open(filename, "r", newline="") as f:
    content_2 = csv.DictReader(f)
    for row_dict in content_2:
        print(row_dict)

with open("csv_example_2.csv", "w", newline="") as f:
    writer = csv.writer(f, dialect="excel")
    rows = [
        ["file_name", "file_hash", "detection_result"],
        ["dota2.exe", "dota2hash", "true"],
    ]
    # string_2 = ['dota2.exe', 'dota2hash', 'true']
    writer.writerows(rows)

with open("csv_example.csv", "w", newline="") as f:
    rows_data = [
        {"file_name": "dota2.exe", "file_hash": "dota2hash", "is_detected": True},
        {"file_name": "cs2.exe", "file_hash": "cs2hash", "is_detected": True},
    ]
    fieldnames = ["file_name", "file_hash", "is_detected"]

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows_data)

try:
    with open("non_existent_file.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("Sorry, the file does not exist. Please check the file name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

line_count = 0

with open(filename, "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        line_count += 1
        print(f"Line {line_count}: {row}")

print(f"Total lines processed: {line_count}")
