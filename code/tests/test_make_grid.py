from code.src.make_grid import encode, decode, prepare_plain_text

def test_encode():
    encoded_text = encode("dqwe90231")
    assert encoded_text == "ನᑴ᨟ᜨᙽ"

def test_decode():
    decoded_text = decode("ನᑴ᨟ᜨᙽ")
    assert decoded_text == "dqwe90231"

