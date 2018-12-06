import random
from abc import ABCMeta, abstractmethod, abstractstaticmethod, abstractproperty


class AbstractPlayer(object, metaclass=ABCMeta):

    @abstractstaticmethod
    def position(self):
        pass

    @abstractstaticmethod
    def possible_actions(self):
        pass

    def __init__(self, action_name=None, minute=None):
        self.action_name = action_name
        self.minute = minute

    def action(self, *args, **kwargs):
        a = random.randint(1, 100)
        res = self._action(self.action_name, a)
        if self.action_name == 'shoot_penalty':
            return "==> {0} scored GOAL from penalty kick!".format(self.__class__.__name__) if res else \
                "==> {} MISSED from penalty kick!".format(self.__class__.__name__)
        elif self.action_name == 'free_kick':
            return "==> {0} scored GOAL from free kick!".format(self.__class__.__name__) if res else \
                "==> {} MISSED from free kick!" .format(self.__class__.__name__)
        return str(res)

    @abstractmethod
    def _action(self, *args, **kwargs):
        pass
