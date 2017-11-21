#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# ringtext
# https://github.com/vesche
#

import readline
from os import system
from ringmaps import ringtext


playing = True

ring =  "+---------------+\n" \
        "| RingText v0.1 |\n" \
        "+---------------+\n" \
        "|      ...      |\n" \
        "|      ...      |\n" \
        "|   .........   |\n" \
        "|   ...   ...   |\n" \
        "|......   ......|\n" \
        "|...    .    ...|\n" \
        "|......   ......|\n" \
        "|   ...   ...   |\n" \
        "|   .........   |\n" \
        "|      ...      |\n" \
        "|      ...      |\n" \
        "+---------------+"   \
        "---------------+"

ring = [[tile for tile in line] for line in ring.split('\n')]


def print_map(x, y):
    ring[y][x] = '@'
    print '\n'.join([''.join(line) for line in ring])
    return


def main():
    x, y = 8, 4

    while playing:
        system("clear")

        print_map(x, y)

        print ringtext(x, y)
        move = raw_input("> ").lower()

        ring[y][x] = '.'

        if move == 'n' and ring[y-1][x] == '.':
            y -= 1
        elif move == 's' and ring[y+1][x] == '.':
            y += 1
        elif move == 'e' and ring[y][x+1] == '.':
            x += 1
        elif move == 'w' and ring[y][x-1] == '.':
            x -= 1


if __name__ == "__main__":
    main()
