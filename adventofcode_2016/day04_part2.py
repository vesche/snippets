#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# Advent of Code 2016, Day 04 - Part 2
# https://github.com/vesche
#

from collections import Counter
from string import ascii_lowercase


def decrypt_rotn(enc_data, n):
    dec = ''
    n %= 26
    for i in enc_data.lower():
        try:
            offset = n + ascii_lowercase.index(i)
            if offset >= 25:
                offset -= 26
            char = ascii_lowercase[offset]
        except ValueError:
            char = i
        dec += char
    return dec


def main():
    with open("day04_input.txt") as f:
        data = f.read().splitlines()

    for line in data:
        line = line.split('-')

        name = ''.join(line[:-1])
        sector = int(line[-1][:3])
        checksum = line[-1][4:9]

        top5 = ''.join([i for i, _ in sorted(Counter(name).most_common(10),
        key=lambda tup: (-tup[1], tup[0]))])[:5]

        if checksum == top5:
            print sector, decrypt_rotn(' '.join(line[:-1]), sector)


if __name__ == "__main__":
    main()
