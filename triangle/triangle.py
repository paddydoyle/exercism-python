def equilateral(sides):
    if not _verify_triangle(sides):
        return False

    # For convenience
    (a, b, c) = sides

    return a == b == c


def isosceles(sides):
    if not _verify_triangle(sides):
        return False

    # For convenience
    (a, b, c) = sorted(sides)

    return a == b or b == c


def scalene(sides):
    if not _verify_triangle(sides):
        return False

    # For convenience
    (a, b, c) = sorted(sides)

    return a != b and b != c


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
