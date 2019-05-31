import re


class Phone(object):
    COUNTRY_CODE_US = '1'
    NANP_LENGTH = 10
    NANP_LEN_COUNTRY = 11

    def __init__(self, number):
        # Strip non-numeric chars
        digits = ''.join(ch for ch in number if ch.isdigit())

        # Validate correct country code, if present.
        if (len(digits) == self.NANP_LEN_COUNTRY and
                digits[0] != self.COUNTRY_CODE_US):
            raise ValueError("For {} digits, the first must be 1".format(
                             self.NANP_LEN_COUNTRY))

        # Strip the leading '1' if it's present.
        if (len(digits) == self.NANP_LEN_COUNTRY and
                digits[0] == self.COUNTRY_CODE_US):
            digits = digits[1:]

        # If not 11 chars, then it must be 10
        if len(digits) != self.NANP_LENGTH:
            raise ValueError("Must be either {} or {} digits long".format(
                             self.NANP_LENGTH, self.NANP_LEN_COUNTRY))

        # Now we know it's 10 digits wide. Seperate the parts.
        self.number = digits
        self.area_code = digits[:3]
        self.exchange_code = digits[3:6]
        self.subscriber = digits[6:]

        # Validate area_code
        if not re.match(r'^[2-9]\d\d$', self.area_code):
            raise ValueError("Area code must start with [2-9]")

        # Validate exchange_code
        if not re.match(r'^[2-9]\d\d$', self.exchange_code):
            raise ValueError("Exchange code must start with [2-9]")

    def pretty(self):
        """
        Return a human-readable representation of the number. For
        '2234567890' it should return '(223) 456-7890'
        """
        return '({}) {}-{}'.format(self.area_code, self.exchange_code,
                                   self.subscriber)
