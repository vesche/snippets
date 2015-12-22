#!/usr/bin/env python2
import os
import time

x, l, o = '_', '|', ' '
zer = [x, l, o, l, l, x, l]
one = [o, o, o, l, o, o, l]
two = [x, o, x, l, l, x, o]
thr = [x, o, x, l, o, x, l]
fou = [o, l, x, l, o, o, l]
fiv = [x, l, x, o, o, x, l]
six = [x, l, x, o, l, x, l]
sev = [x, o, o, l, o, o, l]
eig = [x, l, x, l, l, x, l]
nin = [x, l, x, l, o, o, l]
nul = [o, o, o, o, o, o, o]

def get_pattern(n):
    if n == '0': return zer
    if n == '1': return one
    if n == '2': return two
    if n == '3': return thr
    if n == '4': return fou
    if n == '5': return fiv
    if n == '6': return six
    if n == '7': return sev
    if n == '8': return eig
    if n == '9': return nin
    else: return nul

def display(stdin):
    top, mid, bot = '', '', ''

    for c in stdin:
        p = get_pattern(c)
        top += " {0} ".format(p[0])
        mid += "{0}{1}{2}".format(p[1], p[2], p[3])
        bot += "{0}{1}{2}".format(p[4], p[5], p[6])

    return '\n'.join([top, mid, bot])