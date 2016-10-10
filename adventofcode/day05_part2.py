#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#################################
# Advent of Code, Day 05 - Part 2
# https://github.com/vesche
#################################


def main():
    nice_count = 0

    with open("day05_input.txt", 'r') as f:
        for s in f.read().splitlines():
            nice = True
            pair_count = 0
            for i in range(len(s) - 3):
                pair = s[i:i+2]
                if pair in s[i+2:]:
                    pair_count += 1
            if pair_count == 0:
                nice = False

            lxl_count = 0
            for i in range(len(s) - 2):
                if s[i] == s[i + 2]:
                    lxl_count += 1
            if lxl_count == 0:
                nice = False

            if nice:
                nice_count += 1

    print nice_count


if __name__ == "__main__":
    main()
