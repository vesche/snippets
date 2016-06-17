#!/usr/bin/env python

# [e]vil rune

def gencc(string):
    from random import choice
    cards = []
    for _ in range(int(string)):
        card_numbs = ''.join(map(str, [choice(range(0, 9)) for _ in range(16)]))
        cards.append('-'.join([card_numbs[i:i+4] for i in range(0, len(card_numbs), 4)]))
    return '\n'.join(cards)

def info(_):
    help_text  = "[e]vil rune\n"
    help_text += "actions: gencc"
    return help_text
