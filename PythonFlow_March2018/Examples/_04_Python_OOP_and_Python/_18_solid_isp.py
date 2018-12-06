"""SOLID. ISP"""
# The code that violates ISP

from abc import ABC, abstractmethod


class IMachine(ABC):
    @abstractmethod
    def print(self, item: list):
        pass

    @abstractmethod
    def fax(self, item: list):
        pass

    @abstractmethod
    def scan(self, item: list):
        pass


class Machine(IMachine):
    pass
