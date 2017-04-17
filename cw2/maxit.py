#!/usr/bin/env python

import itertools
import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

ops = ['+', '-', '*', '/']

for line in data:
    a, b, c, d, e = line.split(',')
    
    high = '0'
    for i in itertools.permutations(ops):
        w, x, y, z = i
        test = eval(a + w + b + x + c + y + d + z + e)
        if test > eval(high.split()[0]):
            high = "{:>10.2f} ('{}', '{}', '{}', '{}')".format(test, w, x, y, z)
    
    print high