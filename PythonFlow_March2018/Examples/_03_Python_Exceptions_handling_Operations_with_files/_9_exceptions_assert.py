"""Exception Handling"""

def change_file(path, mode, value):
    """Change the file by passed path and value"""
    try:
        assert value, 'Value is empty'
        # if not value: raise AssertionError('Value is empty')
        file = open(path, mode)
        try:
            file.write(value)
        finally:
            file.close()
    except IOError:
        print('Something went wrong! args: [%s, %s, %s]' % (path, mode, value))
    # except AssertionError:
    #     print('Value is empty')
    else:
        print("File changed")


change_file("the_Zen_of_Python", "a", "")
# AssertionError: Value is empty





