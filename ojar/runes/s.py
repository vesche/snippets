# -*- coding: utf-8 -*-

#
# ojar - [s]tring rune
# https://github.com/vesche/ojar
#


def info(_):
    from runes.common import list_functions
    return '[s]tring rune\nactions: {}'.format(list_functions(__name__))


def length(string):
    return len(string)
