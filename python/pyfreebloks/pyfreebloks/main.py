import os
import itertools

from blessed import Terminal
from functools import partial
from pieces import pieces
from grid import Grid

term = Terminal()
echo = partial(print, end='', flush=True)


def _modify_piece(piece, rotate=False, flip=False, n=5):
    tmp_piece = [list() for _ in range(n)]
    for i in range(len(piece)):
        if rotate:
            tmp_piece[i%n].append(piece[i])
        if flip:
            tmp_piece[i//n].append(piece[i])
    return list(itertools.chain(*[x[::-1] for x in tmp_piece]))


def flip_piece(piece):
    return _modify_piece(piece, flip=True)


def rotate_piece(piece):
    return _modify_piece(piece, rotate=True)


def main():
    print(term.enter_fullscreen())
    grid = Grid(15, 15)
    x, y = 0, 0

    # tmp
    from string import ascii_lowercase as letters
    c = 0
    rotate = 0
    tmp_piece = pieces[letters[c]]

    while True:
        print(term.clear())
        print(x, y)

        if rotate:
            tmp_piece = rotate_piece(tmp_piece)
            rotate = 0

        grid.array(x, y, tmp_piece)
        grid.display()

        with term.cbreak():
            user_input = term.inkey()
        if repr(user_input) == 'KEY_LEFT':
            x -= 1
        if repr(user_input) == 'KEY_DOWN':
            y += 1
        if repr(user_input) == 'KEY_RIGHT':
            x += 1
        if repr(user_input) == 'KEY_UP':
            y -= 1
        if repr(user_input) == 'KEY_ENTER':
            rotate = 1 - rotate
        if repr(user_input) == 'KEY_DELETE':
            c += 1
            tmp_piece = pieces[letters[c]]
        x, y = max(0, x), max(0, y)
        x, y = min(10, x), min(10, y)


if __name__ == '__main__':
    main()
