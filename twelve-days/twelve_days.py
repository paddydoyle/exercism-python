def recite(start_verse, end_verse):
    # Ordinal days. The package num2words could be used here.
    days = ["zeroth",
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

    # Split off first line; we always use that. Include a token
    # for the ordinal day as a word.
    first_line = "On the {} day of Christmas my true love gave to me: "

    # Split off last line for verse one, which does not include the
    # word 'and'. This is duplicated in the array, but simplifies
    # the array slice.
    last_line_verse_one = "a Partridge in a Pear Tree."

    # Reverse order, to make the array slices easier. Also makes it
    # easier to add 'thirteenth' etc, and the array slice below doesn't
    # have to change.
    verses = ["twelve Drummers Drumming, ",
              "eleven Pipers Piping, ",
              "ten Lords-a-Leaping, ",
              "nine Ladies Dancing, ",
              "eight Maids-a-Milking, ",
              "seven Swans-a-Swimming, ",
              "six Geese-a-Laying, ",
              "five Gold Rings, ",
              "four Calling Birds, ",
              "three French Hens, ",
              "two Turtle Doves, ",
              "and " + last_line_verse_one]

    # Calculate once, for convenience.
    n_verses = len(verses)

    lyrics = []

    # Add 1 because the inputs start to count at 1, not 0
    for verse in range(start_verse, end_verse + 1):

        day = days[verse]

        if verse == 1:
            lyrics.append(first_line.format(day) + last_line_verse_one)
        else:
            # Slice the last 'verse' verses.
            lyrics.append(first_line.format(day) +
                          ''.join(verses[n_verses - verse:]))

    return lyrics
