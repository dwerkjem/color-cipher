import encryption.convert_into_colors as cic
import os
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        # No command-line arguments; prompt user for input
        input_text = input("Enter the text or file path: ")
        name = input("Enter the name of the output image file: ")
        
        # Convert text or file content to image
        cic.convert_to_image(input_text, file=name)

    elif len(args) == 1:
        if args[0] == "-h":
            # Help command
            print("Usage: python main.py [input_text_or_file] [output_image_file]")
            print("If no arguments are provided, the program will prompt for input.")
        else:
            # Single argument: input_text_or_file
            name = input("Enter the name of the output image file: ")
            cic.convert_to_image(args[0], file=name)

    elif len(args) == 2:
        if args[0] == "-d":
            # Decode image from file
            file = args[1]
            if os.path.exists(file):
                decoded_text = cic.convert_to_text_from_file(file)
                print("Decoded text:", decoded_text)
            else:
                print(f"Error: File '{file}' not found.")
        else:
            # Two arguments: input_text_or_file and output_image_file
            cic.convert_to_image(args[0], file=args[1])
    else:
        print("Invalid arguments. Use -h for help.")
