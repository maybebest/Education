"""Custom ContextManager Interface"""
from abc import ABC, abstractmethod


class IContextManager(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, *exc):
        """input params (type, value, traceback) """
        pass

