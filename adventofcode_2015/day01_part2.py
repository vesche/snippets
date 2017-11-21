#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code, Day 01 - Part 2
# https://github.com/vesche
#


def main():
    final_floor = 0
    moves = 0

    with open("day01_input.txt", 'r') as f:
        for floor in f.read():
            if floor == '(':
                final_floor += 1
            elif floor == ')':
                final_floor -= 1

            moves += 1
            if final_floor == -1:
                print moves


if __name__ == "__main__":
    main()
