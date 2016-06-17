#!/usr/bin/env python

# [e]vil rune

def gencc(n):
    from random import choice
    cards = []
    for _ in range(int(string)):
        card_numbs = ''.join(map(str, [choice(range(0, 9)) for _ in range(16)]))
        cards.append('-'.join([card_numbs[i:i+4] for i in range(0, \
        len(card_numbs), 4)]))
    return '\n'.join(cards)

def info(_):
    from common import list_functions
    return "[e]vil rune\nactions: {}".format(list_functions(__name__))
