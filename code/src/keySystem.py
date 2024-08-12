import random
import hashlib
from tableOfValues import key_freq_dict


def weightedRandomChoice(choices: dict, amount: int) -> list:
    """
    Given a dictionary of choices and their weights, this function will return a list of choices based on their weights.
    """
    total = sum(choices.values())
    result = []
    for _ in range(amount):
        r = random.uniform(0, total)
        upto = 0
        for c, w in choices.items():
            upto += w
            if upto > r:
                result.append(c)
                break
    return result


def generateKey(key_length: int) -> str:
    """
    Given a key length, this function will generate a key based on the key_freq_dict.
    """
    return "".join(weightedRandomChoice(key_freq_dict(), key_length))


def hashKey(key: str) -> str:
    """
    Given a key, this function will hash the key using SHA-256 and return the hexadecimal digest.
    """
    sha256 = hashlib.sha256()
    sha256.update(key.encode())
    return sha256.hexdigest()


def hash_to_ascii_art_pyramid(hash_str):
    """
    Converts a hash string to ASCII art in a centered pyramid shape.
    """
    # Define a set of ASCII characters to map to
    ascii_chars = "@%#*+=-:. "
    scale = len(ascii_chars) - 1

    # Convert each hex digit to an integer and map to an ASCII character
    ascii_art = [ascii_chars[int(char, 16) * scale // 15] for char in hash_str]

    # Calculate the number of levels in the pyramid
    n = 1
    while (n * (n + 1)) // 2 <= len(ascii_art):
        n += 1
    n -= 1

    # Arrange the ASCII art in a centered pyramid shape
    pyramid_art = []
    index = 0
    max_width = n * 2 - 1
    for i in range(1, n + 1):
        level_length = i * 2 - 1
        level_art = ascii_art[index : index + level_length]
        centered_level_art = "".join(level_art).center(max_width)
        pyramid_art.append(centered_level_art)
        index += level_length

    return "\n".join(pyramid_art)
