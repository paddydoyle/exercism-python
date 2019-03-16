# Score categories
# Change the values as you see fit
YACHT = 1
ONES = 2
TWOS = 4
THREES = 8
FOURS = 16
FIVES = 32
SIXES = 64
FULL_HOUSE = 128
FOUR_OF_A_KIND = 256
LITTLE_STRAIGHT = 512
BIG_STRAIGHT = 1024
CHOICE = 2048


def score(dice, category):
    # We were told that it will always be 5, so this is probably not needed.
    if len(dice) != 5:
        raise ValueError('First argument must be an array of 5 elements')

    # Check inputs: also told to assume that the category will be correct,
    # so skipping a check for that.

    # The array may not be sorted
    dice.sort(key=int)

    # Hmm, no switch/case in Python. Use a dict of funcs instead.
    cases = {
            YACHT: _score_yacht,
            ONES: _score_ones,
            TWOS: _score_twos,
            THREES: _score_threes,
            FOURS: _score_fours,
            FIVES: _score_fives,
            SIXES: _score_sixes,
            FULL_HOUSE: _score_full_house,
            FOUR_OF_A_KIND: _score_four_of_a_kind,
            LITTLE_STRAIGHT: _score_little_straight,
            BIG_STRAIGHT: _score_big_straight,
            CHOICE: _score_choice,
    }

    score_func = cases.get(category, 0)

    return score_func(dice)


def _score_yacht(dice):
    """
    If all 5 dice are equal, return 50, else 0
    """

    # the list is sorted via the score() function, so they are all
    # equal if the first element equals the last
    if dice[0] == dice[-1]:
        return 50
    else:
        return 0


def _score_digit(dice, n):
    """
    Return n x number of n's
    """

    return sum(list(filter(lambda number: number == n, dice)))


def _score_ones(dice):
    """
    Return 1 x number of ones
    """

    return _score_digit(dice, 1)


def _score_twos(dice):
    """
    Return 2 x number of twos
    """

    return _score_digit(dice, 2)


def _score_threes(dice):
    """
    Return 3 x number of threes
    """

    return _score_digit(dice, 3)


def _score_fours(dice):
    """
    Return 4 x number of fours
    """

    return _score_digit(dice, 4)


def _score_fives(dice):
    """
    Return 5 x number of fives
    """

    return _score_digit(dice, 5)


def _score_sixes(dice):
    """
    Return 6 x number of sixes
    """

    return _score_digit(dice, 6)


def _score_full_house(dice):
    """
    If full house (triple and double), return the sum of all dice
    Note: a yacht (all five the same) is not a full house.
    """

    # Test for full house
    if _score_yacht(dice) == 50:
        return 0

    # The list is sorted. So there will be a full house if either
    # - the pair is at the start of the list, and dice[0]==dice[1] and
    #   the triple is at the end of the list, and dice[2]==dice[4]
    # - the pair is at the end of the list, and dice[3]==dice[4] and
    #   the triple is at the start of the list, and dice[0]==dice[2]

    if dice[0] == dice[1] and dice[2] == dice[4]:
        return sum(dice)
    elif dice[0] == dice[2] and dice[3] == dice[4]:
        return sum(dice)
    else:
        return 0


def _score_four_of_a_kind(dice):
    """
    If 4 of a kind, return the sum of those 4
    """

    # The list is sorted. So there will be 4 of a kind if either
    # - the 4 of a kind is at the start of the list, and dice[0]==dice[3]
    # - the 4 of a kind is at the end of the list, and dice[1]==dice[4]

    if dice[0] == dice[3]:
        return 4 * dice[0]
    elif dice[1] == dice[4]:
        return 4 * dice[1]
    else:
        return 0


def _score_little_straight(dice):
    """
    The dice are [1, 2, 3, 4, 5]
    """

    if set(range(1, 6)) == set(dice):
        return 30
    else:
        return 0


def _score_big_straight(dice):
    """
    The dice are [2, 3, 4, 5, 6]
    """

    if set(range(2, 7)) == set(dice):
        return 30
    else:
        return 0


def _score_choice(dice):
    """
    Return the sum of the dice
    """

    return sum(dice)
