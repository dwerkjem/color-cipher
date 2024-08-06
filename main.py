import os
import json

from src.tableOfValues import *
from src.encryptionHelper import *
color_depth = 24
image_resolution = (1920, 1080)
max_dict_resolution = 2 ** color_depth

def gen_file():
    freq_dict = decrease_resolution_of_dict(get_freq_dict(), max_dict_resolution) # type: ignore
    distribution = distribute_characters(freq_dict, max_dict_resolution)
    with open("build/tables/dict{}.json".format(color_depth), "w") as file:
        json.dump(distribution, file)

def ensure_exist():
    assert os.path.exists("build"), "Please run the program from the root directory and ensure that the build directory exists"
    if not os.path.exists("build/tables"):
        os.makedirs("build/tables")
    if not os.path.exists("build/tables/dict{}.json".format(color_depth)):
        gen_file()

def gen_color_dict():
    with open("build/tables/dict{}.json".format(color_depth), "r") as file:
        distribution = json.load(file)
        color_dict = char_list_to_color_dict(list(distribution))
        print("Generated color dictionary")
        return color_dict

def main():
    ensure_exist()
    color_dict = gen_color_dict()
    print(color_dict)
if __name__ == "__main__":
    main()
