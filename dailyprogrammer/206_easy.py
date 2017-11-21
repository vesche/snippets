#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# dailyprogrammer 206 easy
# https://github.com/vesche
#


def main():
    mod = "*3 +2 *2".split()
    term = [0]
    terms = 7

    for i in range(terms):
        current = term[i]
        for j in mod:
            if j[0] == '+':
                current += int(j[1:])
            elif j[0] == '-':
                current -= int(j[1:])
            elif j[0] == '*':
                current *= int(j[1:])
            elif j[0] == '/':
                current /= int(j[1:])
        term.append(current)

    for i in term:
        print "Term", str(term.index(i)) + ":", i


if __name__ == "__main__":
    main()
