"""- Implement Singleton metaclass
  which may be used as metaclass for other classes making their instances Singletons"""

from abc import ABCMeta, abstractmethod

class ISportsman(object, metaclass=ABCMeta):
    @abstractmethod
    def run(self, value): pass

    @abstractmethod
    def jump(self, value): pass

    @abstractmethod
    def swim(self, value): pass


'''AM
Singleton should be implemented using Metaclass functionality

class SingletonMetaClass(type):
    pass
    #do something
    

class Boxer(ISportsman, metaclass=SingletonMetaClass):  

    def run(self, value): 10
    def jump(self, value): 2
    def swim(self, value): 4

print(Boxer() is Boxer())
print(id(Boxer()))
print(id(Boxer()))
'''
class Boxer(ISportsman):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Boxer, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def run(self, value): 10
    def jump(self, value): 2
    def swim(self, value): 4


print(Boxer() is Boxer())
print(id(Boxer()))
print(id(Boxer()))









