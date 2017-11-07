#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

for line in data:
    n, li = line.split()
    n = int(n)
    li = map(int, li.split(','))
    a = li[n-1]
    new_li = li[n-1:]
    back_li = li[:n-1]
    
    print back_li
    
    for i in new_li:
        if i > a:
            print i
            break
        else:
            for x in back_li:
                if x > a:
                    print x
                    break