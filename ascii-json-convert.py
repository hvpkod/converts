import json
import sys


def convert_to_json(input_file_path, output_file_path):
    try:
        with open(input_file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)

    data = {}
    for line in lines:
        key, value = map(str.strip, line.split(" ", 1))
        data[key] = value

    with open(output_file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Conversion completed. JSON data saved to {output_file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file.txt output.json")
        sys.exit(1)

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    convert_to_json(input_file_name, output_file_name)
