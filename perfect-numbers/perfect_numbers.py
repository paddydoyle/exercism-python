def classify(number):
    if number <= 0:
        raise ValueError("Only strictly positive inputs allowed.")

    # Calculate once; multiple tests below.
    factor_sum = sum(factors(number))

    if factor_sum > number:
        return "abundant"
    elif factor_sum == number:
        return "perfect"
    else:
        return "deficient"


def factors(n):
    """
    Return a list of the factors of n, not including n itself.
    For example, the factors of 28 are: [1, 2, 4, 7, 14]
    Assume that n is >= 1, based on input checking above.
    """

    factors = []

    for k in range(1, n):
        if n % k == 0:
            factors.append(k)

    return factors
