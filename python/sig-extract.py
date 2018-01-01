import os

PASSWORD = 'soitgoes'

for f in os.listdir('.'):
    if os.path.isfile(f):
        if ('part1.' in f) or ('part01.' in f) or ('part' not in f):
            print('Extracting {}...'.format(f))
            os.system('unrar x {} -p{}'.format(f, PASSWORD))
