import os


def merge_files(path1, path2, file_name, skip_empty=None):
    try:
        '''AM
        Too many nesting levels, please use following construction
        with open(path1) as file1, open(path2) as file2:
            #do something with file1, file2
        '''
        with open(path1, 'r') as file1, open(path2, 'r') as file2:
            if skip_empty:
                '''AM (not fro rework)
                It could be written easier:
                lines1 = [i for i in file1.readlines() if i.strip()]
                '''
                lines1 = [i for i in file1.readlines() if i.strip()]
                lines2 = [i for i in file2.readlines() if i.strip()]
            else:
                '''AM
                Extra comprehension here
                file1.readlines() returns list            
                '''
                lines1 = file1.readlines()
                lines2 = file2.readlines()
    except FileNotFoundError as err:
        print('==={0}==='.format(err))
    except IOError as err:
        print('Writing to file FAILED', err, err.args)
    except:
        raise Exception('!!!ERROR!!!')
    else:
        assert len(lines1) > 0 and len(lines2) > 0, 'One of files is empty'
        '''AM 
        Too complicated. Following algorithm could be used here:
        while True:
            line1 = lines1.pop(0) if lines1 else None
            line2 = lines2.pop(0) if lines2 else None

            if line1 == None and line2 == None
                break
            if line1:                        
                res_file.write(line1)
            if line2:
                res_file.write(line2)
        '''
        with open(file_name, 'w+') as res_file:
            while True:
                line1 = lines1.pop(0) if lines1 else None
                line2 = lines2.pop(0) if lines2 else None

                if line1 is None and line2 is None:
                    break
                if line1:
                    res_file.write(line1)
                if line2:
                    res_file.write(line2)
        return os.path.abspath(os.path.dirname(res_file.name))


print('Path to result file:', str(merge_files('file1', 'file2', 'merge_file', skip_empty=True)))
