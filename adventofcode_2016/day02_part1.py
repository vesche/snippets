#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code 2016, Day 02 - Part 1
# https://github.com/vesche
#


def main():
    keypad = range(1,10)
    position = 4

    with open("day02_input.txt") as f:
        for line in f.read().splitlines():
            for move in line:
                if move == 'U' and position > 3:
                    position -= 3
                elif move == 'D' and position < 7:
                    position += 3
                elif move == 'L' and position not in [0, 3, 6]:
                    position -= 1
                elif move == 'R' and position not in [2, 5, 8]:
                    position += 1
            print keypad[position],


if __name__ == "__main__":
    main()
