from os import listdir
from os.path import isfile

PATH = './files/'
WIDTH = 11
warning_printed = False

file_names = [name for name in listdir(PATH) if isfile(PATH + name)]
print('Files:', ', '.join(file_names), sep=' ')
files = [open('files/' + file_name, 'r') for file_name in file_names]

out_file = open('file.txt', 'w')
out_file.write(' '.join([f'{name:{WIDTH}}' for name in file_names]) + '\n')

while True:
    lines = [file.readline().split('\n')[0] for file in files]

    empty = [len(line) == 0 for line in lines]
    if min(empty):
        break

    if not warning_printed:
        too_wide = [len(line) > WIDTH for line in lines]
        if max(too_wide):
            print('WIDTH should be bigger')

    out_file.write(' '.join([f'{line:{WIDTH}}' for line in lines]) + '\n')

input('Process finished. Press ENTER to exit.')
