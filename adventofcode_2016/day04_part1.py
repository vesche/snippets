#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code 2016, Day 04 - Part 1
# https://github.com/vesche
#

from collections import Counter


def main():
    total = 0

    with open("day04_input.txt") as f:
        data = f.read().splitlines()

    for line in data:
        line = line.split('-')

        name = ''.join(line[:-1])
        sector = int(line[-1][:3])
        checksum = line[-1][4:9]

        top5 = ''.join([i for i, _ in sorted(Counter(name).most_common(10),
        key=lambda tup: (-tup[1], tup[0]))])[:5]

        if checksum == top5:
            total += sector

    return total


if __name__ == "__main__":
    print main()
