from PIL import Image
import sys


def downscale_image(input_path, output_path, new_width, new_height):
    """
    Downscale an image to the specified dimensions and save it as a PNG.

    Args:
        input_path (str): The path to the input image.
        output_path (str): The path to save the downscaled image.
        new_width (int): The width of the downscaled image.
        new_height (int): The height of the downscaled image.
    """
    # Open the input image
    with Image.open(input_path) as img:
        # Downscale the image
        downscaled_img = img.resize((new_width, new_height), Image.LANCZOS)
        # Ensure the output path has a .png extension
        if not output_path.lower().endswith(".png"):
            output_path += ".png"
        # Save the downscaled image as PNG
        downscaled_img.save(output_path, format="PNG")
        print(f"Image saved to {output_path} in PNG format")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: python downscale_image.py <input_path> <output_path> <new_width> <new_height>"
        )
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    new_width = int(sys.argv[3])
    new_height = int(sys.argv[4])

    downscale_image(input_path, output_path, new_width, new_height)
