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
    factor_sum = sum(k for k in range(1, number) if number % k == 0)
    # factor_sum = sum(factor_sum_prime_factors(number))

    # l = [k for k in range(1, number) if number % k == 0]
    # print("sum of l = {}; l = {}".format(sum(l), l))

    if factor_sum > number:
        return "abundant"
    elif factor_sum == number:
        return "perfect"
    else:
        return "deficient"


def factor_sum_prime_factors(n):
    """
    Return a list of the prime factors of n, including duplicates. For
    example, the factors of 60 are: [2, 2, 3, 5]
    """

    # Edge case
    if n == 1:
        return []

    # Save the original number.
    number = n

    unique_factors = set()

    # Test all powers of 2.
    unique_factors = unique_factors.union(_powers_of_k_divisors(number, 2))

    # Test all powers of odd numbers, up to sqrt of n.
    # Would be nice to just go to the next prime, but then we'd have
    # to find the next prime after the current k, which might be just
    # as much work unless we have a list of them handy.
    k = 3
    while k < n and k * k <= n:
        unique_factors = unique_factors.union(_powers_of_k_divisors(number, k))

        k += 2

    print("unique factors of {} = {}".format(number, sorted(unique_factors)))

    # Now must test combinations of the various factors that we have found
    # already. For example for 168 we have already found
    # [2, 3, 4, 7, 8, 21, 24, 42, 56, 84] but have not yet found
    # [6, 12, 14, 28]
    extra_factors = set()

    while True:
        extra_factors.clear()
        search_list = sorted(unique_factors)

        for i in range(len(search_list)):
            s = search_list[i]

            # Triangular search of the list
            for t in search_list[i+1:]:
                print("s = {}; t = {}; st = {}; rem = {}".format(
                    s, t, s * t, number % (s * t)))
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
def _powers_of_k_divisors(n, k):
    """
    Find all powers of k which divide n. Add the divisor and
    its co-divisor to the set.
    """
    divisors = set()

    i = k

    while i < n and n % i == 0:
        print("i = {}; n = {}; rem = {}".format(i, n, n // k))
        divisors.add(i)
        divisors.add(n // i)

        i *= k

    return divisors
