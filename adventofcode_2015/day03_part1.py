#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#################################
# Advent of Code, Day 03 - Part 1
# https://github.com/vesche
#################################


def main():
    loc = 0
    locations = {0:1}

    with open("day03_input.txt", 'r') as f:
        for direction in f.read():
            if direction == '^':
                loc += 1000
            elif direction == 'v':
                loc -= 1000
            elif direction == '>':
                loc += 1
            elif direction == '<':
                loc -= 1
            try:
                locations[loc] += 1
            except KeyError:
                locations[loc] = 1

    print len(locations)


if __name__ == "__main__":
    main()
