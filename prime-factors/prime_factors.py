from math import sqrt


def prime_factors(n):
    """
    Return a list of the prime factors of n, including duplicates. For
    example, the factors of 60 are: [2, 2, 3, 5]
    """

    factors = []

    # Split off even factors, so we can focus on incrementing
    # odd numbers below.
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Test all odd numbers, up to sqrt of n.
    # Would be nice to just go to the next prime, but then we'd have
    # to find the next prime after the current k, which might be just
    # as much work unless we have a list of them handy.
    k = 3
    while k * k <= n:
        if n % k == 0:
            factors.append(k)
            n //= k
        else:
            k += 2

    # Last divisor must be a prime
    if n != 1:
        factors.append(n)

    return factors
