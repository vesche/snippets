# -*- coding: utf-8 -*-

#
# ojar - [e]vil rune
# https://github.com/vesche/ojar
#


def gencc(n):
    try:
        n = int(n)
    except ValueError:
        return 'Invalid argument.'
    from random import choice
    cards = []
    for _ in range(n):
        card_numbs = ''.join(map(str, [choice(range(0, 9)) for _ in range(16)]))
        cards.append('-'.join([card_numbs[i:i+4] for i in range(0, \
        len(card_numbs), 4)]))
    return '\n'.join(cards)


def info(_):
    from runes.common import list_functions
    return '[e]vil rune\nactions: {}'.format(list_functions(__name__))
