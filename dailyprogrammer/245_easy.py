#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###########################
# dailyprogrammer 245 easy
# https://github.com/vesche
###########################


def main():
    date = raw_input()

    try:
        a, b, c = date.split()
        if len(a) == 4:
            y, m, d = a, b, c
        else:
            y, m, d = c, a, b
    except ValueError:
        pass

    try:
        a, b, c = date.split('/')
        if len(a) == 4:
            y, m, d = a, b, c
        else:
            y, m, d = c, a, b
    except ValueError:
        pass

    try:
        a, b, c = date.split('-')
        if len(a) == 4:
            y, m, d = a, b, c
        else:
            y, m, d = c, b, a
    except ValueError:
        pass

    if len(y) > 3:
        y = y[2:]

    new_line = '20{0}-{1}-{2}'.format(y, m, d)
    print new_line


if __name__ == "__main__":
    main()
