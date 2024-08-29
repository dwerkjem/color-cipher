"""
this module is responsible for converting the text into colors
"""


import sys
from typing import Generator

import numpy as np
sys.path.append('/home/derek/DEV/color-cipher')

from resources.values import get_value as list_of_values


def chunk_text(text:str) -> Generator[str, None, None]:
    """
    Split the text into chunks
    """
    chunked_text = []
    i = 0
    while i < len(text):
        if text[i : i + 7] == "NEW-KEY":
            chunked_text.append(text[i : i + 7])
            i += 7
        elif text[i : i + 7] == "END-KEY":
            chunked_text.append(text[i : i + 7])
            i += 7
        else:
            chunked_text.append(text[i])
            i += 1

    return chunked_text
