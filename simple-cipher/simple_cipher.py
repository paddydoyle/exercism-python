import random
import string


class Cipher(object):
    def __init__(self, key=None):
        self.key = key

        # If no key is supplied, generate a random string of 100 lowercase
        if not self.key:
            # Reset the RNG
            random.seed()

            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))

        # Instead of just storing the key, more time efficient
        # to convert that directly into a list of offsets and
        # store those as well.
        self.offsets = [ord(k) - ord('a') for k in self.key]

    def encode(self, plaintext):
        cipher = []

        for i, ch in enumerate(plaintext):
            # If the text is longer than the key
            key_index = i % len(self.key)

            # Positive offset
            cipher.append(self._shift_lower_ascii(ch, self.offsets[key_index]))

        return ''.join(cipher)

    def decode(self, ciphertext):
        plain = []

        for i, ch in enumerate(ciphertext):
            # If the text is longer than the key
            key_index = i % len(self.key)

            # Negative offset
            plain.append(self._shift_lower_ascii(ch, -self.offsets[key_index]))

        return ''.join(plain)

    def _shift_lower_ascii(self, char, shift):
        # Get ord of the character.
        # Add the shift, then subtract ord('a') to get a value starting from 0.
        # Reduce that mod 26 for the 26 chars in the latin alphabet.
        # Then add back ord('a') to bring to the range ord(a) - ord(z)
        # And finally turn that back into the char.
        return chr(ord('a') + ((ord(char) + shift) - ord('a')) % 26)
