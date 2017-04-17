#!/usr/bin/env python

import sys
# from string import ascii_lowercase, ascii_uppercase
# letters = ascii_lowercase + ascii_uppercase

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    words = line.split()
    
    line_words = []
    
    for word in words:
        #word_length = 0
        #for letter in word:
        #    if letter in letters:
        #        word_length += 1
        #if word_length > 3:
        #    rotate = word[1:3]
        
        #try:
        rotate = word[1:3]
        #except:
        #   rotate = word[1:2]
        
        line_words.append(rotate + word[0] + word[3:])
    
    print ' '.join(line_words)
        