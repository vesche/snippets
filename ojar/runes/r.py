# -*- coding: utf-8 -*-

#
# ojar - [r]andom rune
# https://github.com/vesche/ojar
#


def info(_):
    from runes.common import list_functions
    return '[r]andom rune\nactions: {}'.format(list_functions(__name__))


def number(raw_string):
    from random import randint
    try:
        x, y = map(int, raw_string.split(','))
        if x > y: raise
    except:
        return 'Invalid argument.'
    return randint(x, y)


def string(raw_string):
    from random import choice
    from string import ascii_lowercase
    try:
        n = int(raw_string)
    except:
        return 'Invalid argmuent.'
    return ''.join([choice(ascii_lowercase) for _ in range(n)])
