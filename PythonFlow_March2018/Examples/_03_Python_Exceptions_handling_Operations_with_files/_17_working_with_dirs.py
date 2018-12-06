"""Working with dirs"""

import os
from shutil import copyfile

CWD = os.getcwd()
print("Current working dir:", CWD)
# Current working dir: /.../Examples/06.Python_Operations_with_files_Exceptions_handling

print("Files in '%s': %s" % (CWD, os.listdir(CWD)))
# Files in '<path>': ['<file_name_1>', '<file_name_2>', ..., '<file_name_n>']

os.mkdir('files')
os.chdir('files')
os.chdir('..')

os.rmdir('files')

copyfile('python_feedback', 'python_feedback_copy')
