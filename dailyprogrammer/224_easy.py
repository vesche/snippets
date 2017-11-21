#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# dailyprogrammer 224 easy
# https://github.com/vesche
#

import random


def shuff(l):
    s = []
    while len(l) != 0:
        x = random.choice(l)
        s.append(x)
        l.remove(x)
    return ' '.join(s)


def main():
    print shuff(raw_input().split())


if __name__ == "__main__":
    main()
