#!/usr/bin/env python
import os.path
import sys

MODULE_ROOT = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, MODULE_ROOT)

from to_battle.player import Player
from to_battle.battle import Battle


if __name__ == '__main__':
    player1 = Player('hero', 1)
    player2 = Player('nemesis', 1)
    battle = Battle(player1, player2)
    battle.do_battle()
