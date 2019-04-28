#!/usr/bin/env python

from itertools import cycle

data = [int(i) for i in open('day01.input').readlines()]
print(sum(data))

frequency = 0
freq_seen = set()

for i in cycle(data):
    freq_seen.add(frequency)
    frequency += i
    if frequency in freq_seen:
        print(frequency)
        break
