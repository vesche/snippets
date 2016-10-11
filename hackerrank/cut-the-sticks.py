#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################################
# hackerrank, cut-the-sticks
# https://www.hackerrank.com/challenges/cut-the-sticks
# https://github.com/vesche
######################################################


def main():
    _, sticks = input(), map(int, raw_input().split())

    while len(sticks) != 0:
        print len(sticks)
        cut = min(sticks)
        for i in sticks:
            if i == cut:
                sticks = [x for x in sticks if x != cut]


if __name__ == "__main__":
    main()
