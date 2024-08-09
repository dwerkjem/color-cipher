import colorToImage as cti
def test_rgb_list_to_image():
    rgb_list = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0),
                (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255),
                (128, 128, 128), (128, 0, 0), (0, 128, 0), (0, 0, 128),
                (128, 128, 0), (128, 0, 128), (0, 128, 128), (64, 64, 64),
                (64, 0, 0), (0, 64, 0), (0, 0, 64), (64, 64, 0), (64, 0, 64),
                (0, 64, 64), (192, 192, 192), (192, 0, 0), (0, 192, 0),
                (0, 0, 192,), (192, 192, 0), (192, 0, 192), (0, 192, 192)]
    image_width = 5
    image_height = 6
    result = cti.rgb_list_to_image(rgb_list, image_width, image_height)
    expected_result = cti.Image.new("RGB", (image_width, image_height))
    expected_result.putdata(rgb_list)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"