import heapq
import random


class Character:
    abilities = ['strength', 'dexterity', 'constitution', 'intelligence',
                 'wisdom', 'charisma']

    def __init__(self):
        # Dynamic attributes ftw
        for ability in self.abilities:
            setattr(self, ability, self._dice_throws())

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        # Return random ability from the list.
        return getattr(self, random.choice(self.abilities))

    def _dice_throws(self, num=4, sides=6, top=3):
        # 6-sided dice by default, 4 throws, sum top 3
        return sum(heapq.nlargest(top,
                                  (random.randint(1, sides)
                                   for n in range(num))))


def modifier(constitution):
    return (constitution - 10) // 2
