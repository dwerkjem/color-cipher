import math
from PIL import Image
import numpy as np
import resources.values

values = resources.values.get_value()

def vec3_table_to_image(vec3_table, image_size:list[int], background_color=(0, 0, 0)):
    """
    Converts a table of vec3 values to an image of a specified size.
    
    :param vec3_table: List of vec3 values (RGB tuples).
    :param image_size: Tuple indicating the desired output image size (width, height).
    :param background_color: Background color as an RGB tuple.
    :return: PIL Image object.
    """
    num_colors = len(vec3_table)
    grid_size = math.ceil(math.sqrt(num_colors))
    pixel_size = image_size[0] // grid_size, image_size[1] // grid_size

    # Create a new image with the specified size and background color
    image = Image.new('RGB', image_size, color=background_color)

    for i, vec3 in enumerate(vec3_table):
        x = (i % grid_size) * pixel_size[0]
        y = (i // grid_size) * pixel_size[1]
        
        for dx in range(pixel_size[0]):
            for dy in range(pixel_size[1]):
                image.putpixel((x + dx, y + dy), (int(vec3[0]), int(vec3[1]), int(vec3[2])))

    return image
MAX_I = 255
colors = []
num_colors = len(values) ** 2
JUMP = MAX_I // round(num_colors ** (1/3))

def char_combos():
    chars = []
    for i in values:
        for j in values:
            chars.append((i+j))
    return chars

chars = char_combos()
red=0
green=0
blue=0
# map the chars to colors
for i in range(len(chars)):
    red = red + JUMP
    if red > MAX_I:
        red = 0
        green = green + JUMP
    if green > MAX_I:
        green = 0
        blue = blue + JUMP

    colors.append((red, green, blue))
    #print(chars[i], colors[i])

image = vec3_table_to_image(colors, (512, 512))
image.save('Grid.png')
