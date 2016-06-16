#!/usr/bin/env python

# ? rune

def info(_):
    help_text  = "[r]andom rune\n"
    help_text += "actions: integer, string"
    return help_text

def integer(string):
    from random import randint
    x, y = string.split(',')
    return randint(int(x), int(y))

def string(string):
    from random import choice, randint
    from string import ascii_lowercase
    return ''.join([choice(ascii_lowercase) for _ in range(int(string))])