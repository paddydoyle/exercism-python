# https://en.wikipedia.org/wiki/Pythagorean_triple#Enumeration_of_primitive_Pythagorean_triples
def triplets_with_sum(sum_of_triplet):
    # set([(3, 4, 5)])

    triplets = set()
    # all_triplets = set()

    # It's well known that (3,4,5) is the smallest triplet, so start at 3
    for a in range(3, sum_of_triplet // 2):
        print(">> a = {}".format(a))
        # Fix a, and range b up to half of the sum_of_triplet
        # to reduce duplicates.
        # a < b, so start at a + 1
        # b < c, so finish at '(sum_of_triplet - a + 1) // 2'
        for b in range(a + 1, (sum_of_triplet - a + 1) // 2):
            c = sum_of_triplet - a - b

            triplet = (a, b, c)

            # if triplet in all_triplets:
            #     print("FOUND duplicate {}".format(triplet))

            # all_triplets.add(triplet)

            # print("a {} b {} c {}; sum {}; is_triplet? {}; sum ab {}; c {}"
            #       .format(a, b, c, (a + b + c), is_triplet(triplet),
            #               (a**2 + b**2), c**2))

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
