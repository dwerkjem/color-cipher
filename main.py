import os
import json
from src.tableOfValues import *
from src.encryptionHelper import *

color_depth = 24
image_resolution = (1920, 1080)
max_dict_resolution = 2**color_depth
base_dir = "build/tables"
dict_file = os.path.join(base_dir, f"dict{color_depth}.json")
color_dict_file = os.path.join(base_dir, f"color_dict{color_depth}.json")


def gen_file():
    try:
        freq_dict = decrease_resolution_of_dict(get_freq_dict(), max_dict_resolution)  # type: ignore
        distribution = distribute_characters(freq_dict, max_dict_resolution)
        with open(dict_file, "w") as file:
            json.dump(distribution, file)
    except Exception as e:
        print(f"Error generating file: {e}")


def ensure_exist():
    assert os.path.exists(
        "build"
    ), "Please run the program from the root directory and ensure that the build directory exists"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    if not os.path.exists(dict_file):
        gen_file()

def main():
    ensure_exist()
    with open(dict_file, "r") as file:
        distribution = json.load(file)
    color_dict = char_list_to_color_dict(distribution)
    with open(color_dict_file, "w") as file:
        json.dump(color_dict, file)
if __name__ == "__main__":
    main()
