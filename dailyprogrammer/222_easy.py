#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# dailyprogrammer 222 easy
# https://github.com/vesche
#


letters = ' abcdefghijklmnopqrstuvwxyz'


def justdoit(word):
    word = word.lower()

    for i in range(len(word)):
        upper = word[:i+1][::-1]
        lower = word[i+2:]

        u_total, l_total = 0, 0
        for x in range(len(upper)):
            u_total += (x+1)*(letters.index(upper[x]))
        for y in range(len(lower)):
            l_total += (y+1)*(letters.index(lower[y]))
        if u_total == l_total:
            break

    try:
        output = "{} {} {} - {}".format(upper.upper()[::-1], \
            word[i+1].upper(), lower.upper(), u_total)
    except IndexError:
        output = "{} DOES NOT BALANCE".format(word.upper())

    return output


def main():
    print justdoit("CONSUBSTANTIATION")
    print justdoit("WRONGHEADED")
    print justdoit("UNINTELLIGIBILITY")
    print justdoit("SUPERGLUE")


if __name__ == "__main__":
    main()
