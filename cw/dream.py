#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()


for line in data:
    out_words = []
    words = line.split()
    
    for word in words:
        lenw = len(word)
        
        if lenw > 3:
            outw = word[-2:] + word[:2]
            
            # outw = word[:2][::-1] + word[2:-2] + word[-2:][::-1]
        else:
            outw = word
        
        out_words.append(outw)
    
    print ' '.join(out_words)