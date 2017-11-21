#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code, Day 07 - Part 1 & 2
# https://github.com/vesche
#

import os
import shutil


signals = {}


def parse(i, f):
    line = i.split()

    if line[1] == "->":
        try:
            a = int(line[0])
        except ValueError:
            pass
        try:
            a = signals[line[0]]
        except KeyError:
            pass
        try:
            signals[line[2]] = a
        except UnboundLocalError:
            f.write(i + '\n')

    elif line[0] == "NOT":
        try:
            a = abs(~int(line[1]))
        except ValueError:
            pass
        try:
            a = abs(~signals[line[1]])
        except KeyError:
            pass
        try:
            signals[line[3]] = 65536 - a
        except UnboundLocalError:
            f.write(i + '\n')

    else:
        try:
            a = int(line[0])
        except ValueError:
            pass
        try:
            a = signals[line[0]]
        except KeyError:
            pass
        try:
            b = int(line[2])
        except ValueError:
            pass
        try:
            b = signals[line[2]]
        except KeyError:
            pass
        try:
            if line[1] == "AND":
                signals[line[4]] = a & b
            elif line[1] == "OR":
                signals[line[4]] = a | b
            elif line[1] == "LSHIFT":
                signals[line[4]] = a << b
            elif line[1] == "RSHIFT":
                signals[line[4]] = a >> b
        except UnboundLocalError:
            f.write(i + '\n')


def main():
    shutil.copy("day07_input.txt", "tmp.txt")

    while True:
        instructions = open("tmp.txt", 'r').read().splitlines()
        if not instructions:
            break
        with open("tmp.txt", 'w') as f:
            for i in instructions:
                parse(i, f)

    for s in sorted(signals):
        if s == 'a':
            print signals[s]

    os.remove("tmp.txt")


if __name__ == "__main__":
    main()
