import math


# https://en.wikipedia.org/wiki/Pythagorean_triple#Enumeration_of_primitive_Pythagorean_triples
def triplets_with_sum(sum_of_triplet):
    # set([(3, 4, 5)])

    triplets = set()
    binary_triplets = set()
    # all_triplets = set()

    # It's well known that (3,4,5) is the smallest triplet, so start at 3
    # Go up to (sum_of_triplet // 3) since we're dividing the single
    # number into the sum of 3 numbers, with (a < b < c). So beyond
    # (sum_of_triplet // 3) 'a' won't satifify that condition.
    for a in range(3, sum_of_triplet // 3):
        # print(">> a = {}".format(a))

        # First values of (a, b) pair in this inner loop.
        low_b = a + 1
        low_c = sum_of_triplet - a - low_b

        low_triplet = (a, low_b, low_c)
        # print(">>> low_triplet = {}".format(low_triplet))

        # Last values of (a, b) pair in this inner loop.
        # a != b, so subtract one, then split the difference
        high_b = ((sum_of_triplet - a - 1) // 2)
        high_c = sum_of_triplet - a - high_b

        high_triplet = (a, high_b, high_c)
        # print(">>> high_triplet = {}".format(high_triplet))

        # Have gone past the condition (a < b); we're done
        if high_b <= a:
            # print("xxxxxxxxxxxxxxxxxxxxxxx a = {} high_b = {} top = {}"
            #       .format(a, high_b, (sum_of_triplet // 3)))
            break

        # Check if we've hit an answer at the edges

        # The first pair is a match? No need to continue this branch.
        low_diff = pythag_diff(low_triplet)
        # print("    low diff = {}".format(low_diff))
        if low_diff == 0:
            triplets.add(low_triplet)
            continue

        # The last pair is a match? No need to continue this branch.
        high_diff = pythag_diff(high_triplet)
        # print("    high diff = {}".format(high_diff))
        if high_diff == 0:
            triplets.add(high_triplet)
            continue

        if not _signs_differ(low_diff, high_diff):
            # print("NOT OKKKKKKKKKKKK to search")
            continue

        x = binary_search(sum_of_triplet, low_triplet, high_triplet,
                          low_diff, high_diff)
        # print("result of binary_search = {}".format(x))
        if x:
            # binary_triplets.add(x)
            triplets.add(x)

        # If the biggest 'b' in this inner loop is still to small to
        # reach 'c', then skip this whole branch.
        # if (a**2 + high_b**2) < high_c**2:
        #     # print(">>>>>>> NOT iiiiiiiiiiiii to search")
        #     continue

        # Fix a, and range b up to half of the sum_of_triplet
        # to reduce duplicates.
        # a < b, so start at a + 1
        # b < c, so finish at '(sum_of_triplet - a + 1) // 2'
        # for b in range(a + 1, (sum_of_triplet - a + 1) // 2):
        #     c = sum_of_triplet - a - b

        #     triplet = (a, b, c)

        #     # if triplet in all_triplets:
        #     #     print("FOUND duplicate {}".format(triplet))

        #     # all_triplets.add(triplet)

        #     # print("a {} b {} c {}; sum {}; is_triplet? {}; sum ab {}; c {}"
        #     #       .format(a, b, c, (a + b + c), is_triplet(triplet),
        #     #               (a**2 + b**2), c**2))

        #     if is_triplet(triplet):
        #         triplets.add(triplet)

    # print("len(ALL) = {}".format(len(all_triplets)))
    # print("result of ALL binary_searches = {}".format(binary_triplets))

    return triplets


def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    # Assumes 'triplet' is a tuple
    (a, b, c) = triplet

    return a**2 + b**2 == c**2


# Helper: no built-in sign function
def _sign(x):
    return math.copysign(1, x)


def _signs_differ(low_diff, high_diff):
    return _sign(low_diff) != _sign(high_diff)


def pythag_diff(triplet):
    """
    Calculate the Pythagorean difference of c^2 - (a^2 + b^2)
    """
    (a, b, c) = triplet

    return c**2 - (a**2 + b**2)


def binary_search(sum_of_triplet, low_triplet, high_triplet,
                  low_diff, high_diff):
    """
    'a' is fixed. We're searching on 'b', and can adjust 'c'
    accordingly.
    """

    (low_a, low_b, low_c) = low_triplet
    (high_a, high_b, high_c) = high_triplet

    # print("binary: start: low = {}; high = {}"
    # .format(low_triplet, high_triplet))

    low_sign = _sign(low_diff)
    high_sign = _sign(high_diff)

    # 'a' is the same for both. We are searching on 'b'
    while low_b + 1 < high_b:
        # print("binary: LOOPPPP: low = {}; high = {}"
        # .format(low_triplet, high_triplet))

        # Binary search on 'b'
        mid_b = (low_b + high_b) // 2
        # 'a' is fixed
        mid_a = low_a
        # Adjust 'c' to match them
        mid_c = sum_of_triplet - mid_a - mid_b

        mid_triplet = (mid_a, mid_b, mid_c)

        # print("binary: loop: mid = {}".format(mid_triplet))

        if is_triplet(mid_triplet):
            # print("FOUND = {}; diff = {}"
            # .format(mid_triplet, pythag_diff(mid_triplet)))
            return mid_triplet

        mid_diff = pythag_diff(mid_triplet)
        # print("binary: loop: mid DIFF = {}".format(mid_diff))
        # print("binary: loop: SIGN low = {} high = {}"
        # .format(low_sign, high_sign))

        # Need to test the signs in order to determine the direction
        if _sign(mid_diff) == low_sign:
            # print("shift UP low")
            low_triplet = mid_triplet
            (low_a, low_b, low_c) = low_triplet
            low_diff = pythag_diff(low_triplet)
            low_sign = _sign(low_diff)
        else:
            # print("shift DOWN high")
            high_triplet = mid_triplet
            (high_a, high_b, high_c) = high_triplet
            high_diff = pythag_diff(high_triplet)
            high_sign = _sign(high_diff)

    return None
