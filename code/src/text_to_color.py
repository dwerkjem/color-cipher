"""
This module contains functions for converting text to color. The main function is char_list_to_color_dict, which generates a dictionary mapping each character in a list to a unique RGB color.
Other functions include distribute_characters, which distributes characters across the dictionary according to their frequencies, and decrease_resolution_of_dict, which decreases the resolution of a frequency dictionary.

Functions:
- distribute_characters: Distributes characters across the dictionary according to their frequencies.
- decrease_resolution_of_dict: Decreases the resolution of a frequency dictionary.
- calculate_color_depth: Calculates the color depth based on the total number of colors.
- get_channel_range: Returns the range of values for each color channel based on the color depth.
- generate_rgb_combinations: Generates all possible RGB combinations for a given color depth.
- char_list_to_color_dict: Maps a list of characters to RGB color combinations.

Modules:
- math: Provides mathematical functions.

Usage:
The char_list_to_color_dict function is used to generate a color dictionary for mapping characters to colors. This color dictionary can be used to convert text to color in various applications.

Example:
char_list = ['a', 'b', 'c']
color_dict = char_list_to_color_dict(char_list)
print(color_dict)
# Output: {(0, 0, 0): 'a', (0, 0, 1): 'b', (0, 0, 2): 'c'}
"""

import math


def distribute_characters(char_ratio, L):
    """
    Distributes characters based on their frequency ratio.

    Args:
    char_ratio (dict): A dictionary mapping characters to their frequency ratio.
    L (int): The total number of characters to distribute.

    Returns:
    list: A list of characters distributed according to their frequency ratio.

    Example:
    char_ratio = {"a": 2, "b": 3, "c": 5}
    L = 20
    result = distribute_characters(char_ratio, L)
    # Output: ['a', 'b', 'c', 'b', 'c', 'a', 'b', 'c', 'c', 'c', 'a', 'b', 'c', 'b', 'c', 'a', 'b', 'c', 'c', 'c']
    """
    total_ratio = sum(char_ratio.values())
    char_count = {
        char: int((ratio / total_ratio) * L) for char, ratio in char_ratio.items()
    }
    total_assigned = sum(char_count.values())

    while total_assigned < L:
        for char in char_count:
            if total_assigned < L:
                char_count[char] += 1
                total_assigned += 1
            else:
                break

    while total_assigned > L:
        for char in char_count:
            if total_assigned > L and char_count[char] > 0:
                char_count[char] -= 1
                total_assigned -= 1
            else:
                break

    result = [None] * L
    for char, count in char_count.items():
        if count == 0:
            continue
        interval = L / count
        for i in range(count):
            position = math.floor(i * interval)
            while result[position] is not None:
                position = (position + 1) % L
            result[position] = char

    return result


def decrease_resolution_of_dict(dictionary, maxResolution):
    """
    Decreases the resolution of a frequency dictionary.

    Args:
    dictionary (dict): A dictionary mapping keys to their frequencies.
    maxResolution (int): The maximum resolution to reduce the dictionary to.

    Returns:
    dict: A dictionary with reduced resolution. sum(dictionary.values()) <= maxResolution

    Example:
    dictionary = {"a": 10, "b": 20, "c": 30}
    maxResolution = 40
    reducedDict = decrease_resolution_of_dict(dictionary, maxResolution)
    # Output: {"a": 4, "b": 8, "c": 12}
    """
    totalResolution = sum(dictionary.values())
    if totalResolution <= maxResolution:
        return dictionary

    scalingFactor = maxResolution / totalResolution
    decreasedDict = {key: value * scalingFactor for key, value in dictionary.items()}
    scalingFactorSum = sum(decreasedDict.values())
    normalizationFactor = maxResolution / scalingFactorSum

    normalizedDict = {
        key: max(1, round(value * normalizationFactor))
        for key, value in decreasedDict.items()
    }
    difference = maxResolution - sum(normalizedDict.values())

    sorted_keys = sorted(
        normalizedDict, key=normalizedDict.get, reverse=(difference > 0)
    )
    for key in sorted_keys:
        if difference == 0:
            break
        if (difference > 0) or (normalizedDict[key] > 1):
            normalizedDict[key] += 1 if difference > 0 else -1
            difference += -1 if difference > 0 else 1

    return normalizedDict


def calculate_color_depth(total_colors):
    """
    Calculates the color depth based on the total number of colors.

    Args:
    total_colors (int): The total number of colors.

    Returns:
    int: The color depth for the given number of colors.

    Example:
    total_colors = 256
    color_depth = calculate_color_depth(total_colors)
    # Output : 4

    """
    color_depth = math.log2(total_colors) / 3
    return int(color_depth)


def get_channel_range(color_depth):
    """
    Returns the range of values for each color channel based on the color depth.

    Args:
    color_depth (int): The color depth.

    Returns:
    int: The range of values for each color channel.

    Example:
    color_depth = 8
    channel_range = get_channel_range(color_depth)
    # Output: 256
    """
    return 2**color_depth


def generate_rgb_combinations(color_depth):
    """
    Generates all possible RGB combinations for a given color depth.

    Args:
    color_depth (int): The color depth.

    Returns:
    list: A list of all possible RGB combinations.

    Example:
    color_depth = 1
    result = generate_rgb_combinations(color_depth)
    # Output: [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
    """
    max_value = 2**color_depth
    combinations = [
        (r, g, b)
        for r in range(max_value)
        for g in range(max_value)
        for b in range(max_value)
    ]
    return combinations


def char_list_to_color_dict(char_list):
    """
    Generates a dictionary mapping each character in char_list to a unique RGB color.

    Args:
    char_list (list): A list of characters to map to RGB colors.

    Returns:
    dict: A dictionary mapping characters to RGB colors.

    Example:
    char_list = ['a', 'b', 'c']
    color_dict = char_list_to_color_dict(char_list)
    print(color_dict)
    # Output: {(0, 0, 0): 'a', (0, 0, 1): 'b', (0, 0, 2): 'c'}
    """
    color_depth = calculate_color_depth(len(char_list))
    rgb_combinations = generate_rgb_combinations(color_depth)
    color_dict = {rgb_combinations[i]: char_list[i] for i in range(len(char_list))}
    return color_dict
