"""OOP. Interface"""

from abc import ABC, abstractmethod
class IIterable(ABC):
    @abstractmethod
    def __iter__(self):
        pass

class Team(IIterable):
    def __init__(self):
        self.__members = []

    def __iter__(self):
        return iter(self.__members)

    def add_member(self, member):
        return self.__members.append(member)

    @classmethod
    def fromiterable(cls, iterable):
        instance = cls()
        for el in iterable:
            instance.add_member(el)
        return instance

team = Team.fromiterable({'User1', 'User2', 'User2'})

for member in team:
    print(member)
#  User1
#  User2

