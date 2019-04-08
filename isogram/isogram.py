def is_isogram(string):
    # Extract only alphabetic chars, as lower case.
    all_chars = [x.lower() for x in string if x.isalpha()]

    # Add to a set. Duplicates will be removed.
    unique_chars = set(all_chars)

    # If both sizes are the same, then no duplicates.
    return len(all_chars) == len(unique_chars)
