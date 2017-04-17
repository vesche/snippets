#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    a, b = line.split('=')
    a, b = a.split(), b.split()
    
    try:
        if eval(''.join(a)) == eval(''.join(b)):
            print 'True:   ' + line
        else:
            print 'False:  ' + line
    except:
        print 'Error:  ' + line