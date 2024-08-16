"""
This module contains the key grid for the encryption and decryption of the text.

The key grid is a 28x28 grid that maps characters to their corresponding positions in the grid. The grid is used to encode and decode text by mapping characters to their respective positions in the grid.

Functions:
- `encode(text)`: Encodes the text using the key grid.
- `decode(text)`: Decodes the text using the key grid.

Usage:
To encode text, use the `encode` function. To decode text, use the `decode` function.
"""

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
    "START-OF-NEW-KEY",
    "END-OF-KEY",
]


def chunker(text):
    """
    Split the text into characters and return a list of chunks.
    """
    i = 0
    while i < len(text):
        if text[i : i + 16] == "START-OF-NEW-KEY":
            yield text[i : i + 16]
            i += 16
        elif text[i : i + 10] == "END-OF-KEY":
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
        if text_chunks[i] == "START-OF-NEW-KEY":
            to_encrypt = ["START-OF-NEW-KEY"]
            i += 1

            # Collect the new key value within the "START-OF-NEW-KEY" and "END-OF-KEY" markers
            new_key = []
            while i < len(text_chunks) and text_chunks[i] != "END-OF-KEY":
                new_key.append(text_chunks[i])
                to_encrypt.append(text_chunks[i])
                i += 1
            to_encrypt.append("END-OF-KEY")
            i += 1  # Move past "END-OF-KEY"

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
            key_idx = to_encrypt.remove("START-OF-NEW-KEY")
            key_idx = to_encrypt.remove("END-OF-KEY")
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
    while i < len(text_chunks):
        text_idx = values.index(text_chunks[i])
        key_idx = values.index(key_expanded[i])
        new_idx = (text_idx - key_idx) % len(values)
        decrypted.append(values[new_idx])
        i += 1
        if values[new_idx] == "START-OF-NEW-KEY":
            print("START-OF-NEW-KEY")
            new_key = []
            while i < len(text_chunks) and text_chunks[i] != "END-OF-KEY":
                new_key.append(text_chunks[i])
                i += 1
            i += 1
            print("new_key", new_key)
            key_idx = "".join(new_key)
            key_expanded = expand_key(key_idx, text_chunks)
            continue

    return "".join(decrypted)


original_text = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaSTART-OF-NEW-KEY 55cEND-OF-KEYaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
key = "aaa"
encrypted_text = encrypt(original_text, key)

print("Original text:", original_text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypt(encrypted_text, key))

print("Original text == Decrypted text:", original_text == decrypt(encrypted_text, key))
