# Group the char together by score, minimising repetition.
SCORE_TO_CHAR = [
        (1, 'AEIOULNRST'),
        (2, 'DG'),
        (3, 'BCMP'),
        (4, 'FHVWY'),
        (5, 'K'),
        (8, 'JX'),
        (10, 'QZ'),
        ]

# Invert the above, exploding the strings as we go.
CHAR_TO_SCORE = {char: score for score, chars in SCORE_TO_CHAR
                 for char in chars}


def score(word):
    return sum(CHAR_TO_SCORE.get(char, 0) for char in word.upper())
