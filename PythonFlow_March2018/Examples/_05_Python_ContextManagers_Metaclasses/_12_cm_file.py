"""Context Manager Implementation"""

from _10_context_manager import IContextManager

class FileManager(IContextManager):
    """FileManager class """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.opened_file = open(self.filename, self.mode)

    def __enter__(self):        
        return self

    def __exit__(self, *args):
        self.opened_file.close()
    
    def write(self, value, position=None):
        if position is not None:
            self.opened_file.seek(position, 0)
        self.opened_file.write(value)


with FileManager('test_file', 'w+') as file:
    file.write('foo', 0)


