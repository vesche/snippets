#!/usr/bin/env python

# Unfinished

import math
from collections import Counter

data = [tuple(map(int, i.split(', '))) for i in open('day06.input').read().splitlines()]
max_x = max([x for x, y in data])
max_y = max([y for x, y in data])
coords = {(x, y):[] for x in range(max_x) for y in range(max_y)}

for x1, y1 in coords.keys():
    d = {math.hypot(x2 - x1, y2 - y1):data.index((x2, y2)) for x2, y2 in data}
    man_dist = min(d.keys())
    coords[(x1, y1)].append(d[man_dist])

disq = set()
for x, y in coords:
    # remove overlap
    if len(coords[(x, y)]) == 1:
        coords[(x, y)] = coords[(x, y)][0]
    else:
        coords[(x, y)] = []
    # infinte areas
    if (x == 0) or (x == max_x) or (y == 0) or (y == max_y):
        disq.add(coords[(x, y)])

count = Counter(coords.values())
max_count = min(count.values())
for k, v in count.items():
    if (v > max_count) and (k not in disq):
        max_count = v
print(max_count)
