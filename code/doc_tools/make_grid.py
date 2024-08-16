"""
This script generates a grid of characters to be used for encoding and decoding text.
The grid is saved to a file called grid.txt, and the encoding and decoding functions are provided.
The encoding function takes a string of characters and encodes them using the grid.
The decoding function takes an encoded string and decodes it using the grid.
"""

import unicodedata

import numpy as np


# List of values provided
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
]

# Create a grid of 27x27
grid = np.zeros((27, 27), dtype=object)

# Fill the grid from 1 to 27 column 0 with the values FULL name
for i in range(27):
    grid[i, 0] = values[i]

# Fill the grid from 1 to 27 row 0 with the values full name
for i in range(27):
    grid[0, i] = values[i]

# Generate unique values for the grid, starting with the codepoint 0x1F000
current_codepoint = 0x1F000

for i in range(1, 27):
    for j in range(1, 27):
        while True:
            try:
                # Attempt to use the current codepoint
                char_name = unicodedata.name(chr(current_codepoint))
                grid[i, j] = chr(current_codepoint)
                current_codepoint += 1
                break  # Move to the next grid position
            except ValueError:
                # If the codepoint doesn't correspond to a named character, increment it and try again
                current_codepoint += 1

# Format the grid with padding and | separators
formatted_grid = []
for row in grid:
    formatted_row = " | ".join([f"{str(cell):^5}" for cell in row])
    formatted_grid.append(f"| {formatted_row} |")

# Save the formatted grid to a file
with open("grid.txt", "w") as file:
    for line in formatted_grid:
        file.write(line + "\n")


# Encoding function using the grid to encode the text
def encode(text):
    """
    Encode the text using the grid
    :param text: The text to encode
    :return: The encoded text
    """
    encoded_text = ""
    if len(text) % 2 != 0:
        text += " "
    for i in range(0, len(text), 2):
        row_char = text[i]
        col_char = text[i + 1]
        for j in range(1, 27):
            if grid[j, 0] == row_char:
                for k in range(1, 27):
                    if grid[0, k] == col_char:
                        encoded_text += grid[j, k]
                        break
                break
    return encoded_text


def decode(text):
    """
    Decode the text using the grid
    :param text: The text to decode
    :return: The decoded text
    """
    decoded_text = ""
    for char in text:
        for i in range(1, 27):
            for j in range(1, 27):
                if grid[i, j] == char:
                    decoded_text += grid[i, 0] + grid[0, j]
                    break
    return decoded_text


# Test the encoding and decoding functions
text = input("Enter the text to encode: ")
encoded_text = encode(text)
# Print the encoded text with a tab character between each character
print("\t".join(encoded_text))
decoded_text = decode(encoded_text)
print(f"Decoded text: {decoded_text}")
