"""Iterables."""

LANG = 'Python'

ITER = iter(LANG)
# ITER = LANG.__iter__()

print(ITER)  # <str_iterator object at 0x7f2264037a58>

print(LANG[0])  # P
print(LANG.__getitem__(0))  # P

#######################################################

FILE = open('<your_file_path>', 'r')

FILE_ITER = iter(FILE)
# FILE_ITER = FILE.__iter__()

# <_io.TextIOWrapper name='<your_file_path>' mode='r' encoding='UTF-8'>
print(FILE_ITER)

for line in FILE:
    print(line)

print(FILE.__getitem__(0))
# AttributeError: '_io.TextIOWrapper' object has no attribute '__getitem__'
