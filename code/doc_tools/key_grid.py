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
    "S",
    "E",
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


original_text = input("Enter the text to encrypt: ").lower()
key = input("Enter the encryption key: ").lower()


encrypted_text = encrypt(original_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Original Text:", original_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

if original_text == decrypted_text:
    print("Decryption successful!")
else:
    print("Decryption failed!")
