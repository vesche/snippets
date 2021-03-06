#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#################################
# Advent of Code, Day 06 - Part 2
# https://github.com/vesche
#################################


coords = {}
for x in range(1000):
    for y in range(1000):
        coords[(x,y)] = 0


def lights(update, a, b, c, d):
    for X in range(int(a), int(c)+1):
        for Y in range(int(b), int(d)+1):
            if update == "on":
                coords[(X,Y)] += 1
            elif update == "off":
                if coords[(X,Y)] > 0:
                    coords[(X,Y)] -= 1
            else:
                coords[(X,Y)] += 2


def main():
    with open("day06_input.txt", 'r') as f:
        for i in f.read().splitlines():
            i = i.split()

            if i[0] == "turn":
                update = i[1]
                a, b = i[2].split(',')
                c, d = i[4].split(',')
                lights(update, a, b, c, d)
            else:
                update = i[0]
                a, b = i[1].split(',')
                c, d = i[3].split(',')
                lights(update, a, b, c, d)

    brightness = 0
    for i in coords:
        brightness += coords[i]
    print brightness


if __name__ == "__main__":
    main()
