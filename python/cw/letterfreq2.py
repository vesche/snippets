#!/usr/bin/env python

from __future__ import division
import sys
from string import ascii_lowercase

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

d = {}

for line in data:
    for letter in line:
        letter = letter.lower()
        if letter not in ascii_lowercase+' ':
            continue
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1

total = 0
for k,v in d.iteritems():
    total += v
for k,v in d.iteritems():
    d[k] = float('{:.2%}'.format(v/total)[:-1])

for k,v in sorted(d.items(), key=lambda(k,v): (-v, k)):
    print "'{}' {}%".format(k, str(v))
