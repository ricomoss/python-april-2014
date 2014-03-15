from copy import deepcopy

from to_battle.player import Player
from to_battle.utils import pretty_print


class Battle(object):
    def __init__(self, p1, p2, **kwargs):
        if isinstance(p1, Player) and isinstance(p2, Player):
            self.p1 = p1
            self.p2 = p2
        else:
            msg = '{} expects type {} for player.'.format(
                Battle.__name__, Player.__name__)
            raise TypeError(msg)

        self.reports = list()
        self.p1_dmg_done_key = '{} dmg_done'.format(self.p1.name)
        self.p2_dmg_done_key = '{} dmg_done'.format(self.p2.name)
        self.p1_hp_key = '{} hp'.format(self.p1.name)
        self.p2_hp_key = '{} hp'.format(self.p2.name)
        self.round_report = {
            self.p1_dmg_done_key: 0,
            self.p2_dmg_done_key: 0,
            self.p1_hp_key: self.p1.health,
            self.p2_hp_key: self.p2.health,
            'winner': None,
            'round': 1,
        }

        for key, val in kwargs:
            setattr(self, key, val)
            self.round_report[key] = val

    def handle_attack(self):
        p1_dmg_done = self.p1.attack()
        p2_dmg_done = self.p2.attack()
        self.p1.health -= p2_dmg_done
        self.p2.health -= p1_dmg_done

        self.round_report[self.p1_dmg_done_key] += p1_dmg_done
        self.round_report[self.p2_dmg_done_key] += p2_dmg_done

    def determine_winner(self):
        if self.p1.health <= 0 or self.p2.health <= 0:
            if self.round_report[self.p1_dmg_done_key] > \
                    self.round_report[self.p2_dmg_done_key]:
                return self.p1
            elif self.round_report[self.p1_dmg_done_key] < \
                    self.round_report[self.p2_dmg_done_key]:
                return self.p2
            else:
                return 'Tie'

    def print_report(self):
        pretty_print(self.reports)

    def assign_exp(self, winner):
        if winner == self.p1:
            self.p1.grant_exp(2)
            self.p2.grant_exp(1)
        else:
            self.p2.grant_exp(2)
            self.p1.grant_exp(1)

    def save_info(self):
        self.p1.save_info()
        self.p2.save_info()

    def do_battle(self):
        winner = None
        while winner is None:
            self.handle_attack()
            winner = self.determine_winner()
            self.round_report['winner'] = winner
            self.round_report[self.p1_hp_key] = self.p1.health
            self.round_report[self.p2_hp_key] = self.p2.health
            self.reports.append(deepcopy(self.round_report))
            self.round_report['round'] += 1
        self.assign_exp(winner)
        self.save_info()
        self.print_report()
