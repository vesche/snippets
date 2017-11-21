#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
# 15-puzzle game
# https://github.com/vesche
#

import curses
from random import shuffle

WIDTH  = 12
HEIGHT = 4
MARK   = "   "


def main(stdscr):
    win = curses.newwin(HEIGHT, WIDTH, 0, 0)

    tiles  = ["{:>3}".format(_) for _ in range(1,16)] + [MARK]
    wtiles = tiles[:]
    shuffle(tiles)

    while True:
        # draw board
        for i in range(0, 16, 4):
            stdscr.addstr(i/4, 0, ''.join(tiles[i:i+4]), curses.A_BOLD)

        loc = tiles.index(MARK)
        y, x = loc/4, loc%4*3+2
        stdscr.addstr(y, x, '', curses.A_BOLD)

        c, m = stdscr.getch(), None
        if   c == curses.KEY_RIGHT and 3 <= x <= 11: m = -1
        elif c == curses.KEY_LEFT  and 0 <= x <= 8:  m =  1
        elif c == curses.KEY_UP    and 0 <= y <= 2:  m =  4
        elif c == curses.KEY_DOWN  and 1 <= y <= 3:  m = -4
        elif c == ord('q'): break

        if m: tiles[loc], tiles[loc+m] = tiles[loc+m], MARK
        if tiles == wtiles: break

        stdscr.refresh()


if __name__ == "__main__":
    # init curses
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)

    main(stdscr)

    # teardown curses
    stdscr.keypad(0)
    curses.nocbreak()
    curses.echo()
    curses.endwin()
