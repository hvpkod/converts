import json
import os
import sys

import pandas as pd


def convert_csv_to_json(csv_file):
    # Check if the CSV file exists
    if not os.path.isfile(csv_file):
        print("CSV file not found.")
        sys.exit(1)

    # Extract the file name without extension
    file_name = os.path.splitext(csv_file)[0]

    # Generate the JSON file name
    json_file = file_name + ".json"

    # Read the CSV file using pandas with semicolon delimiter
    data_frame = pd.read_csv(csv_file, delimiter=";")

    # Convert the data frame to JSON format with 4-indentation and Unicode support
    json_data = data_frame.to_json(orient="records", indent=4, force_ascii=False)

    # Write the JSON data to the output file
    with open(json_file, "w", encoding="utf-8") as file:
        file.write(json_data)


if __name__ == "__main__":
    # Check if the CSV file name is provided as a command line argument
    if len(sys.argv) < 2:
        print("Please provide the CSV file name as a command line argument.")
        sys.exit(1)

    # Get the CSV file name from the command line argument
    csv_file = sys.argv[1]

    # Call the function to convert CSV to JSON
    convert_csv_to_json(csv_file)
