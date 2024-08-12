import os
import pickle
from code.src.tableOfValues import get_freq_dict
from code.src.textToColor import (
    char_list_to_color_dict,
    distribute_characters,
    decrease_resolution_of_dict,
)

color_depth = 24
image_resolution = (1920, 1080)
max_dict_resolution = 2**color_depth
base_dir = "code/build/tables"
dict_file = os.path.join(base_dir, f"dict{color_depth}.pkl")
color_dict_file = os.path.join(base_dir, f"color_dict{color_depth}.pkl")


def check_cache():
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    print(f"Generating tables for color depth {color_depth}...")
    # Fit the dictionary to the color depth
    char_ratio = get_freq_dict()
    char_ratio = decrease_resolution_of_dict(char_ratio, max_dict_resolution)
    char_ratio = distribute_characters(char_ratio, max_dict_resolution)
    with open(dict_file, "wb") as f:
        pickle.dump(char_ratio, f)
    colorDict = char_list_to_color_dict(char_ratio)
    with open(color_dict_file, "wb") as f:
        pickle.dump(colorDict, f)


def main():
    check_cache()


if __name__ == "__main__":
    main()
