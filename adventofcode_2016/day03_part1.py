#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Advent of Code 2016, Day 03 - Part 1
# https://github.com/vesche
######################################

from collections import Counter
from itertools import combinations


def main():
    valid = 0

    with open("day03_input.txt") as f:
        for line in f.read().splitlines():
            triangle = map(int, line.split())

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
