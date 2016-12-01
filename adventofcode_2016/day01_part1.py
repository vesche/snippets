#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Advent of Code 2016, Day 01 - Part 1
# https://github.com/vesche
######################################

def main():
    #    N, E, S, W
    d = [0, 0, 0, 0]
    facing = 0

    with open("day01_input.txt") as f:
        data = f.read().strip().split(', ')
    
    for i in data:
        direction = i[0]
        blocks = int(i[1:])
        
        if direction == 'R':
            facing += 1
        elif direction == 'L':
            facing -= 1
        
        facing %= 4
        d[facing] += blocks
        
    x, y = abs(d[0] - d[2]), abs(d[1] - d[3])
    
    print x + y

if __name__ == "__main__":
    main()
