"""SOLID. ISP"""

from abc import ABC, abstractmethod


class IPrinter(ABC):
    @abstractmethod
    def print(self, item: list):
        pass


class IFax(ABC):
    @abstractmethod
    def fax(self, item: list):
        pass


class IScan(ABC):
    @abstractmethod
    def scan(self, item: list):
        pass


class Machine(IPrinter, IFax, IScan):
    pass
