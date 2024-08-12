import math


def distribute_characters(char_ratio, L):
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
    color_depth = math.log2(total_colors) / 3
    return int(color_depth)


def get_channel_range(color_depth):
    return 2**color_depth


def generate_rgb_combinations(color_depth):
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
    """
    color_depth = calculate_color_depth(len(char_list))
    rgb_combinations = generate_rgb_combinations(color_depth)
    color_dict = {rgb_combinations[i]: char_list[i] for i in range(len(char_list))}
    return color_dict