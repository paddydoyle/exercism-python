# https://en.wikipedia.org/wiki/Pythagorean_triple#Enumeration_of_primitive_Pythagorean_triples
def triplets_with_sum(sum_of_triplet):
    # set([(3, 4, 5)])

    triplets = set()
    # all_triplets = set()

    for a in range(1, sum_of_triplet):
        # Fix a, and range b up to half of the sum_of_triplet
        # to reduce duplicates.
        for b in range(a + 1, (sum_of_triplet - a + 1) // 2):
            c = sum_of_triplet - a - b

            triplet = (a, b, c)

            # if triplet in all_triplets:
            #     print("FOUND duplicate {}".format(triplet))

            # all_triplets.add(triplet)

            # print("a = {}; b = {}; c = {}; sum = {}; is_triplet? {}"
            #         .format(a, b, c, (a + b + c), is_triplet(triplet)))

            if is_triplet(triplet):
                triplets.add(triplet)

    # print("len(ALL) = {}".format(len(all_triplets)))

    return triplets


def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    # Assumes 'triplet' is a tuple
    (a, b, c) = triplet

    return a**2 + b**2 == c**2
