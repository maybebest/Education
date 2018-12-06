"""Reading and Writing Files. Bad scenario"""

FILE = open("python_feedback", 'w+')
FILE_2 = open("python_feedback", 'w+')

FILE.write("Python is awesome!")
FILE_2.write("Yeah its great!!")

FILE.seek(0)
FILE_2.seek(0)

print("FILE. Read Line is: ", FILE.readlines())
# FILE. Read Line is:  ['Yeah its great!!e!']

print("FILE_2. Read Line is: ", FILE_2.readlines())
# FILE_2. Read Line is:  ['Yeah its great!!e!']
