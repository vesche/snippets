#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###########################
# dailyprogrammer 290 easy
# https://github.com/vesche
###########################

lower, upper = map(int, raw_input().split())

for n in range(lower, upper+1):
    ns = str(n**2)
    for i in range(len(ns)):
        try:
            a, b = int(ns[:i]), int(ns[i:])
        except ValueError:
            continue

        if a == 0 or b == 0:
            continue
        if a + b == n:
            print n,
            continue
