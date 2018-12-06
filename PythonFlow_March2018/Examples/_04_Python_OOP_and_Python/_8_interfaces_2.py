"""OOP. Interface"""

class Iterable(object):
    def __iter__(self):
        raise NotImplementedError(
            'Method __iter__ is not implemented for iterable')

class Team(Iterable):
    def __init__(self):
        self.__members = []

    def __iter__(self):
        return iter(self.__members)

    def add_member(self, member):
        return self.__members.append(member)

team = Team()
team.add_member('User1')
team.add_member('User2')

for member in team:
    print(member)
#  User1
#  User2

