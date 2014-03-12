import random

from to_battle import constants


# Refactored for Exercise 1 and Advanced Exercise 1
class Player(object):
    def __init__(self, name=None, level=1, **kwargs):
        self.name = name
        if not isinstance(level, int):
            raise TypeError('The player level must be an integer.')
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


class Hero(Player):
    def __init__(self, **kwargs):
        if kwargs.get(name) not in constants.PLAYER_NAME_CHOICES:
            raise KeyError('The player must be one of the possible choices.')
        super(Hero, self).__init__(**kwargs)


class Villain(Player):
    def __init__(self, **kwargs):
        if kwargs.get(name) != constants.THANOS:
            raise ValueError(
                'The only villian currently available is {}'.format(
                    constants.THANOS))
        super(Villain, self).__init__(**kwargs)

    def attack(self):
        return random.uniform(1500, 3000)

    def set_health(self):
        setattr(self, 'health', 150000)
