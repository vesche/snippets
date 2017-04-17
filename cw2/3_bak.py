#!/usr/bin/env python

import sys
from string import ascii_lowercase, ascii_uppercase
letters = ascii_lowercase + ascii_uppercase

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    words = line.split()
    line_words = []
    
    for word in words:
        rotate = word[1:3]
        shit = ''
        for l in rotate:
            if l not in letters:
                rotate.replace(l, ''); word.replace(l, '')
                shit = l
        line_words.append(rotate + word[0] + word[3:] + shit)
    
    print ' '.join(line_words)
