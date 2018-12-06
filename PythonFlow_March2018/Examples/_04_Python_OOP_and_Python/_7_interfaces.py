"""OOP. Interface. Recommended"""

from abc import ABC, abstractmethod, abstractproperty

class IIterable(ABC):
    @abstractmethod
    def __iter__(self):
        pass

class ITeamMember(ABC):
    @abstractproperty
    def name(self):
        pass

class Team(IIterable):
    def __init__(self):
        self.__members = []

    def __iter__(self):
        return iter(self.__members)

    def add_member(self, member: ITeamMember) -> None:
        member.name
        return self.__members.append(member)

team = Team()
team.add_member('User1')
team.add_member('User2')

for member in team:
    print(member)
#  User1
#  User2