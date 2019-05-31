import math


def score(x, y):
    # List of tuples:
    # - the first element is the minimum radius
    # - the second element is the corresponding score
    # Order them in decreasing radius.
    scores = [
            (10, 0),
            (5, 1),
            (1, 5),
            (0, 10)
            ]

    # Euclidean distance from origin.
    dist = math.sqrt(x**2 + y**2)

    # Search from out to in, returning first score where
    # the point distance is beyond that radius.
    for radius, score in scores:
        if dist > radius:
            return score

    return 0
