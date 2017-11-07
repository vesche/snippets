#!/usr/bin/env python

import sys
import calendar


with open(sys.argv[1]) as f:
    data = f.read().splitlines()

d = {}

for line in data:
    for year in line.split():
        r_year = year.split('-')
        if len(r_year) == 2:
            for y in range(int(r_year[0]), int(r_year[1])+1):
                d[str(y)] = calendar.isleap(y)
        else:
            d[year] = calendar.isleap(int(year))

for k,v in sorted(d.items()):
    print '{:>4}: {}'.format(k, v)