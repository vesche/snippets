#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# dailyprogrammer 270 easy
# https://github.com/vesche
#


def main():
    data = open('270_easy_input.txt').read().splitlines()

    for i in range(len(max(data, key=len))):
        for j in data:
            try:
                print(j[i], end='')
            except:
                print(' ', end='')
        print()


if __name__ == "__main__":
    main()
