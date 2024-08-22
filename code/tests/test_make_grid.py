"""
Test the make_grid module

This module tests the make_grid module to ensure that the encoding and decoding functions work as expected.

Functions:
- test_encode: Tests the encode function.
- test_decode: Tests the decode function.

"""

from code.src.make_grid import encode, decode, prepare_plain_text


def test_encode():
    """
    Test the encode function
    """
    encoded_text = encode("dqwe90231")
    assert encoded_text == "ನᑴ᨟ᜨᙽ"


def test_decode():
    """
    Test the decode function
    """
    decoded_text = decode("ನᑴ᨟ᜨᙽ")
    assert decoded_text == "dqwe90231"
