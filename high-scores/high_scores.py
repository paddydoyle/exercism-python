class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

        # Store the top 3 scores on construction (doesn't look
        # like we need to update the list after creation).
        self.top = sorted(scores, reverse=True)[0:3]

        # self.highest = max(scores)

    def personal_best(self):
        # Use stored values. Will break if we can update the list.
        return self.top[0]

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        # Use stored values. Will break if we can update the list.
        return self.top

    def report(self):
        # Temp variable, just to avoid re-calling the function
        latest = self.latest()

        if latest == self.personal_best():
            return "Your latest score was {}. ".format(latest) + \
                    "That's your personal best!"
        else:
            return "Your latest score was {}. ".format(latest) + \
                    "That's {} short of your personal best!".format(
                            self.personal_best() - latest)
