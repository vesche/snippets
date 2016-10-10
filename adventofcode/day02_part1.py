#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#################################
# Advent of Code, Day 02 - Part 1
# https://github.com/vesche
#################################


def main():
    total = 0

    with open("day02_input.txt", 'r') as f:
        for present in f.read().splitlines():
            dim = [l, w, h] = map(int, present.split('x'))
            surface_area = 2*l*w + 2*w*h + 2*h*l
            smallest_side = sorted(dim)[0] * sorted(dim)[1]
            present_total = surface_area + smallest_side
            total += present_total

    print total


if __name__ == "__main__":
    main()
