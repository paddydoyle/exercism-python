def is_isogram(string):
    # Trivial
    if not string:
        return True

    # Extract non-space and non-hypen chars as lower case
    chars = [x.lower() for x in string if x != ' ' and x != '-']

    # Use a set for fast lookup
    unique_chars = set()

    # Look for duplicates so far
    for c in chars:
        if c in unique_chars:
            return False

        unique_chars.add(c)

    # Otherwise no duplicates
    return True
