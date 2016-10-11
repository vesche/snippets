#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################
# dailyprogrammer 274 easy
# https://github.com/vesche
###########################


def main():
    with open('274_easy_input1.txt') as ciphertext, \
        open('274_easy_input2.txt') as declaration:
            declaration = declaration.read().split()
            for n in ciphertext.read().split(', '):
                print(declaration[int(n)-1][0], end='')


if __name__ == "__main__":
    main()
