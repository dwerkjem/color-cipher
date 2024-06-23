import random
from random import seed
import argparse

from src import tableOfValues

TABLE_OF_VALUES = tableOfValues.get_table_of_values()

parser = argparse.ArgumentParser(description="Encrypt or decrypt a message with a key")

# Add the arguments encrypt and decrypt and short forms of them
parser.add_argument("-e", "--encrypt", help="Encrypt a message", action="store_true")
parser.add_argument("-d", "--decrypt", help="Decrypt a message", action="store_true")