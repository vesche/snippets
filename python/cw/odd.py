#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    s = ''
    a, b = map(int, line.split())
    
    x, y = 0, 1
    while b > x:
        if (a >= x) and (x%2 != 0):
            s += str(x)
        
        x, y = y, x+y
    
    print s
    