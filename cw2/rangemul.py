#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    a, b, c = map(int, line.split())
    
    numbs = []
    for i in range(a, c):
        if (i % a == 0) and (i % b == 0):
            numbs.append(i)
    print numbs