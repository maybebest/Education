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


class MergeCM(object):
    def __init__(self, path1, path2, mode, new_file): pass

    def __enter__(self): pass

    def __exit__(self, exc_type, exc_val, exc_tb): pass

    def merge(self, line_numbers=1):
        """ CM has method merge. merge method has optional param
            (line_numbers=1 - merge line_numbers by line_numbers)
        """
        

