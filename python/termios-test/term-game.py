#!/usr/bin/env python

import os
import sys
import termios
import tty


test_map = [' '] * 20
static_map = [' '] * 20


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def main():
    loc = 3
    inkey = _Getch()

    static_loc = 0

    while True:
        test_map[loc] = '@'
        static_map[static_loc] = '+'
        os.system('clear')

        print ''.join(test_map)
        print ''.join(static_map)

        if static_loc < 20:
            static_loc += 1

        while True:
            k = inkey()
            # if k != '': break
            break

        if k == '\x1b[C': # right
            test_map[loc] = ' '
            loc += 1
        elif k == '\x1b[D': # left
            test_map[loc] = ' '
            loc -= 1


if __name__=='__main__':
    main()
