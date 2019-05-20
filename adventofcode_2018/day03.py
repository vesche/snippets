#!/usr/bin/env python

data = [i for i in open('day03.input').readlines()]
fabric = [[0]*1000 for i in range(1000)]

def get_x_y_w_h(line):
    _, _, coord, dim = line.split()
    x, y = map(int, coord[:-1].split(','))
    w, h = map(int, dim.split('x'))
    return x, y, w, h

for line in data:
    x, y, w, h = get_x_y_w_h(line)
    for row in range(h):
        for col in range(w):
            fabric[y+row][x+col] += 1

# part 1
overlap = 0
for strip in fabric:
    for inch in strip:
        if int(inch) >= 2:
            overlap += 1
print(overlap)

# part 2
for line in data:
    x, y, w, h = get_x_y_w_h(line)
    failed = False
    for row in range(h):
        for col in range(w):
            try:
                if fabric[y+row][x+col] != 1:
                    failed = True
            except IndexError:
                failed = True
    if not failed:
        print(line.split()[0])
