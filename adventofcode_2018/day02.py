#!/usr/bin/env python

data = [i for i in open('day02.input').read().splitlines()]
two = three = 0
similar = set()

for ID in data:
    d = {i:ID.count(i) for i in ID}
    if 2 in d.values(): two += 1
    if 3 in d.values(): three += 1

    for ID2 in data:
        if ID != ID2:
            similar.add(''.join([a for a, b in zip(ID, ID2) if a == b]))

print(two * three)
print(max(similar, key=len))
