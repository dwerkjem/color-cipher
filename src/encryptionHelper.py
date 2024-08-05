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
