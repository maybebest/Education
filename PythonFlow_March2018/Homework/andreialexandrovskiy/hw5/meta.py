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

'''AM (not for rework)

class M(type):
    def __new__(cls, class_name, bases, attr):
        def __del__(self):
            print('Del instance')

        attr['__del__'] = __del__

        return super().__new__(cls, class_name, bases, attr)
    def __del__(cls):
        print('Dell class')


class A(object, metaclass=M):
    pass    

class B(A):
    pass
B()
'''
class Meta(type):
    def __del__(self):
        print("Deleted")

    def __call__(self, *args, **kwargs):
        return self.method_for_class_instance()

    @classmethod
    def method_for_class_instance(cls):
        print("Method for class instance")


class A(metaclass=Meta):
    pass


class B(A):
    pass

a=A()
b=B()

