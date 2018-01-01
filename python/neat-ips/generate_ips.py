#!/usr/bin/env python

with open('ascending.txt', 'w') as f:
    for i in range(1, 252):
        f.write("%d.%d.%d.%d\n" % (i, i+1, i+2, i+3))

with open('descending.txt', 'w') as f:
    for i in range(254, 3, -1):
        f.write("%d.%d.%d.%d\n" % (i, i-1, i-2, i-3))
