"""Logger Interface"""

from abc import ABCMeta, abstractmethod


class ILogger(object, metaclass=ABCMeta):
    @abstractmethod
    def info(self, value): pass

    @abstractmethod
    def warn(self, value): pass

    @abstractmethod
    def error(self, value): pass
