import os
import tempfile

class File:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def write(self, data):
        #print(self.path_to_file, os.path.normcase(self.path_to_file))
        #Ложит куда нужно
        #path_file = tempfile.gettempdir() + os.path.normcase(self.path_to_file)
        #Ложит в корень главного диска
        path_file = os.path.join(tempfile.gettempdir(), os.path.normcase(self.path_to_file))
        #print(path_file)
        
        with open(path_file, 'w') as f:
            f.write(data)

    def __add__(self, obj):
        print(str(obj))
        path_obj = os.path.join(tempfile.gettempdir(), os.path.normcase(str(obj)))
        path_file = os.path.join(tempfile.gettempdir(), os.path.normcase(self.path_to_file))
        path_new_file = os.path.join(tempfile.gettempdir(), "new_file")
        
        with open(path_obj, 'r+') as f:
            data_obj = f.read()
            print(data_obj)

        with open(path_file, 'r+') as f:
            data_file = f.read()
            print(data_file)
        

        with open(path_new_file, 'w') as f:
            f.write(data_obj)
            f.write(data_file)

    def __iter__(self):
        pass

    def __str__(self):
        return self.path_to_file


def _main():
    #obj = File('/file.txt')
    #print(obj)
    #obj.write('line\n')

    first = File('/first.txt')
    first.write("I'm first")
    second = File('/second.txt')
    second.write("I'm second")

    new_obj = first + second
    


if __name__ == "__main__":
    _main()

