from abc import abstractproperty, abstractmethod, ABC

from Homework.valeriybutorin.hw4.entities.contact import Contact


class AbstractCall(ABC):
    @abstractmethod
    def call(self, contact: Contact):
        pass

    @abstractproperty
    def recent_calls(self):
        pass
