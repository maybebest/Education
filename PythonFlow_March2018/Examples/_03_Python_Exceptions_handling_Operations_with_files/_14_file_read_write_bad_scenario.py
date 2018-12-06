"""Reading and Writing Files. Very bad scenario"""

files = [open("python_feedback", 'w') for i in range(1000)]
# range(10000) - OSError: [Errno 24] Too many open files: 'python_feedback'

for file in files:
    file.write("Python is awesome! %d" % files.index(file))
