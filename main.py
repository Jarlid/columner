import configparser

from os import listdir
from os.path import isfile

PATH = './files/'
WIDTH = 11

file_names = []

try:
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        file_names = config['DEFAULT']['FileOrder'].split(' ')
    except KeyError:
        pass

    try:
        WIDTH = int(config['DEFAULT']['ColumnWidth'])
    except (KeyError, ValueError):
        pass

except configparser.Error:
    print('config.ini does not exist or has wrong format.')


file_set = set(file_names)
file_names += [name for name in listdir(PATH) if name not in file_set and isfile(PATH + name)]
files = []
opened = []

print('Files:', end=' ')
for i, name in enumerate(file_names):
    try:
        files.append(open(PATH + name, 'r'))
        opened.append(name)
        print(name, end=' ')
    except (FileNotFoundError, PermissionError):
        pass
print()

out_file = open('file.txt', 'w')
out_file.write(' '.join([f'{name:{WIDTH}}' for name in opened]) + '\n')

warning_printed = False
while True:
    lines = [file.readline().split('\n')[0] for file in files]

    empty = [len(line) == 0 for line in lines]
    if min(empty):
        break

    if not warning_printed:
        too_wide = [len(line) > WIDTH for line in lines]
        if max(too_wide):
            print('ColumnWidth should be bigger')
            warning_printed = True

    out_file.write(' '.join([f'{line:{WIDTH}}' for line in lines]) + '\n')

out_file.close()
input('Process finished. Press ENTER to exit.')
