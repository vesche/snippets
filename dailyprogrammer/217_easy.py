#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# dailyprogrammer 217 easy
# https://github.com/vesche
#


def main():
    d, l, f = input(), input(), ''

    for _ in range(d):
        f += raw_input()

    f = map(int, f.split())

    for _ in range(l):
        f[f.index(min(f))] += 1

    for i in range(len(f)):
        if i % d == 0:
            print '\n',
        print f[i],


if __name__ == "__main__":
    main()
