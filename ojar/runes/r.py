#!/usr/bin/env python

# [r]andom rune

def info(_):
    from common import list_functions
    return "[r]andom rune\nactions: {}".format(list_functions(__name__))

def number(raw_string):
    from random import randint
    try:
        x, y = map(int, raw_string.split(','))
        if x > y: raise
    except:
        return "Invalid argument."
    return randint(x, y)

def string(raw_string):
    from random import choice, randint
    from string import ascii_lowercase
    if raw_string:
        return ''.join([choice(ascii_lowercase) for _ in range(int(raw_string))])
    else:
        return "Invalid argument."
