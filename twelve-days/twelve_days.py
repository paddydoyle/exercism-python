def recite(start_verse, end_verse):
    # The package num2words could be used here.
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

    # Split off last line, we always use that, with or without the
    # starting 'and'
    last_line = "a Partridge in a Pear Tree."

    # Reverse order, to make the array slices easier.
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
              "two Turtle Doves, "]

    # Calculate once, for convenience. Add one because we've taken
    # out the last verse; stored separately above.
    n_verses = len(verses) + 1

    outputs = []

    # Add 1 because we're starting to count at 1, not 0
    for verse in range(start_verse, end_verse + 1):

        day = days[verse]

        if verse == 1:
            outputs.append(first_line.format(day) + last_line)
        else:
            outputs.append(first_line.format(day) +
                           ''.join(verses[n_verses - verse:]) +
                           'and ' +
                           last_line)

    return outputs
