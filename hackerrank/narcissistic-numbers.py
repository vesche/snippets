#!/usr/bin/env python2
# -*- coding: utf-8 -*-

######################################################
# hackerrank, narcissistic-numbers
# https://github.com/vesche
######################################################


def narc_test(n):
    digits = map(int, list(str(n)))
    if n == sum([i**len(digits) for i in digits]):
        print n,


def main():
    for n in range(1000000):
        narc_test(n)


if __name__ == "__main__":
    main()
