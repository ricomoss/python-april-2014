import random


# Refactored for Exercise 1 and Advanced Exercise 1
class Player(object):
    def __init__(self, name=None, level=1, **kwargs):
        self.name = name
        self.level = level
        self.set_health()
        for key, val in kwargs:
            setattr(self, key, val)

    def attack(self):
        return int(random.uniform(10, 50) * self.level)

    def set_health(self):
        setattr(self, 'health', 500 * pow(self.level, 2))

    def __str__(self):
        return self.name


