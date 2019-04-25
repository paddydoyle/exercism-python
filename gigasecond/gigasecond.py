from datetime import datetime, timedelta


def add_gigasecond(moment):
    gigasecond = 10**9

    # We can add datetime and timedelta objects
    giga_delta = timedelta(seconds=gigasecond)

    return moment + giga_delta
