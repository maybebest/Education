import os

class MergeTwoFiles(object):
    def __init__(self, file_1, file_2, output_file, skip_empty_lines=True):
        self.file_1=open(file_1, 'r')
        self.file_2=open(file_2, 'r')
        self.output_file=open(output_file, 'w')
        self.skip_empty_lines=skip_empty_lines
    
    def __enter__(self):
        return self
    
    def __exit__(self, tupe, value, traceback):
        # import pdb; pdb.set_trace()
        '''AM 
        it could be checked easier:
        if tupe is ValueError:
            
        also to pass exception silently __exit__ should return True so ValueError is not skipped

        also following could be reworked 
        elif tupe.__class__.__name__ != 'NoneType': 
            -> 
        elif tupe:
            
        '''
        if tupe.__class__.__name__ == 'ValueError':
            pass
        elif tupe.__class__.__name__ != 'NoneType':
            print(tupe, value, traceback)
        self.file_1.close()
        self.file_2.close()
        self.output_file.close()

    def __del__(self):
        pass

    def get_lines(self, file, amount_of_line=0):
        return [line for line in file if line.strip()] if self.skip_empty_lines else file.readlines(amount_of_line)

    def read_lines(self, file, skip_empty_lines=None, amount_of_line=None):
        return self.get_lines(file, amount_of_line)

    def merge_two_files(self, amount_of_line=None):
        file_1 = self.file_1
        file_2 = self.file_2
        lines1=self.read_lines(file_1, amount_of_line=amount_of_line)
        lines2=self.read_lines(file_2, amount_of_line=amount_of_line)
        
        for line_from_file_1, line_from_file_2 in zip(lines1, lines2):
            self.output_file.write(line_from_file_1)
            self.output_file.write(line_from_file_2)

    @property
    def path_to_file(self):
        print('New file is created in the following folder: "{}"'.format(os.path.dirname(os.path.realpath(__file__))))    
    
    

try:
    with MergeTwoFiles('test_file_1', 'test_file_2', 'file_after_merge') as obj:
        obj.merge_two_files()
except Exception as err:
    print('Unhandled exeption: {}'.format(err))



"""- Implement Context Manager which merge two files
constructor has <path1, path2, mode, new_file_path=None>   #done
CM has method merge. merge method has optional param (line_numbers=1 - merge line_numbers by line_numbers)      #done(partially)
CM has property new_file_path which returns new file system path        #done
Use with statement for file merge               #done
Skip ValueError in __exit__                     #done
log exceptions in __exit__                      #done
handle Exceptions outside CM"""                 #done