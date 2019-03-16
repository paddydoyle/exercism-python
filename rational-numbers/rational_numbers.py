from __future__ import division
from math import gcd
from math import pow


class Rational(object):
    def __init__(self, numer, denom):
        numer = int(numer)
        denom = int(denom)

        if not denom:
            raise ValueError('Cannot have denominator 0 in a Rational')

        the_gcd = gcd(numer, denom)
        if the_gcd != 1:
            numer = numer / the_gcd
            denom = denom / the_gcd

        # Canonicalise any negative numbers
        if numer < 0 and denom < 0:
            # Both negative, make positive
            numer = -1 * numer
            denom = -1 * denom
        elif numer > 0 and denom < 0:
            # Negative denom, bring that to the numer
            numer = -1 * numer
            denom = -1 * denom

        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        if not other.denom:
            raise ValueError('Cannot have denominator 0 in a Rational')

        return Rational((self.numer * other.denom + self.denom * other.numer),
                        (self.denom * other.denom))

    def __sub__(self, other):
        if not other.denom:
            raise ValueError('Cannot have denominator 0 in a Rational')

        return Rational((self.numer * other.denom - self.denom * other.numer),
                        (self.denom * other.denom))

    def __mul__(self, other):
        if not other.denom:
            raise ValueError('Cannot have denominator 0 in a Rational')

        return Rational(self.numer * other.numer,
                        self.denom * other.denom)

    def __truediv__(self, other):
        if not other.denom:
            raise ValueError('Cannot have denominator 0 in a Rational')

        return Rational((self.numer * other.denom),
                        (self.denom * other.numer))

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return pow(base ** self.numer, 1 / self.denom)
