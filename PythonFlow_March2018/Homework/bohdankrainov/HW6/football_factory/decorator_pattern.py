from Homework.bohdankrainov.HW6.football_factory.players import *


class PlayerFormUpdate(object):

    form_values = {'bad': 0.5, 'good': 2}
    form = None

    def __new__(cls, player, new_form: str):
        cls.form = cls.form_values.get(new_form, None)
        if cls.form:
            setattr(player, 'player_form', cls.form)
        else:
            return 'ERROR'
        return player


print(FrankLampard, FrankLampard.__dict__)
GoodFrank = PlayerFormUpdate(FrankLampard, 'good')
print(GoodFrank, GoodFrank.__dict__)
