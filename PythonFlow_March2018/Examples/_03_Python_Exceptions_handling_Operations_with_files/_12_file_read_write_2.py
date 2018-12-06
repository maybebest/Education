"""Reading and Writing Files"""

FEEDBACK = ["Python is awesome!", "Yeah its great!!"]

with open("python_feedback", 'w+') as FILE:

    FILE.writelines(map(lambda str: str + '\n', FEEDBACK))

    FILE.seek(0)
    print("Read Line is: ", FILE.readline())
    # Read Line is:  Python is awesome!

    print("Read Lines is: ", FILE.readlines(5))
    # Read Lines is:  ['Yeah its great!!\n']

    FILE.seek(0)
    print("Read Lines is: ", FILE.readlines())
    # Read Lines is:  ['Python is awesome!\n', 'Yeah its great!!\n']
