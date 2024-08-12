import random
import hashlib

from table_of_values import key_freq_dict
from key_system import (
    weightedRandomChoice,
    generateKey,
    hashKey,
    hash_to_ascii_art_pyramid,
)


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


def test_generateKey_seeded():
    random.seed(0)
    key_length = 10
    key = generateKey(key_length)
    expected_key = "tsienisglo"  # based on random.seed(0)

    assert key == expected_key


def test_hashKey():
    key = "test_key"
    hashed_key = hashKey(key)
    expected_hashed_key = hashlib.sha256(key.encode()).hexdigest()

    assert hashed_key == expected_hashed_key


def test_hash_to_ascii_art_pyramid():
    hash_str = "01234567"
    ascii_art = hash_to_ascii_art_pyramid(hash_str)
    expected_ascii_art = "  @  \n @%% \n #**+"

    assert (
        ascii_art == expected_ascii_art
    ), f"Expected:\n{expected_ascii_art}\nGot:\n{ascii_art}"
