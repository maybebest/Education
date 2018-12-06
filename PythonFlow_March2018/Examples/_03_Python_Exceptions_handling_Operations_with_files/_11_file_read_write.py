"""Reading and Writing Files"""

PHRASE = "Python is awesome!\nYeah its great!!\n"

with open("python_feedback", 'w+') as FILE:

    print(len(PHRASE))  # 36

    FILE.write(PHRASE)

    print("Read String is: ", FILE.read(6))  # Read String is:

    print("Current position is: ", FILE.tell())  # Current position is:  36

    FILE.seek(0, 1)
    print("Current position is: ", FILE.tell())  # Current position is:  36

    FILE.seek(0)
    print("Current position is: ", FILE.tell())  # Current position is:  0

    print("Read String is: ", FILE.read(6))  # Read String is:  Python
