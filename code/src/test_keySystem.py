from tableOfValues import key_freq_dict
from keySystem import weightedRandomChoice, generateKey
import random


def test_weightedRandomChoice():
    random.seed(0)
    choices = {"a": 1, "b": 2, "c": 3}
    result = weightedRandomChoice(choices, 5)
    expected_result = [
        "c",
        "c",
        "b",
        "b",
        "c",
    ]  # based on random.seed(0)

    assert result == expected_result


def test_generateKey_length():
    key_length = 10
    key = generateKey(key_length)
    assert len(key) == key_length


def test_generateKey_characters():
    key_length = 50
    key = generateKey(key_length)
    valid_chars = set(key_freq_dict().keys())
    for char in key:
        assert char in valid_chars


def test_generateKey_mocked():
    random.seed(0)
    key_length = 10
    key = generateKey(key_length)
    expected_key = "tsienisglo"  # based on random.seed(0)

    assert key == expected_key
