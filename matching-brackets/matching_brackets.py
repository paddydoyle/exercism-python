def is_paired(input_string):

    # Reverse pairings make pop() matching easier
    reverse_bracket_pairs = {
            ']': '[',
            '}': '{',
            ')': '(',
            }

    # Storing the values in a set for fast lookup, at expense
    # of extra storage.
    opening_brackets = set(reverse_bracket_pairs.values())

    # Store the opening on a stack
    stack = []

    for char in input_string:
        if char in opening_brackets:
            stack.append(char)

        elif char in reverse_bracket_pairs:
            if not stack:
                # Too many closing brackets.
                return False
            if stack.pop() != reverse_bracket_pairs[char]:
                # Unmatched brackets.
                return False

    # Stack should be empty if we have popped all matches.
    return not stack
