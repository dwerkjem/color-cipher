"""
This script generates a grid of Unicode characters to be used for encoding and decoding text.

The grid is a 93x93 matrix where the first row and column contain the full names of the characters, and the rest of the cells contain unique Unicode characters.

The script provides functions to encode and decode text using the grid.

Functions:
- `encode(text)`: Encodes the text using the grid.
- `decode(text)`: Decodes the text using the grid.
- `prepare_plain_text(text)`: Prepares the text for encoding by handling characters more appropriately.

Usage:
The script can be run from the command line with the following arguments:
- `f` or `t`: Indicates whether the input is from a file or text.
- The input text or file path.
- `e` or `d`: Indicates whether to encode or decode the text.
- `o`: Optional flag to specify an output file.
- The output file path.

Example:
To encode text from a file and save the output to a file:
```
python make_grid.py f input.txt e o output.txt
```
"""

import unicodedata
import sys
import numpy as np


# List of values provided
values = [
    " ",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
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
    "\n",
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
    "!",
    "?",
    "'",
    '"',
    ":",
    ";",
    "-",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "<",
    ">",
    "+",
    "=",
    "&",
    "%",
    "$",
    "#",
    "@",
    "*",
    "/",
    "\\",
    "|",
    "_",
    ]

# Create a grid of 93x93 (including headers)
grid = np.zeros((93, 93), dtype=object)

# Fill the grid from 1 to 92 column 0 with the values FULL name
for i in range(92):
    grid[i + 1, 0] = values[i]

# Fill the grid from 1 to 92 row 0 with the values full name
for i in range(92):
    grid[0, i + 1] = values[i]

import unicodedata
import numpy as np


# Initialize the starting codepoint
current_codepoint = 1  # Starting from the first Unicode code point

# Define a set of specific codepoints to skip
skip_codepoints = {
    0x061C,
    0x200E,
    0x200F,
    0x202A,
    0x202B,
    0x202C,
    0x202D,
    0x202E,
    0x2066,
    0x2067,
    0x2068,
    0x2069,
}

for i in range(1, 93):
    for j in range(1, 93):
        while True:
            try:
                # Skip specific codepoints
                if current_codepoint in skip_codepoints:
                    current_codepoint += 1
                    continue

                # Attempt to use the current codepoint
                char_name = unicodedata.name(chr(current_codepoint))

                grid[i, j] = chr(current_codepoint)
                current_codepoint += 1
                break  # Move to the next grid position
            except ValueError:
                # If the codepoint doesn't correspond to a named character, increment it and try again
                current_codepoint += 1


# save the grid to a txt file
with open("grid.txt", "w") as file:
    for i in range(93):
        for j in range(93):
            grid = np.array(grid, dtype=str)
            file.write(grid[i, j])
            file.write(" ")
        file.write("\n")

# Encoding function using the grid to encode the text
def encode(text):
    """
    Encode the text using the grid
    :param text: The text to encode
    :return: The encoded text
    """
    encoded_text = ""
    if len(text) % 2 != 0:
        text += " "  # Add a space if the text length is odd
    for i in range(0, len(text), 2):
        row_char = text[i]
        col_char = text[i + 1]
        for j in range(1, 93):
            if grid[j, 0] == row_char:
                for k in range(1, 93):
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
        for i in range(1, 93):
            for j in range(1, 93):
                if grid[i, j] == char:
                    decoded_text += grid[i, 0] + grid[0, j]
                    break
    return decoded_text.strip()


def prepare_plain_text(text):
    """
    Prepare the text for encoding by handling characters more appropriately.
    :param text: The text to prepare.
    :return: The prepared text.
    """
    prepared_text = ""
    for char in text:
        if char in values:
            prepared_text += char
        elif char.isalpha():
            prepared_text += char.lower()
        elif char == " ":
            prepared_text += char  # Preserve spaces if needed
        elif char.isdigit():
            prepared_text += f" {char} "
        elif char in [".", ",", "`"]:
            prepared_text += f" {char} "

        else:
            try:
                # Get the full Unicode name, handling special cases
                char_name = unicodedata.name(char)
                simplified_name = char_name.lower().replace(" ", "_")
                prepared_text += f" {simplified_name} "
            except ValueError:
                pass  # Skip characters that don't have a Unicode name
    return prepared_text

if __name__ == "__main__":

    args = sys.argv[1:]

    if len(args) == 0:
        print(
            "Usage: python make_grid.py [f | t] [text or file] [e | d] [o ] [output file]"
        )
        sys.exit(1)

    if args[0] == "f":
        with open(args[1], "r") as file:
            text = file.read()
    else:
        text = args[1]


    if args[2] == "e":
        encoded_text = encode(prepare_plain_text(text))
        if len(args) > 3 and args[3] == "o":
            with open(args[4], "w") as file:
                file.write(encoded_text)
        else:
            print(encoded_text)

    if args[2] == "d":
        decoded_text = decode(text)
        if len(args) > 3 and args[3] == "o":
            with open(args[4], "w") as file:
                file.write(decoded_text)
        else:
            print(decoded_text)

    if len(args) > 3 and args[3] == "o":
        with open(args[4], "w") as file:
            file.write(encoded_text)
        print(encoded_text)
