from PIL import Image
import os

def rgb_list_to_image(rgb_list, image_width, image_height):
    # Create a new image with the given width and height
    image = Image.new("RGB", (image_width, image_height))
    image.putdata(rgb_list)
    return image

def up_scale (image, scale):
    return image.resize((image.width*scale, image.height*scale))

def down_scale (image, scale):
    return image.resize((image.width//scale, image.height//scale))

def save_image(image, path="../../images/out.png"):
    image.save(path)

def load_image(path):
    return Image.open(path)