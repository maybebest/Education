"""Exception Handling"""


class EmptyValueException(Exception):
    pass


def change_file(path, mode, value):
    try:
        if not value:
            raise EmptyValueException()
        file = open(path, mode)
        try:
            file.write(value)
        finally:
            file.close()
    except IOError:
        print('Something went wrong! args: [%s, %s, %s]' % (path, mode, value))
    except EmptyValueException:
        print('Value is empty')
    else:
        print("File changed")


change_file("the_Zen_of_Python", "a", "")
#  Value is empty
