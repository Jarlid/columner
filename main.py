import configparser

from os import listdir
from os.path import isfile

PATH = './files/'
WIDTH = 11
warning_printed = False

try:
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        WIDTH = int(config['DEFAULT']['ColumnWidth'])
    except (KeyError, ValueError):
        pass

except configparser.Error:
    print('config.ini does not exist or has wrong format.')


file_names = [name for name in listdir(PATH) if isfile(PATH + name)]
print('Files:', ', '.join(file_names), sep=' ')
files = [open(PATH + file_name, 'r') for file_name in file_names]

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
            print('ColumnWidth should be bigger')
            warning_printed = True

    out_file.write(' '.join([f'{line:{WIDTH}}' for line in lines]) + '\n')

out_file.close()
input('Process finished. Press ENTER to exit.')
