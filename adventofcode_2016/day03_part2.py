#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code 2016, Day 03 - Part 2
# https://github.com/vesche
#

from collections import Counter
from itertools import combinations


def main():
    valid = 0

    with open("day03_input.txt") as f:
        data = f.read().rstrip().split('\n')
        data = ['\n'.join(data[i:i+3]) for i in range(0, len(data), 3)]

        for line in data:
            ta, tb, tc = [], [], []
            for i in line.split('\n'):
                x, y, z = i.split()
                ta.append(x); tb.append(y); tc.append(z)

            for triangle in [ta, tb, tc]:
                triangle = map(int, triangle)

                invalid = False
                for case in combinations(triangle, 2):
                    side = list(Counter(triangle) - Counter(case))[0]
                    if sum(case) <= side:
                        invalid = True; break

                if not invalid:
                    valid += 1

    return valid


if __name__ == "__main__":
    print main()
