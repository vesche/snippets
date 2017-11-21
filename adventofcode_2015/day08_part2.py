#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code, Day 08 - Part 2
# https://github.com/vesche
#


def main():
    encoded, literal = 0, 0

    with open("day08_input.txt") as f:
        lines = f.read().splitlines()

    for line in lines:
        extra = 4
        for char in line[1:-1]:
            if char == "\\" or char == '"':
                extra += 1

        encoded += len(line) + extra
        literal += len(line)

    print encoded - literal


if __name__ == "__main__":
    main()
