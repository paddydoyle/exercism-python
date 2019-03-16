def find_anagrams(word, candidates):
    # Sort the characters in the words, to make them easier
    # to compare.
    sorted_chars = sorted(word.lower())

    # Filter the list to only match anagrams, but the word
    # itself cannot be a match.
    return [candidate for candidate in candidates
            if sorted_chars == sorted(candidate.lower()) and
            word.lower() != candidate.lower()]
