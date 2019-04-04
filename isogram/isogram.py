def is_isogram(string):
    # Trivial
    if not string:
        return True

    # Use a set for fast lookup
    unique_chars = set()

    # Look for duplicates so far
    for c in string:
        # Skip non-space and non-hypen chars
        if c == ' ' or c == '-':
            continue

        c = c.lower()

        if c in unique_chars:
            return False

        unique_chars.add(c)

    # Otherwise no duplicates
    return True
