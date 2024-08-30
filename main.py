import encryption.convert_into_colors as cic

import os

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    name = input("Enter the name of the file: ")
    
    image = cic.convert_to_image(input_text, (512, 512), name)