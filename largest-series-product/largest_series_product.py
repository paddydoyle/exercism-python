from functools import reduce


def largest_product(series, size):
    # Corner case: not entirely sure why this is a valid answer but ok
    if size == 0:
        return 1

    # Test for failure inputs
    if not series:
        raise ValueError("The input string cannot be empty")

    if len(series) < size:
        raise ValueError("The input string '{}' ".format(series) +
                         "is shorter than the slice size {}".format(size))

    if size < 0:
        raise ValueError("The slice size must be non-negative")

    # There will be at least 1 substring, even if the length of the
    # string equals the slice length (i.e. the string itself)
    num_substrings = len(series) - size + 1

    # First generate the list of substrings
    substrs = [series[i:i+size] for i in range(num_substrings)]

    # Using named function in the map, because otherwise it's way too messy
    # as a lambda
    return max(map(_string_to_product, substrs))


def _string_to_product(str_of_digits):
    """
    Input is a string of digits. Convert each to an int
    and calculate the product.
    """

    return reduce(lambda x, y: x*y, [int(i) for i in str_of_digits])
