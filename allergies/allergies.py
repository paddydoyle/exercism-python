class Allergies(object):
    # Hash for fast lookup.
    _allergy_scores = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128,
    }

    def __init__(self, score):
        self._score = score

        # Build a list of what we are allergic to, using bitwise AND.
        self._lst = [item for item, sc in self._allergy_scores.items()
                     if sc & self._score]

    def is_allergic_to(self, item):
        if not self._allergy_scores[item]:
            raise ValueError("Unknown allergen: {}".format(item))

        # In the list?
        return item in self._lst

    @property
    def lst(self):
        return self._lst
