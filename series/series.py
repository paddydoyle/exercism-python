def slices(series, length):
    # Test for failure inputs first
    if len(series) < length:
        raise ValueError("The input string '{}' ".format(series) +
                         "is shorter than the slice length {}".format(length))

    if length < 1:
        raise ValueError("The slice length must be strictly positive")

    # There will be at least 1 substring, even if the length of the
    # string equals the slice length (i.e. the string itself)
    num_substrings = len(series) - length + 1

    return [series[i:i+length] for i in range(num_substrings)]
