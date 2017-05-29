#!/usr/bin/env python

from itertools import permutations

with open('314_easy_input.txt') as f:
    data = f.read().splitlines()

for line in data:
    numbs = line.split()
    combos = [''.join(i) for i in permutations(numbs)]
    combos = map(int, combos)

    print '{} {}'.format(min(combos), max(combos))
