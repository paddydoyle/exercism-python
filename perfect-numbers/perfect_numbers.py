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
    factor_sum = sum(factor_sum_prime_factors(number))

    l = [k for k in range(1, number) if number % k == 0]
    print("sum of l = {}; l = {}".format(sum(l), l))

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

    # Split off even factors, so we can focus on incrementing
    # odd numbers below.
    i = 1
    while 2 < n and n % 2 == 0:
        unique_factors.add(2 * i)
        print("adding ONE {}".format(2 * i))

        unique_factors.add(n // 2)
        print("adding TWO {}".format(n // 2))

        unique_factors.add(number // 2)
        print("adding THREE {}".format(number // 2))

        n //= 2
        i *= 2

    # Test all odd numbers, up to sqrt of n.
    # Would be nice to just go to the next prime, but then we'd have
    # to find the next prime after the current k, which might be just
    # as much work unless we have a list of them handy.
    k = 3
    while k < n and k * k <= n:
        i = 1
        while n % k == 0:
            unique_factors.add(k * i)
            print("adding ONE {}".format(k * i))

            unique_factors.add(n // k)
            print("adding TWO {}".format(n // k))

            unique_factors.add(number // k)
            print("adding THREE {}".format(number // k))
            n //= k
            i *= k

        k += 2

    print("unique factors of {} = {}".format(number, sorted(unique_factors)))

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

    while n % k == 0:
        print("k = {}; n = {}; rem = {}".format(k, n, n // k))
        divisors.add(k)
        divisors.add(n // k)

        k *= k

    return divisors
