#!/usr/bin/env python
import random
import os.path
import sys

MODULE_ROOT = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, MODULE_ROOT)

from class4.utils import pretty_print


# For exercise 1
class Human(object):
    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color

    def set_name(self, new_name):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def set_hair_color(self, new_hair_color):
        self.hair_color = new_hair_color


# For exercise 1
class Cat(object):
    def __init__(self, name, gender, breed, owner):
        self.name = name
        self.gender = gender
        self.breed = breed
        if isinstance(owner, Human) or owner is None:
            self.owner = owner

    def set_name(self, new_name):
        self.name = new_name

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_breed(self, new_breed):
        self.breed = new_breed

    def set_owner(self, new_owner):
        if isinstance(new_owner, Human) or new_owner is None:
            self.owner = new_owner


def exercise2(objs):
    for obj in objs:
        if isinstance(obj, Cat):
            obj.set_owner(None)


def exercise3(objs):
    for obj in objs:
        if isinstance(obj, Cat):
            if obj.owner is None:
                human = Human('Paul', '22', 'Brown')
                obj.set_owner(human)


# For Advanced Exercise 1
class Player(object):
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 500

    def attack(self):
        return int(random.uniform(10, 50) * self.level)

    def __str__(self):
        return self.name


# For Advanced Exercise 1
class Battle(object):
    def __init__(self, p1, p2):
        if isinstance(p1, Player) and isinstance(p2, Player):
            self.p1 = p1
            self.p2 = p2
        else:
            msg = '{} expects type {} for player.'.format(
                Battle.__name__, Player.__name__)
            raise TypeError(msg)

        self.report = {
            'p1_dmg_done': 0,
            'p2_dmg_done': 0,
            'winner': None,
            'round': 1,
        }

    def handle_attack(self):
        p1_dmg_done = self.p1.attack()
        p2_dmg_done = self.p2.attack()
        self.p1.health -= p2_dmg_done
        self.p2.health -= p1_dmg_done

        self.report['p1_dmg_done'] += p1_dmg_done
        self.report['p2_dmg_done'] += p2_dmg_done

    def determine_winner(self):
        if self.p1.health <= 0 or self.p2.health <= 0:
            if self.report['p1_dmg_done'] > self.report['p2_dmg_done']:
                return self.p1
            elif self.report['p1_dmg_done'] < self.report['p2_dmg_done']:
                return self.p2
            else:
                return 'Tie'

    def print_report(self):
        pretty_print(self.report)

    def do_battle(self):
        winner = None
        while winner is None:
            self.handle_attack()
            winner = self.determine_winner()
            self.report['round'] += 1
        self.report['winner'] = winner
        self.print_report()


if __name__ == '__main__':
    p1 = Player('hero')
    p2 = Player('nemesis')
    battle = Battle(p1, p2)
    battle.do_battle()

