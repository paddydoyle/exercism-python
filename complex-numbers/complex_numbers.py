import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # (a + c) + (b + d) * i
        real = self.real + other.real
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        # (a * c - b * d) + (b * c + a * d) * i
        real = (self.real * other.real - self.imaginary * other.imaginary)
        imaginary = (self.imaginary * other.real + self.real * other.imaginary)
        return ComplexNumber(real, imaginary)

    def __sub__(self, other):
        # (a - c) + (b - d) * i
        real = self.real - other.real
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        # (a * c + b * d)/(c^2 + d^2) + (b * c - a * d)/(c^2 + d^2) * i
        divisor = (other.real**2 + other.imaginary**2)
        real = ((self.real * other.real + self.imaginary * other.imaginary) /
                divisor)
        imaginary = ((self.imaginary * other.real -
                      self.real * other.imaginary) /
                     divisor)
        return ComplexNumber(real, imaginary)

    def __abs__(self):
        # sqrt(a^2 + b^2)
        return math.sqrt(self.imaginary**2 + self.real**2)

    def conjugate(self):
        # a - b * i
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        # exp(a) * exp(i * b), with
        # exp(i * b) = cos(b) + i * sin(b)
        real = math.exp(self.real) * math.cos(self.imaginary)
        imaginary = math.exp(self.real) * math.sin(self.imaginary)
        return ComplexNumber(real, imaginary)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
