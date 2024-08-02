def smallest_factor_greater_than_or_equal(number, threshold):
    for i in range(threshold, number + 1):
        if number % i == 0:
            return i
    return None

def map_values_to_colors(values_list: list, color_depth: int, bias: list) -> dict:
    '''
    This function maps values to colors.

    Parameters:
    values_list (list): The list of characters to map to colors.
    color_depth (int): The color depth in bits must be a multiple of 8.
    '''
    values_list_length = len(values_list)
    color_depth = int(color_depth)
    assert color_depth > 8, "Color depth must be greater than 8 bits"
    assert color_depth % 8 == 0, "Color depth must be a multiple of 8 bits"
    num_colors = 2 ** (color_depth // 8)
    assert num_colors >= values_list_length, "Color depth is too small to map all values"
