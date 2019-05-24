def equilateral(sides):
    if not _verify_triangle(sides):
        return False

    return len(set(sides)) == 1


def isosceles(sides):
    if not _verify_triangle(sides):
        return False

    return len(set(sides)) <= 2


def scalene(sides):
    if not _verify_triangle(sides):
        return False

    return len(set(sides)) == 3


def _verify_triangle(sides):
    """
    Common triangle verification checks.
    """

    # All zero sides
    if not any(sides):
        return False

    # For convenience
    (a, b, c) = sorted(sides)

    # Check triangle inequality
    if a + b < c:
        return False

    return True
