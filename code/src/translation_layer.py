"""
This module provides functions for generating an image from text using a color dictionary.

Functions:
- color_similarity: Calculate the similarity between two colors.
- chose_color: Chooses a color that corresponds to a character from a color dictionary and is closest to the original color.
- generate_image_from_text: Generates an image from text using a color dictionary while preserving the look of the input image.

Modules:
- math: Provides mathematical functions.
- PIL: Provides functions for image processing.
- numpy: Provides functions for numerical processing.

Usage:
The generate_image_from_text function can be used to generate an image from text using a color dictionary while preserving the look of the input image.

Example:
color_dict = {
    "a": [(0, 0, 0), (0, 0, 1), (0, 0, 2)],
    "b": [(0, 1, 0), (0, 1, 1), (0, 1, 2)],
    "c": [(0, 2, 0), (0, 2, 1), (0, 2, 2)]
}
text = "abc"
input_image = "input.png"
output_image = "output.png"
average_diff = generate_image_from_text(text, color_dict, input_image, output_image)
print(average_diff)

"""

import math

from code.src.text_to_color import calculate_color_depth

from PIL import Image
import numpy as np


OUTPUT_DIR = "output"


def color_similarity(color1, color2, max_value):
    """
    Calculate the similarity between two colors.

    Args:
        color1 (tuple): The first color as an (R, G, B) tuple.
        color2 (tuple): The second color as an (R, G, B) tuple.
        max_value (int): The maximum value for each color component.

    Returns:
        float: The similarity between the two colors as a float between 0 and 1.
    """
    if len(color1) != 3 or len(color2) != 3:
        raise ValueError("Both colors must be tuples of length 3.")

    # Calculate the Euclidean distance between the two colors
    distance = math.sqrt(
        (color1[0] - color2[0]) ** 2
        + (color1[1] - color2[1]) ** 2
        + (color1[2] - color2[2]) ** 2
    )

    # Normalize the distance to a range of 0 to 1
    max_distance = math.sqrt(3 * (max_value**2))
    similarity = 1 - (distance / max_distance)

    return similarity


def chose_color(color_dict, char, original_color):
    """
    Chooses a color that corresponds to a character from a color dictionary and is closest to the original color.

    Args:
        color_dict (dict): A dictionary mapping characters to colors.
        char (str): The character to choose a color for.
        original_color (tuple): The original color to match.

    Returns:
        tuple: The color corresponding to the character that is closest to the original color.
    """
    if len(original_color) != 3:
        raise ValueError("The original color must be a tuple of length 3.")
    max_value = calculate_color_depth(len(color_dict))
    # Get the colors that correspond to the character
    colors = color_dict[char]

    # Find the color that is closest to the original color
    best_color = None
    best_similarity = 0
    for color in colors:
        similarity = color_similarity(color, original_color, max_value)
        if similarity > best_similarity:
            best_similarity = similarity
            best_color = color

    return best_color


def generate_image_from_text(
    text, color_dict, input_image, output_image=f"{OUTPUT_DIR}/output.png"
):
    """
    Generates an image from text using a color dictionary while preserving the look of the input image.

    Args:
        text (str): The text to convert to an image.
        color_dict (dict): A dictionary mapping characters to colors.
        input_image (str): The path to the input image.
        output_image (str): The path to save the output image.

    Returns:
        float: The average color difference between the input and output images.
    """

    # Load the input image
    input_img = Image.open(input_image)
    input_data = np.array(input_img)

    # Get the dimensions of the input image
    height, width, _ = input_data.shape

    # Create a new image to store the output
    output_data = np.zeros((height, width, 3), dtype=np.uint8)

    # Iterate over the text and generate the output image
    index = 0
    total_diff = 0
    for y in range(height):
        for x in range(width):
            char = text[index % len(text)]
            original_color = input_data[y, x]
            new_color = chose_color(color_dict, char, original_color)
            output_data[y, x] = new_color
            total_diff += color_similarity(original_color, new_color, 255)
            index += 1
    # Save the output image
    output_img = Image.fromarray(output_data)
    output_img.save(output_image)
    # Calculate the average color difference
    average_diff = total_diff / (height * width)

    return average_diff
