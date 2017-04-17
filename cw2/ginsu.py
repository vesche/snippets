#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()


for line in data:
    out_words = []
    words = line.split()
    
    for word in words:
        lenw = len(word)

        if lenw%2 == 0:
            outw = word[:lenw/2][::-1] + word[lenw/2:][::-1]
        else:
            ml = word[lenw/2]
            outw = word[:lenw/2][::-1] + ml + word[(lenw/2)+1:][::-1]
        
        out_words.append(outw)
    
    print ' '.join(out_words)