from Homework.bohdankrainov.HW6.football_factory.players import *
from Homework.bohdankrainov.HW6.football_factory.absplayer import AbstractPlayer
import os


class PlayGenerator(object):

    players = []
    all_actions = []

    def __init__(self, file_name):
        self.file = file_name
        print(os.getcwd())
        self.report = open(self.file, 'w+')

    def __enter__(self):
        print('__enter__')
        return self

    @classmethod
    def add_player(cls, player: AbstractPlayer):
        cls.players.append(player)

    def action(self, action=None):
        if not action:
            action_ind = input('Enter action index\n{0}:\n>>>'.format(self.get_all_actions))
            action = self.all_actions[int(action_ind)]
        minute = input('Enter minute:\n>>>')
        sel = input("Select Player by index for '{0}':\n{1}\n>>>".format(action, [i.__name__ for i in self.players]))
        player = self.players[int(sel)](action, minute)
        print(player.__dict__, player)
        self.report.write('\n{0} min ::: {1} -> {2}\n'.format(minute, player.__class__.__name__, action))
        self.report.write(player.action())
        if input("Next action? ('y' for continue)") == 'y':
            self.action()

    @property
    def get_all_actions(self):
        for p in self.players:
            for i in list(p.possible_actions().keys()):
                if i not in self.all_actions:
                    self.all_actions.append(i)
        return self.all_actions

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_tb, exc_type, exc_val, self.report)
        self.report.close()
        print(self.report.closed)


with PlayGenerator('match_report') as PG:
    PG.add_player(LeoMessi)
    PG.add_player(GiGiBuffon)
    PG.add_player(DavidBeckham)
    PG.action('shoot_penalty')
    PG.add_player(FrankLampard)
    PG.action()


print(PG)
