"""
This is the entry point of the program which generates and caches dictionaries for character frequency and color mapping.

The script performs the following tasks:
1. Imports the required modules.
2. Defines the color depth and image resolution.
3. Defines the maximum dictionary resolution based on the color depth.
4. Defines the `make_cache` function to generate and cache the frequency and color dictionaries.
5. Defines the `main` function to check and generate the cache.
6. Executes the `main` function if the script is run as the main module.

Functions:
- `make_cache()`: Generates and caches the frequency and color dictionaries.
- `main()`: Main function to check and generate the cache.
Modules:
- `os`: Provides functions for interacting with the operating system.
- `pickle`: Implements binary protocols for serializing and de-serializing a Python object structure.
- `code.src.tableOfValues`: Contains the `get_freq_dict` function to get the character frequency dictionary.
- `code.src.textToColor`: Contains the functions `char_list_to_color_dict`, `distribute_characters`, and `decrease_resolution_of_dict` for processing character frequencies and mapping them to colors.
- `code.src.cache_system`: Contains functions for caching and retrieving data.

Usage:
To execute the script, simply run it as the main module. The script will generate and cache the required dictionaries for the specified color depth and save them in the configured directory.
"""

from code.src.values_table import get_freq_dict
from code.src.text_to_color import (
    distribute_characters,
    decrease_resolution_of_dict,
)
from code.src.cache_system import cache_query, cache_result

COLOR_DEPTH = 24
IMAGE_RESOLUTION = (1920, 1080)
MAX_DICT_RESOLUTION = 2**COLOR_DEPTH


def make_cache():
    """
    Generate and cache the frequency and color dictionaries.
    """

    print(f"Generating tables for color depth {COLOR_DEPTH}...")
    # Fit the dictionary to the color depth
    char_ratio = get_freq_dict()
    char_ratio = decrease_resolution_of_dict(char_ratio, MAX_DICT_RESOLUTION)
    char_ratio = distribute_characters(char_ratio, MAX_DICT_RESOLUTION)
    cache_result(f"char_ratio.{COLOR_DEPTH}", char_ratio)


def main():
    """
    Main function to check and generate the cache.
    """
    if cache_query(f"char_ratio.{COLOR_DEPTH}") is None:
        make_cache()


if __name__ == "__main__":
    main()
