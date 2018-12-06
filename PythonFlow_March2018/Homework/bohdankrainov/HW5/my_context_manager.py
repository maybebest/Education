"""
- Implement Context Manager which merge two files
  constructor has <path1, path2, mode, new_file_path=None>
  CM has method merge. merge method has optional param (line_numbers=1 - merge line_numbers by line_numbers)
  CM has property new_file_path which returns new file system path
  Use with statement for file merge
  Skip ValueError in __exit__
  log exceptions in __exit__
  handle Exceptions outside CM
- Enjoy MetaClasses and CMs!
"""

import os


class ContextManager(object):

    def __init__(self, path1, path2, mode):
        self.path1 = path1
        self.path2 = path2
        self.mode = mode
        self.new_file_path = None

    def __enter__(self):
        return self

    def merge(self, line_numbers=1):
        with open(self.path1, 'r+') as file1, open(self.path2, 'r+') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            print('Lists of file lines to merge:', lines1, lines2, sep='\n')
        '''AM
        What if i pass line_numbers argument with value 3?
        i need to merge 3 lines from first file then 3 lines from second file and continue
        this requirement is not implemented

        '''
        '''AM 2
        To many code duplication. Following code could be placed in a function and reused
        ....
        for i in range(int(line_numbers)):
            line1 = lines1.pop(0) if lines1 else None
            if line1:
                self.new_file_path.write(line1)
        ...
        for i in range(int(line_numbers)):
                    line2 = lines2.pop(0) if lines2 else None
                    if lines2:
                        self.new_file_path.write(line2)

        '''
        self.new_file_path = open(os.getcwd() + '/result', self.mode)
        while len(lines1) > 0 or len(lines2) > 0:
            if lines1:
                lines1 = self.write_lines(lines1, line_numbers)
            if lines2:
                lines2 = self.write_lines(lines2, line_numbers)
        raise ValueError('Should be skipped in __exit__')

    def write_lines(self, list_lines: list, count: int=1):
        for i in range(count):
            line = list_lines.pop(0) if list_lines else None
            if line:
                self.new_file_path.write(line)
            else:
                break
        return list_lines

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        self.new_file_path.close()
        if exc_type.__name__ == 'ValueError':
            return True

    '''AM
    Please do not use methods naming convention for properties
    property names - noun
    method names - verb
    '''
    @property
    def new_path(self):
        if self.new_file_path:
            return os.path.abspath(self.new_file_path.name)
        else:
            return self.new_file_path


try:
    with ContextManager('test_1', 'test_2', 'w+') as ContMan:
        print(ContMan.new_path)
        ContMan.merge(line_numbers=2)
    print('Path to file with result:', ContMan.new_path)
except Exception as exc:
    print('===Exception===')
    print(exc, exc.args, exc.__class__)

