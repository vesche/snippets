#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

switch = [0, 1]

for line in data:
    line_words = []
    for word in line.split():
        if switch[0]:
            word = word[::-1]
            
        line_words.append(word)
        switch = switch[::-1]
    print ' '.join(line_words)