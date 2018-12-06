from Homework.bohdankrainov.HW6.football_factory.players import *
import random


class PenaltyShootoutFacade(object):

    __first_team = []
    __second_team = []

    def __init__(self, first: list, second: list):
        self.__first_team.extend(first)
        self.__second_team.extend(second)

    def start(self):
        assert len(self.__first_team) == len(self.__second_team), 'Count of members in teams are not equal'
        res = [0, 0]
        for i in range(len(self.__first_team)):
            print(self.__first_team[i].__name__)
            if self.__first_team[i]('after_match', '120')._action(name='shoot_penalty', act=random.randint(1, 100)):
                res[0] += 1
            print(res)
            print(self.__second_team[i].__name__)
            if self.__second_team[i]('after_match', '120')._action(name='shoot_penalty', act=random.randint(1, 100)):
                res[1] += 1
            print(res)
        return res


penalty_shootout = PenaltyShootoutFacade([LeoMessi, GiGiBuffon], [DavidBeckham, FrankLampard])
print('RESULT:', penalty_shootout.start())
