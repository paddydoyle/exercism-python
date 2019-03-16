import random
import string


class Robot(object):
    def __init__(self):
        """
        The self.name format is:
        - two uppercase letters, followed by
        - three digits
        """

        self.name = ''

        self.name += random.choice(string.ascii_uppercase)
        self.name += random.choice(string.ascii_uppercase)
        self.name += random.choice(string.digits)
        self.name += random.choice(string.digits)
        self.name += random.choice(string.digits)

    def reset(self):
        # Reset the RNG, to ensure a unique name even if an external
        # call is made to randome.seed()
        random.seed()

        # Initialise ourself again
        self.__init__()
