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
            "eight",
            "nineth",
            "tenth",
            "eleventh",
            "twelfth",]

    # Split off first line; we always use that. Include a token
    # for the ordinal day as a word.
    first_line = "On the {} day of Christmas my true love gave to me: "

    # Split off last line, we always use that, with or without the
    # starting 'and'
    last_line = "a Partridge in a Pear Tree."

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
              "two Turtle Doves, ",]

    n_verses = len(verses) + 1
    # print("n_verses {}".format(n_verses))

    outputs = []

    # Add 1 because we're starting to count at 1, not 0
    for verse in range(start_verse, end_verse + 1):
        # print("verse {} of {}".format(start_verse, end_verse))

        day = days[verse]
        # print("day = {}".format(day))

        if verse == 1:
            outputs.append(first_line.format(day) + last_line)
            # print("111111 outputs = {}".format(outputs))
        else:
            outputs.append(first_line.format(day) + ''.join(verses[n_verses - verse:]) + 'and ' + last_line)
            # print("ooo outputs = {}".format(outputs))

    return outputs
