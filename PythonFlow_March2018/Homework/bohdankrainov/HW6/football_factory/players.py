from Homework.bohdankrainov.HW6.football_factory.absplayer import AbstractPlayer


class LeoMessi(AbstractPlayer):

    @staticmethod
    def position():
        return 'RF'

    @staticmethod
    def possible_actions():
        return {'shoot_penalty': 88, 'free_kick': 74}

    def _action(self, name, act: int):
        print('act:', act)
        if name in self.possible_actions():
            act -= 5
        else:
            act += 2
        print(act, 'vs', self.possible_actions().get(name, 50))
        return act < self.possible_actions().get(name, 50)


class GiGiBuffon(AbstractPlayer):

    @staticmethod
    def position():
        return 'GK'

    @staticmethod
    def possible_actions():
        return {'catch_penalty': 70}

    def _action(self, name, act):
        print('Actual:', act)
        if name in self.possible_actions():
            act -= 2
        else:
            act += 4
        print(act, 'vs', self.possible_actions().get(name, 40))
        return act < self.possible_actions().get(name, 40)


class DavidBeckham(AbstractPlayer):

    @staticmethod
    def position():
        return 'RM'

    @staticmethod
    def possible_actions():
        return {'free_kick': 85, 'shoot_penalty': 91}

    def _action(self, name, act):
        print('act:', act)
        if name in self.possible_actions():
            act -= 3
        else:
            act += 4
        print(act, 'vs', self.possible_actions().get(name, 44))
        return act < self.possible_actions().get(name, 44)


class FrankLampard(AbstractPlayer):

    @staticmethod
    def position():
        return 'CM'

    @staticmethod
    def possible_actions():
        return {'free_kick': 80, 'shoot_penalty': 95}

    def _action(self, name, act):
        print('act:', act)
        if name in self.possible_actions():
            act -= 3
        else:
            act += 4
        print(act, 'vs', self.possible_actions().get(name, 55))
        return act < dict(self.possible_actions()).get(name, 55)
