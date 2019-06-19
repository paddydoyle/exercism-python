# Ordinal days. The package num2words could be used here.
ORDINAL_DAYS = ["first",
                "second",
                "third",
                "fourth",
                "fifth",
                "sixth",
                "seventh",
                "eighth",
                "ninth",
                "tenth",
                "eleventh",
                "twelfth"]

# Reverse order, to make the array slices easier. Also makes it
# easier to add 'thirteenth' etc, and the array slice below doesn't
# have to change.
VERSES = ["twelve Drummers Drumming",
          "eleven Pipers Piping",
          "ten Lords-a-Leaping",
          "nine Ladies Dancing",
          "eight Maids-a-Milking",
          "seven Swans-a-Swimming",
          "six Geese-a-Laying",
          "five Gold Rings",
          "four Calling Birds",
          "three French Hens",
          "two Turtle Doves",
          "and a Partridge in a Pear Tree."]

# Template for the verse, including a token for the ordinal day
# and a token for the verse string.
VERSE_TEMPLATE = "On the {} day of Christmas my true love gave to me: {}"


def recite(start_verse, end_verse):
    # Calculate once, for convenience.
    n_verses = len(VERSES)

    lyrics = []

    # Add 1 because the inputs start to count at 1, not 0
    for verse_num in range(start_verse, end_verse + 1):

        # User input starts at 1, array starts at 0
        ordinal_day = ORDINAL_DAYS[verse_num - 1]

        # Slice the last 'verse_num' lines of verses.
        verses = VERSES[n_verses - verse_num:]

        # Remove for one verse, rather than add for 11 verses.
        if verse_num == 1:
            verses[0] = verses[0][4:]

        lyrics.append(VERSE_TEMPLATE.format(ordinal_day, ", ".join(verses)))

    return lyrics
