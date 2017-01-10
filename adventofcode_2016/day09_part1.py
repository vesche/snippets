#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Advent of Code 2016, Day 09 - Part 1
# https://github.com/vesche
######################################

def main():
    l = 0
    extra = 0

    with open("day09_input.txt") as f:
        data = f.read().rstrip()

    data = data.replace('(', ' ').replace(')', ' ').split()

    for i in range(len(data)):
        c = data[i]
        if 'x' in c:
            x, y = map(int, c.split('x'))
            extra += len(data[i+1][:x]*(y-1))
        else:
            l += len(c)

    return l + extra

if __name__ == "__main__":
    print main()
