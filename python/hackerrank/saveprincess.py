#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# hackerrank, saveprincess
# https://github.com/vesche
#


def main():
    n = input()
    for i in range(n):
        line = raw_input()
        if 'p' in line:
            a = line.index('p')
            break

    if (i != 0):
        out = "DOWN"
    else:
        out = "UP"

    if (a != 0):
        out += "\nRIGHT"
    else:
        out += "\nLEFT"

    print '\n'.join(out for _ in range(n-2))


if __name__ == "__main__":
    main()
