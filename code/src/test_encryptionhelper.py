from textToColor import *

def test_distribute_characters():
    char_ratio = {"a": 2, "b": 3, "c": 5}
    L = 20
    result = distribute_characters(char_ratio, L)
    expected_result = [
        "a",
        "b",
        "c",
        "b",
        "c",
        "a",
        "b",
        "c",
        "c",
        "c",
        "a",
        "b",
        "c",
        "b",
        "c",
        "a",
        "b",
        "c",
        "c",
        "c",
    ]
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_decrease_resolution_of_dict_correctly():
    dictionary = {"a": 100, "b": 200, "c": 300}
    maxResolution = 150
    result = decrease_resolution_of_dict(dictionary, maxResolution)
    expected_result = {"a": 25, "b": 50, "c": 75}
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_calculate_color_depth():
    total_colors = 16777216
    result = calculate_color_depth(total_colors)
    expected_result = 8
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_get_channel_range():
    color_depth = 8
    result = get_channel_range(color_depth)
    expected_result = 256
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_generate_rgb_combinations():
    color_depth = 1
    result = generate_rgb_combinations(color_depth)
    expected_result = [
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    ]
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    color_depth = 2
    result = generate_rgb_combinations(color_depth)
    expected_result = [(r, g, b) for r in range(4) for g in range(4) for b in range(4)]
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_char_list_to_color_dict():
    distribution = [ "a", "b", "c", "d", "e", "f", "g", "h"]
    expected_result = {
        (0, 0, 0): "a",
        (0, 0, 1): "b",
        (0, 1, 0): "c",
        (0, 1, 1): "d",
        (1, 0, 0): "e",
        (1, 0, 1): "f",
        (1, 1, 0): "g",
        (1, 1, 1): "h",
    }
    result = char_list_to_color_dict(distribution)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

def test_stress_test_char_list_to_color_dict():
    # Using the provided freq_dict
    freq_dict = {
        "a": 123287,
        "b": 24227,
        "c": 50211,
        "d": 59577,
        "e": 203824,
        "f": 32616,
        "g": 37064,
        "h": 65217,
        "i": 116488,
        "j": 2061,
        "k": 16047,
        "l": 75450,
        "m": 39060,
        "n": 118108,
        "o": 137119,
        "p": 36791,
        "q": 1774,
        "r": 101201,
        "s": 103814,
        "t": 151376,
        "u": 49901,
        "v": 20109,
        "w": 30974,
        "x": 4635,
        "y": 26924,
        "z": 1417,
        "0": 13109,
        "1": 10916,
        "2": 7894,
        "3": 4389,
        "4": 3204,
        "5": 3951,
        "6": 2739,
        "7": 2448,
        "8": 2505,
        "9": 2433,
        " ": 407934,
        "END OF LINE": 49492,
        "END OF TEXT": 4,
        "START OF TEXT": 4,
        "blank": 136,
        "START OF NEW KEY": 1,
        "END OF NEW KEY": 1,
        "UPPERCASE": 386403,
        "START OF SYMBOL": 105362,
        "END OF SYMBOL": 105362,
    }
    distribution = distribute_characters(freq_dict, 16777216)
    assert (
        len(distribution) == 16777216
    ), f"Expected 16777216 items in distribution, but got {len(distribution)}"
    color_dict = char_list_to_color_dict(distribution)
    assert (
        len(color_dict) == 16777216
    ), f"Expected 16777216 colors, but got {len(color_dict)}"