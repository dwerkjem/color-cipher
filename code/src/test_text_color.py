"""
Unit tests for the test_text_to_color module functions.

These tests cover the following functions:
1. distribute_characters: Distributes characters based on their frequency ratio.
2. decrease_resolution_of_dict: Decreases the resolution of a frequency dictionary to a specified maximum resolution.
3. calculate_color_depth: Calculates the color depth needed for a given number of colors.
4. get_channel_range: Returns the range of values for each color channel based on the color depth.
5. generate_rgb_combinations: Generates all possible RGB combinations for a given color depth.
6. char_list_to_color_dict: Maps a list of characters to RGB color combinations.
7. stress_test_char_list_to_color_dict: A stress test for the char_list_to_color_dict function using a large frequency dictionary.

Functions:
- test_distribute_characters: Tests the distribution of characters based on their frequency ratio.
- test_decrease_resolution_of_dict_correctly: Tests the decrease in resolution of a frequency dictionary.
- test_calculate_color_depth: Tests the calculation of color depth.
- test_get_channel_range: Tests the retrieval of the range of values for each color channel.
- test_generate_rgb_combinations: Tests the generation of RGB combinations for different color depths.
- test_char_list_to_color_dict: Tests the mapping of a character list to RGB color combinations.
- test_stress_test_char_list_to_color_dict: Performs a stress test on the char_list_to_color_dict function using a large frequency dictionary.

Modules:
- textToColor: Contains functions for processing character frequencies and mapping them to colors.
"""

from text_to_color import (
    distribute_characters,
    decrease_resolution_of_dict,
    calculate_color_depth,
    get_channel_range,
    generate_rgb_combinations,
    char_list_to_color_dict,
)


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
    distribution = ["a", "b", "c", "d", "e", "f", "g", "h"]
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
    firstFifty = (
        (0, 0, 0),
        (0, 0, 1),
        (0, 0, 2),
        (0, 0, 3),
        (0, 0, 4),
        (0, 0, 5),
        (0, 0, 6),
        (0, 0, 7),
        (0, 0, 8),
        (0, 0, 9),
        (0, 0, 10),
        (0, 0, 11),
        (0, 0, 12),
        (0, 0, 13),
        (0, 0, 14),
        (0, 0, 15),
        (0, 0, 16),
        (0, 0, 17),
        (0, 0, 18),
        (0, 0, 19),
        (0, 0, 20),
        (0, 0, 21),
        (0, 0, 22),
        (0, 0, 23),
        (0, 0, 24),
        (0, 0, 25),
        (0, 0, 26),
        (0, 0, 27),
        (0, 0, 28),
        (0, 0, 29),
        (0, 0, 30),
        (0, 0, 31),
        (0, 0, 32),
        (0, 0, 33),
        (0, 0, 34),
        (0, 0, 35),
        (0, 0, 36),
        (0, 0, 37),
        (0, 0, 38),
        (0, 0, 39),
        (0, 0, 40),
        (0, 0, 41),
        (0, 0, 42),
        (0, 0, 43),
        (0, 0, 44),
        (0, 0, 45),
        (0, 0, 46),
        (0, 0, 47),
        (0, 0, 48),
        (0, 0, 49),
    )

    expected = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "e",
        "n",
        "o",
        "p",
        "q",
        "r",
        "o",
        "s",
        "t",
        "a",
        "i",
        "n",
        "t",
        "e",
        "r",
        "s",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "0",
        "l",
        "t",
        "1",
        "o",
        "e",
        "h",
        "2",
        "3",
        "a",
        "d",
        "n",
        "i",
        "4",
        "5",
    ]
    for i, color in enumerate(firstFifty):
        assert color in color_dict, f"Color {color} not found in color_dict"
        assert (
            color_dict[color] == expected[i]
        ), f"Expected {expected[i]} at color {color}, but got {color_dict[color]}"
