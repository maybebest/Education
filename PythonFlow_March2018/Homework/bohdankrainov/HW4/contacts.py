from abc import ABC, abstractmethod


class IContact(ABC):
    #
    # def __init__(self, name: str, phone: str):
    #     self.name = name
    #     self.phone = phone

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def phone(self):
        pass


class PhoneBookContact(IContact):

    def __init__(self, name: str, phone: str):
        self.__name = name
        self.__phone = phone

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone


