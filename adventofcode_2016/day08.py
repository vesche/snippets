#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code 2016, Day 08
# https://github.com/vesche
#


def main():
    screen = [list('.'*50) for _ in range(6)]

    with open("day08_input.txt") as f:
        for i in f.read().splitlines():
            i = i.split()

            if "rect" in i:
                x, y = map(int, i[1].split('x'))
                for n1 in range(y):
                    for n2 in range(x):
                        screen[n1][n2] = '#'

            elif "column" in i:
                col = int(i[2].replace("x=", ''))
                rot = int(i[4])
                hold = [screen[_][col] for _ in range(6)]
                for _ in range(rot):
                    hold = hold[-1:] + hold[:-1]
                for c in range(6):
                    screen[c][col] = hold[c]

            elif "row" in i:
                row = int(i[2].replace("y=", ''))
                rot = int(i[4])
                for _ in range(rot):
                    screen[row] = screen[row][-1:] + screen[row][:-1]

    for line in screen:
        print ''.join(line)

    total = 0
    for i in screen:
        total += len(''.join(i).replace('.', ''))
    return total


if __name__ == "__main__":
    print main()
