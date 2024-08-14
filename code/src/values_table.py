"""
This file contains the list of values that can be used in the encoding and decoding process

Functions:
- get_values_list: Returns the list of values that can be used in the encoding and decoding process
- get_freq_dict: Returns the frequency dictionary of the values
- key_freq_dict: Returns the frequency dictionary of the values that can be used in the key

Variables:
- values_list: list of values that can be used in the encoding and decoding process
- freq_dict: frequency dictionary of the values

Usage:
The values_list variable contains the list of values that can be used in the encoding and decoding process. The freq_dict variable contains the frequency dictionary of the values.
The get_values_list function can be used to retrieve the list of values, and the get_freq_dict function can be used to retrieve the frequency dictionary of the values.
The key_freq_dict function can be used to retrieve the frequency dictionary of the values that can be used in the key.

Example:
values = get_values_list()
freq_dict = get_freq_dict()
key_freq_dict = key_freq_dict()

print(values)
print(freq_dict)
print(key_freq_dict)

# Output Sample:
# [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'END OF LINE', 'END OF TEXT', 'START OF TEXT', 'blank', 'START OF NEW KEY', 'END OF NEW KEY', 'UPPERCASE', 'START OF SYMBOL', 'END OF SYMBOL']
"""

# list of values that can be used in the encoding and decoding process 128 values
values_list = [
    " ",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "END OF LINE",
    "END OF TEXT",
    "START OF TEXT",
    "blank",
    "START OF NEW KEY",
    "END OF NEW KEY",
    "UPPERCASE",
    "START OF SYMBOL",
    "END OF SYMBOL",
]


def get_values_list():
    """
    Returns the list of values that can be used in the encoding and decoding process

    Returns:
        list: list of values that can be used in the encoding and decoding process
    """
    return values_list


freq_dict = {
    "a": 123287,
    "b": 24227,
    "c": 50211,
    "d": 59577,
    "e": 203824,
    "f": 32616,
    "g": 37064,
    "h": 65217,
    "i": 116488,
    "j": 2061,
    "k": 16047,
    "l": 75450,
    "m": 39060,
    "n": 118108,
    "o": 137119,
    "p": 36791,
    "q": 1774,
    "r": 101201,
    "s": 103814,
    "t": 151376,
    "u": 49901,
    "v": 20109,
    "w": 30974,
    "x": 4635,
    "y": 26924,
    "z": 1417,
    "0": 13109,
    "1": 10916,
    "2": 7894,
    "3": 4389,
    "4": 3204,
    "5": 3951,
    "6": 2739,
    "7": 2448,
    "8": 2505,
    "9": 2433,
    " ": 407934,
    "END OF LINE": 49492,
    "END OF TEXT": 4,
    "START OF TEXT": 4,
    "blank": 136,
    "START OF NEW KEY": 1,
    "END OF NEW KEY": 1,
    "UPPERCASE": 386403,
    "START OF SYMBOL": 105362,
    "END OF SYMBOL": 105362,
}


def get_freq_dict():
    """
    Returns the frequency dictionary of the values

    Returns:
        dict: frequency dictionary of the values
    """
    return freq_dict


def key_freq_dict():
    """
    Returns the frequency dictionary of the values that can be used in the key

    Returns:
        dict: frequency dictionary of the values that can be used in the key
    """
    return dict(list(freq_dict.items())[:36])