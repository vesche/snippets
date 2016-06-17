#!/usr/bin/env python

# [r]andom rune

def info(_):
    help_text  = "[r]andom rune\n"
    help_text += "actions: number, string"
    return help_text

def number(string):
    from random import randint
    x, y = string.split(',')
    return randint(int(x), int(y))

def string(string):
    from random import choice, randint
    from string import ascii_lowercase
    return ''.join([choice(ascii_lowercase) for _ in range(int(string))])