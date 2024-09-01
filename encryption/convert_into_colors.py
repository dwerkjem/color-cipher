import math
from PIL import Image
import resources.values
import os
import itertools

# Load the values
values = resources.values.get_value()

# Generate color and character mappings
MAX_I = 255
num_colors = len(values) ** 2

# Calculate grid size based on num_colors
grid_size = math.ceil(num_colors ** (1 / 3))  # Always round up to ensure enough colors

# Generate evenly spread colors using a 3D grid
def generate_even_colors(grid_size, max_value):
    step = max_value // (grid_size - 1) if grid_size > 1 else max_value
    colors = [(r * step, g * step, b * step) for r, g, b in itertools.product(range(grid_size), repeat=3)]
    return colors

colors = generate_even_colors(grid_size, MAX_I)

# Ensure the number of colors matches the number of character pairs
if len(colors) < num_colors:
    raise ValueError("Generated fewer colors than required. Adjust the grid size or number of values.")
elif len(colors) > num_colors:
    colors = colors[:num_colors]  # Trim excess colors

# Generate character combinations
def char_combos():
    chars = []
    for i in values:
        for j in values:
            chars.append(i + j)
    return chars

chars = char_combos()

# Create color dictionary
color_dict = {chars[i]: colors[i] for i in range(len(chars))}

# Create reverse color dictionary for efficient lookup in convert_to_text
reverse_color_dict = {v: k for k, v in color_dict.items()}

def find_optimal_dimensions_and_pad_text(text: str, min_dimension: int = None) -> tuple[str, tuple[int, int]]:
    """
    Finds the optimal dimensions (width, height) for an image that can fit all colors,
    by finding the closest factors of num_colors. If no factor greater than min_dimension is found,
    pads the text with spaces until suitable dimensions are found.

    :param text: The input text.
    :param min_dimension: The minimum dimension for width and height. If None, it will be dynamically calculated.
    :return: The padded text and a tuple (width, height) representing the dimensions of the image.
    """
    num_colors = len(text) // 2  # Each color represents 2 characters

    if min_dimension is None:
        min_dimension = max(10, int(math.sqrt(num_colors) // 2))  # Dynamically set min_dimension

    while True:
        for width in range(int(math.sqrt(num_colors)), 0, -1):
            if num_colors % width == 0 and width >= min_dimension and num_colors // width >= min_dimension:
                height = num_colors // width
                return text, (width, height)
        # No suitable factor found, pad the text with spaces
        text += " "
        num_colors = len(text) // 2

def vec3_table_to_image(vec3_table, image_size: tuple[int, int], background_color=(0, 0, 0)):
    """
    Converts a table of vec3 values to an image of a specified size, where each color occupies exactly one pixel.
    
    :param vec3_table: List of vec3 values (RGB tuples).
    :param image_size: Tuple indicating the desired output image size (width, height).
    :param background_color: Background color as an RGB tuple.
    :return: PIL Image object.
    """
    image = Image.new('RGB', image_size, color=background_color)

    grid_width = min(len(vec3_table), image_size[0])
    grid_height = (len(vec3_table) + grid_width - 1) // grid_width

    if grid_height > image_size[1]:
        raise ValueError("Image size is too small to fit all the colors as individual pixels.")

    for i, vec3 in enumerate(vec3_table):
        x = i % grid_width
        y = i // grid_width
        image.putpixel((x, y), (int(vec3[0]), int(vec3[1]), int(vec3[2])))

    return image

def convert_to_colors(text: str):
    """
    Converts a string to a list of colors.
    
    :param text: The input text.
    :return: List of colors.
    """
    if len(text) % 2 != 0:
        text += values[0]  # Pad with the first value if odd length

    return [color_dict[text[i:i+2]] for i in range(0, len(text), 2)]

def convert_to_image(text_or_file: str, file: str = None, background_color=(0, 0, 0)):
    """
    Converts a string or text from a file to an image, automatically determining the optimal size.
    
    :param text_or_file: The input text or the file path containing the text.
    :param file: File name to save the image.
    :param background_color: Background color as an RGB tuple.
    :return: PIL Image object.
    """
    if os.path.exists(text_or_file):
        with open(text_or_file, "r") as f:
            text = f.read()
    else:
        text = text_or_file
    
    padded_text, (width, height) = find_optimal_dimensions_and_pad_text(text)
    colors = convert_to_colors(padded_text)
    image = vec3_table_to_image(colors, (width, height), background_color)

    if not os.path.exists("out"):
        os.mkdir("out")
    
    if file:
        image.save(f"out/{file}" if file.endswith('.png') else f"out/{file}.png")
    else:
        image.show()

def convert_to_text(image: Image) -> str:
    """
    Converts an image to a string.
    
    :param image: The input image.
    :return: The output text.
    """
    text = ""
    for y in range(image.height):
        for x in range(image.width):
            color = image.getpixel((x, y))
            text += reverse_color_dict.get(color, '')  # Use the reverse dictionary for efficient lookup
    return text.strip()  # Remove any padding spaces added during encryption

def convert_to_text_from_file(file: str) -> str:
    """
    Converts an image to a string from a file.
    
    :param file: The input image file.
    :return: The output text.
    """
    image = Image.open(file)
    return convert_to_text(image)

def make_all_chars_image():
    """
    Creates an image with all possible character combinations.
    """
    text = "".join(chars)
    convert_to_image(text, "all_chars.png")

make_all_chars_image()