

"""Context Manager Implementation"""

from _10_context_manager import IContextManager


class FileManager(IContextManager):
    """FileManager class """

    def __init__(self, filename, mode):
        self.filename, self.mode = filename, mode
        self.opened_file = open(self.filename, self.mode)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(exc_type)       # <class 'ValueError'>
        print(exc_value)      # negative seek position -5
        print(exc_traceback)  # <traceback object at 0x7f84c49a4248>

        self.opened_file.close()

    def write(self, value, position=None):
        if position is not None:
            self.opened_file.seek(position, 0)
        self.opened_file.write(value)

    @property
    def closed(self):
        return self.opened_file.closed

###########################################


try:
    with FileManager('test_file', 'w+') as file:
        file.write('foo', -5)
except Exception:
    print(file.closed)
    # True
