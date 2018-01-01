#!/usr/bin/env python

import sys
import termios
import tty


def getchar():
    ''' Returns a single character from standard input. '''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    while True:
        ch = getchar()
        print('test: ' + ch)
        break

    if ch == 'q':
        sys.exit(0)

    elif ch == '\x1b[A':
        print('up')

    elif ch == '\x1b[B':
        print('down')

    elif ch == '\x1b[C':
        print('right')

    elif ch == '\x1b[D':
        print('left')


if __name__ == '__main__':
    while True: main()
