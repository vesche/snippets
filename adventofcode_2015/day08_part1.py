#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#################################
# Advent of Code, Day 08 - Part 1
# https://github.com/vesche
#################################


def main():
    literal, actual = 0, 0

    with open("day08_input.txt") as f:
        lines = f.read().splitlines()

    for line in lines:
        literal += len(line)
        actual  += len(eval(line))

    print literal - actual


if __name__ == "__main__":
    main()
