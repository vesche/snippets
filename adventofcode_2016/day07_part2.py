#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Advent of Code 2016, Day 07 - Part 2
# https://github.com/vesche
######################################

def chunks(s):
    return [s[i:i+3] for i in range(0, len(s)) if len(s[i:i+3]) == 3]


def main():
    valid = 0

    with open("day07_input.txt") as f:
        for addr in f.read().splitlines():
            ssl = False

            addr = addr.replace('[', ' ').replace(']', ' ').split()
            outside = addr[::2]
            hypernet = addr[1::2]

            outside_chunks = []
            hypernet_chunks = []
            for i in outside:
                outside_chunks += chunks(i)
            for i in hypernet:
                hypernet_chunks += chunks(i)

            for i in outside_chunks:
                if i[0] == i[-1]:
                    bab = i[1] + i[0] + i[1]
                    if bab in hypernet_chunks:
                        ssl = True; break

            if ssl:
                valid += 1

    return valid


if __name__ == "__main__":
    print main()
