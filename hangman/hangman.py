# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        # Store the original word
        self.word = word
        # Masked word list; fill in if guess is correct.
        self.masked_word = ['_'] * len(word)

    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError("Game already lost!")

        if self.status == STATUS_WIN:
            raise ValueError("Game already won!")

        # Lose a guess if not there, or repeat a guessed char
        if char in self.word and char not in self.masked_word:
            # List of indices where the char occurs.
            for i in [pos for pos, ch in enumerate(self.word) if ch == char]:
                # Clear them in the mask
                self.masked_word[i] = char
        else:
            self.remaining_guesses -= 1

        # Have they won? A win on the last guess still counts
        if '_' not in self.masked_word:
            self.status = STATUS_WIN
        elif self.remaining_guesses == -1:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status
