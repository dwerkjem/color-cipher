"""
Unit tests for key_system.py

These tests cover the following functions:
1. weighted_random_choice: Returns a list of choices based on their weights.
2. generate_key: Generates a key based on the key_freq_dict.
3. hash_key: Hashes a key using SHA-256.
4. hash_to_ascii_art_pyramid: Converts a hash string to ASCII art in a centered pyramid shape.

Functions:
- test_weightedRandomChoice: Tests the selection of items from a dictionary based on their weights.
- test_generateKey_length: Tests the generation of a key of a specified length.
- test_generateKey_characters: Tests the generation of a key with valid characters.
- test_generateKey_seeded: Tests the generation of a key with a seeded random number generator.
- test_hashKey: Tests the hashing of a key using SHA-256.
- test_hash_to_ascii_art_pyramid: Tests the conversion of a hash string to ASCII art in a centered pyramid shape.

Modules:
- random: Provides functions for generating random numbers.
- hashlib: Provides functions for hashing data.
- table_of_values: Contains the key_freq_dict dictionary.

Usage:
To run the tests, run `pytest code/src/test_key_system.py` from the root directory.
"""

import random
import hashlib

from src.table_of_values import key_freq_dict
from src.key_system import (
    weighted_random_choice,
    generate_key,
    hash_key,
    hash_to_ascii_pyramid,
)


def test_weightedRandomChoice():
    """
    Test the selection of items from a dictionary based on their weights.
    """
    random.seed(0)
    choices = {"a": 1, "b": 2, "c": 3}
    result = weighted_random_choice(choices, 5)
    expected_result = [
        "c",
        "c",
        "b",
        "b",
        "c",
    ]  # based on random.seed(0)

    assert result == expected_result


def test_generateKey_length():
    """
    Test the generation of a key of a specified length.
    """
    key_length = 10
    key = generate_key(key_length)
    assert len(key) == key_length


def test_generateKey_characters():
    """
    Test the generation of a key with valid characters.
    """
    key_length = 50
    key = generate_key(key_length)
    valid_chars = set(key_freq_dict().keys())
    for char in key:
        assert char in valid_chars


def test_generateKey_seeded():
    """
    Test the generation of a key with a seeded random number generator.
    """
    random.seed(0)
    key_length = 10
    key = generate_key(key_length)
    expected_key = "tsienisglo"  # based on random.seed(0)

    assert key == expected_key


def test_hashKey():
    """
    Test the hashing of a key using SHA-256.
    """
    key = "test_key"
    hashed_key = hash_key(key)
    expected_hashed_key = hashlib.sha256(key.encode()).hexdigest()

    assert hashed_key == expected_hashed_key


def test_hash_to_ascii_art_pyramid():
    """
    Test the conversion of a hash string to ASCII art in a centered pyramid shape.
    """
    hash_str = "01234567"
    ascii_art = hash_to_ascii_pyramid(hash_str)
    expected_ascii_art = "  @  \n @%% \n #**+"

    assert (
        ascii_art == expected_ascii_art
    ), f"Expected:\n{expected_ascii_art}\nGot:\n{ascii_art}"


if __name__ == "__main__":
    print(__doc__)
