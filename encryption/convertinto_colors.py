import numpy as np
import math

from resorces.values import get_value as list_of_values


from typing import Generator

def chukker(text:str) -> Generator[str]:
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
