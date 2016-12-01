#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Advent of Code 2016, Day 01 - Part 2
# https://github.com/vesche
######################################

def main():
    #    N, E, S, W
    d = [0, 0, 0, 0]
    facing = 0
    locations = []
    
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
        
        for i in range(1, blocks+1):
            if facing == 0:
                d[0] += 1
            elif facing == 1:
                d[1] += 1
            elif facing == 2:
                d[2] += 1
            elif facing == 3:
                d[3] += 1
            
            x, y = d[1] - d[3], d[0] - d[2]
            locations.append([x, y])
            
            if locations.count([x, y]) == 2:
                return abs(x) + abs(y)


if __name__ == "__main__":
    print main()
