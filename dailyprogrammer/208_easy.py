#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# dailyprogrammer 208 easy
# https://github.com/vesche
#


numbs = "3 1 3 4 4 1 4 5 2 1 4 4 4 4 1 4 3 2 5 5 2 2 2 4 2 4 4 4 4 1".split()


def main():
    for i in range(len(numbs)):
        try:
            if numbs[i] == numbs[i + 1]:
                pass
            else:
                print numbs[i],
        except IndexError:
            break


if __name__ == "__main__":
    main()
