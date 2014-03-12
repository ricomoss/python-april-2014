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

        self.report = {
            'p1_dmg_done': 0,
            'p2_dmg_done': 0,
            'winner': None,
            'round': 1,
        }

        for key, val in kwargs:
            setattr(self, key, val)
            self.report[key] = val

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
