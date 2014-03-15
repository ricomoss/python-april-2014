import random

from to_battle import constants


# Refactored for Exercise 1 and Advanced Exercise 1
class Player(object):
    def __init__(self, **kwargs):
        if not isinstance(kwargs.get('level'), int):
            raise TypeError('The player level must be an integer.')
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.set_health()

    def attack(self):
        return int(random.uniform(10, 50) * self.level)

    def set_health(self):
        setattr(self, 'health', 500 * pow(self.level, 2))

    def __str__(self):
        return self.name


class Hero(Player):
    def __init__(self, **kwargs):
        if kwargs.get('name') not in constants.PLAYER_NAME_CHOICES:
            raise KeyError('The player must be one of the possible choices.')
        super(Hero, self).__init__(**kwargs)


class Villain(Player):
    def __init__(self, **kwargs):
        if kwargs.get('name') != constants.VILLAIN_NAME:
            raise ValueError(
                'The only villain currently available is {}'.format(
                    constants.VILLAIN_NAME))
        super(Villain, self).__init__(**kwargs)

    def attack(self):
        return random.uniform(1500, 3000)

    def set_health(self):
        setattr(self, 'health', 150000)
