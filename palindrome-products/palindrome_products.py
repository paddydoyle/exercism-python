def smallest_palindrome(max_factor, min_factor):
    """
    Return list of the smallest palindrome, and a set of its
    factor pairs.
    """

    if max_factor < min_factor:
        raise ValueError("Max must be greater than min")

    smallest = None
    factors = set()

    # Unfortunately cannot just stop when we find the first/smallest
    # palindrome, because we must return all factors of the palindrome
    # in the range of numbers.
    # We can however do a nice optimisation that by using triangular
    # search for (i <= j), once we find the first palindrome then it
    # will be the smallest, and so we no longer have to perform the
    # test for being a palindrome for any further products.
    for i in range(min_factor, max_factor + 1):
        for j in range(i, max_factor + 1):
            product = i * j

            if smallest:
                # Once we have found 'smallest', then no need to
                # re-test for being a palindrome.

                # Test to see if the current product is the same
                # as the largest.
                if product == smallest:
                    factors.update([(i, j)])
                elif product > smallest:
                    # Break the inner loop, because every subsequent
                    # pair of (i, j) will produce a product larger
                    # than 'smallest'
                    break

            elif _is_palindrome(product):
                # We've found the first/smallest
                smallest = product
                factors.update([(i, j)])

    return (smallest, factors)


def largest_palindrome(max_factor, min_factor):
    """
    Return list of the largest palindrome, and a set of its
    factor pairs.
    """

    if max_factor < min_factor:
        raise ValueError("Max must be greater than min")

    largest = None
    factors = set()

    # Unfortunately cannot just stop when we find the last/largest
    # palindrome, because we must return all factors of the palindrome
    # in the range of numbers.
    # Search down in a triangular manner from max_factor with (i <= j).
    # The first palindrome found may not be the largest.
    for i in range(max_factor, min_factor - 1, -1):
        if largest and i * max_factor < largest:
            # Break the outer loop. Because (i <= j) with i and j both
            # decreasing from max_factor, once i * max_factor < largest
            # then every subsequent pair of (i, j) will produce a product
            # smaller than 'largest'.
            break

        for j in range(max_factor, i - 1, -1):
            product = i * j

            if not largest and _is_palindrome(product):
                # We've found the first palindrome. It may not be the
                # largest so we will have to continue searching.
                largest = product
                factors.update([(i, j)])

            elif largest and _is_palindrome(product):
                # Is the new palindrome bigger?
                if product > largest:
                    # If so, reset the largest and the set
                    largest = product

                    factors.clear()
                    factors.update([(i, j)])

                # Test to see if the current product is the same
                # as the largest.
                elif product == largest:
                    factors.update([(i, j)])
                elif product < largest:
                    # Break the inner loop, because every subsequent
                    # pair of (i, j) will produce a product smaller
                    # than 'largest'
                    break

    return (largest, factors)


def _is_palindrome(number):
    """
    Return true if the number as a string is a palindrome.
    """
    word = str(number)

    # Instead of just testing if the reverse is equal to
    # the string, loop up to half-way; this should save time for
    # very long input strings.
    for i, ch in enumerate(word):
        # A counter-example.
        if ch != word[-i-1]:
            return False

        # Break once we get half-way
        if i > len(word)/2:
            return True

    # No counter-example.
    return True
