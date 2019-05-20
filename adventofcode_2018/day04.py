#!/usr/bin/env python

from datetime import datetime
from collections import Counter

data = [i for i in open('day04.input').read().splitlines()]

parsed = {}
for line in data:
    dt, msg = line.split(']')
    parsed[dt] = msg

days_sorted = sorted(parsed, key=lambda day: datetime.strptime(day[1:], "%Y-%m-%d %M:%S"))
guards = {}
current_guard = None

for i in range(len(days_sorted)):
    dt = days_sorted[i]
    min_a = int(dt.split(':')[1])
    msg = parsed[dt]
    if 'Guard' in msg:
        current_guard = int(msg.split()[1][1:])
    if current_guard not in guards:
        guards[current_guard] = []
    if 'asleep' in msg:
        min_b = int(days_sorted[i+1].split(':')[1])
        guards[current_guard] += range(min_a, min_b)

sleepy_guard = max(guards, key=lambda x:len(guards[x]))
m = Counter(guards[sleepy_guard])
sleepy_max = max(m, key=m.get)
print(sleepy_guard * sleepy_max)

most_mins = 0
for guard, mins in guards.items():
    m = Counter(mins)
    for k, v in m.items():
        if v > most_mins:
            most_mins = v
            saved_guard = guard
            saved_min = k

print(saved_guard * saved_min)

