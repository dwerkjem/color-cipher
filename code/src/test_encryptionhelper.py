from encryptionHelper import *

def test_distribute_characters_correctly():
    char_ratio = {"a": 2, "b": 3, "c": 5}  # 10 total
    L = 10
    result = distribute_characters(char_ratio, L)
    expected_result = ["a", "c", "b", "c", "c", "a", "b", "c", "c", "b"]
    assert result == expected_result, f"Expected {expected_result}, but got {result}"
    print("Test passed!")
