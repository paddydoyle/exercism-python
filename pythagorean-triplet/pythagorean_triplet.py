def triplets_with_sum(sum_of_triplet):
    # set([(3, 4, 5)])

    triplets = set()

    for a in range(1, sum_of_triplet):
        for b in range(a, (sum_of_triplet) // 2):
            c = sum_of_triplet - a - b

            triplet = (a, b, c)

            # print("a = {}; b = {}; c = {}; sum = {}; is_triplet? {}"
            # .format(a, b, c, (a + b + c), is_triplet(triplet)))

            if is_triplet(triplet):
                triplets.add(triplet)

    return triplets


def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    # Assumes 'triplet' is a tuple
    (a, b, c) = triplet

    return a**2 + b**2 == c**2
