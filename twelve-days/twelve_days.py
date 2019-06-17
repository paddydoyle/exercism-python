# Ordinal days. The package num2words could be used here.
ORDINAL_DAYS = [None,
                "first",
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
# Include a token for adding 'and ' if required for verse 1.
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
          "{}a Partridge in a Pear Tree."]

# Split off first line; we always use that. Include a token
# for the ordinal day as a word.
# Template for the verse, including a token for the ordinal day
# and the gift string.
VERSE_TEMPLATE = "On the {} day of Christmas my true love gave to me: {}"


def recite(start_verse, end_verse):
    # Calculate once, for convenience.
    n_verses = len(VERSES)

    lyrics = []

    # Add 1 because the inputs start to count at 1, not 0
    for verse_num in range(start_verse, end_verse + 1):

        ordinal_day = ORDINAL_DAYS[verse_num]

        if verse_num == 1:
            bridge = ""
        else:
            bridge = "and "

        # Slice the last 'verse_num' lines of verses.
        # Add the bridge word if required, using the token in last
        # entry of VERSES.
        gift_string = ", ".join(VERSES[n_verses - verse_num:]).format(bridge)

        lyrics.append(VERSE_TEMPLATE.format(ordinal_day, gift_string))

    return lyrics
