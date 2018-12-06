"""Exception Handling"""


def change_file(path, mode, value):
    try:
        file = open(path, mode)
        try:
            file.write(value)
        finally:
            file.close()
    except IOError as err:
        print('Something went wrong! args: [%s, %s, %s]' % (path, mode, value))
        print(err)
    else:
        print("File changed")


change_file("the_Zen_of_Python", "r", "Skip exception handling")
#  Something went wrong! args: [the_Zen_of_Python, r, Skip exception type]
#  not writable

change_file("the_Zen_of_Python", "a", "\nUse exception handling")
#  File changed
