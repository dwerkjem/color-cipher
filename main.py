from src.tableOfValues import *
from src.encryptionHelper import *

def main():
    image_resolution = (1920, 1080)
    color_depth = 6
    max_dict_resolution = 2 ** color_depth
    freq_dict = get_freq_dict()
    freq_dict = decrease_resolution_of_dict(freq_dict, max_dict_resolution) # type: ignore
    distribution = distribute_characters(freq_dict, image_resolution[0] * image_resolution[1])

if __name__ == "__main__":
    main()