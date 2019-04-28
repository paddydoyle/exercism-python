import math


def triplets_with_sum(sum_of_triplet):
    triplets = set()

    # Outer loop: 'a'
    # It's well known that (3,4,5) is the smallest triplet, so start 'a'
    # at 3.
    # Go up to (sum_of_triplet // 3) since we're dividing the single
    # number into the sum of 3 numbers, with (a < b < c). So beyond
    # (sum_of_triplet // 3) 'a' won't satifify that condition.
    for a in range(3, sum_of_triplet // 3):
        # For each pair (a, b), they determines 'c'.

        # First values of (a, b) pair in this inner loop.
        # For a fixed 'a', the next possible 'b' is (a + 1), since we must
        # have a < b < c
        low_b = a + 1
        low_c = sum_of_triplet - a - low_b

        low_triplet = (a, low_b, low_c)

        # Last values of (a, b) pair in this inner loop.
        # We must have (a < b), so subtract one, then split the difference
        high_b = ((sum_of_triplet - a - 1) // 2)
        high_c = sum_of_triplet - a - high_b

        high_triplet = (a, high_b, high_c)

        # Check if we've hit an answer at the edges of the 'b' range.

        # The first pair is a match? No need to continue this branch.
        if is_triplet(low_triplet):
            triplets.add(low_triplet)
            continue

        # The last pair is a match? No need to continue this branch.
        if is_triplet(high_triplet):
            triplets.add(high_triplet)
            continue

        # Else, perform Binary Search on the values of 'b' in this range.
        triplet = _binary_search(low_triplet, high_triplet)
        if triplet:
            triplets.add(triplet)

    return triplets


def is_triplet(triplet):
    """
    Input of a tuple with 3 values.
    Output: whether they form a Pythagorean Triplet
    """
    # Same as testing: a**2 + b**2 == c**2
    return _pythag_diff(triplet) == 0


def _sign(x):
    """
    No built-in sign function.
    """
    return math.copysign(1, x)


def _pythag_diff(triplet):
    """
    Calculate the Pythagorean difference of c^2 - (a^2 + b^2)
    """
    (a, b, c) = triplet

    return c**2 - (a**2 + b**2)


def _binary_search(low_triplet, high_triplet):
    """
    'a' is fixed. We're performing the Binary Search on 'b', and can
    adjust 'c' accordingly.
    Optimisation to first test the signs of the Pythagorean Difference
    (c**2 - (a**2 + b**2)), since if they have the same sign, then there
    can be no solutions in this range.
    The binary search is based on the signs of the pythagorean diffs.
    """
    # First find the pythagorean differences of the low and high
    # triplets.
    low_sign = _sign(_pythag_diff(low_triplet))
    high_sign = _sign(_pythag_diff(high_triplet))

    # If the low and high have the same sign, then there is no way
    # to have a valid triplet in this range (Intermediate Value
    # Theorem), so skip it.
    if _sign(low_sign) == _sign(high_sign):
        return None

    # Else, the signs differ, so we may have a potential match. Proceed
    # with binary search.

    # For calculating 'c' in the loop.
    sum_of_triplet = sum(low_triplet)

    # Slightly more readable indexes into the triplet.
    A, B, C = 0, 1, 2

    # 'a' is fixed
    mid_a = low_triplet[A]

    while low_triplet[B] + 1 < high_triplet[B]:
        # Binary search on 'b'
        mid_b = (low_triplet[B] + high_triplet[B]) // 2

        # Adjust 'c' accordingly
        mid_c = sum_of_triplet - mid_a - mid_b

        mid_triplet = (mid_a, mid_b, mid_c)

        mid_diff = _pythag_diff(mid_triplet)

        # Not calling 'is_triplet' here because we need to know the
        # value of the sign of the diff, if it's not 0, and don't
        # want to repeat essentially the same calculation.
        if mid_diff == 0:
            # It is a triplet!
            return mid_triplet

        # Bisect the range.
        # Need to test the signs in order to determine the direction.
        if _sign(mid_diff) == low_sign:
            low_triplet = mid_triplet
        else:
            # high_sign == mid_sign
            high_triplet = mid_triplet

    # No valid triplets in this range.
    return None
