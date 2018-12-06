# Homework 5
"""
- Implement metaclass which logs class, child class and their instances destruction (dispose).
- Also metaclass should add some method to the class. It could be used at class instance.
- Implement Context Manager which merges two files
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
from abc import ABC

CWD = os.getcwd()


class IContextManager(ABC):

    def __enter__(self): pass

    def __exit__(self, *args): pass


'''AM
Interface should not contain any implementation.
Please leave only methods declaration in interface - other code please 
move to the Merger class which implement this interface.

class IContextManager(ABC):
    @abstractemthod
    def __enter__(self):
        pass
    
    @abstractemthod
    def __exit__(self):
        pass

class Merger(IContextManager):
    def __init__(self):
        #do something

    def __enter__(self):
        #do something
    
    def __exit__(self):
        #do something

    def merge(self):
        #do something
'''
class Merger(IContextManager):

    '''AM 2
    [pylint] E0213:Method should have "self" as first argument
    Each method of class should have "self" as first argument
    '''
    def to_parts(lst, lines_to_merge):
        result = []
        iterations = int(len(lst)/lines_to_merge)
        start = 0
        end = 0 + lines_to_merge
        for i in range(iterations):
            result.append(lst[start:end])
            start += lines_to_merge
            end += lines_to_merge
        result.append(lst[start:])
        return result

    def format_output(lst):
        final = (str(lst))
        final = (final.replace("], [", "\r\n"))
        final = final.replace("], [", "\r\n")
        final = final.replace("[([", "")
        final = final.replace("])]", "")
        final = final.replace("'", "")
        final = final.replace("]), ([", "\r\n")
        return final

    def trim_new_lines(lst):
        trimmed = []
        for i in lst:
            trimmed.append(str(i).replace("\n", ""))
        return trimmed

    def merge(self, lines_to_merge=1):
        lines1 = self.f1.readlines()
        lines2 = self.f2.readlines()
        lines1 = self.trim_new_lines(lines1)
        lines2 = self.trim_new_lines(lines2)
        toadd1 = self.to_parts(lines1, lines_to_merge)
        toadd2 = self.to_parts(lines2, lines_to_merge)
        result = list(zip(toadd1, toadd2))
        result = self.format_output(result)
        self.f3.write(str(result))

    def __init__(self, path1, path2, lines_to_merge):
        self.f1 = open(path1)
        self.f2 = open(path2)
        self.f3 = open(CWD+"\\result.txt", "w")
        self.lines_to_merge = lines_to_merge
        self.new_file_path = CWD+"\\result.txt"

    def __enter__(self):
        '''AM 
        Please don't do call merge method in __enter__
        Please return here something which could be used in with statement
        '''
        '''AM 2 
        please return "self" here
        '''
        return str(self.new_file_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f1.close()
        self.f2.close()
        self.f3.close()
        '''AM
        All types of exceptions should be logged
        only ValueError should be skipped
        '''
        if not exc_type == ValueError:
            print("Exception type:", exc_type)
            print("Exception value:", exc_val)
            print("Exception traceback:", exc_tb)


'''AM
    1) Please call merge method inside with statement
    with Merger(CWD+"\\file1.txt", CWD+"\\file2.txt", 3) as m:
        m.merge()
    2) "handle Exceptions outside CM" requirement is not implemented
'''

try:
    with Merger(CWD+"\\file1.txt", CWD+"\\file2.txt", 3) as m:
        '''AM 2
        [pylint] E1101:Instance of 'str' has no 'merge' member
        m here is an object which is returned from __enter__
        '''
        m.merge()
except Exception as ex:
    print("An error has occurred:", ex)
