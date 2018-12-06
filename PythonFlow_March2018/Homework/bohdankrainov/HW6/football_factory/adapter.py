import random
from Homework.bohdankrainov.HW6.football_factory.players import *


class Maradonna(object):

    def __init__(self, action):
        self.action_name = action

    @staticmethod
    def possible_actions():
        return {'shoot_penalty', 'free_kick', 'dribbling', 'corner kick'}

    @classmethod
    def player_action(cls, name, act):
        if name in cls.possible_actions():
            return act < 93
        else:
            return act < 75


class PlayerAdapter(object):

    def __init__(self, player, **updated_methods):
        self.player = player
        self.__name__ = player.__name__
        for m in updated_methods:
            setattr(self.player, m, updated_methods[m])

    def __getattr__(self, attr):
        return getattr(self, attr)

    def __str__(self):
        return self.player.__name__

    def __call__(self, *args, **kwargs):
        return self.player


all_player_to_test = [FrankLampard, LeoMessi, DavidBeckham, GiGiBuffon,
                      PlayerAdapter(Maradonna, _action=Maradonna.player_action)]

res = []

for i in all_player_to_test:
    res.append((i.__name__, i()._action('free_kick', random.randint(1, 100))))

print('Free Kick results:', res)
