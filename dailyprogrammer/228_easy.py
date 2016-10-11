#!/usr/bin/env python2
# -*- coding: utf-8 -*-

###########################
# dailyprogrammer 228 easy
# https://github.com/vesche
###########################

from string import ascii_lowercase as letters


def sauce(word):
    order = []

    for i in word:
        order.append(letters.index(i))

    if order == sorted(order, key=int):
        return "IN ORDER"
    if order == sorted(order, key=int, reverse=True):
    	return "REVERSE ORDER"
    else:
        return "NOT IN ORDER"


def main():
    f = open('input.txt')

    for word in f.read().splitlines():
        print word, sauce(word.upper())


if __name__ == "__main__":
    main()
