#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###########################
# dailyprogrammer 290 easy
# https://github.com/vesche
###########################

lower, upper = map(int, raw_input().split())

for n in range(lower, upper+1):
    ns = str(n**2)

    for i in range(1, len(ns)):
        a, b = int(ns[:i]), int(ns[i:])

        if a + b == n and a != 0 and b != 0:
            print n,
