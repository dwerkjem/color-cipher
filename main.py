import random
from random import seed
import argparse

from src import tableOfValues

TABLE_OF_VALUES = tableOfValues.get_table_of_values()

parser = argparse.ArgumentParser(description="Encrypt or decrypt a message with a key")

# Add the arguments encrypt and decrypt and short forms of them
parser.add_argument("-e", "--encrypt", help="Encrypt a message", action="store_true")
parser.add_argument("-d", "--decrypt", help="Decrypt a message", action="store_true")
parser.add_argument("-m", "--message", help="The message to encrypt or decrypt", required=True)
parser.add_argument("-k", "--key", help="The key to use for encryption or decryption")
parser.add_argument("-o", "--output", help="The output file to write the result to")
parser.add_argument("-i", "--image", help="The image file to hide the message in")

args = parser.parse_args()

def main():
    # Seed the random number generator
    seed(1)

    # Get the message and key from the command line arguments
    message = args.message

    # If the key is not provided, use the key generator to generate a key