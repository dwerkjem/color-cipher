from encryptionHelper import *

def test_distribute_characters():
    char_ratio = {"a": 2, "b": 3, "c": 5}  # 10 total
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
    # Test for 1-bit color depth
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

    # Test for 2-bit color depth
    color_depth = 2
    result = generate_rgb_combinations(color_depth)
    expected_result = [(r, g, b) for r in range(4) for g in range(4) for b in range(4)]
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

    print("All tests passed!")

def test_char_list_to_color_dict():
    char_list = ["a", "b", "c"]
    result = char_list_to_color_dict(char_list)
    expected_result = {"a": (0, 0, 0), "b": (0, 0, 1), "c": (0, 1, 0)}
    assert result == expected_result, f"Expected {expected_result}, but got {result}"