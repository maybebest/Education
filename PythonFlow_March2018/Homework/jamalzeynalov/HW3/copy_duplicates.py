"""
- Implement function which copying only duplication lines from one file two other.
  Retrieve path1, path2, new_filename, returns folder system path.
"""
import collections

import os


def move_duplicates(old_file_path, new_file_path, new_file_name):
    with open(old_file_path, 'r') as old_file:
        lines = [x for x in old_file]
        duplicates = [item for item, count in collections.Counter(lines).items() if count > 1]
    with open(new_file_path, 'w') as new_file:
        '''AM (not for rework)
        Extra comprehension here:
        ''.join([x for x in duplicates]) -> ''.join(duplicates)
        new_file.write(''.join([x for x in duplicates])) -> new_file.writelines(duplicates)
        '''
        new_file.write(''.join([x for x in duplicates]))
    os.rename(new_file.name, new_file_name)
    return "{}\{}".format(os.getcwd(), new_file_name)


print(move_duplicates("test_data", "task_1_new_file", "task_1_new_file"))
