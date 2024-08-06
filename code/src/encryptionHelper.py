import math

def distribute_characters(char_ratio, L):
    """
    Distributes characters based on the 1U formula.

    Parameters:
    char_ratio (dict): A dictionary where keys are characters and values are their ratios.
    L (int): Total number of positions to distribute the characters.

    Returns:
    list: A list of length L with the characters distributed based on their ratios.
    """
    # Calculate the total ratio sum
    total_ratio = sum(char_ratio.values())

    # Calculate the number of times each character should appear
    char_count = {
        char: int((ratio / total_ratio) * L) for char, ratio in char_ratio.items()
    }

    # Adjust the counts to ensure the total count is exactly L
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

    # Create the result list
    result = [None] * L

    # Distribute the characters evenly
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
    Ensures that the resolution of the dictionary is not greater than maxResolution.
    If it is greater, it decreases the resolution of the dictionary to maxResolution.
    Ensures no value in the dictionary is below 1, raises ResolutionError if not possible.

    Parameters:
    dictionary (dict): A dictionary where keys are characters and values are their ratios.
    maxResolution (int): The maximum resolution of the dictionary.

    Returns:
    dict: A dictionary with a resolution of at most maxResolution.
    """
    # Calculate the total resolution of the dictionary
    totalResolution = sum(dictionary.values())

    # If the total resolution is already less than or equal to maxResolution, return the dictionary as is
    if totalResolution <= maxResolution:
        return dictionary

    # If maxResolution is less than the number of items in the dictionary, raise an error
    assert len(dictionary) <= maxResolution, "ResolutionError: maxResolution is less than the number of items in the dictionary."
    # Calculate the scaling factor to reduce the resolution
    scalingFactor = maxResolution / totalResolution

    # Create a new dictionary with the decreased resolution
    decreasedDict = {key: value * scalingFactor for key, value in dictionary.items()}

    # Normalize the values to ensure they sum up to maxResolution
    scalingFactorSum = sum(decreasedDict.values())
    normalizationFactor = maxResolution / scalingFactorSum

    normalizedDict = {
        key: max(1, round(value * normalizationFactor))
        for key, value in decreasedDict.items()
    }

    # Adjust the total to match maxResolution exactly if needed
    difference = maxResolution - sum(normalizedDict.values())
    if difference != 0:
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


# Importing the itertools module to generate combinations
import itertools


def _calculate_color_depth(total_colors):
    # Calculate the color depth by taking the base-2 logarithm of the total number of colors
    color_depth = math.log2(total_colors)
    assert color_depth.is_integer(), "The total number of colors must be a power of 2."
    return int(color_depth)


def _get_channel_range(color_depth):
    # Each channel's bit depth in a 24-bit color depth (8 bits per channel)
    bits_per_channel = color_depth // 3
    # Calculate the maximum value for each channel
    max_value = (1 << bits_per_channel) - 1
    return max_value


def _generate_rgb_combinations(color_depth=24):
    # Get the maximum value for each channel
    max_value = _get_channel_range(color_depth)

    # Create a list of all possible values for R, G, and B (0 to max_value)
    values = range(max_value + 1)

    # Generate all combinations using itertools.product
    rgb_combinations = list(itertools.product(values, repeat=3))

    return rgb_combinations


def char_list_to_color_dict(char_list):
    # Calculate the total number of colors required
    total_colors = len(char_list)

    # Calculate the color depth based on the total number of colors
    color_depth = _calculate_color_depth(total_colors)

    # Generate all possible RGB combinations for the given color depth
    rgb_combinations = _generate_rgb_combinations(color_depth)

    # Create a dictionary mapping each character to an RGB color
    color_dict = {char: rgb for char, rgb in zip(char_list, rgb_combinations)}

    return color_dict