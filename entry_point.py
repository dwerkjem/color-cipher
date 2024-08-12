"""
This is the entry point of the program which generates and caches dictionaries for character frequency and color mapping.

The script performs the following tasks:
1. Sets configuration parameters such as color depth, image resolution, and the base directory for storing generated tables.
2. Defines file paths for saving the frequency dictionary and color dictionary.
3. Implements the `check_cache` function which:
    a. Creates the base directory if it doesn't exist.
    b. Generates a frequency dictionary fitted to the specified color depth.
    c. Reduces the resolution of the frequency dictionary to fit the maximum dictionary resolution.
    d. Distributes characters across the dictionary according to their frequencies.
    e. Saves the frequency dictionary to a pickle file.
    f. Converts the character list to a color dictionary.
    g. Saves the color dictionary to a pickle file.
4. Calls the `check_cache` function from the `main` function if the script is executed as the main module.

Functions:
- `check_cache()`: Generates and caches the frequency and color dictionaries.
- `main()`: Calls the `check_cache` function.

Modules:
- `os`: Provides functions for interacting with the operating system.
- `pickle`: Implements binary protocols for serializing and de-serializing a Python object structure.
- `code.src.tableOfValues`: Contains the `get_freq_dict` function to get the character frequency dictionary.
- `code.src.textToColor`: Contains the functions `char_list_to_color_dict`, `distribute_characters`, and `decrease_resolution_of_dict` for processing character frequencies and mapping them to colors.

Usage:
To execute the script, simply run it as the main module. The script will generate and cache the required dictionaries for the specified color depth and save them in the configured directory.
"""

import os
import pickle
from src.values_table import get_freq_dict
from code.src.text_to_color import (
    char_list_to_color_dict,
    distribute_characters,
    decrease_resolution_of_dict,
)

COLOR_DEPTH = 24
IMAGE_RESOLUTION = (1920, 1080)
MAX_DICT_RESOLUTION = 2**COLOR_DEPTH
BASE_DIR = "code/build/tables"
dict_file = os.path.join(BASE_DIR, f"dict{COLOR_DEPTH}.pkl")
color_dict_file = os.path.join(BASE_DIR, f"color_dict{COLOR_DEPTH}.pkl")


def check_cache():
    """
    Generate and cache the frequency and color dictionaries.
    """
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    print(f"Generating tables for color depth {COLOR_DEPTH}...")
    # Fit the dictionary to the color depth
    char_ratio = get_freq_dict()
    char_ratio = decrease_resolution_of_dict(char_ratio, MAX_DICT_RESOLUTION)
    char_ratio = distribute_characters(char_ratio, MAX_DICT_RESOLUTION)
    with open(dict_file, "wb") as f:
        pickle.dump(char_ratio, f)
    colorDict = char_list_to_color_dict(char_ratio)
    with open(color_dict_file, "wb") as f:
        pickle.dump(colorDict, f)


def main():
    """
    Main function to check and generate the cache.
    """
    check_cache()


if __name__ == "__main__":
    main()
