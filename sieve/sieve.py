def primes(limit):
    prime_range = range(2, limit + 1)

    # Use a set for ease of removal of subsets.
    prime_set = set(prime_range)

    # There will be lots of skipped num values, due to nature
    # of the sieve algorithm.
    for num in prime_range:
        if num in prime_set:
            # Construct all multiples of the prime.
            multiples = set(range(2 * num, limit + 1, num))

            # And remove them from the main set.
            prime_set = prime_set.difference(multiples)

    return sorted(prime_set)
