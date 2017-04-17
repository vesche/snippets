#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()


for line in data:
    a, b = map(int, line.split())
    
    x, y = 0, 1
    total = 0
    for i in range(1, b):
        if a <= i:
            if (y%2 != 0):
                total += y
        x, y = y, x+y
    print total