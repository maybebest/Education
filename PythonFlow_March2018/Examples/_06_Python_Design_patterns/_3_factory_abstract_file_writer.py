from abc import ABCMeta, abstractmethod, abstractstaticmethod


class AbstractFileWriter(object, metaclass=ABCMeta):
    """Abstract class for file writers"""
    @abstractstaticmethod
    def mode(): pass

    @abstractstaticmethod
    def supported_types(): pass

    def __init__(self, path, value):
        self.path, self.value = path, value

    def write(self):
        with open(self.path, self.mode()) as file:
            self._write(file, self.value)

    @abstractmethod
    def _write(self, file, value):
        pass
