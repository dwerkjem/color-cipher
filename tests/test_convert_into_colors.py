import encryption.convert_into_colors as convert_into_colors

def test_chunk_text():
    text = "NEW-KEYHelloEND-KEYEND-KEY"
    expected = ["NEW-KEY", "H", "e", "l", "l", "o", "END-KEY", "END-KEY"]
    assert list(convert_into_colors.chunk_text(text)) == expected

