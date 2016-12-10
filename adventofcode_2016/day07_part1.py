#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################
# Advent of Code 2016, Day 07 - Part 1
# https://github.com/vesche
######################################

def abba(s):
    chunks = [s[i:i+4] for i in range(0, len(s)) if len(s[i:i+4]) == 4]
    for c in chunks:
        if (c[0] != c[1]) and (c[:2] == c[2:][::-1]):
            return True


def main():
    valid = 0

    with open("day07_input.txt") as f:
        for addr in f.read().splitlines():
            tls = False

            addr = addr.replace('[', ' ').replace(']', ' ').split()
            outside = addr[::2]
            hypernet = addr[1::2]

            for i in outside:
                if abba(i):
                    tls = True
            for i in hypernet:
                if abba(i):
                    tls = False

            if tls:
                valid += 1

    return valid


if __name__ == "__main__":
    print main()
