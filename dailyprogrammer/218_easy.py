#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###########################
# dailyprogrammer 218 easy
# https://github.com/vesche
###########################


def main():
    n, c = input(), 0
    print n,

    while n != int(str(n)[::-1]):
        n, c = n + int(str(n)[::-1]), c + 1

    print "gets palindromic after {} steps: {}".format(str(c), str(n))


if __name__ == "__main__":
    main()
