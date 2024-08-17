"""
This module contains the key grid for the encryption and decryption of the text.

The key grid is a 28x28 grid that maps characters to their corresponding positions in the grid. The grid is used to encode and decode text by mapping characters to their respective positions in the grid.

Functions:
- `encode(text)`: Encodes the text using the key grid.
- `decode(text)`: Decodes the text using the key grid.

Usage:
To encode text, use the `encode` function. To decode text, use the `decode` function.
"""

import sys
import random
import unicodedata

values = [
    " ",
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
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "newline",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ".",
    ",",
    "`",
    "S",  # Start of key
    "E",  # End of key
]


def chunker(text):
    """
    Split the text into characters and return a list of chunks.
    """
    i = 0
    while i < len(text):
        if text[i : i + 16] == "S":
            yield text[i : i + 16]
            i += 16
        elif text[i : i + 10] == "E":
            yield text[i : i + 10]
            i += 10
        elif text[i : i + 7] == "newline":
            yield text[i : i + 7]
            i += 7
        else:
            yield text[i]
            i += 1


def expand_key(key, text):
    """
    Expand the key to fit the text length.
    """
    return key * (len(text) // len(key)) + key[: len(text) % len(key)]


def gen_key(length):
    """
    Generate a key for the text.
    """
    key = []
    for _ in range(length):
        key.append(random.choice(values[0:-2]))
    return "".join(key)


def insert_key(text, count, key_length=16):
    """
    Insert a new key into the text every `count` characters.

    Parameters:
    - text (str): The text where the key will be inserted.
    - count (int): The number of characters between each key insertion.
    - key_length (int): The length of the key to generate.

    Returns:
    - str: The text with the inserted keys.
    """
    # Convert the text to a list to allow insertion of keys
    text = list(text)
    i = 0

    while i < len(text):
        # Generate a new random key for each insertion
        key = gen_key(key_length)
        wrapped_key = "S" + key + "E"

        # Insert the key at the current position
        text.insert(i, wrapped_key)

        # Move the index forward by the count and the length of the inserted key
        i += count + len(wrapped_key)

    # Convert the list back to a string and return it
    return "".join(text)


def encrypt(text, key):
    """
    Encrypt the text using a key grid.
    """
    key_chunks = list(chunker(key))
    text_chunks = list(chunker(text))

    # Fit the key into the text
    key_expanded = expand_key(key_chunks, text_chunks)

    encrypted = []
    i = 0

    while i < len(text_chunks):
        if text_chunks[i] == "S":
            to_encrypt = ["S"]
            i += 1

            # Collect the new key value within the "S" and "E" markers
            new_key = []
            while i < len(text_chunks) and text_chunks[i] != "E":
                new_key.append(text_chunks[i])
                to_encrypt.append(text_chunks[i])
                i += 1
            to_encrypt.append("E")
            i += 1  # Move past "E"

            # Encrypt the to_encrypt list without recursion
            for chunk in to_encrypt:
                if chunk in values:
                    text_idx = values.index(chunk)
                    key_idx = values.index(
                        key_expanded[i - len(to_encrypt) + to_encrypt.index(chunk)]
                    )
                    new_idx = (text_idx + key_idx) % len(values)
                    encrypted.append(values[new_idx])
                else:
                    encrypted.append(chunk)
            key_idx = to_encrypt.remove("S")
            key_idx = to_encrypt.remove("E")
            key_idx = "".join(to_encrypt)
            key_expanded = expand_key(key_idx, text_chunks)
            continue
        # Encrypt using the current key
        text_idx = values.index(text_chunks[i])
        key_idx = values.index(key_expanded[i])
        new_idx = (text_idx + key_idx) % len(values)
        encrypted.append(values[new_idx])
        i += 1

    return "".join(encrypted)


def decrypt(text, key):
    """
    Decrypt the text using a key grid.
    """
    key_chunks = list(chunker(key))
    text_chunks = list(chunker(text))

    # Fit the key into the text
    key_expanded = expand_key(key_chunks, text_chunks)

    decrypted = []
    i = 0
    new_key = []
    while i < len(text_chunks):
        append = False
        if not new_key:
            text_idx = values.index(text_chunks[i])
            key_idx = values.index(key_expanded[i])
            new_idx = (text_idx - key_idx) % len(values)
            decrypted.append(values[new_idx])
        else:
            # expand the new key
            new_key_expanded = expand_key(new_key, text_chunks)
            text_idx = values.index(text_chunks[i])
            key_idx = values.index(new_key_expanded[i])
            new_idx = (text_idx - key_idx) % len(values)

        if new_idx == values.index("S"):

            append = True
        while append:

            if values[new_idx] == "E":
                append = False
                break
            i += 1
            new_key.append(values[new_idx])
            text_idx = values.index(text_chunks[i])
            key_idx = values.index(key_expanded[i])
            new_idx = (text_idx - key_idx) % len(values)
            decrypted.append(values[new_idx])
        if new_key:
            try:
                new_key.remove("S")

            except ValueError:
                pass

            if len(new_key) > len(text_chunks):
                new_key = new_key[: len(text_chunks)]
            print(new_key)
            key_expanded = expand_key(new_key, text_chunks)
            new_key = []

        i += 1
    return "".join(decrypted)


def parse_text(text):
    """
    Parse the text to replace special characters with their names.
    """
    for char in text:
        if char == "\n":
            yield "newline"
        elif char in values:
            yield f"{char}"

        elif char.lower() in values:
            yield f"{char.lower()}"
        else:
            try:
                char_name = unicodedata.name(char)
                simplified_name = char_name.lower().replace("-", " ")
                yield f"{simplified_name}"
            except ValueError:
                pass


arguments = sys.argv[1:]

if len(arguments) < 2:
    print(
        "Usage: python key_grid.py [f | t] [text or file] [key] [e | d] [o | v | ov] [output file]"
    )
    sys.exit(1)

if arguments[0] == "f":
    with open(arguments[1], "r") as file:
        text = file.read()
else:
    text = arguments[1]

text = list(parse_text(text=text))
text = "".join(text).lower()


key = arguments[2]

if arguments[3] == "e":
    text = insert_key(text, 10)
    encrypted_text = encrypt(text, key)
    if len(arguments) > 4 and arguments[4] == "o":
        with open(arguments[5], "w") as file:
            file.write(encrypted_text)
    else:
        print(encrypted_text)

if arguments[3] == "d":
    decrypted_text = decrypt(text, key)
    if len(arguments) > 4 and arguments[4] == "o":
        with open(arguments[5], "w") as file:
            file.write(decrypted_text)
    else:
        print(decrypted_text)

if len(arguments) > 4 and arguments[4] == "o":
    with open(arguments[5], "w") as file:
        file.write(encrypted_text)
    print(encrypted_text)
