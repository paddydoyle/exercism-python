def raindrops(number):
    # List of (test divisors, output words) tuples
    divisors = [
            (3, 'Pling'),
            (5, 'Plang'),
            (7, 'Plong'),
            ]

    # List of words corresponding to successful divisors.
    divisor_strings = [word for i, word in divisors if number % i == 0]

    # If nothing divided, then return the input as a string.
    if not divisor_strings:
        return str(number)

    # Otherwise join the list of matched words.
    return ''.join(divisor_strings)
