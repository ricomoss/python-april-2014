import random
import os
import sys

from to_battle import constants


# Refactored for Exercise 1 and Advanced Exercise 1
class Player(object):
    def __init__(self, **kwargs):
        if not isinstance(kwargs.get('exp'), int):
            raise TypeError('The player experience must be an integer.')
        for key, val in kwargs.items():
            setattr(self, key, val)
        self.level = self._get_level()
        self.set_health()

    def _get_level(self):
        current_lvl = 1
        exp = 10
        if self.exp < exp:
            return current_lvl
        for lvl in range(2, 11):
            if self.exp > exp:
                current_lvl = lvl
            exp *= 10
        return current_lvl

    def attack(self):
        return int(random.uniform(30, 50) * self.level)

    def set_health(self):
        setattr(self, 'health', 500 * pow(self.level, 2))

    def __str__(self):
        return self.name


class Hero(Player):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        if self.name not in constants.PLAYER_NAME_CHOICES:
            raise KeyError('The player must be one of the possible choices.')
        kwargs['exp'] = self._get_exp()
        super(Hero, self).__init__(**kwargs)

    def grant_exp(self, exp):
        self.exp += exp

    def _get_exp(self):
        filename = os.path.join(
            constants.SAVE_INFO_DIR, '{}.save'.format(self.name))
        try:
            with open(filename) as save_file:
                try:
                    exp = int(save_file.read())
                except ValueError:
                    exp = 0
            return exp
        except FileNotFoundError:
            setattr(self, 'exp', 0)
            self.save_info()
            return self._get_exp()

    def save_info(self):
        filename = '{}/{}.save'.format(constants.SAVE_INFO_DIR, self.name)
        with open(filename, 'w') as save_file:
            save_file.write(str(self.exp))


class Villain(Player):
    def __init__(self, **kwargs):
        if kwargs.get('name') != constants.VILLAIN_NAME:
            raise ValueError(
                'The only villain currently available is {}'.format(
                    constants.VILLAIN_NAME))
        super(Villain, self).__init__(exp=0, **kwargs)

    def grant_exp(self, exp=None):
        pass

    def save_info(self):
        pass

    def attack(self):
        return int(random.uniform(1500, 3000))

    def set_health(self):
        setattr(self, 'health', 150000)
