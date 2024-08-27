"""
makes a grid of characters and saves it as an image

Usage: python make_grid.py
"""

import numpy as np
import matplotlib.pyplot as plt

from values import get_value as list_of_values

# List of values provided
values = list_of_values()

GRID_SIZE = len(values)
GRID = np.zeros((GRID_SIZE, GRID_SIZE, 3), dtype=np.uint8)

# Create a grid of colors
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        GRID[i, j] = [(i * 10) % 256, (j * 5) % 256, ((i + j) * 7) % 256]

# Increase figure size to accommodate text
plt.figure(figsize=(20, 20))  # Adjust as needed for your display

# Display the grid
plt.imshow(GRID)

# Set the title and axis labels
plt.title("Character Grid", fontsize=18)
plt.xlabel("Character Index", fontsize=14)
plt.ylabel("Character Index", fontsize=14)

# Set the x and y ticks with reduced font size
plt.xticks(range(GRID_SIZE), values, rotation=90, fontsize=8)
plt.yticks(range(GRID_SIZE), values, fontsize=8)

# Adjust layout to prevent clipping of tick labels
plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

# Save the grid as an image with adjusted padding
plt.savefig("grid.png", bbox_inches="tight", pad_inches=0.5)
