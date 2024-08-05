import os
import json


def get_json_file_length(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
            return len(data)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def main(directory):
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' is not a directory.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                length = get_json_file_length(file_path)
                if length is not None:
                    print(f"{file}: {length} characters")


if __name__ == "__main__":
    directory = "build/tables"
    main(directory)
