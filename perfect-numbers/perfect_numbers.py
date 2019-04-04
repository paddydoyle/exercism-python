def classify(number):
    if number <= 0:
        raise ValueError("Only strictly positive inputs allowed.")

    # TODO: Consider only using the prime factors to calculate the
    # factor_sum for large numbers (for what value of 'large'??). It would
    # still require testing all combinations of prime factors (p
    # factorial?), but that might still be more efficient than testing
    # all values up to number. Not quite p factorial; cut off when the
    # products go above number. Start with the list of prime factors
    # including repeats, and then multiply each pair and test the product.
    # Store the other factor (number divided by the test candidate) as
    # it will be one of the other factors.

    # Calculate once; multiple tests below.
    # factor_sum = sum(k for k in range(1, number) if number % k == 0)
    factor_sum = sum(_factor_sum(number))

    # l = [k for k in range(1, number) if number % k == 0]
    # print("sum of l = {}; l = {}".format(sum(l), l))

    if factor_sum > number:
        return "abundant"
    elif factor_sum == number:
        return "perfect"
    else:
        return "deficient"


def _factor_sum(number):
    """
    Return a list of all unique factors of number. For example, the factors
    60 are: [1, 2, 3, 4, 6, 7, 8, 12, 14, 21, 24, 28, 42, 56, 84]
    """

    # The method is based on finding the prime factors of the number, and
    # storing each divisor and co-divisor in a set.
    # Multiple powers of each given prime factor are tested.
    # The combinatorial expansion of all of the prime (and multiplicative
    # prime) factors are all tested. This may produce other composite
    # combinations, so each time new combinations are found, they are added
    # to the search list.
    # Once no more combinations of factors are found, the loop exits and
    # we have found the factors.
    # Finally, '1' is added to the list.

    # Edge case
    if number == 1:
        return []

    # Use a set so we don't have to worry about duplicates.
    unique_factors = set()

    # Test all powers of 2.
    k = 2
    unique_factors = unique_factors.union(_sieve_powers(number, k))

    # Test all powers of odd numbers, up to sqrt of number.
    # Would be nice to just go to the next prime, but then we'd have
    # to find the next prime after the current k, which might be just
    # as much work unless we have a list of them handy.
    k = 3
    while k < number and k * k <= number:
        unique_factors = unique_factors.union(_sieve_powers(number, k))

        k += 2

    # Now must test combinations of the various factors that we have found
    # already. For example for 168 we have already found
    # [2, 3, 4, 7, 8, 21, 24, 42, 56, 84] but have not yet found
    # [6, 12, 14, 28]
    extra_factors = set()

    # Keep looping until not additional factors are found.
    while True:
        extra_factors.clear()
        search_list = sorted(unique_factors)

        for i in range(len(search_list)):
            s = search_list[i]

            # Triangular search of the list
            for t in search_list[i+1:]:
                st = s * t

                # assumes that the search_list was sorted
                if st >= number:
                    print("breaking the inner: st = {}".format(st))
                    break

                if number % st == 0 and st not in unique_factors:
                    print("FOUND a new factor pair: {} and {}".format(
                        st, number // st))
                    extra_factors.add(st)
                    extra_factors.add(number // st)

        print("INNER: unique_factors = {}".format(unique_factors))
        print("INNER: extra_factors = {}".format(extra_factors))

        if extra_factors:
            unique_factors = unique_factors.union(extra_factors)
        else:
            break

    unique_factors.add(1)

    print("search_list = {}".format(sorted(search_list)))
    print("sum(search_list) = {}".format(sum(search_list)))
    print("unique_factors = {}".format(sorted(unique_factors)))
    print("sum(unique_factors) = {}".format(sum(unique_factors)))

    return unique_factors


# Helper function
def _sieve_powers(n, k):
    """
    Find all powers of k which divide n. Add the divisor and
    its co-divisor to the set. Similar in spirit to a sieve
    approach for finding primes.
    """

    # Use a set to prevent duplicates.
    divisors = set()

    i = k

    while i < n and n % i == 0:
        divisors.add(i)
        divisors.add(n // i)

        # Powers of k
        i *= k

    return divisors
