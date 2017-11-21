#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code, Day 02 - Part 2
# https://github.com/vesche
#


def main():
    total = 0

    with open("day02_input.txt", 'r') as f:
        for present in f.read().splitlines():
            dim = [l, w, h] = map(int, present.split('x'))
            ribbon = 2*sorted(dim)[0] + 2*sorted(dim)[1]
            bow = l*w*h
            present_total = ribbon + bow
            total += present_total

    print total


if __name__ == "__main__":
    main()
