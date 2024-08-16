import numpy as np
import unicodedata

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
