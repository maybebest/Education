import os

'''AM
Requirement is not implemented:
Function should:
"Retrieve path1, path2, new_filename, returns folder system path."
'''
def only_dup():
    new_list = []
    with open('fileA.py', 'r+')as file1, open('fileB.py', 'r+')  as file2, open('new.py', 'w+') as file3:
        lines1 = [f.strip() for f in file1.readlines() if f.strip()]
        lines2 = [f.strip() for f in file2.readlines() if f.strip()]
        for some in lines1:
            if some in lines2:
                new_list.append(some)
        file3.writelines(new_list)
        return os.path.abspath(os.path.dirname(file3.name))

print(only_dup())

'''AM
Requirement is not implemented:
Function should:
"Retrieve path1, path2, new_filename, skip_empty_lines returns folder system path."
"Empty lines may be skipped (optional, defined by default function arg)."
'''
def merge():
    try:
        with open('Homework_lecture1.py', 'r+')as file1, open('Homework_lecture2.py', 'r+')  as file2, open('new2.py', 'w+') as file3:
            lines1 = file1.readlines()
            lines2 = file2.readlines()
            while True:
                line1 = lines1.pop(0) if lines1 else None
                line2 = lines2.pop(0) if lines2 else None

                if line1 is None and line2 is None:
                    break
                if line1:
                    file3.write(line1)
                if line2:
                    file3.write(line2)
            return os.path.abspath(os.path.dirname(file3.name))
    except FileNotFoundError:
        print('NoFile')
    except IOError:
        print('Writing Failed')
    except:
        raise Exception('Brown Allert!!!')
print(merge())